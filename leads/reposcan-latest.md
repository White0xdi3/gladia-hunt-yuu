
===== REPOSCAN 2026-10-14 12:00:50 UTC =====
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
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Oct 14 11:59 .
drwxr-xr-x  4 runner runner 4096 Oct 14 11:59 ..
drwxr-xr-x  9 runner runner 4096 Oct 14 11:59 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct 14 11:59 docs
drwxr-xr-x  7 runner runner 4096 Oct 14 11:59 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct 14 11:59 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct 14 11:59 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct 14 11:59 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct 14 11:59 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct 14 11:59 normalization
drwxr-xr-x 12 runner runner 4096 Oct 14 11:59 num2words2
drwxr-xr-x  9 runner runner 4096 Oct 14 11:59 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct 14 11:59 sdk
drwxr-xr-x  7 runner runner 4096 Oct 14 11:59 skills
drwxr-xr-x 18 runner runner 4096 Oct 14 11:59 vercel-ai
[0m
[0m$ [0mwc -l /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml
42681 /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml
[0m
### Classification Tables

#### REAL_SECRET
| File | Line | SHA256(secret) | Notes |
|------|------|----------------|-------|
| *none* | — | — | No live credentials found in gladiaio/ org repos |

#### TEST_OR_EXAMPLE
| File | Line | Pattern | Verdict |
|------|------|---------|---------|
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | `secret123` | Test fixture |
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | `access123` | Test fixture |
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | `refresh123` | Test fixture |
| vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | `expired-access-token` | Test fixture |
| vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | `rotating-refresh-token` | Test fixture |
| vercel-ai/packages/openai/src/**/*.test.ts | multiple | `test-api-key` | Test fixture (50+ occurrences) |
| vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13, 277 | `test-api-key` | Test fixture |
| vercel-ai/packages/togetherai/src/**/*.test.ts | multiple | `custom-key`, `explicit-key`, `test-api-key` | Test fixture |
| vercel-ai/packages/google-vertex/src/**/*.test.ts | multiple | `test-api-key`, `mocked-token`, `mock.jwt.token`, `invalid-key` | Test fixture |
| vercel-ai/packages/amazon-bedrock/src/**/*.test.ts | multiple | `test-api-key-123`, `dynamic-session-token`, `static-session-token`, `test-session-token`, `async-session-token`, `test-token` | Test fixture |

#### ENDPOINT_LEAK
| File | Line | Endpoint | Notes |
|------|------|----------|-------|
| *none* | — | — | No internal/staging URLs leaked |

#### INTERESTING
| File | Line | Finding | Classification |
|------|------|---------|----------------|
| vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166, 171 | `deniedCIDRs: ['169.254.169.254/32']` | **Defensive control** - explicitly blocks AWS/GCP metadata service (good practice) |
| vercel-ai/pnpm-lock.yaml | 289, 291, 2368 | `@ai-sdk/gladia` linked to local `packages/gladia` | Official Vercel AI SDK integration (in-scope, verified) |
| vercel-ai/.github/tigent.yml | 30 | Provider list includes gladia | CI config for multi-provider testing |

---

### Verdict List

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| vercel-ai sandbox metadata CIDR block | **no** | Defensive security control, not a vulnerability |
| @ai-sdk/gladia in vercel-ai monorepo | **no** | Official integration, verified in-scope |
| All test fixtures (`test-api-key`, `secret123`, etc.) | **no** | Clearly test/example data |
| npm `gladia@0.1.3` (alexisbouchez) | **no (already tracked)** | Orphaned package, supply-chain vector **already ACCEPTED** in KB (2026-10-10), not in gladiaio/ org |

**Summary**: 0 new reportable findings this cycle. Delta confirms 0 new hit lines. All grep hits are either test fixtures, official integrations, or defensive controls. The only live supply-chain issue (orphaned `gladia@0.1.3` npm package leaking API keys in WS URLs) is already tracked in KB and belongs to a personal repo, not the gladiaio org.
