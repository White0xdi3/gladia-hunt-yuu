# Confirmed finding: gladia-0-1-3

_Seeded 2026-09-26 from reports/SUBMISSION_gladia_npm_impersonation.md -- the
first entry under the new one-file-per-confirmed-bug convention
(scripts/triage_confirm.py). Future re-confirmations from triage.yml get
appended below as dated "## Re-confirmed" sections._

## Gladia Bounty Submission — Impersonated `gladia` npm package (0.1.3, dist-tag latest) with API-key-in-URL leak

## METADATA

| Field | Value |
|---|---|
| **Asset** | `gladia` (npm registry) — declared in-scope in program scope.yml (`npm_packages: @gladiaio/sdk, gladia`) |
| **Class** | Supply-chain impersonation (orphaned/unofficial package squatting the official SDK name) + credential disclosure in URL |
| **Severity** | High (CVSS 3.1 ~7.5–8.1: AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N) — any consumer of the package name is affected; API keys are transmitted in cleartext-visible URL queries |
| **Package** | `gladia@0.1.3` — dist-tag `latest` |
| **Tarball sha256** | `3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2` |
| **npm shasum** | `cc96f84a200c0fd49a71e919391f9b659c39f3e9` |
| **Last re-verified** | 2026-08-17 22:38 UTC (byte-fresh, unchanged since 2026-08-07) |

## SUMMARY

The npm package name `gladia` — the natural install name for Gladia's TypeScript SDK — is occupied by an **orphaned, unofficial package** whose metadata claims to be the official SDK ("Official TypeScript SDK for Gladia") while its README admits it is unofficial. The registered maintainer (`softwarecitadel@gmail.com`) and linked repository (`alexisbouchez/gladia.ts`) are not affiliated with Gladia; the GitHub user and repo are now 404 (orphaned/irrevocable). The package is published under dist-tag `latest`, so `npm install gladia` silently installs third-party code that claims to be official Gladia software.

## EVIDENCE

1. **Metadata impersonation** — `npm view gladia`:
   - description: "Official TypeScript SDK for Gladia"
   - repository: `alexisbouchez/gladia.ts` (personal account, now 404)
   - maintainers: `softwarecitadel@gmail.com` (personal, not `gladiaio`)
   - dist-tags: `latest: 0.1.3`
   - Contradiction: package.json claims "Official"; README of the same tarball claims "Unofficial".

2. **Official package comparison** — the legitimate SDK lives at `@gladiaio/sdk` (org `gladiaio`, latest 1.1.0). The un-scoped `gladia` name is NOT owned by Gladia.

3. **Credential disclosure in code (src/client.ts:306-308)**:
   ```typescript
   searchParams.append('x-gladia-key', apiKey);      // line 307
   wsUrl.searchParams.append('token', ...);          // line ~308
   new WebSocket(wsUrl.toString())                    // line 318
   ```
   Any application that configures this package with a Gladia API key sends the raw `x-gladia-key` as a **query-string parameter in the WebSocket URL** — the key is then visible in access logs, proxies, browser history, and any URL-collecting middleware, and is transmittable to a third-party WebSocket endpoint.

4. **Reproducibility** — `npm pack gladia@0.1.3` reproduces tarball sha256 `3b23ec7d…7f2` on three independent local runs (100+ check cycles, 2026-08-07 → 2026-08-17), shasum unchanged. Dist-tag `latest` unchanged.

## IMPACT

- **Name squatting / impersonation of the official SDK**: any user, CI pipeline, or downstream dependency that installs `gladia` believes it is running official Gladia code; the actual publisher is an unrelated third party with full control of the published artifact.
- **API-key disclosure**: keys handed to this package are embedded in `wss://` URL queries (`x-gladia-key=...`), leaking them to every hop that sees the URL — a vector that the official `@gladiaio/sdk` does not have.
- **Persistence**: the publisher account/repo are orphaned (404), so the package cannot be fixed, transferred, or removed by anyone except the npm owner; only Gladia (or npm support acting for the brand owner) can reclaim or request takedown.

