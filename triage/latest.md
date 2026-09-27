===== TRIAGE 2026-09-27 01:35:10 UTC =====
[0m
> build · muse-spark-1.2-contributor-free
[0m
Empty lead set received — hunting scope and inventory to apply the 7-question gate.
[0m→ [0mRead .
[0m→ [0mRead new-leads.txt
[0m→ [0mRead probe-results.txt
[0m→ [0mRead scope.yml
[0m→ [0mRead triage-prompt.txt
[0m→ [0mRead triage-output.txt
[0m→ [0mRead probe-results.md
[0m→ [0mRead leads
[0m→ [0mRead triage
[0m→ [0mRead inventory
[0m→ [0mRead README.md
[0m→ [0mRead leads/lead-mimo.md
[0m→ [0mRead leads/lead-laguna.md
[0m→ [0mRead leads/lead-bigpickle.md
[0m→ [0mRead leads/lead-longcat.md
[0m→ [0mRead leads/lead-nemotron3.md
[0m→ [0mRead leads/lead-ling3.md
[0m→ [0mRead leads/lead-human.md
[0m→ [0mRead leads/reposcan-latest.md
[0m→ [0mRead triage/latest.md
[0m→ [0mRead triage/gladia-0-1-3.md
[0m→ [0mRead inventory/live-highvalue.txt
[0m→ [0mRead inventory/gladia.md
Reconstructed your hunt surface from probe history — now scoring it through the strict 7-question gate.
[0m→ [0mRead reports
[0m→ [0mRead reports/valid-bugs.md
[0m
[0m$ [0mls -R 2>/dev/null | head -n 100
.:
README.md
inventory
knowledge
leads
new-leads.txt
probe-results.md
probe-results.txt
reports
reposcan-raw
scope.yml
scripts
state_mimo.json
triage
triage-output.txt
triage-prompt.txt

./inventory:
gladia.md
live-highvalue.txt
real-subdomains.txt

./knowledge:
facts.json
index.md
openapi-snapshot.json

./leads:
lead-bigpickle.md
lead-human.md
lead-laguna.md
lead-ling3.md
lead-longcat.md
lead-mimo.md
lead-nemotron3.md
reposcan-latest.md

./reports:
hypotheses-bigpickle.txt
hypotheses-mimo.txt
hypotheses-nemotron3.txt
hypotheses.archive-2026-09.md
hypotheses.md
valid-bugs.md

./reposcan-raw:
analysis.txt
gladiaio
grep-delta.txt
grep-hits.prev.txt
grep-hits.txt
npm
rag.txt

./reposcan-raw/gladiaio:
compare-stt
docs
gladia-cli
gladia-quiz-app
gladia-samples
gladiaflow
n8n-nodes-gladia
normalization
num2words2
realtime-multilingual-asr-router
sdk
skills
vercel-ai

./reposcan-raw/gladiaio/compare-stt:

./reposcan-raw/gladiaio/docs:

./reposcan-raw/gladiaio/gladia-cli:

./reposcan-raw/gladiaio/gladia-quiz-app:

./reposcan-raw/gladiaio/gladia-samples:

./reposcan-raw/gladiaio/gladiaflow:

./reposcan-raw/gladiaio/n8n-nodes-gladia:

./reposcan-raw/gladiaio/normalization:

./reposcan-raw/gladiaio/num2words2:

./reposcan-raw/gladiaio/realtime-multilingual-asr-router:

./reposcan-raw/gladiaio/sdk:

./reposcan-raw/gladiaio/skills:

./reposcan-raw/gladiaio/vercel-ai:

./reposcan-raw/npm:
_gladiaio_sdk.json
gladia.json

./scripts:
[0m
**Empty `LEADS` batch — breadth pass over full inventory `inventory/gladia.md` + `scope.yml` + `probe-results.md:1-1113`**

**In-scope assets per `scope.yml:5-13`:** `api.gladia.io:HIGHEST`, `app.gladia.io:HIGH`, `@gladiaio/sdk`+`gladiaio-sdk:MEDIUM`, `gladia.io:LOW`. Out: `*.gladia.io` other, third-party. Rules `scope.yml:35-42` `passive_first:true` `manual_validation_required:true` — scanner output alone REJECTED.

#### Top-3 Anomalies Depth (passive GET/HEAD only)

| # | Lead | Exact Probe `METHOD path?params` | Expected vs Actual `http_code` |
|---|---|---|---|
| 1 | `gladia@0.1.3:306-308` `src/client.ts:306` `wsUrl.searchParams.append('x-gladia-key',apiKey)` | `GET https://registry.npmjs.org/gladia` `200` + `GET https://api.github.com/repos/alexisbouchez/gladia.ts` `404` + `GET https://api.github.com/users/alexisbouchez` `404` | Expected `200`+ affiliated repo/maintainer if official. Actual `200` `description:"Official TypeScript SDK for Gladia"` vs tarball `README:"Unofficial"` + `maintainer:softwarecitadel@gmail.com` + `repo+user 404` orphaned/irrevocable `probe-results.md:3,11,58` frozen 100+ cycles |
| 2 | `app.gladia.io/signin?redirect_to=https://evil.example.com` | `GET /signin?redirect_to=https://evil.example.com` `200` `text/html` `probe-results.md:6,13` `form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"` | Expected `302` allowlist or stripped param. Actual `200` server-side reflection, `CSP 0 form-action` `inventory/gladia.md:152`, `return-to` unsigned `eyJ1cmwiOiIvIn0=` but server resets on tamper (REJECTED cookie vector), `GET /auth/google/callback` `302→accounts.google.com` `client_id=3520...21ha` `PKCE S256` `redirect_uri=https://app.gladia.io/auth/google/callback` FIXED `probe-results.md:199` |
| 3 | `api.gladia.io SSRF audio_url/video_url/CallbackConfigDto.url format:uri` no scheme allowlist `inventory/gladia.md:92` | `GET /v2/pre-recorded` `401 {"message":"no gladia key provided"}` `probe-results.md:4` + `GET /openapi.json` `200 125680B 14paths 7webhooks` + `OPTIONS /v2/transcription Origin:evil.test` `204 ACAO:*` | Expected if unauth SSRF: `200/400`. Actual `401` NestJS uniform gate, key-gated `POST` only `scope.yml:39 no_data_modification` blocks proof |

---

### 7-Question Gate Per Lead

**L1: `gladia@0.1.3` orphaned impersonation + `x-gladia-key` in `wss://` URL `triage/gladia-0-1-3.md:39-42`**
* Q1 In scope? **SPLIT:** `YES` per `scope.yml:28` `npm_packages:gladia` but `HOLD` for Gladia program — root cause code not served by `api/app.gladia.io` (`leads/lead-human.md:15` `Q3 FAIL`). `VALID` for `npm Trust & Safety` venue.
* Q2 Reachable? **YES** public unauth `GET registry.npmjs.org/gladia 200`
* Q3 Real impact? **YES** supply-chain impersonation `dist-tag latest=0.1.3` + credential hygiene hazard `wss://api.gladia.io/v2/live?x-gladia-key=...` leaks via proxy/logs/history vs official `@gladiaio/sdk` header-auth
* Q4 Passive GET/HEAD proof? **YES** `npm view`+`npm pack`+`grep -n x-gladia-key` `sha256 3b23ec7d...` `shasum cc96f84a...` 10+ repros
* Q5 Novel? **NO DUPLICATE** `REPORTED 2026-08-12 riteshekbote@gmail.com→security@gladia.io` `leads/lead-human.md:3` 9+ prior `VALID` `reports/valid-bugs.md:22`
* Q6 Not rejected? **YES** not `always-rejected` list
* Q7 Triager accept? **SPLIT: HOLD (Gladia, duplicate+Q3 conditional) / VALID (npm registry)**
* **Verdict: HOLD (VALID DUPLICATE)** — one-line: orphaned impersonation locked passive, Gladia-venue impact conditional until `WSS ?x-gladia-key` accepted server-side proven.

> **If npm venue:** minimal read-only proof `GET https://registry.npmjs.org/gladia | jq .dist-tags,.description,.maintainers` + `npm pack gladia@0.1.3; sha256sum` + `tar xzf && grep -n "x-gladia-key" package/src/client.ts:307` + `GET https://api.github.com/users/alexisbouchez 404`+`repos/alexisbouchez/gladia.ts 404`. Impact: supply-chain ATO via orphaned account claim + API-key harvesting via URL logging. **CVSS 3.1 7.5 AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:N** (`triage/gladia-0-1-3.md:16`). Channel: `npm Support` impersonation/abandoned-package + duplicate FYI to `security@gladia.io` / `https://gladia.io/bug-bounty-report 301→www→302→docs.google.com/forms/d/1RiodROQS…` `inventory/gladia.md:400` (TBD per `scope.yml:4`, auth-gated).

**L2: `app.gladia.io /signin redirect_to` post-auth open redirect `OATH`**
* Q1 YES `app.gladia.io` HIGH
* Q2 PARTIAL unauth `GET 200` reflects but post-auth `302 Location` honeypot unobserved — requires `HUMAN_ONLY` Google SSO session
* Q3 CONDITIONAL phishing only if honored post-auth; OAuth code theft **BLOCKED** `redirect_uri FIXED` PKCE `inventory/gladia.md:232`
* Q4 **NO** proving requires `GET /signin?redirect_to=https://evil.example.com` with valid session + `follow-redirects=false` capture `Location` — not GET/HEAD unauth
* Q5 YES not VALID before
* Q6 YES valid class
* Q7 **NO** reasonable triager REJECTS reflection alone without `Location: https://evil.example.com` proof
* **Verdict: HOLD (HUMAN_ONLY)** — one-line: reflection+CSP gap confirmed byte-fresh `probe-results.md:6`, post-auth honoring sole unverified gate, `return-to` tamper `REJECTED`.

**L3: `api.gladia.io SSRF` `audio_url/video_url/callback_config.url` `format:uri` `leads/lead-mimo.md:23`**
* Q1 YES `api.gladia.io` HIGHEST
* Q2 NO `GET/POST /v2/pre-recorded→401` key-gated, no bypass 100+ cycles `probe-results.md:4`
* Q3 YES would be High if proven (169.254.169.254)
* Q4 **NO** requires `POST /v2/pre-recorded -H x-gladia-key:<valid> -d {"audio_url":"http://canary"}` error/timing oracle violates `scope.yml:39 no_data_modification` `passive_first`
* Q5 YES design tracked but unproven
* Q6 YES valid class
* Q7 CONDITIONAL only with valid-key POC
* **Verdict: HOLD (AUTH_HELPED)** — one-line: design confirmed `spec format:uri no allowlist 14paths 7webhooks`, proof gated on valid `x-gladia-key`.

**L4-6: Always-Rejected**
* `x-powered-by: Express` on `OPTIONS` only `probe-results.md` differential — **INVALID** `Q6 FAIL` fingerprint info disclosure/BOLA best-practice `reports/valid-bugs.md:101` `Q7 NO triager accepts`
* `CORS ACAO:*` without `ACAC:true` — **INVALID** `Q3/Q6 FAIL` static wildcard, `x-gladia-key` cannot be credentialed cross-site `leads/lead-bigpickle.md:40`
* `/health {"health":"OK"}` 15B `GET /health 200` `inventory/gladia.md:37` undocumented but minimal — **INVALID** `Q3/Q6` public info disclosure `scope.yml:42`
* `/dashboard 200 SPA shell` unauth — **INVALID** client-side enforcement only, no data exposure
* `reposcan-latest.md:4` 652 hits no manual validation — **INVALID** `scope.yml:42 manual_validation_required`

#### Chain Analysis
`open redirect reflection (L2) → OAuth redirect_uri` **CHAIN BROKEN** — `redirect_uri` fixed `3520...21ha` PKCE S256, `state=oauth2:<uuid>` `inventory/gladia.md:232`. `SSRF (L3) → 169.254.169.254 → keys` **CHAIN BLOCKED** `401` gate, no unauth SSRF primitive.

#### [NEXT] PROBE (read-only GET/HEAD, 1rps)
```
GET https://registry.npmjs.org/gladia (verify dist-tags latest=0.1.3, shasum cc96f84a... fresh)
HEAD https://api.github.com/users/alexisbouchez (expect 404 orphaned)
GET https://app.gladia.io/signin?redirect_to=https://evil.example.com (capture form action + full CSP header grep form-action)
GET https://api.gladia.io/openapi.json (ETag/size structural, confirm 14 paths + CallbackConfigDto.url format:uri)
```
*HUMAN_ONLY unlocks:* `register app.gladia.io trial key → WSS wss://api.gladia.io/v2/live?x-gladia-key=<KEY> vs header-auth` if query-auth succeeds → re-file L1 as Gladia vuln; `Google SSO → GET /signin?redirect_to=https://evil.example.com` capture `302 Location` to prove L2.
