
===== REPOSCAN 2026-10-10 22:38:06 UTC =====
## Grep hits:
SCAN SUMMARY: 5694 code/config files scanned, 654 hits
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
**CLASSIFICATION TABLE**

| Category | File | Line | Finding | Classification |
|----------|------|------|---------|----------------|
| TEST_OR_EXAMPLE | vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | `client_secret: 'secret123'` | TEST_OR_EXAMPLE |
| TEST_OR_EXAMPLE | vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | `access_token: 'access123'` | TEST_OR_EXAMPLE |
| TEST_OR_EXAMPLE | vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | `refresh_token: 'refresh123'` | TEST_OR_EXAMPLE |
| TEST_OR_EXAMPLE | vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | `access_token: 'expired-access-token'` | TEST_OR_EXAMPLE |
| TEST_OR_EXAMPLE | vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | `refresh_token: 'rotating-refresh-token'` | TEST_OR_EXAMPLE |
| TEST_OR_EXAMPLE | vercel-ai/packages/openai/**/*.test.ts | multiple | `apiKey: 'test-api-key'` (20+ occurrences) | TEST_OR_EXAMPLE |
| TEST_OR_EXAMPLE | vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13,277 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| TEST_OR_EXAMPLE | vercel-ai/packages/togetherai/src/**/*.test.ts | multiple | `apiKey: 'custom-key'`, `'explicit-key'`, `'test-api-key'` | TEST_OR_EXAMPLE |
| TEST_OR_EXAMPLE | vercel-ai/packages/google-vertex/src/**/*.test.ts | multiple | `apiKey: 'test-api-key'`, `mocked-token`, `mock.jwt.token` | TEST_OR_EXAMPLE |
| TEST_OR_EXAMPLE | vercel-ai/packages/amazon-bedrock/src/**/*.test.ts | multiple | `sessionToken: 'dynamic-session-token'`, `'test-session-token'`, `apiKey: 'test-api-key-123'` | TEST_OR_EXAMPLE |
| TEST_OR_EXAMPLE | vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts | 48 | Comment: `apiKey: 'your-api-key-here'` | TEST_OR_EXAMPLE |
| INTERESTING | vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166,171 | `deniedCIDRs: ['169.254.169.254/32']` — SSRF metadata IP explicitly blocked in tests | INTERESTING |
| ENDPOINT_LEAK | vercel-ai/pnpm-lock.yaml | 289,291 | `@ai-sdk/gladia` linked as local package `packages/gladia` | ENDPOINT_LEAK (internal pkg ref) |
| ENDPOINT_LEAK | vercel-ai/tsconfig.json | 70 | Path alias `"packages/gladia"` | ENDPOINT_LEAK (internal pkg ref) |
| ENDPOINT_LEAK | vercel-ai/tools/analyze-downloads/src/analyze-providers.ts | 21 | Import `'@ai-sdk/gladia'` | ENDPOINT_LEAK (internal pkg ref) |

**VERDICT LIST**

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Hardcoded secrets in test files | **NO** | All are obvious test fixtures (`test-api-key`, `secret123`, `mocked-token`, `mock.jwt.token`) |
| `@ai-sdk/gladia` internal package references | **NO** | Known official org integration (per RAG: `vercel-ai @ai-sdk/gladia = official org integration`) |
| SSRF metadata IP (169.254.169.254) in deny-list test | **NO** | Defensive test pattern, not an exposure |
| No live credentials, no internal endpoints, no PII | **NO** | Scan clean for reportable findings |

**SUMMARY**: 0 reportable findings. All hits are test fixtures, known official integrations, or defensive test patterns.
