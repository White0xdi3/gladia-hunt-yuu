===== TRIAGE 2026-10-17 17:23:55 UTC =====
[0m
> build · nemotron-3-ultra-free
[0m
[0m✱ [0mGlob "**/*.md"[90m 22 matches[0m
[0m✱ [0mGlob "**/scope.yml"[90m 1 match[0m
[0m→ [0mRead scope.yml
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead leads/reposcan-latest.md
[0m→ [0mRead probe-results.md
[0m→ [0mRead triage/latest.md
Based on my analysis of all lead files and probe results, here are the 7-Question Gate evaluations for each unique finding:

---

### **F1: SSRF via audio_url/video_url/callback_url server-side fetch** (api.gladia.io)
- **Q1 Scope**: YES (api.gladia.io = Highest)
- **Q2 Reachable**: CONDITIONAL (key-gated; free trial keys obtainable)
- **Q3 Impact**: YES (cloud metadata 169.254.169.254, internal net, callback exfil → High)
- **Q4 Passive proof**: NO (requires valid x-gladia-key to test internal URLs → AUTH_HELPED)
- **Q5 Novel**: YES
- **Q6 Not rejected**: YES (SSRF-to-metadata is high-value class)
- **Q7 Triager accept**: CONDITIONAL (strong spec evidence: `format:uri` no allowlist, FR/US egress, NestJS backend)
- **VERDICT**: **HOLD** — High-confidence hypothesis, but cannot be proven without valid API key. Minimal proof step: `POST /v2/pre-recorded -H "x-gladia-key: <KEY>" -d '{"audio_url":"http://169.254.169.254/latest/meta-data/"}'` (AUTH_HELPED). Impact: High. CVSS 3.1: 8.2 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N). Channel: Gladia security (security@gladia.io or bug-bounty form).

---

### **F2: WebSocket auth token in URL query parameter** (api.gladia.io)
- **Q1 Scope**: YES (api.gladia.io = Highest)
- **Q2 Reachable**: YES (token in wss:// URL leaks via browser history, Referer, proxy logs)
- **Q3 Impact**: YES (bearer-equivalent token → unauthorized live transcription, audio access → High)
- **Q4 Passive proof**: YES (OpenAPI spec confirms `InitStreamingResponse.url = "wss://api.gladia.io/v2/live?token=<uuid>"`)
- **Q5 Novel**: YES
- **Q6 Not rejected**: YES (CWE-598: token in URL is recognized auth flaw)
- **Q7 Triager accept**: YES (design flaw confirmed by spec)
- **VERDICT**: **VALID** — Minimal proof: `GET https://api.gladia.io/openapi.json` → observe `InitStreamingResponse.url` schema. Impact: High (token theft → ATO on live sessions). CVSS 3.1: 7.5 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N). Channel: Gladia security channel.

---

### **F3: Undocumented /health endpoint** (api.gladia.io)
- **Q1 Scope**: YES
- **Q2 Reachable**: YES (public, 200 OK)
- **Q3 Impact**: NO (only `{"health":"OK"}`; probes confirm no verbose leak via `?full=true`, `?format=json`)
- **Q4 Passive proof**: YES
- **Q5 Novel**: YES
- **Q6 Not rejected**: NO (info disclosure of public health status only → always-rejected)
- **Q7 Triager accept**: NO
- **VERDICT**: **INVALID** — No sensitive data exposed; informational only.

---

### **F4: CORS wildcard with x-gladia-key header allowed** (api.gladia.io)
- **Q1 Scope**: YES
- **Q2 Reachable**: YES
- **Q3 Impact**: NO (static `*`, no `allow-credentials`; cross-origin reads only public endpoints /v1/models, /openapi.json, /health)
- **Q4 Passive proof**: YES
- **Q5 Novel**: YES
- **Q6 Not rejected**: NO (CORS misconfig without credentials = best practice/low)
- **Q7 Triager accept**: NO
- **VERDICT**: **INVALID** — No credential theft possible; public data only.

---

### **F5: x-powered-by: Express on CORS preflight only** (api.gladia.io)
- **Q1 Scope**: YES
- **Q2 Reachable**: YES (OPTIONS public)
- **Q3 Impact**: NO (framework fingerprinting → recon aid only)
- **Q4 Passive proof**: YES
- **Q5 Novel**: YES
- **Q6 Not rejected**: NO (info disclosure/recon → always-rejected class)
- **Q7 Triager accept**: NO
- **VERDICT**: **INVALID** — Reconnaissance aid, not a vulnerability.

---

### **F6: Post-OAuth open redirect via redirect_to** (app.gladia.io)
- **Q1 Scope**: YES (app.gladia.io = High)
- **Q2 Reachable**: PARTIAL (reflection in form action unauthenticated; exploit needs post-auth)
- **Q3 Impact**: MEDIUM (phishing redirect; OAuth redirect_uri fixed PKCE prevents code theft)
- **Q4 Passive proof**: NO (requires Google OAuth session → HUMAN_ONLY)
- **Q5 Novel**: YES
- **Q6 Not rejected**: YES (open redirect is valid class)
- **Q7 Triager accept**: CONDITIONAL (strong indicators: reflection + no CSP form-action + no host allowlist visible)
- **VERDICT**: **HOLD** — Cannot confirm post-auth honoring without valid session. Proof step: Complete Google OAuth with `?redirect_to=https://evil.example.com`, observe final 302 Location (HUMAN_ONLY). Impact: Medium. CVSS 3.1: 6.1 (AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N). Channel: Gladia security.

---

### **F7: return-to cookie unsigned base64url JSON** (app.gladia.io)
- **Q1 Scope**: YES
- **Q2 Reachable**: YES
- **Q3 Impact**: NO (probes confirm server rejects tampered cookie, resets to default)
- **Q4 Passive proof**: YES
- **Q5 Novel**: YES
- **Q6 Not rejected**: NO (no bypass achieved → not a vuln)
- **Q7 Triager accept**: NO
- **VERDICT**: **INVALID** — Server-side validation prevents exploit.

---

### **F8: npm package gladia@0.1.3 impersonates official SDK** (npm registry)
- **Q1 Scope**: CONDITIONAL (Official SDKs in scope; this is third-party typosquat on npm)
- **Q2 Reachable**: YES (public npm)
- **Q3 Impact**: MEDIUM-HIGH (supply chain: "Official" claim vs personal repo/maintainer; key in WS URL; orphaned repo = takeover risk)
- **Q4 Passive proof**: YES (npm metadata, tarball inspection, GitHub 404, README contradiction)
- **Q5 Novel**: NO (**ALREADY REPORTED** 2026-08-12 per lead-human.md → security@gladia.io + npm Trust & Safety)
- **Q6 Not rejected**: YES
- **Q7 Triager accept**: YES but duplicate
- **VERDICT**: **INVALID (DUPLICATE)** — Already reported; awaiting vendor response.

---

### **F9: IDOR on transcription file download endpoints** (api.gladia.io)
- **Q1 Scope**: YES
- **Q2 Reachable**: CONDITIONAL (key-gated; needs cross-account ID)
- **Q3 Impact**: HIGH (cross-tenant PII/audio access)
- **Q4 Passive proof**: NO (requires valid key + other user's ID → AUTH_HELPED)
- **Q5 Novel**: YES
- **Q6 Not rejected**: YES (IDOR/BOLA = high-value)
- **Q7 Triager accept**: CONDITIONAL (spec lacks ownership binding; unproven)
- **VERDICT**: **HOLD** — High impact if true, but unprovable without two valid accounts. Proof: `GET /v2/transcription/{other_id}/file` with own key (AUTH_HELPED). CVSS 3.1: 8.7 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N).

---

### **F10: Query-param parsing injection on /v1/history** (api.gladia.io)
- **Q1 Scope**: YES
- **Q2 Reachable**: CONDITIONAL (key-gated)
- **Q3 Impact**: LOW-MEDIUM (filter bypass/prototype pollution on own tenant)
- **Q4 Passive proof**: NO (requires key to inject payloads → AUTH_HELPED)
- **Q5 Novel**: YES
- **Q6 Not rejected**: YES
- **Q7 Triager accept**: CONDITIONAL
- **VERDICT**: **HOLD** — Spec shows complex parsing surface (`custom_metadata` object + arrays in query string), but key-gated and low blast radius. Proof: `GET /v1/history?custom_metadata[__proto__][x]=1` (AUTH_HELPED).

---

### **F11: Public OpenAPI spec at /openapi.json** (api.gladia.io)
- **Q1 Scope**: YES
- **Q2 Reachable**: YES
- **Q3 Impact**: NO (attack surface enumeration aid only)
- **Q4 Passive proof**: YES
- **Q5 Novel**: YES
- **Q6 Not rejected**: NO (public API docs = informational/best practice)
- **Q7 Triager accept**: NO
- **VERDICT**: **INVALID** — Not a vulnerability.

---

### Summary

| Finding | Verdict | Key Reason |
|---------|---------|------------|
| F1 SSRF audio_url/callback_url | **HOLD** | Requires valid API key (AUTH_HELPED) |
| F2 WebSocket token in URL | **VALID** | Spec-confirmed design flaw, passive proof exists |
| F3 Undocumented /health | **INVALID** | No sensitive disclosure |
| F4 CORS wildcard | **INVALID** | No credentials, public data only |
| F5 x-powered-by Express | **INVALID** | Recon aid only |
| F6 Post-OAuth redirect_to | **HOLD** | Needs authenticated session (HUMAN_ONLY) |
| F7 return-to cookie | **INVALID** | Server validates/resets |
| F8 npm gladia@0.1.3 impersonation | **INVALID (DUPLICATE)** | Already reported 2026-08-12 |
| F9 IDOR file download | **HOLD** | Needs two valid accounts (AUTH_HELPED) |
| F10 /v1/history query injection | **HOLD** | Key-gated, low blast radius |
| F11 Public OpenAPI spec | **INVALID** | Informational only |

**Top actionable**: **F2 (VALID)** — Ready to report with passive evidence. **F1, F6, F9** are high-value but blocked on AUTH_HELPED/HUMAN_ONLY verification.
