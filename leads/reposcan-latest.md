
===== REPOSCAN 2026-10-14 13:45:33 UTC =====
## Grep hits:
SCAN SUMMARY: 5694 code/config files scanned, 657 hits
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
| File | Line | Classification | SHA256 (truncated) |
|------|------|----------------|-------------------|
| *none* | — | — | — |

#### TEST_OR_EXAMPLE
| File | Line | Pattern | Notes |
|------|------|---------|-------|
| `packages/mcp/src/tool/oauth.test.ts` | 740 | `client_secret: 'secret123'` | Test file, obviously fake |
| `packages/mcp/src/tool/oauth.test.ts` | 905 | `access_token: 'access123'` | Test file |
| `packages/mcp/src/tool/oauth.test.ts` | 908 | `refresh_token: 'refresh123'` | Test file |
| `packages/mcp/src/tool/mcp-http-transport.test.ts` | 409 | `access_token: 'expired-access-token'` | Test file |
| `packages/mcp/src/tool/mcp-http-transport.test.ts` | 411 | `refresh_token: 'rotating-refresh-token'` | Test file |
| `packages/openai/**/*.test.ts` | 15+ locations | `apiKey: 'test-api-key'` | All in test files |
| `packages/assemblyai/src/assemblyai-transcription-model.test.ts` | 13, 277 | `apiKey: 'test-api-key'` | Test file |
| `packages/togetherai/src/**/*.test.ts` | 4 locations | `apiKey: 'custom-key'`, `'explicit-key'`, `'test-api-key'` | Test files |
| `packages/google-vertex/src/**/*.test.ts` | 6 locations | `apiKey: 'test-api-key'`, `token: 'mocked-token'`, `'mock.jwt.token'`, `'invalid-key'` | Test files, mocks |
| `packages/amazon-bedrock/src/**/*.test.ts` | 6 locations | `sessionToken: 'dynamic-session-token'`, `'static-session-token'`, `'test-session-token'`, `'async-session-token'`, `apiKey: 'test-api-key-123'`, `'test-api-key'`, `nextToken: 'test-token'` | Test files |
| `packages/amazon-bedrock/src/amazon-bedrock-provider.ts` | 48 | `apiKey: 'your-api-key-here'` | Inline doc placeholder (non-test but clearly example) |
| `packages/openai/src/responses/__fixtures__/openai-compaction.1.json` | 36 | `encrypted_content: "gAAAAABplLP7..."` | Test fixture / test vector |

#### ENDPOINT_LEAK
| File | Line | Content | Notes |
|------|------|---------|-------|
| *none* | — | — | No internal/staging endpoints leaked |

#### INTERESTING
| File | Line | Content | Why Interesting |
|------|------|---------|-----------------|
| `packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166, 171 | `deniedCIDRs: ['169.254.169.254/32']`, `subnets: { deny: ['169.254.169.254/32'] }` | **SSRF protection actively blocking cloud metadata IP** — good security control, not a vuln |
| `pnpm-lock.yaml` | 289, 291, 2368 | `@ai-sdk/gladia`, `link:../../packages/gladia` | Confirms **official Vercel AI SDK integration** for Gladia (`@ai-sdk/gladia` is the official package) |
| `tsconfig.json` | 70 | `"path": "packages/gladia"` | Monorepo structure for Gladia provider |
| `.github/tigent.yml` | 30 | Lists 11 providers (openai, anthropic, google, vertex, azure, bedrock, xai, mistral, cohere, groq, deepseek, fireworks) | Shows vercel-ai is a multi-provider SDK, Gladia is one of many |
| `tools/analyze-downloads/src/analyze-providers.ts` | 21 | `'@ai-sdk/gladia'` | Download analytics for the Gladia provider |

---

### Verdict

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Hardcoded secrets in test files | **NO** | All values are obvious placeholders (`test-api-key`, `secret123`, `mocked-token`, `mock.jwt.token`) in `*.test.ts` or `__fixtures__/` |
| SSRF protection (169.254.169.254 deny list) | **NO** | This is a **defensive control**, not a vulnerability |
| `@ai-sdk/gladia` package reference | **NO** | Confirmed official integration (per RAG: `vercel-ai @ai-sdk/gladia = official org integration`) |
| Orphaned `gladia@0.1.3` npm package | **NO** | Already tracked in RAG as `[ACCEPTED] AUTH@sdk` — supply-chain key theft vector, known alive |

**No new reportable findings this cycle.** The scan surface is the `vercel-ai` fork/integration repo — all hits are test fixtures or expected configuration. The only Gladia-specific signal is the confirmed official `@ai-sdk/gladia` provider.
