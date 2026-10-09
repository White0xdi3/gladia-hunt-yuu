===== TRIAGE 2026-10-09 09:19:53 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/*"[90m 53 matches[0m
[0m→ [0mRead new-leads.txt
[0m→ [0mRead probe-results.txt
[0m→ [0mRead scope.yml
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead leads/reposcan-latest.md
[0m→ [0mRead triage-prompt.txt
Based on the lead files and probe results, here are the distinct leads triaged against the 7-Question Gate:

---

### Lead 1: npm `gladia@0.1.3` impersonation + key-in-WebSocket-URL
**Q1** YES — npm registry is in scope (scope.yml: npm_packages includes `gladia`)  
**Q2** YES — public package, anyone can `npm install gladia`  
**Q3** YES — supply-chain impersonation (false "Official" claim) + credential leakage (raw API key in WS URL query string leaks to proxy/access logs, browser history)  
**Q4** YES — fully passive: `npm view gladia@0.1.3`, tarball inspection, GitHub API 404 on user+repo, source confirms `searchParams.append('x-gladia-key', apiKey)`  
**Q5** YES — not previously reported to Gladia (human reported 2026-08-12 but npm Trust & Safety track separate; no vendor action yet)  
**Q6** YES — not on rejected list (impersonation + credential exposure are actionable)  
**Q7** YES — reasonable triager accepts: orphaned package at dist-tag latest, irrevocable takeover risk, active harm to developers  
**VERDICT: VALID**  
**Proof:** `npm view gladia@0.1.3 description repository.url maintainer` + tarball `src/client.ts:306-308` + GitHub API 404 on alexisbouchez  
**Impact:** Supply-chain API key harvesting + account takeover risk  
**CVSS 3.1:** 7.5 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N)  
**Channel:** Gladia bug bounty form (https://gladia.io/bug-bounty-report) + npm Trust & Safety (https://npmjs.com/support)

---

### Lead 2: SSRF via audio_url/video_url/callback_url on api.gladia.io
**Q1** YES — api.gladia.io is HIGHEST priority in scope  
**Q2** NO — requires valid `x-gladia-key` (all v2 endpoints return 401 without key)  
**Q3** YES — cloud metadata (169.254.169.254), internal network access, data exfiltration via callback  
**Q4** NO — requires AUTH_HELPED (POST with valid key to `/v2/pre-recorded` or `/video/text/video-transcription`)  
**Q5** UNKNOWN — SSRF class is known but specific instance unconfirmed without key  
**Q6** YES — SSRF to cloud metadata is not rejected  
**Q7** HOLD — real surface (spec confirms `format:uri` no allowlist, FR/US egress), but unexploitable without program-provided key  
**VERDICT: HOLD** — needs authorized API key for POC; surface frozen 100+ cycles

---

### Lead 3: Post-auth open redirect via redirect_to on app.gladia.io
**Q1** YES — app.gladia.io is HIGH priority  
**Q2** PARTIAL — reflection is public (GET `/signin?redirect_to=...` reflects in form action), but post-auth behavior requires authenticated session  
**Q3** MEDIUM — phishing redirect post-Google-OAuth; OAuth redirect_uri is FIXED (PKCE) so no code theft  
**Q4** NO — post-auth verification requires HUMAN_ONLY (complete Google SSO flow)  
**Q5** YES — distinct from return-to cookie (rejected)  
**Q6** YES — open redirect post-auth is actionable  
**Q7** HOLD — reflection confirmed byte-fresh 100+ cycles, CSP lacks form-action, but final redirect untested without session  
**VERDICT: HOLD** — needs human OAuth session to confirm server honors redirect_to post-auth

---

### Lead 4: WebSocket auth token in URL query parameter
**Q1** YES — api.gladia.io in scope  
**Q2** YES — token issued via POST `/v2/live` (key-gated), but token in `wss://...?token=<uuid>` leaks via Referer, browser history, proxy logs  
**Q3** YES — bearer-equivalent token enables unauthorized live transcription, audio access  
**Q4** PARTIAL — token format confirmed from OpenAPI spec (passive), but token lifecycle/rotation requires AUTH_HELPED  
**Q5** YES — not previously reported as standalone  
**Q6** YES — token-in-URL is credential hygiene flaw  
**Q7** YES — design flaw with real impact if token intercepted  
**VERDICT: VALID** (design flaw, passive evidence from spec)  
**Proof:** OpenAPI spec `InitStreamingResponse.url` = `wss://api.gladia.io/v2/live?token=<uuid>`  
**Impact:** Token theft → unauthorized live sessions, audio data access  
**CVSS 3.1:** 6.5 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N)  
**Channel:** Gladia bug bounty form

---

### Lead 5: Undocumented /health endpoint on api.gladia.io
**Q1** YES — api.gladia.io in scope  
**Q2** YES — public GET `/health` returns 200 `{"health":"OK"}`  
**Q3** LOW — only `{"health":"OK"}`; no version/build metadata even with `?full=true` or `?format=json` (probed, returns identical)  
**Q4** YES — passive GET confirmed  
**Q5** YES — not in OpenAPI spec (14 documented paths)  
**Q6** NO — info disclosure of public/operational data only; no sensitive data leaked  
**Q7** NO — reasonable triager rejects as low-value operational endpoint  
**VERDICT: INVALID** — information disclosure of non-sensitive public data (always-rejected list)

---

### Lead 6: CORS wildcard with x-gladia-key allowed
**Q1** YES — api.gladia.io in scope  
**Q2** YES — public endpoints (`/v1/models`, `/openapi.json`, `/health`) readable cross-origin  
**Q3** LOW — wildcard is static `*` (not Origin reflection), NO `access-control-allow-credentials`; authenticated endpoints still return 401 cross-origin  
**Q4** YES — passive OPTIONS/GET probes confirm  
**Q5** YES — confirmed not reflecting Origin (contradicted earlier hypothesis)  
**Q6** YES — but wildcard without credentials is standard misconfig, not exploitable for credentialed reads  
**Q7** NO — reasonable triager: low risk, no credential leakage, public data only  
**VERDICT: INVALID** — best practice misconfig only, no exploitable impact

---

### Lead 7: x-powered-by: Express on CORS preflight only
**Q1** YES — api.gladia.io in scope  
**Q2** YES — OPTIONS preflight returns `x-powered-by: Express` (absent on GET)  
**Q3** LOW — framework fingerprinting only; aids CVE targeting but no direct exploit  
**Q4** YES — passive probe confirmed  
**Q5** YES — confirmed this cycle  
**Q6** YES — not rejected but low severity  
**Q7** NO — reasonable triager: info disclosure only, no vulnerability  
**VERDICT: INVALID** — tech stack disclosure is reconnaissance aid, not a vulnerability

---

### Lead 8: IDOR on transcription file download endpoints /{id}/file
**Q1** YES — api.gladia.io in scope  
**Q2** NO — requires valid `x-gladia-key` (all endpoints key-gated)  
**Q3** HIGH — cross-tenant transcription data (PII, audio)  
**Q4** NO — requires AUTH_HELPED (two keys from different accounts)  
**Q5** UNKNOWN — untested without keys  
**Q6** YES — IDOR/BOLA is high-value class  
**Q7** HOLD — spec shows three endpoints but ownership binding unknown; cannot verify without authorized keys  
**VERDICT: HOLD** — needs program-provided keys for cross-account test

---

### Lead 9: Query-param parsing injection on /v1/history
**Q1** YES — api.gladia.io in scope  
**Q2** NO — key-gated (401 without key)  
**Q3** MEDIUM — prototype pollution / filter bypass on own-tenant data  
**Q4** NO — requires AUTH_HELPED (GET with injection payloads)  
**Q5** YES — `custom_metadata` as object with `additionalProperties:true` in query string is unusual  
**Q6** YES — injection class not rejected  
**Q7** HOLD — plausible but unproven without key  
**VERDICT: HOLD** — needs authorized key to test

---

### Lead 10: return-to cookie JWT parsing without signature verification
**Q1** YES — app.gladia.io in scope  
**Q2** YES — cookie set on root `/`  
**Q3** NO — server rejects tampered cookie and resets to default `{"url":"/"}` (confirmed passive probe)  
**Q4** YES — passive test confirmed rejection  
**Q5** N/A — rejected after validation  
**Q6** N/A  
**Q7** NO — no open redirect or auth bypass achieved  
**VERDICT: INVALID** — server-side validation prevents exploitation

---

## Summary

| Lead | Verdict | Key Reason |
|------|---------|------------|
| npm `gladia@0.1.3` impersonation + key-in-URL | **VALID** | Passive, report-ready, supply-chain + credential leak |
| WebSocket token in URL query param | **VALID** | Spec-confirmed design flaw, token leaks via Referer/logs |
| SSRF via audio_url/callback_url | **HOLD** | Real surface, needs authorized key for POC |
| Post-auth open redirect (redirect_to) | **HOLD** | Reflection confirmed, post-auth behavior needs human session |
| IDOR on /{id}/file | **HOLD** | High impact if true, needs cross-account keys |
| Query-param injection /v1/history | **HOLD** | Plausible, needs key |
| Undocumented /health | **INVALID** | Only `{"health":"OK"}`, no sensitive data |
| CORS wildcard | **INVALID** | Static `*`, no credentials, public data only |
| x-powered-by Express | **INVALID** | Reconnaissance only |
| return-to cookie | **INVALID** | Server validates/resets tampered values |

**Top 2 reportable now:** Lead 1 (npm impersonation) and Lead 4 (WS token-in-URL). Both fully passive, in scope, real impact.
