
===== REPOSCAN 2026-09-29 09:57:29 UTC =====
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
### REAL_SECRET
| File | Line | SHA256(prefix) | Context |
|------|------|----------------|---------|
| *(none)* | — | — | No live credentials found |

### TEST_OR_EXAMPLE
| File | Line | Pattern | Verdict |
|------|------|---------|---------|
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | client_secret: 'secret123' | Test fixture |
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | access_token: 'access123' | Test fixture |
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | refresh_token: 'refresh123' | Test fixture |
| vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | access_token: 'expired-access-token' | Test fixture |
| vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | refresh_token: 'rotating-refresh-token' | Test fixture |
| vercel-ai/packages/openai/**/*.test.ts | 30+ | apiKey: 'test-api-key*' | Test fixtures (30 occurrences) |
| vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13,277 | apiKey: 'test-api-key' | Test fixtures |
| vercel-ai/packages/togetherai/src/togetherai-provider.test.ts | 99,112,165 | apiKey: 'custom-key'/'explicit-key' | Test fixtures |
| vercel-ai/packages/google-vertex/**/*.test.ts | 120,187,405,419 | apiKey: 'test-api-key' | Test fixtures |
| vercel-ai/packages/google-vertex/**/*.test.ts | 5,21,68,134,150 | token: 'mocked-token'/'mock.jwt.token'/'invalid-key' | Test fixtures |
| vercel-ai/packages/amazon-bedrock/**/*.test.ts | 128,152,158,100,331,442,209 | sessionToken/apiKey: 'test-*'/'dynamic-*'/'static-*' | Test fixtures |
| vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts | 48 | apiKey: 'your-api-key-here' | Doc placeholder |
| vercel-ai/packages/amazon-bedrock/src/reranking/amazon-bedrock-reranking-model.test.ts | 55 | nextToken: 'test-token' | Test fixture |
| vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json | 36 | encrypted_content: "gAAAAAB..." | Test fixture (encrypted) |

### ENDPOINT_LEAK
| File | Line | Leak Type | Verdict |
|------|------|-----------|---------|
| *(none)* | — | — | No internal endpoints leaked |

### INTERESTING
| File | Line | Finding | Risk Note |
|------|------|---------|-----------|
| vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166,171 | `deniedCIDRs: ['169.254.169.254/32']` + `subnets: { deny: ['169.254.169.254/32'] }` | **SSRF defense present** — explicitly blocks AWS/GCP/Azure metadata IP in sandbox tests |
| vercel-ai/pnpm-lock.yaml | 289-291, 2368 | `@ai-sdk/gladia` linked as `link:../../packages/gladia` | Local package, not published — supply-chain surface |
| vercel-ai/tsconfig.json | 70 | `"path": "packages/gladia"` | Monorepo path alias for @ai-sdk/gladia |
| npm `gladia` 0.1.3 (external) | — | Registry: "Official TypeScript SDK" vs README: "Unofficial TypeScript SDK"; maintainer `softwarecitadel@gmail.com` (personal), repo `alexisbouchez/gladia.ts` (404) | **Supply-chain anomaly** — misleading official claim, orphaned personal repo |

---

### VERDICT

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Hardcoded secrets in test files | **no** | All are obvious test fixtures (`test-api-key`, `secret123`, `mock.jwt.token`) |
| SSRF metadata IP in sandbox tests | **no** | Defensive control (deny list), not a vulnerability |
| `@ai-sdk/gladia` local package | **no** | Internal monorepo link, not deployed |
| npm `gladia` 0.1.3 package metadata mismatch | **yes** | **Supply-chain risk**: Package claims "Official" but is unofficial/personal; registry description vs README conflict; maintainer uses personal email; GitHub repo 404. Report via program disclosure channel. |
