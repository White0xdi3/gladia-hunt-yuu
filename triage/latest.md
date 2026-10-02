===== TRIAGE 2026-10-02 12:56:15 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
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
Based on my analysis of all lead files and the scope.yml, here are the triage verdicts for each unique lead against the 7-Question Gate:

---

### **LEAD 1: SSRF via audio_url/video_url/callback_url on api.gladia.io**
- **Q1 Scope**: YES — api.gladia.io (Highest priority)
- **Q2 Reachable**: YES — Public endpoint, but key-gated (requires valid `x-gladia-key`); low-priv (any API key holder)
- **Q3 Impact**: YES — Cloud metadata (169.254.169.254), internal network enumeration, data exfiltration via callback_url; **High severity**
- **Q4 Passive proof**: NO — Requires `AUTH_HELPED` (valid API key for POST /v2/pre-recorded); GET/HEAD cannot trigger server-side fetch
- **Q5 Novel**: YES — Consistent across 4 models, no prior report indicated
- **Q6 Not rejected**: YES — SSRF not on always-rejected list
- **Q7 Triager accept**: YES — Clear SSRF if proven with key
- **VERDICT: HOLD** — Cannot be proven with passive GET/HEAD only (Q4 fails)
- **Minimal proof**: `POST https://api.gladia.io/v2/pre-recorded -H "x-gladia-key: <valid_key>" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/","callback_url":"http://169.254.169.254/latest/meta-data/"}'` — compare error_message/status/duration vs benign URL
- **CVSS 3.1 (if proven)**: 7.5 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) — High
- **Channel**: Gladia security channel per scope.yml (disclosure_policy TBD)

---

### **LEAD 2: npm package `gladia@0.1.3` impersonation/typosquat + key-in-URL**
- **Q1 Scope**: YES — npm registry for Official SDKs (Medium priority); impersonation affects Gladia brand/users
- **Q2 Reachable**: YES — Public npm registry, anyone can `npm install gladia`
- **Q3 Impact**: YES — Supply chain compromise: developers install unofficial code believing it's official; **src/client.ts:306-308 embeds raw `x-gladia-key` in WebSocket URL query** (`wss://api.gladia.io/v2/live?x-gladia-key=<KEY>`) leaking keys to proxy/access logs/browser history; GitHub repo+user `alexisbouchez` 404 (orphaned/irrevocable takeover risk)
- **Q4 Passive proof**: YES — **Fully passive verified**: registry metadata (description="Official" vs README="Unofficial"), maintainer `softwarecitadel@gmail.com`, publish date 2025-03-28 (pre-dates `@gladiaio/sdk` 2025-09-09), tarball sha256 `3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2`, GitHub API 404 on user+repo
- **Q5 Novel**: YES — Human lead confirms reported 2026-08-12, no vendor action; package still live at dist-tag latest
- **Q6 Not rejected**: YES — Supply chain impersonation + credential hygiene not on rejected list
- **Q7 Triager accept**: YES — Clear impersonation with locked evidence across 10+ independent reproductions
- **VERDICT: VALID**
- **Impact**: Supply-chain API key harvesting + irrevocable account takeover risk; **P3/P4 severity**
- **CVSS 3.1**: 8.8 (AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N) — High
- **Channel**: Gladia security channel (https://gladia.io/bug-bounty-report → Google Forms, SSO-gated) + npm Trust & Safety (https://npmjs.com/support)

---

### **LEAD 3: Post-auth open redirect via `redirect_to` on app.gladia.io/signin**
- **Q1 Scope**: YES — app.gladia.io (High priority)
- **Q2 Reachable**: YES — Public `/signin` reflects `redirect_to` into form action (byte-fresh 100+ cycles), but **post-auth behavior requires authenticated Google OAuth session**
- **Q3 Impact**: LOW-MEDIUM — Phishing redirect after legitimate login; OAuth `redirect_uri` is FIXED (PKCE S256) preventing code/state theft; Google-only OAuth limits exploitability
- **Q4 Passive proof**: NO — Requires `HUMAN_ONLY` (complete Google OAuth flow with session, observe final 302 Location)
- **Q5 Novel**: YES — Consistent across models, unverified post-auth
- **Q6 Not rejected**: YES — Open redirect not rejected (though low impact)
- **Q7 Triager accept**: BORDERLINE — Low impact, requires auth + user interaction; many programs classify post-auth open redirects as Low/Informational
- **VERDICT: HOLD** — Cannot be proven passively (Q4 fails); Q7 borderline
- **Minimal proof**: `HUMAN: Authenticate via Google SSO → GET /signin?redirect_to=https://evil.example.com → complete OAuth → capture post-auth 302 Location`
- **CVSS 3.1 (if proven)**: 4.7 (AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N) — Medium

---

### **LEAD 4: WebSocket token in URL leakage (api.gladia.io/v2/live?token=<uuid>)**
- **Q1 Scope**: YES — api.gladia.io (Highest)
- **Q2 Reachable**: YES — Token issued via authenticated `POST /v2/live` (requires valid `x-gladia-key`)
- **Q3 Impact**: YES — Token in URL leaks via Referer headers, browser history, proxy/server logs; enables unauthorized live transcription sessions, real-time audio access; **High severity**
- **Q4 Passive proof**: NO — Requires `AUTH_HELPED` (valid key to init session and observe `InitStreamingResponse.url` token format)
- **Q5 Novel**: YES — Spec confirms token-in-URL design
- **Q6 Not rejected**: YES
- **Q7 Triager accept**: YES — Token-in-URL is recognized auth flaw
- **VERDICT: HOLD** — Cannot be proven with GET/HEAD only (Q4 fails)
- **Minimal proof**: `POST https://api.gladia.io/v2/live -H "x-gladia-key: <valid_key>" -d '{}' → observe response.url token format; initiate WS connection, inspect upgrade Referer header`
- **CVSS 3.1 (if proven)**: 7.5 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) — High

