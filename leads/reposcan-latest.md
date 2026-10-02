
===== REPOSCAN 2026-10-02 19:18:09 UTC =====
## Grep hits:
SCAN SUMMARY: 5693 code/config files scanned, 654 hits
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

#### TEST_OR_EXAMPLE (all hits — no real secrets)
| File | Line | Pattern | Verdict |
|------|------|---------|---------|
| `vercel-ai/packages/mcp/src/tool/oauth.test.ts` | 740, 905, 908 | `client_secret: 'secret123'`, `access_token: 'access123'`, `refresh_token: 'refresh123'` | Test fixtures |
| `vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts` | 409, 411 | `access_token: 'expired-access-token'`, `refresh_token: 'rotating-refresh-token'` | Test fixtures |
| `vercel-ai/packages/openai/src/**/*.test.ts` | 48, 66, 84, 40, 61, 78, 14, 114, 113, 778, 3310, 45, 246, 381, 10, 54, 12, 17, 73, 13, 137, 12 | `apiKey: 'test-api-key'` (30+ occurrences) | Test fixtures |
| `vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts` | 13, 277 | `apiKey: 'test-api-key'` | Test fixtures |
| `vercel-ai/packages/togetherai/src/**/*.test.ts` | 99, 112, 165, 7 | `apiKey: 'custom-key'`, `'explicit-key'`, `'test-api-key'` | Test fixtures |
| `vercel-ai/packages/google-vertex/src/**/*.test.ts` | 120, 187, 405, 419, 5, 21, 68, 134, 150, 95 | `apiKey: 'test-api-key'`, `token: 'mocked-token'`, `access_token: 'mock.jwt.token'`, `private_key: 'invalid-key'` | Test fixtures/mocks |
| `vercel-ai/packages/amazon-bedrock/src/**/*.test.ts` | 128, 152, 158, 100, 331, 442, 209, 55 | `sessionToken: 'dynamic-session-token'`, `'static-session-token'`, `'test-session-token'`, `'async-session-token'`, `apiKey: 'test-api-key-123'`, `'test-api-key'`, `nextToken: 'test-token'` | Test fixtures |
| `vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts` | 48 | `* apiKey: 'your-api-key-here'` | Doc comment example |

#### INTERESTING (config/security posture)
| File | Line | Finding |
|------|------|---------|
| `vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166, 171 | `deniedCIDRs: ['169.254.169.254/32']` — metadata endpoint explicitly blocked (good) |
| `vercel-ai/pnpm-lock.yaml` | 289, 291, 2368 | `@ai-sdk/gladia` linked as local package — official Vercel AI SDK integration confirmed |
| `vercel-ai/.github/tigent.yml` | 30 | Provider list includes Gladia among 11 providers — supply-chain visibility |

#### ENDPOINT_LEAK / REAL_SECRET
**None found.**

---

### Verdict List

| Candidate | Category | REPORT_CANDIDATE |
|-----------|----------|------------------|
| All `test-api-key` / `secret123` / `mocked-token` fixtures | TEST_OR_EXAMPLE | **no** |
| Sandbox metadata CIDR deny rules | INTERESTING (defensive) | **no** |
| `@ai-sdk/gladia` in vercel-ai monorepo | INTERESTING (official integration) | **no** |
| npm `gladia` 0.1.3 from `alexisbouchez` (personal) | KNOWN (orphaned) | **no** — already tracked in RAG |

**Overall: No new reportable findings this cycle. Delta = 0 new hits. All secrets are test fixtures. Defensive SSRF mitigation (169.254.169.254/32 deny) confirmed in vercel-ai sandbox tests.**
