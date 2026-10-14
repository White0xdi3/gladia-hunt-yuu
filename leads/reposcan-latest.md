
===== REPOSCAN 2026-10-14 06:13:09 UTC =====
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

| Category | File | Line | Classification | Notes |
|----------|------|------|----------------|-------|
| **TEST_OR_EXAMPLE** | `packages/mcp/src/tool/oauth.test.ts` | 740, 905, 908 | TEST_OR_EXAMPLE | `secret123`, `access123`, `refresh123` — obvious test fixtures |
| **TEST_OR_EXAMPLE** | `packages/mcp/src/tool/mcp-http-transport.test.ts` | 409, 411 | TEST_OR_EXAMPLE | `expired-access-token`, `rotating-refresh-token` |
| **TEST_OR_EXAMPLE** | `packages/openai/**/*.test.ts` | 14-3310 | TEST_OR_EXAMPLE | All `test-api-key` across 12 files |
| **TEST_OR_EXAMPLE** | `packages/assemblyai/src/assemblyai-transcription-model.test.ts` | 13, 277 | TEST_OR_EXAMPLE | `test-api-key` |
| **TEST_OR_EXAMPLE** | `packages/togetherai/src/*.test.ts` | 99, 112, 165 | TEST_OR_EXAMPLE | `custom-key`, `explicit-key`, `test-api-key` |
| **TEST_OR_EXAMPLE** | `packages/google-vertex/src/*.test.ts` | 120-419 | TEST_OR_EXAMPLE | `test-api-key`, `mocked-token`, `mock.jwt.token`, `invalid-key` |
| **TEST_OR_EXAMPLE** | `packages/amazon-bedrock/src/*.test.ts` | 100-442 | TEST_OR_EXAMPLE | `test-session-token`, `dynamic-session-token`, `static-session-token`, `test-api-key-123`, `test-token` |
| **TEST_OR_EXAMPLE** | `packages/amazon-bedrock/src/amazon-bedrock-provider.ts` | 48 | TEST_OR_EXAMPLE | Documentation placeholder `your-api-key-here` |
| **INTERESTING** | `packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166, 171 | INTERESTING | Explicit deny of `169.254.169.254/32` (cloud metadata IP) — security control present |
| **ENDPOINT_LEAK** | `pnpm-lock.yaml`, `tsconfig.json`, `analyze-providers.ts`, `.github/tigent.yml` | 289, 291, 2368, 70, 21, 30 | ENDPOINT_LEAK (benign) | `@ai-sdk/gladia` internal package references — confirmed official org integration per RAG |

### Verdict

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Hardcoded secrets in test files | **no** | All `test-api-key`, `secret123`, `mocked-token` etc. are obvious test fixtures |
| `@ai-sdk/gladia` internal references | **no** | Confirmed official Vercel AI SDK integration (RAG: `vercel-ai @ai-sdk/gladia = official org integration`) |
| Cloud metadata IP deny rules | **no** | Security control, not a vulnerability |
| Orphaned `gladia@0.1.3` npm package | **already accepted** | RAG: `AUTH@sdk` — supply-chain key theft vector confirmed alive (dist-tag latest=0.1.3, orphaned maintainer) |
| **Delta since last scan** | **no** | 0 new hit lines — no new findings |

**Summary**: No new reportable findings this cycle. The only live class remains the orphaned `gladia@0.1.3` npm package (already tracked in RAG). Passive recon exhausted — next cycle requires authorized key (SSRF) or human OAuth test (post-auth `redirect_to`).
