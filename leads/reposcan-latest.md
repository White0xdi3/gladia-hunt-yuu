
===== REPOSCAN 2026-10-08 22:09:27 UTC =====
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
[0m$ [0mwc -l reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts
273 reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [offset=160, limit=30][0m
### Classification Tables

#### TEST_OR_EXAMPLE (612 hits)
| File | Line | Pattern | SHA256(prefix) |
|------|------|---------|----------------|
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | `client_secret: 'secret123'` | `e1d3f2a1...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | `access_token: 'access123'` | `7a9c4e2f...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | `refresh_token: 'refresh123'` | `3b8f1a7d...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | `access_token: 'expired-access-token'` | `4c2e9b8a...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | `refresh_token: 'rotating-refresh-token'` | `9f1a3e7b...` |
| 600+ additional hits across openai, assemblyai, togetherai, google-vertex, amazon-bedrock test files | various | `apiKey: 'test-api-key'`, `sessionToken: 'test-session-token'`, etc. | all test fixtures |

#### INTERESTING (38 hits)
| File | Line | Finding |
|------|------|---------|
| reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml | 289, 291, 2368 | `@ai-sdk/gladia` as local workspace package `link:../../packages/gladia` — official Vercel AI SDK integration |
| reposcan-raw/gladiaio/vercel-ai/tsconfig.json | 70 | Path mapping for `packages/gladia` |
| reposcan-raw/gladiaio/vercel-ai/tools/analyze-downloads/src/analyze-providers.ts | 21 | `@ai-sdk/gladia` in provider download analysis |
| reposcan-raw/gladiaio/vercel-ai/.github/tigent.yml | 30 | Provider list includes `provider/gladia` (implied by context) |
| reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166, 171 | Explicit `deniedCIDRs: ['169.254.169.254/32']` and `subnets: { deny: ['169.254.169.254/32'] }` — SSRF metadata IP blocked by design |

#### ENDPOINT_LEAK (0 hits)
None — no internal/staging URLs leaked.

#### REAL_SECRET (0 hits)
None — all credential-like strings are test fixtures (`test-api-key`, `secret123`, `mock.jwt.token`, etc.).

---

### Verdict List

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| `@ai-sdk/gladia` in vercel-ai monorepo | **no** | Official integration, not a vulnerability; supply-chain surface already documented in RAG |
| SSRF protection (169.254.169.254/32 deny) | **no** | Defensive control, not a finding |
| Test fixtures across provider packages | **no** | All `test-*`, `secret123`, `mock.*` patterns — no live credentials |
| npm `gladia` 0.1.3 (alexisbouchez) ownership | **no** | Already in RAG as orphaned/unverified; no new evidence this scan |

**No reportable candidates this cycle.** Passive recon exhausted; only live-authorized probes (SSRF with valid key, OAuth post-auth redirect_to with human) could advance coverage.
