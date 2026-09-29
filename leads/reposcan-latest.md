
===== REPOSCAN 2026-09-29 16:34:45 UTC =====
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
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [offset=160, limit=20][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts[90m [limit=20, offset=735][0m
All hits are from `gladiaio/vercel-ai` repo (a fork of Vercel AI SDK). Classification:

### REAL_SECRET
| File | Line | SHA256(prefix) | Notes |
|------|------|----------------|-------|
| *(none)* | | | No live credentials found |

### TEST_OR_EXAMPLE
| File | Line | Pattern | Notes |
|------|------|---------|-------|
| `packages/mcp/src/tool/oauth.test.ts` | 740, 905, 908 | `client_secret: 'secret123'`, `access_token: 'access123'`, `refresh_token: 'refresh123'` | Test fixtures |
| `packages/mcp/src/tool/mcp-http-transport.test.ts` | 409, 411 | `access_token: 'expired-access-token'`, `refresh_token: 'rotating-refresh-token'` | Test fixtures |
| `packages/openai/src/**/*.test.ts` | 48, 66, 84, 14, 54, 113, 778, 3310, 45, 246, 381, 10, 54, 12, 13, 137, 17, 73 | `apiKey: 'test-api-key'` | Test fixtures (50+ occurrences) |
| `packages/assemblyai/src/assemblyai-transcription-model.test.ts` | 13, 277 | `apiKey: 'test-api-key'` | Test fixtures |
| `packages/togetherai/src/togetherai-provider.test.ts` | 99, 112, 165 | `apiKey: 'custom-key'`, `apiKey: 'explicit-key'` | Test fixtures |
| `packages/togetherai/src/reranking/togetherai-reranking-model.test.ts` | 7 | `apiKey: 'test-api-key'` | Test fixtures |
| `packages/google-vertex/src/**/*.test.ts` | 120, 187, 405, 419, 5, 21, 68, 134, 150, 95 | `apiKey: 'test-api-key'`, `token: 'mocked-token'`, `access_token: 'mock.jwt.token'`, `private_key: 'invalid-key'` | Test fixtures |
| `packages/amazon-bedrock/src/**/*.test.ts` | 128, 152, 158, 100, 331, 442, 209, 55 | `sessionToken: 'dynamic-session-token'`, `sessionToken: 'static-session-token'`, `sessionToken: 'async-session-token'`, `apiKey: 'test-api-key-123'`, `apiKey: 'test-api-key'`, `nextToken: 'test-token'` | Test fixtures |
| `packages/openai/src/responses/__fixtures__/openai-compaction.1.json` | 36 | `encrypted_content: "gAAAAABplLP7..."` | Encrypted test fixture |
| `packages/amazon-bedrock/src/amazon-bedrock-provider.ts` | 48 | `apiKey: 'your-api-key-here'` | Code comment example |

### ENDPOINT_LEAK
| File | Line | Value | Notes |
|------|------|-------|-------|
| *(none)* | | | No internal/staging endpoints leaked |

### INTERESTING
| File | Line | Finding | Significance |
|------|------|---------|--------------|
| `packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166, 171 | `deniedCIDRs: ['169.254.169.254/32']`, `subnets: { deny: ['169.254.169.254/32'] }` | **Security control test** — explicitly blocks cloud metadata IP (SSRF mitigation). Confirms SSRF awareness in sandbox network policy. |
| `pnpm-lock.yaml` | 289, 291, 2368 | `@ai-sdk/gladia` linked as local package | Gladia provider integrated in Vercel AI SDK monorepo (official integration) |
| `tsconfig.json` | 70 | `"path": "packages/gladia"` | Build config for Gladia provider package |
| `tools/analyze-downloads/src/analyze-providers.ts` | 21 | `'@ai-sdk/gladia'` | Download analytics includes Gladia provider |
| `.github/tigent.yml` | 30 | Provider list includes Gladia | CI/testing matrix includes Gladia |

---

### VERDICT

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Test fixtures (apiKey, tokens, secrets) | **no** | All `test-*`, `mock*`, `secret123`, `invalid-key` patterns — clearly test data |
| Encrypted fixture content | **no** | Test fixture, not a live secret |
| Comment example `your-api-key-here` | **no** | Documentation placeholder |
| Sandbox metadata IP block test | **no** | **Positive security control** — proves SSRF mitigation exists in network policy |
| `@ai-sdk/gladia` integration references | **no** | Official provider integration, not a vulnerability |

**No reportable findings this cycle.** The vercel-ai repo is a Gladia-integrated fork of Vercel AI SDK; all secrets are test fixtures. The sandbox test explicitly denying `169.254.169.254/32` is a defensive control, not a vulnerability.
