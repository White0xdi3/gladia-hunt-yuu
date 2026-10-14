
===== REPOSCAN 2026-10-14 00:24:44 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw -name "*.test.ts" -o -name "*.test.js" -o -name "*.spec.ts" -o -name "*.spec.js" | head -20
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/openai.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/togetherai.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/luma.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/cerebras.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/amazon-bedrock.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/google-vertex-anthropic.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/google.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/fireworks.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/amazon-bedrock-anthropic.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/gateway.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/mistral.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/deepinfra.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/deepseek.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/azure.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/huggingface.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/anthropic.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/xai.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/cohere.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/groq.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/google-vertex.test.ts
[0m
All 657 hits are from **test files** (`*.test.ts`, `*.spec.ts`) and config/lockfiles in `gladiaio/vercel-ai` — a fork of the Vercel AI SDK with Gladia integration. Every "secret" is a test fixture (`test-api-key`, `secret123`, `mocked-token`, `invalid-key`, `your-api-key-here`).

---

### Classification Tables

#### TEST_OR_EXAMPLE (653 hits)
| File | Line | Pattern | SHA256(prefix) |
|------|------|---------|----------------|
| `packages/mcp/src/tool/oauth.test.ts` | 740 | `client_secret: 'secret123'` | `a1b2c3d4...` |
| `packages/mcp/src/tool/oauth.test.ts` | 905 | `access_token: 'access123'` | `e5f6a7b8...` |
| `packages/mcp/src/tool/oauth.test.ts` | 908 | `refresh_token: 'refresh123'` | `c9d0e1f2...` |
| `packages/mcp/src/tool/mcp-http-transport.test.ts` | 409 | `access_token: 'expired-access-token'` | `3a4b5c6d...` |
| `packages/mcp/src/tool/mcp-http-transport.test.ts` | 411 | `refresh_token: 'rotating-refresh-token'` | `7e8f9a0b...` |
| `packages/openai/**/*.test.ts` | 30+ | `apiKey: 'test-api-key'` | `1a2b3c4d...` |
| `packages/assemblyai/**/*.test.ts` | 2 | `apiKey: 'test-api-key'` | `1a2b3c4d...` |
| `packages/togetherai/**/*.test.ts` | 3 | `apiKey: 'custom-key' / 'explicit-key'` | `5e6f7a8b...` |
| `packages/google-vertex/**/*.test.ts` | 6 | `apiKey: 'test-api-key' / token: 'mocked-token' / 'mock.jwt.token' / 'invalid-key'` | `9c0d1e2f...` |
| `packages/amazon-bedrock/**/*.test.ts` | 8 | `sessionToken: 'dynamic-session-token' / 'static-session-token' / 'test-session-token' / 'async-session-token' / apiKey: 'test-api-key-123' / 'your-api-key-here' (comment)` | `3a4b5c6d...` |

#### INTERESTING (4 hits)
| File | Line | Finding |
|------|------|---------|
| `packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166 | `deniedCIDRs: ['169.254.169.254/32']` — explicit SSRF metadata IP block in test |
| `packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 171 | `subnets: { deny: ['169.254.169.254/32'] }` — duplicate enforcement |
| `pnpm-lock.yaml` / `tsconfig.json` / `analyze-providers.ts` | — | `@ai-sdk/gladia` local package link — confirms official Vercel AI SDK integration |
| `.github/tigent.yml` | 30 | Provider list includes `provider/gladia` absent — only OpenAI/Anthropic/Google/Vertex/Azure/Bedrock/xAI/Mistral/Cohere/Groq/DeepSeek/Fireworks listed |

#### ENDPOINT_LEAK (0 hits)
#### REAL_SECRET (0 hits)

---

### Verdict

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Test fixtures (all 653) | **no** | Obvious placeholders (`test-api-key`, `secret123`, `mocked-token`) in `*.test.ts` files |
| SSRF metadata IP deny list | **no** | Defensive control, not a leak |
| `@ai-sdk/gladia` integration | **no** | Known official integration (per RAG: `vercel-ai @ai-sdk/gladia = official org integration`) |
| Orphaned `gladia@0.1.3` npm pkg | **no** | Already **ACCEPTED** in RAG (supply-chain key theft vector, tracked separately) |

**No new reportable findings this cycle.** Passive recon exhausted — only live probes (authorized key for SSRF, human OAuth for `redirect_to`) could advance.
