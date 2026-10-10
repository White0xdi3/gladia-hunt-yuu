===== TRIAGE 2026-10-10 22:43:34 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/*"[90m 54 matches[0m
[0m→ [0mRead scope.yml
[0m→ [0mRead probe-results.txt
[0m→ [0mRead new-leads.txt
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead leads/reposcan-latest.md
Now I have a complete picture. Let me apply the 7-Question Gate to each unique vulnerability class across all leads.

---

## TRIAGE VERDICTS

### 1. **npm `gladia@0.1.3` impersonation + API key leakage in WebSocket URL** (npm registry)
**Q1 Scope:** YES — npm packages listed in scope.yml (`@gladiaio/sdk`, `gladia`); this typosquat directly targets developers using the program's SDK  
**Q2 Reachable:** YES — Public npm registry, anyone can `npm install gladia`  
**Q3 Impact:** YES — Supply-chain impersonation (description "Official" vs README "Unofficial"), orphaned repo (GitHub user+repo 404 = irrevocable takeover risk), src/client.ts:306-308 embeds raw `x-gladia-key` in `wss://api.gladia.io/v2/live?x-gladia-key=<KEY>` URL query → keys leak via proxy/access logs, browser history, Referer headers. Medium-High.  
**Q4 Passive proof:** YES — Registry metadata, tarball sha256 `3b23ec7d…7f2`, shasum `cc96f84a…`, GitHub API 404 on user+repo, README vs package.json contradiction, source code inspection — all verified passively across 10+ independent reproductions  
**Q5 Novel:** YES — Locked finding, not previously reported to program  
**Q6 Not rejected:** YES — Supply-chain impersonation + credential hygiene flaw are valid classes  
**Q7 Triager accept:** YES — Clear evidence package, report-ready  

**VERDICT: VALID**  
**Minimal proof:** `npm view gladia@0.1.3 description repository.url maintainer` + tarball `src/client.ts:306-308` showing `searchParams.append('x-gladia-key', apiKey)` + `npm view @gladiaio/sdk` for official comparison  
**Impact:** Supply-chain API key harvesting + account takeover risk (orphaned namespace)  
**CVSS 3.1:** 7.4 (AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:N) — P3/P4  
**Channel:** npm Trust & Safety (primary) + Gladia security@gladia.io (secondary per scope.yml)

---

### 2. **SSRF via audio_url/video_url/callback_config.url** (api.gladia.io POST /v2/pre-recorded, /v2/live, legacy /video/text/video-transcription)
**Q1 Scope:** YES — api.gladia.io Highest priority  
**Q2 Reachable:** NO (unaauthenticated) / PARTIAL (low-priv) — All endpoints key-gated (401 without `x-gladia-key`). Requires valid API key.  
**Q3 Impact:** YES — Spec confirms `format:uri` with NO scheme allowlist; `/v1/models` exposes FR/US egress regions; 7 webhook delivery paths; NestJS backend likely follows redirects → cloud metadata (169.254.169.254), internal network access. High (with key).  
**Q4 Passive proof:** NO — Requires AUTH_HELPED (valid key) to send payloads and observe error_code/status/timing differences for reachability signal.  
**Q5 Novel:** YES — SSRF-by-design in spec (no scheme validation at schema level)  
**Q6 Not rejected:** YES — SSRF-to-cloud-metadata is HIGH-VALUE class  
**Q7 Triager accept:** CONDITIONAL — Would accept with PoC using valid key; unprovable without it  

**VERDICT: HOLD** — Needs valid `x-gladia-key` for PoC.  
**Next probe:** `POST https://api.gladia.io/v2/pre-recorded -H "x-gladia-key: <KEY>" -H "Content-Type: application/json" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/"}'` vs benign canary URL — compare `error_message`/`status`/duration

---

### 3. **WebSocket auth token in URL query parameter** (api.gladia.io `wss://api.gladia.io/v2/live?token=<uuid>`)
**Q1 Scope:** YES — api.gladia.io Highest  
**Q2 Reachable:** PARTIAL — Token only issued after authenticated POST /v2/live (requires valid key)  
**Q3 Impact:** YES — Bearer-equivalent token in URL leaks via Referer on WS upgrade, browser history, proxy/server logs. High if token is long-lived/session-scoped.  
**Q4 Passive proof:** NO — Requires AUTH_HELPED to init session, capture token, test Referer leakage on WS handshake, verify rotation/invalidation.  
**Q5 Novel:** YES — Design choice per OpenAPI spec  
**Q6 Not rejected:** YES — Token-in-URL is auth hygiene flaw  
**Q7 Triager accept:** CONDITIONAL — With PoC showing leakage  

**VERDICT: HOLD** — Needs valid key for session init + WS handshake inspection.  
**Next probe:** `POST https://api.gladia.io/v2/live -H "x-gladia-key: <KEY>" -d '{}'` → capture `response.url` token → open WS connection → inspect `Referer` header on upgrade → test token reuse after disconnect

---

### 4. **Post-auth open redirect via redirect_to** (app.gladia.io `/signin?redirect_to=`)
**Q1 Scope:** YES — app.gladia.io High  
**Q2 Reachable:** PARTIAL — `redirect_to` reflected into form action unauthenticated (confirmed), but post-auth honoring requires authenticated Google OAuth session  
**Q3 Impact:** MEDIUM — Post-auth redirect to attacker domain (phishing). OAuth `redirect_uri` is FIXED (PKCE S256) so no code/state theft. Return-to cookie tampering REJECTED (server resets).  
**Q4 Passive proof:** NO — Requires HUMAN_ONLY (complete Google OAuth flow with `redirect_to=https://evil.example.com`, capture final 302 Location)  
**Q5 Novel:** Reflection confirmed byte-fresh; post-auth behavior unverified  
**Q6 Not rejected:** YES — Open redirect is valid class  
**Q7 Triager accept:** CONDITIONAL — Needs post-auth PoC  

**VERDICT: HOLD** — Requires authenticated Google OAuth session.  
**Next probe:** HUMAN: Complete Google SSO with `?redirect_to=https://evil.example.com` (and `//evil.example.com`, `https://app.gladia.io.evil.example.com/` variants) → capture post-auth 302 Location + Set-Cookie

---

### 5. **CORS wildcard with x-gladia-key allowed** (api.gladia.io)
**Q1 Scope:** YES  
**Q2 Reachable:** YES — Public endpoints  
**Q3 Impact:** NO — `access-control-allow-origin: *` with `allow-headers: x-gladia-key` but **NO** `access-control-allow-credentials`. Only public endpoints (`/v1/models`, `/openapi.json`, `/health`) readable cross-origin. No credentialed data exposure.  
**Q4 Passive proof:** YES — Confirmed via OPTIONS/GET probes  
**Q5 Novel:** NO — Standard misconfig without credentials  
**Q6 Rejected:** YES — "Info disclosure of public data" / "best practice only" (no credential leakage)  
**Q7 Triager accept:** NO  

**VERDICT: INVALID** — Low impact, public data only, credentials blocked.

---

### 6. **Undocumented /health endpoint** (api.gladia.io)
**Q1 Scope:** YES  
**Q2 Reachable:** YES — Public, unauthenticated  
**Q3 Impact:** NO — Returns only `{"health":"OK"}` (15B). Tested `?full=true`, `?format=json`, `/actuator/health` — all return identical body or 404. No version/build/metadata leakage.  
**Q4 Passive proof:** YES  
**Q5 Novel:** NO — Benign health check  
**Q6 Rejected:** YES — "Info disclosure of public data"  
**Q7 Triager accept:** NO  

**VERDICT: INVALID** — Benign, no sensitive disclosure.

---

### 7. **Tech stack disclosure: x-powered-by: Express on CORS preflight only** (api.gladia.io)
**Q1 Scope:** YES  
**Q2 Reachable:** YES — OPTIONS preflight public  
**Q3 Impact:** LOW — Framework fingerprinting aids recon (targeted CVE scanning), no direct exploit  
**Q4 Passive proof:** YES — Confirmed: present on OPTIONS, absent on GET  
**Q5 Novel:** SLIGHTLY — Preflight-only differential  
**Q6 Rejected:** YES — "Info disclosure" / "best practice" (header hardening)  
**Q7 Triager accept:** NO — Typically informational  

**VERDICT: INVALID** — Informational only.

---

### 8. **IDOR on transcription file download /{id}/file** (api.gladia.io GET /v2/transcription/{id}/file, /v2/pre-recorded/{id}/file, /v2/live/{id}/file)
**Q1 Scope:** YES  
**Q2 Reachable:** PARTIAL — Key-gated; cross-account test requires two valid keys from different accounts  
**Q3 Impact:** HIGH — Unauthorized access to other users' transcription audio/text (PII)  
**Q4 Passive proof:** NO — Requires AUTH_HELPED with two keys  
**Q5 Novel:** Spec doesn't document ownership binding  
**Q6 Not rejected:** YES — IDOR/BOLA is HIGH-VALUE class  
**Q7 Triager accept:** CONDITIONAL — With cross-account PoC  

**VERDICT: HOLD** — Needs two valid API keys for cross-tenant test.

---

### 9. **Query-param parsing injection on /v1/history** (api.gladia.io GET /v1/history?custom_metadata=…&status[]=…&date=…)
**Q1 Scope:** YES  
**Q2 Reachable:** PARTIAL — Key-gated  
**Q3 Impact:** LOW-MEDIUM — Filter bypass / prototype pollution on own-tenant query (key-gated)  
**Q4 Passive proof:** NO — Requires AUTH_HELPED  
**Q5 Novel:** Complex query parsing surface (object + arrays in query string)  
**Q6 Not rejected:** YES  
**Q7 Triager accept:** CONDITIONAL — With PoC  

**VERDICT: HOLD** — Needs valid key for injection testing.

---

### 10. **return-to cookie unsigned base64url JSON** (app.gladia.io)
**Q1 Scope:** YES  
**Q2 Reachable:** YES — Cookie set on root  
**Q3 Impact:** NO — Tampering tested: server rejects and resets to default `{"url":"/"}`  
**Q4 Passive proof:** YES — Verified  
**Q5 Novel:** NO — Not a JWT despite appearance  
**Q6 Rejected:** YES — Tested and confirmed non-exploitable  
**Q7 Triager accept:** NO  

**VERDICT: INVALID** — Validated as non-exploitable (server-side validation/reset).

---

## SUMMARY

| # | Finding | Verdict | Proof Level | Next Action |
|---|---------|---------|-------------|-------------|
| 1 | npm `gladia@0.1.3` impersonation + key-in-URL | **VALID** | PASSIVE (complete) | Report to npm Trust & Safety + Gladia security |
| 2 | SSRF via audio_url/video_url/callback_url | **HOLD** | AUTH_HELPED | Need valid `x-gladia-key` for PoC |
| 3 | WS token in URL query param leakage | **HOLD** | AUTH_HELPED | Need valid key for session init |
| 4 | Post-auth open redirect via redirect_to | **HOLD** | HUMAN_ONLY | Need authenticated Google OAuth session |
| 5 | CORS wildcard + x-gladia-key | **INVALID** | PASSIVE | — |
| 6 | Undocumented /health endpoint | **INVALID** | PASSIVE | — |
| 7 | x-powered-by Express on preflight | **INVALID** | PASSIVE | — |
| 8 | IDOR on /{id}/file download | **HOLD** | AUTH_HELPED (2 keys) | Need two valid keys cross-account |
| 9 | Query-param injection /v1/history | **HOLD** | AUTH_HELPED | Need valid key |
| 10 | return-to cookie unsigned | **INVALID** | PASSIVE (tested) | — |

**Only one VALID, report-ready finding this cycle:** the npm `gladia@0.1.3` orphaned impersonation with API key leakage. All high-impact API findings (SSRF, IDOR, WS token leak, open redirect) are gated behind authentication/authorization and require manual validation with credentials the hunt does not possess.
