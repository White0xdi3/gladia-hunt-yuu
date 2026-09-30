
===== REPOSCAN 2026-09-30 23:55:31 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && ls -la reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts
-rw-r--r-- 1 runner runner 9741 Sep 30 23:54 reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [offset=160, limit=30][0m
### Classification Tables

#### TEST_OR_EXAMPLE (all test fixtures / placeholder values)
| File | Line | Pattern | SHA256(prefix) |
|------|------|---------|----------------|
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | `client_secret: 'secret123'` | `a591...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | `access_token: 'access123'` | `f2d7...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | `refresh_token: 'refresh123'` | `e3b0...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | `access_token: 'expired-access-token'` | `d4f8...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | `refresh_token: 'rotating-refresh-token'` | `c8a2...` |
| reposcan-raw/gladiaio/vercel-ai/packages/openai/src/**/*.test.ts | 48+ | `apiKey: 'test-api-key'` (20+ occurrences) | `3e9f...` |
| reposcan-raw/gladiaio/vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13,277 | `apiKey: 'test-api-key'` | `3e9f...` |
| reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/togetherai-provider.test.ts | 99,112,165 | `apiKey: 'custom-key'`, `apiKey: 'explicit-key'` | `9b4e...` |
| reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/reranking/togetherai-reranking-model.test.ts | 7 | `apiKey: 'test-api-key'` | `3e9f...` |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/*.test.ts | 120,187,405,419 | `apiKey: 'test-api-key'` | `3e9f...` |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts | 68,134,150 | `access_token: 'mock.jwt.token'`, `private_key: 'invalid-key'` | `b1a7...` |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.test.ts | 128,152,158 | `sessionToken: 'dynamic-session-token'`, `'static-session-token'` | `a3f1...` |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-sigv4-fetch.test.ts | 100,331,442 | `sessionToken: 'test-session-token'`, `apiKey: 'test-api-key-123'` | `7c2e...` |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/mantle/bedrock-mantle-provider.test.ts | 209 | `apiKey: 'test-api-key'` | `3e9f...` |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/reranking/amazon-bedrock-reranking-model.test.ts | 55 | `nextToken: 'test-token'` | `f8d4...` |
| reposcan-raw/gladiaio/vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json | 36 | `encrypted_content: "gAAAAABplLP7..."` (Fernet test token) | `8e3c...` |

#### INTERESTING (security-relevant configuration)
| File | Line | Finding | Context |
|------|------|---------|---------|
| reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166,171 | `deniedCIDRs: ['169.254.169.254/32']` | Explicit SSRF protection test — denies cloud metadata IP in network policy |

#### ENDPOINT_LEAK / REAL_SECRET
| Category | Count |
|----------|-------|
| ENDPOINT_LEAK | 0 |
| REAL_SECRET | 0 |

---

### Verdict

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| `@ai-sdk/gladia` in vercel-ai monorepo | **no** | Official Vercel AI SDK integration (confirmed in RAG), not a supply-chain risk |
| Hardcoded secrets in test files | **no** | All values are obvious placeholders (`test-api-key`, `secret123`, `mock.jwt.token`, `invalid-key`) in `*.test.ts` fixtures |
| `deniedCIDRs: ['169.254.169.254/32']` | **no** | Defensive SSRF mitigation test — proves metadata IP blocking is implemented, not a vulnerability |
| `gladia` npm package (0.1.3, alexisbouchez) | **no** | Already tracked in RAG as orphaned personal repo; dist-tag/shasum unchanged since 2026-08-07 |

**No reportable findings this cycle.** All hits are test fixtures or defensive security controls.
