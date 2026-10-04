
===== REPOSCAN 2026-10-04 07:00:05 UTC =====
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
**Classification Table**

| Category | File | Line | Classification | Notes |
|----------|------|------|----------------|-------|
| Config/Dependency | vercel-ai/pnpm-lock.yaml | 289, 291, 2368 | CONFIG | `@ai-sdk/gladia` local package link |
| Config | vercel-ai/tsconfig.json | 70 | CONFIG | Path mapping for packages/gladia |
| Code | vercel-ai/tools/analyze-downloads/src/analyze-providers.ts | 21 | CODE | Import reference |
| CI Config | vercel-ai/.github/tigent.yml | 30 | CONFIG | Provider list for CI |
| **INTERESTING** | **vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts** | **166, 171** | **INTERESTING** | **SSRF protection test: explicit deny of `169.254.169.254/32` (cloud metadata)** |
| Test/Fixture | vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740, 905, 908 | TEST_OR_EXAMPLE | `secret123`, `access123`, `refresh123` |
| Test/Fixture | vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409, 411 | TEST_OR_EXAMPLE | `expired-access-token`, `rotating-refresh-token` |
| Test/Fixture | vercel-ai/packages/openai/src/**/*.test.ts | 48-3310 | TEST_OR_EXAMPLE | Repeated `test-api-key` |
| Test/Fixture | vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json | 36 | TEST_OR_EXAMPLE | Fixture `encrypted_content` (base64) |
| Test/Fixture | vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13, 277 | TEST_OR_EXAMPLE | `test-api-key` |
| Test/Fixture | vercel-ai/packages/togetherai/src/togetherai-provider.test.ts | 99, 112, 165 | TEST_OR_EXAMPLE | `custom-key`, `explicit-key`, `test-api-key` |
| Test/Fixture | vercel-ai/packages/google-vertex/src/**/*.test.ts | 120-419 | TEST_OR_EXAMPLE | `test-api-key`, `mocked-token`, `mock.jwt.token`, `invalid-key` |
| Test/Fixture | vercel-ai/packages/amazon-bedrock/src/**/*.test.ts | 48-442 | TEST_OR_EXAMPLE | `test-api-key`, `dynamic-session-token`, `static-session-token`, `async-session-token`, `test-session-token` |

**Verdict List**

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| SSRF protection test (169.254.169.254/32 deny) | **no** | Defensive test proving awareness, not a vulnerability |
| All hardcoded `test-api-key`, `secret123`, `mocked-token`, etc. | **no** | Clearly test/fixture data (naming, context in `.test.ts` files) |
| `@ai-sdk/gladia` local package in vercel-ai monorepo | **no** | Official integration per knowledge base, not supply-chain risk |
| No live secrets, endpoint leaks, or real credentials found | **no** | 100% test/config noise |

**Summary**: DELTA confirms 0 new hits. All 654 hits are pre-existing test fixtures, config, or defensive SSRF test code. No reportable findings this cycle.
