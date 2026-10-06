
===== REPOSCAN 2026-10-06 17:18:13 UTC =====
## Grep hits:
SCAN SUMMARY: 5696 code/config files scanned, 654 hits
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio/vercel-ai -name "*.test.ts" -o -name "*.fixture*" | head -20
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/openai.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/togetherai.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/luma.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/cerebras.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/amazon-bedrock.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/google-vertex-anthropic.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/google.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/fireworks.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/amazon-bedrock-anthropic.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/gateway.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/mistral.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/deepinfra.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/deepseek.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/azure.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/huggingface.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/anthropic.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/xai.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/cohere.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/groq.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/google-vertex.test.ts
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json
### CLASSIFICATION TABLES

#### TEST_OR_EXAMPLE (all test fixtures, mock data, sample keys)
| File | Line | Pattern | Classification |
|------|------|---------|----------------|
| `packages/mcp/src/tool/oauth.test.ts` | 740 | `client_secret: 'secret123'` | TEST_OR_EXAMPLE |
| `packages/mcp/src/tool/oauth.test.ts` | 905 | `access_token: 'access123'` | TEST_OR_EXAMPLE |
| `packages/mcp/src/tool/oauth.test.ts` | 908 | `refresh_token: 'refresh123'` | TEST_OR_EXAMPLE |
| `packages/mcp/src/tool/mcp-http-transport.test.ts` | 409 | `access_token: 'expired-access-token'` | TEST_OR_EXAMPLE |
| `packages/mcp/src/tool/mcp-http-transport.test.ts` | 411 | `refresh_token: 'rotating-refresh-token'` | TEST_OR_EXAMPLE |
| `packages/openai/src/openai-provider.test.ts` | 48,66,84 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/openai/src/files/openai-files.test.ts` | 40,61,78 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/openai/src/image/openai-image-model.test.ts` | 14,114 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/openai/src/chat/openai-chat-language-model.test.ts` | 113,778,3310 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/openai/src/completion/openai-completion-language-model.test.ts` | 45,246,381 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/openai/src/speech/openai-speech-model.test.ts` | 10,54 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/openai/src/embedding/openai-embedding-model.test.ts` | 13,137 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/openai/src/skills/openai-skills.test.ts` | 12 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/openai/src/transcription/openai-transcription-model.test.ts` | 17,73 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/assemblyai/src/assemblyai-transcription-model.test.ts` | 13,277 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/togetherai/src/togetherai-provider.test.ts` | 99,112,165 | `apiKey: 'custom-key'`, `'explicit-key'` | TEST_OR_EXAMPLE |
| `packages/togetherai/src/reranking/togetherai-reranking-model.test.ts` | 7 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/google-vertex/src/google-vertex-provider.test.ts` | 120 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/google-vertex/src/google-vertex-provider-base.test.ts` | 187,405,419 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/google-vertex/src/google-vertex-auth-google-auth-library.test.ts` | 5,21 | `token: 'mocked-token'` | TEST_OR_EXAMPLE |
| `packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts` | 68,134,150 | `access_token: 'mock.jwt.token'`, `private_key: 'invalid-key'` | TEST_OR_EXAMPLE |
| `packages/google-vertex/src/edge/google-vertex-provider-edge.test.ts` | 95 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/amazon-bedrock/src/amazon-bedrock-provider.test.ts` | 128,152,158 | `sessionToken: 'dynamic-session-token'`, `'static-session-token'` | TEST_OR_EXAMPLE |
| `packages/amazon-bedrock/src/amazon-bedrock-provider.ts` | 48 | Comment: `apiKey: 'your-api-key-here'` | TEST_OR_EXAMPLE |
| `packages/amazon-bedrock/src/amazon-bedrock-sigv4-fetch.test.ts` | 100,331,442 | `sessionToken: 'test-session-token'`, `'async-session-token'`, `apiKey: 'test-api-key-123'` | TEST_OR_EXAMPLE |
| `packages/amazon-bedrock/src/mantle/bedrock-mantle-provider.test.ts` | 209 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| `packages/amazon-bedrock/src/reranking/amazon-bedrock-reranking-model.test.ts` | 55 | `nextToken: 'test-token'` | TEST_OR_EXAMPLE |
| `packages/openai/src/responses/__fixtures__/openai-compaction.1.json` | 36 | `encrypted_content: "gAAAAABplLP7..."` (Fernet test fixture) | TEST_OR_EXAMPLE |

#### INTERESTING (security-relevant config, supply-chain signals)
| File | Line | Finding | Why Interesting |
|------|------|---------|-----------------|
| `packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166,171 | `deniedCIDRs: ['169.254.169.254/32']`, `subnets: { deny: ['169.254.169.254/32'] }` | Explicit SSRF protection blocking cloud metadata IP in test config — shows awareness |
| `pnpm-lock.yaml` | 289,291,2368 | `@ai-sdk/gladia` linked as local package `packages/gladia` | Confirms official Gladia provider in Vercel AI SDK monorepo (supply-chain surface) |
| `tsconfig.json` | 70 | `"path": "packages/gladia"` | TypeScript path mapping for Gladia provider package |
| `tools/analyze-downloads/src/analyze-providers.ts` | 21 | `'@ai-sdk/gladia'` in provider analysis | Gladia tracked in provider analytics |
| `.github/tigent.yml` | 30 | `provider/gladia` absent from list (only openai, anthropic, google, etc.) | Gladia not in CI test matrix — potential coverage gap |

#### ENDPOINT_LEAK / REAL_SECRET
| Category | Count |
|----------|-------|
| REAL_SECRET | 0 |
| ENDPOINT_LEAK | 0 |

---

### VERDICT LIST

| Candidate | REPORT_CANDIDATE | Rationale |
|-----------|------------------|-----------|
| Hardcoded secrets in test files | **no** | All `apiKey: 'test-api-key'`, `secret123`, `mocked-token` etc. are in `*.test.ts` or `__fixtures__/` — standard test fixtures, no signs of life |
| Fernet `encrypted_content` fixture | **no** | `gAAAAA...` prefix = Fernet test vector in `__fixtures__/openai-compaction.1.json`, not a real secret |
| SSRF protection config (`169.254.169.254/32`) | **no** | Defensive config in test (`vercel-sandbox.test.ts`), not a vulnerability |
| `@ai-sdk/gladia` in vercel-ai monorepo | **no** | Already documented in RAG as "official org integration; supply-chain repo surface stat" — known, not new |
| Gladia absent from `.github/tigent.yml` test matrix | **no** | Coverage gap, not a security issue |

**NO REPORTABLE CANDIDATES THIS SCAN** — all hits are test fixtures or known supply-chain artifacts.
