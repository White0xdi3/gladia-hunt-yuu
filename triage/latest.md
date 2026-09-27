===== TRIAGE 2026-09-27 08:23:51 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/*"[90m 49 matches[0m
[0m→ [0mRead scope.yml
[0m→ [0mRead probe-results.txt
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead triage/latest.md
[0m→ [0mRead leads/reposcan-latest.md
Now I have a comprehensive view of all leads. Let me validate each distinct lead against the 7-Question Gate.

---

## LEAD 1: SSRF via audio_url/video_url/callback_url server-side fetch (api.gladia.io)

**Q1 Scope**: YES — api.gladia.io is Highest priority in scope.yml
**Q2 Reachable**: NO — requires valid `x-gladia-key` (AUTH_HELPED); no public/unauthenticated access
**Q3 Impact**: YES — Cloud metadata (169.254.169.254), internal network read, callback SSRF → HIGH
**Q4 Provable passively**: NO — needs authenticated POST with malicious payloads
**Q5 Novel**: YES — not yet reported; confirmed by spec+RAG (format:uri, no scheme allowlist, 7 webhook paths, FR/US egress)
**Q6 Not rejected**: YES — genuine SSRF class, not info-disclosure/best-practice
**Q7 Triager accept**: CONDITIONAL — would accept **if** proven with valid key; currently unproven

**VERDICT**: **HOLD** — High-value target but gate Q2/Q4 fail without program-provided key. Minimal proof: `POST /v2/pre-recorded -H "x-gladia-key: <KEY>" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/","callback_config":{"url":"http://169.254.169.254:80/"}}'` → compare error_code/status/timing vs benign URL. CVSS 3.1: 7.5 (AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N) if proven. Channel: Gladia bug bounty form (security@gladia.io per scope).

---

## LEAD 2: npm `gladia@0.1.3` orphaned impersonation + raw API key in WebSocket URL

**Q1 Scope**: YES — `gladia` (unscoped) explicitly listed in scope.yml npm_packages
**Q2 Reachable**: YES — public on npm registry, installable by any developer
**Q3 Impact**: YES — Supply chain: "Official" claim vs README "Unofficial"; orphaned repo (alexisbouchez 404); src/client.ts:306-308 embeds raw `x-gladia-key` in `wss://api.gladia.io/v2/live?x-gladia-key=<KEY>` → keys leak to proxy/access logs/browser history → MEDIUM-HIGH
**Q4 Provable passively**: YES — `npm view gladia@0.1.3`, tarball inspection, GitHub API 404 on user+repo, source code review all passive
**Q5 Novel**: NO — **ALREADY REPORTED** 2026-08-12 by human (lead-human.md) to security@gladia.io via bug bounty form; awaiting vendor response
**Q6 Not rejected**: YES — supply-chain impersonation + credential hygiene flaw
**Q7 Triager accept**: YES — human already validated and submitted

**VERDICT**: **VALID** (but **DUPLICATE** — already reported). Minimal proof: registry metadata (description="Official", maintainer=softwarecitadel@gmail.com, repo=alexisbouchez/gladia.ts 404), tarball src/client.ts line 307 `searchParams.append('x-gladia-key', this.apiKey)`. CVSS 3.1: 6.5 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:N). Channel: Gladia bug bounty form + npm Trust & Safety.

---

## LEAD 3: Post-auth open redirect via `redirect_to` parameter (app.gladia.io)

**Q1 Scope**: YES — app.gladia.io is High priority
**Q2 Reachable**: PARTIAL — reflection confirmed unauthenticated (GET `/signin?redirect_to=https://evil.example.com` → form action reflects URL), but **exploitation requires authenticated Google OAuth session**
**Q3 Impact**: YES — post-auth redirect to attacker domain → phishing, potential OAuth state theft if `redirect_to` reused as `redirect_uri` → LOW-MEDIUM
**Q4 Provable passively**: NO — post-auth behavior **HUMAN_ONLY** (needs live Google SSO session)
**Q5 Novel**: YES — not yet proven; reflection confirmed 100+ cycles, OAuth `redirect_uri` FIXED (PKCE S256), CSP lacks `form-action`
**Q6 Not rejected**: YES — open redirect not on rejected list
**Q7 Triager accept**: CONDITIONAL — would accept **if** post-auth honoring proven; currently unproven

**VERDICT**: **HOLD** — Reflection confirmed, but Q2/Q4 fail for exploitation without authenticated session. Minimal proof: complete Google OAuth with `?redirect_to=https://evil.example.com`, capture final 302 Location. CVSS 3.1: 4.3 (AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:N/A:N) if proven. Channel: Gladia bug bounty form.

---

## LEAD 4: WebSocket auth token in URL query parameter (api.gladia.io)

**Q1 Scope**: YES — api.gladia.io Highest
**Q2 Reachable**: PARTIAL — token issued via `POST /v2/live` (requires `x-gladia-key`), then `wss://api.gladia.io/v2/live?token=<uuid>` — token in URL leaks via Referer, proxy logs, browser history
**Q3 Impact**: YES — bearer-equivalent token for live transcription sessions → audio stream access → HIGH
**Q4 Provable passively**: NO — needs valid key to initiate session and observe token format/behavior (AUTH_HELPED)
**Q5 Novel**: YES — design flaw confirmed by OpenAPI spec (`InitStreamingResponse.url` contains token query param)
**Q6 Not rejected**: YES — credential-in-URL is recognized auth hygiene flaw
**Q7 Triager accept**: CONDITIONAL — would accept if token longevity/reuse proven; currently speculative

**VERDICT**: **HOLD** — Design flaw confirmed by spec, but Q2/Q4 require valid key to prove exploitability. Minimal proof: `POST /v2/live -H "x-gladia-key: <KEY>"` → observe response `url` with `token=<uuid>`; initiate WS, check Referer header on upgrade; test token reuse after disconnect. CVSS 3.1: 7.1 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) if token is long-lived. Channel: Gladia bug bounty form.

---

## LEAD 5: Undocumented `/health` endpoint (api.gladia.io)

**Q1 Scope**: YES — api.gladia.io Highest
**Q2 Reachable**: YES — public GET `/health` returns 200 `{"health":"OK"}`
**Q3 Impact**: NO — only returns `{"health":"OK"}`; no version, build info, dependency status; `/health?full=true` and `/health?format=json` return identical output (probed)
**Q4 Provable passively**: YES — GET `/health`, `/health?full=true`, `/health?format=json` all return same minimal JSON
**Q5 Novel**: YES — not in OpenAPI spec (14 documented paths)
**Q6 Not rejected**: **FAILS** — information disclosure of trivial public data ("OK") is on always-rejected list
**Q7 Triager accept**: NO — reasonable triager would reject as low-value misconfig

**VERDICT**: **INVALID** — Q3/Q6 fail. No sensitive data exposed; undocumented health endpoint returning only "OK" is not a vulnerability.

---

## LEAD 6: Tech stack disclosure via `x-powered-by: Express` on CORS preflight only (api.gladia.io)

**Q1 Scope**: YES — api.gladia.io Highest
**Q2 Reachable**: YES — OPTIONS preflight returns `x-powered-by: Express`; absent on GET
**Q3 Impact**: NO — framework fingerprinting only; aids reconnaissance but no direct exploit; LOW
**Q4 Provable passively**: YES — `curl -X OPTIONS -H "Origin: https://evil.test" ...` vs GET comparison
**Q5 Novel**: YES — confirmed preflight-only differential
**Q6 Not rejected**: **FAILS** — framework fingerprinting via header is widely considered best-practice/low-severity info disclosure, often not rewarded
**Q7 Triager accept**: UNLIKELY — most programs treat this as informational only

**VERDICT**: **INVALID** — Q3/Q6 fail. Low-severity fingerprinting, not a vulnerability.

---

## LEAD 7: IDOR on transcription file download endpoints `/{id}/file` (api.gladia.io)

**Q1 Scope**: YES — api.gladia.io Highest
**Q2 Reachable**: NO — requires valid `x-gladia-key` + valid transcription ID owned by another user (AUTH_HELPED)
**Q3 Impact**: YES — cross-tenant transcription data (PII, audio) → HIGH
**Q4 Provable passively**: NO — needs two valid keys/accounts to test cross-account access
**Q5 Novel**: YES — hypothesis only, spec shows 3 endpoints (`/v2/transcription/{id}/file`, `/v2/pre-recorded/{id}/file`, `/v2/live/{id}/file`), ownership binding opaque
**Q6 Not rejected**: YES — genuine IDOR class
**Q7 Triager accept**: CONDITIONAL — would accept if proven with two accounts; currently untestable

**VERDICT**: **HOLD** — High impact if proven, but Q2/Q4 require two valid API keys. Minimal proof: with two accounts (A, B), A creates transcription → gets ID; B uses own key to `GET /v2/transcription/{A_id}/file` → 200 = IDOR. CVSS 3.1: 8.1 (AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N). Channel: Gladia bug bounty form.

---

## LEAD 8: Query-param parsing injection on `/v1/history` (api.gladia.io)

**Q1 Scope**: YES — api.gladia.io Highest
**Q2 Reachable**: NO — requires valid `x-gladia-key` (key-gated, 401 without)
**Q3 Impact**: LOW-MEDIUM — filter bypass/prototype pollution on **own-tenant** query only; no cross-tenant impact
**Q4 Provable passively**: NO — needs authenticated GET with injection payloads (AUTH_HELPED)
**Q5 Novel**: YES — `custom_metadata` as object (additionalProperties:true) + `status`/`kind` as arrays in query string; NestJS deep-parse footgun
**Q6 Not rejected**: YES — not on rejected list
**Q7 Triager accept**: UNLIKELY — low impact (self-tenant only), key-gated, requires proof of 500/altered results

**VERDICT**: **HOLD** — Low impact, key-gated, unproven. Minimal proof: `GET /v1/history?custom_metadata[__proto__][x]=1` with valid key → observe 500 vs baseline. CVSS 3.1: 3.1 (AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N) if prototype pollution. Channel: Gladia bug bounty form.

---

## LEAD 9: CORS wildcard reflects arbitrary origin (api.gladia.io) — **REJECTED BY PROBES**

**Q1 Scope**: YES
**Q2 Reachable**: YES
**Q3 Impact**: NO — probes confirm static `access-control-allow-origin: *` (no Origin reflection), no `access-control-allow-credentials`; only public endpoints readable cross-origin
**Q4 Provable passively**: YES — confirmed by probes
**Q5 Novel**: N/A — hypothesis disproven
**Q6 Not rejected**: **FAILS** — wildcard without credentials is standard misconfig, not exploitable
**Q7 Triager accept**: NO

**VERDICT**: **INVALID** — Disproven by passive probes (static `*`, no origin reflection, no credentials).

---

## LEAD 10: return-to cookie JWT parsing without signature (app.gladia.io) — **REJECTED BY PROBES**

**Q1 Scope**: YES
**Q2 Reachable**: YES
**Q3 Impact**: NO — server rejects tampered cookie and resets to default `{"url":"/"}`; no open redirect
**Q4 Provable passively**: YES — confirmed by tampering test
**Q5 Novel**: N/A — hypothesis disproven
**Q6 Not rejected**: N/A
**Q7 Triager accept**: NO

**VERDICT**: **INVALID** — Disproven; server validates/resets cookie.

---

## SUMMARY

| Lead | Verdict | Reason |
|------|---------|--------|
| SSRF via audio_url/video_url/callback_url | **HOLD** | High value, needs valid API key (AUTH_HELPED) |
| npm gladia@0.1.3 impersonation + key leak | **VALID (DUPLICATE)** | Already reported 2026-08-12, awaiting vendor response |
| Post-auth open redirect (redirect_to) | **HOLD** | Reflection confirmed, needs authenticated session (HUMAN_ONLY) |
| WS token in URL query param | **HOLD** | Design flaw confirmed, needs valid key (AUTH_HELPED) |
| Undocumented /health endpoint | **INVALID** | Only returns `{"health":"OK"}` — rejected list |
| x-powered-by on preflight | **INVALID** | Low-severity fingerprinting, best-practice only |
| IDOR on /{id}/file endpoints | **HOLD** | High impact if proven, needs two valid keys (AUTH_HELPED) |
| Query injection on /v1/history | **HOLD** | Low impact (self-tenant), key-gated, unproven |
| CORS wildcard origin reflection | **INVALID** | Disproven — static `*`, no credentials |
| return-to cookie tampering | **INVALID** | Disproven — server rejects/resets |

**Top 3 actionable for this cycle** (per directives):
1. **SSRF** — HIGH-VALUE CLASS; chain with auth bypass if any; request program key for POC
2. **npm impersonation** — Already reported; follow up with npm Trust & Safety per human lead
3. **IDOR** — HIGH-VALUE CLASS; request two trial keys for cross-tenant test

[NEXT] PROBE (read-only, no key): `GET https://api.gladia.io/v1/history?custom_metadata[__proto__][x]=1` (expect 401 — confirms key gate; if 500/altered → injection signal)