---

### **LEAD 5: Undocumented `/health` endpoint on api.gladia.io**
- **Q1 Scope**: YES — api.gladia.io
- **Q2 Reachable**: YES — Public `GET /health` returns 200 `{"health":"OK"}`
- **Q3 Impact**: NO — Returns static `{"health":"OK"}` only; probes `?full=true`, `?format=json` return identical output; no version/build/metadata disclosure
- **Q4 Passive proof**: YES — Already proven via GET
- **Q5 Novel**: YES — Not in OpenAPI spec
- **Q6 Not rejected**: **NO** — "Info disclosure of public data" is on always-rejected list; this is operational public data
- **Q7 Triager accept**: NO — Just health check, no sensitive data
- **VERDICT: INVALID** — Q3/Q6/Q7 fail (informational only)

---

### **LEAD 6: Tech stack disclosure via `x-powered-by: Express` on CORS preflight**
- **Q1 Scope**: YES — api.gladia.io
- **Q2 Reachable**: YES — Public `OPTIONS` preflight
- **Q3 Impact**: LOW — Framework fingerprinting aids reconnaissance only; no direct exploit
- **Q4 Passive proof**: YES — Proven via `OPTIONS` probe (present on preflight, absent on GET)
- **Q5 Novel**: YES
- **Q6 Not rejected**: BORDERLINE — "Best practice" / framework header disclosure often rejected as informational
- **Q7 Triager accept**: UNLIKELY — Most programs treat as Low/Informational
- **VERDICT: INVALID** — Q3/Q6/Q7 fail (informational)

---

