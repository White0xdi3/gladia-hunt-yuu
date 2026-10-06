
===== REPOSCAN 2026-10-06 03:04:24 UTC =====
## Grep hits:
SCAN SUMMARY: 5695 code/config files scanned, 654 hits
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw -name "*.test.ts" -o -name "*.spec.ts" | head -20
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
### Classification Tables

#### TEST_OR_EXAMPLE (all hits — test/fixture data only)

| File | Line | Pattern | Context |
|------|------|---------|---------|
| vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166, 171 | `169.254.169.254/32` | SSRF test deny-list for cloud metadata IP |
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740, 905, 908 | `client_secret`, `access_token`, `refresh_token` | OAuth test fixtures (`secret123`, `access123`, `refresh123`) |
| vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409, 411 | `access_token`, `refresh_token` | Expired/rotating token test fixtures |
| vercel-ai/packages/openai/src/**/*.test.ts | 48, 66, 84, 14, 114, 778, 3310, 45, 246, 381, 10, 54, 12, 17, 73, 13, 137 | `test-api-key` | OpenAI provider test fixtures (20+ occurrences) |
| vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13, 277 | `test-api-key` | AssemblyAI test fixture |
| vercel-ai/packages/togetherai/src/togetherai-provider.test.ts | 99, 112, 165 | `custom-key`, `explicit-key`, `test-api-key` | TogetherAI test fixtures |
| vercel-ai/packages/google-vertex/src/*.test.ts | 120, 187, 405, 419, 5, 21, 68, 134, 150, 95 | `test-api-key`, `mocked-token`, `mock.jwt.token`, `invalid-key` | Google Vertex test fixtures |
| vercel-ai/packages/amazon-bedrock/src/*.test.ts | 100, 128, 152, 158, 331, 442, 209, 55 | `sessionToken`, `test-api-key`, `nextToken` | Bedrock test fixtures |

#### INTERESTING (config / supply-chain signals)

| File | Line | Pattern | Why Notable |
|------|------|---------|-------------|
| vercel-ai/pnpm-lock.yaml | 289, 291, 2368 | `@ai-sdk/gladia` version `link:../../packages/gladia` | Official Vercel AI SDK integration for Gladia (local workspace dep) |
| vercel-ai/tsconfig.json | 70 | `"path": "packages/gladia"` | Monorepo path alias for Gladia provider |
| vercel-ai/tools/analyze-downloads/src/analyze-providers.ts | 21 | `@ai-sdk/gladia` import | Download analytics includes Gladia provider |
| vercel-ai/.github/tigent.yml | 30 | Provider list includes gladia | CI test matrix includes Gladia |

---

### SHORT VERDICT LIST

| Candidate | Category | REPORT_CANDIDATE | Reason |
|-----------|----------|------------------|--------|
| All hardcoded `test-api-key`, `secret123`, `mock.jwt.token`, `169.254.169.254/32` | TEST_OR_EXAMPLE | **no** | Confined to `*.test.ts` fixtures; no production credentials |
| `@ai-sdk/gladia` workspace dependency | INTERESTING | **no** | Official Vercel AI SDK integration (confirmed in RAG); supply-chain transparency |
| `gladia` npm 0.1.3 (alexisbouchez personal repo) | INTERESTING | **no** | Already tracked in RAG as orphaned/irrevocable; not in gladiaio org |

**No REAL_SECRET or ENDPOINT_LEAK candidates this cycle.** All hits are test fixtures or expected monorepo config. Passive recon remains exhausted per RAG.
