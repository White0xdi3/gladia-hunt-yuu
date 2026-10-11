
===== REPOSCAN 2026-10-11 20:20:18 UTC =====
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
### Classification Tables

#### TEST_OR_EXAMPLE (56 hits)
| File | Line | Context |
|------|------|---------|
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740, 905, 908 | `client_secret: 'secret123'`, `access_token: 'access123'`, `refresh_token: 'refresh123'` |
| vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409, 411 | `access_token: 'expired-access-token'`, `refresh_token: 'rotating-refresh-token'` |
| vercel-ai/packages/openai/src/**/*.test.ts | 20+ lines | `apiKey: 'test-api-key'` (ubiquitous test fixture) |
| vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13, 277 | `apiKey: 'test-api-key'` |
| vercel-ai/packages/togetherai/src/**/*.test.ts | 4 lines | `apiKey: 'custom-key'`, `apiKey: 'explicit-key'`, `apiKey: 'test-api-key'` |
| vercel-ai/packages/google-vertex/src/**/*.test.ts | 8 lines | `apiKey: 'test-api-key'`, `token: 'mocked-token'`, `access_token: 'mock.jwt.token'`, `private_key: 'invalid-key'` |
| vercel-ai/packages/amazon-bedrock/src/**/*.test.ts | 7 lines | `sessionToken: 'dynamic-session-token'`, `sessionToken: 'static-session-token'`, `apiKey: 'test-api-key-123'`, `apiKey: 'test-api-key'`, `nextToken: 'test-token'` |
| vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts | 48 | JSDoc example: `* apiKey: 'your-api-key-here'` |

#### INTERESTING (7 hits)
| File | Line | Why |
|------|------|-----|
| vercel-ai/pnpm-lock.yaml | 289, 291, 2368 | `@ai-sdk/gladia` linked as local package — official Vercel AI SDK integration |
| vercel-ai/tsconfig.json | 70 | Path alias `"packages/gladia"` confirms monorepo structure |
| vercel-ai/tools/analyze-downloads/src/analyze-providers.ts | 21 | Provider analytics includes `@ai-sdk/gladia` |
| vercel-ai/.github/tigent.yml | 30 | CI matrix lists 11 providers including Gladia |
| vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166, 171 | **SSRF defense**: explicit `deny: ['169.254.169.254/32']` — metadata endpoint blocked |

#### REAL_SECRET: 0
#### ENDPOINT_LEAK: 0

---

### Verdict

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| All test fixtures | **no** | Clearly `.test.ts` files, placeholder values (`test-api-key`, `secret123`, `mocked-token`) |
| `@ai-sdk/gladia` integration | **no** | Official Vercel AI provider package, expected in `gladiaio/vercel-ai` monorepo |
| SSRF defense in sandbox tests | **no** | Positive security control (deny metadata IP), not a vulnerability |
| Orphaned `gladia@0.1.3` on npm | **already accepted** | Known supply-chain issue (RAG: `AUTH@sdk` ACCEPTED 2026-10-11) — no new evidence here |

**No new reportable findings this cycle.** The scan covers `gladiaio/vercel-ai` which is a **Vercel-owned integration repo** (not Gladia core), and all hits are test fixtures or expected integration metadata.
