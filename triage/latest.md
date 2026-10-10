===== TRIAGE 2026-10-10 13:55:55 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/*"[90m 54 matches[0m
[0m→ [0mRead new-leads.txt
[0m→ [0mRead probe-results.txt
[0m→ [0mRead probe-results.md
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead scope.yml
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead reposcan-raw/grep-hits.txt
Now I have all the data. Let me apply the 7-Question Gate to each distinct lead and produce verdicts.

---

## TRIAGE VERDICTS

### LEAD 1: SSRF via `audio_url`/`video_url`/`callback_url` server-side fetch (api.gladia.io)
**Q1 Scope:** YES — api.gladia.io is Highest priority per scope.yml  
**Q2 Attacker reach:** NO — Requires valid `x-gladia-key` (401 without); key-gated only  
**Q3 Real impact:** YES — Cloud metadata (169.254.169.254), internal network access if reachable  
**Q4 Passive proof:** NO — Needs authenticated POST with internal URL to observe error/timing delta; probe results show only 401 on unauthenticated requests  
**Q5 Novel:** YES — Not previously reported to program (per lead-human, no vendor action on this vector)  
**Q6 Not rejected:** YES — SSRF is not on always-rejected list  
**Q7 Triager accept:** HOLD — Auth-gated; cannot validate without program-provided key  

**VERDICT: HOLD** — Auth-gated SSRF surface confirmed by spec+RAG (format:uri no allowlist, FR/US egress, 7 webhook paths), but passive validation impossible. Requires `AUTH_HELPED` probe with valid key.  
**Next:** `[NEXT] PROBE: POST https://api.gladia.io/v2/pre-recorded -H "x-gladia-key: <VALID_KEY>" -H "Content-Type: application/json" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/"}'` — compare error_code/status/duration vs benign URL.

---

### LEAD 2: npm `gladia@0.1.3` orphaned impersonation + raw API key in WebSocket URL
**Q1 Scope:** YES — npm `gladia` listed in scope.yml npm_packages  
**Q2 Attacker reach:** YES — Public registry, installable by anyone (`npm i gladia`)  
**Q3 Real impact:** YES — Supply-chain: package claims "Official" but README says "Unofficial"; maintainer `softwarecitadel@gmail.com` (personal); repo `alexisbouchez/gladia.ts` 404 (user+repo orphaned → irrevocable takeover risk); src/client.ts:306-308 embeds raw `x-gladia-key` in `wss://api.gladia.io/v2/live` query string → keys leak in proxy/access logs, browser history, Referer  
**Q4 Passive proof:** YES — All evidence from registry metadata + tarball inspection + GitHub API (404) + source RAG; reproduced 10+ independent times  
**Q5 Novel:** YES — Reported by human 2026-08-12, no vendor action yet (lead-human)  
**Q6 Not rejected:** YES — Supply-chain impersonation + credential hygiene flaw not on rejected list  
**Q7 Triager accept:** YES — Clear evidence, report-ready  

**VERDICT: VALID**  
**Impact:** Medium-High (P3/P4) — developers installing impersonated "official" SDK leak API keys via WS URL; orphaned package = irrevocable takeover risk  
**CVSS 3.1:** AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:N = **7.1 High** (supply-chain + credential exposure)  
**Channel:** Gladia security channel per scope.yml → `https://gladia.io/bug-bounty-report` (Google Forms, SSO-gated)  
**Proof steps (passive, already complete):**
1. `npm view gladia@0.1.3 description repository.url maintainer` → "Official TypeScript SDK for Gladia" + personal repo/maintainer
2. `curl -s https://api.github.com/repos/alexisbouchez/gladia.ts` → 404 (user+repo both 404)
3. Tarball inspection: `src/client.ts:306-308` → `wsUrl.searchParams.append('x-gladia-key', this.apiKey)` + `new WebSocket(wsUrl.toString())`
4. Compare with official `@gladiaio/sdk` → uses POST `/v2/live` then connects to short-lived `session.url` (no key in URL)

---

### LEAD 3: Post-auth open redirect via `redirect_to` on `app.gladia.io/signin`
**Q1 Scope:** YES — app.gladia.io is High priority per scope.yml  
**Q2 Attacker reach:** PARTIAL — `redirect_to` reflected in form action unauthenticated (200, confirmed 100+ cycles), but post-auth honor requires valid Google OAuth session  
**Q3 Real impact:** YES — If honored post-auth: phishing redirect to attacker domain; OAuth redirect_uri is FIXED (PKCE S256) so code/state theft NOT possible via this vector  
**Q4 Passive proof:** NO — Final post-auth Location header unobservable without authenticated session  
**Q5 Novel:** YES — Not previously reported as validated vulnerability  
**Q6 Not rejected:** YES — Open redirect not on rejected list (but requires auth)  
**Q7 Triager accept:** HOLD — Unverified post-auth behavior; all unauthenticated reflection confirmed, OAuth redirect_uri FIXED prevents escalation  

**VERDICT: HOLD** — Form-action reflection byte-fresh (100+ cycles), CSP has 0 `form-action` directives (gap confirmed), but post-auth honoring untested.  
**Next:** `[NEXT] PROBE: HUMAN — authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth; capture final 302 Location + Set-Cookie; test //evil.example.com and https://app.gladia.io.evil.example.com variants`

---

### LEAD 4: WebSocket auth token in URL query parameter (`wss://api.gladia.io/v2/live?token=<uuid>`)
**Q1 Scope:** YES — api.gladia.io Highest priority  
**Q2 Attacker reach:** YES — Token issued via POST `/v2/live` (key-gated), then used in WS URL  
**Q3 Real impact:** YES — Token in URL leaks via: browser history, Referer headers on WS upgrade, TLS-terminating proxy logs, server access logs, URL sharing  
**Q4 Passive proof:** PARTIAL — Spec confirms token-in-URL design (OpenAPI `InitStreamingResponse.url`), but token format/lifetime/rotation unobservable without key  
**Q5 Novel:** YES — Not previously reported  
**Q6 Not rejected:** YES — Token-in-URL credential leakage is valid finding  
**Q7 Triager accept:** HOLD — Design confirmed by spec; exploitability (token lifetime, rotation, Referrer-Policy on WS handshake) unproven without key  

**VERDICT: HOLD** — Spec confirms `wss://api.gladia.io/v2/live?token=<uuid>`; token is bearer-equivalent for live session.  
**Next:** `[NEXT] PROBE: POST https://api.gladia.io/v2/live -H "x-gladia-key: <VALID_KEY>" -H "Content-Type: application/json" -d '{}' → observe response.url token format; initiate WS connection and inspect upgrade request headers for Referer; check if token works after session close`

---

### LEAD 5: Undocumented `/health` endpoint on api.gladia.io
**Q1 Scope:** YES — api.gladia.io Highest priority  
**Q2 Attacker reach:** YES — Public, unauthenticated (200 `{"health":"OK"}`)  
**Q3 Real impact:** NO — Returns only `{"health":"OK"}` (15 bytes); probe confirms no verbose mode via `?full=true`, `?format=json`, `/actuator/health` — all return identical output or 404  
**Q4 Passive proof:** YES — Verified via GET probes  
**Q5 Novel:** YES — Not in OpenAPI spec (14 documented paths)  
**Q6 Not rejected:** NO — **Fails Q6**: Information disclosure of non-sensitive public health status; no version/build/metadata leak. On always-rejected list as "info disclosure of public data / best practice"  
**Q7 Triager accept:** NO  

**VERDICT: INVALID** — `/health` returns minimal static JSON; no sensitive disclosure. Rejected by multiple models after `?full=true` probe returned identical output.

---

### LEAD 6: CORS wildcard with `x-gladia-key` allowed cross-origin
**Q1 Scope:** YES — api.gladia.io Highest priority  
**Q2 Attacker reach:** YES — Preflight allows `Access-Control-Allow-Headers: x-gladia-key` with `Access-Control-Allow-Origin: *`  
**Q3 Real impact:** NO — **Fails Q3**: No `Access-Control-Allow-Credentials: true`; wildcard is static `*` (not Origin reflection); credentialed requests cannot be made cross-origin. Only unauthenticated public endpoints (`/v1/models`, `/health`, `/openapi.json`) readable cross-origin — already public.  
**Q4 Passive proof:** YES — Confirmed via OPTIONS/GET probes  
**Q5 Novel:** N/A  
**Q6 Not rejected:** NO — CORS wildcard without credentials is standard misconfig, not exploitable for authenticated data exfiltration  
**Q7 Triager accept:** NO  

**VERDICT: INVALID** — Verified: `access-control-allow-origin: *` static, no credentials support, Origin not reflected. Cross-origin reads limited to already-public endpoints.

---

### LEAD 7: Tech stack disclosure via `x-powered-by: Express` on CORS preflight only
**Q1 Scope:** YES — api.gladia.io Highest priority  
**Q2 Attacker reach:** YES — Visible on OPTIONS preflight (204)  
**Q3 Real impact:** NO — **Fails Q3**: Framework fingerprinting alone is recon aid, not a vulnerability. No CVE exploited, no sensitive data leaked. On rejected list as "best practice / info disclosure"  
**Q4 Passive proof:** YES — Confirmed: present on OPTIONS, absent on GET  
**Q5 Novel:** N/A  
**Q6 Not rejected:** NO  
**Q7 Triager accept:** NO  

**VERDICT: INVALID** — Low-severity reconnaissance aid only; not a security vulnerability per program rules.

---

### LEAD 8: IDOR on transcription file download endpoints (`/{id}/file`)
**Q1 Scope:** YES — api.gladia.io Highest priority  
**Q2 Attacker reach:** NO — Requires valid `x-gladia-key` (key-gated 401)  
**Q3 Real impact:** YES — Cross-account transcription data (PII, audio) if authorization not bound to key scope  
**Q4 Passive proof:** NO — Needs two accounts/keys to test cross-account access  
**Q5 Novel:** YES — Not previously reported  
**Q6 Not rejected:** YES — IDOR is high-value class  
**Q7 Triager accept:** HOLD — Spec shows three `/file` endpoints; ownership-binding logic opaque in spec; untestable without keys  

**VERDICT: HOLD** — Confidence 50 (spec-only, no ownership-binding visible).  
**Next:** `[NEXT] PROBE: AUTH_HELPED — obtain two valid x-gladia-keys (authorized), POST /v2/transcription with test audio, GET /v2/transcription/{other_user_id}/file with own key; observe 200 (IDOR) vs 403 (protected)`

---

### LEAD 9: Query-param parsing injection on `/v1/history` (`custom_metadata` object + array params)
**Q1 Scope:** YES — api.gladia.io Highest priority  
**Q2 Attacker reach:** NO — Key-gated (401 without key)  
**Q3 Real impact:** LOW — Prototype pollution / filter bypass on own-tenant query only (key-gated)  
**Q4 Passive proof:** NO — Requires key to inject payloads (`custom_metadata[__proto__][x]=1`, `custom_metadata[$ne]=null`)  
**Q5 Novel:** YES — Not previously reported  
**Q6 Not rejected:** YES — Injection class not rejected  
**Q7 Triager accept:** HOLD — Low impact (self-tenant only), key-gated, unproven  

**VERDICT: HOLD** — Spec confirms `custom_metadata` as object with `additionalProperties:true` + `status`/`kind` as arrays in query string; NestJS deep-parse foot-gun possible but impact limited to own data.

---

### LEAD 10: Return-to cookie JWT parsing without signature verification (app.gladia.io)
**Q1 Scope:** YES — app.gladia.io High priority  
**Q2 Attacker reach:** YES — Cookie set on root `/`  
**Q3 Real impact:** NO — **Fails Q3**: Server rejects tampered cookie and resets to default `{"url":"/"}` (confirmed by multiple models); no open redirect via cookie tampering  
**Q4 Passive proof:** YES — Verified via tampering test  
**Q5 Novel:** N/A  
**Q6 Not rejected:** NO — Fails Q3 (no impact)  
**Q7 Triager accept:** NO  

**VERDICT: INVALID** — Cookie is unsigned base64url JSON (not JWT), but server validates/resets on tamper. No vulnerability.

---

## SUMMARY

| # | Lead | Verdict | Key Reason |
|---|------|---------|------------|
| 1 | SSRF via audio_url/callback_url | **HOLD** | Auth-gated; spec confirms SSRF-by-design but needs key to prove |
| 2 | npm `gladia@0.1.3` impersonation + key-in-URL | **VALID** | Passive proof complete; supply-chain + credential leakage; report-ready |
| 3 | Post-auth open redirect via redirect_to | **HOLD** | Form-action reflection confirmed; post-auth honor untested (needs session) |
| 4 | WS token in URL query param | **HOLD** | Spec confirms design; token lifetime/rotation/Referrer-Policy unproven |
| 5 | Undocumented /health endpoint | **INVALID** | Only `{"health":"OK"}`; no sensitive disclosure |
| 6 | CORS wildcard + x-gladia-key | **INVALID** | Static `*`, no credentials; only public endpoints readable cross-origin |
| 7 | x-powered-by: Express on preflight | **INVALID** | Recon aid only; not a vulnerability |
| 8 | IDOR on /{id}/file endpoints | **HOLD** | Key-gated; ownership-binding unknown; needs two keys |
| 9 | /v1/history query-param injection | **HOLD** | Key-gated; low impact (self-tenant); unproven |
| 10 | Return-to cookie unsigned JWT | **INVALID** | Server rejects tamper; no open redirect |

---

## IMMEDIATE ACTIONABLE REPORT

**Only LEAD 2 is VALID and report-ready today.**

**Report Target:** `https://gladia.io/bug-bounty-report` (Google Forms, SSO-gated)  
**Evidence Package:** (from lead-human/lead-mimo, 10+ independent reproductions)
- Package: `npmjs.com/package/gladia` v0.1.3 (dist-tag `latest`)
- Description claims "Official TypeScript SDK for Gladia"
- Maintainer: `softwarecitadel@gmail.com` (no Gladia affiliation)
- Repository: `github.com/alexisbouchez/gladia.ts` → **404** (user + repo both 404 = orphaned, irrevocable takeover risk)
- Tarball sha256: `3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2`
- Source: `src/client.ts:306-308` → `wsUrl.searchParams.append('x-gladia-key', this.apiKey)` + `new WebSocket(wsUrl.toString())` — raw API key in WS URL query
- Contradiction: README.md says "Unofficial TypeScript SDK" vs package.json "Official"
- Official SDK: `@gladiaio/sdk@1.1.0` (publisher `bot-npmjs-gladiaio` under Gladia org) uses header auth + short-lived session URL

**CVSS 3.1:** **7.1 High** (AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:N)  
**Severity:** Medium-High (P3/P4) — supply-chain impersonation + credential hygiene flaw + irrevocable takeover risk
