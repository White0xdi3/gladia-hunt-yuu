===== TRIAGE 2026-10-03 21:31:00 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/scope.yml"[90m 1 match[0m
[0m✱ [0mGlob "**/leads*"[90m 0 matches[0m
[0m→ [0mRead scope.yml
[0m✱ [0mGlob "**/*.yml"[90m 1 match[0m
[0m✱ [0mGlob "**/*.md"[90m 21 matches[0m
[0m→ [0mRead probe-results.md
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead inventory/gladia.md
Now I have all the leads and probe results. Let me evaluate each distinct lead against the 7-Question Gate.
Now I have all the data. Let me evaluate each distinct lead against the 7-Question Gate.

---

### LEAD 1: SSRF via `audio_url`/`video_url`/`callback_url` server-side fetch
**Asset:** `api.gladia.io` (HIGHEST scope) — `POST /v2/pre-recorded`, `POST /v2/live`, legacy `/audio/text/audio-transcription`, `/video/text/video-transcription`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES — `api.gladia.io` is HIGHEST priority asset |
| **Q2 Attacker reachable?** | PARTIAL — All endpoints are **key-gated** (401 without `x-gladia-key`). Requires valid API key (AUTH_HELPED). Not public/unauthenticated. |
| **Q3 Real security impact?** | YES — Cloud metadata access (169.254.169.254), internal network enumeration, data exfiltration via callback_url. **High severity if key obtained**. |
| **Q4 Provable without invasive testing?** | NO — Requires valid API key to test (AUTH_HELPED). Passive probes only show 401. |
| **Q5 Novel/unreported?** | YES — Design-level SSRF surface (no scheme allowlist in OpenAPI `CallbackConfigDto.url`, `audio_url`, `video_url` all `format:uri` with no pattern/enum). Confirmed frozen across 100+ cycles. |
| **Q6 Not on always-rejected list?** | YES — Not info disclosure, not self-XSS, not rate-limit alone. SSRF is explicitly HIGH-VALUE class per directives. |
| **Q7 Triager would accept?** | CONDITIONAL — Only with valid API key for PoC. Without key: **HOLD (AUTH_HELPED gate)**. With key + confirmed internal fetch: **VALID**. |

**Verdict: HOLD** — *High-value SSRF-by-design surface confirmed by spec+RAG, but key-gated (AUTH_HELPED). Cannot prove exploitation without program-provided or trial `x-gladia-key`. Next step requires authorized key.*

---

### LEAD 2: npm `gladia@0.1.3` orphaned impersonation + raw API key in WebSocket URL
**Asset:** npm registry `gladia@0.1.3` (dist-tag `latest`) — **NOT an official Gladia asset** but supply-chain risk to Gladia users

| Q | Answer |
|---|--------|
| **Q1 In scope?** | DEBATABLE — Scope lists "Official SDKs (npm @gladiaio/sdk, PyPI gladiaio-sdk)" as MEDIUM. This is an **unofficial/impersonating** package. Not a Gladia-owned asset. However, it directly impacts Gladia users by harvesting their API keys. |
| **Q2 Attacker reachable?** | YES — Public npm registry, `dist-tag latest=0.1.3`, installable by anyone `npm i gladia`. |
| **Q3 Real security impact?** | YES — (1) **Impersonation**: `package.json` claims "Official TypeScript SDK for Gladia" but README says "Unofficial"; maintainer `softwarecitadel@gmail.com` (personal); repo `alexisbouchez/gladia.ts` returns **404 (user+repo both gone)** — orphaned, irrevocable takeover risk. (2) **Credential exposure**: `src/client.ts:306-308` does `wsUrl.searchParams.append('x-gladia-key', this.apiKey)` then `new WebSocket(wsUrl.toString())` — raw API key embedded in `wss://api.gladia.io/v2/live?x-gladia-key=...` query string, leaking to proxy/logs/browser history. Official `@gladiaio/sdk` uses POST-then-token flow (header auth, then short-lived session URL). |
| **Q4 Provable without invasive testing?** | YES — **Fully passive**: `npm view gladia@0.1.3` metadata, tarball inspection (sha256 `3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2` reproduced 10+ independent times), GitHub API 404 on user+repo. |
| **Q5 Novel/unreported?** | YES — Independently verified across 5+ models, 100+ cycles. Human already reported 2026-08-12 but **no vendor action yet** (per `lead-human.md`). |
| **Q6 Not on always-rejected list?** | YES — Supply-chain impersonation + credential leakage is not "info disclosure of public data" or "best practice". |
| **Q7 Triager would accept?** | YES for **npm Trust & Safety venue** (impersonation policy). For **Gladia program venue**: CONDITIONAL — only if `wss://api.gladia.io/v2/live` actually accepts `x-gladia-key` as query param (legacy compat). If WS rejects query-param auth, the fake SDK leaks keys to an endpoint that never accepts them (broken SDK, not Gladia vuln). **Needs 1 valid key to prove Gladia-side impact.** |

**Verdict: VALID (npm venue) / HOLD (Gladia venue pending WS query-param auth test)**
- **Minimal proof**: `npm view gladia@0.1.3` + tarball `src/client.ts:307` + GitHub 404 on `alexisbouchez` user+repo.
- **Impact**: Supply-chain API key harvesting + irrevocable account takeover risk (orphaned package at `latest`).
- **CVSS 3.1**: `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:N` (7.1 High) — for npm impersonation + key leakage.
- **Reporting channel**: **npm Trust & Safety** (primary, via `npmjs.com/support`) + **Gladia security channel** (secondary, conditional on WS query-param test).

---

### LEAD 3: Post-auth open redirect via `redirect_to` parameter on `/signin`
**Asset:** `app.gladia.io` (HIGH scope) — `GET /signin?redirect_to=https://evil.example.com`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES — `app.gladia.io` is HIGH priority asset |
| **Q2 Attacker reachable?** | PARTIAL — Reflection is **unauthenticated** (GET returns 200 with `action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"` reflected). But **exploitation requires post-auth redirect** (Google OAuth flow completion). |
| **Q3 Real security impact?** | CONDITIONAL — If server honors `redirect_to` after Google OAuth, enables phishing redirect to attacker domain. OAuth `redirect_uri` is **FIXED** (PKCE S256, `https://app.gladia.io/auth/google/callback`) — prevents code/state theft. CSP has **0 `form-action` directives** (gap confirmed). Impact: **Medium (phishing)**. |
| **Q4 Provable without invasive testing?** | NO — Passive confirms reflection into form action. **Post-auth behavior unobservable without valid Google SSO session (HUMAN_ONLY).** |
| **Q5 Novel/unreported?** | YES — Confirmed byte-fresh across 100+ cycles. Reflection into form action for all variant classes (`https://`, `//`, bare-host, confusing-subdomain `app.gladia.io.evil`, path-only). |
| **Q6 Not on always-rejected list?** | YES — Open redirect is not "self-XSS" or "info disclosure". |
| **Q7 Triager would accept?** | CONDITIONAL — Only with authenticated session proving post-auth 302 to external host. Without: **HOLD (HUMAN_ONLY gate)**. |

**Verdict: HOLD** — *Reflection confirmed passive; post-auth honoring unverified (requires human Google SSO session). OAuth redirect_uri FIXED prevents code theft. CSP form-action gap confirmed.*

---

### LEAD 4: WebSocket auth token in URL query parameter (`wss://api.gladia.io/v2/live?token=<uuid>`)
**Asset:** `api.gladia.io` (HIGHEST) — per OpenAPI `InitStreamingResponse.url`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES — `api.gladia.io` HIGHEST |
| **Q2 Attacker reachable?** | PARTIAL — Token issued only after authenticated `POST /v2/live` (requires `x-gladia-key`). Token in URL leaks via Referer, browser history, proxy logs, TLS-terminating logs. |
| **Q3 Real security impact?** | YES — Token theft → unauthorized live transcription sessions, real-time audio access. **High severity**. |
| **Q4 Provable without invasive testing?** | NO — Requires valid API key to initiate session and observe token format (AUTH_HELPED). Passive only sees 401. |
| **Q5 Novel/unreported?** | YES — Design per OpenAPI spec. |
| **Q6 Not on always-rejected list?** | YES — Token-in-URL is credential leakage class. |
| **Q7 Triager would accept?** | CONDITIONAL — With valid key + observed token in URL + Referer leakage: **VALID**. Without key: **HOLD**. |

**Verdict: HOLD** — *Spec-confirmed design flaw (token in URL query). Needs AUTH_HELPED to prove token format, lifetime, Referer-Policy on WS upgrade.*

---

### LEAD 5: Undocumented `/health` endpoint on `api.gladia.io`
**Asset:** `api.gladia.io` — `GET /health` returns `200 {"health":"OK"}`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES |
| **Q2 Attacker reachable?** | YES — Public, unauthenticated, CORS `*`. |
| **Q3 Real security impact?** | LOW — Returns only `{"health":"OK"}`. Probes `?full=true`, `?format=json`, `/actuator/health` all return identical minimal output. No version/build/dependency leakage. |
| **Q4 Provable without invasive testing?** | YES — Passive GET confirmed. |
| **Q5 Novel/unreported?** | YES — Not in OpenAPI spec (14 paths). |
| **Q6 Not on always-rejected list?** | **NO** — This is **info disclosure of minimal public data** (health check). Always-rejected: "info disclosure of public data", "best practice". |
| **Q7 Triager would accept?** | NO — Low-risk informational only. |

**Verdict: INVALID** — *Undocumented but leaks no sensitive data. Rejected per Q6 (always-rejected: info disclosure of public data).*

---

### LEAD 6: CORS wildcard + `x-powered-by: Express` on preflight only
**Asset:** `api.gladia.io` — OPTIONS preflight returns `access-control-allow-origin: *`, `x-powered-by: Express`; GET does not.

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES |
| **Q2 Attacker reachable?** | YES — Public preflight. |
| **Q3 Real security impact?** | LOW — Framework fingerprinting aids targeted CVE scanning. No credential leakage (`access-control-allow-credentials` absent). Wildcard is static `*`, not Origin reflection. |
| **Q4 Provable without invasive testing?** | YES — Passive OPTIONS/GET confirmed. |
| **Q5 Novel/unreported?** | YES — Preflight-only header differential confirmed. |
| **Q6 Not on always-rejected list?** | **NO** — "Best practice" / "tech stack disclosure" alone is always-rejected. Low risk. |
| **Q7 Triager would accept?** | NO — Informational only. |

**Verdict: INVALID** — *Framework fingerprinting via preflight-only header is low-risk best-practice finding. Rejected per Q6.*

---

### LEAD 7: IDOR on transcription file download `/{id}/file`
**Asset:** `api.gladia.io` — `GET /v2/transcription/{id}/file`, `/v2/pre-recorded/{id}/file`, `/v2/live/{id}/file`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES |
| **Q2 Attacker reachable?** | NO — All endpoints **key-gated** (401 without `x-gladia-key`). Requires valid key + valid transcription ID owned by another user. |
| **Q3 Real security impact?** | HIGH (if proven) — Cross-tenant PII/audio access. |
| **Q4 Provable without invasive testing?** | NO — Requires valid key + cross-account test (AUTH_HELPED). |
| **Q5 Novel/unreported?** | UNKNOWN — Spec doesn't expose ownership-binding logic. |
| **Q6 Not on always-rejected list?** | YES — IDOR is HIGH-VALUE class. |
| **Q7 Triager would accept?** | CONDITIONAL — Only with valid key proving cross-account access. Without: **HOLD**. |

**Verdict: HOLD** — *Spec-only hypothesis. Needs AUTH_HELPED with valid key to test cross-account resource isolation.*

---

### LEAD 8: Query-param parsing injection on `/v1/history` (`custom_metadata` object, `status`/`kind` arrays)
**Asset:** `api.gladia.io` — `GET /v1/history` (key-gated)

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES |
| **Q2 Attacker reachable?** | NO — Key-gated (401). |
| **Q3 Real security impact?** | LOW-MEDIUM — Prototype pollution / filter bypass on own-tenant query. Key-gated limits blast radius. |
| **Q4 Provable without invasive testing?** | NO — Requires key + injection payloads (AUTH_HELPED). |
| **Q5 Novel/unreported?** | YES — Complex query parsing surface (`additionalProperties:true` object + arrays in query string). |
| **Q6 Not on always-rejected list?** | YES — Injection class. |
| **Q7 Triager would accept?** | CONDITIONAL — Only with key + 500/altered results. Without: **HOLD**. |

**Verdict: HOLD** — *Key-gated query parsing anomaly. Needs AUTH_HELPED.*

---

### LEAD 9: `return-to` cookie unsigned base64url JSON (no JWT signature)
**Asset:** `app.gladia.io` — `return-to=eyJ1cmwiOiIvIn0%3D` decodes to `{"url":"/"}`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES |
| **Q2 Attacker reachable?** | YES — Cookie set on root `/`. |
| **Q3 Real security impact?** | NONE — **Server rejects tampered value and resets to default** (confirmed by multiple models). No open redirect via cookie tampering. |
| **Q4 Provable without invasive testing?** | YES — Passive tamper test confirmed reset. |
| **Q5 Novel/unreported?** | N/A — No vuln. |
| **Q6 Not on always-rejected list?** | N/A |
| **Q7 Triager would accept?** | NO — Explicitly **REJECTED** by nemotron3, bigpickle, laguna, mimo after validation. |

**Verdict: INVALID** — *Server-side validation resets tampered cookie. No open redirect via this vector.*

---

### LEAD 10: Undocumented `/v2/live/health` endpoint (key-gated 401)
**Asset:** `api.gladia.io` — Discovered 2026-08-18, returns 401 NestJS, not in 14-path OpenAPI spec

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES |
| **Q2 Attacker reachable?** | NO — Key-gated (401). |
| **Q3 Real security impact?** | NONE — Just another health endpoint behind auth. |
| **Q4 Provable without invasive testing?** | YES — Passive GET shows 401. |
| **Q5 Novel/unreported?** | YES — Undocumented. |
| **Q6 Not on always-rejected list?** | **NO** — Info disclosure of auth-gated endpoint existence. |
| **Q7 Triager would accept?** | NO. |

**Verdict: INVALID** — *Auth-gated undocumented health endpoint. No impact.*

---

## SUMMARY

| Lead | Verdict | Reason |
|------|---------|--------|
| **SSRF via audio_url/video_url/callback_url** | **HOLD** | High-value SSRF-by-design confirmed by spec+RAG; key-gated (AUTH_HELPED). Needs valid `x-gladia-key` for PoC. |
| **npm `gladia@0.1.3` orphaned impersonation + key-in-URL** | **VALID (npm venue)** / **HOLD (Gladia venue)** | Fully passive proof: impersonation metadata + tarball key leakage + orphaned repo (404). Report to **npm Trust & Safety** now. Gladia venue conditional on WS query-param auth test. |
| **Post-auth open redirect via `redirect_to`** | **HOLD** | Reflection confirmed passive; post-auth honoring requires human Google SSO session (HUMAN_ONLY). OAuth redirect_uri FIXED prevents code theft. |
| **WebSocket token in URL query** | **HOLD** | Spec-confirmed design flaw; needs AUTH_HELPED to prove token format/leakage. |
| **Undocumented `/health` endpoint** | **INVALID** | Leaks only `{"health":"OK"}` — always-rejected info disclosure. |
| **CORS wildcard + Express fingerprint** | **INVALID** | Best-practice/tech-stack disclosure only. |
| **IDOR on `/{id}/file`** | **HOLD** | Spec-only; needs AUTH_HELPED with valid key for cross-account test. |
| **Query-param injection `/v1/history`** | **HOLD** | Key-gated; needs AUTH_HELPED. |
| **`return-to` cookie unsigned** | **INVALID** | Server validates/resets — explicitly rejected by all models. |
| **Undocumented `/v2/live/health`** | **INVALID** | Auth-gated, no impact. |

---

### IMMEDIATELY ACTIONABLE (VALID)
**Lead 2 (npm venue): `gladia@0.1.3` orphaned impersonation + API key leakage**
- **Proof**: `npm view gladia@0.1.3` → description "Official", maintainer `softwarecitadel@gmail.com`, repo `alexisbouchez/gladia.ts` (GitHub user+repo 404), tarball `src/client.ts:307` `searchParams.append('x-gladia-key', apiKey)` → WebSocket URL query.
- **Impact**: Supply-chain key harvesting + irrevocable takeover (orphaned at `latest`).
- **CVSS 3.1**: `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:N` (7.1 High)
- **Channel**: **npm Trust & Safety** (`https://www.npmjs.com/support`) — primary. Gladia security channel (via `https://gladia.io/bug-bounty-report` → Google Forms) — secondary, conditional.

---

### [NEXT] PROBE REQUESTS (read-only, for next cycle)
If you can provide a valid `x-gladia-key` (program-provided or trial), these AUTH_HELPED probes would unblock HOLD leads:

1. **SSRF PoC**:
   ```
   POST https://api.gladia.io/v2/pre-recorded
   Headers: x-gladia-key: <VALID_KEY>, Content-Type: application/json
   Body: {"audio_url":"http://169.254.169.254/latest/meta-data/","callback_url":"http://169.254.169.254/latest/meta-data/"}
   ```
   Compare `status`/`error_message`/duration vs benign control URL.

2. **WebSocket token observation**:
   ```
   POST https://api.gladia.io/v2/live
   Headers: x-gladia-key: <VALID_KEY>, Content-Type: application/json
   Body: {}
   ```
   Observe `response.url` → `wss://api.gladia.io/v2/live?token=<uuid>` format; initiate WS and inspect upgrade `Referer` header.

3. **IDOR test** (needs two accounts or known other-user transcription ID):
   ```
   GET https://api.gladia.io/v2/transcription/<OTHER_USER_ID>/file
   Headers: x-gladia-key: <YOUR_VALID_KEY>
   ```
   Observe 200 (IDOR) vs 403/404 (protected).

4. **Query-param injection** `/v1/history`:
   ```
   GET https://api.gladia.io/v1/history?custom_metadata[__proto__][x]=1
   Headers: x-gladia-key: <VALID_KEY>
   ```
   Observe 500/timing skew vs baseline.

5. **Post-auth redirect_to test** (HUMAN_ONLY):
   - Authenticate via Google SSO on `app.gladia.io`
   - Visit `/signin?redirect_to=https://evil.example.com` post-auth
   - Capture final 302 `Location` header.

Without a valid key, only **Lead 2 (npm venue)** is reportable today.
