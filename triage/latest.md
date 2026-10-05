===== TRIAGE 2026-10-05 22:48:12 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/*"[90m 53 matches[0m
[0m→ [0mRead new-leads.txt
[0m→ [0mRead probe-results.txt
[0m→ [0mRead scope.yml
[0m→ [0mRead probe-results.md
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead leads/reposcan-latest.md
Now I have a complete picture. Let me consolidate the distinct leads and triage each against the 7-Question Gate.

## DISTINCT LEADS TRIAGE

### LEAD 1: npm `gladia@0.1.3` orphaned impersonation + API key leak in WebSocket URL
**Asset:** npm registry (gladia@0.1.3) — **NOT in Gladia scope** (scope lists only `@gladiaio/sdk` and `gladiaio-sdk` as official SDKs)
| Q | Answer |
|---|---|
| Q1 Scope? | **NO** — `gladia` (unscoped) is not `@gladiaio/sdk` or `gladiaio-sdk`. It's a third-party package. |
| Q2 Attacker reach? | YES — public npm registry, `dist-tag: latest` |
| Q3 Real impact? | YES — supply-chain impersonation + raw API key in WS URL query (logs/proxy/browser history) |
| Q4 Passive proof? | YES — registry metadata + tarball source + GitHub 404 all verified passively |
| Q5 Novel? | YES — not previously reported to Gladia (human reported 2026-08-12, awaiting response) |
| Q6 Not rejected? | YES — not on always-rejected list |
| Q7 Triager accept? | **NO for Gladia venue** — root cause lives in third-party package, not Gladia asset. **YES for npm Trust & Safety venue**. |

**VERDICT: INVALID for Gladia program** (out of scope asset). **VALID for npm Trust & Safety** (report there). Gladia-side only becomes valid if `wss://api.gladia.io/v2/live?x-gladia-key=<KEY>` works (query-param auth on WS) — needs 1 valid key to prove. **[NEXT] PROBE: WSS handshake to `wss://api.gladia.io/v2/live?x-gladia-key=<VALID_KEY>` vs header-auth control** (AUTH_HELPED).

---

### LEAD 2: api.gladia.io SSRF via audio_url/video_url/callback_url (server-side fetch)
**Asset:** api.gladia.io — **HIGHEST priority in scope**
| Q | Answer |
|---|---|
| Q1 Scope? | YES — api.gladia.io explicitly in scope (Highest) |
| Q2 Attacker reach? | **CONDITIONAL** — endpoint is key-gated (401 without `x-gladia-key`). Needs valid API key (AUTH_HELPED). |
| Q3 Real impact? | YES — cloud metadata (169.254.169.254), internal network read, potential data exfiltration via callback_url POST. Severity: High. |
| Q4 Passive proof? | **NO** — requires authenticated POST with internal URL to observe error/timing delta. Cannot prove without key. |
| Q5 Novel? | YES — not previously reported; spec+RAG frozen 100+ cycles confirming design. |
| Q6 Not rejected? | YES — not on rejected list (SSRF is high-value class). |
| Q7 Triager accept? | **HOLD** — genuine high-value vulnerability class, but **cannot be validated without a valid API key**. Passive-only gate fails (Q4). |

**VERDICT: HOLD** — SSRF-by-design confirmed in spec (audio_url/video_url/callback_config.url = `format:uri` no scheme allowlist; 7 webhook paths; FR/US egress). **Requires AUTH_HELPED validation with program-provided key**. Minimal proof: `POST /v2/pre-recorded -H "x-gladia-key: <KEY>" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/"}'` vs canary URL; compare `error_message`/`status`/duration. CVSS 3.1: 7.1 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N). Channel: Gladia security channel per scope.yml.

---

### LEAD 3: app.gladia.io post-auth open redirect via `redirect_to` parameter
**Asset:** app.gladia.io — **HIGH priority in scope**
| Q | Answer |
|---|---|
| Q1 Scope? | YES — app.gladia.io in scope (High) |
| Q2 Attacker reach? | **CONDITIONAL** — `redirect_to` reflected in form action unauthenticated (passive confirmed), but **post-auth honoring requires authenticated Google SSO session** (HUMAN_ONLY). |
| Q3 Real impact? | MEDIUM — post-auth redirect to attacker domain enables phishing; OAuth code/state theft only if `redirect_to` reused as `redirect_uri` (PKCE S256 FIXED prevents this). |
| Q4 Passive proof? | **NO** — passive confirms reflection into form action; **post-auth behavior untestable without live session**. |
| Q5 Novel? | YES — not previously reported. |
| Q6 Not rejected? | YES — open redirect is not on rejected list. |
| Q7 Triager accept? | **HOLD** — plausible but unverified end-to-end. Sole gate is post-auth redirect (HUMAN_ONLY). |

**VERDICT: HOLD** — Reflection confirmed byte-fresh (100+ cycles): `GET /signin?redirect_to=https://evil.example.com` → form `action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"`. CSP has 0 `form-action` directives. OAuth `redirect_uri` FIXED (PKCE S256). Return-to cookie tamper-reset REJECTED. **Requires human OAuth session to validate post-auth Location**. Minimal proof: complete Google SSO with `?redirect_to=https://evil.example.com`, capture final 302 Location. CVSS 3.1: 5.4 (AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N). Channel: Gladia security channel.

---

### LEAD 4: api.gladia.io WebSocket auth token in URL query parameter
**Asset:** api.gladia.io — **HIGHEST priority in scope**
| Q | Answer |
|---|---|
| Q1 Scope? | YES |
| Q2 Attacker reach? | YES — token issued via `POST /v2/live` (key-gated), but token in `wss://...?token=<uuid>` URL leaks via Referer (WS upgrade), browser history, proxy/server logs. |
| Q3 Real impact? | HIGH — token theft = unauthorized live transcription sessions, real-time audio access. |
| Q4 Passive proof? | **PARTIAL** — spec confirms token-in-URL design; cannot observe live Referer leakage without initiating WS (AUTH_HELPED). |
| Q5 Novel? | YES. |
| Q6 Not rejected? | YES. |
| Q7 Triager accept? | **HOLD** — design flaw confirmed in OpenAPI spec; exploitation requires token issuance (key-gated) + Referer observation. |

**VERDICT: HOLD** — OpenAPI explicitly shows `InitStreamingResponse.url = "wss://api.gladia.io/v2/live?token=<uuid>"`. Token is bearer-equivalent for live session. **Requires AUTH_HELPED: POST /v2/live with valid key → observe token format → initiate WS → inspect upgrade Referer header → verify token reuse after disconnect**. CVSS 3.1: 7.5 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N). Channel: Gladia security channel.

---

### LEAD 5: api.gladia.io undocumented `/health` endpoint
**Asset:** api.gladia.io — **HIGHEST priority in scope**
| Q | Answer |
|---|---|
| Q1 Scope? | YES |
| Q2 Attacker reach? | YES — public, unauthenticated (200 OK) |
| Q3 Real impact? | **NO** — returns only `{"health":"OK"}` (15 bytes). No version, build info, dependency status, metadata. `?full=true`, `?format=json`, `/actuator/health` all return identical/404. |
| Q4 Passive proof? | YES — GET /health returns 200; verbose probes negative. |
| Q5 Novel? | YES — undocumented in OpenAPI. |
| Q6 Not rejected? | **NO** — **info disclosure of non-sensitive public data** (health check OK is standard, non-sensitive). Always-rejected list includes "info disclosure of public data". |
| Q7 Triager accept? | NO — no security impact. |

**VERDICT: INVALID** — Q3 FAIL (no real impact), Q6 FAIL (on always-rejected list: info disclosure of public/non-sensitive data).

---

### LEAD 6: api.gladia.io CORS wildcard with `x-gladia-key` allowed cross-origin
**Asset:** api.gladia.io — **HIGHEST priority in scope**
| Q | Answer |
|---|---|
| Q1 Scope? | YES |
| Q2 Attacker reach? | YES — public endpoints readable cross-origin |
| Q3 Real impact? | **LOW** — only public endpoints (/v1/models, /openapi.json, /health) readable cross-origin. **No credentials allowed** (`access-control-allow-credentials` absent). Authenticated endpoints return 401 but CORS headers still present — no credentialed cross-origin read possible. |
| Q4 Passive proof? | YES — confirmed static `access-control-allow-origin: *` + `access-control-allow-headers: x-gladia-key` on preflight and GET. |
| Q5 Novel? | YES. |
| Q6 Not rejected? | **NO** — **best practice / low-impact misconfig** (wildcard without credentials is standard misconfig, not directly exploitable for data theft). |
| Q7 Triager accept? | NO — no practical exploit without credentials. |

**VERDICT: INVALID** — Q3 FAIL (no real security impact), Q6 FAIL (best practice misconfig, not exploitable).

---

### LEAD 7: api.gladia.io `x-powered-by: Express` on CORS preflight only
**Asset:** api.gladia.io — **HIGHEST priority in scope**
| Q | Answer |
|---|---|
| Q1 Scope? | YES |
| Q2 Attacker reach? | YES — public OPTIONS preflight |
| Q3 Real impact? | **LOW** — framework fingerprinting only. Lowers bar for CVE targeting but no direct exploit. |
| Q4 Passive proof? | YES — confirmed: OPTIONS returns `x-powered-by: Express`; GET does not. |
| Q5 Novel? | YES. |
| Q6 Not rejected? | **NO** — **info disclosure / best practice** (tech stack disclosure is on rejected list). |
| Q7 Triager accept? | NO — not a vulnerability, just reconnaissance aid. |

**VERDICT: INVALID** — Q3 FAIL (no real impact), Q6 FAIL (tech stack disclosure / info disclosure of public data).

---

### LEAD 8: api.gladia.io IDOR on transcription file download `/{id}/file`
**Asset:** api.gladia.io — **HIGHEST priority in scope**
| Q | Answer |
|---|---|
| Q1 Scope? | YES |
| Q2 Attacker reach? | **CONDITIONAL** — key-gated (requires valid `x-gladia-key`). Cross-account test needs two keys. |
| Q3 Real impact? | HIGH — unauthorized access to other users' transcription data (PII, audio). |
| Q4 Passive proof? | **NO** — requires authenticated requests with different keys. |
| Q5 Novel? | YES. |
| Q6 Not rejected? | YES — IDOR/BOLA is high-value class. |
| Q7 Triager accept? | **HOLD** — plausible but unvalidated without keys. |

**VERDICT: HOLD** — Spec defines three GET `/{id}/file` endpoints; authorization model opaque. **Requires AUTH_HELPED with two accounts/keys**. Minimal proof: with key A, create transcription → get ID → with key B, GET `/{id}/file` → observe 200 (IDOR) vs 403. CVSS 3.1: 7.1 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N). Channel: Gladia security channel.

---

### LEAD 9: api.gladia.io query-param parsing injection on `/v1/history`
**Asset:** api.gladia.io — **HIGHEST priority in scope**
| Q | Answer |
|---|---|
| Q1 Scope? | YES |
| Q2 Attacker reach? | **CONDITIONAL** — key-gated (401 without key). |
| Q3 Real impact? | LOW-MEDIUM — filter bypass / prototype pollution on **own-tenant query only** (key-gated). No cross-tenant impact. |
| Q4 Passive proof? | **NO** — requires authenticated requests with injection payloads. |
| Q5 Novel? | YES. |
| Q6 Not rejected? | YES. |
| Q7 Triager accept? | **HOLD** — low impact (self-tenant only), key-gated, unvalidated. |

**VERDICT: HOLD** — Spec: `custom_metadata` object (additionalProperties:true), `status`/`kind` arrays, date filters in query string. NestJS deep-parse foot-gun possible. **Requires AUTH_HELPED with key**. Minimal proof: `GET /v1/history?custom_metadata[__proto__][x]=1` → observe 500/altered results. CVSS 3.1: 4.3 (AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N). Channel: Gladia security channel.

---

### LEAD 10: app.gladia.io return-to cookie (unsigned base64url JSON, no JWT signature)
**Asset:** app.gladia.io — **HIGH priority in scope**
| Q | Answer |
|---|---|
| Q1 Scope? | YES |
| Q2 Attacker reach? | YES — cookie set on root `/` |
| Q3 Real impact? | **NO** — server **rejects tampered cookie and resets to default** `{"url":"/"}`. No open redirect via cookie tampering. |
| Q4 Passive proof? | YES — tampering test done, server resets. |
| Q5 Novel? | N/A — no vulnerability. |
| Q6 Not rejected? | N/A |
| Q7 Triager accept? | NO — tested and mitigated. |

**VERDICT: INVALID** — Q3 FAIL (server-side validation prevents exploit). Previously hypothesized, now confirmed mitigated.

---

## SUMMARY VERDICTS

| Lead | Verdict | Reason |
|---|---|---|
| 1. npm `gladia@0.1.3` impersonation | **INVALID (Gladia)** / **VALID (npm T&S)** | Out of scope asset; report to npm Trust & Safety |
| 2. api.gladia.io SSRF (audio_url/callback) | **HOLD** | High-value class, spec-confirmed, needs AUTH_HELPED key |
| 3. app.gladia.io post-auth open redirect | **HOLD** | Reflection confirmed, post-auth honoring needs HUMAN_ONLY session |
| 4. api.gladia.io WS token in URL | **HOLD** | Design flaw in spec, needs AUTH_HELPED to observe Referer leakage |
| 5. api.gladia.io /health undocumented | **INVALID** | No sensitive data disclosed (always-rejected: public info disclosure) |
| 6. api.gladia.io CORS wildcard | **INVALID** | No credentials allowed, no practical exploit (best practice only) |
| 7. api.gladia.io x-powered-by Express | **INVALID** | Tech stack disclosure only (always-rejected: info disclosure) |
| 8. api.gladia.io IDOR /{id}/file | **HOLD** | High-value class, needs two keys for cross-account test |
| 9. api.gladia.io /v1/h
| 9. api.gladia.io /v1/history query injection | **HOLD** | Low impact (self-tenant), key-gated, unvalidated |
| 10. app.gladia.io return-to cookie | **INVALID** | Server rejects tampering, no exploit |

---

## ACTIONABLE NEXT STEPS (READ-ONLY PROBES)

The following **require program approval / valid credentials** and cannot be executed passively:

1. **[NEXT] PROBE (AUTH_HELPED)** — SSRF validation:
   ```
   POST https://api.gladia.io/v2/pre-recorded
   Headers: x-gladia-key: <VALID_KEY>, Content-Type: application/json
   Body: {"audio_url":"http://169.254.169.254/latest/meta-data/"}
   ```
   Compare `status`/`error_message`/duration vs canary URL (`http://<attacker-canary>`). Repeat for `video_url` on `/video/text/video-transcription` and `callback.url`.

2. **[NEXT] PROBE (AUTH_HELPED)** — WS token Referer leakage:
   ```
   POST https://api.gladia.io/v2/live -H "x-gladia-key: <VALID_KEY>" -H "Content-Type: application/json" -d '{}'
   → Extract token from response.url
   → Initiate WSS connection to wss://api.gladia.io/v2/live?token=<uuid>
   → Inspect upgrade request headers for Referer
   → Verify token reuse after disconnect
   ```

3. **[NEXT] PROBE (HUMAN_ONLY)** — Post-auth open redirect:
   ```
   1. Authenticate to app.gladia.io via Google SSO
   2. GET https://app.gladia.io/signin?redirect_to=https://evil.example.com
   3. Complete OAuth flow
   4. Capture final HTTP 302 Location header
   5. Test variants: //evil.example.com, https://app.gladia.io.evil.example.com/
   ```

4. **[NEXT] PROBE (AUTH_HELPED)** — IDOR cross-account:
   ```
   With key A: POST /v2/pre-recorded → get transcription ID
   With key B: GET /v2/pre-recorded/{id}/file → observe 200 vs 403
   ```

5. **[NEXT] PROBE (AUTH_HELPED)** — Query injection:
   ```
   GET /v1/history?custom_metadata[__proto__][x]=1
   GET /v1/history?custom_metadata[$ne]=null
   GET /v1/history?date[gt]=...
   ```

---

## REPORTING CHANNEL
Per `scope.yml`: **"TBD - operator-provided program scope (update once public channel confirmed)"**. The human-validated lead confirms: `https://gladia.io/bug-bounty-report` (301→www→302→Google Forms, Google SSO auth-gated).

For npm `gladia@0.1.3`: **npm Trust & Safety** (`https://www.npmjs.com/support`) — separate venue, root cause is npm registry policy.