### **LEAD 7: IDOR on transcription file download `/v2/transcription/{id}/file` (and `/pre-recorded`, `/live`)**
- **Q1 Scope**: YES — api.gladia.io
- **Q2 Reachable**: YES — Public endpoints but key-gated (requires valid `x-gladia-key`)
- **Q3 Impact**: YES — Cross-account access to transcription audio/text (PII, sensitive content); **High severity**
- **Q4 Passive proof**: NO — Requires `AUTH_HELPED` (valid key + another user's transcription ID)
- **Q5 Novel**: YES — Spec shows no ownership-binding logic
- **Q6 Not rejected**: YES
- **Q7 Triager accept**: YES — Clear IDOR if proven
- **VERDICT: HOLD** — Cannot be proven passively (Q4 fails)
- **Minimal proof**: `AUTH_HELPED: With valid key, POST /v2/transcription → GET /v2/transcription/{other_user_id}/file → observe 200 (IDOR) vs 403 (protected)`

---

### **LEAD 8: CORS wildcard reflects arbitrary origin**
- **Q1 Scope**: YES
- **Q2 Reachable**: YES
- **Q3 Impact**: NO — Probes confirm **static `access-control-allow-origin: *`** (no Origin reflection); no `access-control-allow-credentials`
- **Q4 Passive proof**: YES — Proven static wildcard
- **Q5 Novel**: NO — Disproven (was hypothesized, then rejected)
- **Q6 Not rejected**: N/A — Not a vulnerability
- **Q7 Triager accept**: NO — Standard wildcard without credentials is low-risk misconfig
- **VERDICT: INVALID** — Disproven; static wildcard not origin reflection

---

### **LEAD 9: return-to cookie JWT parsing without signature verification**
- **Q1 Scope**: YES — app.gladia.io
- **Q2 Reachable**: YES
- **Q3 Impact**: NO — **Disproven**: Server rejects tampered cookie and resets to default `{"url":"/"}`; no open redirect
- **Q4 Passive proof**: YES — Proven rejection via cookie tampering test
- **Q5 Novel**: N/A — Disproven
- **Q6 Not rejected**: N/A
- **Q7 Triager accept**: NO — Disproven
- **VERDICT: INVALID** — Disproven by passive testing

---

### **LEAD 10: OpenAPI shadow endpoints / undocumented v2 paths**
- **Q1 Scope**: YES
- **Q2 Reachable**: N/A
- **Q3 Impact**: N/A
- **Q4 Passive proof**: NO — **Disproven**: Probes for `/debug`, `/admin`, `/actuator/health`, `/v1/*`, `/metrics` all return 404; OpenAPI spec stable at 14 paths
- **Q5 Novel**: N/A — Disproven
- **Q6 Not rejected**: N/A
- **Q7 Triager accept**: NO — Disproven
- **VERDICT: INVALID** — Disproven by enumeration

---

### **SUMMARY**

| Lead | Verdict | Key Reason |
|------|---------|------------|
| SSRF via audio_url/callback_url | **HOLD** | Requires valid API key (AUTH_HELPED) |
| npm `gladia@0.1.3` impersonation | **VALID** | Fully passive proven; supply chain + key leak |
| Post-auth open redirect (redirect_to) | **HOLD** | Requires human OAuth session (HUMAN_ONLY) |
| WebSocket token in URL | **HOLD** | Requires valid API key (AUTH_HELPED) |
| Undocumented /health endpoint | **INVALID** | Info disclosure of public data (rejected) |
| x-powered-by Express on preflight | **INVALID** | Informational only |
| IDOR on /{id}/file download | **HOLD** | Requires valid key + cross-account test |
| CORS origin reflection | **INVALID** | Disproven (static wildcard) |
| return-to cookie JWT flaw | **INVALID** | Disproven (server resets) |
| OpenAPI shadow endpoints | **INVALID** | Disproven (no undocumented paths) |

**Only 1 lead is VALID and report-ready now**: **npm `gladia@0.1.3` impersonation** (Lead 2). The other high-value leads (SSRF, WebSocket token leak, IDOR) are **HOLD** pending authorized API key for `AUTH_HELPED` validation.
