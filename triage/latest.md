===== TRIAGE 2026-10-08 22:16:15 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/leads*"[90m 0 matches[0m
[0m✱ [0mGlob "**/scope.yml"[90m 1 match[0m
[0m→ [0mRead scope.yml
[0m✱ [0mGlob "**/*"[90m 53 matches[0m
[0m→ [0mRead probe-results.txt
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead new-leads.txt
Now I have a full picture of all leads from all models. Let me apply the 7-Question Gate to each unique lead.

---

## TRIAGE VERDICTS

### LEAD 1: npm `gladia@0.1.3` orphaned impersonation + API key in WS URL
**Asset:** npm registry (`gladia@0.1.3`) — **IN SCOPE** (Official SDKs npm/PyPI = Medium)

| Q | Answer |
|---|--------|
| Q1 Scope? | **YES** — npm package listed in scope.yml under Official SDKs (Medium) |
| Q2 Reachable? | **YES** — public npm registry, no auth required |
| Q3 Impact? | **YES** — Supply-chain: "Official" claim false (README says Unofficial), orphaned repo (404), maintainer personal gmail, **embeds raw `x-gladia-key` in WebSocket URL query** (`src/client.ts:306-308`) diverging from official SDK's header+token flow; keys leak to proxy/logs/browser history |
| Q4 Passive proof? | **YES** — `npm view gladia@0.1.3` metadata + tarball inspection + GitHub API 404 all verified passively |
| Q5 Novel? | **YES** — not previously reported to Gladia (human filed 2026-08-12, no vendor action yet) |
| Q6 Not rejected? | **YES** — not on always-rejected list (impersonation + credential hygiene = real) |
| Q7 Triager accept? | **YES** — clear supply-chain risk + credential exposure |

**VERDICT: VALID**  
**Impact:** Supply-chain API key harvesting + irrevocable takeover risk (orphaned GitHub account)  
**CVSS 3.1:** 7.5 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N) — High  
**Minimal proof:** `npm view gladia@0.1.3 description repository.url maintainer` + tarball `src/client.ts:306-308` showing `searchParams.append('x-gladia-key', apiKey)`  
**Channel:** Gladia security form (https://gladia.io/bug-bounty-report) + npm Trust & Safety

---

### LEAD 2: SSRF via `audio_url`/`video_url`/`callback_url` server-side fetch
**Asset:** `api.gladia.io` (Highest) — POST `/v2/pre-recorded`, `/v2/live`, legacy `/audio|/video/text/*`

| Q | Answer |
|---|--------|
| Q1 Scope? | **YES** — api.gladia.io = Highest |
| Q2 Reachable? | **PARTIAL** — key-gated (401 without `x-gladia-key`); needs valid API key |
| Q3 Impact? | **YES** — Cloud metadata (169.254.169.254), internal network read, callback POST exfil; **High** if key obtained |
| Q4 Passive proof? | **NO** — requires `AUTH_HELPED` (valid key + POST with internal URL); probe results show 401 without key |
| Q5 Novel? | **YES** — spec confirms `format:uri` with NO scheme allowlist, 7 webhook paths, FR/US egress |
| Q6 Not rejected? | **YES** — SSRF-to-metadata is high-value class |
| Q7 Triager accept? | **CONDITIONAL** — real vuln class but **blocked on key**; cannot prove without invasive test |

**VERDICT: HOLD** — Auth-gated; needs program-provided trial key for POC.  
**Next:** `[NEXT] PROBE: POST https://api.gladia.io/v2/pre-recorded -H "x-gladia-key: <valid_key>" -H "Content-Type: application/json" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/"}'` (AUTH_HELPED)

---

### LEAD 3: Post-auth open redirect via `redirect_to` on `app.gladia.io/signin`
**Asset:** `app.gladia.io` (High) — `/signin?redirect_to=`

| Q | Answer |
|---|--------|
| Q1 Scope? | **YES** — app.gladia.io = High |
| Q2 Reachable? | **PARTIAL** — reflection confirmed passively (form action), but **post-auth honoring requires authenticated session** |
| Q3 Impact? | **MEDIUM** — phishing redirect after Google OAuth; OAuth `redirect_uri` is FIXED (PKCE S256) so no code theft |
| Q4 Passive proof? | **NO** — final 302 Location post-auth unobserved; needs `HUMAN_ONLY` session |
| Q5 Novel? | **YES** — CSP lacks `form-action` directive (gap confirmed) |
| Q6 Not rejected? | **YES** — open redirect is valid class |
| Q7 Triager accept? | **CONDITIONAL** — unverified post-auth behavior |

**VERDICT: HOLD** — Requires human Google OAuth session to verify post-auth redirect.  
**Next:** `[NEXT] HUMAN: Authenticate via Google SSO, then GET /signin?redirect_to=https://evil.example.com post-auth, capture final 302 Location`

---

### LEAD 4: `x-powered-by: Express` on CORS preflight only
**Asset:** `api.gladia.io` (Highest) — OPTIONS responses

| Q | Answer |
|---|--------|
| Q1 Scope? | **YES** |
| Q2 Reachable? | **YES** — public OPTIONS preflight |
| Q3 Impact? | **LOW** — framework fingerprinting only; aids CVE targeting but no direct exploit |
| Q4 Passive proof? | **YES** — `curl -X OPTIONS -H "Origin: https://evil.test" -H "Access-Control-Request-Headers: x-gladia-key" https://api.gladia.io/v2/transcription` returns `x-powered-by: Express`; absent on GET |
| Q5 Novel? | **YES** — preflight-only disclosure |
| Q6 Not rejected? | **YES** — not "info disclosure of public data" (header hidden on GET) |
| Q7 Triager accept? | **YES** — valid misconfig, Low severity |

**VERDICT: VALID**  
**Impact:** Reconnaissance aid (Node/Express version targeting)  
**CVSS 3.1:** 3.7 (AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N) — Low  
**Minimal proof:** OPTIONS preflight shows `x-powered-by: Express`; GET does not  
**Channel:** Gladia security form

---

### LEAD 5: Undocumented `/health` endpoint on `api.gladia.io`
**Asset:** `api.gladia.io` (Highest)

| Q | Answer |
|---|--------|
| Q1 Scope? | **YES** |
| Q2 Reachable? | **YES** — public GET returns 200 `{"health":"OK"}` |
| Q3 Impact? | **NO** — no version/build/dependency leakage; `?full=true`, `?format=json` return identical body |
| Q4 Passive proof? | **YES** |
| Q5 Novel? | **NO** — already documented in leads as "undocumented but benign" |
| Q6 Not rejected? | **NO** — **info disclosure of non-sensitive public data** (always-rejected) |
| Q7 Triager accept? | **NO** |

**VERDICT: INVALID** — No sensitive data leaked; health check is standard operational endpoint.

---

### LEAD 6: WebSocket auth token in URL query (`wss://api.gladia.io/v2/live?token=<uuid>`)
**Asset:** `api.gladia.io` (Highest)

| Q | Answer |
|---|--------|
| Q1 Scope? | **YES** |
| Q2 Reachable? | **PARTIAL** — token issued after key-gated POST `/v2/live` |
| Q3 Impact? | **MEDIUM** — token in URL leaks via Referer, browser history, proxy logs; but token is **short-lived session token**, not API key |
| Q4 Passive proof? | **NO** — requires key-gated POST to observe token format |
| Q5 Novel? | **NO** — documented in OpenAPI spec (`InitStreamingResponse.url`) |
| Q6 Not rejected? | **YES** — token-in-URL is recognized hygiene issue |
| Q7 Triager accept? | **WEAK** — by-design per spec; not a vuln, a design choice |

**VERDICT: INVALID** — Documented behavior, session token (not long-lived key), requires auth to obtain.

---

### LEAD 7: CORS wildcard (`*`) with `x-gladia-key` allowed cross-origin
**Asset:** `api.gladia.io` (Highest)

| Q | Answer |
|---|--------|
| Q1 Scope? | **YES** |
| Q2 Reachable? | **YES** |
| Q3 Impact? | **LOW** — no `access-control-allow-credentials`; cannot read authenticated responses cross-origin |
| Q4 Passive proof? | **YES** — OPTIONS/GET show static `*`, allow-headers includes `x-gladia-key` |
| Q5 Novel? | **NO** — standard CORS config for public APIs |
| Q6 Not rejected? | **NO** — **best practice / config hardening only**; no exploit without credentials |
| Q7 Triager accept? | **NO** |

**VERDICT: INVALID** — Wildcard without credentials is not exploitable for cross-origin reads of authenticated data.

---

### LEAD 8: IDOR on transcription file download `/{id}/file`
**Asset:** `api.gladia.io` (Highest) — `/v2/transcription/{id}/file`, `/v2/pre-recorded/{id}/file`, `/v2/live/{id}/file`

| Q | Answer |
|---|--------|
| Q1 Scope? | **YES** |
| Q2 Reachable? | **PARTIAL** — key-gated (401 without key) |
| Q3 Impact? | **HIGH** — cross-tenant audio/PII access if object-level auth missing |
| Q4 Passive proof? | **NO** — needs two valid keys (different users) to test cross-account access |
| Q5 Novel? | **YES** — spec opaque on ownership binding |
| Q6 Not rejected? | **YES** — IDOR is high-value class |
| Q7 Triager accept? | **CONDITIONAL** — plausible but untestable without two accounts |

**VERDICT: HOLD** — Requires two valid API keys (different tenants) for POC.  
**Next:** `[NEXT] PROBE: AUTH_HELPED x2 — obtain two trial keys, create transcription with key A, GET /v2/transcription/{id}/file with key B`

---

### LEAD 9: Query-param parsing injection on `/v1/history` (`custom_metadata` object, `status`/`kind` arrays)
**Asset:** `api.gladia.io` (Highest) — GET `/v1/history`

| Q | Answer |
|---|--------|
| Q1 Scope? | **YES** |
| Q2 Reachable? | **PARTIAL** — key-gated |
| Q3 Impact? | **LOW-MED** — filter bypass / prototype pollution on **own-tenant** query only |
| Q4 Passive proof? | **NO** — needs key + injection payloads |
| Q5 Novel? | **YES** — non-native query parsing (object/array in querystring) |
| Q6 Not rejected? | **YES** |
| Q7 Triager accept? | **WEAK** — key-gated, self-tenant only |

**VERDICT: HOLD** — Auth-gated, low impact (own data only). Defer.

---

### LEAD 10: `return-to` cookie JWT parsing without signature verification
**Asset:** `app.gladia.io` (High)

| Q | Answer |
|---|--------|
| Q1 Scope? | **YES** |
| Q2 Reachable? | **YES** |
| Q3 Impact? | **NO** — server **rejects tampered cookie and resets to default** `{"url":"/"}` (confirmed by multiple models) |
| Q4 Passive proof? | **YES** — tamper test already done |
| Q5 Novel? | **NO** — disproven |
| Q6 Not rejected? | **N/A** |
| Q7 Triager accept? | **NO** |

**VERDICT: INVALID** — Server validates/resets; no open redirect via cookie.

---

### LEAD 11: CORS wildcard reflects arbitrary Origin
**Asset:** `api.gladia.io` (Highest)

| Q | Answer |
|---|---|
| Q1 Scope? | **YES** |
| Q2 Reachable? | **YES** |
| Q3 Impact? | **NO** — **disproven**: later probes show **static `access-control-allow-origin: *`** (not Origin reflection) |
| Q4 Passive proof? | **YES** — confirmed static `*` |
| Q5 Novel? | **NO** — hypothesis retracted |
| Q6 Not rejected? | **N/A** |
| Q7 Triager accept? | **NO** |

**VERDICT: INVALID** — Origin reflection disproven; static wildcard.

---

### LEAD 12: OpenAPI shadow/undocumented endpoints
**Asset:** `api.gladia.io` (Highest)

| Q | Answer |
|---|---|
| Q1 Scope? | **YES** |
| Q2 Reachable? | **YES** |
| Q3 Impact? | **NO** — **NO_DRIFT** confirmed across 100+ cycles: 14 paths stable, `/health` only undocumented, all others 404 |
| Q4 Passive proof? | **YES** — exhaustive probing done |
| Q5 Novel? | **NO** — exhaustively checked |
| Q6 Not rejected? | **N/A** |
| Q7 Triager accept? | **NO** |

**VERDICT: INVALID** — No shadow endpoints exist; surface frozen.

---

## SUMMARY

| Lead | Verdict | Reason |
|------|---------|--------|
| npm `gladia@0.1.3` impersonation + key-in-URL | **VALID** | Passive proof complete; supply-chain + credential hygiene |
| SSRF via `audio_url`/`callback_url` | **HOLD** | Needs valid API key (AUTH_HELPED) |
| Post-auth open redirect `redirect_to` | **HOLD** | Needs human Google OAuth session (HUMAN_ONLY) |
| `x-powered-by: Express` on preflight | **VALID** | Passive proven; Low severity |
| Undocumented `/health` | **INVALID** | No sensitive data |
| WS token in URL | **INVALID** | By-design per spec; session token |
| CORS wildcard + auth header | **INVALID** | No credentials; not exploitable |
| IDOR on `/{id}/file` | **HOLD** | Needs two keys (AUTH_HELPED x2) |
| `/v1/history` query injection | **HOLD** | Auth-gated, self-tenant only |
| `return-to` cookie JWT | **INVALID** | Server rejects tampering |
| CORS Origin reflection | **INVALID** | Disproven (static `*`) |
| OpenAPI shadow endpoints | **INVALID** | NO_DRIFT confirmed |

---

## IMMEDIATELY REPORTABLE (VALID, passive proof complete)

1. **npm `gladia@0.1.3` orphaned impersonation + API key in WebSocket URL** — **High** (CVSS 7.5) — Report via Gladia security form + npm Trust & Safety
2. **`x-powered-by: Express` leaked on CORS preflight only** — **Low** (CVSS 3.7) — Report via Gladia security form

## BLOCKED ON AUTHORIZED ACCESS (HOLD)

3. **SSRF via `audio_url`/`video_url`/`callback_url`** — Requires program-provided `x-gladia-key` for POC
4. **Post-auth open redirect via `redirect_to`** — Requires human Google OAuth session
5. **IDOR on transcription file download** — Requires two valid keys (different tenants)

---

**Next action:** Submit the npm impersonation report (locked, 10+ independent reproductions). If program provides a trial key, execute SSRF POC immediately.
