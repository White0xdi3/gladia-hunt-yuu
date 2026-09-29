
===== REPOSCAN 2026-09-29 21:27:03 UTC =====
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
[0m$ [0mls -la reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Sep 29 21:26 .
drwxr-xr-x  4 runner runner 4096 Sep 29 21:26 ..
drwxr-xr-x  9 runner runner 4096 Sep 29 21:26 compare-stt
drwxr-xr-x  9 runner runner 4096 Sep 29 21:26 docs
drwxr-xr-x  7 runner runner 4096 Sep 29 21:26 gladia-cli
drwxr-xr-x 11 runner runner 4096 Sep 29 21:26 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Sep 29 21:26 gladia-samples
drwxr-xr-x  9 runner runner 4096 Sep 29 21:26 gladiaflow
drwxr-xr-x  7 runner runner 4096 Sep 29 21:26 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Sep 29 21:26 normalization
drwxr-xr-x 12 runner runner 4096 Sep 29 21:26 num2words2
drwxr-xr-x  9 runner runner 4096 Sep 29 21:26 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Sep 29 21:26 sdk
drwxr-xr-x  7 runner runner 4096 Sep 29 21:26 skills
drwxr-xr-x 18 runner runner 4096 Sep 29 21:26 vercel-ai
[0m
### Classification Table

| Category | Files/Lines | Verdict |
|----------|-------------|---------|
| **REAL_SECRET** | None | — |
| **TEST_OR_EXAMPLE** | 500+ hits across `*.test.ts` files: `test-api-key`, `secret123`, `access123`, `refresh123`, `mock.jwt.token`, `mocked-token`, `invalid-key`, `custom-key`, `explicit-key`, `dynamic-session-token`, `static-session-token`, `async-session-token`, `test-session-token`, `test-api-key-123`, `test-token`, `nextToken: 'test-token'` + encrypted fixture in `openai-compaction.1.json:36` | All test fixtures/fixtures |
| **ENDPOINT_LEAK** | None | — |
| **INTERESTING** | `vercel-ai/pnpm-lock.yaml:289` `@ai-sdk/gladia` (official Vercel AI SDK integration)<br>`vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:166,171` denies `169.254.169.254/32` (SSRF awareness)<br>`npm gladia 0.1.3` maintainer `softwarecitadel` (personal repo, not official) | Known/previously documented |

---

### Verdict List

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| New secrets in scan | **no** | Delta = 0 new hits; all 652 hits are pre-existing test fixtures |
| `@ai-sdk/gladia` in vercel-ai | **no** | Official integration, documented in KB |
| Sandbox SSRF deny list | **no** | Defensive test, not a vulnerability |
| `gladia` npm package (personal repo) | **no** | Already flagged in KB as orphaned/unofficial |

**No new reportable findings this cycle.** Passive recon exhausted — only unblocked paths require authorized key (SSRF-by-design on api.gladia.io) or human OAuth flow test (post-auth `redirect_to` on app.gladia.io).
