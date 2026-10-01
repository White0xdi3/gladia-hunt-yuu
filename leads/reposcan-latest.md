
===== REPOSCAN 2026-10-01 13:27:48 UTC =====
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
### Classification Tables

#### REAL_SECRET
| File | Line | SHA256(secret) | Notes |
|------|------|----------------|-------|
| *none* | — | — | No live credentials found |

#### TEST_OR_EXAMPLE
| File | Line | Pattern | Verdict |
|------|------|---------|---------|
| `packages/mcp/src/tool/oauth.test.ts` | 740, 905, 908 | `secret123`, `access123`, `refresh123` | Test fixtures |
| `packages/mcp/src/tool/mcp-http-transport.test.ts` | 409, 411 | `expired-access-token`, `rotating-refresh-token` | Test fixtures |
| `packages/openai/src/**/*.test.ts` | 48–3310 | `test-api-key` (20+ occurrences) | Test fixtures |
| `packages/assemblyai/src/assemblyai-transcription-model.test.ts` | 13, 277 | `test-api-key` | Test fixtures |
| `packages/togetherai/src/**/*.test.ts` | 99, 112, 165, 7 | `custom-key`, `explicit-key`, `test-api-key` | Test fixtures |
| `packages/google-vertex/src/**/*.test.ts` | 120, 187, 405, 419, 5, 21, 68, 134, 150, 95 | `test-api-key`, `mocked-token`, `mock.jwt.token`, `invalid-key` | Test fixtures/mocks |
| `packages/amazon-bedrock/src/**/*.test.ts` | 128, 152, 158, 100, 331, 442, 209, 55 | `dynamic-session-token`, `static-session-token`, `test-session-token`, `async-session-token`, `test-api-key-123`, `test-token` | Test fixtures |
| `packages/amazon-bedrock/src/amazon-bedrock-provider.ts` | 48 | `your-api-key-here` | Documentation placeholder |
| `packages/openai/src/responses/__fixtures__/openai-compaction.1.json` | 36 | `encrypted_content` (Fernet token) | Test fixture |

#### ENDPOINT_LEAK
| File | Line | Leak |
|------|------|------|
| *none* | — | No internal/staging endpoints exposed |

#### INTERESTING
| File | Line | Finding |
|------|------|---------|
| `packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166, 171 | **SSRF defense confirmed** — `deniedCIDRs: ['169.254.169.254/32']` blocks IMDS (good) |
| `.github/tigent.yml` | 30 | Provider matrix includes 11 AI providers (supply-chain surface) |
| `pnpm-lock.yaml` / `tsconfig.json` | 289, 291, 2368, 70 | `@ai-sdk/gladia` = official org integration (local workspace package) |
| `tools/analyze-downloads/src/analyze-providers.ts` | 21 | `@ai-sdk/gladia` import in analytics tooling |
| **npm `gladia` 0.1.3** | — | **Misleading package**: registry says "Official TypeScript SDK" but README says "Unofficial"; maintainer `softwarecitadel@gmail.com` (personal), repo `alexisbouchez/gladia.ts` 404 — **supply-chain risk** |

---

### Verdict List

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Hardcoded secrets in test files | **no** | All `test-api-key`, `secret123`, `mocked-token` — obvious fixtures |
| SSRF defense in sandbox tests | **no** | `169.254.169.254/32` deny list is a **security control**, not a leak |
| `@ai-sdk/gladia` in vercel-ai monorepo | **no** | Official org integration, local workspace package |
| npm package `gladia` 0.1.3 (alexisbouchez) | **yes** | **Misleading "Official" claim + orphaned personal repo** — supply-chain confusion risk; verify ownership via program channel |
| OpenAI/AssemblyAI/TogetherAI/Google/AWS test keys | **no** | All in `*.test.ts` files with clearly fake values |

---

### Summary
**0 actionable secrets** — all hits are test fixtures or legitimate security controls (IMDS blocking).  
**1 supply-chain anomaly**: npm `gladia@0.1.3` masquerades as official SDK but points to a dead personal repo. Recommend flagging to Gladia for npm namespace clarification.
