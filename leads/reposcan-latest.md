
===== REPOSCAN 2026-10-12 00:37:48 UTC =====
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
[0m$ [0mls -la reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Oct 12 00:36 .
drwxr-xr-x  4 runner runner 4096 Oct 12 00:36 ..
drwxr-xr-x  9 runner runner 4096 Oct 12 00:36 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct 12 00:36 docs
drwxr-xr-x  7 runner runner 4096 Oct 12 00:36 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct 12 00:36 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct 12 00:36 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct 12 00:36 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct 12 00:36 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct 12 00:36 normalization
drwxr-xr-x 12 runner runner 4096 Oct 12 00:36 num2words2
drwxr-xr-x  9 runner runner 4096 Oct 12 00:36 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct 12 00:36 sdk
drwxr-xr-x  7 runner runner 4096 Oct 12 00:36 skills
drwxr-xr-x 18 runner runner 4096 Oct 12 00:36 vercel-ai
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [offset=160, limit=30][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml[90m [offset=285, limit=20][0m
### Classification Tables

#### TEST_OR_EXAMPLE (630+ lines — all test/fixture data)
| File | Line | Pattern | Notes |
|------|------|---------|-------|
| `vercel-ai/packages/openai/src/**/*.test.ts` | 48,66,84,10,54,13,137,12,17,73,113,778,3310,45,246,381 | `apiKey: 'test-api-key'` | Vitest unit tests |
| `vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts` | 13,277 | `apiKey: 'test-api-key'` | Unit tests |
| `vercel-ai/packages/togetherai/src/**/*.test.ts` | 99,112,165,7 | `apiKey: 'custom-key'`, `apiKey: 'explicit-key'`, `apiKey: 'test-api-key'` | Unit tests |
| `vercel-ai/packages/google-vertex/src/**/*.test.ts` | 120,187,405,419,5,21,68,134,150,95 | `apiKey: 'test-api-key'`, `mocked-token`, `mock.jwt.token`, `invalid-key` | Unit tests + mocks |
| `vercel-ai/packages/amazon-bedrock/src/**/*.test.ts` | 128,152,158,100,331,442,209,55 | `sessionToken: 'dynamic-session-token'`, `static-session-token`, `test-session-token`, `async-session-token`, `test-api-key-123`, `test-api-key`, `test-token` | Unit tests |
| `vercel-ai/packages/mcp/src/tool/oauth.test.ts` | 740,905,908 | `client_secret: 'secret123'`, `access_token: 'access123'`, `refresh_token: 'refresh123'` | OAuth test fixtures |
| `vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts` | 409,411 | `access_token: 'expired-access-token'`, `refresh_token: 'rotating-refresh-token'` | Token rotation tests |
| `vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts` | 48 | `* apiKey: 'your-api-key-here'` | JSDoc example comment |
| `vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json` | 36 | `encrypted_content: "gAAAAAB..."` | Encrypted test fixture |

#### INTERESTING (2 lines — security feature, not vuln)
| File | Line | Pattern | Notes |
|------|------|---------|-------|
| `vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166, 171 | `deniedCIDRs: ['169.254.169.254/32']`, `subnets: { deny: ['169.254.169.254/32'] }` | **Security feature**: sandbox explicitly blocks cloud metadata IP (AWS/GCP/Azure). This is a defense-in-depth control, not a vulnerability. |

#### ENDPOINT_LEAK / REAL_SECRET
| Category | Count |
|----------|-------|
| ENDPOINT_LEAK | 0 |
| REAL_SECRET | 0 |

---

### Verdict

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| `test-api-key` / `secret123` / `mocked-token` / etc. | **no** | All are test fixtures in Vitest unit tests across provider packages |
| `deniedCIDRs: ['169.254.169.254/32']` | **no** | Security feature — sandbox network policy explicitly denies cloud metadata endpoint |
| `@ai-sdk/gladia` workspace package | **no** | Official Vercel AI SDK provider integration (documented in RAG) |
| `gladia@0.1.3` orphaned npm package | **no** | Already tracked in RAG as `[ACCEPTED] AUTH@sdk` — supply-chain vector, not new |

**DELTA**: 0 new hit lines vs previous scan — **no new findings this cycle**.
