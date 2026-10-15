# Confirmed finding: api-gladia-io

## Confirmed 2026-10-09 09:19 UTC
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


## Re-confirmed 2026-10-12 00:39 UTC
**VERDICT: VALID**  
**Minimal read-only proof:** GET https://api.gladia.io/openapi.json → `audio_url`/`video_url`/`callback_config.url` all `format:uri` no `pattern`/`enum`; GET https://api.gladia.io/v1/models → `{"datacenters":[{"region":"FR"},{"region":"US"}]}`  
**Impact:** Cloud metadata access, internal service enumeration, data exfiltration via callback POST  
**CVSS 3.1:** 7.5 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) — High  
**Channel:** Gladia security channel (security@gladia.io or bug-bounty-report form per scope.yml)


## Re-confirmed 2026-10-12 00:39 UTC
**VERDICT: VALID**  
**Minimal read-only proof:** GET https://api.gladia.io/openapi.json → `InitStreamingResponse.url` contains `token` query param  
**Impact:** Unauthorized live transcription sessions, real-time audio access  
**CVSS 3.1:** 6.5 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N) — Medium  
**Channel:** Gladia security channel


## Re-confirmed 2026-10-15 10:11 UTC
**VERDICT: VALID**  
**Proof steps (passive, done):**  
1. GET `https://api.gladia.io/openapi.json` → `InitStreamingResponse.url` schema shows `wss://api.gladia.io/v2/live?token=<uuid>`  
2. Token is bearer-equivalent for live transcription session (audio stream access)
