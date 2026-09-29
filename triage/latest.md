===== TRIAGE 2026-09-29 08:46:34 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/*"[90m 51 matches[0m
[0m→ [0mRead scope.yml
[0m→ [0mRead new-leads.txt
[0m→ [0mRead probe-results.txt
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead inventory/live-highvalue.txt
[0m→ [0mRead probe-results.md
Now I have all the data. Let me triage each unique lead against the 7-Question Gate.

---

## TRIAGE VERDICTS

### LEAD 1: npm `gladia@0.1.3` orphaned impersonation + API key in WebSocket URL
**Asset:** npm registry (`gladia@0.1.3`) — **MEDIUM priority** per scope.yml (Official SDKs)

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** — npm package `gladia` is the typosquat target of official `@gladiaio/sdk` (scope lists npm packages) |
| Q2 Attacker reachable? | **YES** — public npm registry, no auth needed to install |
| Q3 Real impact? | **YES** — supply-chain impersonation (description "Official" vs README "Unofficial"), dead repo (alexisbouchez 404), dist-tag `latest=0.1.3` persists, key leakage via `searchParams.append('x-gladia-key', apiKey)` in WS URL query |
| Q4 Provable passively? | **YES** — registry metadata, tarball source, GitHub 404 all verified via GET |
| Q5 Novel/unreported? | **YES** — human already reported 2026-08-12 to security@gladia.io + npm Trust & Safety; no vendor action yet |
| Q6 Not always-rejected? | **YES** — not info disclosure of public data; active impersonation + credential hygiene flaw |
| Q7 Triager accepts? | **YES** — clear supply-chain risk, irrevocable takeover vector |

**VERDICT: VALID**  
**Impact:** Supply-chain API key harvesting + account takeover (P3/P4)  
**CVSS 3.1:** 7.5 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N) — network, low complexity, no auth, user interaction (install), high confidentiality  
**Proof:** `npm view gladia@0.1.3` → description "Official", maintainer `softwarecitadel@gmail.com`, repo `alexisbouchez/gladia.ts` (404), tarball `src/client.ts:306-308` embeds key in WS URL  
**Channel:** Gladia bug-bounty-report (https://gladia.io/bug-bounty-report) + npm Trust & Safety (npmjs.com/support) — dual venue per lead-human.md

---

### LEAD 2: app.gladia.io `/signin?redirect_to=` reflection → post-auth open redirect
**Asset:** app.gladia.io — **HIGH** priority per scope.yml

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** — app.gladia.io explicitly in scope (High) |
| Q2 Attacker reachable? | **YES** — unauthenticated GET reflects `redirect_to` into form `action` (probe 200, byte-fresh) |
| Q3 Real impact? | **HOLD** — reflection confirmed, but **post-auth honoring UNVERIFIED** (requires Google SSO session); OAuth `redirect_uri` FIXED (PKCE S256) prevents code/state theft; return-to cookie tamper REJECTED; CSP lacks `form-action` directive (gap) |
| Q4 Provable passively? | **NO** — needs authenticated session to observe final 302 Location |
| Q5 Novel/unreported? | **YES** — not previously reported |
| Q6 Not always-rejected? | **YES** — not self-XSS; post-auth open redirect is real class |
| Q7 Triager accepts? | **HOLD** — unproven without auth; only reflection is proven |

**VERDICT: HOLD** — post-auth honoring unproven (AUTH_HELPED/HUMAN_ONLY). Reflection alone is not a vulnerability without evidence the server honors it after authentication.  
**Next:** `[NEXT] PROBE: HUMAN — complete Google OAuth with ?redirect_to=https://evil.example.com, capture final 302 Location`

---

### LEAD 3: api.gladia.io SSRF via `audio_url`/`video_url`/`callback_config.url` (no scheme allowlist)
**Asset:** api.gladia.io — **HIGHEST** priority per scope.yml

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** — api.gladia.io (Highest) |
| Q2 Attacker reachable? | **NO** — all endpoints key-gated (401 NestJS `x-gladia-key`); no valid key available for passive validation |
| Q3 Real impact? | **YES** — spec confirms `format:uri` with NO scheme allowlist, 7 webhook delivery paths, `/v1/models` exposes FR/US egress regions; SSRF-by-design |
| Q4 Provable passively? | **NO** — requires valid API key (AUTH_HELPED) to test internal fetch (169.254.169.254) |
| Q5 Novel/unreported? | **YES** — spec-confirmed design flaw, not previously reported |
| Q6 Not always-rejected? | **YES** — SSRF to cloud metadata is High severity |
| Q7 Triager accepts? | **HOLD** — key-gated, no bypass found across 100+ cycles; surface frozen |

**VERDICT: HOLD** — genuine SSRF-by-design surface confirmed in spec, but **key-gated with no auth bypass**. Cannot prove exploitability without valid key.  
**CVSS (if proven):** 7.1 (AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N) — key-gated (PR:L), scope change (internal network)  
**Next:** `[NEXT] PROBE: AUTH_HELPED — POST /v2/pre-recorded with x-gladia-key + audio_url=http://169.254.169.254/latest/meta-data/`

---

### LEAD 4: api.gladia.io `x-powered-by: Express` on CORS preflight only
**Asset:** api.gladia.io — **HIGHEST**

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **YES** — OPTIONS preflight returns header (probe confirmed) |
| Q3 Real impact? | **NO** — framework fingerprinting alone is Low severity (recon aid), not a vulnerability |
| Q4 Provable passively? | **YES** — `curl -X OPTIONS -H "Origin: https://evil.test" ...` |
| Q5 Novel/unreported? | **YES** |
| Q6 Not always-rejected? | **NO** — **ON ALWAYS-REJECTED LIST**: "best practice", "info disclosure of public data", "tech stack disclosure" |
| Q7 Triager accepts? | **NO** |

**VERDICT: INVALID** — always-rejected class (framework fingerprinting / recon aid only)

---

### LEAD 5: api.gladia.io IDOR on `/v2/transcription/{id}/file` (and /pre-recorded, /live)
**Asset:** api.gladia.io — **HIGHEST**

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **NO** — key-gated (401), needs valid key + cross-account resource ID |
| Q3 Real impact? | **YES** — if no object-level auth, cross-tenant transcription data (PII, audio) |
| Q4 Provable passively? | **NO** — requires AUTH_HELPED with two accounts |
| Q5 Novel/unreported? | **YES** |
| Q6 Not always-rejected? | **YES** |
| Q7 Triager accepts? | **HOLD** — unproven without key |

**VERDICT: HOLD** — plausible IDOR surface (spec shows no ownership binding), but key-gated and untestable without two valid accounts.  
**Next:** `[NEXT] PROBE: AUTH_HELPED — two valid keys, POST /v2/pre-recorded with key A, GET /v2/pre-recorded/{id_from_A}/file with key B`

---

### LEAD 6: api.gladia.io undocumented `/health` endpoint
**Asset:** api.gladia.io — **HIGHEST**

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **YES** — GET /health returns 200 `{"health":"OK"}` (probe confirmed) |
| Q3 Real impact? | **NO** — returns minimal static JSON; no version, build, metadata leakage (probed `?full=true`, `?format=json` — identical) |
| Q4 Provable passively? | **YES** |
| Q5 Novel/unreported? | **YES** |
| Q6 Not always-rejected? | **NO** — **ON ALWAYS-REJECTED LIST**: "info disclosure of public data" (health check is public by design) |
| Q7 Triager accepts? | **NO** |

**VERDICT: INVALID** — always-rejected (public health endpoint, no sensitive disclosure)

---

### LEAD 7: api.gladia.io CORS wildcard (`access-control-allow-origin: *`)
**Asset:** api.gladia.io — **HIGHEST**

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **YES** — static `*` on all responses (probe confirmed) |
| Q3 Real impact? | **NO** — no `access-control-allow-credentials`; cannot read authenticated responses cross-origin; only public endpoints (/v1/models, /openapi.json, /health) readable |
| Q4 Provable passively? | **YES** |
| Q5 Novel/unreported? | **YES** |
| Q6 Not always-rejected? | **NO** — **ON ALWAYS-REJECTED LIST**: "best practice" (wildcard without credentials is not exploitable) |
| Q7 Triager accepts? | **NO** |

**VERDICT: INVALID** — always-rejected (CORS wildcard without credentials = Low/Info, not a vuln)

---

### LEAD 8: api.gladia.io WebSocket auth token in URL query (`wss://api.gladia.io/v2/live?token=<uuid>`)
**Asset:** api.gladia.io — **HIGHEST**

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **NO** — token issued only after POST /v2/live with valid `x-gladia-key` (key-gated) |
| Q3 Real impact? | **YES** — token in URL leaks via Referer, browser history, proxy logs, server logs |
| Q4 Provable passively? | **NO** — needs valid key to init session and observe token format |
| Q5 Novel/unreported? | **YES** |
| Q6 Not always-rejected? | **YES** |
| Q7 Triager accepts? | **HOLD** — design flaw confirmed in spec, but key-gated |

**VERDICT: HOLD** — spec-confirmed token-in-URL design, but requires valid key to prove exploitability.  
**CVSS (if proven):** 5.3 (AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)  
**Next:** `[NEXT] PROBE: AUTH_HELPED — POST /v2/live with x-gladia-key, observe response.url token format`

---

### LEAD 9: api.gladia.io `/v1/history` query-param injection (`custom_metadata` object, `status`/`kind` arrays)
**Asset:** api.gladia.io — **HIGHEST**

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **NO** — key-gated (401) |
| Q3 Real impact? | **LOW** — prototype pollution / filter bypass on own-tenant query only (key-gated) |
| Q4 Provable passively? | **NO** |
| Q5 Novel/unreported? | **YES** |
| Q6 Not always-rejected? | **YES** |
| Q7 Triager accepts? | **HOLD** — low impact, key-gated, untestable |

**VERDICT: HOLD** — speculative injection surface, key-gated, low impact even if proven

---

### LEAD 10: app.gladia.io `return-to` cookie (unsigned base64url JSON)
**Asset:** app.gladia.io — **HIGH**

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **YES** — cookie set on root `/` |
| Q3 Real impact? | **NO** — probe confirmed server **rejects tampered value and resets** to default; no open redirect |
| Q4 Provable passively? | **YES** — `curl -b "return-to=eyJ1cmwiOiJodHRwczovL2V2aWwuY29tIn0=" https://app.gladia.io/` → reset |
| Q5 Novel/unreported? | **YES** |
| Q6 Not always-rejected? | **NO** — tested and **REJECTED** (server validates/resets) |
| Q7 Triager accepts? | **NO** |

**VERDICT: INVALID** — tested, server-side validation blocks exploit

---

### LEAD 11: app.gladia.io `/dashboard` SPA shell served without auth
**Asset:** app.gladia.io — **HIGH**

| Q | Answer |
|---|--------|
| Q1 In scope? | **YES** |
| Q2 Attacker reachable? | **YES** — GET /dashboard returns 200 HTML (probe confirmed) |
| Q3 Real impact? | **NO** — client-side auth enforcement; API calls fail 401 without key; shell is static |
| Q4 Provable passively? | **YES** |
| Q5 Novel/unreported? | **YES** |
| Q6 Not always-rejected? | **NO** — **ON ALWAYS-REJECTED LIST**: "best practice" (SPA shell without auth is normal; API enforces) |
| Q7 Triager accepts? | **NO** |

**VERDICT: INVALID** — always-rejected (client-side SPA pattern, API enforces auth)

---

## SUMMARY

| Lead | Verdict | Priority |
|------|---------|----------|
| npm `gladia@0.1.3` impersonation + key leak | **VALID** | **REPORT NOW** |
| app.gladia.io `/signin` redirect_to post-auth open redirect | **HOLD** | Needs auth session |
| api.gladia.io SSRF-by-design (audio_url/callback) | **HOLD** | Needs valid key |
| api.gladia.io x-powered-by Express (preflight) | **INVALID** | Always-rejected |
| api.gladia.io IDOR on /{id}/file | **HOLD** | Needs 2 keys |
| api.gladia.io /health undocumented | **INVALID** | Always-rejected |
| api.gladia.io CORS wildcard | **INVALID** | Always-rejected |
| api.gladia.io WS token in URL query | **HOLD** | Needs valid key |
| api.gladia.io /v1/history query injection | **HOLD** | Low impact, key-gated |
| app.gladia.io return-to cookie | **INVALID** | Tested, server rejects |
| app.gladia.io /dashboard SPA shell | **INVALID** | Always-rejected |

---

## IMMEDIATE ACTION

**Only one lead is VALID and report-ready right now:**

> **npm `gladia@0.1.3` orphaned impersonation + API key in WebSocket URL**  
> **Channel:** Gladia bug-bounty-report (https://gladia.io/bug-bounty-report) + npm Trust & Safety  
> **Evidence package:** sha256 `3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2`, shasum `cc96f84a200c0fd49a71e919391f9b659c39f3e9`, GitHub user+repo 404, package.json "Official" vs README "Unofficial", `src/client.ts:306-308` raw key in WS URL  
> **Human status:** Already reported 2026-08-12 to security@gladia.io — **follow up 2026-08-26** (14-day mark)

All HOLD leads require **AUTH_HELPED** or **HUMAN_ONLY** validation that cannot be done passively. No further passive probes will advance them.
