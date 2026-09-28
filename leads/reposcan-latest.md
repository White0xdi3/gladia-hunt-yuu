
===== REPOSCAN 2026-09-28 01:43:34 UTC =====
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

#### REAL_SECRET
| File | Line | SHA256(secret) | Notes |
|------|------|----------------|-------|
| *none* | — | — | No live credentials found |

#### TEST_OR_EXAMPLE
| File | Line | Pattern | Context |
|------|------|---------|---------|
| vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166, 171 | `169.254.169.254/32` | **Defensive** — denied CIDRs in sandbox tests (SSRF protection) |
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740, 905, 908 | `secret123`, `access123`, `refresh123` | Test fixtures |
| vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409, 411 | `expired-access-token`, `rotating-refresh-token` | Test fixtures |
| vercel-ai/packages/openai/src/**/*.test.ts | many | `test-api-key` | Test fixtures (OpenAI provider) |
| vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13, 277 | `test-api-key` | Test fixtures |
| vercel-ai/packages/togetherai/src/*.test.ts | 99, 112, 165, 7 | `custom-key`, `explicit-key`, `test-api-key` | Test fixtures |
| vercel-ai/packages/google-vertex/src/*.test.ts | 120, 187, 405, 419, 68, 134, 150, 95 | `test-api-key`, `invalid-key`, `mock.jwt.token` | Test fixtures |
| vercel-ai/packages/amazon-bedrock/src/*.test.ts | 128, 152, 158, 100, 331, 442, 209, 55 | `dynamic-session-token`, `static-session-token`, `test-api-key-123`, `test-session-token`, `async-session-token`, `test-token` | Test fixtures |
| vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts | 48 | `your-api-key-here` | Documentation placeholder in source |

#### ENDPOINT_LEAK
| File | Line | Endpoint | Notes |
|------|------|----------|-------|
| *none* | — | — | Metadata IP only appears in **deny-lists** |

#### INTERESTING
| File | Line | Finding | Risk |
|------|------|---------|------|
| vercel-ai/pnpm-lock.yaml | 289, 291, 2368 | `@ai-sdk/gladia` linked as local package `packages/gladia` | Official Vercel AI SDK integration (confirmed in RAG) |
| vercel-ai/tools/analyze-downloads/src/analyze-providers.ts | 21 | Imports `@ai-sdk/gladia` | Usage confirmation |
| vercel-ai/.github/tigent.yml | 30 | Lists `provider/gladia` among providers | CI awareness |
| npm `gladia` 0.1.3 | — | Description "Official" but README "Unofficial"; owner `alexisbouchez` (personal) | **Supply-chain note** — already in RAG as ACCEPTED OTHER@sdk |

---

### Verdict

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Hardcoded secrets in test files | **no** | All `test-*`, `mock-*`, `secret123`, `invalid-key` — fixtures |
| `169.254.169.254` references | **no** | Appear only in **deny-lists** (SSRF defense) |
| `@ai-sdk/gladia` in vercel-ai | **no** | Official integration, not a vulnerability |
| npm `gladia` package discrepancy | **no** | Already tracked in RAG (ACCEPTED OTHER@sdk) |

**No reportable findings this cycle.** Delta = 0 new hits; full grep = 100% test fixtures / defensive code / known supply-chain note.
