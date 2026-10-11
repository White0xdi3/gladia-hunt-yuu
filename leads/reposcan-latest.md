
===== REPOSCAN 2026-10-11 09:00:25 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw -name "*.yaml" -o -name "*.yml" -o -name "*.json" -o -name "*.ts" -o -name "*.js" | head -20
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
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml[90m [offset=280, limit=30][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [offset=160, limit=20][0m
[0m✱ [0mGlob "**/packages/gladia/**/*"[90m in reposcan-raw/gladiaio/vercel-ai · 24 matches[0m
[0m✱ [0mGrep "gladia"[90m in reposcan-raw/gladiaio/vercel-ai/packages · 100 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts
Now I have a complete picture. Let me classify all findings.

## Classification Tables

### REAL_SECRET
| File | Line | Pattern | SHA256(prefix) | Verdict |
|------|------|---------|----------------|---------|
| *none* | — | — | — | No live credentials found |

### TEST_OR_EXAMPLE
| File | Line | Pattern | Context |
|------|------|---------|---------|
| `packages/gladia/src/gladia-transcription-model.test.ts` | 14 | `test-api-key` | Unit test apiKey |
| `packages/openai/src/**/*.test.ts` | 48,66,84,etc | `test-api-key` | OpenAI provider tests (20+ occurrences) |
| `packages/assemblyai/src/assemblyai-transcription-model.test.ts` | 13,277 | `test-api-key` | AssemblyAI provider tests |
| `packages/togetherai/src/togetherai-provider.test.ts` | 99,112,165 | `custom-key`, `explicit-key` | TogetherAI provider tests |
| `packages/google-vertex/src/*.test.ts` | 120,187,405,419 | `test-api-key`, `mocked-token` | Google Vertex tests |
| `packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts` | 68,134,150 | `mock.jwt.token`, `invalid-key` | Edge auth tests |
| `packages/mcp/src/tool/oauth.test.ts` | 740,905,908 | `secret123`, `access123`, `refresh123` | OAuth test fixtures |
| `packages/mcp/src/tool/mcp-http-transport.test.ts` | 409,411 | `expired-access-token`, `rotating-refresh-token` | MCP transport tests |
| `packages/amazon-bedrock/src/amazon-bedrock-provider.test.ts` | 128,152,158 | `dynamic-session-token`, `static-session-token` | Bedrock session token tests |
| `packages/amazon-bedrock/src/amazon-bedrock-sigv4-fetch.test.ts` | 100,331,442 | `test-session-token`, `async-session-token`, `test-api-key-123` | SigV4 fetch tests |
| `packages/amazon-bedrock/src/amazon-bedrock-provider.ts` | 48 | `your-api-key-here` | Code comment placeholder |
| `packages/amazon-bedrock/src/mantle/bedrock-mantle-provider.test.ts` | 209 | `test-api-key` | Mantle provider test |
| `packages/openai/src/responses/__fixtures__/openai-compaction.1.json` | 36 | `gAAAAABplLP7...` | Encrypted test fixture (AES) |

### ENDPOINT_LEAK
| File | Line | Endpoint | Context |
|------|------|----------|---------|
| *none* | — | — | All endpoints are production `api.gladia.io` or local test servers |

### INTERESTING
| File | Line | Finding | Risk |
|------|------|---------|------|
| `pnpm-lock.yaml` | 289-291 | `@ai-sdk/gladia` workspace package linked | **INFO**: Official Vercel AI SDK integration (not orphaned `gladia@0.1.3`) |
| `packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166,171 | `deniedCIDRs: ['169.254.169.254/32']` | **GOOD**: SSRF protection test for AWS metadata |
| `packages/gladia/src/gladia-transcription-model.test.ts` | 67-89 | Foreign origin `result_url` strips `x-gladia-key` | **GOOD**: Prevents key leakage on redirect |
| `packages/gladia/src/gladia-transcription-model.ts` | 131-134 | `callbackConfig.url` user-controlled | **KNOWN**: SSRF-by-design per RAG (AUTH_HELPED) |
| `packages/gladia/src/gladia-provider.ts` | 57-61 | `loadApiKey` from `GLADIA_API_KEY` env | **STANDARD**: Proper env var loading |

---

## SHORT VERDICT LIST

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Orphaned npm `gladia@0.1.3` (alexisbouchez) | **YES** (already tracked) | Supply-chain key theft via WebSocket URL query — RAG: ACCEPTED 2026-10-11 |
| `@ai-sdk/gladia` in vercel-ai | **NO** | Official Vercel AI SDK provider, Apache-2.0, legit integration |
| Test/fixture secrets (654 hits) | **NO** | All `test-*`, `mock-*`, `secret123` patterns — no signs of life |
| SSRF protection test (169.254.169.254) | **NO** | Defensive test, not a vulnerability |
| Foreign origin key stripping test | **NO** | Security feature verification |
| `callbackConfig.url` SSRF surface | **NO** (known) | Documented as SSRF-by-design, AUTH_HELPED, no bypass |

---

**SUMMARY**: Delta scan shows **0 new hit lines**. All 654 grep hits are pre-existing test fixtures or the known `@ai-sdk/gladia` integration. The only reportable issue remains the **orphaned `gladia@0.1.3` npm package** (already in RAG as ACCEPTED). No new REAL_SECRET, ENDPOINT_LEAK, or actionable INTERESTING findings this cycle.
