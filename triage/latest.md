===== TRIAGE 2026-10-06 21:46:43 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/scope.yml"[90m 1 match[0m
[0m✱ [0mGlob "**/*"[90m 53 matches[0m
[0m→ [0mRead scope.yml
[0m→ [0mRead probe-results.txt
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
Based on my analysis of all lead files and the scope.yml, here are the 7-Question Gate evaluations for each unique vulnerability class:

---

### LEAD 1: npm `gladia@0.1.3` impersonation/typosquat with API key leakage in WebSocket URL
**Q1 Scope?** YES — npm `gladia` explicitly listed in scope.yml npm_packages  
**Q2 Reachable?** YES — Public npm registry, zero auth to install/inspect  
**Q3 Impact?** YES — Supply-chain: developers install fake "Official" SDK; src/client.ts:306-308 embeds raw `x-gladia-key` in `wss://api.gladia.io/v2/live?x-gladia-key=<KEY>` URL query → keys leak via proxy logs, browser history, Referer headers. Orphaned repo (alexisbouchez 404) = irrevocable takeover risk.  
**Q4 Passive proof?** YES — `npm view gladia@0.1.3` metadata (description "Official", maintainer softwarecitadel@gmail.com, repo alexisbouchez/gladia.ts 404), tarball sha256 `3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2`, source inspection confirming key-in-URL — all PASSIVE, reproduced 10+ independent times  
**Q5 Novel?** YES — Independent bot validation; human reported 2026-08-12 but vendor unresponsive  
**Q6 Not rejected?** YES — Not info-disclosure/best-practice/rate-limit/self-XSS; active supply-chain + credential hygiene flaw  
**Q7 Triager accept?** YES — Clear impersonation + key leakage design flaw  

**VERDICT: VALID**  
**Proof:** `npm view gladia@0.1.3` + tarball `src/client.ts:306-308` + GitHub API 404 on user+repo  
**Impact:** Supply-chain API key harvesting + account takeover risk (P3/P4)  
**CVSS 3.1:** 8.2 (AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:N)  
**Channel:** Gladia bug-bounty form (https://gladia.io/bug-bounty-report → Google Forms, SSO-gated) + npm Trust & Safety (https://npmjs.com/support)

---

### LEAD 2: SSRF via `audio_url`/`video_url`/`callback_config.url` on `api.gladia.io/v2/pre-recorded`
**Q1 Scope?** YES — api.gladia.io Highest priority  
**Q2 Reachable?** PARTIAL — Requires valid `x-gladia-key` (key-gated, 401 NestJS HttpException)  
**Q3 Impact?** YES — Cloud metadata (169.254.169.254), internal network scan, callback POST exfiltration (High)  
**Q4 Passive proof?** NO — OpenAPI spec confirms `format:uri` no scheme allowlist, 7 webhook paths, FR/US egress via `/v1/models`, but **no passive confirmation of server-side fetch behavior**; all models mark AUTH_HELPED  
**Q5 Novel?** Spec surface known, exploitation unconfirmed  
**Q6 Not rejected?** YES  
**Q7 Triager accept?** HOLD — Without valid key + POC showing internal fetch reflection (error_code/timing differential), unproven  

**VERDICT: HOLD** — Needs AUTH_HELPED: `POST /v2/pre-recorded -H "x-gladia-key: <KEY>" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/"}'` vs canary URL, compare `error_message`/`status`/duration

---

### LEAD 3: Post-auth open redirect via `redirect_to` on `app.gladia.io/signin`
**Q1 Scope?** YES — app.gladia.io High priority  
**Q2 Reachable?** PARTIAL — Reflection into form action PASSIVE confirmed (`action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"`), but **post-auth honoring requires authenticated Google OAuth session (HUMAN_ONLY)**  
**Q3 Impact?** MEDIUM — Phishing redirect post-login; OAuth `redirect_uri` FIXED (PKCE S256) prevents code theft; return-to cookie tamper REJECTED  
**Q4 Passive proof?** NO — Final 302 Location after OAuth completion unobserved  
**Q5 Novel?** Reflection confirmed, post-auth behavior unknown  
**Q6 Not rejected?** YES  
**Q7 Triager accept?** HOLD — Confidence 45-55 across models; needs human OAuth flow test  

**VERDICT: HOLD** — Needs HUMAN: Complete Google SSO with `?redirect_to=https://evil.example.com`, capture post-auth 302 Location

---

### LEAD 4: CORS wildcard static `*` on `api.gladia.io` (no Origin reflection, no credentials)
**Q1 Scope?** YES  
**Q2 Reachable?** YES  
**Q3 Impact?** LOW — Cross-origin read of public endpoints only (/v1/models, /openapi.json, /health); no `access-control-allow-credentials`  
**Q4 Passive proof?** YES — Probes confirm static `*`, no Origin reflection  
**Q5 Novel?** NO — Standard misconfig  
**Q6 Not rejected?** NO — CORS wildcard without credentials = best-practice misconfig, not vulnerability  
**Q7 Triager accept?** NO  

**VERDICT: INVALID** — Static `*` without credentials not a vulnerability per program rules

---

### LEAD 5: WebSocket auth token in URL query parameter (`wss://api.gladia.io/v2/live?token=<uuid>`)
**Q1 Scope?** YES  
**Q2 Reachable?** PARTIAL — Requires valid key to init session via `POST /v2/live`  
**Q3 Impact?** HIGH — Token in URL leaks via Referer, browser history, proxy/server logs; bearer-equivalent for live session  
**Q4 Passive proof?** PARTIAL — OpenAPI spec confirms design; token format/rotation/unverified without key  
**Q5 Novel?** Design documented in spec  
**Q6 Not rejected?** YES  
**Q7 Triager accept?** HOLD — Design flaw confirmed, exploitation needs AUTH_HELPED  

**VERDICT: HOLD** — Needs AUTH_HELPED: `POST /v2/live` with valid key → inspect `url` token format, test WS upgrade Referer headers, verify token invalidation post-disconnect

---

### LEAD 6: Undocumented `/health` endpoint on `api.gladia.io`
**Q1 Scope?** YES  
**Q2 Reachable?** YES — Public, 200 OK  
**Q3 Impact?** NO — Returns only `{"health":"OK"}` (15B); verbose params `?full=true`, `?format=json`, `/actuator/health` all return identical/404 — no version/build/metadata leak  
**Q4 Passive proof?** YES — Probed exhaustively  
**Q5 Novel?** NO  
**Q6 Not rejected?** BORDERLINE — Minimal info disclosure of public health status  
**Q7 Triager accept?** NO  

**VERDICT: INVALID** — No sensitive information disclosed

---

### LEAD 7: `x-powered-by: Express` on CORS preflight only
**Q1 Scope?** YES  
**Q2 Reachable?** YES — Public OPTIONS requests  
**Q3 Impact?** LOW — Framework fingerprinting only (Node/Express CVE targeting aid)  
**Q4 Passive proof?** YES — Confirmed: present on OPTIONS, absent on GET  
**Q5 Novel?** NO — Common header leakage  
**Q6 Not rejected?** NO — Tech stack disclosure = information disclosure/best practice  
**Q7 Triager accept?** NO  

**VERDICT: INVALID** — Framework fingerprinting not a vulnerability

---

### LEAD 8: IDOR on transcription file download `/{id}/file` endpoints
**Q1 Scope?** YES  
**Q2 Reachable?** NO — Requires valid `x-gladia-key` + another user's transcription ID (cross-account)  
**Q3 Impact?** HIGH if true — PII/audio cross-tenant access  
**Q4 Passive proof?** NO — Spec shows no ownership-binding logic, but untestable without key + target ID  
**Q5 Novel?** Speculative  
**Q6 Not rejected?** YES  
**Q7 Triager accept?** HOLD  

**VERDICT: HOLD** — Needs AUTH_HELPED with two accounts

---

### LEAD 9: `return-to` cookie JWT parsing without signature (app.gladia.io)
**Q1 Scope?** YES  
**Q2 Reachable?** YES  
**Q3 Impact?** NONE — Server rejects tampered cookie, resets to default `{"url":"/"}` (confirmed by nemotron3, laguna, bigpickle)  
**Q4 Passive proof?** YES — Tamper test done, server resets  
**Q5 Novel?** N/A  
**Q6 Not rejected?** N/A  
**Q7 Triager accept?** NO  

**VERDICT: INVALID** — Exploitability disproven

---

### LEAD 10: Query-param parsing injection on `/v1/history` (`custom_metadata` object, array params)
**Q1 Scope?** YES  
**Q2 Reachable?** PARTIAL — Requires valid key  
**Q3 Impact?** LOW-MEDIUM — Filter bypass / prototype pollution on own-tenant query only  
**Q4 Passive proof?** NO — Needs AUTH_HELPED  
**Q5 Novel?** Speculative from OpenAPI schema  
**Q6 Not rejected?** YES  
**Q7 Triager accept?** HOLD  

**VERDICT: HOLD** — Needs AUTH_HELPED: `GET /v1/history?custom_metadata[__proto__][x]=1` etc.

---

### SUMMARY
| Lead | Verdict | Key Blocker |
|------|---------|-------------|
| npm `gladia@0.1.3` impersonation + key-in-URL | **VALID** | None — report-ready |
| SSRF via audio_url/video_url/callback_url | **HOLD** | Valid API key for POC |
| Post-auth open redirect via redirect_to | **HOLD** | Authenticated Google OAuth session |
| CORS wildcard static `*` | **INVALID** | No credentials, best-practice only |
| WS token in URL query | **HOLD** | Valid API key to init session |
| Undocumented /health | **INVALID** | No sensitive data |
| x-powered-by Express on preflight | **INVALID** | Info disclosure only |
| IDOR on /{id}/file | **HOLD** | Valid key + cross-account ID |
| return-to cookie JWT parsing | **INVALID** | Server rejects tampering |
| /v1/history query-param injection | **HOLD** | Valid API key |

**Only one lead passes all 7 gates with passive evidence: the npm `gladia@0.1.3` impersonation/key-leakage.** It is report-ready for both Gladia's bug-bounty form and npm Trust & Safety. All HIGH-value API flaws (SSRF, IDOR, WS token leakage) remain HOLD pending AUTH_HELPED validation with a valid `x-gladia-key`.
