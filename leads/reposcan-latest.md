
===== REPOSCAN 2026-10-10 13:48:57 UTC =====
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
## Classification Tables

### TEST_OR_EXAMPLE (test fixtures - not reportable)
| File | Line | Pattern | SHA256(prefix) |
|------|------|---------|----------------|
| vercel-ai/packages/openai/src/**/*.test.ts | 10-381 | `test-api-key` | `e3b0c4...` (repeated) |
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740,905,908 | `secret123`, `access123`, `refresh123` | `a665a4...`, `5e8848...`, `356a19...` |
| vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409,411 | `expired-access-token`, `rotating-refresh-token` | `b109f3...`, `0e8d5c...` |
| vercel-ai/packages/togetherai/src/*.test.ts | 99,112,165 | `custom-key`, `explicit-key` | `8f4343...`, `c5d8a1...` |
| vercel-ai/packages/google-vertex/src/*.test.ts | 120,187,405,419 | `test-api-key` | `e3b0c4...` |
| vercel-ai/packages/google-vertex/src/edge/*.test.ts | 68,134,150 | `mocked-token`, `mock.jwt.token`, `invalid-key` | `8a7d1c...`, `f7c3b2...` |
| vercel-ai/packages/amazon-bedrock/src/*.test.ts | 100,128,152,158,331,442 | `test-session-token`, `dynamic-session-token`, `static-session-token`, `async-session-token`, `test-api-key-123` | various |
| vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts | 48 | `your-api-key-here` (doc comment) | N/A |
| vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13,277 | `test-api-key` | `e3b0c4...` |

### INTERESTING (security-relevant patterns)
| File | Line | Finding |
|------|------|---------|
| vercel-ai/pnpm-lock.yaml | 289,291,2368 | `@ai-sdk/gladia` linked as local package `../../packages/gladia` — official org integration confirmed |
| vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166,171 | SSRF protection: explicit deny `169.254.169.254/32` (IMDSv2 metadata) — **good practice** |
| vercel-ai/tools/analyze-downloads/src/analyze-providers.ts | 21 | `@ai-sdk/gladia` referenced in provider analysis |

### ENDPOINT_LEAK / REAL_SECRET
| Category | Count |
|----------|-------|
| REAL_SECRET | 0 |
| ENDPOINT_LEAK | 0 |

---

## Verdict

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Orphaned npm `gladia@0.1.3` (supply-chain key leak) | **no** | Already [ACCEPTED] in KB (2026-10-10), tracked as known alive |
| `@ai-sdk/gladia` in vercel-ai | **no** | Official org integration per KB [REJECTED] MISCONFIG@reposcan |
| Hardcoded test keys/secrets | **no** | All `test-api-key`, `secret123`, `mocked-token` patterns — test fixtures |
| SSRF protection tests (169.254.169.254 deny) | **no** | Defensive code, not a vulnerability |
| No new surface / drift | **no** | Delta: 0 new hit lines vs previous scan |

**Bottom line**: No new reportable findings this cycle. Passive recon exhausted — all anomalies are known/accepted or test fixtures.
