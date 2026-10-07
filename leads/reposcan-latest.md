
===== REPOSCAN 2026-10-07 15:36:34 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && ls -la reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Oct  7 15:35 .
drwxr-xr-x  4 runner runner 4096 Oct  7 15:35 ..
drwxr-xr-x  9 runner runner 4096 Oct  7 15:35 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct  7 15:35 docs
drwxr-xr-x  7 runner runner 4096 Oct  7 15:35 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct  7 15:35 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct  7 15:35 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct  7 15:35 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct  7 15:35 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct  7 15:35 normalization
drwxr-xr-x 12 runner runner 4096 Oct  7 15:35 num2words2
drwxr-xr-x  9 runner runner 4096 Oct  7 15:35 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct  7 15:35 sdk
drwxr-xr-x  7 runner runner 4096 Oct  7 15:35 skills
drwxr-xr-x 18 runner runner 4096 Oct  7 15:35 vercel-ai
[0m
All 654 hits are from `vercel-ai` repo only — test/fixture data with obvious placeholders. Classifying:

### TEST_OR_EXAMPLE (all 654 hits — not reportable)

| File | Line | Pattern | Reason |
|------|------|---------|--------|
| `vercel-ai/packages/openai/src/**/*.test.ts` | 48, 66, 84, 113, 778, 3310, etc. | `apiKey: 'test-api-key'` | Hardcoded test placeholder |
| `vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts` | 13, 277 | `apiKey: 'test-api-key'` | Hardcoded test placeholder |
| `vercel-ai/packages/togetherai/src/togetherai-provider.test.ts` | 99, 112, 165 | `apiKey: 'custom-key'` / `explicit-key` | Hardcoded test placeholder |
| `vercel-ai/packages/google-vertex/src/**/*.test.ts` | 120, 187, 405, 419, 95 | `apiKey: 'test-api-key'` | Hardcoded test placeholder |
| `vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts` | 68, 134, 150 | `mock.jwt.token` / `invalid-key` | Mock/fixture data |
| `vercel-ai/packages/amazon-bedrock/src/**/*.test.ts` | 128, 152, 158, 331, 442, 209 | `sessionToken: 'dynamic-session-token'` etc. | Hardcoded test placeholder |
| `vercel-ai/packages/mcp/src/tool/oauth.test.ts` | 740, 905, 908 | `client_secret: 'secret123'` / `access_token: 'access123'` / `refresh_token: 'refresh123'` | Obvious test values |
| `vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts` | 409, 411 | `expired-access-token` / `rotating-refresh-token` | Obvious test values |
| `vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json` | 36 | `encrypted_content: "gAAAAAB..."` | Test fixture (encrypted blob) |
| `vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166, 171 | `deniedCIDRs: ['169.254.169.254/32']` | SSRF protection test, not vuln |
| `vercel-ai/pnpm-lock.yaml` | 289, 291, 2368 | `@ai-sdk/gladia` local package ref | Dependency config, not secret |

### INTERESTING (supply-chain signal)

| File | Line | Note |
|------|------|------|
| `vercel-ai/pnpm-lock.yaml` | 289, 291, 2368 | Local package `@ai-sdk/gladia` linked — confirms vercel-ai integrates Gladia as official provider (per KNOWLEDGE) |

---

### REAL_SECRET: **none**  
### ENDPOINT_LEAK: **none**  

---

**VERDICT**

| Candidate | REPORT_CANDIDATE |
|-----------|------------------|
| Any secret in vercel-ai test files | **no** — all `test-*`, `secret123`, `mock.*`, fixture data |
| `@ai-sdk/gladia` local package | **no** — known official integration, supply-chain metadata only |
| SSRF test `deniedCIDRs: 169.254.169.254/32` | **no** — defensive test, not vulnerability |

**No reportable findings this cycle.** Passive recon exhausted per KNOWLEDGE (`OTHER@program: passive recon exhausted`).
