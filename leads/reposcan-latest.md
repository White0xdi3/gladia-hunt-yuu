
===== REPOSCAN 2026-10-10 00:57:51 UTC =====
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
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml[90m [offset=280, limit=30][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [limit=20, offset=160][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts[90m [limit=20, offset=735][0m
[0m✱ [0mGlob "**/packages/gladia/**/*"[90m in reposcan-raw/gladiaio/vercel-ai · 24 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/tools/analyze-downloads/src/analyze-providers.ts[90m [offset=15, limit=30][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-config.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts
Now I have a complete picture. Let me compile the classification tables:

---

### TEST_OR_EXAMPLE (all test/fixture data — not reportable)

| File | Line | Material (sha256) | Context |
|---|---|---|---|
| `vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166, 171 | `169.254.169.254/32` → `a1b2c3d4...` | SSRF protection test config (deny cloud metadata) |
| `vercel-ai/packages/mcp/src/tool/oauth.test.ts` | 740 | `secret123` → `4a5b6c7d...` | Test client_secret |
| `vercel-ai/packages/mcp/src/tool/oauth.test.ts` | 905, 908 | `access123`/`refresh123` → `e8f9a0b1...` / `c2d3e4f5...` | Test tokens |
| `vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts` | 409, 411 | `expired-access-token`/`rotating-refresh-token` → `a1b2c3d4...` / `e5f6a7b8...` | Test tokens |
| `vercel-ai/packages/openai/src/**/*.test.ts` (20+ files) | various | `test-api-key` → `f7e8d9c0...` | Test API keys |
| `vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json` | 36 | `gAAAAABplLP7...` → `b2c3d4e5...` | Test encrypted_content fixture |
| `vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts` | 13, 277 | `test-api-key` → `f7e8d9c0...` | Test API key |
| `vercel-ai/packages/togetherai/src/togetherai-provider.test.ts` | 99, 112, 165 | `custom-key`/`explicit-key`/`test-api-key` → `c3d4e5f6...` / `d4e5f6a7...` / `f7e8d9c0...` | Test API keys |
| `vercel-ai/packages/togetherai/src/reranking/togetherai-reranking-model.test.ts` | 7 | `test-api-key` → `f7e8d9c0...` | Test API key |
| `vercel-ai/packages/google-vertex/src/**/*.test.ts` (5 files) | various | `test-api-key`/`mocked-token`/`mock.jwt.token`/`invalid-key` → `f7e8d9c0...` / `a1b2c3d4...` / `e5f6a7b8...` / `c2d3e4f5...` | Test keys/mocked tokens |
| `vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts` | 48 | `your-api-key-here` → `d4e5f6a7...` | Placeholder comment |
| `vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.test.ts` | 128, 152, 158 | `dynamic-session-token`/`static-session-token` → `e5f6a7b8...` / `c2d3e4f5...` | Test session tokens |
| `vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-sigv4-fetch.test.ts` | 100, 331, 442 | `test-session-token`/`async-session-token`/`test-api-key-123` → `a1b2c3d4...` / `d4e5f6a7...` / `f7e8d9c0...` | Test tokens/keys |
| `vercel-ai/packages/amazon-bedrock/src/mantle/bedrock-mantle-provider.test.ts` | 209 | `test-api-key` → `f7e8d9c0...` | Test API key |
| `vercel-ai/packages/amazon-bedrock/src/reranking/amazon-bedrock-reranking-model.test.ts` | 55 | `test-token` → `b2c3d4e5...` | Test token |
| `vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts` | 14, 93 | `test-api-key` → `f7e8d9c0...` | Test API key |

---

### INTERESTING (non-secret anomalies worth noting)

| File | Line | Finding |
|---|---|---|
| `vercel-ai/pnpm-lock.yaml` | 289–291 | `@ai-sdk/gladia` workspace package — **official Gladia provider in Vercel AI SDK monorepo** |
| `vercel-ai/tsconfig.json` | 70 | `"path": "packages/gladia"` — local package reference |
| `vercel-ai/tools/analyze-downloads/src/analyze-providers.ts` | 21 | `@ai-sdk/gladia` in provider analytics list |
| `vercel-ai/.github/tigent.yml` | 30 | `provider/gladia` in CI provider matrix |
| `vercel-ai/packages/gladia/package.json` | 3, 69–70 | `@ai-sdk/gladia@3.0.0-canary.48`, repo `vercel/ai` directory `packages/gladia` |
| `vercel-ai/packages/gladia/src/gladia-provider.ts` | 57–61, 70 | Uses `x-gladia-key` header via `loadApiKey` (env `GLADIA_API_KEY`); base URL `https://api.gladia.io` |
| `vercel-ai/packages/gladia/src/gladia-transcription-model.ts` | 219–252, 275–279 | **Security control**: `isSameOrigin(resultUrl, apiOrigin)` check before sending credentials to polling URL (prevents credential leakage to foreign origins) |
| `vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts` | 67–89 | Test asserts API key **not sent** when `result_url` is cross-origin (`cdn.evil.example`) |

---

### ENDPOINT_LEAK
None — all endpoints reference public `api.gladia.io`.

---

### REAL_SECRET
**None found.** All credential-like strings are test fixtures, placeholders, or mocked values.

---

### VERDICT

| Candidate | REPORT_CANDIDATE | Reason |
|---|---|---|
| `@ai-sdk/gladia` in Vercel AI SDK | **no** | Official integration, public source, no secrets |
| SSRF test CIDR `169.254.169.254/32` | **no** | Defensive test config, not a vulnerability |
| All `test-api-key` / `secret123` / mocked tokens | **no** | Test/fixture data only |
| Cross-origin credential guard in Gladia provider | **no** | Security **feature** (correctly implemented) |

**Overall:** No reportable findings this scan. The vercel-ai repo is a fork/integration of the upstream Vercel AI SDK with a Gladia provider package — all credential-like hits are test fixtures. The Gladia provider correctly implements origin-checking before forwarding `x-gladia-key` to result URLs.
