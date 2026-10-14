===== TRIAGE 2026-10-14 12:11:13 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/*"[90m 54 matches[0m
[0m→ [0mRead scope.yml
[0m→ [0mRead probe-results.txt
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead probe-results.md
Now I have a comprehensive view. Let me apply the 7-Question Gate to each distinct lead across all models.

---

## LEAD TRIAGE VALIDATION (7-Question Gate)

### 1. SSRF via `audio_url`/`video_url`/`callback_url` server-side fetch → `api.gladia.io`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES — `api.gladia.io` is **Highest** priority per scope.yml |
| **Q2 Attacker reachable?** | PARTIAL — All endpoints are **key-gated** (401 without `x-gladia-key`). Attacker needs a valid API key. |
| **Q3 Real security impact?** | YES — Cloud metadata access (169.254.169.254), internal network enumeration, data exfiltration via callback. **High** severity *if* key obtained. |
| **Q4 Provable without invasive testing?** | **NO** — Requires `AUTH_HELPED` (valid `x-gladia-key`). Spec confirms `format:uri` with **no scheme allowlist**; `/v1/models` confirms FR/US egress; 7 webhook paths. But no passive PoC possible. |
| **Q5 Novel/unreported?** | YES — Design-level SSRF surface persists across 100+ cycles, unpatched. |
| **Q6 Not on rejected list?** | YES — SSRF is not auto-rejected. |
| **Q7 Triager would accept?** | YES — **But only with valid key for PoC**. |

**VERDICT: HOLD** — Cannot prove without valid API key.  
**→ [NEXT] PROBE (AUTH_HELPED):**  
`POST https://api.gladia.io/v2/pre-recorded -H "x-gladia-key: <VALID_KEY>" -H "Content-Type: application/json" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/","callback_url":"http://169.254.169.254/latest/meta-data/"}'`  
Compare `status`/`error_message`/duration vs benign canary URL. Repeat via `/video/text/video-transcription` with `video_url`.

---

### 2. npm package `gladia@0.1.3` impersonates official SDK + leaks API key in WebSocket URL

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES — Official SDKs (`@gladiaio/sdk`, `gladiaio-sdk`) are **Medium** priority. Impersonator on npm registry is supply-chain surface. |
| **Q2 Attacker reachable?** | YES — Public npm registry, `dist-tag: latest`, installable by any developer. |
| **Q3 Real security impact?** | YES — **Supply-chain impersonation**: description claims "Official TypeScript SDK" but README says "Unofficial"; maintainer `softwarecitadel@gmail.com` (personal); repo `alexisbouchez/gladia.ts` → **GitHub 404 (user+repo orphaned)**. Code at `src/client.ts:306-308` embeds raw `x-gladia-key` in `wss://api.gladia.io/v2/live?x-gladia-key=...` query string — keys leak in proxy/access logs, browser history. **Medium-High (P3/P4)**. |
| **Q4 Provable without invasive testing?** | **YES — PASSIVE complete.** Verified across 10+ independent `npm pack` reproductions: sha256 `3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2`, shasum `cc96f84a200c0fd49a71e919391f9b659c39f3e9`. GitHub API confirms user+repo 404 (irrevocable). |
| **Q5 Novel/unreported?** | YES — Human reported 2026-08-12 to `security@gladia.io` (awaiting response). Not yet resolved. |
| **Q6 Not on rejected list?** | YES — Supply-chain impersonation + credential hygiene flaw not on rejected list. |
| **Q7 Triager would accept?** | YES — Clear ownership anomaly + credential exposure in URL. |

**VERDICT: VALID** — **Report-ready**  
**Minimal passive proof:**  
1. `npm view gladia@0.1.3` → description "Official TypeScript SDK", repository `github.com/alexisbouchez/gladia.ts`, maintainer `softwarecitadel`  
2. `curl -s https://api.github.com/repos/alexisbouchez/gladia.ts` → **HTTP 404** (user+repo orphaned)  
3. Tarball inspection: `src/client.ts:306-308` → `searchParams.append('x-gladia-key', this.apiKey); new WebSocket(wsUrl.toString())`  
4. Contrast: Official `@gladiaio/sdk` uses POST `/v2/live` → short-lived `session.url` (no key in URL)  

**Impact:** Supply-chain API key harvesting + irrevocable account takeover risk (orphaned GitHub).  
**CVSS 3.1:** `7.1 (AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:N/A:N)`  
**Reporting channel:** Gladia Bug Bounty form (`https://gladia.io/bug-bounty-report` → Google Forms, SSO-gated) per scope.yml disclosure policy.

---

### 3. Post-auth open redirect via `redirect_to` → `app.gladia.io/signin`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES — `app.gladia.io` is **High** priority. |
| **Q2 Attacker reachable?** | PARTIAL — Unauthenticated GET reflects `redirect_to` URL-encoded into form `action` (confirmed 100+ cycles for `https://evil`, `//evil`, bare-host, confusing-subdomain, path-only). **But exploit requires post-auth session.** |
| **Q3 Real security impact?** | YES — If honored post-Google-OAuth: phishing redirect to attacker domain, potential OAuth state/code theft if `redirect_to` reused as `redirect_uri`. **Medium** (requires auth + user interaction). |
| **Q4 Provable without invasive testing?** | **NO** — Requires **HUMAN_ONLY** (valid Google SSO session). Passive reflection confirmed; post-auth `Location` header unobserved. |
| **Q5 Novel/unreported?** | YES — Reflection confirmed; post-auth behavior unknown. |
| **Q6 Not on rejected list?** | YES — Open redirect not auto-rejected. |
| **Q7 Triager would accept?** | CONDITIONAL — Only if post-auth redirect to external host confirmed. |

**VERDICT: HOLD** — Requires authenticated Google OAuth session to verify.  
**→ [NEXT] PROBE (HUMAN_ONLY):**  
Complete Google OAuth sign-in with `?redirect_to=https://evil.example.com` (also test `//evil.example.com`, `https://app.gladia.io.evil.example.com/`). Capture final **post-auth HTTP 302 Location** + `Set-Cookie`. Test if `redirect_to` is reused as OAuth `redirect_uri` injection.

---

### 4. WebSocket auth token in URL query parameter → `api.gladia.io/v2/live`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES — `api.gladia.io` Highest. |
| **Q2 Attacker reachable?** | PARTIAL — Token issued after `POST /v2/live` with valid `x-gladia-key`. Token in `wss://api.gladia.io/v2/live?token=<uuid>` leaks via Referer, proxy logs, browser history. |
| **Q3 Real security impact?** | YES — Bearer-equivalent token enables unauthorized live transcription sessions, real-time audio access. **High**. |
| **Q4 Provable without invasive testing?** | PARTIAL — Spec confirms token-in-URL design. Need `AUTH_HELPED` to confirm token is long-lived/session-scoped, no rotation on disconnect, `Referrer-Policy` on WS upgrade. |
| **Q5 Novel/unreported?** | YES — Documented in OpenAPI but not reported as flaw. |
| **Q6 Not on rejected list?** | YES. |
| **Q7 Triager would accept?** | CONDITIONAL — If token confirmed bearer-equivalent + long-lived. |

**VERDICT: HOLD** — Needs `AUTH_HELPED` to confirm token properties.  
**→ [NEXT] PROBE (AUTH_HELPED):**  
`POST https://api.gladia.io/v2/live -H "x-gladia-key: <VALID_KEY>" -H "Content-Type: application/json" -d '{}'` → observe `response.url` token format. Initiate WS connection, inspect upgrade request headers for `Referer`. Test token reuse after session close.

---

### 5. Undocumented `/health` endpoint → `api.gladia.io`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES |
| **Q2 Attacker reachable?** | YES — Public, unauthenticated, returns 200 `{"health":"OK"}`. |
| **Q3 Real security impact?** | **NO** — No verbose mode (`?full=true`, `?format=json` return identical output). No version/build/metadata disclosure. **Low** at best. |
| **Q4 Provable without invasive testing?** | YES — Passive confirmed. |
| **Q5 Novel/unreported?** | YES — Absent from OpenAPI spec. |
| **Q6 Not on rejected list?** | **BORDERLINE** — "Info disclosure of public data" / best practice. |
| **Q7 Triager would accept?** | **NO** — Negligible impact. |

**VERDICT: INVALID** — Low-severity info disclosure, rejected per always-rejected list.

---

### 6. Tech stack disclosure: `x-powered-by: Express` on CORS preflight only → `api.gladia.io`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES |
| **Q2 Attacker reachable?** | YES — `OPTIONS` preflight returns header; absent on `GET`. |
| **Q3 Real security impact?** | **LOW** — Framework fingerprinting aids CVE targeting only. |
| **Q4 Provable without invasive testing?** | YES — Passive confirmed. |
| **Q5 Novel/unreported?** | Known. |
| **Q6 Not on rejected list?** | **NO** — "Best practice" / info disclosure, Low severity. |
| **Q7 Triager would accept?** | **NO** — Standalone not acceptable. |

**VERDICT: INVALID** — Best-practice misconfig, not a vulnerability.

---

### 7. IDOR on transcription file download `/{id}/file` → `api.gladia.io`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES |
| **Q2 Attacker reachable?** | PARTIAL — Key-gated + needs valid transcription UUID from another account. |
| **Q3 Real security impact?** | YES — Cross-tenant PII/audio access. **High** if proven. |
| **Q4 Provable without invasive testing?** | **NO** — Requires `AUTH_HELPED` with **two valid API keys** (different accounts). |
| **Q5 Novel/unreported?** | Spec shows no ownership-binding property. |
| **Q6 Not on rejected list?** | YES. |
| **Q7 Triager would accept?** | CONDITIONAL — Only with cross-account PoC. |

**VERDICT: HOLD** — Needs `AUTH_HELPED` with two accounts.  
**→ [NEXT] PROBE (AUTH_HELPED):**  
With Key A: `POST /v2/pre-recorded` → get `id`. With Key B: `GET /v2/pre-recorded/{id}/file` → observe 200 (IDOR) vs 403/404 (protected).

---

### 8. Query-param parsing injection on `/v1/history` → `api.gladia.io`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES |
| **Q2 Attacker reachable?** | PARTIAL — Key-gated. |
| **Q3 Real security impact?** | LOW-MEDIUM — Filter bypass / prototype pollution on **own-tenant** query only. |
| **Q4 Provable without invasive testing?** | **NO** — Requires `AUTH_HELPED`. |
| **Q5 Novel/unreported?** | Spec shows `custom_metadata` (object, `additionalProperties:true`), `status`/`kind` arrays, date filters in query string. |
| **Q6 Not on rejected list?** | YES. |
| **Q7 Triager would accept?** | UNLIKELY — Low confidence (48%), own-tenant only, needs key. |

**VERDICT: HOLD** — Low priority, needs `AUTH_HELPED`.

---

### 9. CORS wildcard reflects arbitrary Origin → `api.gladia.io`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES |
| **Q2 Attacker reachable?** | YES — Public endpoints. |
| **Q3 Real security impact?** | **NO** — Probe confirms **static `access-control-allow-origin: *`** (not Origin reflection). No `access-control-allow-credentials`. Cross-origin reads of public endpoints (`/v1/models`, `/openapi.json`, `/health`) only. |
| **Q4 Provable without invasive testing?** | YES — Passive confirmed static `*`. |
| **Q5 Novel/unreported?** | N/A — Hypothesis disproven. |
| **Q6 Not on rejected list?** | N/A |
| **Q7 Triager would accept?** | **NO** — Disproven. |

**VERDICT: INVALID** — Hypothesis rejected by probe (static `*`, no reflection, no credentials).

---

### 10. `return-to` cookie JWT parsing without signature verification → `app.gladia.io`

| Q | Answer |
|---|--------|
| **Q1 In scope?** | YES |
| **Q2 Attacker reachable?** | YES — Cookie set on root. |
| **Q3 Real security impact?** | **NO** — Probe confirms: cookie is **unsigned base64url JSON** (`{"url":"/"}`), server **rejects tampered value and resets to default**. No open redirect via cookie. |
| **Q4 Provable without invasive testing?** | YES — Passive confirmed. |
| **Q5 Novel/unreported?** | N/A — Disproven. |
| **Q6 Not on rejected list?** | N/A |
| **Q7 Triager would accept?** | **NO** — Server validates/resets. |

**VERDICT: INVALID** — Hypothesis rejected by probe (server-side validation confirmed).

---

## SUMMARY

| Lead | Verdict | Next Action |
|------|---------|-------------|
| **SSRF via audio_url/video_url/callback_url** | **HOLD** | `[NEXT] PROBE (AUTH_HELPED)` — POST `/v2/pre-recorded` with metadata URL + valid key |
| **npm `gladia@0.1.3` impersonation + key-in-URL** | **VALID** | **REPORT NOW** — Passive proof complete; submit via Gladia Bug Bounty form |
| **Post-auth open redirect (`redirect_to`)** | **HOLD** | `[NEXT] PROBE (HUMAN_ONLY)` — Complete Google OAuth with redirect_to, capture post-auth Location |
| **WS token in URL query param** | **HOLD** | `[NEXT] PROBE (AUTH_HELPED)` — Init live session, inspect token properties |
| Undocumented `/health` | **INVALID** | — |
| `x-powered-by: Express` on preflight | **INVALID** | — |
| IDOR on `/{id}/file` | **HOLD** | `[NEXT] PROBE (AUTH_HELPED)` — Requires two valid keys |
| Query-param injection `/v1/history` | **HOLD** | Low priority, needs `AUTH_HELPED` |
| CORS Origin reflection | **INVALID** | — (disproven: static `*`) |
| `return-to` cookie JWT flaw | **INVALID** | — (disproven: server validates/resets) |

---

**TOP PRIORITY FOR REPORTING:** **Lead #2 (npm impersonation)** — Only fully passive, report-ready finding with clear supply-chain impact. Human already submitted 2026-08-12; follow-up due 2026-08-26.
