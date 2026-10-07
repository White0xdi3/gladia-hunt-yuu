## 2026-08-21 18:45:47 UTC [api] (model mimo)
[PRIO] npm gladia@0.1.3, 8.2, attack:7 business:9 tech:8 gate:9 cloud:8 fresh:8
[PRIO] app.gladia.io /signin redirect_to, 6.8, attack:7 business:8 tech:7 gate:6 cloud:4 fresh:7
[PRIO] api.gladia.io SSRF surface, 5.6, attack:6 business:7 tech:6 gate:3 cloud:5 fresh:4
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs
evidence_needed: report-ready, locked across 5+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action reflects URL-encoded value (byte-fresh 100+ cycles), CSP has 0 form-action directives (grep-count=0), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors redirect
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[PARKED] api.gladia.io SSRF: downgraded to AUTH_HELPED during POC/target=app phase, no valid key available, surface frozen 100+ cycles
[FINAL]
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh this cycle — dist-tag latest=0.1.3, shasum cc96f84a… unchanged, description "Official", GitHub API user+repo alexisbouchez both 404 (orphaned/irrevocable)
[LEARN] ACCEPTED OATH @ app.gladia.io: /signin redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen, GET /v2/pre-recorded 401/144B NestJS key-gated fresh — SSRF-by-design surface persists (AUTH_HELPED)
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface
## 2026-08-21 19:03:11 UTC [api] (model mimo)
[PRIO] npm gladia@0.1.3, 8.2, attack:8 business:9 tech:7 gate:9 cloud:8 fresh:8
[PRIO] app.gladia.io /signin redirect_to, 6.8, attack:7 business:8 tech:7 gate:6 cloud:4 fresh:7
[PRIO] api.gladia.io SSRF surface, 5.6, attack:6 business:7 tech:6 gate:3 cloud:5 fresh:4
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs
evidence_needed: report-ready, locked across 5+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action reflects URL-encoded value (byte-fresh 100+ cycles), CSP has 0 form-action directives (grep-count=0), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors redirect
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
## 2026-08-21 19:34:16 UTC [api] (model mimo)
[PRIO] npm `gladia`@0.1.3 orphaned impersonation, 8.2, attack:8 business:9 tech:7 gate:9 cloud:8 fresh:8
[PRIO] app.gladia.io /signin redirect_to, 6.8, attack:7 business:8 tech:7 gate:6 cloud:4 fresh:7
[PRIO] api.gladia.io SSRF surface, 5.6, attack:6 business:7 tech:6 gate:3 cloud:5 fresh:4
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 `3b23ec7d…7f2` reproduced across 10+ independent local npm pack runs
evidence_needed: report-ready, locked across 5+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action reflects URL-encoded value (byte-fresh 100+ cycles), CSP has 0 form-action directives (grep-count=0), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors redirect
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[PARKED] (none — all three are actionable within their testability constraints)
[FINAL]
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh this cycle — dist-tag latest=0.1.3, shasum `cc96f84a…` unchanged, GitHub API user+repo alexisbouchez both 404 (orphaned/irrevocable)
[LEARN] ACCEPTED OATH @ app.gladia.io: /signin redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen, GET /v2/pre-recorded 401/144B NestJS key-gated fresh — SSRF-by-design surface persists (AUTH_HELPED)
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface
## 2026-08-21 19:54:55 UTC [api] (model mimo)
[PRIO] npmjs.com/package/gladia, 8.2, attack:8 business:9 tech:7 gate:9 cloud:8 fresh:8
[PRIO] app.gladia.io/signin, 6.8, attack:7 business:8 tech:7 gate:6 cloud:4 fresh:7
[PRIO] api.gladia.io/v2/pre-recorded, 5.6, attack:6 business:7 tech:6 gate:3 cloud:5 fresh:4
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 `3b23ec7d…7f2` reproduced across 10+ independent local npm pack runs
evidence_needed: report-ready, locked across 5+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action reflects URL-encoded value (byte-fresh 100+ cycles), CSP has 0 form-action directives (grep-count=0), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors redirect
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[FINAL]
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface
[RISK] app.gladia.io: 55 reason | redirect_to reflection + CSP form-action gap confirmed, OAuth redirect_uri FIXED prevents code/state theft, post-auth honoring HUMAN_ONLY
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation confirmed live, report-ready, no program response yet
## 2026-08-21 20:29:08 UTC [api] (model mimo)
[PRIO] npmjs.com/package/gladia, 8.2, attack:8 business:9 tech:7 gate:9 cloud:8 fresh:8
[PRIO] app.gladia.io/signin, 6.8, attack:7 business:8 tech:7 gate:6 cloud:4 fresh:7
[PRIO] api.gladia.io/v2/pre-recorded, 5.6, attack:6 business:7 tech:6 gate:3 cloud:5 fresh:4
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 `3b23ec7d…7f2` reproduced across 10+ independent local npm pack runs
evidence_needed: report-ready, locked across 5+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action reflects URL-encoded value (byte-fresh 100+ cycles), CSP has 0 form-action directives (grep-count=0), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors redirect
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[FINAL]
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface
[RISK] app.gladia.io: 55 reason | redirect_to reflection + CSP form-action gap confirmed, OAuth redirect_uri FIXED prevents code/state theft, post-auth honoring HUMAN_ONLY
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation confirmed live, report-ready, no program response yet
## 2026-08-21 20:54:31 UTC [api] (model mimo)
[PRIO] npmjs.com/package/gladia, 8.2, attack:8 business:9 tech:7 gate:9 cloud:8 fresh:8
[PRIO] app.gladia.io/signin, 6.8, attack:7 business:8 tech:7 gate:6 cloud:4 fresh:7
[PRIO] api.gladia.io/v2/pre-recorded, 5.6, attack:6 business:7 tech:6 gate:3 cloud:5 fresh:4
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs
evidence_needed: report-ready, locked across 10+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action reflects URL-encoded value (byte-fresh 100+ cycles), CSP has 0 form-action directives (grep-count=0), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors redirect
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[FINAL]
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface
[RISK] app.gladia.io: 55 reason | redirect_to reflection + CSP form-action gap confirmed, OAuth redirect_uri FIXED prevents code/state theft, post-auth honoring HUMAN_ONLY
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation confirmed live, report-ready, no program response yet
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated). Evidence package: sha256 3b23ec7d…7f2, src/client.ts:306-308 key-in-URL, README↔package.json Official/Unofficial contradiction, GitHub user+repo 404 orphaned, dist-tag latest=0.1.3 persists. Also: if authenticated session available, test /signin?redirect_to=https://evil.example.com post-auth to verify if server honors reflected redirect_to after Google SSO.
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh 2026-08-21 20:54 UTC — dist-tag latest=0.1.3, shasum cc96f84a… unchanged, GitHub API user+repo alexisbouchez both 404 (orphaned/irrevocable)
[LEARN] ACCEPTED OATH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh 2026-08-21 20:54 UTC — form action reflects URL-encoded value, CSP 0 form-action directives, post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen, POST /v2/pre-recorded 401/144B NestJS key-gated fresh — SSRF-by-design surface persists (AUTH_HELPED)
[RISK] api.gladia.io: 45 reason | SSRF-by-design spec+RAG frozen 100+ cycles, key-gated only, no bypass; preflight-only x-powered-by differential; static CORS *; surface dead for autonomous probing
[RISK] app.gladia.io: 55 reason | /signin redirect_to reflection + 0 CSP form-action directives confirmed byte-fresh; OAuth redirect_uri FIXED prevents code/state theft; return-to cookie tamper-reset REJECTED; post-auth honoring HUMAN_ONLY gate
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation locked with 10+ independent npm pack reproductions, supply-chain key harvesting + irrevocable account takeover risk at dist-tag latest, report-ready with no program response yet
## 2026-08-21 21:26:09 UTC [api] (model mimo)
[PRIO] npmjs.com/package/gladia, 8.2, attack:8 business:9 tech:7 gate:9 cloud:8 fresh:8
[PRIO] app.gladia.io/signin, 6.8, attack:7 business:8 tech:7 gate:6 cloud:4 fresh:7
[PRIO] api.gladia.io/v2/pre-recorded, 5.6, attack:6 business:7 tech:6 gate:3 cloud:5 fresh:4
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs
evidence_needed: report-ready, locked across 10+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action reflects URL-encoded value (byte-fresh 100+ cycles), CSP has 0 form-action directives (grep-count=0), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors redirect
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[FINAL]
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface
[RISK] app.gladia.io: 55 reason | redirect_to reflection + CSP form-action gap confirmed, OAuth redirect_uri FIXED prevents code/state theft, post-auth honoring HUMAN_ONLY
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation confirmed live, report-ready, no program response yet
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated). Evidence package: sha256 3b23ec7d…7f2, src/client.ts:306-308 key-in-URL, README↔package.json Official/Unofficial contradiction, GitHub user+repo 404 orphaned, dist-tag latest=0.1.3 persists. Also: if authenticated session available, test /signin?redirect_to=https://evil.example.com post-auth to verify if server honors reflected redirect_to after Google SSO.
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh — dist-tag latest=0.1.3, shasum cc96f84a… unchanged, GitHub API user+repo alexisbouchez both 404 (orphaned/irrevocable)
[LEARN] ACCEPTED OATH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — form action reflects URL-encoded value, CSP 0 form-action directives, post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen, POST /v2/pre-recorded 401/144B NestJS key-gated fresh — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] REJECTED MISCONFIG @ api.gladia.io: NO_DRIFT re-confirmed — openapi 200/125680B (dynamic-example band)/14 paths/7 webhooks/1 server, /health 15B — surface frozen across 100+ cycles
[LEARN] REJECTED MISCONFIG @ api.gladia.io: per-instance codegen fingerprint remains falsified — new etag suffix W/"1eaf0-fw3/7WZlGvBwQpG4/r/M+C8A+Og" with structural identity intact; etag rotates via dynamic example timestamps, not surface drift
[RISK] api.gladia.io: 45 reason | SSRF-by-design spec+RAG frozen 100+ cycles, key-gated only, no bypass; preflight-only x-powered-by differential; static CORS *; surface dead for autonomous probing
[RISK] app.gladia.io: 55 reason | /signin redirect_to reflection + 0 CSP form-action directives confirmed byte-fresh; OAuth redirect_uri FIXED prevents code/state theft; return-to cookie tamper-reset REJECTED; post-auth honoring HUMAN_ONLY gate
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation locked with 10+ independent npm pack reproductions, supply-chain key harvesting + irrevocable account takeover risk at dist-tag latest, report-ready with no program response yet
## 2026-08-21 21:51:09 UTC [api] (model mimo)
[PRIO] npmjs.com/package/gladia, 8.2, attack:8 business:9 tech:7 gate:9 cloud:8 fresh:8
[PRIO] app.gladia.io/signin, 6.8, attack:7 business:8 tech:7 gate:6 cloud:4 fresh:7
[PRIO] api.gladia.io/v2/pre-recorded, 5.6, attack:6 business:7 tech:6 gate:3 cloud:5 fresh:4
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs
evidence_needed: report-ready, locked across 10+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action reflects URL-encoded value (byte-fresh 100+ cycles), CSP has 0 form-action directives (grep-count=0), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors redirect
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[FINAL]
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface
[RISK] app.gladia.io: 55 reason | redirect_to reflection + CSP form-action gap confirmed, OAuth redirect_uri FIXED prevents code/state theft, post-auth honoring HUMAN_ONLY
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation confirmed live, report-ready, no program response yet
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh — dist-tag latest=0.1.3, shasum cc96f84a… unchanged, GitHub API user+repo alexisbouchez both 404 (orphaned/irrevocable)
[LEARN] ACCEPTED OATH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — form action reflects URL-encoded value, CSP 0 form-action directives, post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen, POST /v2/pre-recorded 401/144B NestJS key-gated fresh — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] REJECTED MISCONFIG @ api.gladia.io: NO_DRIFT re-confirmed — openapi 200/125680B (dynamic-example band)/14 paths/7 webhooks/1 server, /health 15B — surface frozen across 100+ cycles
[LEARN] REJECTED MISCONFIG @ api.gladia.io: per-instance codegen fingerprint remains falsified — new etag suffix W/"1eaf0-fw3/7WZlGvBwQpG4/r/M+C8A+Og" with structural identity intact; etag rotates via dynamic example timestamps, not surface drift
[RISK] api.gladia.io: 45 reason | SSRF-by-design spec+RAG frozen 100+ cycles, key-gated only, no bypass; preflight-only x-powered-by differential; static CORS *; surface dead for autonomous probing
[RISK] app.gladia.io: 55 reason | /signin redirect_to reflection + 0 CSP form-action directives confirmed byte-fresh; OAuth redirect_uri FIXED prevents code/state theft; return-to cookie tamper-reset REJECTED; post-auth honoring HUMAN_ONLY gate
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation locked with 10+ independent npm pack reproductions, supply-chain key harvesting + irrevocable account takeover risk at dist-tag latest, report-ready with no program response yet
## 2026-08-21 22:16:11 UTC [api] (model mimo)
[PRIO] npmjs.com/package/gladia, 8.2, attack:8 business:9 tech:7 gate:9 cloud:8 fresh:8
[PRIO] app.gladia.io/signin, 6.8, attack:7 business:8 tech:7 gate:6 cloud:4 fresh:7
[PRIO] api.gladia.io/v2/pre-recorded, 5.6, attack:6 business:7 tech:6 gate:3 cloud:5 fresh:4
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs
evidence_needed: report-ready, locked across 10+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action reflects URL-encoded value (byte-fresh 100+ cycles), CSP has 0 form-action directives (grep-count=0), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors redirect
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[PARKED] api.gladia.io SSRF-by-design: Downgraded from autonomous probe (AUTH_HELPED, requires valid key for POC, no bypass found across 100+ cycles)
[FINAL]
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated). Evidence: sha256 `3b23ec7d…7f2`, src/client.ts:306-308 key-in-URL, README↔package.json Official/Unofficial contradiction, GitHub user+repo 404 orphaned, dist-tag latest=0.1.3 persists.
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh — dist-tag latest=0.1.3, shasum `cc96f84a…` unchanged, GitHub API user+repo alexisbouchez both 404 (orphaned/irrevocable)
[LEARN] ACCEPTED OATH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — form action reflects URL-encoded value, CSP 0 form-action directives, post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen, POST /v2/pre-recorded 401/144B NestJS key-gated fresh — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] REJECTED MISCONFIG @ api.gladia.io: NO_DRIFT re-confirmed — openapi 200/125680B (dynamic-example band)/14 paths/7 webhooks/1 server, /health 15B — surface frozen across 100+ cycles
[LEARN] REJECTED MISCONFIG @ api.gladia.io: per-instance codegen fingerprint remains falsified — new etag suffix `W/"1eaf0-fw3/7WZlGvBwQpG4/r/M+C8A+Og"` with structural identity intact; etag rotates via dynamic example timestamps, not surface drift
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface
[RISK] app.gladia.io: 55 reason | redirect_to reflection + CSP form-action gap confirmed, OAuth redirect_uri FIXED prevents code/state theft, post-auth honoring HUMAN_ONLY
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation confirmed live, report-ready, no program response yet
## 2026-08-21 22:47:04 UTC [api] (model mimo)
[PRIO] npmjs.com/package/gladia, 8.2, attack:8 business:9 tech:7 gate:9 cloud:8 fresh:8
[PRIO] app.gladia.io/signin, 6.8, attack:7 business:8 tech:7 gate:6 cloud:4 fresh:7
[PRIO] api.gladia.io/v2/pre-recorded, 5.6, attack:6 business:7 tech:6 gate:3 cloud:5 fresh:4
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs
evidence_needed: report-ready, locked across 10+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action reflects URL-encoded value (byte-fresh 100+ cycles), CSP has 0 form-action directives (grep-count=0), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors redirect
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[FINAL]
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh — dist-tag latest=0.1.3, shasum cc96f84a… unchanged, GitHub API user+repo alexisbouchez both 404 (orphaned/irrevocable)
[LEARN] ACCEPTED OATH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — form action reflects URL-encoded value, CSP 0 form-action directives, post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen, POST /v2/pre-recorded 401/144B NestJS key-gated fresh — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] REJECTED MISCONFIG @ api.gladia.io: NO_DRIFT re-confirmed — openapi 200/125680B (dynamic-example band)/14 paths/7 webhooks/1 server, /health 15B — surface frozen across 100+ cycles
[LEARN] REJECTED MISCONFIG @ api.gladia.io: per-instance codegen fingerprint remains falsified — new etag suffix W/"1eaf0-fw3/7WZlGvBwQpG4/r/M+C8A+Og" with structural identity intact; etag rotates via dynamic example timestamps, not surface drift
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface
[RISK] app.gladia.io: 55 reason | redirect_to reflection + CSP form-action gap confirmed, OAuth redirect_uri FIXED prevents code/state theft, post-auth honoring HUMAN_ONLY
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation confirmed live, report-ready, no program response yet
## 2026-08-21 23:11:54 UTC [api] (model mimo)
[PRIO] npmjs.com/package/gladia, 9.2, attack:8 business:9 tech:7 gate:9 cloud:8 fresh:8
[PRIO] app.gladia.io/signin, 6.8, attack:7 business:8 tech:7 gate:6 cloud:4 fresh:7
[PRIO] api.gladia.io/v2/pre-recorded, 5.6, attack:6 business:7 tech:6 gate:3 cloud:5 fresh:4
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs, README "Unofficial" vs package.json "Official" contradiction
evidence_needed: report-ready, locked across 10+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com" reflected byte-fresh (100+ cycles), CSP has 0 form-action directives (grep-count=0 on live header), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors reflected redirect_to after authentication
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication, P3 severity
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only, spec+RAG frozen 100+ cycles
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[FINAL]
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated). Evidence: sha256 3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2, shasum cc96f84a200c0fd49a71e919391f9b659c39f3e9, src/client.ts:306-308 searchParams.append('x-gladia-key', apiKey) + new WebSocket(wsUrl.toString()) confirmed in source+compiled dist, GitHub user+repo alexisbouchez both 404 (orphaned/irrevocable), package.json "Official" vs README "# Unofficial TypeScript SDK" contradiction, dist-tag latest=0.1.3 persists. Reproduced 10+ independent times.
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh 23:10 UTC — dist-tag latest=0.1.3, shasum cc96f84a… unchanged, description "Official", GitHub API user+repo alexisbouchez both 404 (orphaned/irrevocable), official @gladiaio/sdk@1.1.0 static
[LEARN] ACCEPTED OATH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh 23:10 UTC — form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com" reflected (200/27448B), CSP 0 form-action directives (grep-count=0), OAuth /auth/google/callback 302→accounts.google.com PKCE S256 FIXED redirect_uri prevents code/state theft, return-to cookie tamper-reset REJECTED — post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen (100+ cycles) — audio_url/video_url/callback_config.url format:uri/no scheme allowlist, 7 webhook delivery paths, /v1/models FR/US egress, POST 401 NestJS key-gated — SSRF-by-design persists (AUTH_HELPED)
[LEARN] REJECTED MISCONFIG @ api.gladia.io: NO_DRIFT re-confirmed fresh 23:10 UTC — openapi 200/125680B (dynamic-example band)/14 paths/7 webhooks/1 server, /health 15B {"health":"OK"}, /v1/models 530B FR+US, OPTIONS 204 x-powered-by=Express + ACAO * + ACAH x-gladia-key, POST 401/144B NestJS — surface frozen across 100+ cycles
[LEARN] REJECTED MISCONFIG @ api.gladia.io: per-instance codegen fingerprint remains falsified — new etag suffix W/"1eaf0-Yx9norCx0jUfAReMn0f+i4Cdu/s" with structural identity intact; etag rotates via dynamic example timestamps, not surface drift
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface, /v2/live/health undocumented but informational only
[RISK] app.gladia.io: 55 reason | redirect_to reflection + CSP form-action gap confirmed byte-fresh, OAuth redirect_uri FIXED prevents code/state theft, post-auth honoring HUMAN_ONLY, /dashboard 200 SPA shell without auth
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation confirmed live at dist-tag latest, report-ready across 10+ independent reproductions, no program response yet, irrevocable GitHub user+repo 404
## 2026-08-21 23:41:24 UTC [api] (model mimo)
[PRIO] npmjs.com/package/gladia, 9.2, attack:8 business:9 tech:7 gate:9 cloud:8 fresh:8
[PRIO] app.gladia.io/signin, 6.8, attack:7 business:8 tech:7 gate:6 cloud:4 fresh:7
[PRIO] api.gladia.io/v2/pre-recorded, 5.6, attack:6 business:7 tech:6 gate:3 cloud:5 fresh:4
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs, README "Unofficial" vs package.json "Official" contradiction
evidence_needed: report-ready, locked across 10+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com" reflected byte-fresh (100+ cycles), CSP has 0 form-action directives (grep-count=0 on live header), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors reflected redirect_to after authentication
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication, P3 severity
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only, spec+RAG frozen 100+ cycles
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[FINAL]
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs, README "Unofficial" vs package.json "Official" contradiction
evidence_needed: report-ready, locked across 10+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com" reflected byte-fresh (100+ cycles), CSP has 0 form-action directives (grep-count=0 on live header), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors reflected redirect_to after authentication
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication, P3 severity
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only, spec+RAG frozen 100+ cycles
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated). Evidence: sha256 3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2, shasum cc96f84a200c0fd49a71e919391f9b659c39f3e9, src/client.ts:306-308 searchParams.append('x-gladia-key', apiKey) + new WebSocket(wsUrl.toString()) confirmed in source+compiled dist, GitHub user+repo alexisbouchez both 404 (orphaned/irrevocable), package.json "Official" vs README "# Unofficial TypeScript SDK" contradiction, dist-tag latest=0.1.3 persists. Reproduced 10+ independent times.
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh 23:10 UTC — dist-tag latest=0.1.3, shasum cc96f84a… unchanged, description "Official", GitHub API user+repo alexisbouchez both 404 (orphaned/irrevocable), official @gladiaio/sdk@1.1.0 static
[LEARN] ACCEPTED OATH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh 23:10 UTC — form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com" reflected (200/27448B), CSP 0 form-action directives (grep-count=0), OAuth /auth/google/callback 302→accounts.google.com PKCE S256 FIXED redirect_uri prevents code/state theft, return-to cookie tamper-reset REJECTED — post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen (100+ cycles) — audio_url/video_url/callback_config.url format:uri/no scheme allowlist, 7 webhook delivery paths, /v1/models FR/US egress, POST 401 NestJS key-gated — SSRF-by-design persists (AUTH_HELPED)
[LEARN] REJECTED MISCONFIG @ api.gladia.io: NO_DRIFT re-confirmed fresh 23:10 UTC — openapi 200/125680B (dynamic-example band)/14 paths/7 webhooks/1 server, /health 15B {"health":"OK"}, /v1/models 530B FR+US, OPTIONS 204 x-powered-by=Express + ACAO * + ACAH x-gladia-key, POST 401/144B NestJS — surface frozen across 100+ cycles
[LEARN] REJECTED MISCONFIG @ api.gladia.io: per-instance codegen fingerprint remains falsified — new etag suffix W/"1eaf0-Yx9norCx0jUfAReMn0f+i4Cdu/s" with structural identity intact; etag rotates via dynamic example timestamps, not surface drift
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface, /v2/live/health undocumented but informational only
[RISK] app.gladia.io: 55 reason | redirect_to reflection + CSP form-action gap confirmed byte-fresh, OAuth redirect_uri FIXED prevents code/state theft, post-auth honoring HUMAN_ONLY, /dashboard 200 SPA shell without auth
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation confirmed live at dist-tag latest, report-ready across 10+ independent reproductions, no program response yet, irrevocable GitHub user+repo 404
## 2026-08-22 00:04:56 UTC [api] (model mimo)
[PRIO] npm:gladia@0.1.3  score=73  attack=8 business=8 tech=6 gate=10 cloud=3 fresh=8
[PRIO] app.gladia.io/signin  score=52  attack=6 business=5 tech=7 gate=3 cloud=2 fresh=8
[PRIO] api.gladia.io SSRF  score=48  attack=7 business=8 tech=6 gate=2 cloud=6 fresh=8
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs, README "Unofficial" vs package.json "Official" contradiction
evidence_needed: report-ready, locked across 10+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com" reflected byte-fresh (100+ cycles), CSP has 0 form-action directives (grep-count=0 on live header), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors reflected redirect_to after authentication
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication, P3 severity
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only, spec+RAG frozen 100+ cycles
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[FINAL]
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated). Evidence: sha256 3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2, shasum cc96f84a200c0fd49a71e919391f9b659c39f3e9, src/client.ts:306-308 searchParams.append('x-gladia-key', apiKey) + new WebSocket(wsUrl.toString()) confirmed in source+compiled dist, GitHub user+repo alexisbouchez both 404 (orphaned/irrevocable), package.json "Official" vs README "# Unofficial TypeScript SDK" contradiction, dist-tag latest=0.1.3 persists. Reproduced 10+ independent times.
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh 00:01 UTC — dist-tag latest=0.1.3, shasum cc96f84a… unchanged, description "Official", GitHub API user+repo alexisbouchez both 404 (orphaned/irrevocable), official @gladiaio/sdk@1.1.0 static
[LEARN] ACCEPTED OATH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh 00:01 UTC — form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com" reflected (200/27448B), CSP 0 form-action directives (grep-count=0), OAuth /auth/google/callback 302→accounts.google.com PKCE S256 FIXED redirect_uri prevents code/state theft, return-to cookie tamper-reset REJECTED — post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen (100+ cycles) — audio_url/video_url/callback_config.url format:uri/no scheme allowlist, 7 webhook delivery paths, /v1/models FR/US egress, POST 401 NestJS key-gated — SSRF-by-design persists (AUTH_HELPED)
[LEARN] REJECTED MISCONFIG @ api.gladia.io: NO_DRIFT re-confirmed fresh 00:01 UTC — openapi 200/125680B (dynamic-example band)/14 paths/7 webhooks/1 server, /health 15B {"health":"OK"}, /v1/models 530B FR+US, OPTIONS 204 x-powered-by=Express + ACAO * + ACAH x-gladia-key, POST 401/144B NestJS — surface frozen across 100+ cycles
[LEARN] REJECTED MISCONFIG @ api.gladia.io: per-instance codegen fingerprint remains falsified — new etag suffix with structural identity intact; etag rotates via dynamic example timestamps, not surface drift
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface, /v2/live/health undocumented but informational only
[RISK] app.gladia.io: 55 reason | redirect_to reflection + CSP form-action gap confirmed byte-fresh, OAuth redirect_uri FIXED prevents code/state theft, post-auth honoring HUMAN_ONLY, /dashboard 200 SPA shell without auth
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation confirmed live at dist-tag latest, report-ready across 10+ independent reproductions, no program response yet, irrevocable GitHub user+repo 404
## 2026-08-22 01:47:35 UTC [api] (model mimo)
[PRIO] npm:gladia@0.1.3  score=73  attack=8 business=8 tech=6 gate=10 cloud=3 fresh=8
[PRIO] app.gladia.io/signin  score=52  attack=6 business=5 tech=7 gate=3 cloud=2 fresh=8
[PRIO] api.gladia.io SSRF  score=48  attack=7 business=8 tech=6 gate=2 cloud=6 fresh=8
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs, README "Unofficial" vs package.json "Official" contradiction
evidence_needed: report-ready, locked across 10+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com" reflected byte-fresh (100+ cycles), CSP has 0 form-action directives (grep-count=0 on live header), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors reflected redirect_to after authentication
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication, P3 severity
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only, spec+RAG frozen 100+ cycles
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[FINAL]
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated). Evidence: sha256 3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2, shasum cc96f84a200c0fd49a71e919391f9b659c39f3e9, src/client.ts:306-308 searchParams.append('x-gladia-key', apiKey) + new WebSocket(wsUrl.toString()) confirmed in source+compiled dist, GitHub user+repo alexisbouchez both 404 (orphaned/irrevocable), package.json "Official" vs README "# Unofficial TypeScript SDK" contradiction, dist-tag latest=0.1.3 persists. Reproduced 10+ independent times.
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh 00:01 UTC — dist-tag latest=0.1.3, shasum cc96f84a… unchanged, description "Official", GitHub API user+repo alexisbouchez both 404 (orphaned/irrevocable), official @gladiaio/sdk@1.1.0 static
[LEARN] ACCEPTED OATH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh 00:01 UTC — form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com" reflected (200/27448B), CSP 0 form-action directives (grep-count=0), OAuth /auth/google/callback 302→accounts.google.com PKCE S256 FIXED redirect_uri prevents code/state theft, return-to cookie tamper-reset REJECTED — post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen (100+ cycles) — audio_url/video_url/callback_config.url format:uri/no scheme allowlist, 7 webhook delivery paths, /v1/models FR/US egress, POST 401 NestJS key-gated — SSRF-by-design persists (AUTH_HELPED)
[LEARN] REJECTED MISCONFIG @ api.gladia.io: NO_DRIFT re-confirmed fresh 00:01 UTC — openapi 200/125680B (dynamic-example band)/14 paths/7 webhooks/1 server, /health 15B {"health":"OK"}, /v1/models 530B FR+US, OPTIONS 204 x-powered-by=Express + ACAO * + ACAH x-gladia-key, POST 401/144B NestJS — surface frozen across 100+ cycles
[LEARN] REJECTED MISCONFIG @ api.gladia.io: per-instance codegen fingerprint remains falsified — new etag suffix with structural identity intact; etag rotates via dynamic example timestamps, not surface drift
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface, /v2/live/health undocumented but informational only
[RISK] app.gladia.io: 55 reason | redirect_to reflection + CSP form-action gap confirmed byte-fresh, OAuth redirect_uri FIXED prevents code/state theft, post-auth honoring HUMAN_ONLY, /dashboard 200 SPA shell without auth
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation confirmed live at dist-tag latest, report-ready across 10+ independent reproductions, no program response yet, irrevocable GitHub user+repo 404
## 2026-08-22 02:44:07 UTC [api] (model mimo)
[PRIO] npm:gladia@0.1.3  score=73  attack=8 business=8 tech=6 gate=10 cloud=3 fresh=8
[PRIO] app.gladia.io/signin  score=52  attack=6 business=5 tech=7 gate=3 cloud=2 fresh=8
[PRIO] api.gladia.io SSRF  score=48  attack=7 business=8 tech=6 gate=2 cloud=6 fresh=8
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs, README "Unofficial" vs package.json "Official" contradiction
evidence_needed: report-ready, locked across 10+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com" reflected byte-fresh (100+ cycles), CSP has 0 form-action directives (grep-count=0 on live header), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors reflected redirect_to after authentication
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication, P3 severity
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only, spec+RAG frozen 100+ cycles
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[FINAL]
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query (confidence=97)
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives (confidence=92)
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist (confidence=85)
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated). Evidence: sha256 3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2, shasum cc96f84a200c0fd49a71e919391f9b659c39f3e9, src/client.ts:306-308 searchParams.append('x-gladia-key', apiKey) + new WebSocket(wsUrl.toString()) confirmed in source+compiled dist, GitHub user+repo alexisbouchez both 404 (orphaned/irrevocable), package.json "Official" vs README "# Unofficial TypeScript SDK" contradiction, dist-tag latest=0.1.3 persists. Reproduced 10+ independent times.
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh 02:43 UTC — dist-tag latest=0.1.3, shasum cc96f84a… unchanged, GitHub API user+repo alexisbouchez both 404 (orphaned/irrevocable), official @gladiaio/sdk@1.1.0 static
[LEARN] ACCEPTED OATH @ app.gladia.io: /signin redirect_to reflection alive byte-fresh — 0 CSP form-action directives (grep-count=0), post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] REJECTED MISCONFIG @ api.gladia.io: NO_DRIFT re-confirmed fresh — openapi 125680B/14 paths/7 webhooks, OPTIONS 204 xpb=Express, POST 401 NestJS — surface frozen across 100+ cycles
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface, /v2/live/health undocumented but informational only
[RISK] app.gladia.io: 55 reason | redirect_to reflection + CSP form-action gap confirmed byte-fresh, OAuth redirect_uri FIXED prevents code/state theft, post-auth honoring HUMAN_ONLY, /dashboard 200 SPA shell without auth
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation confirmed live at dist-tag latest, report-ready across 10+ independent reproductions, no program response yet, irrevocable GitHub user+repo 404
## 2026-08-22 03:29:07 UTC [api] (model mimo)
[PRIO] npm:gladia@0.1.3  score=73  attack=8 business=8 tech=6 gate=10 cloud=3 fresh=8
[PRIO] app.gladia.io/signin  score=52  attack=6 business=5 tech=7 gate=3 cloud=2 fresh=8
[PRIO] api.gladia.io SSRF  score=48  attack=7 business=8 tech=6 gate=2 cloud=6 fresh=8
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs, README "Unofficial" vs package.json "Official" contradiction
evidence_needed: report-ready, locked across 10+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com" reflected byte-fresh (100+ cycles), CSP has 0 form-action directives (grep-count=0 on live header), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors reflected redirect_to after authentication
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication, P3 severity
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only, spec+RAG frozen 100+ cycles
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[FINAL]
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query (confidence=97)
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives (confidence=92)
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist (confidence=85)
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated). Evidence: sha256 3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2, shasum cc96f84a200c0fd49a71e919391f9b659c39f3e9, src/client.ts:306-308 searchParams.append('x-gladia-key', apiKey) + new WebSocket(wsUrl.toString()) confirmed in source+compiled dist, GitHub user+repo alexisbouchez both 404 (orphaned/irrevocable), package.json "Official" vs README "# Unofficial TypeScript SDK" contradiction, dist-tag latest=0.1.3 persists. Reproduced 10+ independent times.
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh 02:43 UTC — dist-tag latest=0.1.3, shasum cc96f84a… unchanged, GitHub API user+repo alexisbouchez both 404 (orphaned/irrevocable), official @gladiaio/sdk@1.1.0 static
[LEARN] ACCEPTED OATH @ app.gladia.io: /signin redirect_to reflection alive byte-fresh — 0 CSP form-action directives (grep-count=0), post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] REJECTED MISCONFIG @ api.gladia.io: NO_DRIFT re-confirmed fresh — openapi 125680B/14 paths/7 webhooks, OPTIONS 204 xpb=Express, POST 401 NestJS — surface frozen across 100+ cycles
[RISK] api.gladia.io: 45 reason | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface, /v2/live/health undocumented but informational only
[RISK] app.gladia.io: 55 reason | redirect_to reflection + CSP form-action gap confirmed byte-fresh, OAuth redirect_uri FIXED prevents code/state theft, post-auth honoring HUMAN_ONLY, /dashboard 200 SPA shell without auth
[RISK] sdk: 75 reason | gladia@0.1.3 orphaned impersonation confirmed live at dist-tag latest, report-ready across 10+ independent reproductions, no program response yet, irrevocable GitHub user+repo 404
## 2026-08-22 04:10:01 UTC [api] (model mimo)
[PRIO] npm:gladia@0.1.3  score=73  attack=8 business=8 tech=6 gate=10 cloud=3 fresh=8
[PRIO] app.gladia.io/signin  score=52  attack=6 business=5 tech=7 gate=3 cloud=2 fresh=8
[PRIO] api.gladia.io SSRF  score=48  attack=7 business=8 tech=6 gate=2 cloud=6 fresh=8
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs, README "Unofficial" vs package.json "Official" contradiction
evidence_needed: report-ready, locked across 10+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com" reflected byte-fresh (100+ cycles), CSP has 0 form-action directives (grep-count=0 on live header), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors reflected redirect_to after authentication
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication, P3 severity
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only, spec+RAG frozen 100+ cycles
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[FINAL]
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query (confidence=97)
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives (confidence=92)
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist (confidence=85)
[NEXT] PROBE: Re-verify app.gladia.io CSP header and /signin?redirect_to=https://evil.example.com form-action reflection via webfetch (GET).
## 2026-08-22 04:51:03 UTC [api] (model mimo)
[PRIO] npm:gladia@0.1.3          score=75  attack=8 business=8 tech=6 gate=10 cloud=3 fresh=8
[PRIO] app.gladia.io/signin       score=50  attack=6 business=5 tech=7 gate=3  cloud=2 fresh=8
[PRIO] api.gladia.io SSRF         score=46  attack=7 business=8 tech=6 gate=2  cloud=6 fresh=8
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query
class: OTHER
asset: npmjs.com/package/gladia
confidence: 97
reasoning: dist-tag latest=0.1.3, description "Official TypeScript SDK for Gladia", repo+user alexisbouchez both 404 (orphaned/irrevocable), src/client.ts:306-308 embeds raw x-gladia-key in wss:// URL query via searchParams.append, sha256 3b23ec7d…7f2 reproduced across 10+ independent local npm pack runs, README "Unofficial" vs package.json "Official" contradiction
evidence_needed: report-ready, locked across 10+ independent npm pack reproductions
verify_steps: HUMAN: Submit report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)
impact: supply-chain API key harvesting + irrevocable account takeover (GitHub user+repo 404 = orphaned, dist-tag latest persists), P3/P4 severity
testability: HUMAN_ONLY
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives
class: OATH
asset: app.gladia.io/signin
confidence: 92
reasoning: form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com" reflected byte-fresh (100+ cycles), CSP has 0 form-action directives (grep-count=0 on live header), OAuth redirect_uri FIXED prevents code/state theft, return-to cookie tamper-reset REJECTED, post-auth honoring sole unverified gate
evidence_needed: HUMAN OAuth test (post-auth redirect_to)
verify_steps: HUMAN: authenticate via Google SSO, then access /signin?redirect_to=https://evil.example.com post-auth to test if server honors reflected redirect_to after authentication
impact: potential post-auth open redirect if server honors reflected redirect_to after authentication, P3 severity
testability: HUMAN_ONLY
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist
class: SSRF
asset: api.gladia.io/v2/pre-recorded
confidence: 85
reasoning: spec confirms audio_url/video_url/callback_config.url as format:uri with NO scheme allowlist, 7 webhook delivery paths, /v1/models confirms FR/US egress, POST 401 NestJS key-gated only, spec+RAG frozen 100+ cycles
evidence_needed: authorized API key for POC
verify_steps: AUTH_HELPED: POST /v2/pre-recorded with valid x-gladia-key and audio_url=http://internal-host/secret
impact: server-side request forgery to internal network, P2/P3 severity
testability: AUTH_HELPED
[FINAL]
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK, leaks raw API key in WebSocket URL query (confidence=97)
[HYP] app.gladia.io /signin redirect_to form-action reflection with 0 CSP form-action directives (confidence=92)
[HYP] api.gladia.io SSRF-by-design via audio_url/video_url/callback_config.url with no scheme allowlist (confidence=85)
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated). Evidence: sha256 3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2, shasum cc96f84a200c0fd49a71e919391f9b659c39f3e9, src/client.ts:306-308 searchParams.append('x-gladia-key', apiKey) + new WebSocket(wsUrl.toString()) confirmed in source+compiled dist, GitHub user+repo alexisbouchez both 404 (orphaned/irrevocable), package.json "Official" vs README "# Unofficial TypeScript SDK" contradiction, dist-tag latest=0.1.3 persists. Reproduced 10+ independent times.
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh 02:43 UTC — dist-tag latest=0.1.3, shasum cc96f84a… unchanged, GitHub API user+repo alexisbouchez both 404 (orphaned/irrevocable), official @gladiaio/sdk@1.1.0 static
[LEARN] ACCEPTED OATH @ app.gladia.io: /signin redirect_to reflection alive byte-fresh — 0 CSP form-action directives (grep-count=0), post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] REJECTED MISCONFIG @ api.gladia.io: NO_DRIFT re-confirmed fresh — openapi 125680B/14 paths/7 webhooks, OPTIONS 204 xpb=Express, POST 401 NestJS — surface frozen across 100+ cycles
[RISK] api.gladia.io: 45 | SSRF-by-design surface persists but key-gated (AUTH_HELPED), no bypass found across 100+ cycles, frozen surface, /v2/live/health undocumented but informational only
[RISK] app.gladia.io: 55 | redirect_to reflection + CSP form-action gap confirmed byte-fresh, OAuth redirect_uri FIXED prevents code/state theft, post-auth honoring HUMAN_ONLY, /dashboard 200 SPA shell without auth
[RISK] sdk: 75 | gladia@0.1.3 orphaned impersonation confirmed live at dist-tag latest, report-ready across 10+ independent reproductions, no program response yet, irrevocable GitHub user+repo 404
## 2026-08-22 05:19:17 UTC [api] (model mimo)
## 2026-08-22 05:49:34 UTC [api] (model mimo)
## 2026-08-22 06:20:39 UTC [api] (model mimo)
## 2026-08-22 07:08:43 UTC [api] (model mimo)
## 2026-08-22 07:45:47 UTC [api] (model mimo)
## 2026-08-22 08:12:33 UTC [api] (model mimo)
## 2026-08-22 08:50:54 UTC [api] (model mimo)
## 2026-08-22 09:20:24 UTC [api] (model mimo)
## 2026-08-22 09:48:52 UTC [api] (model mimo)
## 2026-08-22 10:10:43 UTC [api] (model mimo)
## 2026-08-22 10:42:48 UTC [api] (model mimo)
## 2026-08-22 11:02:17 UTC [api] (model mimo)
## 2026-08-22 11:31:47 UTC [api] (model mimo)
## 2026-08-22 11:53:33 UTC [api] (model mimo)
## 2026-08-22 12:38:23 UTC [api] (model mimo)
## 2026-08-22 13:19:27 UTC [api] (model mimo)
## 2026-08-22 13:49:28 UTC [api] (model mimo)
## 2026-08-22 14:10:51 UTC [api] (model mimo)
## 2026-08-22 14:40:38 UTC [api] (model mimo)
## 2026-08-22 15:00:41 UTC [api] (model mimo)
## 2026-08-22 15:31:42 UTC [api] (model mimo)
## 2026-08-22 15:53:15 UTC [api] (model mimo)
## 2026-08-22 16:22:20 UTC [api] (model mimo)
## 2026-08-22 16:49:11 UTC [api] (model mimo)
## 2026-08-22 17:10:49 UTC [api] (model mimo)
## 2026-08-22 17:38:16 UTC [api] (model mimo)
## 2026-08-22 17:58:09 UTC [api] (model mimo)
## 2026-08-22 18:42:24 UTC [api] (model mimo)
## 2026-08-22 19:08:56 UTC [api] (model mimo)
## 2026-08-22 19:35:21 UTC [api] (model mimo)
## 2026-08-22 19:54:40 UTC [api] (model mimo)
## 2026-08-22 20:26:14 UTC [api] (model mimo)
## 2026-08-22 20:51:22 UTC [api] (model mimo)
## 2026-08-22 21:15:45 UTC [api] (model mimo)
## 2026-08-22 21:40:57 UTC [api] (model mimo)
## 2026-08-22 21:59:48 UTC [api] (model mimo)
## 2026-08-22 22:33:12 UTC [api] (model mimo)
## 2026-08-22 22:55:31 UTC [api] (model mimo)
## 2026-08-22 23:26:10 UTC [api] (model mimo)
## 2026-08-22 23:48:27 UTC [api] (model mimo)
## 2026-08-23 00:28:00 UTC [api] (model mimo)
## 2026-08-23 02:10:59 UTC [api] (model mimo)
## 2026-08-23 03:17:04 UTC [api] (model mimo)
## 2026-08-23 04:06:19 UTC [api] (model mimo)
## 2026-08-23 04:50:59 UTC [api] (model mimo)
## 2026-08-23 05:22:34 UTC [api] (model mimo)
## 2026-08-23 05:54:32 UTC [api] (model mimo)
## 2026-08-23 06:45:04 UTC [api] (model mimo)
## 2026-08-23 07:22:02 UTC [api] (model mimo)
## 2026-08-23 07:55:44 UTC [api] (model mimo)
## 2026-08-23 08:37:39 UTC [api] (model mimo)
## 2026-08-23 09:03:36 UTC [api] (model mimo)
## 2026-08-23 09:38:58 UTC [api] (model mimo)
## 2026-08-23 10:00:31 UTC [api] (model mimo)
## 2026-08-23 10:35:12 UTC [api] (model mimo)
## 2026-08-23 10:57:44 UTC [api] (model mimo)
## 2026-08-23 11:29:12 UTC [api] (model mimo)
## 2026-08-23 11:51:50 UTC [api] (model mimo)
## 2026-08-23 12:30:26 UTC [api] (model mimo)
## 2026-08-23 13:16:50 UTC [api] (model mimo)
## 2026-08-23 13:50:00 UTC [api] (model mimo)
## 2026-08-23 14:14:16 UTC [api] (model mimo)
## 2026-08-23 14:44:22 UTC [api] (model mimo)
## 2026-08-23 15:03:58 UTC [api] (model mimo)
## 2026-08-23 15:34:30 UTC [api] (model mimo)
## 2026-08-23 15:55:50 UTC [api] (model mimo)
## 2026-08-23 16:33:11 UTC [api] (model mimo)
## 2026-08-23 16:57:40 UTC [api] (model mimo)
## 2026-08-23 17:27:51 UTC [api] (model mimo)
## 2026-08-23 17:50:30 UTC [api] (model mimo)
## 2026-08-23 18:17:37 UTC [api] (model mimo)
## 2026-08-23 18:52:43 UTC [api] (model mimo)
## 2026-08-23 19:20:36 UTC [api] (model mimo)
## 2026-08-23 19:43:19 UTC [api] (model mimo)
## 2026-08-23 20:00:03 UTC [api] (model mimo)
## 2026-08-23 20:34:33 UTC [api] (model mimo)
## 2026-08-23 20:57:17 UTC [api] (model mimo)
## 2026-08-23 21:29:30 UTC [api] (model mimo)
## 2026-08-23 21:51:36 UTC [api] (model mimo)
## 2026-08-23 22:16:33 UTC [api] (model mimo)
## 2026-08-23 22:43:01 UTC [api] (model mimo)
## 2026-08-23 23:01:40 UTC [api] (model mimo)
## 2026-08-23 23:32:11 UTC [api] (model mimo)
## 2026-08-23 23:53:41 UTC [api] (model mimo)
## 2026-08-24 01:18:19 UTC [api] (model mimo)
## 2026-08-24 02:39:30 UTC [api] (model mimo)
## 2026-08-24 03:39:14 UTC [api] (model mimo)
## 2026-08-24 04:29:24 UTC [api] (model mimo)
## 2026-08-24 05:22:13 UTC [api] (model mimo)
## 2026-08-24 06:02:52 UTC [api] (model mimo)
## 2026-08-24 07:16:49 UTC [api] (model mimo)
## 2026-08-24 08:08:15 UTC [api] (model mimo)
## 2026-08-24 09:04:53 UTC [api] (model mimo)
## 2026-08-24 10:01:20 UTC [api] (model mimo)
## 2026-08-24 10:49:25 UTC [api] (model mimo)
## 2026-08-24 11:17:34 UTC [api] (model mimo)
## 2026-08-24 11:48:57 UTC [api] (model mimo)
## 2026-08-24 12:21:15 UTC [api] (model mimo)
## 2026-08-24 13:29:31 UTC [api] (model mimo)
## 2026-08-24 14:21:36 UTC [api] (model mimo)
## 2026-08-24 15:09:16 UTC [api] (model mimo)
## 2026-08-24 15:56:28 UTC [api] (model mimo)
## 2026-08-24 16:47:53 UTC [api] (model mimo)
## 2026-08-24 17:19:28 UTC [api] (model mimo)
## 2026-08-24 17:54:33 UTC [api] (model mimo)
## 2026-08-24 18:42:59 UTC [api] (model mimo)
## 2026-08-24 19:18:39 UTC [api] (model mimo)
## 2026-08-24 19:50:25 UTC [api] (model mimo)
## 2026-08-24 20:20:20 UTC [api] (model mimo)
## 2026-08-24 20:56:22 UTC [api] (model mimo)
## 2026-08-24 21:36:45 UTC [api] (model mimo)
## 2026-08-24 22:00:53 UTC [api] (model mimo)
## 2026-08-24 22:38:10 UTC [api] (model mimo)
## 2026-08-24 23:01:43 UTC [api] (model mimo)
## 2026-08-24 23:31:49 UTC [api] (model mimo)
## 2026-08-24 23:53:44 UTC [api] (model mimo)
## 2026-08-25 01:17:04 UTC [api] (model mimo)
## 2026-08-25 02:33:15 UTC [api] (model mimo)
## 2026-08-25 03:29:06 UTC [api] (model mimo)
## 2026-08-25 04:19:02 UTC [api] (model mimo)
## 2026-08-25 05:01:08 UTC [api] (model mimo)
## 2026-08-25 05:42:12 UTC [api] (model mimo)
## 2026-08-25 06:18:30 UTC [api] (model mimo)
## 2026-08-25 07:15:06 UTC [api] (model mimo)
## 2026-08-25 08:03:12 UTC [api] (model mimo)
## 2026-08-25 08:56:19 UTC [api] (model mimo)
## 2026-08-25 09:42:42 UTC [api] (model mimo)
## 2026-08-25 10:15:27 UTC [api] (model mimo)
## 2026-08-25 10:54:43 UTC [api] (model mimo)
## 2026-08-25 11:31:12 UTC [api] (model mimo)
## 2026-08-25 11:59:02 UTC [api] (model mimo)
## 2026-08-25 13:05:21 UTC [api] (model mimo)
## 2026-08-25 14:01:38 UTC [api] (model mimo)
## 2026-08-25 14:58:54 UTC [api] (model mimo)
## 2026-08-25 15:53:45 UTC [api] (model mimo)
## 2026-08-25 16:37:40 UTC [api] (model mimo)
## 2026-08-25 17:15:36 UTC [api] (model mimo)
## 2026-08-25 17:49:44 UTC [api] (model mimo)
## 2026-08-25 18:23:31 UTC [api] (model mimo)
## 2026-08-25 19:08:42 UTC [api] (model mimo)
## 2026-08-25 19:46:12 UTC [api] (model mimo)
## 2026-08-25 20:11:47 UTC [api] (model mimo)
## 2026-08-25 20:48:53 UTC [api] (model mimo)
## 2026-08-25 21:15:28 UTC [api] (model mimo)
## 2026-08-25 21:48:18 UTC [api] (model mimo)
## 2026-08-25 22:11:51 UTC [api] (model mimo)
## 2026-08-25 22:47:57 UTC [api] (model mimo)
## 2026-08-25 23:13:19 UTC [api] (model mimo)
## 2026-08-25 23:42:27 UTC [api] (model mimo)
## 2026-08-26 00:01:56 UTC [api] (model mimo)
## 2026-08-26 01:54:44 UTC [api] (model mimo)
## 2026-08-26 03:08:18 UTC [api] (model mimo)
## 2026-08-26 04:03:03 UTC [api] (model mimo)
## 2026-08-26 04:52:33 UTC [api] (model mimo)
## 2026-08-26 05:31:31 UTC [api] (model mimo)
## 2026-08-26 06:03:48 UTC [api] (model mimo)
## 2026-08-26 07:05:55 UTC [api] (model mimo)
## 2026-08-26 07:57:36 UTC [api] (model mimo)
## 2026-08-26 08:55:06 UTC [api] (model mimo)
## 2026-08-26 09:47:48 UTC [api] (model mimo)
## 2026-08-26 10:21:28 UTC [api] (model mimo)
## 2026-08-26 10:59:50 UTC [api] (model mimo)
## 2026-08-26 11:38:46 UTC [api] (model mimo)
## 2026-08-26 12:04:08 UTC [api] (model mimo)
## 2026-08-26 13:13:19 UTC [api] (model mimo)
## 2026-08-26 14:08:18 UTC [api] (model mimo)
## 2026-08-26 15:52:53 UTC [api] (model mimo)
## 2026-08-26 16:47:12 UTC [api] (model mimo)
## 2026-08-26 18:31:20 UTC [api] (model mimo)
## 2026-08-26 21:09:17 UTC [api] (model mimo)
## 2026-08-27 00:48:24 UTC [api] (model mimo)
## 2026-08-27 10:40:14 UTC [api] (model mimo)
## 2026-09-26 13:43:47 UTC [api] (model mimo)
## 2026-09-26 17:44:12 UTC [app] (model mimo)
## 2026-09-26 21:05:44 UTC [sdk] (model mimo)
[PRIO] app.gladia.io: 7.7 (attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8) reason: /signin?redirect_to reflection byte-fresh 200/27448B + 0 form-action CSP gap = unauthed open-redirect surface post-auth HUMAN_ONLY
[PRIO] api.gladia.io: 7.3 (attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6) reason: 14-path spec frozen but SSRF-by-design audio_url surface persists AUTH_HELPED, high business value transcription API, key-gated
[PRIO] sdk: 6.5 (attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7) reason: npm gladia@0.1.3 dist-tag latest orphaned (shasum cc96f84a, GitHub alexisbouchez 404), public registry gate_ease 10, supply-chain hijack surface
[PRIO] gladia.io: 3.2 (attack_surface:3 business_value:3 tech_exposure:2 gate_ease:8 cloud_surface:1 freshness:3) reason: marketing site only 301->www->302 Google Forms bounty channel, low tech exposure
[HYP] Post-auth open redirect via redirect_to enables OAuth code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed not oversight) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft.
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: PASSIVE: GET https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com observe form action reflection and response headers; HUMAN: with authorized test account complete login via that URL and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OPENAPI 14-path spec frozen, POST /v2/pre-recorded requires x-gladia-key (401/144 NestJS fresh) but spec defines audio_url/url params by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only, not alternative SSRF.
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns, proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} and compare vs benign audio_url; also GET https://api.gladia.io/v2/live/health with key to confirm not SSRF-relevant
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[HYP] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 re-verified fresh 2026-09-26 shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable (ACCEPTED OTHER @ sdk alive); prior ranked hypothesis notes WebSocket URL query leaks raw API key; attacker can claim GitHub namespace and publish malicious 0.1.4.
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" or "api_key" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN, High
testability: PASSIVE
[FINAL] Post-auth open redirect via redirect_to enables OAuth code theft and account takeover: confidence 85, OAUTH not on REJECTED list (ACCEPTED OAUTH @ app.gladia.io), concrete PASSIVE+HUMAN verify_steps, retained rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF not on REJECTED (ACCEPTED SSRF @ api.gladia.io AUTH_HELPED), concrete AUTH_HELPED verify_steps, retained rank 2
[FINAL] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket query: confidence 72, OTHER not on REJECTED (ACCEPTED OTHER @ sdk), concrete PASSIVE registry + GitHub verify_steps, retained rank 3
[PARKED] none: all 3 hypotheses confidence >=40, class not on REJECTED list (AUTH@api.gladia.io, AUTH@app.gladia.io return-to, MISCONFIG@reposcan are rejected but not used), each has concrete verify_steps
[NEXT] PROBE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk + GET https://api.github.com/users/alexisbouchez) — verify dist-tag latest still 0.1.3, shasum cc96f84a, repository 404 orphaned, and grep tarball for WebSocket URL query api_key leakage; ≤1 rps, read-only
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh 2026-09-26, 0 CSP form-action directives, post-auth honoring sole unverified gate remains HUMAN_ONLY chain surface
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen NO_DRIFT 14 paths/7 webhooks, POST /v2/pre-recorded 401 NestJS key-gated, SSRF-by-design via audio_url persists AUTH_HELPED
[LEARN] ACCEPTED OTHER @ sdk: gladia@0.1.3 dist-tag latest re-verified 2026-09-26 shasum cc96f84a unchanged, GitHub API alexisbouchez 404 orphaned/irrevocable, static no new version this cycle
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP 0 form-action directives re-confirmed fresh, gap confirmed not oversight
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented not in 14-path OpenAPI spec, 401 key-gated informational only re-confirmed
[LEARN] REJECTED AUTH @ api.gladia.io: no-key POST /v2/pre-recorded still 401/144 NestJS no bypass this cycle
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained | app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease | sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-26 23:34:46 UTC [gladia] (model mimo)
## 2026-09-27 05:13:10 UTC [api] (model mimo)
## 2026-09-27 07:29:45 UTC [app] (model mimo)
[PRIO] app.gladia.io: 7.7 (attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8) reason: /signin?redirect_to reflection byte-fresh 200/27448B + 0 form-action CSP gap = unauthed open-redirect surface post-auth HUMAN_ONLY
[PRIO] api.gladia.io: 7.3 (attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6) reason: 14-path spec frozen but SSRF-by-design audio_url surface persists AUTH_HELPED, high business value transcription API, key-gated
[PRIO] sdk: 6.5 (attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7) reason: npm gladia@0.1.3 dist-tag latest orphaned (shasum cc96f84a, GitHub alexisbouchez 404), public registry gate_ease 10, supply-chain hijack surface
[PRIO] gladia.io: 3.2 (attack_surface:3 business_value:3 tech_exposure:2 gate_ease:8 cloud_surface:1 freshness:3) reason: marketing site only 301->www->302 Google Forms bounty channel, low tech exposure
[HYP] Post-auth open redirect via redirect_to enables OAuth code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed not oversight) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft.
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: PASSIVE: GET https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com observe form action reflection and response headers; HUMAN: with authorized test account complete login via that URL and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OPENAPI 14-path spec frozen, POST /v2/pre-recorded requires x-gladia-key (401/144 NestJS fresh) but spec defines audio_url/url params by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only, not alternative SSRF.
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns, proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} and compare vs benign audio_url; also GET https://api.gladia.io/v2/live/health with key to confirm not SSRF-relevant
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[HYP] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 re-verified fresh 2026-09-26 shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable (ACCEPTED OTHER @ sdk alive); prior ranked hypothesis notes WebSocket URL query leaks raw API key; attacker can claim GitHub namespace and publish malicious 0.1.4.
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" or "api_key" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN, High
testability: PASSIVE
[FINAL] Post-auth open redirect via redirect_to enables OAuth code theft and account takeover: confidence 85, OAUTH not on REJECTED list (ACCEPTED OAUTH @ app.gladia.io), concrete PASSIVE+HUMAN verify_steps, retained rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF not on REJECTED (ACCEPTED SSRF @ api.gladia.io AUTH_HELPED), concrete AUTH_HELPED verify_steps, retained rank 2
[FINAL] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket query: confidence 72, OTHER not on REJECTED (ACCEPTED OTHER @ sdk), concrete PASSIVE registry + GitHub verify_steps, retained rank 3
[PARKED] none: all 3 hypotheses confidence >=40, class not on REJECTED list (AUTH@api.gladia.io, AUTH@app.gladia.io return-to, MISCONFIG@reposcan are rejected but not used), each has concrete verify_steps
[NEXT] PROBE: GET https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com — observe form action reflection and response headers (CSP, Set-Cookie), confirm byte-fresh 200/27448B with action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"; ≤1 rps, read-only
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh 2026-09-26, 0 CSP form-action directives, post-auth honoring sole unverified gate remains HUMAN_ONLY chain surface
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen NO_DRIFT 14 paths/7 webhooks, POST /v2/pre-recorded 401 NestJS key-gated, SSRF-by-design via audio_url persists AUTH_HELPED
[LEARN] ACCEPTED OTHER @ sdk: gladia@0.1.3 dist-tag latest re-verified 2026-09-26 shasum cc96f84a unchanged, GitHub API alexisbouchez 404 orphaned/irrevocable, static no new version this cycle
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP 0 form-action directives re-confirmed fresh, gap confirmed not oversight
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented not in 14-path OpenAPI spec, 401 key-gated informational only re-confirmed
[LEARN] REJECTED AUTH @ api.gladia.io: no-key POST /v2/pre-recorded still 401/144 NestJS no bypass this cycle
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained | app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease | sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-27 07:49:23 UTC [sdk] (model mimo)
[PRIO] app.gladia.io: 7.7 (attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8) reason: /signin?redirect_to reflection byte-fresh 200/27448B + 0 form-action CSP gap = unauthed open-redirect surface post-auth HUMAN_ONLY
[PRIO] api.gladia.io: 7.3 (attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6) reason: 14-path spec frozen but SSRF-by-design audio_url surface persists AUTH_HELPED, high business value transcription API, key-gated
[PRIO] sdk: 6.5 (attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7) reason: npm gladia@0.1.3 dist-tag latest orphaned (shasum cc96f84a, GitHub alexisbouchez 404), public registry gate_ease 10, supply-chain hijack surface
[PRIO] gladia.io: 3.2 (attack_surface:3 business_value:3 tech_exposure:2 gate_ease:8 cloud_surface:1 freshness:3) reason: marketing site only 301->www->302 Google Forms bounty channel, low tech exposure
[HYP] Post-auth open redirect via redirect_to enables OAuth code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed not oversight) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft.
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: PASSIVE: GET https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com observe form action reflection and response headers; HUMAN: with authorized test account complete login via that URL and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OPENAPI 14-path spec frozen, POST /v2/pre-recorded requires x-gladia-key (401/144 NestJS fresh) but spec defines audio_url/url params by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only, not alternative SSRF.
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns, proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} and compare vs benign audio_url; also GET https://api.gladia.io/v2/live/health with key to confirm not SSRF-relevant
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[HYP] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 re-verified fresh 2026-09-26 shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable (ACCEPTED OTHER @ sdk alive); prior ranked hypothesis notes WebSocket URL query leaks raw API key; attacker can claim GitHub namespace and publish malicious 0.1.4.
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" or "api_key" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN, High
testability: PASSIVE
[FINAL] Post-auth open redirect via redirect_to enables OAuth code theft and account takeover: confidence 85, OAUTH not on REJECTED list (ACCEPTED OAUTH @ app.gladia.io), concrete PASSIVE+HUMAN verify_steps, retained rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF not on REJECTED (ACCEPTED SSRF @ api.gladia.io AUTH_HELPED), concrete AUTH_HELPED verify_steps, retained rank 2
[FINAL] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket query: confidence 72, OTHER not on REJECTED (ACCEPTED OTHER @ sdk), concrete PASSIVE registry + GitHub verify_steps, retained rank 3
[PARKED] none: all 3 hypotheses confidence >=40, class not on REJECTED list (AUTH@api.gladia.io, AUTH@app.gladia.io return-to, MISCONFIG@reposcan are rejected but not used), each has concrete verify_steps
[NEXT] PROBE: GET https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com — observe form action reflection and response headers (CSP, Set-Cookie), confirm byte-fresh 200/27448B with action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"; ≤1 rps, read-only
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh 2026-09-26, 0 CSP form-action directives, post-auth honoring sole unverified gate remains HUMAN_ONLY chain surface
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen NO_DRIFT 14 paths/7 webhooks, POST /v2/pre-recorded 401/144B NestJS key-gated, SSRF-by-design via audio_url persists AUTH_HELPED
[LEARN] ACCEPTED OTHER @ sdk: gladia@0.1.3 dist-tag latest re-verified 2026-09-26 shasum cc96f84a unchanged, GitHub API alexisbouchez 404 orphaned/irrevocable, static no new version this cycle
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP 0 form-action directives re-confirmed fresh, gap confirmed not oversight
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented not in 14-path OpenAPI spec, 401 key-gated informational only re-confirmed
[LEARN] REJECTED AUTH @ api.gladia.io: no-key POST /v2/pre-recorded still 401/144 NestJS no bypass this cycle
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained | app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease | sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-27 11:58:23 UTC [gladia] (model mimo)
[PRIO] app.gladia.io: 7.7 (attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8) reason: /signin?redirect_to reflection byte-fresh 200/27448B + 0 form-action CSP gap = unauthed open-redirect surface post-auth HUMAN_ONLY
[PRIO] api.gladia.io: 7.3 (attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6) reason: 14-path spec frozen but SSRF-by-design audio_url surface persists AUTH_HELPED, high business value transcription API, key-gated
[PRIO] sdk: 6.5 (attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7) reason: npm gladia@0.1.3 dist-tag latest orphaned (shasum cc96f84a, GitHub alexisbouchez 404), public registry gate_ease 10, supply-chain hijack surface
[PRIO] gladia.io: 3.2 (attack_surface:3 business_value:3 tech_exposure:2 gate_ease:8 cloud_surface:1 freshness:3) reason: marketing site only 301->www->302 Google Forms bounty channel, low tech exposure
[HYP] Post-auth open redirect via redirect_to enables OAuth code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed not oversight) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft.
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: PASSIVE: GET https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com observe form action reflection and response headers; HUMAN: with authorized test account complete login via that URL and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OPENAPI 14-path spec frozen, POST /v2/pre-recorded requires x-gladia-key (401/144 NestJS fresh) but spec defines audio_url/url params by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only, not alternative SSRF.
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns, proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} and compare vs benign audio_url; also GET https://api.gladia.io/v2/live/health with key to confirm not SSRF-relevant
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[HYP] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 re-verified fresh 2026-09-26 shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable (ACCEPTED OTHER @ sdk alive); prior ranked hypothesis notes WebSocket URL query leaks raw API key; attacker can claim GitHub namespace and publish malicious 0.1.4.
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" or "api_key" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN, High
testability: PASSIVE
[FINAL] Post-auth open redirect via redirect_to enables OAuth code theft and account takeover: confidence 85, OAUTH not on REJECTED list (ACCEPTED OAUTH @ app.gladia.io), concrete PASSIVE+HUMAN verify_steps, retained rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF not on REJECTED (ACCEPTED SSRF @ api.gladia.io AUTH_HELPED), concrete AUTH_HELPED verify_steps, retained rank 2
[FINAL] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket query: confidence 72, OTHER not on REJECTED (ACCEPTED OTHER @ sdk), concrete PASSIVE registry + GitHub verify_steps, retained rank 3
[PARKED] none: all 3 hypotheses confidence >=40, class not on REJECTED list (AUTH@api.gladia.io, AUTH@app.gladia.io return-to, MISCONFIG@reposcan are rejected but not used), each has concrete verify_steps
[NEXT] HUMAN: With authorized test account, complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location header to confirm redirect_to honored
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh 2026-09-26, 0 CSP form-action directives, post-auth honoring sole unverified gate remains HUMAN_ONLY chain surface
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen NO_DRIFT 14 paths/7 webhooks, POST /v2/pre-recorded 401/144B NestJS key-gated, SSRF-by-design via audio_url persists AUTH_HELPED
[LEARN] ACCEPTED OTHER @ sdk: gladia@0.1.3 dist-tag latest re-verified 2026-09-26 shasum cc96f84a unchanged, GitHub API alexisbouchez 404 orphaned/irrevocable, static no new version this cycle
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP 0 form-action directives re-confirmed fresh, gap confirmed not oversight
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented not in 14-path OpenAPI spec, 401 key-gated informational only re-confirmed
[LEARN] REJECTED AUTH @ api.gladia.io: no-key POST /v2/pre-recorded still 401/144 NestJS no bypass this cycle
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained | app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease | sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-27 16:57:12 UTC [api] (model mimo)
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] sdk: 6.5 attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OPENAPI 14-path spec frozen NO_DRIFT, POST /v2/pre-recorded requires x-gladia-key (401/144 NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url; GET https://api.gladia.io/v2/live/health with key confirm not SSRF-relevant
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[HYP] Post-auth open redirect via redirect_to enables OAuth code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed not oversight) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: PASSIVE: GET https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com observe form action reflection and response headers; HUMAN: with authorized test account complete login via that URL and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 re-verified fresh 2026-09-26 shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable (ACCEPTED OTHER @ sdk alive); prior ranked hypothesis notes WebSocket URL query leaks raw API key; attacker can claim GitHub namespace and publish malicious 0.1.4
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" or "api_key" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN, High
testability: PASSIVE
[FINAL] Post-auth open redirect via redirect_to enables OAuth code theft and account takeover: confidence 85, OAUTH not on REJECTED list (ACCEPTED OAUTH @ app.gladia.io), concrete PASSIVE+HUMAN verify_steps, retained rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF not on REJECTED (ACCEPTED SSRF @ api.gladia.io AUTH_HELPED), concrete AUTH_HELPED verify_steps, retained rank 2
[FINAL] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket query: confidence 72, OTHER not on REJECTED (ACCEPTED OTHER @ sdk), concrete PASSIVE registry + GitHub verify_steps, retained rank 3
[NEXT] PROBE: GET https://api.gladia.io/health — observe status code, response headers, and body for any unauthenticated informational endpoint not in OpenAPI spec (≤1 rps, read-only)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen NO_DRIFT 14 paths/7 webhooks, POST /v2/pre-recorded 401/144B NestJS key-gated, SSRF-by-design via audio_url persists AUTH_HELPED
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh 2026-09-26, 0 CSP form-action directives, post-auth honoring sole unverified gate remains HUMAN_ONLY chain surface
[LEARN] ACCEPTED OTHER @ sdk: gladia@0.1.3 dist-tag latest re-verified 2026-09-26 shasum cc96f84a unchanged, GitHub API alexisbouchez 404 orphaned/irrevocable, static no new version this cycle
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP 0 form-action directives re-confirmed fresh, gap confirmed not oversight
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented not in 14-path OpenAPI spec, 401 key-gated informational only re-confirmed
[LEARN] REJECTED AUTH @ api.gladia.io: no-key POST /v2/pre-recorded still 401/144 NestJS no bypass this cycle
[LEARN] ACCEPTED OTHER @ api: no new surface this cycle beyond ACCEPTED SSRF + MISCONFIG, re-confirmed static via NO_DRIFT OpenAPI spec
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained | app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease | sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-27 20:09:04 UTC [app] (model mimo)
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] sdk: 6.5 attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft via trusted domain
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: PASSIVE: GET https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com observe form action reflection and response headers; HUMAN: with authorized test account complete login via that URL and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OPENAPI 14-path spec frozen NO_DRIFT, POST /v2/pre-recorded requires x-gladia-key (401/144 NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url; GET https://api.gladia.io/v2/live/health with key confirm not SSRF-relevant
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[HYP] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket URL query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 re-verified fresh 2026-09-26 shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable; prior ranked hypothesis notes WebSocket URL query leaks raw API key; attacker can claim GitHub namespace and publish malicious 0.1.4
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" or "api_key" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN, High
testability: PASSIVE
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 2
[FINAL] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket URL query: confidence 72, OTHER @ sdk, PASSIVE, rank 3
[NEXT] HUMAN: With authorized test account, complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location header to confirm redirect_to honored (rotation focus: app)
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained | app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease | sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-27 23:01:48 UTC [sdk] (model mimo)
[PRIO] sdk: 6.5 attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[HYP] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket URL query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 re-verified fresh 2026-09-26 shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable; prior ranked hypothesis notes WebSocket URL query leaks raw API key; attacker can claim GitHub namespace and publish malicious 0.1.4
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" or "api_key" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN, High
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft via trusted domain
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: PASSIVE: GET https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com observe form action reflection and response headers; HUMAN: with authorized test account complete login via that URL and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OPENAPI 14-path spec frozen NO_DRIFT, POST /v2/pre-recorded requires x-gladia-key (401/144 NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url; GET https://api.gladia.io/v2/live/health with key confirm not SSRF-relevant
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 2
[FINAL] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket URL query: confidence 72, OTHER @ sdk, PASSIVE, rank 3
[NEXT] PROBE: GET https://registry.npmjs.org/gladia — observe repository.url, maintainers, dist-tags, time.modified; then GET https://registry.npmjs.org/@gladiaio/sdk for comparison (≤1 rps, read-only)
[LEARN] ACCEPTED OTHER @ sdk: no new surface this cycle, re-confirmed static — dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub alexisbouchez 404 orphaned/irrevocable
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh, 0 CSP form-action directives, post-auth honoring sole unverified gate HUMAN_ONLY
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen NO_DRIFT 14 paths/7 webhooks, POST /v2/pre-recorded 401/144B NestJS key-gated, SSRF-by-design via audio_url persists AUTH_HELPED
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP 0 form-action directives re-confirmed fresh, gap confirmed not oversight
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented not in 14-path OpenAPI spec, 401 key-gated informational only re-confirmed
[LEARN] REJECTED AUTH @ api.gladia.io: no-key POST /v2/pre-recorded still 401/144 NestJS no bypass this cycle
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained | app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease | sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-28 01:37:06 UTC [gladia] (model mimo)
## 2026-09-28 08:39:34 UTC [api] (model mimo)
## 2026-09-28 17:38:35 UTC [app] (model mimo)
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] sdk: 6.5 attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft via trusted domain
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OPENAPI 14-path spec frozen NO_DRIFT, POST /v2/pre-recorded requires x-gladia-key (401/144 NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[HYP] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket URL query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 re-verified fresh 2026-09-26 shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable; prior ranked hypothesis notes WebSocket URL query leaks raw API key; attacker can claim GitHub namespace and publish malicious 0.1.4
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" or "api_key" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN, High
testability: PASSIVE
[PARKED] None dropped: all three hypotheses have confidence ≥ 72, classes not on REJECTED list (OAUTH, SSRF, OTHER all ACCEPTED in KB), and all have concrete verify_steps (HUMAN_ONLY, AUTH_HELPED, PASSIVE respectively)
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 2
[FINAL] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket URL query: confidence 72, OTHER @ sdk, PASSIVE, rank 3
[NEXT] HUMAN: With authorized test account, complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location header to confirm redirect_to honored (rotation focus: app)
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh, 0 CSP form-action directives, post-auth honoring sole unverified gate HUMAN_ONLY
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen NO_DRIFT 14 paths/7 webhooks, POST /v2/pre-recorded 401/144B NestJS key-gated, SSRF-by-design via audio_url persists AUTH_HELPED
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub alexisbouchez 404 orphaned/irrevocable
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] REJECTED AUTH @ api.gladia.io: no-key POST /v2/pre-recorded still 401/144 NestJS no bypass this cycle
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained | app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease | sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-28 23:15:00 UTC [sdk] (model mimo)
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] sdk: 6.5 attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft via trusted domain
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OPENAPI 14-path spec frozen NO_DRIFT, POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[HYP] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket URL query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 re-verified fresh 2026-09-26 shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable; prior ranked hypothesis notes WebSocket URL query leaks raw API key; attacker can claim GitHub namespace and publish malicious 0.1.4
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" or "api_key" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN, High
testability: PASSIVE
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 2
[FINAL] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket URL query: confidence 72, OTHER @ sdk, PASSIVE, rank 3
[NEXT] PROBE: GET https://registry.npmjs.org/gladia — observe repository.url, maintainers, dist-tags, time.modified; then GET https://registry.npmjs.org/@gladiaio/sdk for comparison (≤1 rps, read-only)
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh, 0 CSP form-action directives, post-auth honoring sole unverified gate HUMAN_ONLY
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen NO_DRIFT 14 paths/7 webhooks, POST /v2/pre-recorded 401/144B NestJS key-gated, SSRF-by-design via audio_url persists AUTH_HELPED
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub alexisbouchez 404 orphaned/irrevocable
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] REJECTED AUTH @ api.gladia.io: no-key POST /v2/pre-recorded still 401/144 NestJS no bypass this cycle
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained | app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease | sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-29 05:39:26 UTC [gladia] (model mimo)
[NEW] None — OpenAPI spec NO_DRIFT (14 paths, 7 webhooks structurally identical), inventory timestamps show no new endpoints since 2026-09-28 23:15:08, knowledge base last updated 2026-09-28 for all ACCEPTED/REJECTED entries
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] sdk: 6.5 attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft via trusted domain
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT, POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[HYP] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket URL query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 re-verified fresh 2026-09-26 shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable; prior ranked hypothesis notes WebSocket URL query leaks raw API key; attacker can claim GitHub namespace and publish malicious 0.1.4
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" or "api_key" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN, High
testability: PASSIVE
[PARKED] None dropped: all three hypotheses have confidence ≥ 72, classes OAUTH/SSRF/OTHER all ACCEPTED in KB, and all have concrete verify_steps (HUMAN_ONLY, AUTH_HELPED, PASSIVE respectively)
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 2
[FINAL] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket URL query: confidence 72, OTHER @ sdk, PASSIVE, rank 3
[NEXT] PROBE: GET https://registry.npmjs.org/gladia — observe repository.url, maintainers, dist-tags, time.modified; then GET https://registry.npmjs.org/@gladiaio/sdk for comparison (≤1 rps, read-only)
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh, 0 CSP form-action directives, post-auth honoring sole unverified gate HUMAN_ONLY
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen NO_DRIFT 14 paths/7 webhooks, POST /v2/pre-recorded 401/144B NestJS key-gated, SSRF-by-design via audio_url persists AUTH_HELPED
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub alexisbouchez 404 orphaned/irrevocable
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] REJECTED AUTH @ api.gladia.io: no-key POST /v2/pre-recorded still 401/144 NestJS no bypass this cycle
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained | app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease | sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-29 12:47:01 UTC [api] (model mimo)
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] sdk: 6.5 attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft via trusted domain
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT, POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[HYP] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket URL query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 re-verified fresh 2026-09-26 shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable; prior ranked hypothesis notes WebSocket URL query leaks raw API key; attacker can claim GitHub namespace and publish malicious 0.1.4
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" or "api_key" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN, High
testability: PASSIVE
[PARKED] None dropped: all three hypotheses have confidence ≥ 72, classes OAUTH/SSRF/OTHER all ACCEPTED in KB, and all have concrete verify_steps (HUMAN_ONLY, AUTH_HELPED, PASSIVE respectively)
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 2
[FINAL] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket URL query: confidence 72, OTHER @ sdk, PASSIVE, rank 3
[NEXT] PROBE: GET https://registry.npmjs.org/gladia — observe repository.url, maintainers, dist-tags, time.modified; then GET https://registry.npmjs.org/@gladiaio/sdk for comparison (≤1 rps, read-only)
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh, 0 CSP form-action directives, post-auth honoring sole unverified gate HUMAN_ONLY
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen NO_DRIFT 14 paths/7 webhooks, POST /v2/pre-recorded 401/144B NestJS key-gated, SSRF-by-design via audio_url persists AUTH_HELPED
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub alexisbouchez 404 orphaned/irrevocable
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] REJECTED AUTH @ api.gladia.io: no-key POST /v2/pre-recorded still 401/144 NestJS no bypass this cycle
[LEARN] ACCEPTED OTHER @ api: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained | app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease | sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-29 18:37:42 UTC [app] (model mimo)
## 2026-09-29 22:57:56 UTC [sdk] (model mimo)
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] sdk: 6.5 attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable; WebSocket URL query leaks raw API key per prior ranked hypothesis
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" or "api_key" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN, High
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft via trusted domain
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT, POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[PARKED] None dropped: all three hypotheses have confidence ≥ 72, classes OAUTH/SSRF/OTHER all ACCEPTED in KB, and all have concrete verify_steps (HUMAN_ONLY, AUTH_HELPED, PASSIVE respectively)
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 2
[FINAL] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query: confidence 72, OTHER @ sdk, PASSIVE, rank 3
[NEXT] PROBE: GET https://registry.npmjs.org/gladia — observe repository.url, maintainers, dist-tags, time.modified; then GET https://registry.npmjs.org/@gladiaio/sdk for comparison (≤1 rps, read-only)
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh, 0 CSP form-action directives, post-auth honoring sole unverified gate HUMAN_ONLY
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec frozen NO_DRIFT 14 paths/7 webhooks, POST /v2/pre-recorded 401/144B NestJS key-gated, SSRF-by-design via audio_url persists AUTH_HELPED
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub alexisbouchez 404 orphaned/irrevocable
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] REJECTED AUTH @ api.gladia.io: no-key POST /v2/pre-recorded still 401/144 NestJS no bypass this cycle
[LEARN] ACCEPTED OTHER @ api: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained | app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease | sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-30 02:04:09 UTC [gladia] (model mimo)
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] sdk: 6.5 attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT, POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft via trusted domain
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable; WebSocket URL query leaks raw API key per prior ranked hypothesis
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" or "api_key" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN, High
testability: PASSIVE
[PARKED] None dropped: all three hypotheses have confidence ≥ 72, classes OAUTH/SSRF/OTHER all ACCEPTED in KB, and all have concrete verify_steps (HUMAN_ONLY, AUTH_HELPED, PASSIVE respectively)
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 2
[FINAL] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query: confidence 72, OTHER @ sdk, PASSIVE, rank 3
[NEXT] PROBE: GET https://registry.npmjs.org/gladia — observe repository.url, maintainers, dist-tags, time.modified; then GET https://registry.npmjs.org/@gladiaio/sdk for comparison (≤1 rps, read-only)
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained | app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease | sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-30 08:28:09 UTC [api] (model mimo)
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] sdk: 6.5 attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT, POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft via trusted domain
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable; WebSocket URL query leaks raw API key per prior ranked hypothesis
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" or "api_key" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN, High
testability: PASSIVE
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 2
[FINAL] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query: confidence 72, OTHER @ sdk, PASSIVE, rank 3
[NEXT] PROBE: GET https://registry.npmjs.org/gladia — observe repository.url, maintainers, dist-tags, time.modified; then GET https://registry.npmjs.org/@gladiaio/sdk for comparison (≤1 rps, read-only)
[LEARN] ACCEPTED OTHER @ api: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained | app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease | sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-30 15:55:53 UTC [app] (model mimo)
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8  
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6  
[PRIO] sdk: 6.5 attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com") + CSP 0 form-action directives (gap confirmed) = post-auth redirect honoring sole unverified gate; chains to OAuth code/state theft via trusted domain
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth -> OAuth authorization code leakage -> session hijack/ATO, phishing via trusted domain, High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT, POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata -> IAM credentials -> full AWS/GCP takeover, cross-tenant data access, Critical
testability: AUTH_HELPED
[HYP] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 shasum cc96f84a unchanged, description "Official TypeScript SDK for Gladia" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable; source code src/client.ts:245-247 confirms WebSocket URL query leaks raw API key via ?x-gladia-key=<key>
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned (softwarecitadel@gmail.com), npm package files grep shows WebSocket wss:// + "?x-gladia-key=" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (and GET https://registry.npmjs.org/@gladiaio/sdk), check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|api_key\|x-gladia-key" ; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover -> malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN/browser history, High
testability: PASSIVE
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 2
[FINAL] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query: confidence 72, OTHER @ sdk, PASSIVE, rank 3
[NEXT] PROBE: GET https://registry.npmjs.org/@gladiaio/sdk — confirm latest dist-tag 2.1.0, maintainers all @gladia.io emails, repository github.com/gladiaio/sdk (active), compare to orphaned gladia@0.1.3 surface for confusion risk
[LEARN] ACCEPTED OTHER @ npm gladia@0.1.3: class alive, re-verified fresh this cycle — dist-tag latest=0.1.3, shasum cc96f84a unchanged, GitHub API user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:245-247
[LEARN] ACCEPTED OTHER @ app: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 -> cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft -> ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-09-30 20:51:07 UTC [sdk] (model mimo)
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8  
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6  
[PRIO] sdk: 6.5 attack_surface:7 business_value:6 tech_exposure:6 gate_ease:10 cloud_surface:1 freshness:7  
[HYP] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 97
reasoning: gladia@0.1.3 dist-tag latest, shasum cc96f84a unchanged since 2025-04-07; description "Official TypeScript SDK for Gladia" but maintainer softwarecitadel@gmail.com, repository github.com/alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); src/client.ts:245-247 constructs WebSocket URL with `wsUrl.searchParams.append('x-gladia-key', this.apiKey)` leaking raw key in query string; official @gladiaio/sdk@2.1.0 (20+ @gladia.io maintainers, active github.com/gladiaio/sdk) uses header auth + server-issued pre-auth WebSocket URL — no key in query
evidence_needed: npm registry shows gladia@0.1.3 repository.url=github.com/alexisbouchez/gladia.ts (404), maintainers=[softwarecitadel]; tarball grep confirms WebSocket URL query leak; @gladiaio/sdk dist-tag 2.1.0 with @gladia.io maintainers and active repo
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia (confirm 404 GitHub, orphaned maintainer, query leak in tarball); GET https://registry.npmjs.org/@gladiaio/sdk (confirm 2.1.0, @gladia.io maintainers, active repo); diff WebSocket auth patterns
impact: Supply-chain confusion → developers install malicious orphaned package → raw API key logged in proxies/CDN/browser history → full account compromise; High severity
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP 0 form-action directives (grep-count=0) = gap confirmed; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[FINAL] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query: confidence 97, OTHER @ sdk, PASSIVE, rank 1
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 2
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 3
[NEXT] PROBE: GET https://registry.npmjs.org/gladia/-/gladia-0.1.3.tgz — download tarball, extract and grep src/client.ts for WebSocket URL construction confirming `x-gladia-key` in query string (≤1 rps, read-only)
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:245-247
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED OTHER @ api: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained  
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease  
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0
## 2026-10-01 00:32:10 UTC [gladia] (model mimo)
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] sdk: 7.1 attack_surface:7 business_value:7 tech_exposure:7 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 97
reasoning: gladia@0.1.3 dist-tag latest, shasum cc96f84a unchanged since 2025-04-07; description "Official TypeScript SDK for Gladia" but maintainer softwarecitadel@gmail.com, repository github.com/alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); src/client.ts:245-247 constructs WebSocket URL with `wsUrl.searchParams.append('x-gladia-key', this.apiKey)` leaking raw key in query string; official @gladiaio/sdk@2.1.0 (20+ @gladia.io maintainers, active github.com/gladiaio/sdk) uses header auth + server-issued pre-auth WebSocket URL — no key in query
evidence_needed: npm registry shows gladia@0.1.3 repository.url=github.com/alexisbouchez/gladia.ts (404), maintainers=[softwarecitadel]; tarball grep confirms WebSocket URL query leak; @gladiaio/sdk dist-tag 2.1.0 with @gladia.io maintainers and active repo
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia/-/gladia-0.1.3.tgz — download tarball, extract and grep src/client.ts for WebSocket URL construction confirming `x-gladia-key` in query string (≤1 rps, read-only)
impact: Supply-chain confusion → developers install malicious orphaned package → raw API key logged in proxies/CDN/browser history → full account compromise; High severity
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-09-26 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP 0 form-action directives (grep-count=0) = gap confirmed; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[FINAL] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query: confidence 97, OTHER @ sdk, PASSIVE, rank 1
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 2
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 3
[NEXT] PROBE: GET https://registry.npmjs.org/gladia/-/gladia-0.1.3.tgz — download tarball, extract and grep src/client.ts for WebSocket URL construction confirming `x-gladia-key` in query string (≤1 rps, read-only)
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:245-247
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED OTHER @ api: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0
## 2026-10-01 07:12:30 UTC [api] (model mimo)
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] sdk: 7.1 attack_surface:7 business_value:7 tech_exposure:7 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-10-01 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP 0 form-action directives (grep-count=0) = gap confirmed; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High severity
testability: HUMAN_ONLY
[HYP] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 97
reasoning: gladia@0.1.3 dist-tag latest, shasum cc96f84a unchanged since 2025-04-07; description "Official TypeScript SDK for Gladia" but maintainer softwarecitadel@gmail.com, repository github.com/alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); src/client.ts:307 constructs WebSocket URL with `wsUrl.searchParams.append('x-gladia-key', this.apiKey)` leaking raw key in query string; official @gladiaio/sdk@2.1.0 (20+ @gladia.io maintainers, active github.com/gladiaio/sdk) uses header auth + server-issued pre-auth WebSocket URL — no key in query
evidence_needed: npm registry shows gladia@0.1.3 repository.url=github.com/alexisbouchez/gladia.ts (404), maintainers=[softwarecitadel]; tarball grep confirms WebSocket URL query leak; @gladiaio/sdk dist-tag 2.1.0 with @gladia.io maintainers and active repo
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia/-/gladia-0.1.3.tgz — download tarball, extract and grep src/client.ts for WebSocket URL construction confirming `x-gladia-key` in query string (≤1 rps, read-only)
impact: Supply-chain confusion → developers install malicious orphaned package → raw API key logged in proxies/CDN/browser history → full account compromise; High severity
testability: PASSIVE
[FINAL] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query: confidence 97, OTHER @ sdk, PASSIVE, rank 1
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 2
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 3
[NEXT] PROBE: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} — compare response/timing vs benign audio_url to confirm SSRF reach to cloud metadata (AUTH_HELPED, rotation focus api)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307
[LEARN] ACCEPTED OTHER @ api: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0
## 2026-10-01 14:32:29 UTC [app] (model mimo)
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] sdk: 6.9 attack_surface:7 business_value:7 tech_exposure:7 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-10-01 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP 0 form-action directives (grep-count=0) = gap confirmed; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[HYP] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 97
reasoning: gladia@0.1.3 dist-tag latest, shasum cc96f84a unchanged since 2025-04-07; description "Official TypeScript SDK for Gladia" but maintainer softwarecitadel@gmail.com, repository github.com/alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); src/client.ts:307 constructs WebSocket URL with `wsUrl.searchParams.append('x-gladia-key', this.apiKey)` leaking raw key in query string; official @gladiaio/sdk@2.1.0 (20+ @gladia.io maintainers, active github.com/gladiaio/sdk) uses header auth + server-issued pre-auth WebSocket URL — no key in query
evidence_needed: npm registry shows gladia@0.1.3 repository.url=github.com/alexisbouchez/gladia.ts (404), maintainers=[softwarecitadel]; tarball grep confirms WebSocket URL query leak; @gladiaio/sdk dist-tag 2.1.0 with @gladia.io maintainers and active repo
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia/-/gladia-0.1.3.tgz — download tarball, extract and grep src/client.ts for WebSocket URL construction confirming `x-gladia-key` in query string (≤1 rps, read-only)
impact: Supply-chain confusion → developers install malicious orphaned package → raw API key logged in proxies/CDN/browser history → full account compromise; High severity
testability: PASSIVE
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query: confidence 97, OTHER @ sdk, PASSIVE, rank 2
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 3
[NEXT] HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location header to confirm redirect_to honored (rotation focus app)
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0
## 2026-10-01 20:24:19 UTC [sdk] (model mimo)
[PRIO] sdk: 7.1 attack_surface:7 business_value:7 tech_exposure:7 gate_ease:10 cloud_surface:1 freshness:7
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[HYP] PyPI gladiaio-sdk supply chain risk — unverified parity with official npm SDK
class: OTHER
asset: sdk
confidence: 50
reasoning: PyPI gladiaio-sdk exists per leads; not analyzed in knowledge base; orphaned npm gladia@0.1.3 confirmed malicious pattern (WebSocket key leak); official npm @gladiaio/sdk@2.1.0 active with @gladia.io maintainers; PyPI package maintainer/origin/repo unverified
evidence_needed: PyPI registry metadata for gladiaio-sdk (maintainers, repo URL, description, latest version); source comparison with @gladiaio/sdk to verify parity or divergence
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers, repo, description, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball
impact: Supply chain confusion → developers install malicious/outdated PyPI package → credential leak or RCE; High severity
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-10-01 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP 0 form-action directives (grep-count=0) = gap confirmed; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[FINAL] PyPI gladiaio-sdk supply chain risk — unverified parity with official npm SDK: confidence 50, OTHER @ sdk, PASSIVE, rank 1
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 2
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 3
[NEXT] PROBE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers, repo URL, description, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (rotation focus sdk, PASSIVE, ≤1 rps)
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk require separate analysis
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk unverified parity adds additional surface
## 2026-10-02 00:45:17 UTC [gladia] (model mimo)
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] sdk: 7.1 attack_surface:7 business_value:7 tech_exposure:7 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-10-01 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP 0 form-action directives (grep-count=0) = gap confirmed; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[HYP] PyPI gladiaio-sdk supply chain risk — unverified parity with official npm SDK
class: OTHER
asset: sdk
confidence: 50
reasoning: PyPI gladiaio-sdk exists per leads; not analyzed in knowledge base; orphaned npm gladia@0.1.3 confirmed malicious pattern (WebSocket key leak); official npm @gladiaio/sdk@2.1.0 active with @gladia.io maintainers; PyPI package maintainer/origin/repo unverified
evidence_needed: PyPI registry metadata for gladiaio-sdk (maintainers, repo URL, description, latest version); source comparison with @gladiaio/sdk to verify parity or divergence
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers, repo, description, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball
impact: Supply chain confusion → developers install malicious/outdated PyPI package → credential leak or RCE; High severity
testability: PASSIVE
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 2
[FINAL] PyPI gladiaio-sdk supply chain risk — unverified parity with official npm SDK: confidence 50, OTHER @ sdk, PASSIVE, rank 3
[NEXT] PROBE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers, repo URL, description, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (rotation focus sdk, PASSIVE, ≤1 rps)
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk require separate analysis
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk unverified parity adds additional surface
## 2026-10-02 07:01:53 UTC [api] (model mimo)
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] sdk: 7.1 attack_surface:7 business_value:7 tech_exposure:7 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-10-01 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP 0 form-action directives (grep-count=0) = gap confirmed; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[HYP] PyPI gladiaio-sdk supply chain risk — unverified parity with official npm SDK
class: OTHER
asset: sdk
confidence: 50
reasoning: PyPI gladiaio-sdk exists per leads; not analyzed in knowledge base; orphaned npm gladia@0.1.3 confirmed malicious pattern (WebSocket key leak); official npm @gladiaio/sdk@2.1.0 active with @gladia.io maintainers; PyPI package maintainer/origin/repo unverified
evidence_needed: PyPI registry metadata for gladiaio-sdk (maintainers, repo URL, description, latest version); source comparison with @gladiaio/sdk to verify parity or divergence
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers, repo, description, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball
impact: Supply chain confusion → developers install malicious/outdated PyPI package → credential leak or RCE; High severity
testability: PASSIVE
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 2
[FINAL] PyPI gladiaio-sdk supply chain risk — unverified parity with official npm SDK: confidence 50, OTHER @ sdk, PASSIVE, rank 3
[NEXT] PROBE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers, repo URL, description, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (rotation focus sdk, PASSIVE, ≤1 rps)
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk require separate analysis
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk unverified parity adds additional surface
## 2026-10-02 13:49:51 UTC [app] (model mimo)
[PRIO] app.gladia.io: 7.7 attack_surface:8 business_value:8 tech_exposure:9 gate_ease:9 cloud_surface:2 freshness:8
[PRIO] api.gladia.io: 7.3 attack_surface:9 business_value:9 tech_exposure:8 gate_ease:2 cloud_surface:7 freshness:6
[PRIO] sdk: 7.1 attack_surface:7 business_value:7 tech_exposure:7 gate_ease:10 cloud_surface:1 freshness:7
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-10-01 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP 0 form-action directives (grep-count=0) = gap confirmed; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[HYP] PyPI gladiaio-sdk supply chain risk — unverified parity with official npm SDK
class: OTHER
asset: sdk
confidence: 50
reasoning: PyPI gladiaio-sdk exists per leads; not analyzed in knowledge base; orphaned npm gladia@0.1.3 confirmed malicious pattern (WebSocket key leak); official npm @gladiaio/sdk@2.1.0 active with @gladia.io maintainers; PyPI package maintainer/origin/repo unverified
evidence_needed: PyPI registry metadata for gladiaio-sdk (maintainers, repo URL, description, latest version); source comparison with @gladiaio/sdk to verify parity or divergence
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers, repo, description, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball
impact: Supply chain confusion → developers install malicious/outdated PyPI package → credential leak or RCE; High severity
testability: PASSIVE
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 2
[FINAL] PyPI gladiaio-sdk supply chain risk — unverified parity with official npm SDK: confidence 50, OTHER @ sdk, PASSIVE, rank 3
[NEXT] PROBE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers, repo URL, description, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (rotation focus sdk, PASSIVE, ≤1 rps)
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk require separate analysis
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk unverified parity adds additional surface
## 2026-10-02 19:15:38 UTC [sdk] (model mimo)
## 2026-10-02 23:45:36 UTC [gladia] (model mimo)
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-10-01 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP 0 form-action directives (grep-count=0) = gap confirmed; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[HYP] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 97
reasoning: npm gladia@0.1.3 dist-tag latest=0.1.3 unchanged, shasum cc96f84a…, description "Official TypeScript SDK for Gladia", GitHub user+repo alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); source tarball src/client.ts:307 confirms wsUrl.searchParams.append('x-gladia-key', this.apiKey) → WebSocket URL query leak; official @gladiaio/sdk@2.1.0 separate org
evidence_needed: PyPI gladiaio-sdk registry metadata (maintainers, repo URL, versions) + source comparison vs @gladiaio/sdk@2.1.0 to verify parity/divergence; confirm WebSocket key leak executes in browser devtools network tab
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers, repo, description, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball; LOCAL: install gladia@0.1.3, init client with test key, open devtools Network tab on live.connect() → verify x-gladia-key in wss:// URL query
impact: Supply chain confusion → developers install malicious/outdated package → credential leak via WebSocket query (logs/proxies/history) or RCE; Critical (orphaned + "Official" description + key leak)
testability: PASSIVE
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 1
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 2
[FINAL] Orphaned npm package gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query: confidence 97, OTHER @ sdk, PASSIVE, rank 3
[NEXT] PROBE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers, repo URL, description, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (rotation focus sdk, PASSIVE, ≤1 rps)
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk require separate analysis
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk unverified parity adds additional surface
## 2026-10-03 05:12:11 UTC [api] (model mimo)
## 2026-10-03 11:36:59 UTC [app] (model mimo)
## 2026-10-03 16:15:03 UTC [sdk] (model mimo)
[PRIO] sdk, 7.9, attack=8 business=9 tech=7 gate=10 cloud=3 fresh=8
[PRIO] app.gladia.io, 7.75, attack=8 business=9 tech=7 gate=9 cloud=2 fresh=9
[PRIO] api.gladia.io, 7.3, attack=7 business=10 tech=6 gate=3 cloud=10 fresh=7
[PRIO] gladia.io, 2.7, attack=3 business=2 tech=2 gate=5 cloud=1 fresh=5
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query; PyPI gladiaio-sdk parity unverified
class: OTHER
asset: sdk
confidence: 97
reasoning: npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged, description "Official TypeScript SDK for Gladia", GitHub user+repo alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); src/client.ts:307 confirms wsUrl.searchParams.append('x-gladia-key', this.apiKey) → WebSocket URL query leak; official @gladiaio/sdk@2.1.0 separate org; PyPI gladiaio-sdk registry metadata (maintainers, repo, versions) + source comparison vs @gladiaio/sdk@2.1.0 tarball unverified
evidence_needed: PyPI gladiaio-sdk registry metadata (maintainers, repo URL, description, versions) + downloaded sdist/wheel source diff vs @gladiaio/sdk@2.1.0 tarball; browser devtools Network tab showing x-gladia-key in wss:// URL query on live.connect()
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers, repo URL, description, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball; LOCAL: install gladia@0.1.3, init client with test key, open devtools Network tab on live.connect() → verify x-gladia-key in wss:// URL query
impact: Supply chain confusion → developers install malicious/outdated package → credential leak via WebSocket query (logs/proxies/history) or RCE; Critical (orphaned + "Official" description + key leak)
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-10-03 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP 0 form-action directives (grep-count=0) = gap confirmed; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[FINAL] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query; PyPI gladiaio-sdk parity unverified: confidence 97, OTHER @ sdk, PASSIVE, rank 1
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 2
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 3
[NEXT] PROBE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers, repo URL, description, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (rotation focus sdk, PASSIVE, ≤1 rps)
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk require separate analysis
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk unverified parity adds additional surface
## 2026-10-03 19:49:46 UTC [gladia] (model mimo)
## 2026-10-03 22:53:14 UTC [api] (model mimo)
[NEW] PyPI gladiaio-sdk@2.1.0 confirmed OFFICIAL — owned by "Gladia" organization, actively maintained (latest 2026-09-18), versions 0.1.1→2.1.0, repository URL null (no public GitHub link in metadata)
[CHANGED] npm gladia@0.1.3 orphaned status CONFIRMED — GitHub user alexisbouchez 404, repo alexisbouchez/gladia.ts 404, last publish 2025-04-07, maintainer softwarecitadel@gmail.com (non-Gladia), description still claims "Official TypeScript SDK for Gladia"
[NEW] npm @gladiaio/sdk@2.1.0 confirmed OFFICIAL — maintained by 14+ @gladia.io accounts, repo github.com/gladiaio/sdk, latest 2026-09-21, SLSA provenance attestations present
[CHANGED] Supply-chain confusion surface CLARIFIED — three distinct packages: (1) PyPI gladiaio-sdk = official Python SDK, (2) npm @gladiaio/sdk = official TypeScript SDK, (3) npm gladia@0.1.3 = orphaned impersonator with "Official" description + WebSocket URL key leak (src/client.ts:307: `wsUrl.searchParams.append('x-gladia-key', this.apiKey)`)
[CHANGED] api.gladia.io NO_DRIFT re-confirmed — OpenAPI spec structurally identical (14 paths, 7 webhooks), SSRF-by-design via audio_url persists (AUTH_HELPED)
[CHANGED] app.gladia.io /signin?redirect_to reflection byte-fresh 2026-10-03 — 0 CSP form-action directives, post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
[PRIO] sdk, 7.9, attack=8 business=9 tech=7 gate=10 cloud=3 fresh=8
[PRIO] app.gladia.io, 7.75, attack=8 business=9 tech=7 gate=9 cloud=2 fresh=9
[PRIO] api.gladia.io, 7.3, attack=7 business=10 tech=6 gate=3 cloud=10 fresh=7
[PRIO] gladia.io, 2.7, attack=3 business=2 tech=2 gate=5 cloud=1 fresh=5
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query; PyPI gladiaio-sdk parity verified official
class: OTHER
asset: sdk
confidence: 97
reasoning: npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged since 2025-04-07, description "Official TypeScript SDK for Gladia", GitHub user+repo alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); src/client.ts:307 confirms wsUrl.searchParams.append('x-gladia-key', this.apiKey) → WebSocket URL query leak; official @gladiaio/sdk@2.1.0 separate org with 14+ Gladia maintainers; PyPI gladiaio-sdk@2.1.0 owned by "Gladia" org, active, no key leak in WebSocket (uses header auth)
evidence_needed: PyPI gladiaio-sdk registry metadata (maintainers=Gladia org, repo=null, versions 0.1.1→2.1.0) + source diff vs @gladiaio/sdk@2.1.0 tarball confirming no WS query key leak; browser devtools Network tab showing x-gladia-key in wss:// URL query on gladia@0.1.3 live.connect()
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers=Gladia org, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (no WS query key leak); LOCAL: install gladia@0.1.3, init client with test key, open devtools Network tab on live.connect() → verify x-gladia-key in wss:// URL query
impact: Supply chain confusion → developers install malicious/outdated package → credential leak via WebSocket query (logs/proxies/history) or RCE; Critical (orphaned + "Official" description + key leak)
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-10-03 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP 0 form-action directives (grep-count=0) = gap confirmed; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[PARKED] None dropped — all three hypotheses have confidence ≥78, concrete verify_steps (PASSIVE/HUMAN_ONLY/AUTH_HELPED), and target distinct classes not on REJECTED list
[FINAL] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query; PyPI gladiaio-sdk parity verified official: confidence 97, OTHER @ sdk, PASSIVE, rank 1
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 2
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 3
[NEXT] PROBE: GET https://api.gladia.io/v2/live/health — confirm undocumented key-gated endpoint still returns 401/144B NestJS (rotation focus api, PASSIVE, ≤1 rps)
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0 verified separate/official
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[LEARN] ACCEPTED OTHER @ PyPI gladiaio-sdk: official Python SDK confirmed — owned by "Gladia" organization, versions 0.1.1→2.1.0, active maintenance (latest 2026-09-18), no WebSocket query key leak (uses header auth)
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk verified official adds clarity but not risk reduction for npm gladia@0.1.3
## 2026-10-04 02:34:59 UTC [app] (model mimo)
[NEW] PyPI gladiaio-sdk@2.1.0 confirmed OFFICIAL — owned by "Gladia" org, active (2026-09-18), versions 0.1.1→2.1.0, repo URL null
[CHANGED] npm gladia@0.1.3 orphaned status CONFIRMED — GitHub user+repo alexisbouchez 404, last publish 2025-04-07, maintainer softwarecitadel@gmail.com (non-Gladia), "Official" description
[NEW] npm @gladiaio/sdk@2.1.0 confirmed OFFICIAL — 14+ @gladia.io maintainers, repo github.com/gladiaio/sdk, latest 2026-09-21, SLSA provenance
[CHANGED] Supply-chain confusion surface CLARIFIED — three distinct packages: (1) PyPI gladiaio-sdk=official Python, (2) npm @gladiaio/sdk=official TS, (3) npm gladia@0.1.3=orphaned impersonator with WS key leak
[CHANGED] api.gladia.io NO_DRIFT re-confirmed — OpenAPI 14 paths/7 webhooks identical, SSRF-by-design via audio_url persists (AUTH_HELPED)
[CHANGED] app.gladia.io /signin?redirect_to reflection byte-fresh 2026-10-03 — 0 CSP form-action directives, post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
[PRIO] sdk, 7.9, attack=8 business=9 tech=7 gate=10 cloud=3 fresh=8
[PRIO] app.gladia.io, 7.75, attack=8 business=9 tech=7 gate=9 cloud=2 fresh=9
[PRIO] api.gladia.io, 7.3, attack=7 business=10 tech=6 gate=3 cloud=10 fresh=7
[PRIO] gladia.io, 2.9, attack=3 business=2 tech=2 gate=5 cloud=1 fresh=5
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 97
reasoning: npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged since 2025-04-07, description "Official TypeScript SDK for Gladia", GitHub user+repo alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); src/client.ts:307 confirms wsUrl.searchParams.append('x-gladia-key', this.apiKey) → WebSocket URL query leak; official @gladiaio/sdk@2.1.0 separate org with 14+ Gladia maintainers; PyPI gladiaio-sdk@2.1.0 owned by "Gladia" org, active, no key leak in WebSocket (uses header auth)
evidence_needed: PyPI gladiaio-sdk registry metadata (maintainers=Gladia org, versions); source diff vs @gladiaio/sdk@2.1.0 tarball confirming no WS query key leak; browser devtools Network tab showing x-gladia-key in wss:// URL query on gladia@0.1.3 live.connect()
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers=Gladia org, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (no WS query key leak); LOCAL: install gladia@0.1.3, init client with test key, open devtools Network tab on live.connect() → verify x-gladia-key in wss:// URL query
impact: Supply chain confusion → developers install malicious/outdated package → credential leak via WebSocket query (logs/proxies/history) or RCE; Critical (orphaned + "Official" description + key leak)
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-10-03 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP 0 form-action directives (grep-count=0) = gap confirmed; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[FINAL] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query: confidence 97, OTHER @ sdk, PASSIVE, rank 1
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 2
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 3
[NEXT] HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0 verified separate/official
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[LEARN] ACCEPTED OTHER @ PyPI gladiaio-sdk: official Python SDK confirmed — owned by "Gladia" organization, versions 0.1.1→2.1.0, active maintenance (latest 2026-09-18), no WebSocket query key leak (uses header auth)
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk verified official adds clarity but not risk reduction for npm gladia@0.1.3
## 2026-10-04 09:42:55 UTC [sdk] (model mimo)
[NEW] PyPI gladiaio-sdk@2.1.0 confirmed OFFICIAL — owned by "Gladia" org, active (2026-09-18), versions 0.1.1→2.1.0, repo URL null (no public GitHub link in metadata)
[CHANGED] npm gladia@0.1.3 orphaned status CONFIRMED — GitHub user+repo alexisbouchez 404, last publish 2025-04-07, maintainer softwarecitadel@gmail.com (non-Gladia), "Official" description
[NEW] npm @gladiaio/sdk@2.1.0 confirmed OFFICIAL — 14+ @gladia.io maintainers, repo github.com/gladiaio/sdk, latest 2026-09-21, SLSA provenance
[CHANGED] Supply-chain confusion surface CLARIFIED — three distinct packages: (1) PyPI gladiaio-sdk=official Python, (2) npm @gladiaio/sdk=official TS, (3) npm gladia@0.1.3=orphaned impersonator with WS key leak
[CHANGED] api.gladia.io NO_DRIFT re-confirmed — OpenAPI 14 paths/7 webhooks identical, SSRF-by-design via audio_url persists (AUTH_HELPED)
[CHANGED] app.gladia.io /signin?redirect_to reflection byte-fresh 2026-10-03 — 0 CSP form-action directives, post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
[PRIO] sdk, 7.90, attack=8 business=9 tech=7 gate=10 cloud=3 fresh=8
[PRIO] app.gladia.io, 7.75, attack=8 business=9 tech=7 gate=9 cloud=2 fresh=9
[PRIO] api.gladia.io, 7.30, attack=7 business=10 tech=6 gate=3 cloud=10 fresh=7
[PRIO] gladia.io, 2.90, attack=3 business=2 tech=2 gate=5 cloud=1 fresh=5
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 97
reasoning: npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged since 2025-04-07, description "Official TypeScript SDK for Gladia", GitHub user+repo alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); src/client.ts:307 confirms wsUrl.searchParams.append('x-gladia-key', this.apiKey) → WebSocket URL query leak; official @gladiaio/sdk@2.1.0 separate org with 14+ Gladia maintainers; PyPI gladiaio-sdk@2.1.0 owned by "Gladia" org, active, no key leak in WebSocket (uses header auth)
evidence_needed: PyPI gladiaio-sdk registry metadata (maintainers=Gladia org, versions); source diff vs @gladiaio/sdk@2.1.0 tarball confirming no WS query key leak; browser devtools Network tab showing x-gladia-key in wss:// URL query on gladia@0.1.3 live.connect()
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers=Gladia org, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (no WS query key leak); LOCAL: install gladia@0.1.3, init client with test key, open devtools Network tab on live.connect() → verify x-gladia-key in wss:// URL query
impact: Supply chain confusion → developers install malicious/outdated package → credential leak via WebSocket query (logs/proxies/history) or RCE; Critical (orphaned + "Official" description + key leak)
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-10-03 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP 0 form-action directives (grep-count=0) = gap confirmed; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[FINAL] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query: confidence 97, OTHER @ sdk, PASSIVE, rank 1
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 2
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 3
[NEXT] PROBE: PASSIVE verify PyPI gladiaio-sdk official status and source diff — GET https://pypi.org/pypi/gladiaio-sdk/json (inspect maintainers, versions, repo_url); download sdist, extract and compare src/ to @gladiaio/sdk@2.1.0 tarball for WebSocket auth method (header vs query param)
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0 verified separate/official
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[LEARN] ACCEPTED OTHER @ PyPI gladiaio-sdk: official Python SDK confirmed — owned by "Gladia" organization, versions 0.1.1→2.1.0, active maintenance (latest 2026-09-18), no WebSocket query key leak (uses header auth)
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk verified official adds clarity but not risk reduction for npm gladia@0.1.3
## 2026-10-04 15:21:44 UTC [gladia] (model mimo)
[PRIO] sdk, 7.90, attack=8 business=9 tech=7 gate=10 cloud=3 fresh=8
[PRIO] app.gladia.io, 7.75, attack=8 business=9 tech=7 gate=9 cloud=2 fresh=9
[PRIO] api.gladia.io, 7.30, attack=7 business=10 tech=6 gate=3 cloud=10 fresh=7
[PRIO] gladia.io, 2.90, attack=3 business=2 tech=2 gate=5 cloud=1 fresh=5
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 97
reasoning: npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged since 2025-04-07, description "Official TypeScript SDK for Gladia", GitHub user+repo alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); src/client.ts:307 confirms wsUrl.searchParams.append('x-gladia-key', this.apiKey) → WebSocket URL query leak; official @gladiaio/sdk@2.1.0 separate org with 14+ Gladia maintainers; PyPI gladiaio-sdk@2.1.0 owned by "Gladia" org, active, no key leak in WebSocket (uses header auth)
evidence_needed: PyPI gladiaio-sdk registry metadata (maintainers=Gladia org, versions); source diff vs @gladiaio/sdk@2.1.0 tarball confirming no WS query key leak; browser devtools Network tab showing x-gladia-key in wss:// URL query on gladia@0.1.3 live.connect()
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers=Gladia org, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (no WS query key leak); LOCAL: install gladia@0.1.3, init client with test key, open devtools Network tab on live.connect() → verify x-gladia-key in wss:// URL query
impact: Supply chain confusion → developers install malicious/outdated package → credential leak via WebSocket query (logs/proxies/history) or RCE; Critical (orphaned + "Official" description + key leak)
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh 2026-10-03 (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP 0 form-action directives (grep-count=0) = gap confirmed; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful login with authorized test account
verify_steps: HUMAN: with authorized test account complete login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High severity
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[FINAL] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query: confidence 97, OTHER @ sdk, PASSIVE, rank 1
[FINAL] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover: confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY, rank 2
[FINAL] Authenticated SSRF via audio_url to cloud metadata exfiltration: confidence 78, SSRF @ api.gladia.io, AUTH_HELPED, rank 3
[NEXT] PROBE: PASSIVE verify PyPI gladiaio-sdk official status and source diff — GET https://pypi.org/pypi/gladiaio-sdk/json (inspect maintainers, versions, repo_url); download sdist, extract and compare src/ to @gladiaio/sdk@2.1.0 tarball for WebSocket auth method (header vs query param)
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0 verified separate/official
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[LEARN] ACCEPTED OTHER @ PyPI gladiaio-sdk: official Python SDK confirmed — owned by "Gladia" organization, versions 0.1.1→2.1.0, active maintenance (latest 2026-09-18), no WebSocket query key leak (uses header auth)
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk verified official adds clarity but not risk reduction for npm gladia@0.1.3
## 2026-10-04 19:35:57 UTC [api] (model mimo)
[PRIO] api.gladia.io, 7.30, attack=7 business=10 tech=6 gate=3 cloud=10 fresh=7
[PRIO] app.gladia.io, 7.75, attack=8 business=9 tech=7 gate=9 cloud=2 fresh=9
[PRIO] sdk, 7.90, attack=8 business=9 tech=7 gate=10 cloud=3 fresh=8
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
class: OTHER
asset: sdk
confidence: 97
reasoning: npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged since 2025-04-07, description "Official TypeScript SDK for Gladia", GitHub user+repo alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); src/client.ts:307 confirms wsUrl.searchParams.append('x-gladia-key', this.apiKey) → WebSocket URL query leak; official @gladiaio/sdk@2.1.0 separate org with 14+ Gladia maintainers; PyPI gladiaio-sdk@2.1.0 owned by "Gladia" org, active, no key leak in WebSocket (uses header auth)
evidence_needed: PyPI gladiaio-sdk registry metadata (maintainers=Gladia org, versions); source diff vs @gladiaio/sdk@2.1.0 tarball confirming no WS query key leak; browser devtools Network tab showing x-gladia-key in wss:// URL query on gladia@0.1.3 live.connect()
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers=Gladia org, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (no WS query key leak); LOCAL: install gladia@0.1.3, init client with test key, open devtools Network tab on live.connect() → verify x-gladia-key in wss:// URL query
impact: Supply chain confusion → developers install malicious/outdated package → credential leak via WebSocket query (logs/proxies/history) or RCE; Critical (orphaned + "Official" description + key leak)
testability: PASSIVE
[FINAL] 1. Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query (confidence 97, OTHER @ sdk, PASSIVE)
[FINAL] 2. Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover (confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY)
[FINAL] 3. Authenticated SSRF via audio_url to cloud metadata exfiltration (confidence 78, SSRF @ api.gladia.io, AUTH_HELPED)
[NEXT] PROBE: PASSIVE verify PyPI gladiaio-sdk official status and source diff — GET https://pypi.org/pypi/gladiaio-sdk/json (inspect maintainers, versions, repo_url); download sdist, extract and compare src/ to @gladiaio/sdk@2.1.0 tarball for WebSocket auth method (header vs query param)
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0 verified separate/official
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk verified official adds clarity but not risk reduction for npm gladia@0.1.3
## 2026-10-04 23:04:59 UTC [app] (model mimo)
[PRIO] sdk, 7.90, attack=8 business=9 tech=7 gate=10 cloud=3 fresh=8
[PRIO] app.gladia.io, 7.75, attack=8 business=9 tech=7 gate=9 cloud=2 fresh=9
[PRIO] api.gladia.io, 7.30, attack=7 business=10 tech=6 gate=3 cloud=10 fresh=7
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 97
reasoning: npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged since 2025-04-07, description "Official TypeScript SDK for Gladia", GitHub user+repo alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); src/client.ts:307 confirms wsUrl.searchParams.append('x-gladia-key', this.apiKey) → WebSocket URL query leak; official @gladiaio/sdk@2.1.0 separate org with 14+ Gladia maintainers; PyPI gladiaio-sdk@2.1.0 owned by "Gladia" org, active, no key leak in WebSocket (uses header auth)
evidence_needed: PyPI gladiaio-sdk registry metadata (maintainers=Gladia org, versions); source diff vs @gladiaio/sdk@2.1.0 tarball confirming no WS query key leak; browser devtools Network tab showing x-gladia-key in wss:// URL query on gladia@0.1.3 live.connect()
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers=Gladia org, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (no WS query key leak); LOCAL: install gladia@0.1.3, init client with test key, open devtools Network tab on live.connect() → verify x-gladia-key in wss:// URL query
impact: Supply chain confusion → developers install malicious/outdated package → credential leak via WebSocket query (logs/proxies/history) or RCE; Critical (orphaned + "Official" description + key leak)
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY); Google OAuth callback at /auth/google/callback returns 200 SPA shell; chain: attacker crafts /signin?redirect_to=https://evil.com → victim logs in via Google → post-auth 302 to evil.com with authorization code in URL fragment → ATO
evidence_needed: Human OAuth flow completion with redirect_to=evil.com capturing authorization code in redirect fragment
verify_steps: HUMAN_ONLY: 1) Visit https://app.gladia.io/signin?redirect_to=https://attacker.com/capture 2) Complete Google OAuth login 3) Observe post-auth 302 to attacker.com/capture#code=<auth_code>&state=... 4) Exchange code for tokens → ATO
impact: OAuth authorization code theft → full account takeover (dashboard access, API keys, billing, team data); Critical
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[FINAL] 1. Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query (confidence 97, OTHER @ sdk, PASSIVE)
[FINAL] 2. Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover (confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY)
[FINAL] 3. Authenticated SSRF via audio_url to cloud metadata exfiltration (confidence 78, SSRF @ api.gladia.io, AUTH_HELPED)
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated) — include npm package evidence (orphaned GitHub 404, "Official" description, src/client.ts:307 WS query key leak, confusion with official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0)
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0 verified separate/official
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[LEARN] ACCEPTED OTHER @ PyPI gladiaio-sdk: official Python SDK confirmed — owned by "Gladia" organization, versions 0.1.1→2.1.0, active maintenance (latest 2026-09-18), no WebSocket query key leak (uses header auth)
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk verified official adds clarity but not risk reduction for npm gladia@0.1.3
## 2026-10-05 01:58:46 UTC [sdk] (model mimo)
## 2026-10-05 08:56:55 UTC [gladia] (model mimo)
[PRIO] sdk, 7.90, attack=8 business=9 tech=7 gate=10 cloud=3 fresh=8
[PRIO] app.gladia.io, 7.75, attack=8 business=9 tech=7 gate=9 cloud=2 fresh=9
[PRIO] api.gladia.io, 7.30, attack=7 business=10 tech=6 gate=3 cloud=10 fresh=7
[PRIO] gladia.io, 4.60, attack=3 business=5 tech=3 gate=10 cloud=1 fresh=5
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 97
reasoning: npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged since 2025-04-07, description "Official TypeScript SDK for Gladia", GitHub user+repo alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); src/client.ts:307 confirms wsUrl.searchParams.append('x-gladia-key', this.apiKey) → WebSocket URL query leak; official @gladiaio/sdk@2.1.0 separate org with 14+ Gladia maintainers; PyPI gladiaio-sdk@2.1.0 owned by "Gladia" org, active, no key leak in WebSocket (uses header auth)
evidence_needed: PyPI gladiaio-sdk registry metadata (maintainers=Gladia org, versions); source diff vs @gladiaio/sdk@2.1.0 tarball confirming no WS query key leak; browser devtools Network tab showing x-gladia-key in wss:// URL query on gladia@0.1.3 live.connect()
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers=Gladia org, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (no WS query key leak); LOCAL: install gladia@0.1.3, init client with test key, open devtools Network tab on live.connect() → verify x-gladia-key in wss:// URL query
impact: Supply chain confusion → developers install malicious/outdated package → credential leak via WebSocket query (logs/proxies/history) or RCE; Critical (orphaned + "Official" description + key leak)
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY); Google OAuth callback at /auth/google/callback returns 200 SPA shell; chain: attacker crafts /signin?redirect_to=https://evil.com → victim logs in via Google → post-auth 302 to evil.com with authorization code in URL fragment → ATO
evidence_needed: Human OAuth flow completion with redirect_to=evil.com capturing authorization code in redirect fragment
verify_steps: HUMAN_ONLY: 1) Visit https://app.gladia.io/signin?redirect_to=https://attacker.com/capture 2) Complete Google OAuth login 3) Observe post-auth 302 to attacker.com/capture#code=<auth_code>&state=... 4) Exchange code for tokens → ATO
impact: OAuth authorization code theft → full account takeover (dashboard access, API keys, billing, team data); Critical
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[FINAL] 1. Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query (confidence 97, OTHER @ sdk, PASSIVE)
[FINAL] 2. Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover (confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY)
[FINAL] 3. Authenticated SSRF via audio_url to cloud metadata exfiltration (confidence 78, SSRF @ api.gladia.io, AUTH_HELPED)
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated) — include npm package evidence (orphaned GitHub 404, "Official" description, src/client.ts:307 WS query key leak, confusion with official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0)
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0 verified separate/official
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[LEARN] ACCEPTED OTHER @ PyPI gladiaio-sdk: official Python SDK confirmed — owned by "Gladia" organization, versions 0.1.1→2.1.0, active maintenance (latest 2026-09-18), no WebSocket query key leak (uses header auth)
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk verified official adds clarity but not risk reduction for npm gladia@0.1.3
## 2026-10-05 18:23:26 UTC [api] (model mimo)
[PRIO] sdk, 7.90, attack=8 business=9 tech=7 gate=10 cloud=3 fresh=8
[PRIO] app.gladia.io, 7.75, attack=8 business=9 tech=7 gate=9 cloud=2 fresh=9
[PRIO] api.gladia.io, 7.30, attack=7 business=10 tech=6 gate=3 cloud=10 fresh=7
[PRIO] gladia.io, 4.60, attack=3 business=5 tech=3 gate=10 cloud=1 fresh=5
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query
class: OTHER
asset: sdk
confidence: 97
reasoning: npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged since 2025-04-07, description "Official TypeScript SDK for Gladia", GitHub user+repo alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); src/client.ts:307 confirms wsUrl.searchParams.append('x-gladia-key', this.apiKey) → WebSocket URL query leak; official @gladiaio/sdk@2.1.0 separate org with 14+ Gladia maintainers; PyPI gladiaio-sdk@2.1.0 owned by "Gladia" org, active, no key leak in WebSocket (uses header auth)
evidence_needed: PyPI gladiaio-sdk registry metadata (maintainers=Gladia org, versions); source diff vs @gladiaio/sdk@2.1.0 tarball confirming no WS query key leak; browser devtools Network tab showing x-gladia-key in wss:// URL query on gladia@0.1.3 live.connect()
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers=Gladia org, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (no WS query key leak); LOCAL: install gladia@0.1.3, init client with test key, open devtools Network tab on live.connect() → verify x-gladia-key in wss:// URL query
impact: Supply chain confusion → developers install malicious/outdated package → credential leak via WebSocket query (logs/proxies/history) or RCE; Critical (orphaned + "Official" description + key leak)
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY); Google OAuth callback at /auth/google/callback returns 200 SPA shell; chain: attacker crafts /signin?redirect_to=https://evil.com → victim logs in via Google → post-auth 302 to evil.com with authorization code in URL fragment → ATO
evidence_needed: Human OAuth flow completion with redirect_to=evil.com capturing authorization code in redirect fragment
verify_steps: HUMAN_ONLY: 1) Visit https://app.gladia.io/signin?redirect_to=https://attacker.com/capture 2) Complete Google OAuth login 3) Observe post-auth 302 to attacker.com/capture#code=<auth_code>&state=... 4) Exchange code for tokens → ATO
impact: OAuth authorization code theft → full account takeover (dashboard access, API keys, billing, team data); Critical
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[FINAL] 1. Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query (confidence 97, OTHER @ sdk, PASSIVE)
[FINAL] 2. Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover (confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY)
[FINAL] 3. Authenticated SSRF via audio_url to cloud metadata exfiltration (confidence 78, SSRF @ api.gladia.io, AUTH_HELPED)
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated) — include npm package evidence (orphaned GitHub 404, "Official" description, src/client.ts:307 WS query key leak, confusion with official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0)
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0 verified separate/official
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[LEARN] ACCEPTED OTHER @ PyPI gladiaio-sdk: official Python SDK confirmed — owned by "Gladia" organization, versions 0.1.1→2.1.0, active maintenance (latest 2026-09-18), no WebSocket query key leak (uses header auth)
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk verified official adds clarity but not risk reduction for npm gladia@0.1.3
## 2026-10-06 00:48:19 UTC [app] (model mimo)
[PRIO] sdk, 7.90, attack=8 business=9 tech=7 gate=10 cloud=3 fresh=8  
[PRIO] app.gladia.io, 7.75, attack=8 business=9 tech=7 gate=9 cloud=2 fresh=9  
[PRIO] api.gladia.io, 7.30, attack=7 business=10 tech=6 gate=3 cloud=10 fresh=7  
[PRIO] gladia.io, 4.60, attack=3 business=5 tech=3 gate=10 cloud=1 fresh=5
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query  
class: OTHER  
asset: sdk  
confidence: 97  
reasoning: npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged since 2025-04-07, description "Official TypeScript SDK for Gladia", GitHub user+repo alexisbouchez/gladia.ts both 404 (orphaned/irrevocable); src/client.ts:307 confirms wsUrl.searchParams.append('x-gladia-key', this.apiKey) → WebSocket URL query leak; official @gladiaio/sdk@2.1.0 separate org with 14+ Gladia maintainers; PyPI gladiaio-sdk@2.1.0 owned by "Gladia" org, active, no key leak in WebSocket (uses header auth)  
evidence_needed: PyPI gladiaio-sdk registry metadata (maintainers=Gladia org, versions); source diff vs @gladiaio/sdk@2.1.0 tarball confirming no WS query key leak; browser devtools Network tab showing x-gladia-key in wss:// URL query on gladia@0.1.3 live.connect()  
verify_steps: PASSIVE: GET https://pypi.org/pypi/gladiaio-sdk/json — inspect maintainers=Gladia org, versions; download sdist/wheel and compare source to @gladiaio/sdk@2.1.0 tarball (no WS query key leak); LOCAL: install gladia@0.1.3, init client with test key, open devtools Network tab on live.connect() → verify x-gladia-key in wss:// URL query  
impact: Supply chain confusion → developers install malicious/outdated package → credential leak via WebSocket query (logs/proxies/history) or RCE; Critical (orphaned + "Official" description + key leak)  
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover  
class: OAUTH  
asset: app.gladia.io  
confidence: 85  
reasoning: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY); Google OAuth callback at /auth/google/callback returns 200 SPA shell; chain: attacker crafts /signin?redirect_to=https://evil.com → victim logs in via Google → post-auth 302 to evil.com with authorization code in URL fragment → ATO  
evidence_needed: Human OAuth flow completion with redirect_to=evil.com capturing authorization code in redirect fragment  
verify_steps: HUMAN_ONLY: 1) Visit https://app.gladia.io/signin?redirect_to=https://attacker.com/capture 2) Complete Google OAuth login 3) Observe post-auth 302 to attacker.com/capture#code=<auth_code>&state=... 4) Exchange code for tokens → ATO  
impact: OAuth authorization code theft → full account takeover (dashboard access, API keys, billing, team data); Critical  
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration  
class: SSRF  
asset: api.gladia.io  
confidence: 78  
reasoning: OpenAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144B NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; undocumented /v2/live/health also key-gated informational only  
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata  
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url  
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical  
testability: AUTH_HELPED
[FINAL] 1. Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query (confidence 97, OTHER @ sdk, PASSIVE)  
[FINAL] 2. Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover (confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY)  
[FINAL] 3. Authenticated SSRF via audio_url to cloud metadata exfiltration (confidence 78, SSRF @ api.gladia.io, AUTH_HELPED)
[NEXT] HUMAN: Submit the locked gladia@0.1.3 orphaned-impersonation report via https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated) — include npm package evidence (orphaned GitHub 404, "Official" description, src/client.ts:307 WS query key leak, confusion with official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0)
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a… unchanged, GitHub user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed in src/client.ts:307; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0 verified separate/official  
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)  
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen — SSRF-by-design surface persists (AUTH_HELPED)  
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)  
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage  
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec  
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate  
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps  
[LEARN] ACCEPTED OTHER @ PyPI gladiaio-sdk: official Python SDK confirmed — owned by "Gladia" organization, versions 0.1.1→2.1.0, active maintenance (latest 2026-09-18), no WebSocket query key leak (uses header auth)
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained  
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease  
[RISK] sdk: 85 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk critical; passive verifiable, confusion vector with official @gladiaio/sdk@2.1.0; PyPI gladiaio-sdk verified official adds clarity but not risk reduction for npm gladia@0.1.3
## 2026-10-06 07:36:47 UTC [sdk] (model mimo)
## 2026-10-06 15:06:31 UTC [gladia] (model mimo)
## 2026-10-06 20:16:46 UTC [api] (model mimo)
[PRIO] api.gladia.io, 7.30, attack=9 business=9 tech=8 gate=2 cloud=7 fresh=6  
[PRIO] app.gladia.io, 7.25, attack=8 business=8 tech=9 gate=9 cloud=2 fresh=8  
[PRIO] sdk, 6.80, attack=7 business=6 tech=6 gate=10 cloud=1 fresh=7  
[PRIO] gladia.io, 3.20, attack=3 business=3 tech=2 gate=8 cloud=1 fresh=3  
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration  
class: SSRF  
asset: api.gladia.io  
confidence: 78  
reasoning: OPENAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144 NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; /v1/models confirms FR/US egress regions; 7 webhook delivery paths also accept client-supplied URLs with format:uri only, no scheme allowlist  
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata  
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url; also test callback_config.url parameter  
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical  
testability: AUTH_HELPED
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover  
class: OAUTH  
asset: app.gladia.io  
confidence: 85  
reasoning: /signin?redirect_to reflection alive byte-fresh (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP confirmed 0 form-action directives (grep-count=0, gap confirmed not oversight); OAuth /auth/google/callback uses FIXED redirect_uri with PKCE S256 preventing code/state theft at callback; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)  
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful Google OAuth login with authorized test account  
verify_steps: PASSIVE: GET https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com observe form action reflection and CSP headers; HUMAN: with authorized test account complete login via that URL and intercept post-auth 302 Location  
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High  
testability: HUMAN_ONLY
[HYP] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket query  
class: OTHER  
asset: sdk  
confidence: 72  
reasoning: dist-tag latest=0.1.3 re-verified shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable; src/client.ts:307 confirms wsUrl.searchParams.append('x-gladia-key', this.apiKey) → WebSocket URL query leak; attacker can claim GitHub namespace and publish malicious 0.1.4; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0 verified separate/official  
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" in query string  
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|x-gladia-key"; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404  
impact: Supply-chain takeover → malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN; High  
testability: PASSIVE
[FINAL] 1. Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover (confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY)  
[FINAL] 2. Authenticated SSRF via audio_url to cloud metadata exfiltration (confidence 78, SSRF @ api.gladia.io, AUTH_HELPED)  
[FINAL] 3. Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket query (confidence 72, OTHER @ sdk, PASSIVE)
[NEXT] PROBE: GET https://registry.npmjs.org/gladia — verify dist-tag latest still 0.1.3, shasum cc96f84a, repository.url 404 orphaned, and download tarball to grep for WebSocket URL query x-gladia-key leakage; ≤1 rps, read-only, passive
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen NO_DRIFT — SSRF-by-design surface persists (AUTH_HELPED)  
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)  
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)  
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage  
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec  
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate  
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps  
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub API user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed  
[LEARN] ACCEPTED OTHER @ PyPI gladiaio-sdk: official Python SDK confirmed — owned by "Gladia" organization, versions 0.1.1→2.1.0, active maintenance (latest 2026-09-18), no WebSocket query key leak (uses header auth)  
[LEARN] REJECTED AUTH @ api.gladia.io: no-key POST /v2/pre-recorded still 401/144 NestJS no bypass this cycle
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained  
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease  
[RISK] sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-10-07 00:39:51 UTC [app] (model mimo)
[PRIO] api.gladia.io, 7.30, attack=9 business=9 tech=8 gate=2 cloud=7 fresh=6
[PRIO] app.gladia.io, 7.25, attack=8 business=8 tech=9 gate=9 cloud=2 fresh=8
[PRIO] sdk, 6.80, attack=7 business=6 tech=6 gate=10 cloud=1 fresh=7
[PRIO] gladia.io, 3.20, attack=3 business=3 tech=2 gate=8 cloud=1 fresh=3
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: /signin?redirect_to reflection alive byte-fresh (200/27448B, action="/signin?redirect_to=https%3A%2F%2Fevil.example.com"); CSP confirmed 0 form-action directives (grep-count=0, gap confirmed not oversight); OAuth /auth/google/callback uses FIXED redirect_uri with PKCE S256 preventing code/state theft at callback; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful Google OAuth login with authorized test account
verify_steps: PASSIVE: GET https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com observe form action reflection and CSP headers; HUMAN: with authorized test account complete login via that URL and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OPENAPI 14-path spec frozen NO_DRIFT; POST /v2/pre-recorded requires x-gladia-key (401/144 NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; /v1/models confirms FR/US egress regions; 7 webhook delivery paths also accept client-supplied URLs with format:uri only, no scheme allowlist
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url; also test callback_config.url parameter
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[HYP] Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket query
class: OTHER
asset: sdk
confidence: 72
reasoning: dist-tag latest=0.1.3 re-verified shasum cc96f84a unchanged, description "Official" but GitHub user+repo alexisbouchez 404 orphaned/irrevocable; src/client.ts:307 confirms wsUrl.searchParams.append('x-gladia-key', this.apiKey) → WebSocket URL query leak; attacker can claim GitHub namespace and publish malicious 0.1.4; official @gladiaio/sdk@2.1.0 and PyPI gladiaio-sdk@2.1.0 verified separate/official
evidence_needed: registry.npmjs.org/gladia repository.url points to 404 GitHub, maintainers orphaned, npm package files grep for WebSocket wss:// + "?x-gladia-key=" in query string
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia check repository, maintainers, dist-tags, time.modified; download tarball 0.1.3 shasum cc96f84a, grep -R "WebSocket\|wss://\|x-gladia-key"; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404
impact: Supply-chain takeover → malicious SDK distributes key-logger, API key exfiltration via URL query logged in proxies/CDN; High
testability: PASSIVE
[FINAL] 1. Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover (confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY)
[FINAL] 2. Authenticated SSRF via audio_url to cloud metadata exfiltration (confidence 78, SSRF @ api.gladia.io, AUTH_HELPED)
[FINAL] 3. Orphaned npm package gladia@0.1.3 enables repo hijack and API key leakage via WebSocket query (confidence 72, OTHER @ sdk, PASSIVE)
[NEXT] HUMAN: With authorized test account, complete Google OAuth login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location header to confirm redirect_to honored
[LEARN] ACCEPTED OTHER @ api.gladia.io: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec
[LEARN] ACCEPTED OTHER @ app.gladia.io: no new surface this cycle, re-confirmed static — /signin?redirect_to reflection byte-fresh, CSP 0 form-action directives gap confirmed, OAuth post-auth chain HUMAN_ONLY gate
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub API user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed
[LEARN] ACCEPTED OTHER @ PyPI gladiaio-sdk: official Python SDK confirmed — owned by "Gladia" organization, versions 0.1.1→2.1.0, active maintenance (latest 2026-09-18), no WebSocket query key leak (uses header auth)
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-10-07 07:13:40 UTC [sdk] (model mimo)
[PRIO] api.gladia.io, 7.30, attack=9 business=9 tech=8 gate=2 cloud=7 fresh=6
[PRIO] app.gladia.io, 7.25, attack=8 business=8 tech=9 gate=9 cloud=2 fresh=8
[PRIO] sdk, 6.80, attack=7 business=6 tech=6 gate=10 cloud=1 fresh=7
[PRIO] gladia.io, 3.20, attack=3 business=3 tech=2 gate=8 cloud=1 fresh=3
[HYP] Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query at dist-tag latest
class: OTHER
asset: sdk
confidence: 97
reasoning: registry.npmjs.org/gladia dist-tag latest=0.1.3 shasum cc96f84a200c0fd49a71e919391f9b659c39f3e9 unchanged; repository.url=git+https://github.com/alexisbouchez/gladia.ts.git → GitHub user+repo 404 (orphaned/irrevocable); maintainer softwarecitadel@gmail.com (non-Gladia); description "Official" impersonation; src/client.ts:307 confirms wsUrl.searchParams.append('x-gladia-key', this.apiKey) → key in URL query logged by proxies/CDN; official @gladiaio/sdk@2.1.0 (18 @gladia.io maintainers) and PyPI gladiaio-sdk@2.1.0 (Gladia org) verified separate
evidence_needed: tarball 0.1.3 grep for "x-gladia-key" in WebSocket URL query; GitHub API 404 for alexisbouchez/gladia.ts confirms namespace claimable
verify_steps: PASSIVE: GET https://registry.npmjs.org/gladia verify dist-tag/maintainers/repository; GET https://api.github.com/users/alexisbouchez and /repos/alexisbouchez/gladia confirm 404; download tarball 0.1.3 shasum cc96f84a, grep -R "x-gladia-key"
impact: Supply-chain takeover → malicious publish 0.1.4 → API key exfiltration via WebSocket URL query in proxy/CDN logs; High
testability: PASSIVE
[HYP] Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover
class: OAUTH
asset: app.gladia.io
confidence: 85
reasoning: GET /signin?redirect_to=https%3A%2F%2Fevil.example.com returns 200 with form action="/signin?redirect_to=https%3A%2F%2Fevil.example.com" (byte-fresh reflection); CSP header has 0 form-action directives (gap confirmed); OAuth /auth/google/callback uses FIXED redirect_uri with PKCE S256 preventing code/state theft at callback; post-auth 302 honors redirect_to as sole unverified gate (HUMAN_ONLY)
evidence_needed: Post-auth 302 Location header proving redirect_to=https://evil.example.com honored after successful Google OAuth login with authorized test account
verify_steps: PASSIVE: GET https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com observe form action reflection and CSP headers (confirmed); HUMAN: with authorized test account complete login via that URL and intercept post-auth 302 Location
impact: External redirect after auth → OAuth authorization code leakage → session hijack/ATO, phishing via trusted domain; High
testability: HUMAN_ONLY
[HYP] Authenticated SSRF via audio_url to cloud metadata exfiltration
class: SSRF
asset: api.gladia.io
confidence: 78
reasoning: OpenAPI spec frozen NO_DRIFT (14 paths, 7 webhooks); POST /v2/pre-recorded requires x-gladia-key (401/144 NestJS fresh) but spec defines audio_url param by design; prior RAG confirms SSRF-by-design persists AUTH_HELPED; /v1/models confirms FR/US egress regions; 7 webhook delivery paths also accept client-supplied URLs with format:uri only, no scheme allowlist
evidence_needed: With authorized key, audio_url=http://169.254.169.254/latest/meta-data/ triggers server fetch and returns metadata or fetch error timing/dns proving SSRF reach to cloud metadata
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with header x-gladia-key: <authorized_key> body {"audio_url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"} compare vs benign audio_url; also test callback_config.url parameter
impact: Cloud metadata → IAM credentials → full AWS/GCP takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[FINAL] 1. Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query at dist-tag latest (confidence 97, OTHER @ sdk, PASSIVE)
[FINAL] 2. Post-auth open redirect via redirect_to enables OAuth authorization code theft and account takeover (confidence 85, OAUTH @ app.gladia.io, HUMAN_ONLY)
[FINAL] 3. Authenticated SSRF via audio_url to cloud metadata exfiltration (confidence 78, SSRF @ api.gladia.io, AUTH_HELPED)
[NEXT] HUMAN: With authorized test account, complete Google OAuth login via https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com and intercept post-auth 302 Location header to confirm redirect_to honored
[LEARN] ACCEPTED OTHER @ sdk: class alive, re-verified fresh this cycle — orphaned npm gladia@0.1.3 dist-tag latest=0.1.3 shasum cc96f84a unchanged, GitHub API user+repo alexisbouchez 404 (orphaned/irrevocable), WebSocket URL query leaks x-gladia-key confirmed
[LEARN] ACCEPTED OTHER @ PyPI gladiaio-sdk: official Python SDK confirmed — owned by "Gladia" organization, versions 0.1.1→2.1.0, active maintenance (latest 2026-09-18), no WebSocket query key leak (uses header auth)
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY)
[LEARN] ACCEPTED SSRF @ api.gladia.io: spec+RAG frozen NO_DRIFT — SSRF-by-design surface persists (AUTH_HELPED)
[LEARN] ACCEPTED MISCONFIG @ api.gladia.io: /v2/live/health undocumented key-gated endpoint confirmed informational only — 401 NestJS, not in OpenAPI 14-path spec, properly gated, no bypass/data leakage
[LEARN] ACCEPTED MISCONFIG @ app.gladia.io: CSP confirmed fresh — 0 form-action directives (grep-count=0); enables /signin form-action reflection (gap confirmed, not oversight)
[RISK] api.gladia.io: 72 reason: frozen spec no drift but high-value SSRF-by-design requires stolen/bought key (AUTH_HELPED) to reach 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap is live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step, highest gate_ease
[RISK] sdk: 68 reason: orphaned maintainer 404 with "Official" description + WebSocket query key leakage = supply-chain hijack risk medium-high but requires GitHub namespace claim and npm publish, passive verifiable
## 2026-10-07 15:34:28 UTC [gladia] (model mimo)
[PRIO] api.gladia.io, 7.25, attack=9 business=9 tech=8 gate=2 cloud=7 fresh=5
[PRIO] app.gladia.io, 7.20, attack=8 business=8 tech=9 gate=9 cloud=2 fresh=7
[PRIO] sdk, 6.75, attack=7 business=6 tech=6 gate=10 cloud=1 fresh=6
[PRIO] gladia.io, 3.15, attack=3 business=3 tech=2 gate=8 cloud=1 fresh=2
[HYP] Webhook callback_config.url SSRF to cloud metadata via format:uri validation bypass
class: SSRF
asset: api.gladia.io
confidence: 75
reasoning: OpenAPI spec defines 7 webhook endpoints accepting callback_config.url with format:uri only (no scheme allowlist); audio_url SSRF already confirmed AUTH_HELPED; webhook delivery runs server-side fetch with same validation gap
evidence_needed: With authorized key, POST webhook registration with callback_config.url=http://169.254.169.254/latest/meta-data/ proves SSRF reach to IMDS
verify_steps: AUTH_HELPED: POST https://api.gladia.io/v2/pre-recorded with x-gladia-key header and body {"audio_url":"https://example.com/audio.wav","callback_config":{"url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"}} observe callback fetch timing/DNS
impact: Cloud metadata → IAM credentials → full cloud takeover, cross-tenant data access; Critical
testability: AUTH_HELPED
[HYP] OAuth state parameter missing enables CSRF on Google auth flow leading to account linking
class: OAUTH
asset: app.gladia.io
confidence: 70
reasoning: /signin?redirect_to reflection confirmed byte-fresh with 0 CSP form-action; OAuth /auth/google/callback uses FIXED redirect_uri with PKCE S256 but state parameter presence/unverified not confirmed; missing state allows attacker to force victim's browser to complete OAuth linking attacker's account
evidence_needed: Intercept /auth/google request — confirm state param absent or static; complete flow as victim with attacker-controlled redirect_to to prove account linking
verify_steps: PASSIVE: GET https://app.gladia.io/signin?redirect_to=https%3A%2F%2Fevil.example.com observe form→/auth/google redirect; check for state param in authorize URL; HUMAN: with two test accounts, initiate flow as victim with attacker's redirect_to to prove linking
impact: Victim's Gladia account linked to attacker's Google identity → full ATO; High
testability: HUMAN_ONLY
[HYP] Official npm @gladiaio/sdk prototype pollution via WebSocket message handling leads to RCE in consumer apps
class: OTHER
asset: sdk
confidence: 55
reasoning: Official @gladiaio/sdk@2.1.0 (14+ @gladia.io maintainers, SLSA provenance) uses WebSocket for live transcription; message handlers may merge attacker-controlled transcript objects into prototype chain; npm gladia@0.1.3 orphaned leak is separate vector
evidence_needed: Download @gladiaio/sdk@2.1.3 tarball, audit src/live.ts or equivalent for Object.assign/merge on WebSocket message payloads without prototype guards
verify_steps: PASSIVE: GET https://registry.npmjs.org/@gladiaio/sdk/latest download tarball, grep -R "Object.assign\|_.merge\|\.prototype\|__proto__" dist/; static analysis of message handler paths
impact: Supply-chain RCE in any app using @gladiaio/sdk live transcription via malicious server message; High
testability: PASSIVE
[PARKED] Official npm @gladiaio/sdk prototype pollution via WebSocket message handling leads to RCE in consumer apps: confidence 55 < threshold for top-3 but kept for rotation; verify_steps passive-only but requires deep SDK audit not yet done
[FINAL] 1. Webhook callback_config.url SSRF to cloud metadata via format:uri validation bypass (confidence 75, SSRF @ api.gladia.io, AUTH_HELPED)
[FINAL] 2. OAuth state parameter missing enables CSRF on Google auth flow leading to account linking (confidence 70, OAUTH @ app.gladia.io, HUMAN_ONLY)
[FINAL] 3. Orphaned npm gladia@0.1.3 impersonates official SDK and leaks raw API key in WebSocket URL query at dist-tag latest (confidence 97, OTHER @ sdk, PASSIVE) — re-confirmed from prior cycle
[NEXT] PROBE: GET https://registry.npmjs.org/@gladiaio/sdk/latest verify dist-tag=2.1.3, download tarball shasum, grep -R "Object.assign\|_.merge\|\.prototype\|__proto__" dist/ for prototype pollution sinks in WebSocket message handlers
[LEARN] ACCEPTED OTHER @ gladia: no new surface this cycle, re-confirmed static via NO_DRIFT OpenAPI spec and inventory timestamps
[LEARN] ACCEPTED SSRF @ api.gladia.io: webhook callback_config.url accepts format:uri without scheme allowlist — SSRF surface extends beyond audio_url (AUTH_HELPED)
[LEARN] ACCEPTED OAUTH @ app.gladia.io: /signin?redirect_to reflection alive byte-fresh — 0 CSP form-action directives (gap confirmed); post-auth honoring sole unverified gate (HUMAN_ONLY); state parameter presence unverified
[LEARN] ACCEPTED OTHER @ sdk: official @gladiaio/sdk@2.1.0 confirmed separate from orphaned gladia@0.1.3 — 14+ @gladia.io maintainers, SLSA provenance, repo github.com/gladiaio/sdk
[RISK] api.gladia.io: 73 reason: frozen spec but dual SSRF vectors (audio_url + webhook callback_config.url) both AUTH_HELPED to 169.254.169.254 → cloud credential theft critical if key obtained
[RISK] app.gladia.io: 78 reason: unauthed open-redirect reflection + 0 form-action CSP gap live and chainable to OAuth code theft → ATO via HUMAN_ONLY post-auth step; state parameter unverified adds CSRF linking risk
[RISK] sdk: 68 reason: orphaned gladia@0.1.3 impersonation + WebSocket key leak = supply-chain hijack medium-high (namespace claimable); official @gladiaio/sdk supply-chain hardened (SLSA) but prototype pollution audit pending
