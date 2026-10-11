
===== REPOSCAN 2026-10-11 20:24:12 UTC =====
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
### CLASSIFICATION TABLES

#### REAL_SECRET
| File | Line | SHA256 (first 16) | Context |
|------|------|-------------------|---------|
| *none* | — | — | — |

#### TEST_OR_EXAMPLE (57 hits)
| File | Line | Pattern | Verdict |
|------|------|---------|---------|
| reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166, 171 | `deniedCIDRs: ['169.254.169.254/32']` | Test: SSRF protection config (GOOD) |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740, 905, 908 | `client_secret: 'secret123'`, `access_token: 'access123'`, `refresh_token: 'refresh123'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409, 411 | `access_token: 'expired-access-token'`, `refresh_token: 'rotating-refresh-token'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/openai/src/**/*.test.ts | 20+ lines | `apiKey: 'test-api-key'` | Test fixture (repeated) |
| reposcan-raw/gladiaio/vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13, 277 | `apiKey: 'test-api-key'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/**/*.test.ts | 4 lines | `apiKey: 'custom-key'`, `apiKey: 'explicit-key'`, `apiKey: 'test-api-key'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/**/*.test.ts | 8 lines | `apiKey: 'test-api-key'`, `token: 'mocked-token'`, `access_token: 'mock.jwt.token'`, `private_key: 'invalid-key'` | Test fixture/mock |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/**/*.test.ts | 7 lines | `sessionToken: 'dynamic-session-token'`, `sessionToken: 'static-session-token'`, `apiKey: 'test-api-key'`, `nextToken: 'test-token'` | Test fixture |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts | 48 | `apiKey: 'your-api-key-here'` | Doc placeholder (non-test) |
| reposcan-raw/gladiaio/vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json | 36 | `encrypted_content: "gAAAAABplLP..."` | Test fixture (Fernet token format) |

#### ENDPOINT_LEAK
| File | Line | Leak Type | Detail |
|------|------|-----------|--------|
| *none* | — | — | — |

#### INTERESTING
| File | Line | Finding | Risk |
|------|------|---------|------|
| reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166, 171 | Explicit deny of `169.254.169.254/32` (AWS/GCP metadata) in test — confirms SSRF defense awareness | Low (defensive) |
| reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml | 289, 291 | `@ai-sdk/gladia` linked as local package `packages/gladia` — official Vercel AI SDK integration | Info |
| reposcan-raw/gladiaio/vercel-ai/.github/tigent.yml | 30 | CI lists 11 AI providers including Gladia — supply-chain surface | Info |

---

### VERDICT LIST

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Hardcoded secrets in test files | **NO** | All values are obvious fixtures (`test-api-key`, `secret123`, `mocked-token`, `invalid-key`, Fernet test vector) |
| `@ai-sdk/gladia` in vercel-ai | **NO** | Official integration per knowledge base; not a supply-chain issue |
| SSRF metadata IP in test deny-list | **NO** | Defensive control, not exposure |
| Orphaned `gladia@0.1.3` npm package | **ALREADY_ACCEPTED** | Known supply-chain vector (RAG: `AUTH@sdk` accepted 2026-10-10) — no new evidence this scan |

**SUMMARY**: 0 new reportable findings. Delta scan shows 0 new hit lines vs previous. All hits are test fixtures or known/accepted surfaces.