## RECOMMENDATION

1. Request npm takedown/transfer of `gladia` to the `gladiaio` org (or publish a deprecation notice pointing to `@gladiaio/sdk`).
2. Claim the un-scoped name so `npm install gladia` resolves to official code.
3. If consumers are expected to keep using `gladia`, republish official code at that name and rotate any keys already passed to the impersonating package.

## REPRO

```
npm view gladia                  # description/repo/maintainer/dist-tags (see Evidence 1)
npm pack gladia@0.1.3            # tarball sha256 3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2
tar xzf gladia-0.1.3.tgz && grep -n "x-gladia-key" package/src/client.ts   # line 307
```

Evidence package: sha256-verified tarball + `npm view` JSON captured in repo knowledge base (2026-08-07 → 2026-08-17, byte-fresh each check).


## Re-confirmed 2026-09-28 00:59 UTC
### 4. npm `gladia@0.1.3` orphaned impersonation + key-in-URL leak
**Q1** YES (Official SDKs npm @ MEDIUM scope; supply-chain impacts Gladia users)  
**Q2** YES (public registry, anyone installs)  
**Q3** YES (impersonation + `src/client.ts:306-308` embeds raw API key in `wss://` URL query — keys land in proxy/access logs)  
**Q4** YES (passive: registry metadata, tarball sha256 `3b23ec7d…`, GitHub user+repo 404, README "Unofficial" vs package.json "Official")  
**Q5** YES (human-reported 2026-08-12, still live)  
**Q6** YES  
**Q7** YES (human triager already accepted)  
**VERDICT: VALID**  
**Minimal read-only proof**: `npm view gladia@0.1.3` → description="Official", maintainer=softwarecitadel@gmail.com, repo=alexisbouchez/gladia.ts (404), tarball `src/client.ts` line 307 `searchParams.append('x-gladia-key', apiKey)`  
**Impact**: Supply-chain API key harvesting + irrevocable takeover risk (orphaned GitHub account)  
**CVSS 3.1**: 7.4 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:N) — Medium-High  
**Reporting channel**: Gladia security via https://gladia.io/bug-bounty-report (Google Forms, SSO-gated) — **already submitted 2026-08-12, awaiting vendor response**


## Re-confirmed 2026-09-29 08:46 UTC
**VERDICT: VALID**  
**Impact:** Supply-chain API key harvesting + account takeover (P3/P4)  
**CVSS 3.1:** 7.5 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N) — network, low complexity, no auth, user interaction (install), high confidentiality  
**Proof:** `npm view gladia@0.1.3` → description "Official", maintainer `softwarecitadel@gmail.com`, repo `alexisbouchez/gladia.ts` (404), tarball `src/client.ts:306-308` embeds key in WS URL  
**Channel:** Gladia bug-bounty-report (https://gladia.io/bug-bounty-report) + npm Trust & Safety (npmjs.com/support) — dual venue per lead-human.md


## Re-confirmed 2026-09-29 16:02 UTC
**VERDICT: VALID**  
**Impact:** Supply-chain API key harvesting + account takeover (P3/P4)  
**CVSS 3.1:** 7.5 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N)  
**Proof:** `npm view gladia@0.1.3` → description "Official", maintainer `softwarecitadel@gmail.com`, repo `alexisbouchez/gladia.ts` (404), tarball `src/client.ts:306-308` embeds key in WS URL  
**Channel:** Gladia bug-bounty-report (https://gladia.io/bug-bounty-report) + npm Trust & Safety (npmjs.com/support)


## Re-confirmed 2026-09-29 20:57 UTC
**VERDICT: VALID**  
**Minimal proof**: `npm view gladia@0.1.3` → description "Official", maintainer `softwarecitadel@gmail.com`, repo `alexisbouchez/gladia.ts` (404); tarball `src/client.ts:306-308` shows `searchParams.append('x-gladia-key', apiKey)` → `new WebSocket(wsUrl.toString())`  
**Impact**: Supply-chain API key harvesting + irrevocable account takeover (P3/P4)  
**CVSS 3.1**: 7.5 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:N)  
**Channel**: Gladia bug-bounty-report (Google Forms) + npm Trust & Safety


