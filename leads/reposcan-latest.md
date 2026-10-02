
===== REPOSCAN 2026-10-02 12:46:56 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw -name "*.ts" -o -name "*.js" -o -name "*.json" -o -name "*.yaml" -o -name "*.yml" | head -20
reposcan-raw/gladiaio/vercel-ai/examples/mcp/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/server-instructions/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/server-instructions/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/http/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/http/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/shopify-mcp/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/repro-test.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/image-content/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/provider-metadata/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/provider-metadata/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-ui/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-with-auth/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-with-auth/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-multi-step/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-multi-step/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-prompts/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-prompts/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/output-schema/client.ts
[0m
[0m✱ [0mGrep "deniedCIDRs|169\.254\.169\.254"[90m in reposcan-raw · 4 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml[90m [limit=30, offset=280][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [offset=160, limit=30][0m
### CLASSIFICATION TABLE

| Category | File | Line | Evidence | Classification |
|----------|------|------|----------|----------------|
| **TEST_OR_EXAMPLE** | `packages/openai/src/**/*.test.ts` | 48,66,84,40,61,78,14,114,113,778,3310,45,246,381,10,54,13,137,12,17,73 | `apiKey: 'test-api-key'`, `apiKey: 'custom-key'`, `apiKey: 'explicit-key'` | Test fixtures |
| **TEST_OR_EXAMPLE** | `packages/mcp/src/tool/oauth.test.ts` | 740,905,908 | `client_secret: 'secret123'`, `access_token: 'access123'`, `refresh_token: 'refresh123'` | OAuth test fixtures |
| **TEST_OR_EXAMPLE** | `packages/mcp/src/tool/mcp-http-transport.test.ts` | 409,411 | `access_token: 'expired-access-token'`, `refresh_token: 'rotating-refresh-token'` | Test fixtures |
| **TEST_OR_EXAMPLE** | `packages/amazon-bedrock/src/**/*.test.ts` | 100,128,152,158,331,442,209,55 | `sessionToken: 'test-session-token'`, `'dynamic-session-token'`, `'static-session-token'`, `'async-session-token'`, `apiKey: 'test-api-key-123'`, `nextToken: 'test-token'` | Test fixtures |
| **TEST_OR_EXAMPLE** | `packages/google-vertex/src/**/*.test.ts` | 5,18,21,68,120,187,405,419,95,134,150 | `token: 'mocked-token'`, `access_token: 'mock.jwt.token'`, `private_key: 'invalid-key'`, `apiKey: 'test-api-key'` | Test fixtures |
| **TEST_OR_EXAMPLE** | `packages/openai/src/responses/__fixtures__/openai-compaction.1.json` | 36 | `encrypted_content: "gAAAAABplLP7..."` | Test fixture (encrypted) |
| **TEST_OR_EXAMPLE** | `packages/togetherai/src/*.test.ts` | 99,112,165,7 | `apiKey: 'custom-key'`, `apiKey: 'explicit-key'`, `apiKey: 'test-api-key'` | Test fixtures |
| **TEST_OR_EXAMPLE** | `packages/assemblyai/src/*.test.ts` | 13,277 | `apiKey: 'test-api-key'` | Test fixtures |
| **INTERESTING (SECURITY CONTROL)** | `packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166,171 | `deniedCIDRs: ['169.254.169.254/32']`, `subnets: { deny: ['169.254.169.254/32'] }` | **Defense-in-depth: explicit metadata endpoint blocking** |
| **INTERESTING (INTEGRATION)** | `pnpm-lock.yaml` | 289-291 | `@ai-sdk/gladia: workspace:*` → `link:../../packages/gladia` | Official Vercel AI SDK provider for Gladia |
| **INTERESTING (INTEGRATION)** | `tsconfig.json` | 70 | `"path": "packages/gladia"` | Monorepo structure |
| **INTERESTING (INTEGRATION)** | `tools/analyze-downloads/src/analyze-providers.ts` | 21 | `'@ai-sdk/gladia'` in provider list | Confirmed official integration |
| **INTERESTING (CI)** | `.github/tigent.yml` | 30 | `provider/gladia` in test matrix | CI tests Gladia provider |

### VERDICT LIST

| Candidate | Reportable? | Reason |
|-----------|-------------|--------|
| Hardcoded secrets in test files | **NO** | All values are explicit test fixtures (`test-api-key`, `secret123`, `mocked-token`, `invalid-key`) |
| `169.254.169.254` references | **NO** | **Security control** — sandbox tests verify metadata endpoint is explicitly DENIED |
| `@ai-sdk/gladia` provider | **NO** | Official Vercel AI SDK integration (upstream vercel/ai repo), not a Gladia-owned secret |
| No real API keys, tokens, or credentials found | **NO** | Zero live credentials detected |

**OVERALL: REPORT_CANDIDATE = NO**

---

**Key insight**: The `vercel-ai` repo is the **upstream Vercel AI SDK monorepo** (github.com/vercel/ai), mirrored under `gladiaio/`. The `@ai-sdk/gladia` provider is an official integration maintained by Vercel. The `deniedCIDRs` test demonstrates **proper SSRF defense** — not a vulnerability.
