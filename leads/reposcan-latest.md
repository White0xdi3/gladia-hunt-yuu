
===== REPOSCAN 2026-10-09 16:12:53 UTC =====
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
## Classification Results

### REAL_SECRET
| File | Line | SHA256 (prefix) | Notes |
|------|------|-----------------|-------|
| *none* | — | — | No live credentials found |

### TEST_OR_EXAMPLE
| File | Line | Pattern | Context |
|------|------|---------|---------|
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | `client_secret: 'secret123'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | `access_token: 'access123'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | `refresh_token: 'refresh123'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | `access_token: 'expired-access-token'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | `refresh_token: 'rotating-refresh-token'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/openai/src/**/*.test.ts | multiple | `apiKey: 'test-api-key'` | Test fixtures (20+ occurrences) |
| reposcan-raw/gladiaio/vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13,277 | `apiKey: 'test-api-key'` | Test fixtures |
| reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/**/*.test.ts | multiple | `apiKey: 'custom-key'`, `'explicit-key'`, `'test-api-key'` | Test fixtures |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/**/*.test.ts | multiple | `apiKey: 'test-api-key'`, `token: 'mocked-token'`, `access_token: 'mock.jwt.token'`, `private_key: 'invalid-key'` | Test fixtures |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/**/*.test.ts | multiple | `sessionToken: 'dynamic-session-token'`, `'static-session-token'`, `'async-session-token'`, `'test-session-token'`, `apiKey: 'test-api-key-123'`, `'your-api-key-here'` (comment) | Test fixtures |

### ENDPOINT_LEAK
| File | Line | Value | Notes |
|------|------|-------|-------|
| *none* | — | — | No internal/staging endpoints leaked |

### INTERESTING
| File | Line | Finding | Risk |
|------|------|---------|------|
| reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml | 289,291,2368 | `@ai-sdk/gladia` linked as local package `packages/gladia` | **Supply-chain surface** — Vercel AI SDK official Gladia integration lives here (per KB) |
| reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166,171 | `deniedCIDRs: ['169.254.169.254/32']` | **SSRF defense present** — Cloud metadata IP explicitly blocked in tests |
| reposcan-raw/gladiaio/vercel-ai/tools/analyze-downloads/src/analyze-providers.ts | 21 | `@ai-sdk/gladia` in provider list | Confirms Gladia as supported provider in Vercel AI SDK |
| reposcan-raw/gladiaio/vercel-ai/.github/tigent.yml | 30 | Provider list includes `provider/gladia` (implied) | CI test matrix coverage |

---

## Verdict

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Hardcoded secrets in test fixtures | **no** | All values are obvious test placeholders (`test-api-key`, `secret123`, `mocked-token`, `invalid-key`, etc.) |
| `@ai-sdk/gladia` in vercel-ai | **no** | Known official integration (KB: "vercel-ai `@ai-sdk/gladia` = official org integration"); supply-chain surface only |
| SSRF protection test (169.254.169.254) | **no** | Defensive control, not a vulnerability |
| npm `gladia` 0.1.3 ownership discrepancy | **no** | Already tracked in KB (orphaned/irrevocable personal repo `alexisbouchez/gladia.ts`) |

**Overall**: No new reportable findings this cycle. Delta = 0 new hit lines vs previous scan (confirmed by KB). Passive recon remains exhausted per KB.
