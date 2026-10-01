===== TRIAGE 2026-10-01 13:36:00 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/*.md"[90m 20 matches[0m
[0m✱ [0mGlob "**/scope.yml"[90m 1 match[0m
[0m→ [0mRead scope.yml
[0m→ [0mRead probe-results.md
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead leads/reposcan-latest.md
Now I have all the data. Let me evaluate each distinct vulnerability lead against the 7-Question Gate.

---

## LEAD 1: npm `gladia@0.1.3` impersonation/typosquat (Supply Chain)

**Q1 Scope**: YES — npm packages `@gladiaio/sdk` and `gladia` are in scope.yml (Medium priority)
**Q2 Attacker reach**: YES — Public npm registry, anyone can install
**Q3 Real impact**: YES — Developers install thinking it's official; package embeds raw API keys in WebSocket URLs (`searchParams.append('x-gladia-key', apiKey)`); repo+user `alexisbouchez` 404 = orphaned/irrevocable takeover risk
**Q4 Passive proof**: YES — `npm view gladia@0.1.3` metadata + tarball inspection + GitHub API 404 all confirmed passively
**Q5 Novel**: YES — Not previously reported to Gladia (human report filed 2026-08-12, awaiting response)
**Q6 Not rejected**: YES — Not on always-rejected list (supply-chain impersonation + credential hygiene hazard)
**Q7 Triager accept**: YES — Clear impersonation + key leakage in URL query string

**VERDICT: VALID**
- **Minimal proof**: `npm view gladia@0.1.3 description repository.url maintainer` + tarball `src/client.ts:306-308` showing `searchParams.append('x-gladia-key', apiKey)` → `wss://api.gladia.io/v2/live?x-gladia-key=<KEY>`
- **Impact**: Supply-chain API key harvesting + irrevocable account takeover risk (P3/P4)
- **CVSS 3.1**: 7.1 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N) — network, low complexity, no auth, user interaction (install), high confidentiality
- **Channel**: Gladia security channel per scope.yml (https://gladia.io/bug-bounty-report → Google Forms) + npm Trust & Safety

---

## LEAD 2: SSRF via `audio_url`/`video_url`/`callback_url` on `api.gladia.io/v2/pre-recorded`

**Q1 Scope**: YES — `api.gladia.io` is Highest priority in scope.yml
**Q2 Attacker reach**: PARTIAL — Requires valid `x-gladia-key` (key-gated). Unauthenticated = 401. Low-priv = valid key holder.
**Q3 Real impact**: YES — Spec confirms `audio_url`/`video_url`/`callback_config.url` as `format:uri` with NO scheme allowlist; `/v1/models` reveals FR/US datacenter egress; 7 webhook paths; server-side fetch by design
**Q4 Passive proof**: NO — Requires valid API key to test (`AUTH_HELPED`). Passive probes only show 401.
**Q5 Novel**: YES — Confirmed by spec+RAG across 100+ cycles, no bypass found
**Q6 Not rejected**: YES — SSRF-to-cloud-metadata is HIGH-VALUE class per directives
**Q7 Triager accept**: CONDITIONAL — Would accept IF valid key provided and POC demonstrates internal reachability

**VERDICT: HOLD** — "Requires valid x-gladia-key for POC; surface frozen 100+ cycles, key-gated only. Cannot prove without AUTH_HELPED test. Submit only if program provides test key."

---

## LEAD 3: Post-auth open redirect via `redirect_to` on `app.gladia.io/signin`

**Q1 Scope**: YES — `app.gladia.io` is High priority in scope.yml
**Q2 Attacker reach**: PARTIAL — Unauthenticated reflection confirmed (form action reflects URL-encoded value). Post-auth behavior requires authenticated session (HUMAN_ONLY).
**Q3 Real impact**: CONDITIONAL — If server honors `redirect_to` after Google OAuth, enables phishing. OAuth `redirect_uri` is FIXED (PKCE S256) — no code/state theft. CSP has 0 `form-action` directives (gap).
**Q4 Passive proof**: PARTIAL — Reflection confirmed passively (100+ cycles). Post-auth redirect UNVERIFIED (needs live session).
**Q5 Novel**: YES — Not previously reported
**Q6 Not rejected**: YES — Open redirect on auth flow is HIGH-VALUE class
**Q7 Triager accept**: CONDITIONAL — Would accept IF post-auth redirect to external host demonstrated

**VERDICT: HOLD** — "Post-auth honoring sole unverified gate (HUMAN_ONLY). Reflection confirmed byte-fresh; OAuth redirect_uri FIXED prevents escalation. Needs authenticated session test."

---

## LEAD 4: Undocumented `/health` endpoint on `api.gladia.io`

**Q1 Scope**: YES — `api.gladia.io` Highest priority
**Q2 Attacker reach**: YES — Public, unauthenticated (GET → 200 `{"health":"OK"}`)
**Q3 Real impact**: NO — Returns only `{"health":"OK"}` (15 bytes). No version, build info, metadata. `/health?full=true` returns identical output. Probe results confirm static response.
**Q4 Passive proof**: YES — Confirmed via GET probes
**Q5 Novel**: YES — Not in OpenAPI spec
**Q6 Not rejected**: NO — **FAILS Q3/Q6**: Info disclosure of trivial public data (health check OK). Always-rejected per policy.
**Q7 Triager accept**: NO — No security impact beyond "service is up"

**VERDICT: INVALID** — "Info disclosure of trivial health status only; no version/build/metadata leakage; `/health?full=true` identical to base; always-rejected class"

---

## LEAD 5: WebSocket auth token in URL query parameter (`wss://api.gladia.io/v2/live?token=<uuid>`)

**Q1 Scope**: YES — `api.gladia.io` Highest priority
**Q2 Attacker reach**: PARTIAL — Token issued via POST `/v2/live` (key-gated). Token in URL leaks via Referer, browser history, proxy logs, server logs.
**Q3 Real impact**: YES — Bearer-equivalent token for live transcription sessions; token theft → unauthorized live audio access
**Q4 Passive proof**: NO — Token format confirmed via OpenAPI spec, but token issuance/rotation/invalidation requires valid key (`AUTH_HELPED`)
**Q5 Novel**: YES — Design per spec
**Q6 Not rejected**: YES — Auth token in URL is HIGH-VALUE class
**Q7 Triager accept**: CONDITIONAL — Would accept IF token proven long-lived/session-scoped and Referrer-Policy absent on WS upgrade

**VERDICT: HOLD** — "Spec confirms token-in-URL design; needs AUTH_HELPED to confirm token lifetime, rotation, Referrer-Policy on WS handshake. High impact if proven."

---

## LEAD 6: CORS wildcard + `x-powered-by: Express` on CORS preflight only

**Q1 Scope**: YES — `api.gladia.io` Highest priority
**Q2 Attacker reach**: YES — Public, unauthenticated
**Q3 Real impact**: LOW — CORS `access-control-allow-origin: *` static (no origin reflection). No `access-control-allow-credentials`. `x-powered-by: Express` only on OPTIONS preflight (not GET). Framework fingerprinting only.
**Q4 Passive proof**: YES — Confirmed via OPTIONS/GET probes (100+ cycles)
**Q5 Novel**: NO — Known misconfiguration class
**Q6 Not rejected**: NO — **FAILS Q3/Q6**: Framework fingerprinting alone is Low severity info disclosure; CORS wildcard without credentials is standard misconfig not exploitable for cross-origin reads of authenticated endpoints
**Q7 Triager accept**: NO — Low-value reconnaissance aid only

**VERDICT: INVALID** — "CORS * static (no origin echo), no credentials allowed; x-powered-by only on preflight; reconnaissance-only, no exploitable impact"

---

## LEAD 7: IDOR on transcription file download endpoints (`/{id}/file`)

**Q1 Scope**: YES — `api.gladia.io` Highest priority
**Q2 Attacker reach**: NO — Key-gated (401 without key). Requires valid key + valid ID owned by another user.
**Q3 Real impact**: HIGH IF TRUE — Cross-tenant transcription data (PII, audio)
**Q4 Passive proof**: NO — Requires AUTH_HELPED with two valid keys
**Q5 Novel**: UNKNOWN — Spec defines endpoints but ownership model opaque
**Q6 Not rejected**: YES — IDOR/BOLA is HIGH-VALUE class
**Q7 Triager accept**: CONDITIONAL — Would accept IF cross-account access demonstrated with valid keys

**VERDICT: HOLD** — "Parked at confidence 50; spec shows 3 file download endpoints but ownership binding unknown. Needs two valid API keys to test cross-account access. Cannot verify passively."

---

## SUMMARY

| Lead | Verdict | Key Reason |
|------|---------|------------|
| npm `gladia@0.1.3` impersonation | **VALID** | Proven supply-chain impersonation + API key in WS URL |
| SSRF via `audio_url`/`callback_url` | **HOLD** | Key-gated; needs valid key for POC |
| Post-auth open redirect `redirect_to` | **HOLD** | Post-auth behavior unverified (HUMAN_ONLY) |
| Undocumented `/health` | **INVALID** | Trivial info disclosure only |
| WS token in URL query | **HOLD** | Needs AUTH_HELPED to confirm token lifetime/rotation |
| CORS wildcard + Express fingerprint | **INVALID** | Recon only; no creds; static * |
| IDOR on `/{id}/file` | **HOLD** | Needs two valid keys; parked |

---

**REPORT-READY NOW**: Only **Lead 1 (npm impersonation)** is fully validated and reportable via passive evidence alone. The human report was already submitted 2026-08-12 via `security@gladia.io` (10 days ago, no response). Per `lead-human.md`, follow-up due 2026-08-26.

**NEXT PROBES NEEDED** (require program cooperation):
1. `[NEXT] PROBE: POST https://api.gladia.io/v2/pre-recorded -H "x-gladia-key: <VALID_KEY>" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/"}'` — for SSRF POC
2. `[NEXT] PROBE: Complete Google OAuth on app.gladia.io with ?redirect_to=https://evil.example.com` — for post-auth redirect
3. `[NEXT] PROBE: POST https://api.gladia.io/v2/live -H "x-gladia-key: <VALID_KEY>"` → observe WS token format, then connect and check Referrer-Policy — for WS token leakage
