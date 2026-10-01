===== TRIAGE 2026-10-01 06:14:49 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/*"[90m 51 matches[0m
[0m→ [0mRead scope.yml
[0m→ [0mRead probe-results.txt
[0m→ [0mRead probe-results.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-nemotron3.md
Now I have all the leads. Let me consolidate the unique findings and apply the 7-Question Gate to each.

---

### **FINDING 1: npm `gladia`@0.1.3 orphaned impersonation + API key in WebSocket URL**

**Asset:** npm registry `gladia` package (dist-tag latest=0.1.3) — **Medium** per scope.yml (Official SDKs)

| Q | Answer |
|---|--------|
| Q1 Scope | YES — Official SDKs (npm @gladiaio/sdk, PyPI gladiaio-sdk) are Medium priority. This is a name-squat on the unscoped `gladia` name impersonating the official SDK. |
| Q2 Reachability | YES — Public npm registry, anyone can `npm install gladia`. |
| Q3 Impact | YES — **Supply-chain impersonation**: description claims "Official TypeScript SDK for Gladia" but README says "Unofficial"; maintainer `softwarecitadel@gmail.com` (personal); repo `alexisbouchez/gladia.ts` returns **404 (user+repo both gone = orphaned/irrevocable)**. **Credential exposure**: source `src/client.ts:306-308` does `wsUrl.searchParams.append('x-gladia-key', apiKey)` then `new WebSocket(wsUrl.toString())` — raw API key embedded in `wss://api.gladia.io/v2/live?x-gladia-key=<KEY>` query string. Keys leak via TLS-terminating proxy logs, server access logs, browser history, Referer headers, URL sharing. |
| Q4 Proof (passive) | YES — All evidence from passive registry metadata + tarball inspection + GitHub API 404 + source code review (RAG). `npm view gladia@0.1.3` + `npm pack` + `tar -xzf` confirms sha256 `3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2`, shasum `cc96f84a200c0fd49a71e919391f9b659c39f3e9`. |
| Q5 Novelty | YES — Not previously reported to Gladia or npm. |
| Q6 Not rejected | YES — Not info-disclosure-of-public-data, not best-practice, not rate-limit, not self-XSS. This is active supply-chain impersonation + credential hygiene flaw. |
| Q7 Triager accept | YES — Clear policy violation (impersonation) + measurable credential exposure design flaw. |

**VERDICT: VALID**

**Minimal read-only proof:**
1. `npm view gladia@0.1.3 description repository.url maintainer dist-tags` → shows "Official TypeScript SDK for Gladia", repo `github.com/alexisbouchez/gladia.ts`, maintainer `softwarecitadel@gmail.com`, latest=0.1.3
2. `curl -s https://api.github.com/repos/alexisbouchez/gladia.ts` → HTTP 404 (repo gone)
3. `curl -s https://api.github.com/users/alexisbouchez` → HTTP 404 (user gone)
4. `npm pack gladia@0.1.3 && tar -xzf gladia-0.1.3.tgz && cat package/src/client.ts | grep -n "x-gladia-key"` → line 307: `wsUrl.searchParams.append('x-gladia-key', this.apiKey)`

**Impact:** Supply-chain takeover risk (orphaned account can be claimed) + API key harvesting via WebSocket URL logging. **CVSS 3.1: 7.1 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:N)** — Medium-High.

**Reporting channel:** **Dual-track** — (1) npm Trust & Safety (`npmjs.com/support` — impersonation + abandoned package policy), (2) Gladia security (`security@gladia.io` or `https://gladia.io/bug-bounty-report`) — for the credential-in-URL design flaw *if* `wss://api.gladia.io/v2/live?x-gladia-key=<KEY>` is accepted by the server (needs 1 valid key to confirm; if rejected, it's only an npm issue).

---

### **FINDING 2: SSRF-by-design via `audio_url`/`video_url`/`callback_config.url` (api.gladia.io)**

**Asset:** `api.gladia.io` — **Highest** per scope.yml

| Q | Answer |
|---|--------|
| Q1 Scope | YES — api.gladia.io is Highest priority. |
| Q2 Reachability | **CONDITIONAL** — Endpoints (`/v2/pre-recorded`, `/v2/upload`, `/v2/live`, legacy `/audio/text/audio-transcription`, `/video/text/video-transcription`) are **key-gated (401 without `x-gladia-key`)**. Attacker needs a valid API key. Program-provided trial key or personal account required. |
| Q3 Impact | YES — **High**. OpenAPI spec confirms `audio_url`, `video_url`, `callback_config.url` all `format:uri` with **no scheme allowlist/pattern**. `/v1/models` reveals egress regions FR/US. Server-side fetch of attacker-controlled URLs (including `http://169.254.169.254/latest/meta-data/`, internal hosts, `file://`, `localhost`) is by design. Callback POST extends to outbound POST SSRF. |
| Q4 Proof (passive) | **PARTIAL** — Spec analysis + SDK RAG confirms zero client-side validation. Passive probes confirm endpoints exist and are key-gated (401). **Cannot prove actual SSRF without a valid key** (AUTH_HELPED). |
| Q5 Novelty | YES — Not reported. |
| Q6 Not rejected | YES — Not info-disclosure, not best-practice. This is a designed-in SSRF surface gated by auth. |
| Q7 Triager accept | **HOLD** — Real vulnerability class, high impact, but **cannot be proven without a valid API key** (AUTH_HELPED). Passive-only triage cannot confirm exploitability. |

**VERDICT: HOLD** — Requires authorized API key to prove. Spec + RAG confirms SSRF-by-design surface; actual exploitability unconfirmed without key.

**Next step (if key available):**  
`POST https://api.gladia.io/v2/pre-recorded -H "x-gladia-key: <KEY>" -H "Content-Type: application/json" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/"}'` → compare `status`/`error_message`/duration vs benign canary URL. Repeat for `video_url` on `/video/text/video-transcription` and `callback_config.url`.

---

### **FINDING 3: Post-auth open redirect via `redirect_to` (app.gladia.io/signin)**

**Asset:** `app.gladia.io` — **High** per scope.yml

| Q | Answer |
|---|--------|
| Q1 Scope | YES — app.gladia.io is High priority. |
| Q2 Reachability | **CONDITIONAL** — `redirect_to` reflected into form action **unauthenticated** (passive GET confirms). But **post-auth honoring requires authenticated session** (Google OAuth). |
| Q3 Impact | **MEDIUM** — If server honors `redirect_to` after successful Google OAuth, user lands on attacker domain (phishing). OAuth `redirect_uri` is **FIXED (PKCE S256)** per probe — no code/state theft. Return-to cookie tampering **REJECTED** (server resets). |
| Q4 Proof (passive) | **PARTIAL** — Reflection confirmed: `GET /signin?redirect_to=https://evil.example.com` → form `action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"`. CSP has **0 `form-action` directives** (gap). **Post-auth behavior unobservable without session** (HUMAN_ONLY). |
| Q5 Novelty | YES — Not reported. |
| Q6 Not rejected | YES — Not self-XSS, not info-disclosure. |
| Q7 Triager accept | **HOLD** — Real vector, but **sole unverified gate is post-auth redirect** which requires human OAuth session. Cannot be proven passively. |

**VERDICT: HOLD** — Requires authenticated Google OAuth session to verify if `redirect_to` is honored post-auth.

**Next step (if session available):**  
Authenticate via Google SSO → `GET /signin?redirect_to=https://evil.example.com` → complete OAuth → capture final `302 Location` + `Set-Cookie`. Test variants: `//evil.example.com`, `https://app.gladia.io.evil.example.com/`.

---

### **FINDING 4: WebSocket auth token in URL query parameter (api.gladia.io/v2/live)**

**Asset:** `api.gladia.io` — **Highest**

| Q | Answer |
|---|--------|
| Q1 Scope | YES |
| Q2 Reachability | **CONDITIONAL** — Requires valid `x-gladia-key` to POST `/v2/live` and receive `url` with token. |
| Q3 Impact | **HIGH** — Token in `wss://api.gladia.io/v2/live?token=<uuid>` leaks via: browser history, Referer header on WS upgrade, TLS-terminating proxy logs, server access logs, URL sharing. Token is bearer-equivalent for live session. |
| Q4 Proof (passive) | **PARTIAL** — OpenAPI spec confirms `InitStreamingResponse.url` contains token as query param. **Cannot observe token format/rotation without key** (AUTH_HELPED). |
| Q5 Novelty | YES |
| Q6 Not rejected | YES |
| Q7 Triager accept | **HOLD** — Design flaw confirmed in spec, but exploitability (token lifetime, rotation, Referrer-Policy) unproven without key. |

**VERDICT: HOLD** — Requires authorized key to confirm token behavior.

---

### **FINDING 5: CORS wildcard (`*`) on api.gladia.io (no credentials)**

**Asset:** `api.gladia.io` — **Highest**

| Q | Answer |
|---|--------|
| Q1 Scope | YES |
| Q2 Reachability | YES — Public endpoints (`/openapi.json`, `/v1/models`, `/health`, `/v2/pre-recorded` OPTIONS). |
| Q3 Impact | **LOW** — `access-control-allow-origin: *` with **NO `access-control-allow-credentials`**. Cross-origin reads of **public** endpoints only. Authenticated endpoints return 401; credentialed requests cannot carry `x-gladia-key` cross-origin via browser (no `allow-credentials`). |
| Q4 Proof (passive) | YES — Probe confirms: `OPTIONS /v2/pre-recorded` → `ACAO: *`, `ACAH: x-gladia-key`, **no `ACAC`**. GET `/v1/models` with `Origin: evil.test` → `ACAO: *`. |
| Q5 Novelty | NO — Standard CORS misconfig, widely known. |
| Q6 Not rejected | **FAIL** — This is "best practice / low-impact misconfig" territory. Wildcard without credentials on public endpoints is not a vulnerability per se. |
| Q7 Triager accept | NO — Reasonable triager would classify as informational / hardening, not a vulnerability. |

**VERDICT: INVALID** — Low-impact misconfiguration, not a vulnerability. No credential leakage, no authenticated data exposure.

---

### **FINDING 6: `x-powered-by: Express` on CORS preflight only (api.gladia.io)**

**Asset:** `api.gladia.io` — **Highest**

| Q | Answer |
|---|--------|
| Q1 Scope | YES |
| Q2 Reachability | YES — `OPTIONS` preflight on any v2 endpoint. |
| Q3 Impact | **LOW** — Framework fingerprinting aids reconnaissance (targeted CVE scanning). Header absent on GET responses (differential). |
| Q4 Proof (passive) | YES — `curl -X OPTIONS -H "Origin: https://evil.test" -H "Access-Control-Request-Method: POST" -H "Access-Control-Request-Headers: x-gladia-key" https://api.gladia.io/v2/transcription` → `x-powered-by: Express`. GET same URL → no `x-powered-by`. |
| Q5 Novelty | NO — Common fingerprinting vector. |
| Q6 Not rejected | **FAIL** — "Best practice / info disclosure of public tech stack" — not a vulnerability. |
| Q7 Triager accept | NO — Informational at best. |

**VERDICT: INVALID** — Reconnaissance aid only, not a vulnerability.

---

### **FINDING 7: Undocumented `/health` endpoint (api.gladia.io)**

**Asset:** `api.gladia.io` — **Highest**

| Q | Answer |
|---|--------|
| Q1 Scope | YES |
| Q2 Reachability | YES — Public, unauthenticated. |
| Q3 Impact | **LOW** — Returns `{"health":"OK"}` (15 bytes). No verbose mode (`?full=true`, `?format=json` return same). No version/build/dependency leakage. |
| Q4 Proof (passive) | YES — `GET /health` → 200 `{"health":"OK"}`; `GET /health?full=true` → identical. Not in OpenAPI spec (14 paths). |
| Q5 Novelty | NO — Common undocumented health endpoint. |
| Q6 Not rejected | **FAIL** — "Info disclosure of public data / best practice" — returns static OK, no sensitive data. |
| Q7 Triager accept | NO — Not a vulnerability. |

**VERDICT: INVALID** — No sensitive information disclosed.

---

### **FINDING 8: IDOR on transcription file download `/v2/transcription/{id}/file` etc.**

**Asset:** `api.gladia.io` — **Highest**

| Q | Answer |
|---|---|
| Q1 Scope | YES |
| Q2 Reachability | **CONDITIONAL** — Key-gated (401). Needs valid key + valid transcription ID owned by another user. |
| Q3 Impact | **HIGH** — Cross-tenant access to transcription audio/text (PII, sensitive content). |
| Q4 Proof (passive) | **NO** — Spec shows endpoints exist; ownership model opaque. **Cannot prove without two accounts/keys** (AUTH_HELPED ×2). |
| Q5 Novelty | YES |
| Q6 Not rejected | YES |
| Q7 Triager accept | **HOLD** — Real high-impact class, but completely untestable without authorized multi-tenant access. |

**VERDICT: HOLD** — Requires two valid API keys (attacker + victim) to test cross-account access.

---

### **FINDING 9: Query-param parsing injection on `/v1/history` (`custom_metadata` object)**

**Asset:** `api.gladia.io` — **Highest**

| Q | Answer |
|---|---|
| Q1 Scope | YES |
| Q2 Reachability | **CONDITIONAL** — Key-gated (401). |
| Q3 Impact | **LOW-MEDIUM** — Prototype pollution / filter bypass on own-tenant query. Key-gated limits blast radius. |
| Q4 Proof (passive) | **NO** — Spec shows `custom_metadata` as `object` with `additionalProperties:true` in query string. **Cannot test injection without key** (AUTH_HELPED). |
| Q5 Novelty | YES |
| Q6 Not rejected | YES |
| Q7 Triager accept | **HOLD** — Untestable without key; low impact even if proven (own-tenant only). |

**VERDICT: HOLD** — Requires authorized key; low severity.

---

### **FINDING 10: `return-to` cookie unsigned base64url JSON (app.gladia.io)**

**Asset:** `app.gladia.io` — **High**

| Q | Answer |
|---|---|
| Q1 Scope | YES |
| Q2 Reachability | YES — Cookie set on root `/`. |
| Q3 Impact | **NONE PROVEN** — Cookie is `eyJ1cmwiOiIvIn0=` = `{"url":"/"}` (unsigned). **Server rejects tampered values and resets to default** (probe confirmed). No open redirect via cookie tampering. |
| Q4 Proof (passive) | YES — Tampering test: `Cookie: return-to=eyJ1cmwiOiJodHRwczovL2V2aWwuY29tIn0=` → server resets to `{"url":"/"}`. |
| Q5 Novelty | N/A |
| Q6 Not rejected | **FAIL** — Tested and **rejected**; no vulnerability exists. |
| Q7 Triager accept | NO — Actively disproven. |

**VERDICT: INVALID** — Server-side validation prevents exploitation.

---

## **SUMMARY TRIAGE TABLE**

| # | Finding | Asset | Verdict | Reason |
|---|---------|-------|---------|--------|
| 1 | npm `gladia`@0.1.3 impersonation + key-in-URL | npm (Medium) | **VALID** | Passive-proven supply-chain impersonation (orphaned repo) + credential hygiene flaw |
| 2 | SSRF via `audio_url`/`video_url`/`callback_url` | api.gladia.io (Highest) | **HOLD** | Spec-confirmed SSRF-by-design; needs valid API key to prove exploitability |
| 3 | Post-auth open redirect via `redirect_to` | app.gladia.io (High) | **HOLD** | Reflection confirmed; post-auth honoring requires human OAuth session |
| 4 | WebSocket token in URL query param | api.gladia.io (Highest) | **HOLD** | Spec-confirmed design flaw; needs key to confirm token behavior |
| 5 | CORS wildcard (`*`) no credentials | api.gladia.io (Highest) | **INVALID** | Low-impact misconfig; no credential leakage, public endpoints only |
| 6 | `x-powered-by: Express` on preflight only | api.gladia.io (Highest) | **INVALID** | Reconnaissance aid only; not a vulnerability |
| 7 | Undocumented `/health` endpoint | api.gladia.io (Highest) | **INVALID** | Returns static `{"health":"OK"}`; no sensitive data |
| 8 | IDOR on `/{id}/file` download | api.gladia.io (Highest) | **HOLD** | High impact but needs two valid keys (cross-tenant) |
| 9 | Query-param injection `/v1/history` | api.gladia.io (Highest) | **HOLD** | Low impact (own-tenant); needs key |
| 10 | `return-to` cookie unsigned | app.gladia.io (High) | **INVALID** | Server resets tampered values; actively disproven |

---

### **IMMEDIATELY REPORTABLE (VALID)**

**Only Finding 1** — npm `gladia`@0.1.3 orphaned impersonation + API key in WebSocket URL.

**Report now via:**
1. **npm Trust & Safety**: `https://www.npmjs.com/support` — impersonation + abandoned package (orphaned GitHub user/repo)
2. **Gladia security**: `security@gladia.io` or `https://gladia.io/bug-bounty-report` — for the credential-in-URL design flaw *conditional on* `wss://api.gladia.io/v2/live?x-gladia-key=<KEY>` being accepted by the server (test with 1 valid key if available).

---

### **REQUIRE AUTHORIZED ACCESS (HOLD — need program-provided key/session)**

| Finding | What's needed |
|---------|---------------|
| SSRF (api.gladia.io) | 1 valid `x-gladia-key` → POST `/v2/pre-recorded` with `audio_url=http://169.254.169.254/latest/meta-data/` |
| Post-auth redirect (app.gladia.io) | Google OAuth session → complete sign-in with `?redirect_to=https://evil.example.com` |
| WS token leak (api.gladia.io) | 1 valid key → POST `/v2/live` → inspect token format, lifetime, Referrer-Policy |
| IDOR (api.gladia.io) | 2 valid keys (different accounts) + transcription IDs |
| Query injection (api.gladia.io) | 1 valid key → GET `/v1/history?custom_metadata[__proto__][x]=1` |

---

[NEXT] PROBE: If you can provide a valid `x-gladia-key` (program trial or personal), the immediate high-value test is:
```
POST https://api.gladia.io/v2/pre-recorded -H "x-gladia-key: <KEY>" -H "Content-Type: application/json" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/"}'
```
Compare `status`/`error_message`/duration vs `{"audio_url":"http://<attacker-canary>"}`. This single request confirms or denies the highest-impact finding (SSRF to cloud metadata).
