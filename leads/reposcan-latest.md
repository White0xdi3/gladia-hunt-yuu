
===== REPOSCAN 2026-10-03 05:13:35 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw -name "*.ts" -o -name "*.js" -o -name "*.json" -o -name "*.yaml" -o -name "*.yml" | head -20
reposcan-raw/gladiaio/vercel-ai/examples/mcp/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/server-instructions/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/server-instructions/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/http/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/http/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/shopify-mcp/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/repro-test.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/image-content/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/provider-metadata/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/provider-metadata/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-ui/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-with-auth/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-with-auth/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-multi-step/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-multi-step/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-prompts/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-prompts/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/output-schema/client.ts
[0m
**CLASSIFICATION TABLES**

| Category | File | Line | Pattern | Classification |
|----------|------|------|---------|----------------|
| **TEST_OR_EXAMPLE** | vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | `client_secret: 'secret123'` | Test fixture |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | `access_token: 'access123'` | Test fixture |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | `refresh_token: 'refresh123'` | Test fixture |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | `access_token: 'expired-access-token'` | Test fixture |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | `refresh_token: 'rotating-refresh-token'` | Test fixture |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/openai/src/**/*.test.ts | 48+ | `apiKey: 'test-api-key'` (20+ occurrences) | Test fixture |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13, 277 | `apiKey: 'test-api-key'` | Test fixture |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/togetherai/src/*.test.ts | 99, 112, 165 | `apiKey: 'custom-key'`, `explicit-key` | Test fixture |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/google-vertex/src/*.test.ts | 120, 187, 405, 419 | `apiKey: 'test-api-key'` | Test fixture |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/google-vertex/src/edge/*.test.ts | 68, 134, 150 | `mock.jwt.token`, `invalid-key`, `mocked-token` | Test fixture |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/amazon-bedrock/src/*.test.ts | 100, 128, 152, 158, 331, 442 | `sessionToken: 'test-session-token'`, `dynamic-session-token`, `static-session-token`, `async-session-token`, `test-api-key-123` | Test fixture |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts | 48 | `apiKey: 'your-api-key-here'` | Documentation placeholder |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json | 36 | `encrypted_content: "gAAAAABplLP7..."` | Test fixture (encrypted) |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/amazon-bedrock/src/reranking/amazon-bedrock-reranking-model.test.ts | 55 | `nextToken: 'test-token'` | Test fixture |

| Category | File | Line | Pattern | Classification |
|----------|------|------|---------|----------------|
| **INTERESTING** | vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166, 171 | `deniedCIDRs: ['169.254.169.254/32']` | **Security control** - explicit SSRF block to AWS metadata endpoint in test config |
| **INTERESTING** | vercel-ai/pnpm-lock.yaml | 289, 291, 2368 | `@ai-sdk/gladia` version link: `../../packages/gladia` | Official Vercel AI SDK integration (per RAG: verified official org integration) |
| **INTERESTING** | vercel-ai/tsconfig.json | 70 | `"path": "packages/gladia"` | Monorepo structure for Gladia provider |
| **INTERESTING** | vercel-ai/.github/tigent.yml | 30 | Provider list includes `provider/gladia` | CI test matrix includes Gladia |
| **INTERESTING** | vercel-ai/tools/analyze-downloads/src/analyze-providers.ts | 21 | `'@ai-sdk/gladia'` | Download analytics for Gladia provider |

| Category | File | Line | Pattern | Classification |
|----------|------|------|---------|----------------|
| **ENDPOINT_LEAK** | — | — | None found | — |
| **REAL_SECRET** | — | — | None found | — |

**VERDICT**

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Hardcoded test keys (`test-api-key`, `secret123`, `mock.jwt.token`, etc.) | **no** | All in `*.test.ts` / fixtures — test data only |
| `deniedCIDRs: ['169.254.169.254/32']` | **no** | Defensive control (deny list), not vulnerability |
| `@ai-sdk/gladia` in vercel-ai monorepo | **no** | Official integration, already tracked in RAG |
| npm `gladia` 0.1.3 (alexisbouchez personal repo) | **no** | Already in RAG as ORPHANED/UNVERIFIED — known, not new |
| Encrypted fixture content | **no** | Test fixture, not a secret |

**SUMMARY**: 0 reportable findings this cycle. All hits are test fixtures, defensive controls, or previously documented integrations. No new attack surface, secrets, or misconfigurations detected.
