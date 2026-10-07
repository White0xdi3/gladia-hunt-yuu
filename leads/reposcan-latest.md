
===== REPOSCAN 2026-10-07 07:18:06 UTC =====
## Grep hits:
SCAN SUMMARY: 5694 code/config files scanned, 651 hits
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
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [offset=160, limit=30][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml[90m [limit=20, offset=285][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
---

### Classification Tables

#### REAL_SECRET
| File | Line | SHA256 (truncated) | Notes |
|------|------|-------------------|-------|
| *none* | - | - | No live credentials found |

#### TEST_OR_EXAMPLE
| File | Line | Pattern | Context |
|------|------|---------|---------|
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | `client_secret: 'secret123'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | `access_token: 'access123'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | `refresh_token: 'refresh123'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | `access_token: 'expired-access-token'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | `refresh_token: 'rotating-refresh-token'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/openai/**/*.test.ts | multiple | `apiKey: 'test-api-key'` | Test fixtures (50+ occurrences) |
| reposcan-raw/gladiaio/vercel-ai/packages/assemblyai/**/*.test.ts | multiple | `apiKey: 'test-api-key'` | Test fixtures |
| reposcan-raw/gladiaio/vercel-ai/packages/togetherai/**/*.test.ts | multiple | `apiKey: 'custom-key'`, `'explicit-key'` | Test fixtures |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/**/*.test.ts | multiple | `apiKey: 'test-api-key'`, `token: 'mocked-token'`, `'mock.jwt.token'`, `'invalid-key'` | Test fixtures |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/**/*.test.ts | multiple | `sessionToken: 'dynamic-session-token'`, `'static-session-token'`, `'async-session-token'`, `'test-session-token'`, `apiKey: 'test-api-key-123'` | Test fixtures |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-sigv4-fetch.test.ts | 442 | `apiKey: 'test-api-key-123'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json | 36 | `encrypted_content: "gAAAAABplLP7..."` | Test fixture (encrypted blob) |

#### ENDPOINT_LEAK
| File | Line | Reference | Notes |
|------|------|-----------|-------|
| reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml | 289-291 | `@ai-sdk/gladia` workspace:* → packages/gladia | Official Vercel AI SDK provider for Gladia (confirmed in RAG) |
| reposcan-raw/gladiaio/vercel-ai/tsconfig.json | 70 | `"path": "packages/gladia"` | Internal workspace config |
| reposcan-raw/gladiaio/vercel-ai/tools/analyze-downloads/src/analyze-providers.ts | 21 | `'@ai-sdk/gladia'` | Analytics script reference |
| reposcan-raw/gladiaio/vercel-ai/.github/tigent.yml | 30 | Provider list including gladia | CI config |

#### INTERESTING
| File | Line | Finding | Significance |
|------|------|---------|--------------|
| reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166, 171 | `deniedCIDRs: ['169.254.169.254/32']` | **SSRF protection test** - explicitly denies AWS/GCP/Azure metadata endpoint (correct defensive coding) |
| reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json | 69-70 | `"repository": "https://github.com/vercel/ai", "directory": "packages/gladia"` | Confirms this is a fork/mirror of Vercel's official Gladia provider |
| reposcan-raw/gladiaio/vercel-ai (entire repo) | - | Vercel AI SDK fork with `@ai-sdk/gladia` provider | **Not an official Gladia repo** - it's the Vercel AI SDK monorepo mirrored in gladiaio org; the `@ai-sdk/gladia` package IS the official integration (per RAG) |

---

### Verdict

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Hardcoded secrets in test files | **no** | All are test fixtures (`test-api-key`, `secret123`, `mocked-token`, etc.) |
| `@ai-sdk/gladia` in vercel-ai | **no** | Official Vercel AI SDK provider for Gladia (confirmed in RAG: `vercel-ai @ai-sdk/gladia = official org integration`) |
| SSRF protection test (169.254.169.254/32) | **no** | Defensive test verifying metadata endpoint is blocked |
| vercel-ai repo ownership | **no** | Known fork/mirror of Vercel AI SDK; not Gladia-owned code |
| npm `gladia` 0.1.3 (alexisbouchez) | **no** | Already tracked in RAG as orphaned/unofficial; dist-tag/shasum unchanged |

**Summary**: Zero reportable findings this cycle. The vercel-ai repo is a known mirror of the Vercel AI SDK containing the official `@ai-sdk/gladia` provider. All "secrets" are test fixtures. The SSRF test demonstrates proper metadata-endpoint blocking. No new surface, no drift.