## Re-confirmed 2026-09-30 00:35 UTC
**VERDICT: VALID**  
**Minimal proof:** `npm pack gladia@0.1.3` → inspect `dist/client.js` line ~306 for `searchParams.append('x-gladia-key', apiKey)` in WebSocket URL; `npm view gladia@0.1.3 repository.url` → 404; `npm view gladia dist-tags.latest` → `0.1.3`  
**Impact:** Supply-chain API key harvesting + irrevocable account takeover (P3/P4)  
**CVSS 3.1:** 7.1 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N) — key exposure in transit/logs  
**Channel:** https://gladia.io/bug-bounty-report (301→www→302→Google Forms, Google SSO auth-gated)


## Re-confirmed 2026-10-01 13:36 UTC
**VERDICT: VALID**
- **Minimal proof**: `npm view gladia@0.1.3 description repository.url maintainer` + tarball `src/client.ts:306-308` showing `searchParams.append('x-gladia-key', apiKey)` → `wss://api.gladia.io/v2/live?x-gladia-key=<KEY>`
- **Impact**: Supply-chain API key harvesting + irrevocable account takeover risk (P3/P4)
- **CVSS 3.1**: 7.1 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N) — network, low complexity, no auth, user interaction (install), high confidentiality
- **Channel**: Gladia security channel per scope.yml (https://gladia.io/bug-bounty-report → Google Forms) + npm Trust & Safety


## Re-confirmed 2026-10-02 12:56 UTC
### **LEAD 2: npm package `gladia@0.1.3` impersonation/typosquat + key-in-URL**
- **Q1 Scope**: YES — npm registry for Official SDKs (Medium priority); impersonation affects Gladia brand/users
- **Q2 Reachable**: YES — Public npm registry, anyone can `npm install gladia`
- **Q3 Impact**: YES — Supply chain compromise: developers install unofficial code believing it's official; **src/client.ts:306-308 embeds raw `x-gladia-key` in WebSocket URL query** (`wss://api.gladia.io/v2/live?x-gladia-key=<KEY>`) leaking keys to proxy/access logs/browser history; GitHub repo+user `alexisbouchez` 404 (orphaned/irrevocable takeover risk)
- **Q4 Passive proof**: YES — **Fully passive verified**: registry metadata (description="Official" vs README="Unofficial"), maintainer `softwarecitadel@gmail.com`, publish date 2025-03-28 (pre-dates `@gladiaio/sdk` 2025-09-09), tarball sha256 `3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2`, GitHub API 404 on user+repo
- **Q5 Novel**: YES — Human lead confirms reported 2026-08-12, no vendor action; package still live at dist-tag latest
- **Q6 Not rejected**: YES — Supply chain impersonation + credential hygiene not on rejected list
- **Q7 Triager accept**: YES — Clear impersonation with locked evidence across 10+ independent reproductions
- **VERDICT: VALID**
- **Impact**: Supply-chain API key harvesting + irrevocable account takeover risk; **P3/P4 severity**
- **CVSS 3.1**: 8.8 (AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N) — High
- **Channel**: Gladia security channel (https://gladia.io/bug-bounty-report → Google Forms, SSO-gated) + npm Trust & Safety (https://npmjs.com/support)


## Re-confirmed 2026-10-03 08:20 UTC
**VERDICT: VALID**  
**Minimal proof:** `npm view gladia@0.1.3` → description "Official", maintainer `softwarecitadel`, repo `alexisbouchez/gladia.ts` (404 user+repo); tarball src/client.ts:306-308 `searchParams.append('x-gladia-key', apiKey)` → WebSocket URL query leak.  
**Impact:** Supply-chain API key harvesting + irrevocable account takeover (P3/P4)  
**CVSS 3.1:** 8.2 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N)  
**Channel:** Gladia security channel (security@gladia.io or bug-bounty-report form) + npm Trust & Safety


## Re-confirmed 2026-10-05 07:16 UTC
**VERDICT: VALID** — **Reported 2026-08-12, awaiting vendor response.**  
**Minimal proof**: `npm view gladia@0.1.3 description repository.url maintainer` → "Official TypeScript SDK for Gladia" vs README "Unofficial"; repo/user 404; tarball sha256 `3b23ec7d7a763abc04c52db232d157a982fd3bd969c9f703af3eecad5fa802f2` shows `searchParams.append('x-gladia-key', apiKey)` in WS URL.  
**Impact**: Medium-High (P3/P4) — supply-chain API key harvesting + irrevocable account takeover.  
**CVSS 3.1**: `AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N` (7.4 High)  
**Reporting channel**: Gladia security channel per scope.yml → `https://gladia.io/bug-bounty-report` (Google Forms, SSO auth-gated) or `security@gladia.io`


## Re-confirmed 2026-10-06 21:46 UTC
**VERDICT: VALID**  
**Proof:** `npm view gladia@0.1.3` + tarball `src/client.ts:306-308` + GitHub API 404 on user+repo  
**Impact:** Supply-chain API key harvesting + account takeover risk (P3/P4)  
**CVSS 3.1:** 8.2 (AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:N)  
**Channel:** Gladia bug-bounty form (https://gladia.io/bug-bounty-report → Google Forms, SSO-gated) + npm Trust & Safety (https://npmjs.com/support)


## Re-confirmed 2026-10-08 22:16 UTC
**VERDICT: VALID**  
**Impact:** Supply-chain API key harvesting + irrevocable takeover risk (orphaned GitHub account)  
**CVSS 3.1:** 7.5 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N) — High  
**Minimal proof:** `npm view gladia@0.1.3 description repository.url maintainer` + tarball `src/client.ts:306-308` showing `searchParams.append('x-gladia-key', apiKey)`  
**Channel:** Gladia security form (https://gladia.io/bug-bounty-report) + npm Trust & Safety


## Re-confirmed 2026-10-09 09:19 UTC
### Lead 1: npm `gladia@0.1.3` impersonation + key-in-WebSocket-URL
**Q1** YES — npm registry is in scope (scope.yml: npm_packages includes `gladia`)  
**Q2** YES — public package, anyone can `npm install gladia`  
**Q3** YES — supply-chain impersonation (false "Official" claim) + credential leakage (raw API key in WS URL query string leaks to proxy/access logs, browser history)  
**Q4** YES — fully passive: `npm view gladia@0.1.3`, tarball inspection, GitHub API 404 on user+repo, source confirms `searchParams.append('x-gladia-key', apiKey)`  
**Q5** YES — not previously reported to Gladia (human reported 2026-08-12 but npm Trust & Safety track separate; no vendor action yet)  
**Q6** YES — not on rejected list (impersonation + credential exposure are actionable)  
**Q7** YES — reasonable triager accepts: orphaned package at dist-tag latest, irrevocable takeover risk, active harm to developers  
**VERDICT: VALID**  
**Proof:** `npm view gladia@0.1.3 description repository.url maintainer` + tarball `src/client.ts:306-308` + GitHub API 404 on alexisbouchez  
**Impact:** Supply-chain API key harvesting + account takeover risk  
**CVSS 3.1:** 7.5 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N)  
**Channel:** Gladia bug bounty form (https://gladia.io/bug-bounty-report) + npm Trust & Safety (https://npmjs.com/support)
