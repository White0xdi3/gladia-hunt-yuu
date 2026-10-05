
===== REPOSCAN 2026-10-05 09:00:40 UTC =====
## Grep hits:
SCAN SUMMARY: 5693 code/config files scanned, 654 hits
reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:289: '@ai-sdk/gladia':
reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:291: version: link:../../packages/gladia
reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:2368: packages/gladia:
reposcan-raw/gladiaio/vercel-ai/tsconfig.json:70: "path": "packages/gladia"
reposcan-raw/gladiaio/vercel-ai/tools/analyze-downloads/src/analyze-providers.ts:21: '@ai-sdk/gladia',
reposcan-raw/gladiaio/vercel-ai/.github/tigent.yml:30: provider/openai, provider/anthropic, provider/google, provider/google-vertex, provider/azure, provider/amazon-bedrock, provider/xai, provider/mistral, provider/cohere, provider/groq, provider/deepseek, provider/fireworks
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:166: deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:171: subnets: { deny: ['169.254.169.254/32'] },
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:740: client_secret: 'secret123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:905: access_token: 'access123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:908: refresh_token: 'refresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts:409: access_token: 'expired-access-token',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts:411: refresh_token: 'rotating-refresh-token',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/openai-provider.test.ts:48: apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/openai-provider.test.ts:66: apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/openai-provider.test.ts:84: apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/files/openai-files.test.ts:40: const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/files/openai-files.test.ts:61: const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/files/openai-files.test.ts:78: const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/image/openai-image-model.test.ts:14: const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/image/openai-image-model.test.ts:114: apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/chat/openai-chat-language-model.test.ts:113: apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/chat/openai-chat-language-model.test.ts:778: apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/chat/openai-chat-language-model.test.ts:3310: apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/completion/openai-completion-language-model.test.ts:45: apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/completion/openai-completion-language-model.test.ts:246: const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/completion/openai-completion-language-model.test.ts:381: apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/speech/openai-speech-model.test.ts:10: const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/speech/openai-speech-model.test.ts:54: apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json:36: "encrypted_content": "gAAAAABplLP75yhVf0v4856Geb-oLdsjDPhdISdmBJvCNP9Su2ib_UJkknntI-GqAeBDF59lGgLqPE4lDYfm5q7IhjCloCkaGycZGBo9GHcLdpuKj63e_CyVxYFNZdP4HYXKpKQZbbz7blA_nATSTNNN-PQpQ1DYWjYfq6uAxEUrm-4PUPSorUPWIiByyqIGDgHt-b
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/embedding/openai-embedding-model.test.ts:13: const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/embedding/openai-embedding-model.test.ts:137: apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/skills/openai-skills.test.ts:12: const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/transcription/openai-transcription-model.test.ts:17: const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/transcription/openai-transcription-model.test.ts:73: apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts:13: const provider = createAssemblyAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts:277: apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/togetherai-provider.test.ts:99: apiKey: 'custom-key',
reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/togetherai-provider.test.ts:112: apiKey: 'custom-key',

