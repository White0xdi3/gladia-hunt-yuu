
===== REPOSCAN 2026-09-30 16:00:48 UTC =====
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
### Classification Tables

#### TEST_OR_EXAMPLE (56 hits)
| File | Line | Pattern | Classification |
|------|------|---------|----------------|
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | `client_secret: 'secret123'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | `access_token: 'access123'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | `refresh_token: 'refresh123'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | `access_token: 'expired-access-token'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | `refresh_token: 'rotating-refresh-token'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/openai/src/openai-provider.test.ts | 48,66,84 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/openai/src/files/openai-files.test.ts | 40,61,78 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/openai/src/image/openai-image-model.test.ts | 14,114 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/openai/src/chat/openai-chat-language-model.test.ts | 113,778,3310 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/openai/src/completion/openai-completion-language-model.test.ts | 45,246,381 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/openai/src/speech/openai-speech-model.test.ts | 10,54 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/openai/src/skills/openai-skills.test.ts | 12 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/openai/src/transcription/openai-transcription-model.test.ts | 17,73 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13,277 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/togetherai/src/togetherai-provider.test.ts | 99,112,165 | `apiKey: 'custom-key'/'explicit-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/togetherai/src/reranking/togetherai-reranking-model.test.ts | 7 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/google-vertex/src/google-vertex-provider.test.ts | 120 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/google-vertex/src/google-vertex-provider-base.test.ts | 187,405,419 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/google-vertex/src/google-vertex-auth-google-auth-library.test.ts | 5,21 | `token: 'mocked-token'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts | 68,150 | `access_token: 'mock.jwt.token'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts | 134 | `private_key: 'invalid-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/google-vertex/src/edge/google-vertex-provider-edge.test.ts | 95 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.test.ts | 128,152,158 | `sessionToken: 'dynamic-session-token'/'static-session-token'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts | 48 | `apiKey: 'your-api-key-here'` (doc comment) | TEST_OR_EXAMPLE |
| vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-sigv4-fetch.test.ts | 100,331,442 | `sessionToken: 'test-session-token'/'async-session-token'`, `apiKey: 'test-api-key-123'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/amazon-bedrock/src/mantle/bedrock-mantle-provider.test.ts | 209 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE |
| vercel-ai/packages/amazon-bedrock/src/reranking/amazon-bedrock-reranking-model.test.ts | 55 | `nextToken: 'test-token'` | TEST_OR_EXAMPLE |

#### INTERESTING (2 hits)
| File | Line | Pattern | Note |
|------|------|---------|------|
| vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166 | `deniedCIDRs: ['169.254.169.254/32']` | Explicit SSRF protection blocking AWS/GCP metadata endpoint |
| vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 171 | `subnets: { deny: ['169.254.169.254/32'] }` | Duplicate SSRF protection config |

#### ENDPOINT_LEAK (0 hits)
No internal/dev/staging URLs or API endpoints leaked beyond test fixtures.

#### REAL_SECRET (0 hits)
No hardcoded credentials with signs of life. All secrets are obvious test fixtures (`test-api-key`, `secret123`, `mocked-token`, etc.).

---

### Verdict

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| SSRF protection in vercel-sandbox | **no** | Defensive control, not a vulnerability |
| npm `gladia` 0.1.3 (alexisbouchez) claiming "Official" | **no** | Known from prior cycle (RAG: `OTHER@sdk` accepted 2026-09-30) — orphaned personal repo, misleading but not a secret leak |
| All test fixtures | **no** | Clearly fake values in `.test.ts` files |

**No new reportable findings this cycle.** The vercel-ai repo is the Vercel AI SDK monorepo (official `@ai-sdk/gladia` integration), not a Gladia-owned repo — its test fixtures are expected noise.
