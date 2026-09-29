===== TRIAGE 2026-09-29 20:57:09 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/*"[90m 51 matches[0m
[0m→ [0mRead probe-results.txt
[0m→ [0mRead scope.yml
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
Based on my analysis of all lead files and the scope.yml, here are the triage verdicts for each unique vulnerability class:

---

### 1. SSRF via audio_url/video_url/callback_url server-side fetch (api.gladia.io)
**Q1** YES (api.gladia.io = Highest)  
**Q2** PARTIAL (requires valid x-gladia-key; 401 without)  
**Q3** YES (cloud metadata 169.254.169.254, internal network, HIGH if proven)  
**Q4** NO (requires AUTH_HELPED POST with valid key; GET/HEAD cannot prove server-side fetch)  
**Q5** Known hypothesis across all models, unproven  
**Q6** YES (SSRF not on rejected list)  
**Q7** HOLD — triager would accept IF key-gated POC provided; currently unvalidated  

**VERDICT: HOLD** — Spec confirms `format:uri` with no scheme allowlist; `/v1/models` shows FR/US egress; 7 webhook paths. Needs authorized key to prove.

---

### 2. npm `gladia@0.1.3` orphaned impersonation + key-in-URL (npm registry)
**Q1** YES (Official SDKs = Medium priority; npm registry in scope)  
**Q2** YES (public package, anyone installs)  
**Q3** YES (supply-chain: "Official" claim vs README "Unofficial"; orphaned repo alexisbouchez 404 = irrevocable takeover; src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query → leaks to proxy/logs/history)  
**Q4** YES (PASSIVE complete: registry metadata, tarball sha256 `3b23ec7d...`, GitHub 404, source code verified)  
**Q5** YES (human-reported 2026-08-12; still live, no vendor action)  
**Q6** YES (supply-chain impersonation not rejected)  
**Q7** YES — multiple models 95-97% confidence, report-ready  

**VERDICT: VALID**  
**Minimal proof**: `npm view gladia@0.1.3` → description "Official", maintainer `softwarecitadel@gmail.com`, repo `alexisbouchez/gladia.ts` (404); tarball `src/client.ts:306-308` shows `searchParams.append('x-gladia-key', apiKey)` → `new WebSocket(wsUrl.toString())`  
**Impact**: Supply-chain API key harvesting + irrevocable account takeover (P3/P4)  
**CVSS 3.1**: 7.5 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:N)  
**Channel**: Gladia bug-bounty-report (Google Forms) + npm Trust & Safety

---

### 3. Post-auth open redirect via redirect_to (app.gladia.io)
**Q1** YES (app.gladia.io = High)  
**Q2** PARTIAL (unauthenticated reflection confirmed; post-auth requires HUMAN_ONLY session)  
**Q3** MEDIUM (phishing post-auth; OAuth redirect_uri FIXED via PKCE → no code theft)  
**Q4** NO (requires authenticated Google OAuth session to observe final 302 Location)  
**Q5** Known hypothesis  
**Q6** YES  
**Q7** HOLD — unverified post-auth behavior  

**VERDICT: HOLD** — Form action reflects `redirect_to` URL-encoded for all variants (https://evil, //evil, confusing-subdomain). CSP has 0 `form-action` directives. Post-auth honoring untested.

---

### 4. WebSocket auth token in URL query param (api.gladia.io)
**Q1** YES (Highest)  
**Q2** YES (spec shows `wss://api.gladia.io/v2/live?token=<uuid>`)  
**Q3** HIGH (token leaks via Referer, browser history, proxy/server logs; bearer-equivalent)  
**Q4** PARTIAL (spec confirms design; exploitability needs AUTH_HELPED to check token lifetime, rotation, Referrer-Policy on WS upgrade)  
**Q5** Known from OpenAPI  
**Q6** YES  
**Q7** HOLD — design flaw confirmed, exploitability needs validation  

**VERDICT: HOLD** — Token-in-URL by design per spec. Need valid key to init session and inspect WS handshake headers.

---

### 5. Undocumented /health endpoint (api.gladia.io)
**Q1** YES  
**Q2** YES (public GET → 200 `{"health":"OK"}`)  
**Q3** NO (only `{"health":"OK"}`; `?full=true`/` ?format=json` return identical; no version/build/metadata)  
**Q4** YES (PASSIVE)  
**Q5** Known  
**Q6** NO — "info disclosure of public data" on always-rejected list  
**Q7** NO  

**VERDICT: INVALID** — Zero sensitive data disclosed.

---

### 6. CORS wildcard with x-gladia-key allowed (api.gladia.io)
**Q1** YES  
**Q2** YES  
**Q3** NO (static `access-control-allow-origin: *`; NO `access-control-allow-credentials`; only public endpoints `/v1/models`, `/openapi.json`, `/health` readable cross-origin)  
**Q4** YES (PASSIVE)  
**Q5** Known  
**Q6** NO — "best practice / rate limit absence alone" tier; wildcard without creds on public data  
**Q7** NO  

**VERDICT: INVALID** — No credential leakage, no sensitive data exposure.

---

### 7. x-powered-by: Express on CORS preflight only (api.gladia.io)
**Q1** YES  
**Q2** YES (OPTIONS preflight)  
**Q3** LOW (framework fingerprinting only)  
**Q4** YES (PASSIVE)  
**Q5** Known  
**Q6** NO — "info disclosure of public data" tier  
**Q7** NO  

**VERDICT: INVALID** — Low-value reconnaissance aid only.

---

### 8. IDOR on transcription file download /{id}/file (api.gladia.io)
**Q1** YES  
**Q2** NO (requires valid x-gladia-key + cross-account transcription ID)  
**Q3** HIGH (PII/audio cross-tenant)  
**Q4** NO (AUTH_HELPED required)  
**Q5** Hypothesis only  
**Q6** YES  
**Q7** HOLD  

**VERDICT: HOLD** — Spec shows 3 GET `{id}/file` endpoints; ownership binding opaque. Needs authorized key + cross-account test.

---

### 9. return-to cookie JWT parsing without signature (app.gladia.io)
**Q1** YES  
**Q2** YES  
**Q3** NONE — **DISPROVEN**: server rejects tampered cookie, resets to `{"url":"/"}`  
**Q4** YES (PASSIVE test confirmed)  
**Q5** Tested and rejected  
**Q6** N/A  
**Q7** NO  

**VERDICT: INVALID** — Multiple models confirmed server validates/resets tampered cookie.

---

### 10. Query-param parsing injection on /v1/history (api.gladia.io)
**Q1** YES  
**Q2** NO (key-gated, 401 without)  
**Q3** LOW-MEDIUM (filter bypass / prototype pollution on own-tenant)  
**Q4** NO (AUTH_HELPED)  
**Q5** Hypothesis (bigpickle only)  
**Q6** YES  
**Q7** HOLD  

**VERDICT: HOLD** — `custom_metadata` object + `status`/`kind` arrays in query string; NestJS deep-parse surface. Needs key.

---

### Summary
| Lead | Verdict |
|------|---------|
| SSRF audio_url/callback_url | HOLD |
| npm gladia@0.1.3 impersonation | **VALID** |
| Post-auth redirect_to open redirect | HOLD |
| WebSocket token in URL | HOLD |
| Undocumented /health | INVALID |
| CORS wildcard | INVALID |
| x-powered-by Express | INVALID |
| IDOR /{id}/file | HOLD |
| return-to cookie JWT | INVALID |
| /v1/history query injection | HOLD |

**Only one VALID finding this cycle**: npm `gladia@0.1.3` orphaned impersonation with credential-leaking WebSocket URL construction. All others require AUTH_HELPED or HUMAN_ONLY validation, or are invalid/low-value.
