
===== REPOSCAN 2026-10-15 07:25:11 UTC =====
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
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [limit=30, offset=160][0m
Based on my analysis of the grep hits from the `gladiaio/vercel-ai` repository (a fork of Vercel AI SDK with Gladia integration), here's the classification:

---

### **REAL_SECRET** — *None found*

All credential-like strings are test fixtures with obvious placeholder patterns (`test-api-key`, `secret123`, `mocked-token`, etc.).

---

### **TEST_OR_EXAMPLE** — *630+ hits across test files*

| File | Line | Pattern | Classification |
|------|------|---------|----------------|
| `packages/mcp/src/tool/oauth.test.ts` | 740, 905, 908 | `secret123`, `access123`, `refresh123` | Test fixture |
| `packages/mcp/src/tool/mcp-http-transport.test.ts` | 409, 411 | `expired-access-token`, `rotating-refresh-token` | Test fixture |
| `packages/openai/src/**/*.test.ts` | 48–3310 | `test-api-key` (50+ occurrences) | Test fixture |
| `packages/assemblyai/src/assemblyai-transcription-model.test.ts` | 13, 277 | `test-api-key` | Test fixture |
| `packages/togetherai/src/**/*.test.ts` | 99, 112, 165 | `custom-key`, `explicit-key`, `test-api-key` | Test fixture |
| `packages/google-vertex/src/**/*.test.ts` | 120–419 | `test-api-key`, `mocked-token`, `mock.jwt.token`, `invalid-key` | Test fixture |
| `packages/amazon-bedrock/src/**/*.test.ts` | 100–442 | `dynamic-session-token`, `static-session-token`, `test-session-token`, `async-session-token`, `test-api-key-123` | Test fixture |
| `packages/openai/src/responses/__fixtures__/openai-compaction.1.json` | 36 | `encrypted_content: "gAAAAABplLP7..."` | Test fixture (base64) |

---

### **ENDPOINT_LEAK** — *None found*

No internal/dev/staging URLs or non-public API endpoints exposed.

---

### **INTERESTING** — *3 items*

| File | Line | Finding | Significance |
|------|------|---------|--------------|
| `pnpm-lock.yaml` | 289, 291, 2368 | `@ai-sdk/gladia` linked as local package `packages/gladia` | **Official Gladia provider for Vercel AI SDK** — confirms `@ai-sdk/gladia` is the blessed integration (not the orphaned `gladia@0.1.3` on npm) |
| `tsconfig.json` | 70 | `"path": "packages/gladia"` | Local package structure for the provider |
| `packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166, 171 | `deniedCIDRs: ['169.254.169.254/32']` | **Security control** — sandbox explicitly blocks cloud metadata IP (good practice, not a vuln) |
| `tools/analyze-downloads/src/analyze-providers.ts` | 21 | `'@ai-sdk/gladia'` in provider list | Download analytics tracking for the Gladia provider |

---

### **VERDICT**

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Orphaned `gladia@0.1.3` on npm (from prior knowledge) | **YES** | Supply-chain: `latest` dist-tag points to personal repo `alexisbouchez/gladia.ts` (404), leaks API key in WS URL — **already tracked in KB as ACCEPTED** |
| `@ai-sdk/gladia` in vercel-ai | **NO** | Official integration, local package, no secrets |
| Sandbox CIDR deny `169.254.169.254/32` | **NO** | Defensive security control |
| All test fixtures | **NO** | Obvious placeholders, no signs of life |

**No new reportable findings this cycle.** The vercel-ai repo is a clean fork with proper test hygiene. The only live supply-chain risk remains the orphaned `gladia@0.1.3` package (already documented in KB).
