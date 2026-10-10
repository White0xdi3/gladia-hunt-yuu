
===== REPOSCAN 2026-10-10 00:51:21 UTC =====
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
### TEST_OR_EXAMPLE (55 hits)
| File | Line | Pattern | Classification |
|------|------|---------|----------------|
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | `client_secret: 'secret123'` | Test fixture |
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | `access_token: 'access123'` | Test fixture |
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | `refresh_token: 'refresh123'` | Test fixture |
| vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | `access_token: 'expired-access-token'` | Test fixture |
| vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | `refresh_token: 'rotating-refresh-token'` | Test fixture |
| vercel-ai/packages/openai/src/openai-provider.test.ts | 48,66,84 | `apiKey: 'test-api-key'` | Test fixture |
| vercel-ai/packages/openai/src/files/openai-files.test.ts | 40,61,78 | `apiKey: 'test-api-key'` | Test fixture |
| vercel-ai/packages/openai/src/image/openai-image-model.test.ts | 14,114 | `apiKey: 'test-api-key'` | Test fixture |
| vercel-ai/packages/openai/src/chat/openai-chat-language-model.test.ts | 113,778,3310 | `apiKey: 'test-api-key'` | Test fixture |
| vercel-ai/packages/openai/src/completion/openai-completion-language-model.test.ts | 45,246,381 | `apiKey: 'test-api-key'` | Test fixture |
| vercel-ai/packages/openai/src/speech/openai-speech-model.test.ts | 10,54 | `apiKey: 'test-api-key'` | Test fixture |
| vercel-ai/packages/openai/src/skills/openai-skills.test.ts | 12 | `apiKey: 'test-api-key'` | Test fixture |
| vercel-ai/packages/openai/src/transcription/openai-transcription-model.test.ts | 17,73 | `apiKey: 'test-api-key'` | Test fixture |
| vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13,277 | `apiKey: 'test-api-key'` | Test fixture |
| vercel-ai/packages/togetherai/src/togetherai-provider.test.ts | 99,112,165 | `apiKey: 'custom-key'/'explicit-key'` | Test fixture |
| vercel-ai/packages/togetherai/src/reranking/togetherai-reranking-model.test.ts | 7 | `apiKey: 'test-api-key'` | Test fixture |
| vercel-ai/packages/google-vertex/src/google-vertex-provider.test.ts | 120 | `apiKey: 'test-api-key'` | Test fixture |
| vercel-ai/packages/google-vertex/src/google-vertex-provider-base.test.ts | 187,405,419 | `apiKey: 'test-api-key'` | Test fixture |
| vercel-ai/packages/google-vertex/src/google-vertex-auth-google-auth-library.test.ts | 5,21 | `token: 'mocked-token'` | Test mock |
| vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts | 68,150 | `access_token: 'mock.jwt.token'` | Test mock |
| vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts | 134 | `private_key: 'invalid-key'` | Test fixture |
| vercel-ai/packages/google-vertex/src/edge/google-vertex-provider-edge.test.ts | 95 | `apiKey: 'test-api-key'` | Test fixture |
| vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.test.ts | 128,152,158 | `sessionToken: 'dynamic-session-token'/'static-session-token'` | Test fixture |
| vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts | 48 | `apiKey: 'your-api-key-here'` | Doc comment example |
| vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-sigv4-fetch.test.ts | 100,331,442 | `sessionToken: 'test-session-token'/'async-session-token'`, `apiKey: 'test-api-key-123'` | Test fixture |
| vercel-ai/packages/amazon-bedrock/src/mantle/bedrock-mantle-provider.test.ts | 209 | `apiKey: 'test-api-key'` | Test fixture |
| vercel-ai/packages/amazon-bedrock/src/reranking/amazon-bedrock-reranking-model.test.ts | 55 | `nextToken: 'test-token'` | Test fixture |
| vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json | 36 | `encrypted_content: "gAAAAABplLP..."` | Test vector/fixture |

### INTERESTING (4 hits)
| File | Line | Pattern | Note |
|------|------|---------|------|
| vercel-ai/pnpm-lock.yaml | 289,291,2368 | `@ai-sdk/gladia` package linked | Official Vercel AI SDK integration (RAG confirmed) |
| vercel-ai/tsconfig.json | 70 | `"path": "packages/gladia"` | Local package alias |
| vercel-ai/.github/tigent.yml | 30 | Provider list incl. gladia | CI config |
| vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166,171 | `deniedCIDRs: ['169.254.169.254/32']` | **Security control** — explicitly blocks cloud metadata IP (good) |

### REAL_SECRET
*None*

### ENDPOINT_LEAK
*None*

---

### VERDICT

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| All test fixtures/mocks | **no** | Clearly test data in `.test.ts` / `__fixtures__` — placeholder values (`test-api-key`, `secret123`, `mocked-token`) |
| `@ai-sdk/gladia` in vercel-ai | **no** | Official org integration per RAG; supply-chain surface stat only |
| Sandbox metadata IP deny rule | **no** | Defensive control (blocks 169.254.169.254), not a vulnerability |
| npm `gladia` 0.1.3 (unofficial) | **no** | Already tracked in RAG (orphaned personal repo, shasum unchanged) |

**No reportable findings this cycle.** Passive recon remains exhausted per RAG.
