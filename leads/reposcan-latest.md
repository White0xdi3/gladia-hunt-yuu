
===== REPOSCAN 2026-09-28 08:47:00 UTC =====
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
## Classification Results

### REAL_SECRET
| File | Line | SHA256 (first 16) | Context |
|------|------|-------------------|---------|
| *none found* | | | |

### TEST_OR_EXAMPLE (59 hits)
| File | Line | Pattern | Classification |
|------|------|---------|----------------|
| `vercel-ai/packages/mcp/src/tool/oauth.test.ts` | 740 | `client_secret: 'secret123'` | Test fixture |
| `vercel-ai/packages/mcp/src/tool/oauth.test.ts` | 905 | `access_token: 'access123'` | Test fixture |
| `vercel-ai/packages/mcp/src/tool/oauth.test.ts` | 908 | `refresh_token: 'refresh123'` | Test fixture |
| `vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts` | 409 | `access_token: 'expired-access-token'` | Test fixture |
| `vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts` | 411 | `refresh_token: 'rotating-refresh-token'` | Test fixture |
| `vercel-ai/packages/openai/src/**/*.test.ts` | 22 locations | `apiKey: 'test-api-key'` | Test fixture |
| `vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts` | 13, 277 | `apiKey: 'test-api-key'` | Test fixture |
| `vercel-ai/packages/togetherai/src/*.test.ts` | 4 locations | `apiKey: 'custom-key'`, `'explicit-key'` | Test fixture |
| `vercel-ai/packages/google-vertex/src/*.test.ts` | 7 locations | `apiKey: 'test-api-key'`, `token: 'mocked-token'`, `'mock.jwt.token'`, `'invalid-key'` | Test fixture |
| `vercel-ai/packages/amazon-bedrock/src/*.test.ts` | 7 locations | `sessionToken: 'dynamic-session-token'`, `'static-session-token'`, `'test-session-token'`, `'async-session-token'`, `apiKey: 'test-api-key-123'`, `nextToken: 'test-token'` | Test fixture |
| `vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts` | 48 | `apiKey: 'your-api-key-here'` | Doc example |
| `vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json` | 36 | `encrypted_content: "gAAAAABplLP..."` | Test fixture (encrypted) |

### ENDPOINT_LEAK
| File | Line | Detail |
|------|------|--------|
| *none found* | | |

### INTERESTING
| File | Line | Detail |
|------|------|--------|
| `vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166, 171 | SSRF protection: `deniedCIDRs: ['169.254.169.254/32']` — explicit cloud metadata blocking |
| `vercel-ai/pnpm-lock.yaml` | 289, 291, 2368 | `@ai-sdk/gladia` linked as local package — official Vercel AI SDK integration |
| `vercel-ai/tsconfig.json` | 70 | Path alias for `packages/gladia` |
| `vercel-ai/.github/tigent.yml` | 30 | Gladia listed as supported provider in CI config |

---

## Verdict

**REPORT_CANDIDATE: no**

**Summary**: Zero real secrets. All 652 hits are test fixtures (`test-api-key`, `secret123`, `mocked-token`, etc.), documentation placeholders (`your-api-key-here`), or configuration references. The only security-relevant finding is **positive**: the Vercel sandbox tests explicitly deny `169.254.169.254/32` (AWS/GCP/Azure metadata endpoint), showing SSRF mitigation awareness.

The `@ai-sdk/gladia` package in `vercel-ai` is the official Vercel AI SDK provider for Gladia (confirmed in RAG), not a supply-chain risk.
