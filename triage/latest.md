===== TRIAGE 2026-10-10 07:19:32 UTC =====
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
[0m→ [0mRead leads/reposcan-latest.md
[0m→ [0mRead reports/hypotheses.md
Now I have a complete picture of all leads from the various models. Let me evaluate each unique lead against the 7-Question Gate.

---

## TRIAGE VERDICTS

### LEAD 1: npm `gladia@0.1.3` orphaned impersonation + API key leakage in WS URL
**Asset:** npm registry (gladia@0.1.3) — **OUT OF SCOPE** per scope.yml (not Gladia-owned asset)
| Q | Answer |
|---|--------|
| Q1 | **NO** — npm registry is third-party; package not owned/operated by Gladia |
| Q2 | YES — public npm registry |
| Q3 | YES — supply-chain key harvesting, account takeover risk |
| Q4 | YES — passive metadata + tarball inspection |
| Q5 | YES — novel impersonation + key-in-URL design flaw |
| Q6 | NO — **always-rejected: third-party service not owned by Gladia** (scope.yml line 20) |
| Q7 | NO — triager would reject as OOS |

**VERDICT: INVALID** — Asset is third-party npm registry, not in program scope. Report to npm Trust & Safety, not Gladia.

---

### LEAD 2: SSRF via `audio_url`/`video_url`/`callback_url` server-side fetch on `api.gladia.io`
**Asset:** `api.gladia.io` (HIGHEST priority)
| Q | Answer |
|---|--------|
| Q1 | **YES** — api.gladia.io is HIGHEST priority asset |
| Q2 | **NO** — requires valid `x-gladia-key` (AUTH_HELPED); no unauthenticated access |
| Q3 | **YES** — cloud metadata (169.254.169.254), internal network access, data exfiltration |
| Q4 | **NO** — requires authenticated POST with valid key; cannot prove passively |
| Q5 | YES — SSRF-by-design confirmed in spec (no scheme allowlist), frozen surface |
| Q6 | YES — not on rejected list; high-impact SSRF class |
| Q7 | **CONDITIONAL** — real vuln IF key-gated fetch reaches internal endpoints, but unproven without key |

**VERDICT: HOLD** — High-value target but **cannot prove without valid API key**. Auth-gated SSRF is real risk but needs AUTH_HELPED validation.  
**Minimal proof (requires key):** `POST /v2/pre-recorded -H "x-gladia-key: <KEY>" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/"}'` — compare error/status/timing vs benign URL.  
**Impact:** Cloud metadata read, internal network SSRF — **CVSS 3.1: 7.1 (High) AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N**  
**Channel:** Gladia security (per scope.yml disclosure_policy)

---

### LEAD 3: Post-auth open redirect via `redirect_to` on `app.gladia.io/signin`
**Asset:** `app.gladia.io` (HIGH priority)
| Q | Answer |
|---|--------|
| Q1 | **YES** — app.gladia.io is HIGH priority |
| Q2 | **PARTIAL** — reflection is unauthenticated (GET), but exploit requires post-auth session |
| Q3 | **YES** — phishing, OAuth flow manipulation; Medium (High if redirect_uri injectable) |
| Q4 | **NO** — post-auth behavior **cannot be verified passively**; requires HUMAN OAuth session |
| Q5 | YES — CSP form-action gap (0 directives) confirmed, redirect_to reflection byte-fresh |
| Q6 | YES — not rejected class |
| Q7 | **CONDITIONAL** — real if server honors redirect_to post-auth; unproven |

**VERDICT: HOLD** — Reflection confirmed, CSP gap confirmed, but **post-auth honoring untestable passively**. Requires authorized Google OAuth session.  
**Minimal proof (HUMAN):** Complete Google OAuth via `/signin?redirect_to=https://evil.example.com`, capture final 302 Location.  
**Impact:** Post-auth phishing redirect — **CVSS 3.1: 5.4 (Medium) AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N**  
**Channel:** Gladia security

---

### LEAD 4: WebSocket auth token in URL query param (`wss://api.gladia.io/v2/live?token=<uuid>`)
**Asset:** `api.gladia.io` (HIGHEST)
| Q | Answer |
|---|--------|
| Q1 | **YES** — api.gladia.io HIGHEST |
| Q2 | **NO** — token only issued after authenticated `POST /v2/live` with valid key |
| Q3 | **YES** — token in URL leaks via Referer, browser history, proxy/logs; bearer-equivalent for live session |
| Q4 | **NO** — requires valid key to initiate session and observe token format |
| Q5 | YES — design flaw per OpenAPI spec (InitStreamingResponse.url) |
| Q6 | YES — credential-in-URL is recognized auth hygiene flaw |
| Q7 | **CONDITIONAL** — real design flaw, but exploit requires session token issuance |

**VERDICT: HOLD** — Design flaw confirmed in spec, but **token issuance requires valid API key**. Cannot prove token leakage without initiating live session.  
**Minimal proof (requires key):** `POST /v2/live -H "x-gladia-key: <KEY>"` → observe `url` with `token=` query param; initiate WS and inspect Referer headers.  
**Impact:** Session token theft → unauthorized live transcription, audio access — **CVSS 3.1: 6.5 (Medium) AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N**  
**Channel:** Gladia security

---

### LEAD 5: Undocumented `/health` endpoint on `api.gladia.io`
**Asset:** `api.gladia.io` (HIGHEST)
| Q | Answer |
|---|--------|
| Q1 | **YES** — api.gladia.io HIGHEST |
| Q2 | **YES** — public, unauthenticated GET returns 200 |
| Q3 | **NO** — returns only `{"health":"OK"}` (15 bytes); no version, build, metadata leaked. Probed `?full=true`, `?format=json` — identical response. |
| Q4 | YES — fully passive |
| Q5 | NO — undocumented endpoint but no sensitive disclosure |
| Q6 | **YES** — **always-rejected: info disclosure of non-sensitive public data** |
| Q7 | NO — reasonable triager rejects as non-vuln |

**VERDICT: INVALID** — No security impact; returns static health string only.

---

### LEAD 6: Tech stack disclosure via `x-powered-by: Express` on CORS preflight
**Asset:** `api.gladia.io` (HIGHEST)
| Q | Answer |
|---|--------|
| Q1 | **YES** — api.gladia.io HIGHEST |
| Q2 | **YES** — OPTIONS preflight returns header; public, unauthenticated |
| Q3 | **NO** — framework fingerprinting alone is reconnaissance aid, not exploit |
| Q4 | YES — passive OPTIONS probe |
| Q5 | NO — well-known misconfiguration class |
| Q6 | **YES** — **always-rejected: best practice / info disclosure alone** |
| Q7 | NO — triager rejects as non-vuln (no direct exploit) |

**VERDICT: INVALID** — Reconnaissance aid only; no direct security impact.

---

### LEAD 7: IDOR on transcription file download endpoints `/{id}/file`
**Asset:** `api.gladia.io` (HIGHEST)
| Q | Answer |
|---|--------|
| Q1 | **YES** — api.gladia.io HIGHEST |
| Q2 | **NO** — requires valid `x-gladia-key` + valid transcription ID from another user |
| Q3 | **YES** — cross-tenant transcription data (PII, audio) access |
| Q4 | **NO** — cannot verify object-level authorization without two accounts/keys |
| Q5 | YES — spec shows 3 file download endpoints with opaque ownership model |
| Q6 | YES — IDOR is high-value class |
| Q7 | **CONDITIONAL** — plausible but completely unproven without cross-account test |

**VERDICT: HOLD** — Spec suggests risk but **zero evidence without two valid keys**. Purely speculative.  
**Minimal proof (requires 2 keys):** POST `/v2/pre-recorded` with key A → GET `/v2/transcription/{id_from_A}/file` with key B → observe 200 vs 403.

---

### LEAD 8: Query-param parsing injection on `/v1/history` (`custom_metadata` object, array params)
**Asset:** `api.gladia.io` (HIGHEST)
| Q | Answer |
|---|--------|
| Q1 | **YES** — api.gladia.io HIGHEST |
| Q2 | **NO** — key-gated (401 without key) |
| Q3 | **LOW** — prototype pollution / filter bypass on own-tenant query only |
| Q4 | **NO** — requires valid key to test injection payloads |
| Q5 | YES — unusual object/array query params in GET |
| Q6 | YES — not rejected class |
| Q7 | **UNLIKELY** — low impact, key-gated, own-tenant only |

**VERDICT: INVALID** — Low impact, key-gated, no cross-tenant impact. Prototype pollution on own query is not a vulnerability.

---

### LEAD 9: `return-to` cookie JWT parsing without signature verification
**Asset:** `app.gladia.io` (HIGH)
| Q | Answer |
|---|--------|
| Q1 | **YES** — app.gladia.io HIGH |
| Q2 | YES — cookie set on root `/` |
| Q3 | **NO** — server **rejects tampered cookie and resets to default** `{"url":"/"}` (confirmed by multiple models) |
| Q4 | YES — passive tamper test done |
| Q5 | NO — tested and disproven |
| Q6 | N/A |
| Q7 | NO — disproven |

**VERDICT: INVALID** — Server validates/resets cookie; no open redirect via cookie tampering.

---

### LEAD 10: CORS wildcard reflects arbitrary origin
**Asset:** `api.gladia.io` (HIGHEST)
| Q | Answer |
|---|--------|
| Q1 | **YES** — api.gladia.io HIGHEST |
| Q2 | YES — public |
| Q3 | **NO** — probe confirms **static `*` not Origin reflection**; no credentials allowed |
| Q4 | YES — passive |
| Q5 | NO — tested and disproven |
| Q6 | N/A |
| Q7 | NO — disproven |

**VERDICT: INVALID** — Static `*`, no credential support, no origin reflection.

---

## SUMMARY

| Lead | Verdict | Reason |
|------|---------|--------|
| npm `gladia@0.1.3` impersonation + key leak | **INVALID** | Third-party asset (npm registry) — OUT OF SCOPE |
| SSRF via audio_url/video_url/callback_url | **HOLD** | High-value, spec-confirmed, but **requires valid API key** (AUTH_HELPED) |
| Post-auth open redirect via redirect_to | **HOLD** | Reflection + CSP gap confirmed, but **post-auth honoring untestable passively** (HUMAN_ONLY) |
| WS token in URL query param | **HOLD** | Design flaw in spec, but **token issuance requires valid key** |
| Undocumented /health endpoint | **INVALID** | No sensitive disclosure — static `{"health":"OK"}` only |
| x-powered-by: Express on preflight | **INVALID** | Reconnaissance aid only — best practice, no direct impact |
| IDOR on /{id}/file endpoints | **HOLD** | Spec suggests risk but **zero evidence without two keys** |
| Query-param injection on /v1/history | **INVALID** | Low impact, key-gated, own-tenant only |
| return-to cookie JWT parsing | **INVALID** | Disproven — server resets tampered cookie |
| CORS wildcard Origin reflection | **INVALID** | Disproven — static `*`, no reflection |

---

## NEXT ACTIONS (for HOLD items)

1. **SSRF (api.gladia.io)** — `[NEXT] PROBE: POST https://api.gladia.io/v2/pre-recorded -H "x-gladia-key: <VALID_KEY>" -H "Content-Type: application/json" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/"}'` — compare error/status/timing vs benign URL
2. **Post-auth redirect (app.gladia.io)** — `[NEXT] HUMAN: Complete Google OAuth via /signin?redirect_to=https://evil.example.com, capture final 302 Location`
3. **WS token leakage (api.gladia.io)** — `[NEXT] PROBE: POST https://api.gladia.io/v2/live -H "x-gladia-key: <VALID_KEY>" -H "Content-Type: application/json" -d '{}' → observe response.url token format; initiate WS and inspect Referer`

**Reporting channel for VALID findings:** Gladia Bug Bounty form at `https://gladia.io/bug-bounty-report` (Google Forms, SSO-gated) per scope.yml disclosure_policy.
