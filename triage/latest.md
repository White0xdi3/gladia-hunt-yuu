===== TRIAGE 2026-09-30 00:35:53 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/scope*"[90m 1 match[0m
[0m✱ [0mGlob "**/*.yml"[90m 1 match[0m
[0m✱ [0mGlob "**/leads*"[90m 0 matches[0m
[0m→ [0mRead scope.yml
[0m✱ [0mGlob "**/*"[90m 51 matches[0m
[0m→ [0mRead probe-results.md
[0m→ [0mRead new-leads.txt
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead reports/hypotheses.md
Based on the probe results and hypotheses, I'll triage the three main leads against the 7-Question Gate.

---

### LEAD 1: Orphaned npm `gladia@0.1.3` impersonates official SDK, leaks raw API key in WebSocket URL query

**Q1 Scope?** YES — npm `gladia` package listed in scope.yml (Medium priority, official SDKs)
**Q2 Attacker reachable?** YES — public npm registry, `npm install gladia` pulls 0.1.3 at dist-tag `latest`
**Q3 Real impact?** YES — supply-chain API key harvesting: SDK embeds raw `x-gladia-key` in `wss://` URL query (`searchParams.append('x-gladia-key', apiKey)`), logs/URLs leak keys; GitHub user+repo `alexisbouchez` 404 = orphaned/irrevocable; dist-tag `latest=0.1.3` persists
**Q4 Provable passively?** YES — 10+ independent `npm pack` reproductions confirm sha256 `3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2`, src/client.ts:306-308 key-in-URL, package.json "Official" vs README "# Unofficial" contradiction, GitHub API 404s
**Q5 Novel/unreported?** YES — no prior report found; orphaned impersonation + key-in-URL is unique
**Q6 Not rejected?** YES — not info disclosure of public data, not best practice, not self-XSS
**Q7 Triager accept?** YES — clear supply-chain vulnerability with irrevocable takeover risk

**VERDICT: VALID**  
**Minimal proof:** `npm pack gladia@0.1.3` → inspect `dist/client.js` line ~306 for `searchParams.append('x-gladia-key', apiKey)` in WebSocket URL; `npm view gladia@0.1.3 repository.url` → 404; `npm view gladia dist-tags.latest` → `0.1.3`  
**Impact:** Supply-chain API key harvesting + irrevocable account takeover (P3/P4)  
**CVSS 3.1:** 7.1 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N) — key exposure in transit/logs  
**Channel:** https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)

---

### LEAD 2: app.gladia.io `/signin?redirect_to=` form-action reflection, 0 CSP `form-action` directives

**Q1 Scope?** YES — app.gladia.io (High priority)
**Q2 Attacker reachable?** YES — public unauthenticated endpoint, reflects `redirect_to` in `<form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com">` (200 OK, byte-fresh 100+ cycles)
**Q3 Real impact?** POTENTIAL — post-auth open redirect if server honors `redirect_to` after Google SSO; OAuth `redirect_uri` FIXED (PKCE S256) prevents code/state theft at callback; return-to cookie tamper-reset REJECTED; only unverified gate is post-auth honoring
**Q4 Provable passively?** PARTIAL — reflection + CSP gap confirmed (0 `form-action` directives, grep-count=0); post-auth honoring REQUIRES HUMAN OAuth test (cannot be proven GET/HEAD only)
**Q5 Novel/unreported?** YES — CSP form-action gap + reflected form-action is specific
**Q6 Not rejected?** YES — not self-XSS, not info disclosure
**Q7 Triager accept?** HOLD — impact contingent on post-auth behavior (HUMAN_ONLY); cannot confirm exploitation without authenticated session

**VERDICT: HOLD** — post-auth redirect honoring unconfirmed; requires authorized test account to complete Google SSO and intercept post-auth 302 Location

**Minimal read-only proof (done):** `GET /signin?redirect_to=https://evil.example.com` → 200, form action reflects value, CSP header lacks `form-action`  
**Next step:** `[NEXT] PROBE: HUMAN with authorized test account: complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location`

---

### LEAD 3: api.gladia.io SSRF-by-design via `audio_url`/`video_url`/`callback_config.url` (no scheme allowlist)

**Q1 Scope?** YES — api.gladia.io (Highest priority)
**Q2 Attacker reachable?** NO — POST `/v2/pre-recorded` returns 401/144B (NestJS) without valid `x-gladia-key`; requires AUTH_HELPED
**Q3 Real impact?** YES — SSRF to internal network/cloud metadata (169.254.169.254) via 7 webhook delivery paths; spec confirms `format:uri` with NO scheme allowlist; FR/US egress confirmed
**Q4 Provable passively?** NO — requires valid API key for POC (AUTH_HELPED)
**Q5 Novel/unreported?** YES — SSRF-by-design in spec, not previously reported
**Q6 Not rejected?** YES — not scanner-only, not best practice
**Q7 Triager accept?** HOLD — key-gated (401), no bypass found across 100+ cycles; cannot validate without authorized key

**VERDICT: HOLD** — SSRF surface confirmed in spec but key-gated; no unauthenticated bypass; requires program-provided API key for POC

**Minimal read-only proof (done):** `GET /openapi.json` → confirms `audio_url`/`video_url`/`callback_config.url` as `format:uri` no scheme allowlist; `POST /v2/pre-recorded` → 401/144B NestJS  
**Next step:** `[NEXT] PROBE: AUTH_HELPED — POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret`

---

### Summary

| Lead | Verdict | Reason |
|------|---------|--------|
| npm `gladia@0.1.3` orphaned impersonation + key leak | **VALID** | Report-ready, 10+ reproductions, supply-chain P3/P4 |
| app.gladia.io `/signin` redirect_to reflection | **HOLD** | Post-auth honoring unconfirmed (HUMAN_ONLY) |
| api.gladia.io SSRF-by-design (audio_url) | **HOLD** | Key-gated 401, no bypass, AUTH_HELPED required |
