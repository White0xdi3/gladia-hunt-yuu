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
