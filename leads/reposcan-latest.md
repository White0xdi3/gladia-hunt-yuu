
===== REPOSCAN 2026-10-06 10:30:13 UTC =====
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
## Classification Tables

### REAL_SECRET
| File | Line | SHA256(prefix) | Notes |
|------|------|----------------|-------|
| *(none)* | | | No hardcoded live credentials found |

### TEST_OR_EXAMPLE
| File | Line | Pattern | Context |
|------|------|---------|---------|
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | `client_secret: 'secret123'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | `access_token: 'access123'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | `refresh_token: 'refresh123'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | `access_token: 'expired-access-token'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | `refresh_token: 'rotating-refresh-token'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/openai/**/*.test.ts | 15+ | `apiKey: 'test-api-key'` | Test fixtures (all OpenAI provider tests) |
| reposcan-raw/gladiaio/vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13, 277 | `apiKey: 'test-api-key'` | Test fixtures |
| reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/togetherai-provider.test.ts | 99, 112, 165 | `apiKey: 'custom-key'`, `apiKey: 'explicit-key'` | Test fixtures |
| reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/reranking/togetherai-reranking-model.test.ts | 7 | `apiKey: 'test-api-key'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/**/*.test.ts | 5+ | `apiKey: 'test-api-key'`, `token: 'mocked-token'`, `access_token: 'mock.jwt.token'`, `private_key: 'invalid-key'` | Test fixtures/mocks |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/**/*.test.ts | 128+ | `sessionToken: 'dynamic-session-token'`, `sessionToken: 'static-session-token'`, `sessionToken: 'test-session-token'`, `sessionToken: 'async-session-token'`, `apiKey: 'test-api-key-123'`, `apiKey: 'test-api-key'`, `nextToken: 'test-token'` | Test fixtures |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts | 48 | `apiKey: 'your-api-key-here'` | Inline documentation example (comment) |
| reposcan-raw/gladiaio/vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json | 36 | `encrypted_content: "gAAAAABplLP7..."` | Test fixture (Fernet-encrypted blob) |

### ENDPOINT_LEAK
| File | Line | Value | Notes |
|------|------|-------|-------|
| *(none)* | | | No internal/dev/staging endpoints leaked |

### INTERESTING
| File | Line | Finding | Risk Note |
|------|------|---------|-----------|
| reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166, 171 | `deniedCIDRs: ['169.254.169.254/32']`, `subnets: { deny: ['169.254.169.254/32'] }` | **Positive**: Actively blocking AWS/GCP metadata endpoint in sandbox tests — SSRF mitigation present |
| reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml | 289, 291, 2368 | `@ai-sdk/gladia` linked as local package | Confirms `@ai-sdk/gladia` = official Vercel AI SDK integration (per RAG) |
| reposcan-raw/gladiaio/vercel-ai/tools/analyze-downloads/src/analyze-providers.ts | 21 | `'@ai-sdk/gladia'` import | Provider analysis includes Gladia |
| reposcan-raw/gladiaio/vercel-ai/.github/tigent.yml | 30 | Provider list includes openai, anthropic, google, azure, bedrock, xai, mistral, cohere, groq, deepseek, fireworks | CI tests multi-provider matrix |

---

## Verdict List

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Hardcoded secrets in test files | **no** | All are obvious test fixtures (`test-api-key`, `secret123`, `mocked-token`, etc.) |
| `@ai-sdk/gladia` in vercel-ai | **no** | Official integration confirmed by RAG; local package link in monorepo |
| SSRF metadata blocking in sandbox tests | **no** | Defensive control — **good practice**, not a finding |
| `gladia` npm package (0.1.3, maintainer softwarecitadel) | **no** | Already tracked in RAG as unofficial/personal repo; not in gladiaio/ org |
| OpenAPI/endpoint leaks | **no** | None found in this scan |

**Overall**: No reportable findings this cycle. All hits are test fixtures, documentation examples, or positive security controls (metadata endpoint blocking). The `@ai-sdk/gladia` integration is official per RAG.
