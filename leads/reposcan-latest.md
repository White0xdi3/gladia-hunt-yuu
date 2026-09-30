
===== REPOSCAN 2026-09-30 13:52:01 UTC =====
## Grep hits:
SCAN SUMMARY: 5688 code/config files scanned, 652 hits
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
### Classification Table

| Category | File:Line | Evidence | Classification |
|----------|-----------|----------|----------------|
| **TEST_OR_EXAMPLE** | `packages/sandbox-vercel/src/vercel-sandbox.test.ts:166,171` | `deniedCIDRs: ['169.254.169.254/32']` — test config blocking cloud metadata IP | TEST_OR_EXAMPLE (security control test) |
| **TEST_OR_EXAMPLE** | `packages/mcp/src/tool/oauth.test.ts:740,905,908` | `client_secret: 'secret123'`, `access_token: 'access123'`, `refresh_token: 'refresh123'` | TEST_OR_EXAMPLE (obvious test fixtures) |
| **TEST_OR_EXAMPLE** | `packages/mcp/src/tool/mcp-http-transport.test.ts:409,411` | `access_token: 'expired-access-token'`, `refresh_token: 'rotating-refresh-token'` | TEST_OR_EXAMPLE |
| **TEST_OR_EXAMPLE** | `packages/openai/src/**/*.test.ts` (20+ lines) | `apiKey: 'test-api-key'` repeated across provider tests | TEST_OR_EXAMPLE |
| **TEST_OR_EXAMPLE** | `packages/assemblyai/src/assemblyai-transcription-model.test.ts:13,277` | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| **TEST_OR_EXAMPLE** | `packages/togetherai/src/togetherai-provider.test.ts:99,112,165` | `apiKey: 'custom-key'`, `apiKey: 'explicit-key'` | TEST_OR_EXAMPLE |
| **TEST_OR_EXAMPLE** | `packages/google-vertex/src/**/*.test.ts` (6 lines) | `apiKey: 'test-api-key'`, `token: 'mocked-token'`, `access_token: 'mock.jwt.token'`, `private_key: 'invalid-key'` | TEST_OR_EXAMPLE |
| **TEST_OR_EXAMPLE** | `packages/amazon-bedrock/src/**/*.test.ts` (7 lines) | `sessionToken: 'dynamic-session-token'`, `static-session-token`, `test-session-token`, `async-session-token`, `apiKey: 'test-api-key-123'`, `nextToken: 'test-token'` | TEST_OR_EXAMPLE |
| **TEST_OR_EXAMPLE** | `packages/amazon-bedrock/src/amazon-bedrock-provider.ts:48` | `* apiKey: 'your-api-key-here'` — JSDoc example | TEST_OR_EXAMPLE |
| **INTERESTING** | `pnpm-lock.yaml:289,291,2368` + `tsconfig.json:70` + `analyze-providers.ts:21` + `.github/tigent.yml:30` | `@ai-sdk/gladia` linked as local package in vercel-ai monorepo; listed in provider matrix | INTERESTING (official org integration confirmed by RAG) |
| **INTERESTING** | (external/npm) `gladia@0.1.3` | npm description "Official TypeScript SDK" but README "Unofficial"; maintainer `softwarecitadel` personal; repo `alexisbouchez/gladia.ts` 404 | INTERESTING (supply-chain: misleading official claim, orphaned personal repo) |

---

### Verdict List

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Hardcoded secrets in test files | **no** | All are obvious test fixtures (`test-api-key`, `secret123`, `mocked-token`, etc.) |
| `@ai-sdk/gladia` in vercel-ai | **no** | Confirmed official org integration (RAG: `vercel-ai @ai-sdk/gladia = official org integration`) |
| `gladia@0.1.3` npm package (misleading "Official" + personal maintainer) | **no** | Known since 2026-08-07 (RAG: `npm gladia 0.1.3... maintainer softwarecitadel... repo alexisbouchez 404 orphaned/irrevocable`); supply-chain surface but not a vuln in Gladia-owned code |
| SSRF protection test (169.254.169.254 deny list) | **no** | Defensive control, not a vulnerability |

**No reportable findings this cycle.** All secrets are test fixtures; the only anomalous surface (`gladia@0.1.3` npm) is a known, pre-existing supply-chain oddity in a non-Gladia-owned package.