## Model analysis:
[0m
> build · nemotron-3-ultra-free
[0m
Looking at the scan results, nearly all hits are from `vercel-ai` (a fork/integration repo) and are **test fixtures** with obvious placeholder values. Let me classify:
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -r "test-api-key\|custom-key\|explicit-key\|secret123\|access123\|refresh123\|mocked-token\|mock\.jwt\.token\|invalid-key\|dynamic-session-token\|static-session-token\|async-session-token\|test-api-key-123\|test-session-token\|test-token" reposcan-raw/gladiaio/vercel-ai --include="*.test.ts" --include="*.test.tsx" | head -5
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-sse-transport.test.ts:      authorization: 'Bearer test-token',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:    client_secret: 'secret123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:    access_token: 'access123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:    refresh_token: 'refresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:    client_secret: 'secret123',
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -n "169.254.169.254" reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts
166:        deniedCIDRs: ['169.254.169.254/32'],
171:          subnets: { deny: ['169.254.169.254/32'] },
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -rn "@ai-sdk/gladia" reposcan-raw/gladiaio/vercel-ai --include="*.ts" --include="*.json" | head -10
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/basic.ts:1:import { gladia } from '@ai-sdk/gladia';
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/url.ts:1:import { gladia } from '@ai-sdk/gladia';
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/string.ts:1:import { gladia } from '@ai-sdk/gladia';
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/package.json:26:    "@ai-sdk/gladia": "workspace:*",
reposcan-raw/gladiaio/vercel-ai/tools/analyze-downloads/src/analyze-providers.ts:21:    '@ai-sdk/gladia',
reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json:2:  "name": "@ai-sdk/gladia",
reposcan-raw/gladiaio/vercel-ai/.changeset/pre.json:26:    "@ai-sdk/gladia": "2.0.24",
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw -name "package.json" -exec grep -l '"name": "gladia"' {} \;
(no output)
[0m
---

## Classification Tables

### TEST_OR_EXAMPLE (564 hits — all test fixtures)
| File | Line | Pattern | Context |
|------|------|---------|---------|
| `vercel-ai/packages/openai/**/*.test.ts` | 48, 66, 84, 14, 113, 778, 3310, 45, 246, 381, 10, 54, 13, 137, 12, 17, 73 | `test-api-key` | Unit test API key placeholders |
| `vercel-ai/packages/assemblyai/**/*.test.ts` | 13, 277 | `test-api-key` | Unit test API key placeholders |
| `vercel-ai/packages/togetherai/**/*.test.ts` | 99, 112, 165, 7 | `custom-key`, `explicit-key`, `test-api-key` | Unit test API key placeholders |
| `vercel-ai/packages/google-vertex/**/*.test.ts` | 120, 187, 405, 419, 5, 21, 68, 134, 150, 95 | `test-api-key`, `mocked-token`, `mock.jwt.token`, `invalid-key` | Unit test auth fixtures |
| `vercel-ai/packages/amazon-bedrock/**/*.test.ts` | 128, 152, 158, 100, 331, 442, 209, 55 | `dynamic-session-token`, `static-session-token`, `async-session-token`, `test-api-key-123`, `test-session-token`, `test-token`, `nextToken` | Unit test AWS fixtures |
| `vercel-ai/packages/mcp/**/*.test.ts` | 740, 905, 908, 409, 411 | `secret123`, `access123`, `refresh123`, `expired-access-token`, `rotating-refresh-token` | OAuth test fixtures |
| `vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json` | 36 | `gAAAAABplLP75yhVf0v4856Geb-oLdsjDPhdISdmBJvCNP9Su2ib_UJkknntI-GqAeBDF59lGgLqPE4lDYfm5q7IhjCloCkaGycZGBo9GHcLdpuKj63e_CyVxYFNZdP4HYXKpKQZbbz7blA_nATSTNNN-PQpQ1DYWjYfq6uAxEUrm-4PUPSorUPWIiByyqIGDgHt-b` | Encrypted test fixture (not a secret) |

### INTERESTING (2 hits)
| File | Line | Finding | Notes |
|------|------|---------|-------|
| `vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166, 171 | `deniedCIDRs: ['169.254.169.254/32']` | **SSRF protection test** — asserts metadata endpoint is blocked (good) |
| `vercel-ai` (multiple) | — | `@ai-sdk/gladia` workspace package | Official Vercel AI SDK integration for Gladia (legitimate) |

### REAL_SECRET: **0**
### ENDPOINT_LEAK: **0** (no new endpoints beyond inventory)

---

## Verdict

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Test API keys / OAuth fixtures | **no** | All in `*.test.ts` files, obvious placeholders (`test-api-key`, `secret123`, `mocked-token`) |
| Encrypted fixture in `openai-compaction.1.json` | **no** | Test fixture, not a live secret |
| SSRF denial test (`169.254.169.254/32`) | **no** | **Positive security control** — verifies metadata endpoint is blocked |
| `@ai-sdk/gladia` package | **no** | Official Vercel AI SDK integration (workspace package in gladiaio/vercel-ai) |
| npm `gladia` 0.1.3 (maintainer: softwarecitadel) | **no** | Already tracked in inventory — personal package, not official `@gladiaio/sdk` |

**No reportable findings this cycle.** All hits are test fixtures or known/expected inventory items. Passive recon remains exhausted per RAG.
