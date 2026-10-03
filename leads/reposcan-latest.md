
===== REPOSCAN 2026-10-03 22:55:56 UTC =====
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
[0m$ [0mls -la reposcan-raw/gladiaio/vercel-ai/packages/gladia/ 2>/dev/null || echo "not found"
total 72
drwxr-xr-x  3 runner runner  4096 Oct  3 22:54 .
drwxr-xr-x 68 runner runner  4096 Oct  3 22:54 ..
-rw-r--r--  1 runner runner 26407 Oct  3 22:54 CHANGELOG.md
-rw-r--r--  1 runner runner  1376 Oct  3 22:54 README.md
-rw-r--r--  1 runner runner  2030 Oct  3 22:54 package.json
drwxr-xr-x  4 runner runner  4096 Oct  3 22:54 src
-rw-r--r--  1 runner runner   139 Oct  3 22:54 tsconfig.build.json
-rw-r--r--  1 runner runner   404 Oct  3 22:54 tsconfig.json
-rw-r--r--  1 runner runner   337 Oct  3 22:54 tsup.config.ts
-rw-r--r--  1 runner runner   119 Oct  3 22:54 turbo.json
-rw-r--r--  1 runner runner   328 Oct  3 22:54 vitest.edge.config.js
-rw-r--r--  1 runner runner   320 Oct  3 22:54 vitest.node.config.js
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
[0m✱ [0mGlob "reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/**/*.ts"[90m 0 matches[0m
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/
total 120
drwxr-xr-x 4 runner runner  4096 Oct  3 22:54 .
drwxr-xr-x 3 runner runner  4096 Oct  3 22:54 ..
drwxr-xr-x 2 runner runner  4096 Oct  3 22:54 __fixtures__
drwxr-xr-x 2 runner runner  4096 Oct  3 22:54 __snapshots__
-rw-r--r-- 1 runner runner  5100 Oct  3 22:54 gladia-api-types.ts
-rw-r--r-- 1 runner runner   285 Oct  3 22:54 gladia-config.ts
-rw-r--r-- 1 runner runner  1197 Oct  3 22:54 gladia-error.test.ts
-rw-r--r-- 1 runner runner   462 Oct  3 22:54 gladia-error.ts
-rw-r--r-- 1 runner runner  2841 Oct  3 22:54 gladia-provider.ts
-rw-r--r-- 1 runner runner  7021 Oct  3 22:54 gladia-transcription-model-options.ts
-rw-r--r-- 1 runner runner  6112 Oct  3 22:54 gladia-transcription-model.test.ts
-rw-r--r-- 1 runner runner 12356 Oct  3 22:54 gladia-transcription-model.ts
-rw-r--r-- 1 runner runner   269 Oct  3 22:54 index.ts
-rw-r--r-- 1 runner runner 40169 Oct  3 22:54 transcript-test.mp3
-rw-r--r-- 1 runner runner   235 Oct  3 22:54 version.ts
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-api-types.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/gladia-upload.json
### Classification Table

| Category | File | Line | Match | Classification | Notes |
|----------|------|------|-------|----------------|-------|
| **TEST_OR_EXAMPLE** | vercel-ai/packages/openai/src/**/*.test.ts | multiple | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE | Standard test placeholder across all OpenAI provider tests |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/togetherai/src/**/*.test.ts | 99,112,165 | `apiKey: 'custom-key'`, `'explicit-key'` | TEST_OR_EXAMPLE | Test fixtures |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13,277 | `apiKey: 'test-api-key'` | TEST_OR_EXAMPLE | Test fixture |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/google-vertex/src/**/*.test.ts | multiple | `apiKey: 'test-api-key'`, `'mocked-token'` | TEST_OR_EXAMPLE | Test fixtures + mocked auth |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/amazon-bedrock/src/**/*.test.ts | multiple | `sessionToken: 'test-session-token'`, `'dynamic-session-token'`, `'static-session-token'`, `apiKey: 'test-api-key-123'`, `nextToken: 'test-token'` | TEST_OR_EXAMPLE | Test fixtures |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740,905,908 | `client_secret: 'secret123'`, `access_token: 'access123'`, `refresh_token: 'refresh123'` | TEST_OR_EXAMPLE | OAuth test mocks |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409,411 | `access_token: 'expired-access-token'`, `refresh_token: 'rotating-refresh-token'` | TEST_OR_EXAMPLE | Test fixtures |
| **TEST_OR_EXAMPLE** | vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json | 36 | `encrypted_content: "gAAAAABplLP75yhVf..."` | TEST_OR_EXAMPLE | Encrypted test fixture |
| **INTERESTING** | vercel-ai/pnpm-lock.yaml | 289,291 | `@ai-sdk/gladia`, `link:../../packages/gladia` | INTERESTING | Official Vercel AI SDK Gladia provider (v3.0.0-canary.48), NOT @gladiaio/sdk |
| **INTERESTING** | vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166,171 | `deniedCIDRs: ['169.254.169.254/32']` | INTERESTING | **Security control** - SSRF protection blocking cloud metadata endpoint (GOOD) |
| **INTERESTING** | vercel-ai/packages/gladia/src/gladia-transcription-model.ts | 277-279 | `isSameOrigin(resultUrl, apiOrigin)` check | INTERESTING | **Security control** - Prevents credential leakage to foreign result_url origins (GOOD) |

### Verdict List

| Candidate | Reportable? | Reason |
|-----------|-------------|--------|
| `@ai-sdk/gladia` package in vercel-ai | **NO** | Official Vercel AI SDK provider (github.com/vercel/ai), not a Gladia-owned SDK. Confirmed in RAG as official org integration. |
| SSRF protection in sandbox-vercel (`169.254.169.254/32`) | **NO** | Defensive security control, not a vulnerability |
| `isSameOrigin` credential guard in Gladia provider | **NO** | Correct security implementation - strips auth when polling foreign result_url |
| All `test-api-key`, `secret123`, `access123`, etc. | **NO** | Test fixtures only - no signs of life |
| `encrypted_content` in OpenAI fixture | **NO** | Test fixture data |

### Summary
**REPORT_CANDIDATE: no** for all hits. This scan contains only:
1. Test fixtures with obvious placeholder credentials (no entropy, standard naming)
2. The official `@ai-sdk/gladia` Vercel AI provider package (v3.0.0-canary.48) - correctly attributed to Vercel, not Gladia
3. Two **positive security controls**: SSRF metadata IP blocking and same-origin credential guarding

No secrets, no endpoint leaks, no misconfigurations requiring disclosure.
