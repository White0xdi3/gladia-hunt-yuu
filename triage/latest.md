===== TRIAGE 2026-09-28 00:59:08 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/*lead*"[90m 8 matches[0m
[0m✱ [0mGlob "**/scope.yml"[90m 1 match[0m
[0m→ [0mRead scope.yml
[0m→ [0mRead new-leads.txt
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
Based on my analysis of all lead files and the scope.yml, here are the 7-Question Gate verdicts for each unique hypothesis:

---

### 1. WebSocket auth token in URL query parameter (api.gladia.io)
**Q1** YES (api.gladia.io HIGHEST)  
**Q2** PARTIAL (requires valid API key to initiate session → AUTH_HELPED)  
**Q3** YES (token leaks via Referer/logs/history → session hijack)  
**Q4** NO (needs POST /v2/live with valid key to observe token format)  
**Q5** YES  
**Q6** YES  
**Q7** YES  
**VERDICT: HOLD** — real auth design flaw but requires AUTH_HELPED proof; cannot validate passively

---

### 2. Undocumented `/health` endpoint (api.gladia.io)
**Q1** YES  
**Q2** YES (public GET)  
**Q3** NO (only `{"health":"OK"}`; `?full=true` returns identical output — probes confirmed)  
**Q4** YES  
**Q5** YES (absent from OpenAPI)  
**Q6** NO (info disclosure of public operational data — always-rejected class)  
**Q7** NO  
**VERDICT: INVALID** — no security impact beyond public health status

---

### 3. SSRF via `audio_url`/`video_url`/`callback_url` server-side fetch (api.gladia.io)
**Q1** YES (HIGHEST asset)  
**Q2** NO (all endpoints key-gated: 401 without `x-gladia-key`)  
**Q3** YES (cloud metadata 169.254.169.254, internal network, callback SSRF → High)  
**Q4** NO (requires POST with valid key → AUTH_HELPED)  
**Q5** YES  
**Q6** YES  
**Q7** YES  
**VERDICT: HOLD** — High-severity SSRF-by-design confirmed in spec, but key-gated; needs valid key for PoC

---

### 4. npm `gladia@0.1.3` orphaned impersonation + key-in-URL leak
**Q1** YES (Official SDKs npm @ MEDIUM scope; supply-chain impacts Gladia users)  
**Q2** YES (public registry, anyone installs)  
**Q3** YES (impersonation + `src/client.ts:306-308` embeds raw API key in `wss://` URL query — keys land in proxy/access logs)  
**Q4** YES (passive: registry metadata, tarball sha256 `3b23ec7d…`, GitHub user+repo 404, README "Unofficial" vs package.json "Official")  
**Q5** YES (human-reported 2026-08-12, still live)  
**Q6** YES  
**Q7** YES (human triager already accepted)  
**VERDICT: VALID**  
**Minimal read-only proof**: `npm view gladia@0.1.3` → description="Official", maintainer=softwarecitadel@gmail.com, repo=alexisbouchez/gladia.ts (404), tarball `src/client.ts` line 307 `searchParams.append('x-gladia-key', apiKey)`  
**Impact**: Supply-chain API key harvesting + irrevocable takeover risk (orphaned GitHub account)  
**CVSS 3.1**: 7.4 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:N) — Medium-High  
**Reporting channel**: Gladia security via https://gladia.io/bug-bounty-report (Google Forms, SSO-gated) — **already submitted 2026-08-12, awaiting vendor response**

---

### 5. CORS wildcard reflects arbitrary Origin (api.gladia.io)
**Q1** YES  
**Q2** YES  
**Q3** NO (probes confirm static `access-control-allow-origin: *`, no Origin reflection, no credentials)  
**Q4** YES  
**Q5** N/A (disproven)  
**Q6** N/A  
**Q7** NO  
**VERDICT: INVALID** — static `*` without credentials is not exploitable for cross-origin reads

---

### 6. Post-OAuth open redirect via `redirect_to` (app.gladia.io)
**Q1** YES (app.gladia.io HIGH)  
**Q2** PARTIAL (reflection confirmed passively; post-auth behavior needs session → HUMAN_ONLY)  
**Q3** MEDIUM (phishing; OAuth `redirect_uri` is FIXED PKCE S256 — no code theft)  
**Q4** NO (requires full Google OAuth flow with session)  
**Q5** YES  
**Q6** YES  
**Q7** MAYBE (depends on unverified post-auth honoring)  
**VERDICT: HOLD** — reflection confirmed, post-auth validation blocked on HUMAN_ONLY

---

### 7. `return-to` cookie JWT parsing without signature (app.gladia.io)
**Q1** YES  
**Q2** YES  
**Q3** NO (cookie is unsigned base64url JSON `{"url":"/"}`; server rejects tampered value and resets)  
**Q4** YES  
**Q5** N/A (disproven)  
**Q6** N/A  
**Q7** NO  
**VERDICT: INVALID** — server-side validation prevents open redirect

---

### 8. Tech stack disclosure: `x-powered-by: Express` on CORS preflight only (api.gladia.io)
**Q1** YES  
**Q2** YES (public OPTIONS)  
**Q3** LOW (framework fingerprinting only — aids reconnaissance)  
**Q4** YES  
**Q5** YES  
**Q6** NO (best-practice header disclosure — always-rejected class)  
**Q7** NO  
**VERDICT: INVALID** — low-value info disclosure

---

### 9. IDOR on transcription file download `/{id}/file` (api.gladia.io)
**Q1** YES  
**Q2** NO (requires valid key + cross-account resource ID → AUTH_HELPED)  
**Q3** YES (cross-tenant PII/audio access → High)  
**Q4** NO  
**Q5** YES (untested)  
**Q6** YES  
**Q7** YES  
**VERDICT: HOLD** — speculative; needs AUTH_HELPED with two accounts

---

### 10. Query-param parsing injection on `/v1/history` (api.gladia.io)
**Q1** YES  
**Q2** NO (key-gated)  
**Q3** LOW-MEDIUM (filter bypass/prototype pollution on own tenant)  
**Q4** NO  
**Q5** YES  
**Q6** YES  
**Q7** MAYBE  
**VERDICT: HOLD** — requires AUTH_HELPED

---

### 11. OpenAPI shadow/undocumented v2 paths (api.gladia.io)
**Q1** YES  
**Q2** YES  
**Q3** NO (probes: `/admin`, `/debug`, `/v1/`, `/internal`, `/actuator/health` all 404)  
**Q4** YES  
**Q5** N/A  
**Q6** N/A  
**Q7** NO  
**VERDICT: INVALID** — no shadow endpoints exist

---

## Summary
| Lead | Verdict | Notes |
|------|---------|-------|
| WS token in URL | HOLD | Needs valid API key |
| `/health` endpoint | INVALID | Public data only |
| SSRF `audio_url`/`callback_url` | HOLD | Key-gated, High if proven |
| **npm `gladia@0.1.3` impersonation** | **VALID** | **Reported 2026-08-12, passive proof complete** |
| CORS Origin reflection | INVALID | Static `*` disproven |
| Post-OAuth `redirect_to` | HOLD | Needs human OAuth session |
| `return-to` cookie | INVALID | Server resets tampered value |
| `x-powered-by` Express | INVALID | Best-practice disclosure |
| IDOR `/{id}/file` | HOLD | Needs two accounts + key |
| `/v1/history` injection | HOLD | Needs key |
| Shadow endpoints | INVALID | All 404 |

**Only one VALID finding this cycle**: the orphaned npm package `gladia@0.1.3` — already reported to Gladia security (2026-08-12) and npm Trust & Safety. No new VALID vulnerabilities to report.
