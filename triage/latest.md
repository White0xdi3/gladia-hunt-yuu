===== TRIAGE 2026-10-03 08:20:39 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/scope.yml"[90m 1 match[0m
[0m✱ [0mGlob "**/*.md"[90m 21 matches[0m
[0m→ [0mRead scope.yml
[0m→ [0mRead probe-results.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead reports/hypotheses.md
Now I have a complete picture of all the leads. Let me evaluate each distinct hypothesis against the 7-Question Gate.

---

## TRIAGE VERDICTS

### 1. npm `gladia@0.1.3` Orphaned Impersonation + Key-in-URL
**Asset:** npm registry (gladia@0.1.3, dist-tag latest) — **IN SCOPE** (Official SDKs npm/PyPI = MEDIUM)

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** — npm package is explicitly in scope (Medium priority) |
| Q2 Attacker reachable? | **YES** — Public npm registry, no auth needed to install/view |
| Q3 Real impact? | **YES** — Supply-chain impersonation ("Official" claim vs personal repo/maintainer 404) + raw API key leaked in WS URL query (src/client.ts:306-308) → key harvesting via proxy/access logs, irrevocable account takeover risk (orphaned GitHub user+repo) |
| Q4 Passive proof? | **YES** — All evidence via `npm view`, tarball inspection, GitHub API 404, source code RAG (sha256 `3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2` locked across 10+ reproductions) |
| Q5 Novel? | **YES** — Not previously reported; ownership anomaly + credential-hygiene flaw in same package |
| Q6 Not on reject list? | **YES** — Not info disclosure of public data, not best-practice, not self-XSS; this is active impersonation + key exposure |
| Q7 Triager accepts? | **YES** — Clear supply-chain vulnerability with reproducible evidence |

**VERDICT: VALID**  
**Minimal proof:** `npm view gladia@0.1.3` → description "Official", maintainer `softwarecitadel`, repo `alexisbouchez/gladia.ts` (404 user+repo); tarball src/client.ts:306-308 `searchParams.append('x-gladia-key', apiKey)` → WebSocket URL query leak.  
**Impact:** Supply-chain API key harvesting + irrevocable account takeover (P3/P4)  
**CVSS 3.1:** 8.2 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N)  
**Channel:** Gladia security channel (security@gladia.io or bug-bounty-report form) + npm Trust & Safety

---

### 2. SSRF via audio_url/video_url/callback_config.url on api.gladia.io
**Asset:** api.gladia.io (POST /v2/pre-recorded, /v2/upload, /v2/live, legacy /audio|/video/*) — **IN SCOPE** (HIGHEST)

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** — api.gladia.io is Highest priority |
| Q2 Attacker reachable? | **NO (without key)** — All endpoints return 401 without `x-gladia-key`; requires valid API key (AUTH_HELPED) |
| Q3 Real impact? | **YES (conditional)** — Cloud metadata (169.254.169.254), internal network read, callback POST SSRF → High severity IF key obtained |
| Q4 Passive proof? | **NO** — Cannot prove SSRF without valid key; spec confirms design but no passive confirmation of fetch behavior |
| Q5 Novel? | **YES** — SSRF-by-design in transcription API with no scheme allowlist |
| Q6 Not on reject list? | **YES** — Not a reject-class issue |
| Q7 Triager accepts? | **HOLD** — Requires AUTH_HELPED validation; cannot pass gate without key |

**VERDICT: HOLD** — Auth-gated; needs program-provided trial key to prove. Passive evidence: OpenAPI spec (format:uri, no allowlist), /v1/models FR/US egress, SDK RAG (no client-side validation).  
**Next step:** [NEXT] PROBE with valid key: `POST /v2/pre-recorded -H "x-gladia-key: <KEY>" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/"}'`

---

### 3. Post-Auth Open Redirect via redirect_to on app.gladia.io/signin
**Asset:** app.gladia.io (HIGH)

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** — app.gladia.io is High priority |
| Q2 Attacker reachable? | **PARTIAL** — Reflection is public (GET /signin?redirect_to= reflects into form action), but post-auth honoring requires authenticated session (HUMAN_ONLY) |
| Q3 Real impact? | **CONDITIONAL** — Post-auth redirect to attacker domain → phishing; OAuth code theft ONLY if redirect_to reused as redirect_uri (OAuth redirect_uri is FIXED PKCE S256, so code theft path blocked) |
| Q4 Passive proof? | **NO** — Cannot prove post-auth behavior without session |
| Q5 Novel? | **YES** — CSP form-action gap (0 directives) + reflection across all host-confusion variants confirmed |
| Q6 Not on reject list? | **YES** — Not self-XSS, not best-practice |
| Q7 Triager accepts? | **HOLD** — Unverified post-auth gate; redirect_to reflection alone is not a vulnerability without proof of honoring |

**VERDICT: HOLD** — Requires authenticated session to verify post-auth Location header. Passive evidence: form action reflection byte-fresh, CSP 0 form-action directives, OAuth redirect_uri FIXED.  
**Next step:** [NEXT] HUMAN: With authorized session, GET /signin?redirect_to=https://evil.example.com → complete Google OAuth → capture post-auth 302 Location.

---

### 4. Tech Stack Disclosure: x-powered-by: Express on CORS Preflight Only
**Asset:** api.gladia.io (OPTIONS responses) — **IN SCOPE** (HIGHEST)

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **YES** — OPTIONS preflight is public, no auth |
| Q3 Real impact? | **LOW** — Framework fingerprinting aids CVE targeting; no direct exploit |
| Q4 Passive proof? | **YES** — Confirmed via probe: `OPTIONS /v2/transcription` → `x-powered-by: Express` (204); `GET /v2/transcription` → 401, no x-powered-by |
| Q5 Novel? | **YES** — Preflight-only differential fingerprint |
| Q6 Not on reject list? | **NO** — **FAILS Q6** — This is "best practice / info disclosure of public data" class (framework header on preflight). Always-rejected per scope: "best practice, info disclosure of public data". |
| Q7 Triager accepts? | **NO** — Low-severity recon aid, not a vulnerability |

**VERDICT: INVALID** — Q6 fails (best-practice/framework-fingerprint class on always-rejected list).

---

### 5. Undocumented /health Endpoint on api.gladia.io
**Asset:** api.gladia.io — **IN SCOPE** (HIGHEST)

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **YES** — Public GET, no auth |
| Q3 Real impact? | **NO** — Returns only `{"health":"OK"}` (15B); no version, build info, dependency status; ?full=true, ?format=json return identical output |
| Q4 Passive proof? | **YES** — Probed and confirmed |
| Q5 Novel? | **NO** — Undocumented health endpoint returning minimal OK is common |
| Q6 Not on reject list? | **NO** — **FAILS Q6** — Info disclosure of public/benign data (health check) |
| Q7 Triager accepts? | **NO** |

**VERDICT: INVALID** — Q3 and Q6 fail (no real impact, benign info disclosure).

---

### 6. WebSocket Auth Token in URL Query Parameter (api.gladia.io)
**Asset:** api.gladia.io (/v2/live WebSocket) — **IN SCOPE** (HIGHEST)

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **NO (without key)** — Requires valid x-gladia-key to initiate session and get token URL (AUTH_HELPED) |
| Q3 Real impact? | **YES (conditional)** — Token in URL leaks via Referer, browser history, proxy/server logs → session hijacking |
| Q4 Passive proof? | **NO** — Cannot get token without key |
| Q5 Novel? | **YES** — Token-in-URL design per OpenAPI spec |
| Q6 Not on reject list? | **YES** |
| Q7 Triager accepts? | **HOLD** — Auth-gated |

**VERDICT: HOLD** — Requires valid API key to prove token format and leakage. Passive: OpenAPI spec confirms `wss://api.gladia.io/v2/live?token=<uuid>` design.  
**Next step:** [NEXT] PROBE with key: `POST /v2/live -H "x-gladia-key: <KEY>"` → observe response.url token format.

---

### 7. CORS Wildcard Reflects Arbitrary Origin (Origin Echo)
**Asset:** api.gladia.io — **IN SCOPE** (HIGHEST)

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **N/A** — **HYPOTHESIS DISPROVEN** |
| Q3 Real impact? | **N/A** |
| Q4 Passive proof? | **YES** — Probes confirm static `access-control-allow-origin: *` (NOT Origin reflection) |
| Q5 Novel? | **N/A** |
| Q6 Not on reject list? | **N/A** |
| Q7 Triager accepts? | **N/A** |

**VERDICT: INVALID** — Hypothesis disproven by passive probes (static `*`, no credentials). Not a vulnerability.

---

### 8. IDOR on Transcription File Download /{id}/file
**Asset:** api.gladia.io — **IN SCOPE** (HIGHEST)

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **NO (without key)** — All endpoints key-gated (401) |
| Q3 Real impact? | **YES (conditional)** — Cross-account transcription data (PII, audio) → High |
| Q4 Passive proof? | **NO** — Requires valid key + valid ID owned by another user |
| Q5 Novel? | **YES** |
| Q6 Not on reject list? | **YES** |
| Q7 Triager accepts? | **HOLD** — Auth-gated, confidence ~50 |

**VERDICT: HOLD** — Requires AUTH_HELPED with valid key. PARKED in multiple models.

---

### 9. Query-Param Parsing Injection on /v1/history
**Asset:** api.gladia.io — **IN SCOPE** (HIGHEST)

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **NO (without key)** — Endpoint key-gated (401) |
| Q3 Real impact? | **LOW-MED** — Filter bypass / prototype pollution on own-tenant query |
| Q4 Passive proof? | **NO** — Requires key + injection payloads |
| Q5 Novel? | **YES** — Object/array query params in URL |
| Q6 Not on reject list? | **YES** |
| Q7 Triager accepts? | **HOLD** — Auth-gated |

**VERDICT: HOLD** — Requires AUTH_HELPED with valid key.

---

### 10. OpenAPI Shadow Endpoints / Undocumented v2 Paths
**Asset:** api.gladia.io — **IN SCOPE** (HIGHEST)

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **YES** — Public endpoints |
| Q3 Real impact? | **NO** — Probed /admin, /debug, /health, /metrics, /v1/, /internal/, /actuator/health → all 404; NO_DRIFT confirmed 100+ cycles |
| Q4 Passive proof? | **YES** — Probed and confirmed absent |
| Q5 Novel? | **NO** — No shadow endpoints found |
| Q6 Not on reject list? | **N/A** |
| Q7 Triager accepts? | **NO** — No vulnerability exists |

**VERDICT: INVALID** — No shadow endpoints; surface frozen.

---

### 11. return-to Cookie JWT Parsing Without Signature Verification
**Asset:** app.gladia.io — **IN SCOPE** (HIGH)

| Q | Answer |
|---|---|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **YES** — Cookie set on root `/` |
| Q3 Real impact? | **NO** — Server REJECTS tampered cookie, resets to default `{"url":"/"}`; no open redirect |
| Q4 Passive proof? | **YES** — Tested and confirmed server-side validation/reset |
| Q5 Novel? | **NO** — Mitigated by design |
| Q6 Not on reject list? | **N/A** |
| Q7 Triager accepts? | **NO** — Mitigated, not a vulnerability |

**VERDICT: INVALID** — Q3 fails (server validates/resets; no exploit).

---

## SUMMARY

| Lead | Verdict |
|------|---------|
| npm `gladia@0.1.3` orphaned impersonation + key-in-URL | **VALID** (report-ready) |
| SSRF via audio_url/video_url/callback_config.url | **HOLD** (needs key) |
| Post-auth open redirect via redirect_to | **HOLD** (needs session) |
| x-powered-by: Express on preflight only | **INVALID** (best-practice/reject-list) |
| Undocumented /health endpoint | **INVALID** (benign info disclosure) |
| WebSocket token in URL query | **HOLD** (needs key) |
| CORS Origin reflection | **INVALID** (disproven) |
| IDOR on /{id}/file download | **HOLD** (needs key) |
| /v1/history query-param injection | **HOLD** (needs key) |
| OpenAPI shadow endpoints | **INVALID** (none found) |
| return-to cookie JWT parsing | **INVALID** (mitigated) |

---

## IMMEDIATE ACTIONABLE REPORT

**Only ONE lead passes all 7 gates with passive evidence: the npm `gladia@0.1.3` orphaned impersonation.**

**Report package (copy-paste ready):**
```
Package: https://www.npmjs.com/package/gladia (v0.1.3, dist-tag latest)
Issue: Impersonation of Gladia (gladia.io) official SDK + credential hygiene flaw

Evidence:
1. Description claims "Official TypeScript SDK for Gladia - State-of-the-art Speech to Text API"
2. Maintainer: softwarecitadel (softwarecitadel@gmail.com) — no Gladia affiliation
3. Repository github.com/alexisbouchez/gladia.ts returns 404; user alexisbouchez 404 (orphaned, irrevocable)
4. Genuine SDK: @gladiaio/sdk@1.1.0 published by bot-npmjs-gladiaio under Gladia org
5. README.md line 3: "Unofficial TypeScript SDK for Gladia" — contradicts package.json "Official"
6. src/client.ts:306-308 embeds raw x-gladia-key in WebSocket URL query:
   wsUrl.searchParams.append('x-gladia-key', this.apiKey)
   new WebSocket(wsUrl.toString())  // wss://api.gladia.io/v2/live?x-gladia-key=<KEY>
7. Tarball sha256: 3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2 (locked 10+ reproductions)

Requested action: Transfer name to Gladia / unpublish for impersonation + abandoned-package policy.
Severity: MEDIUM-HIGH (P3/P4) — supply-chain API key harvesting + irrevocable account takeover risk
```

**Submit via:** https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO) — per scope.yml disclosure policy. Also file with npm Trust & Safety (npmjs.com/support) for faster registry action.
