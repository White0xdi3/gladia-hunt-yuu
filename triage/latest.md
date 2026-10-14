===== TRIAGE 2026-10-14 00:28:25 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/scope.yml"[90m 1 match[0m
[0m✱ [0mGlob "**/*lead*"[90m 8 matches[0m
[0m→ [0mRead scope.yml
[0m→ [0mRead new-leads.txt
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
Based on my analysis of all lead files and the scope.yml, here are the triage verdicts for each distinct lead hypothesis:

---

### **LEAD 1: SSRF via audio_url/video_url/callback_url server-side fetch (api.gladia.io)**
**VERDICT: HOLD**
- Q1✓ In scope (api.gladia.io = HIGHEST)
- Q2✓ Attacker reachable with valid API key (self-serve trial available)
- Q3✓ Real impact: Cloud metadata (169.254.169.254), internal network access, data exfiltration via callback — **High**
- Q4✗ **FAIL** — Requires AUTH_HELPED (POST with valid `x-gladia-key`); cannot prove with GET/HEAD only per passive-first rule
- Q5✓ Novel (not previously reported)
- Q6✓ Not on rejected list
- Q7✓ Would accept *if proven*, but currently unproven
- **Reason**: Key-gated; needs program-provided or personal trial key to validate SSRF

---

### **LEAD 2: npm package `gladia@0.1.3` impersonation + API key leakage in WebSocket URLs (npm registry)**
**VERDICT: VALID**
- Q1✓ In scope (Official SDKs @gladiaio/sdk = MEDIUM; impersonation undermines official namespace)
- Q2✓ Public npm registry — anyone can `npm install gladia`
- Q3✓ **Real impact**: (a) Supply-chain impersonation — description claims "Official TypeScript SDK" but README says "Unofficial"; maintainer `softwarecitadel@gmail.com` (personal); repo `alexisbouchez/gladia.ts` returns 404 (orphaned, irrevocable takeover risk). (b) **Credential leakage** — `src/client.ts:306-308` embeds raw `x-gladia-key` in `wss://api.gladia.io/v2/live?x-gladia-key=<KEY>` query string, leaking keys to proxy/access logs, browser history, Referer headers.
- Q4✓ **PASSIVE proven** — `npm view gladia@0.1.3` metadata + tarball inspection + GitHub 404 all confirmed across 10+ independent cycles
- Q5✓ Novel — human-reported 2026-08-12, no vendor action yet
- Q6✓ Not on rejected list (supply-chain impersonation + credential exposure)
- Q7✓ Reasonable triager accepts — multiple models + human validation, report-ready
- **Minimal read-only proof**: 
  - `npm view gladia@0.1.3 description repository.url maintainer` → "Official TypeScript SDK" vs README "Unofficial"; maintainer personal; repo 404
  - Tarball `src/client.ts:306-308`: `wsUrl.searchParams.append('x-gladia-key', this.apiKey)` → `new WebSocket(wsUrl.toString())`
  - Official `@gladiaio/sdk` uses POST-then-token flow (no key in URL)
- **Impact**: Supply-chain compromise (developers install fake official SDK) + API key harvesting via WS URL logging → account takeover, billing fraud, audio data access
- **CVSS 3.1**: `AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N = 8.6 (High)` — or `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N = 7.5 (High)` for key exposure
- **Reporting channel**: Gladia security channel per scope.yml (https://gladia.io/bug-bounty-report → Google Forms) **AND** npm Trust & Safety (https://npmjs.com/support)

---

### **LEAD 3: Post-auth open redirect via redirect_to (app.gladia.io/signin)**
**VERDICT: HOLD**
- Q1✓ In scope (app.gladia.io = High)
- Q2✗ **HUMAN_ONLY** — Requires authenticated Google OAuth session to test post-auth `Location` header
- Q3✓ Medium impact — post-auth redirect to attacker domain enables phishing; OAuth `redirect_uri` is FIXED (PKCE S256) so no code theft
- Q4✗ **FAIL** — Cannot prove without completing OAuth flow (HUMAN_ONLY)
- Q5✓ Novel
- Q6✓ Not on rejected list
- Q7✓ Would accept *if confirmed*, but sole unverified gate is post-auth behavior
- **Reason**: Form-action reflection confirmed passively (`action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"`), CSP lacks `form-action` directive, but post-auth redirect untested without live session

---

### **LEAD 4: WebSocket auth token in URL query parameter (api.gladia.io/v2/live)**
**VERDICT: HOLD**
- Q1✓ In scope (api.gladia.io = HIGHEST)
- Q2✗ **AUTH_HELPED** — Needs valid key to POST `/v2/live` and observe `InitStreamingResponse.url` with `token=<uuid>`
- Q3✓ High impact — bearer token in URL leaks via Referer, browser history, proxy/server logs
- Q4✗ **FAIL** — Requires AUTH_HELPED
- Q5✓ Novel
- Q6✓ Not on rejected list
- Q7✓ Would accept if proven
- **Reason**: Key-gated; cannot validate token format/leakage vectors passively

---

### **LEAD 5: Undocumented /health endpoint (api.gladia.io)**
**VERDICT: INVALID**
- Q1✓ In scope
- Q2✓ Publicly reachable (GET /health → 200)
- Q3✗ **FAIL** — Returns only `{"health":"OK"}`; verbose probes (`?full=true`, `?format=json`, `/actuator/health`) all return identical minimal response — **no sensitive disclosure**
- Q4✓ Passive proven
- Q5✓ Documented
- Q6✗ **FAIL** — Info disclosure of trivial public health status is on always-rejected list
- Q7✗ Unlikely — reasonable triager rejects "health OK" as vulnerability

---

### **LEAD 6: CORS wildcard reflects arbitrary origin (api.gladia.io)**
**VERDICT: INVALID**
- Q1✓ In scope
- Q2✓ Public
- Q3✗ **FAIL** — Probes confirm **static `access-control-allow-origin: *`** (not Origin reflection); **no `access-control-allow-credentials`** → cross-origin reads only work for *public* endpoints (`/v1/models`, `/openapi.json`, `/health`). No credentialed data exposure.
- Q4✓ Passive proven
- Q5✓ Tested
- Q6✗ **FAIL** — Wildcard CORS without credentials on public API endpoints is standard/best practice, not a vulnerability
- Q7✗ Unlikely — reasonable triager rejects

---

### **LEAD 7: x-powered-by: Express on CORS preflight only (api.gladia.io)**
**VERDICT: INVALID**
- Q1✓ In scope
- Q2✓ Public OPTIONS
- Q3✗ **LOW** — Framework fingerprinting only (reconnaissance aid)
- Q4✓ Passive proven (OPTIONS has header, GET does not)
- Q5✓ Documented
- Q6✗ **FAIL** — Tech stack disclosure is on always-rejected list (info disclosure / best practice)
- Q7✗ Unlikely — reasonable triager treats as informational

---

### **LEAD 8: IDOR on transcription file download endpoints /{id}/file (api.gladia.io)**
**VERDICT: HOLD**
- Q1✓ In scope
- Q2✗ **AUTH_HELPED** — Needs valid key + another user's transcription ID
- Q3✓ High impact — cross-account access to PII/audio
- Q4✗ **FAIL** — Requires two accounts/keys to test cross-tenant isolation
- Q5✓ Hypothesized
- Q6✓ Not on rejected list
- Q7✓ Would accept if proven
- **Reason**: Spec shows 3 GET `/{id}/file` endpoints; ownership-binding logic opaque; cannot verify without authorized testing

---

### **LEAD 9: Query-param parsing injection on /v1/history (api.gladia.io)**
**VERDICT: HOLD**
- Q1✓ In scope
- Q2✗ **AUTH_HELPED** — Requires valid key
- Q3✓ Low-Medium — filter bypass / prototype pollution on **own-tenant** query only
- Q4✗ **FAIL** — Requires AUTH_HELPED
- Q5✓ Hypothesized
- Q6✓ Not on rejected list
- Q7✓ Would accept if proven (but low impact, same-tenant)
- **Reason**: Key-gated; `custom_metadata` (object, `additionalProperties:true`), `status`/`kind` (arrays) in query string — NestJS deep-parse surface

---

### **LEAD 10: OpenAPI shadow endpoints / undocumented v2 paths (api.gladia.io)**
**VERDICT: INVALID**
- Q1✓ In scope
- Q2✓ Public
- Q3✗ **FAIL** — Exhaustive probes: `/debug`, `/admin`, `/actuator/health`, `/metrics`, `/v1/*`, `/v2/live/init` all return 404. No shadow endpoints exist.
- Q4✓ Passive proven (negative result)
- Q5✗ Not novel — tested and negative
- Q7✗ No vulnerability to accept

---

### **LEAD 11: return-to cookie JWT parsing without signature verification (app.gladia.io)**
**VERDICT: INVALID**
- Q1✓ In scope
- Q2✓ Cookie set on root
- Q3✗ **FAIL** — Testing confirmed: server **rejects tampered cookie** and resets to default `{"url":"/"}`. No open redirect.
- Q4✓ Passive proven
- Q5✗ Tested and negative
- Q7✗ No vulnerability

---

## Summary

| Lead | Verdict | Key Blocking Factor |
|------|---------|---------------------|
| SSRF (audio_url/callback) | **HOLD** | Needs valid API key (AUTH_HELPED) |
| **npm gladia@0.1.3 impersonation + key leak** | **VALID** | **Fully proven passively — report ready** |
| Post-auth open redirect | **HOLD** | Needs human OAuth session (HUMAN_ONLY) |
| WS token in URL | **HOLD** | Needs valid API key (AUTH_HELPED) |
| /health endpoint | **INVALID** | Trivial disclosure only |
| CORS wildcard reflection | **INVALID** | Static `*`, no creds, public endpoints only |
| x-powered-by Express | **INVALID** | Info disclosure (rejected list) |
| IDOR /{id}/file | **HOLD** | Needs two accounts/keys (AUTH_HELPED) |
| /v1/history query injection | **HOLD** | Key-gated, low impact (AUTH_HELPED) |
| Shadow endpoints | **INVALID** | Probed — none exist |
| return-to cookie | **INVALID** | Tested — server validates/resets |

**Only one lead is immediately reportable: the npm `gladia@0.1.3` impersonation with credential leakage.** All high-impact API leads (SSRF, IDOR, WS token leak) are blocked by the program's passive-first / AUTH_HELPED constraints.
