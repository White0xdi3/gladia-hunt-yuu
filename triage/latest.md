===== TRIAGE 2026-10-15 00:02:08 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
I don't see the actual leads in your message - it ends with "LEADS:" but no content follows. Please provide the leads you want me to triage.

Also, let me check if there's a scope.yml or any relevant files in the workspace first.
[0m✱ [0mGlob "**/*.md"[90m 22 matches[0m
[0m✱ [0mGlob "**/scope.yml"[90m 1 match[0m
[0m→ [0mRead scope.yml
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead probe-results.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead leads/reposcan-latest.md
Now I have a comprehensive view of all leads. Let me evaluate each unique hypothesis against the 7-Question Gate.

## TRIAGE RESULTS

### 1. SSRF via audio_url/video_url/callback_url (api.gladia.io POST /v2/pre-recorded, /v2/upload, /v2/live, legacy endpoints)

| Q | Answer |
|---|---|
| **Q1 Scope** | YES — api.gladia.io is HIGHEST priority in scope.yml |
| **Q2 Reachable** | NO — All endpoints return 401 without valid `x-gladia-key` (probe: 401). Requires AUTH_HELPED. No unauthenticated/low-priv access. |
| **Q3 Impact** | YES — Cloud metadata (169.254.169.254), internal network enumeration, data exfiltration. High severity IF exploitable. |
| **Q4 Passive proof** | NO — Requires valid API key + POST with internal URLs. Cannot prove with GET/HEAD only. |
| **Q5 Novel** | UNKNOWN — Spec confirms `format:uri` no scheme allowlist, 7 webhook paths, FR/US egress. But unvalidated without key. |
| **Q6 Not rejected** | YES — Not on always-rejected list. |
| **Q7 Triager accept** | HOLD — Real SSRF-by-design surface, but key-gated. Cannot validate without program-provided key. |

**VERDICT: HOLD** — Requires AUTH_HELPED (valid x-gladia-key). No passive proof possible.  
**Next**: `[NEXT] PROBE: POST https://api.gladia.io/v2/pre-recorded -H "x-gladia-key: <VALID_KEY>" -H "Content-Type: application/json" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/"}'` (needs program key)

---

### 2. npm `gladia@0.1.3` orphaned impersonation + key-in-URL (npm registry)

| Q | Answer |
|---|---|
| **Q1 Scope** | NO — Package is on npm registry, owned by `softwarecitadel` (personal), repo `alexisbouchez/gladia.ts` (404). NOT a Gladia asset. Scope.yml lists only `@gladiaio/sdk` and `gladiaio-sdk` as Official SDKs (MEDIUM). Third-party packages are OUT OF SCOPE. |
| **Q2 Reachable** | YES — Public npm package, installable by anyone. |
| **Q3 Impact** | YES — Supply chain: developers install thinking it's official; key embedded in WS URL query leaks to proxy/logs; orphaned repo = irrevocable takeover risk. Medium-High. |
| **Q4 Passive proof** | YES — Registry metadata (`npm view`), tarball source (`src/client.ts:306-308`), GitHub 404 all confirmed passively. |
| **Q5 Novel** | YES — Not previously reported to Gladia (human filed 2026-08-12, awaiting response). |
| **Q6 Not rejected** | YES — Not info disclosure/best practice. |
| **Q7 Triager accept** | NO for Gladia venue (Q1 fail). YES for npm Trust & Safety venue. |

**VERDICT: INVALID (Gladia venue)** — Out of scope (not a Gladia asset).  
**VALID (npm venue)** — Report to npm Trust & Safety (impersonation + abandoned package).  
**Channel**: https://www.npmjs.com/support (not Gladia security channel).  
**Note**: Human already reported to Gladia 2026-08-12; Gladia triage correctly split venue.

---

### 3. Post-auth open redirect via `redirect_to` (app.gladia.io /signin?redirect_to=)

| Q | Answer |
|---|---|
| **Q1 Scope** | YES — app.gladia.io is HIGH priority in scope.yml |
| **Q2 Reachable** | PARTIAL — Reflection confirmed passively (GET returns 200 with `action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"`). But exploit requires authenticated Google OAuth session (post-auth redirect). |
| **Q3 Impact** | MEDIUM — Post-auth phishing redirect. OAuth `redirect_uri` is FIXED (PKCE S256) per probe, so no code/state theft. |
| **Q4 Passive proof** | NO — Requires HUMAN_ONLY: complete Google OAuth with `redirect_to=evil` and observe final 302 Location. |
| **Q5 Novel** | UNKNOWN — Reflection confirmed, post-auth behavior untested. |
| **Q6 Not rejected** | YES — Not on always-rejected list. |
| **Q7 Triager accept** | HOLD — Reflection is real; exploitability gated behind auth. |

**VERDICT: HOLD** — Requires authenticated Google OAuth session to validate post-auth redirect.  
**Next**: `[NEXT] HUMAN: Authenticate via Google SSO on app.gladia.io, then visit /signin?redirect_to=https://evil.example.com and observe post-auth 302 Location.`

---

### 4. CORS wildcard reflects arbitrary origin (api.gladia.io)

| Q | Answer |
|---|---|
| **Q1 Scope** | YES — api.gladia.io in scope |
| **Q2 Reachable** | YES — Public endpoints |
| **Q3 Impact** | NO — Probes confirm static `access-control-allow-origin: *` (NOT Origin reflection). No `access-control-allow-credentials`. Cross-origin reads of public data only (/v1/models, /openapi.json, /health). Low impact. |
| **Q4 Passive proof** | YES — Probes confirm static `*` not reflection. |
| **Q5 Novel** | N/A — Hypothesis disproven. |
| **Q6 Not rejected** | N/A |
| **Q7 Triager accept** | NO — Disproven by passive probes. |

**VERDICT: INVALID** — Probes show static `*`, no Origin reflection. No credential leakage.

---

### 5. Tech stack disclosure: `x-powered-by: Express` on CORS preflight only (api.gladia.io)

| Q | Answer |
|---|---|
| **Q1 Scope** | YES |
| **Q2 Reachable** | YES — OPTIONS preflight public |
| **Q3 Impact** | NO — Framework fingerprinting only. Low severity. On always-rejected list ("info disclosure of public data", "best practice"). |
| **Q4 Passive proof** | YES — Confirmed: OPTIONS returns `x-powered-by: Express`, GET does not. |
| **Q5 Novel** | N/A |
| **Q6 Not rejected** | NO — On always-rejected list (info disclosure/best practice). |
| **Q7 Triager accept** | NO — Standard misconfiguration, not a vulnerability. |

**VERDICT: INVALID** — Always-rejected: info disclosure of public data / best practice.

---

### 6. IDOR on transcription file download endpoints `/{id}/file` (api.gladia.io)

| Q | Answer |
|---|---|
| **Q1 Scope** | YES |
| **Q2 Reachable** | NO — Requires valid `x-gladia-key` (401 without) + valid transcription ID from another user. AUTH_HELPED + cross-account test needed. |
| **Q3 Impact** | YES — Cross-account transcription data (PII, audio). High. |
| **Q4 Passive proof** | NO — Requires key + cross-account IDs. |
| **Q5 Novel** | UNKNOWN |
| **Q6 Not rejected** | YES |
| **Q7 Triager accept** | HOLD — Spec shows endpoints, but authorization model opaque. Needs key. |

**VERDICT: HOLD** — Requires AUTH_HELPED with valid key + cross-account test.

---

### 7. Undocumented `/health` endpoint (api.gladia.io)

| Q | Answer |
|---|---|
| **Q1 Scope** | YES |
| **Q2 Reachable** | YES — GET /health returns 200 `{"health":"OK"}` publicly |
| **Q3 Impact** | NO — Minimal info disclosure. Probe: `/health?full=true` returns identical output. No version/build metadata. Low. On always-rejected list ("info disclosure of public data"). |
| **Q4 Passive proof** | YES — Confirmed. |
| **Q5 Novel** | N/A |
| **Q6 Not rejected** | NO — Always-rejected (info disclosure of public data). |
| **Q7 Triager accept** | NO — Just `{"health":"OK"}`. |

**VERDICT: INVALID** — Always-rejected: minimal info disclosure.

---

### 8. WebSocket auth token in URL query parameter (api.gladia.io wss://api.gladia.io/v2/live?token=<uuid>)

| Q | Answer |
|---|---|
| **Q1 Scope** | YES |
| **Q2 Reachable** | PARTIAL — Token issued after POST /v2/live with valid key. Requires AUTH_HELPED to obtain token. Once in URL, leaks via Referer, logs, history. |
| **Q3 Impact** | YES — Token theft → unauthorized live transcription, audio access. High. |
| **Q4 Passive proof** | PARTIAL — Design confirmed via OpenAPI spec (InitStreamingResponse.url). But exploitability (token leakage, rotation, Referrer-Policy) needs auth. |
| **Q5 Novel** | UNKNOWN |
| **Q6 Not rejected** | YES |
| **Q7 Triager accept** | HOLD — Design flaw confirmed (token in URL), but exploitation needs valid key. |

**VERDICT: HOLD** — Design confirmed passively; exploitation requires AUTH_HELPED.

---

### 9. Query-param parsing injection on `/v1/history` (api.gladia.io)

| Q | Answer |
|---|---|
| **Q1 Scope** | YES |
| **Q2 Reachable** | NO — Requires valid `x-gladia-key` (401 without). AUTH_HELPED. |
| **Q3 Impact** | LOW-MEDIUM — Filter bypass / prototype pollution on own-tenant query. Key-gated. |
| **Q4 Passive proof** | NO — Requires key + injection payloads. |
| **Q5 Novel** | UNKNOWN |
| **Q6 Not rejected** | YES |
| **Q7 Triager accept** | HOLD — Spec shows `custom_metadata` object + array params in query string (NestJS deep-parse surface). Needs key. |

**VERDICT: HOLD** — Requires AUTH_HELPED.

---

### 10. Return-to cookie JWT parsing without signature (app.gladia.io)

| Q | Answer |
|---|---|
| **Q1 Scope** | YES |
| **Q2 Reachable** | YES — Cookie set on root |
| **Q3 Impact** | NO — Proven: cookie is unsigned base64url JSON `{"url":"/"}`. Tampering rejected (server resets to default). No open redirect. |
| **Q4 Passive proof** | YES — Confirmed by probe. |
| **Q5 Novel** | N/A — Disproven. |
| **Q6 Not rejected** | N/A |
| **Q7 Triager accept** | NO — Server validates/resets. |

**VERDICT: INVALID** — Disproven by passive validation (server rejects tampered cookie).

---

### 11. OpenAPI shadow endpoints / undocumented v2 paths (api.gladia.io)

| Q | Answer |
|---|---|
| **Q1 Scope** | YES |
| **Q2 Reachable** | YES — Spec public |
| **Q3 Impact** | NO — Probes: 14 paths stable, /v1/* 404, /debug /admin /actuator/health /metrics all 404. No shadow endpoints. |
| **Q4 Passive proof** | YES — Confirmed no undocumented endpoints. |
| **Q5 Novel** | N/A — Disproven. |
| **Q6 Not rejected** | N/A |
| **Q7 Triager accept** | NO — Surface frozen, fully enumerated. |

**VERDICT: INVALID** — Disproven by exhaustive passive probes.

---

## SUMMARY

| # | Hypothesis | Verdict | Reason |
|---|---|---|---|
| 1 | SSRF via audio_url/video_url/callback_url | **HOLD** | Key-gated (401), needs AUTH_HELPED |
| 2 | npm gladia@0.1.3 impersonation | **INVALID (Gladia)** / **VALID (npm)** | Out of scope for Gladia; report to npm Trust & Safety |
| 3 | Post-auth open redirect (redirect_to) | **HOLD** | Needs authenticated Google OAuth session |
| 4 | CORS Origin reflection | **INVALID** | Disproven: static `*`, no reflection |
| 5 | x-powered-by Express on preflight | **INVALID** | Always-rejected: info disclosure/best practice |
| 6 | IDOR on /{id}/file | **HOLD** | Key-gated + cross-account test needed |
| 7 | Undocumented /health | **INVALID** | Always-rejected: minimal info disclosure |
| 8 | WS token in URL query | **HOLD** | Design confirmed; exploitation needs key |
| 9 | Query-param injection /v1/history | **HOLD** | Key-gated |
| 10 | return-to cookie open redirect | **INVALID** | Disproven: server validates/resets |
| 11 | OpenAPI shadow endpoints | **INVALID** | Disproven: surface frozen, fully enumerated |

---

## ACTIONABLE NEXT STEPS (READ-ONLY PROBES)

```
[NEXT] PROBE: POST https://api.gladia.io/v2/pre-recorded -H "x-gladia-key: <VALID_KEY>" -H "Content-Type: application/json" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/","callback_url":"http://169.254.169.254/latest/meta-data/"}'
  → Validates SSRF (Hypothesis 1). Needs program-provided key.

[NEXT] HUMAN: Authenticate via Google SSO on app.gladia.io, visit /signin?redirect_to=https://evil.example.com, observe post-auth 302 Location.
  → Validates post-auth open redirect (Hypothesis 3).

[NEXT] PROBE: POST https://api.gladia.io/v2/live -H "x-gladia-key: <VALID_KEY>" -H "Content-Type: application/json" -d '{}' → observe response.url token format; initiate WS connection, inspect upgrade Referer; test token reuse after disconnect.
  → Validates WS token leakage (Hypothesis 8). Needs program key.

[NEXT] PROBE: GET https://api.gladia.io/v1/history?custom_metadata[__proto__][x]=1 -H "x-gladia-key: <VALID_KEY>"
  → Validates query-param injection (Hypothesis 9). Needs program key.
```

---

## REPORTING CHANNELS

- **Gladia security channel**: https://gladia.io/bug-bounty-report (Google Forms, SSO auth-gated) — per scope.yml disclosure policy
- **npm Trust & Safety**: https://www.npmjs.com/support — for `gladia@0.1.3` impersonation (VALID finding, but wrong venue for Gladia program)
- **No other channels** — All other hypotheses are HOLD (need auth) or INVALID (disproven/always-rejected)
