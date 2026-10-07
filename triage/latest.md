===== TRIAGE 2026-10-07 08:57:07 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/*"[90m 53 matches[0m
[0m→ [0mRead probe-results.md
[0m→ [0mRead scope.yml
[0m→ [0mRead new-leads.txt
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
Now I have a comprehensive view of all leads. Let me triage each distinct lead against the 7-Question Gate.

---

## LEAD 1: npm `gladia@0.1.3` orphaned impersonation + key-in-URL (WebSocket)

**Q1 Scope**: YES — npm package `gladia` listed in scope.yml under `npm_packages` (gladia)
**Q2 Reachable**: YES — Public npm registry, no auth required
**Q3 Impact**: YES — Supply-chain impersonation (false "Official" claim) + credential hygiene hazard (raw API key in WS URL query string leaks to proxy/access logs, browser history, URL sharing)
**Q4 Passive proof**: YES — Registry metadata + tarball source inspection confirms: description="Official TypeScript SDK", README="Unofficial", maintainer=softwarecitadel@gmail.com, repo=alexisbouchez/gladia.ts (404 user+repo), src/client.ts:306-308 `searchParams.append('x-gladia-key', apiKey)` → WebSocket URL
**Q5 Novel**: YES — Not previously reported to Gladia (human report sent 2026-08-12 but no vendor action; independent validation ongoing)
**Q6 Not rejected**: YES — Not info-disclosure/best-practice/self-XSS; real supply-chain + credential exposure
**Q7 Triager accept**: YES — Clear impersonation + key leak in URL; actionable

**VERDICT: VALID**

**Minimal read-only proof steps**:
1. `npm view gladia@0.1.3 description repository.url maintainer` → shows "Official", personal repo, personal maintainer
2. Download tarball: `npm pack gladia@0.1.3` → inspect `package/src/client.ts:306-308` → `wsUrl.searchParams.append('x-gladia-key', this.apiKey)`
3. `curl -s https://api.github.com/repos/alexisbouchez/gladia.ts` → 404 (orphaned)
4. Compare with official `@gladiaio/sdk` → uses header auth + short-lived session URL, never key in query

**Impact**: Supply-chain API key harvesting (P3/P4); irrevocable takeover risk (orphaned GitHub account)

**CVSS 3.1**: 7.4 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N) — Network, Low complexity, No auth, No UI, High confidentiality (keys in logs)

**Reporting channel**: Gladia security channel per scope.yml → https://gladia.io/bug-bounty-report (Google Forms, SSO-gated) + npm Trust & Safety (registry impersonation)

---

## LEAD 2: app.gladia.io `/signin?redirect_to=` reflection → post-auth open redirect

**Q1 Scope**: YES — app.gladia.io listed as High priority
**Q2 Reachable**: YES — Unauthenticated GET reflects `redirect_to` into form `action` attribute (probe: HTTP 200, `action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"`)
**Q3 Impact**: CONDITIONAL — Only if server honors `redirect_to` **after** successful Google OAuth. Current evidence: reflection confirmed, CSP lacks `form-action` (0 directives), OAuth `redirect_uri` FIXED (PKCE S256 prevents code theft), return-to cookie tamper REJECTED. Post-auth behavior **unverified** (requires human session)
**Q4 Passive proof**: PARTIAL — Reflection proven passively; post-auth honoring requires AUTH_HELPED
**Q5 Novel**: YES — Not previously reported as validated vuln
**Q6 Not rejected**: YES — Not self-XSS/rate-limit; potential post-auth redirect is real class
**Q7 Triager accept**: HOLD — Cannot confirm end-to-end without authenticated session

**VERDICT: HOLD** — Post-auth honoring unverified (AUTH_HELPED gate). Reflection + CSP gap confirmed; needs human OAuth test.

**[NEXT] PROBE**: Human: Authenticate via Google SSO to app.gladia.io, then GET `/signin?redirect_to=https://evil.example.com`, complete OAuth, observe final `Location` header. Test variants: `//evil.example.com`, `https://app.gladia.io.evil.example.com/`.

---

## LEAD 3: api.gladia.io SSRF via `audio_url`/`video_url`/`callback_config.url` (no scheme allowlist)

**Q1 Scope**: YES — api.gladia.io (Highest priority)
**Q2 Reachable**: AUTH_GATED — All endpoints return HTTP 401 without `x-gladia-key` (probe: consistent 401 across 100+ cycles)
**Q3 Impact**: YES — Cloud metadata (169.254.169.254) + internal network read via server-side fetch; 7 webhook delivery paths; FR/US egress confirmed
**Q4 Passive proof**: NO — Spec confirms surface (`format:uri`, no allowlist), but reachability requires valid key + observing error/timing differential
**Q5 Novel**: YES — SSRF-by-design surface documented, not exploited
**Q6 Not rejected**: YES — Not best-practice; real SSRF class if reachable
**Q7 Triager accept**: HOLD — Key-gated; no bypass found; AUTH_HELPED only

**VERDICT: HOLD** — SSRF-by-design spec confirmed (frozen 100+ cycles), but requires valid `x-gladia-key` for POC. No unauthenticated bypass.

**[NEXT] PROBE**: AUTH_HELPED: With valid `x-gladia-key`, POST `/v2/pre-recorded {"audio_url":"http://169.254.169.254/latest/meta-data/"}` vs control; compare `error_message`/`status`/duration. Repeat via `/video/text/video-transcription` (legacy) and `callback_config.url` (outbound POST).

---

## LEAD 4: api.gladia.io IDOR on `/v2/transcription/{id}/file`, `/v2/pre-recorded/{id}/file`, `/v2/live/{id}/file`

**Q1 Scope**: YES — api.gladia.io
**Q2 Reachable**: AUTH_GATED — All endpoints return 401 without key
**Q3 Impact**: YES — Cross-account transcription data access (PII, audio)
**Q4 Passive proof**: NO — Spec shows endpoints but no ownership-binding logic visible; requires two valid keys from different accounts
**Q5 Novel**: YES — Not tested
**Q6 Not rejected**: YES — Real IDOR class
**Q7 Triager accept**: HOLD — AUTH_HELPED, needs two accounts/keys

**VERDICT: HOLD** — Spec-only hypothesis; cannot verify without authorized multi-account testing.

---

## LEAD 5: api.gladia.io `x-powered-by: Express` on CORS preflight only

**Q1 Scope**: YES — api.gladia.io
**Q2 Reachable**: YES — Passive OPTIONS probe confirms (probe: OPTIONS returns `x-powered-by: Express`, GET does not)
**Q3 Impact**: NO — Framework fingerprinting only; aids recon but no direct exploit
**Q4 Passive proof**: YES — Confirmed via probe
**Q5 Novel**: NO — Known low-severity misconfig class
**Q6 Not rejected**: NO — Falls under "best practice / info disclosure" (recon aid only)
**Q7 Triager accept**: NO — Low severity, not a vulnerability

**VERDICT: INVALID** — Recon aid only; rejected per always-rejected list (info disclosure / best practice)

---

## LEAD 6: api.gladia.io CORS wildcard (`*`) with `x-gladia-key` allowed cross-origin

**Q1 Scope**: YES — api.gladia.io
**Q2 Reachable**: YES — Preflight allows `Access-Control-Request-Headers: x-gladia-key`
**Q3 Impact**: NO — No `Access-Control-Allow-Credentials: true`; cannot exfiltrate authenticated responses cross-origin. Only enables unauthenticated cross-origin reads of public endpoints (`/v1/models`, `/openapi.json`, `/health`)
**Q4 Passive proof**: YES — Probe confirms
**Q5 Novel**: NO — Standard CORS config
**Q6 Not rejected**: NO — No credential support = not exploitable for credentialed attacks
**Q7 Triager accept**: NO

**VERDICT: INVALID** — Wildcard without credentials; public endpoints only; not a vulnerability

---

## LEAD 7: api.gladia.io WebSocket auth token in URL query param (`wss://api.gladia.io/v2/live?token=<uuid>`)

**Q1 Scope**: YES — api.gladia.io (OpenAPI spec documents this)
**Q2 Reachable**: AUTH_GATED — Requires valid key to initiate session via POST `/v2/live`
**Q3 Impact**: LOW — Token in URL leaks to proxy/access logs, but token is short-lived session token (not long-lived API key). Official SDK uses this flow.
**Q4 Passive proof**: SPEC ONLY — OpenAPI documents `url` field with token; cannot verify token lifetime without key
**Q5 Novel**: NO — Documented design
**Q6 Not rejected**: NO — Design choice, not a flaw; token != API key
**Q7 Triager accept**: NO

**VERDICT: INVALID** — Documented short-lived session token in URL; not the long-lived API key. Different from Lead 1 (npm SDK leaks *API key*).

---

## LEAD 8: api.gladia.io `/v1/history` query-param parsing injection (`custom_metadata` object, `status`/`kind` arrays)

**Q1 Scope**: YES — api.gladia.io
**Q2 Reachable**: AUTH_GATED — 401 without key
**Q3 Impact**: LOW-MED — Filter bypass / prototype pollution on own-tenant query (key-gated)
**Q4 Passive proof**: NO — Spec shows complex query parsing; needs key to test injection
**Q5 Novel**: YES — Not previously tested
**Q6 Not rejected**: YES — Real parsing foot-gun class
**Q7 Triager accept**: HOLD — AUTH_HELPED only

**VERDICT: HOLD** — Spec-confirmed complex query parsing (NestJS deep-parse); needs valid key to test `custom_metadata[__proto__]` etc.

---

## LEAD 9: app.gladia.io `/dashboard` SPA shell served 200 without auth

**Q1 Scope**: YES — app.gladia.io
**Q2 Reachable**: YES — Probe: HTTP 200, `text/html`
**Q3 Impact**: NO — Client-side enforcement only; static shell, no data leakage
**Q4 Passive proof**: YES
**Q5 Novel**: NO — Common SPA pattern
**Q6 Not rejected**: NO — Best practice / info disclosure (public shell)
**Q7 Triager accept**: NO

**VERDICT: INVALID** — SPA shell without server-side auth is standard; no sensitive data exposed

---

## LEAD 10: api.gladia.io `/health` undocumented endpoint

**Q1 Scope**: YES — api.gladia.io
**Q2 Reachable**: YES — Probe: HTTP 200, `{"health":"OK"}` (15B)
**Q3 Impact**: NO — No verbose output, no version/build metadata (`/health?full=true` returns same)
**Q4 Passive proof**: YES
**Q5 Novel**: NO
**Q6 Not rejected**: NO — Info disclosure of public health status
**Q7 Triager accept**: NO

**VERDICT: INVALID** — Benign health check; no sensitive data

---

## SUMMARY TABLE

| # | Lead | Verdict | Key Reason |
|---|------|---------|------------|
| 1 | npm `gladia@0.1.3` impersonation + key-in-WS-URL | **VALID** | Proven passively: false "Official" claim + orphaned repo + API key in URL query |
| 2 | app.gladia.io `/signin?redirect_to=` post-auth open redirect | **HOLD** | Reflection + CSP gap confirmed; post-auth honoring requires human OAuth test |
| 3 | api.gladia.io SSRF via `audio_url`/`video_url`/`callback_config.url` | **HOLD** | Spec-confirmed SSRF-by-design; key-gated (401), no bypass found |
| 4 | api.gladia.io IDOR on `/{id}/file` endpoints | **HOLD** | Spec-only; needs two authorized accounts |
| 5 | api.gladia.io `x-powered-by: Express` on preflight | **INVALID** | Recon aid only (best practice / info disclosure) |
| 6 | api.gladia.io CORS wildcard + `x-gladia-key` allowed | **INVALID** | No credentials; public endpoints only |
| 7 | api.gladia.io WS token in URL query | **INVALID** | Short-lived session token (design), not API key |
| 8 | api.gladia.io `/v1/history` query-param injection | **HOLD** | Spec-confirmed complex parsing; needs key |
| 9 | app.gladia.io `/dashboard` unauthenticated SPA shell | **INVALID** | Standard SPA pattern; no data leak |
| 10 | api.gladia.io `/health` undocumented | **INVALID** | Benign health check |

---

**NEXT ACTIONS FOR VALID LEAD (1)**:
- Submit report via https://gladia.io/bug-bounty-report (Google Forms, SSO) with evidence package
- File npm impersonation report via https://www.npmjs.com/support (registry policy)

**NEXT PROBES FOR HOLD LEADS (2,3,4,8)**:
- Lead 2: Human OAuth session test on app.gladia.io
- Lead 3: AUTH_HELPED SSRF test with valid `x-gladia-key` (program-provided or trial)
- Lead 4: AUTH_HELPED IDOR test with two valid keys
- Lead 8: AUTH_HELPED query injection test with valid key
