===== TRIAGE 2026-10-05 07:16:05 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/*"[90m 53 matches[0m
[0m→ [0mRead scope.yml
[0m→ [0mRead probe-results.txt
[0m→ [0mRead new-leads.txt
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead probe-results.md
Based on my analysis of all lead files and probe results, here are the **7-Question Gate verdicts** for each distinct high-value lead:

---

### 1. SSRF via `audio_url`/`video_url`/`callback_url` server-side fetch — **api.gladia.io** (HIGHEST priority)

| Q | Answer | Evidence |
|---|--------|----------|
| Q1 Scope? | **YES** | api.gladia.io is Highest in scope.yml |
| Q2 Reachable? | **AUTH_HELPED** | Endpoints key-gated (401 without `x-gladia-key`); keys obtainable via signup |
| Q3 Real impact? | **YES** | Cloud metadata (169.254.169.254), internal network enumeration, callback SSRF — High severity if proven |
| Q4 Passive proof? | **NO** | Requires POST with valid key to observe server-side fetch behavior (error/timing diff) |
| Q5 Novel? | **YES** | Spec confirms `format:uri` with no scheme allowlist; 7 webhook paths; FR/US egress |
| Q6 Not rejected? | **YES** | SSRF-to-metadata not on rejected list |
| Q7 Triager accept? | **CONDITIONAL** | Only with valid key POC; theoretical "SSRF-by-design" without key |

**VERDICT: HOLD** — Cannot be proven with GET/HEAD only. Spec + RAG frozen 100+ cycles confirm SSRF surface (no scheme allowlist, callback_url, FR/US egress), but passive validation blocked by key gate.  
**Next step**: `[NEXT] PROBE: POST https://api.gladia.io/v2/pre-recorded -H "x-gladia-key: <valid_key>" -H "Content-Type: application/json" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/","callback_url":"http://169.254.169.254/latest/meta-data/}'` (AUTH_HELPED)

---

### 2. npm `gladia@0.1.3` orphaned impersonation + key-in-URL — **npm registry** (MEDIUM priority)

| Q | Answer | Evidence |
|---|--------|----------|
| Q1 Scope? | **YES** | Official SDKs (@gladiaio/sdk) are Medium in scope.yml; impersonator directly related |
| Q2 Reachable? | **YES** | Public npm registry, dist-tag `latest=0.1.3` |
| Q3 Real impact? | **YES** | Supply-chain: "Official" claim vs README "Unofficial"; maintainer `softwarecitadel@gmail.com` (personal); repo `alexisbouchez/gladia.ts` 404 (orphaned/irrevocable takeover risk); **src/client.ts:306-308 embeds raw `x-gladia-key` in WS URL query** — keys leak to proxy/access logs |
| Q4 Passive proof? | **YES** | `npm view gladia@0.1.3` metadata + tarball inspection + GitHub API 404 all confirmed across 10+ independent reproductions |
| Q5 Novel? | **YES** | Human-validated 2026-08-22; reported 2026-08-12 to security@gladia.io; no vendor action |
| Q6 Not rejected? | **YES** | Supply-chain impersonation + credential exposure not on rejected list |
| Q7 Triager accept? | **YES** | Locked evidence across 5+ models, 10+ npm pack reproductions, report-ready |

**VERDICT: VALID** — **Reported 2026-08-12, awaiting vendor response.**  
**Minimal proof**: `npm view gladia@0.1.3 description repository.url maintainer` → "Official TypeScript SDK for Gladia" vs README "Unofficial"; repo/user 404; tarball sha256 `3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2` shows `searchParams.append('x-gladia-key', apiKey)` in WS URL.  
**Impact**: Medium-High (P3/P4) — supply-chain API key harvesting + irrevocable account takeover.  
**CVSS 3.1**: `AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N` (7.4 High)  
**Reporting channel**: Gladia security channel per scope.yml → `https://gladia.io/bug-bounty-report` (Google Forms, SSO auth-gated) or `security@gladia.io`

---

### 3. Post-OAuth open redirect via `redirect_to` — **app.gladia.io** (HIGH priority)

| Q | Answer | Evidence |
|---|--------|----------|
| Q1 Scope? | **YES** | app.gladia.io is High in scope.yml |
| Q2 Reachable? | **YES** | Public `/signin?redirect_to=` reflects URL-encoded value into form `action` (byte-fresh 100+ cycles) |
| Q3 Real impact? | **UNVERIFIED** | Only if server honors `redirect_to` post-Google-OAuth. OAuth `redirect_uri` is FIXED (PKCE S256) — no code/state theft. Return-to cookie tamper-reset REJECTED. |
| Q4 Passive proof? | **PARTIAL** | GET proves reflection into form action; **post-auth honoring requires HUMAN_ONLY session** |
| Q5 Novel? | **YES** | Consistently found across all models |
| Q6 Not rejected? | **YES** | Post-auth open redirect not on rejected list |
| Q7 Triager accept? | **HOLD** | Unverified post-auth behavior; reflection alone = info disclosure |

**VERDICT: HOLD** — Reflection confirmed passively; post-auth honoring untestable without authenticated Google SSO session.  
**Next step**: `[NEXT] HUMAN: Authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors redirect`

---

### 4. WebSocket auth token in URL query parameter — **api.gladia.io** (HIGHEST)

| Q | Answer | Evidence |
|---|--------|----------|
| Q1 Scope? | **YES** | api.gladia.io Highest |
| Q2 Reachable? | **YES** | Spec shows `InitStreamingResponse.url = "wss://api.gladia.io/v2/live?token=<uuid>"` |
| Q3 Real impact? | **YES** | Token-in-URL leaks via browser history, Referer headers, proxy/server logs; bearer-equivalent for live sessions |
| Q4 Passive proof? | **PARTIAL** | Spec confirms design; **Referrer-Policy on WS handshake + token lifetime require AUTH_HELPED** |
| Q5 Novel? | **YES** | Explicit in OpenAPI spec |
| Q6 Not rejected? | **YES** | Credential leakage via URL not on rejected list |
| Q7 Triager accept? | **CONDITIONAL** | Design flaw confirmed; exploitability depends on token scope/rotation and Referrer-Policy |

**VERDICT: HOLD** — Design flaw confirmed by spec (token in URL). Cannot verify Referrer-Policy or token rotation without valid key to initiate WS session.  
**Next step**: `[NEXT] PROBE: POST https://api.gladia.io/v2/live -H "x-gladia-key: <valid_key>" -H "Content-Type: application/json" -d '{}'` → observe response.url token format; initiate WS and inspect upgrade headers for Referer.

---

### 5. Undocumented `/health` endpoint — **api.gladia.io** (HIGHEST)

| Q | Answer | Evidence |
|---|--------|----------|
| Q1 Scope? | **YES** | api.gladia.io Highest |
| Q2 Reachable? | **YES** | Public, unauthenticated, returns 200 `{"health":"OK"}` |
| Q3 Real impact? | **NO** | No verbose mode (`?full=true`, `?format=json` return identical); no version/build/metadata disclosure |
| Q4 Passive proof? | **YES** | GET /health returns 200; absent from 14-path OpenAPI spec |
| Q5 Novel? | **YES** | Not in spec |
| Q6 Not rejected? | **NO** | **Fails** — "info disclosure of public data" is on always-rejected list |
| Q7 Triager accept? | **NO** | Public health check with no sensitive data |

**VERDICT: INVALID** — Fails Q3 (no real impact) and Q6 (rejected class: info disclosure of public health status). Multiple models rejected: `/health?full=true does NOT leak verbose output`.

---

### 6. CORS wildcard reflects arbitrary origin — **api.gladia.io** (HIGHEST)

| Q | Answer | Evidence |
|---|--------|----------|
| Q1 Scope? | **YES** | api.gladia.io Highest |
| Q2 Reachable? | **YES** | Public endpoints |
| Q3 Real impact? | **NO** | **Confirmed static `*`** — no Origin reflection. `access-control-allow-origin: *` without `access-control-allow-credentials` = standard wildcard, not exploitable for cross-origin reads of authenticated endpoints |
| Q4 Passive proof? | **YES** | Probes confirm static `*` on GET and OPTIONS |
| Q5 Novel? | **N/A** | Not a vulnerability |
| Q6 Not rejected? | **N/A** | |
| Q7 Triager accept? | **NO** | Not exploitable |

**VERDICT: INVALID** — Multiple models re-verified: "CORS wildcard returns static `*` (not reflecting request Origin)". Wildcard without credentials is not a vulnerability.

---

### 7. `x-powered-by: Express` on CORS preflight only — **api.gladia.io** (HIGHEST)

| Q | Answer | Evidence |
|---|--------|----------|
| Q1 Scope? | **YES** | api.gladia.io Highest |
| Q2 Reachable? | **YES** | OPTIONS preflight public |
| Q3 Real impact? | **LOW** | Framework fingerprinting aids CVE targeting only |
| Q4 Passive proof? | **YES** | Confirmed: present on OPTIONS, absent on GET |
| Q5 Novel? | **YES** | |
| Q6 Not rejected? | **NO** | **Fails** — "best practice" is on always-rejected list |
| Q7 Triager accept? | **NO** | Low-severity info disclosure / best practice violation |

**VERDICT: INVALID** — Fails Q3 (low real impact) and Q6 (best practice violation). Accepted as MISCONFIG by models but classified Low.

---

### 8. IDOR on transcription file download `/v2/transcription/{id}/file` — **api.gladia.io** (HIGHEST)

| Q | Answer | Evidence |
|---|--------|----------|
| Q1 Scope? | **YES** | api.gladia.io Highest |
| Q2 Reachable? | **AUTH_HELPED** | Requires valid `x-gladia-key` |
| Q3 Real impact? | **HIGH** | Cross-account transcription data (PII, audio) |
| Q4 Passive proof? | **NO** | Requires two accounts/keys to test cross-account access |
| Q5 Novel? | **UNKNOWN** | |
| Q6 Not rejected? | **YES** | |
| Q7 Triager accept? | **CONDITIONAL** | Only with valid keys |

**VERDICT: HOLD** — Requires AUTH_HELPED with two different accounts. Cannot be validated passively.

---

### 9. Query-param parsing injection on `/v1/history` — **api.gladia.io** (HIGHEST)

| Q | Answer | Evidence |
|---|--------|----------|
| Q1 Scope? | **YES** | api.gladia.io Highest |
| Q2 Reachable? | **AUTH_HELPED** | Key-gated (401) |
| Q3 Real impact? | **LOW-MED** | Filter bypass / prototype pollution on own-tenant query |
| Q4 Passive proof? | **NO** | Requires key to test injection payloads |
| Q5 Novel? | **UNKNOWN** | |
| Q6 Not rejected? | **YES** | |
| Q7 Triager accept? | **NO** | Low confidence (48%), key-gated, low impact |

**VERDICT: HOLD** — Low priority, key-gated, low impact.

---

### 10. `return-to` cookie JWT parsing without signature verification — **app.gladia.io** (HIGH)

| Q | Answer | Evidence |
|---|--------|----------|
| Q1 Scope? | **YES** | app.gladia.io High |
| Q2 Reachable? | **YES** | Cookie set on root |
| Q3 Real impact? | **NONE** | **Server rejects tampered cookie and resets to default** — proven NOT vulnerable |
| Q4 Passive proof? | **YES** | Verified: unsigned base64url JSON, server validates/resets |
| Q5 Novel? | **N/A** | Not a vulnerability |
| Q6 Not rejected? | **N/A** | |
| Q7 Triager accept? | **NO** | Not a vulnerability |

**VERDICT: INVALID** — Multiple models rejected: "return-to cookie tampering test — server rejects tampered value and resets to default".

---

### 11. OpenAPI shadow endpoints / undocumented v2 paths — **api.gladia.io** (HIGHEST)

| Q | Answer | Evidence |
|---|--------|----------|
| Q1 Scope? | **YES** | api.gladia.io Highest |
| Q2 Reachable? | **UNKNOWN** | |
| Q3 Real impact? | **UNKNOWN** | |
| Q4 Passive proof? | **NO** | Requires active fuzzing (prohibited by `passive_first: true`) |
| Q5 Novel? | **UNKNOWN** | |
| Q6 Not rejected? | **YES** | |
| Q7 Triager accept? | **NO** | Cannot be validated passively |

**VERDICT: INVALID** — Rejected: "detecting undocumented endpoints requires active fuzzing, prohibited under passive-first". NO_DRIFT confirmed 100+ cycles.

---

## Summary

| Lead | Asset | Verdict | Reason |
|------|-------|---------|--------|
| SSRF via audio_url/video_url/callback_url | api.gladia.io | **HOLD** | Spec confirms SSRF-by-design; needs valid key for POC |
| **npm gladia@0.1.3 impersonation + key-in-URL** | npm registry | **VALID** | **Reported 2026-08-12, report-ready, awaiting vendor** |
| Post-OAuth open redirect (redirect_to) | app.gladia.io | **HOLD** | Reflection confirmed; post-auth honoring needs HUMAN session |
| WebSocket token in URL query | api.gladia.io | **HOLD** | Spec confirms design flaw; needs key to verify Referrer-Policy |
| Undocumented /health endpoint | api.gladia.io | **INVALID** | Public health check, no sensitive data (rejected class) |
| CORS wildcard reflects Origin | api.gladia.io | **INVALID** | Static `*` confirmed, no reflection |
| x-powered-by Express on preflight | api.gladia.io | **INVALID** | Best practice violation, low impact |
| IDOR on /{id}/file download | api.gladia.io | **HOLD** | Needs two accounts/keys |
| Query-param injection /v1/history | api.gladia.io | **HOLD** | Low confidence, key-gated, low impact |
| return-to cookie JWT parsing | app.gladia.io | **INVALID** | Server validates/resets — not vulnerable |
| OpenAPI shadow endpoints | api.gladia.io | **INVALID** | Active fuzzing prohibited |

---

**Highest actionable item**: **npm `gladia@0.1.3` orphaned impersonation** — already reported, report-ready with locked evidence..submit via Gladia security channel (bug-bounty-report form or security@gladia.io).
