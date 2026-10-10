
===== REPOSCAN 2026-10-10 22:30:35 UTC =====
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
### Classification Tables

#### REAL_SECRET
| File | Line | Secret SHA256 | Context |
|------|------|---------------|---------|
| *none* | — | — | — |

#### TEST_OR_EXAMPLE (57 hits)
| File | Line | Pattern |
|------|------|---------|
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | `client_secret: 'secret123'` |
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | `access_token: 'access123'` |
| vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | `refresh_token: 'refresh123'` |
| vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | `access_token: 'expired-access-token'` |
| vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | `refresh_token: 'rotating-refresh-token'` |
| vercel-ai/packages/openai/src/**/*.test.ts | 48,66,84,113,778,3310,45,246,381,10,54,13,137,12,17,73 | `apiKey: 'test-api-key'` (20 occurrences) |
| vercel-ai/packages/openai/src/files/openai-files.test.ts | 40,61,78 | `apiKey: 'test-api-key'` (3) |
| vercel-ai/packages/openai/src/image/openai-image-model.test.ts | 14,114 | `apiKey: 'test-api-key'` (2) |
| vercel-ai/packages/openai/src/completion/openai-completion-language-model.test.ts | 45,246,381 | `apiKey: 'test-api-key'` (3) |
| vercel-ai/packages/openai/src/speech/openai-speech-model.test.ts | 10,54 | `apiKey: 'test-api-key'` (2) |
| vercel-ai/packages/openai/src/embedding/openai-embedding-model.test.ts | 13,137 | `apiKey: 'test-api-key'` (2) |
| vercel-ai/packages/openai/src/skills/openai-skills.test.ts | 12 | `apiKey: 'test-api-key'` |
| vercel-ai/packages/openai/src/transcription/openai-transcription-model.test.ts | 17,73 | `apiKey: 'test-api-key'` (2) |
| vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13,277 | `apiKey: 'test-api-key'` (2) |
| vercel-ai/packages/togetherai/src/togetherai-provider.test.ts | 99,112,165 | `apiKey: 'custom-key'`, `apiKey: 'explicit-key'` (3) |
| vercel-ai/packages/togetherai/src/reranking/togetherai-reranking-model.test.ts | 7 | `apiKey: 'test-api-key'` |
| vercel-ai/packages/google-vertex/src/**/*.test.ts | 120,187,405,419,5,21,68,134,150,95 | `apiKey: 'test-api-key'`, `token: 'mocked-token'`, `access_token: 'mock.jwt.token'`, `private_key: 'invalid-key'` (10) |
| vercel-ai/packages/amazon-bedrock/src/**/*.test.ts | 128,152,158,100,331,442,209,55 | `sessionToken: 'dynamic-session-token'`, `sessionToken: 'static-session-token'`, `sessionToken: 'test-session-token'`, `sessionToken: 'async-session-token'`, `apiKey: 'test-api-key-123'`, `apiKey: 'test-api-key'`, `nextToken: 'test-token'` (8) |
| vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json | 36 | `encrypted_content: "gAAAAABplLP7..."` (fixture) |

#### ENDPOINT_LEAK
| File | Line | Endpoint |
|------|------|----------|
| *none* | — | — |

#### INTERESTING (3 hits)
| File | Line | Finding |
|------|------|---------|
| vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166 | `deniedCIDRs: ['169.254.169.254/32']` — explicit SSRF guard for AWS/GCP metadata endpoint |
| vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 171 | `subnets: { deny: ['169.254.169.254/32'] }` — duplicate metadata-block rule |
| vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts | 48 | `* apiKey: 'your-api-key-here'` — placeholder in **production source** (not test), JSDoc example |

---

### Verdict

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| REAL_SECRET | **no** | Zero live credentials found; all hits are test fixtures or obvious placeholders (`test-api-key`, `secret123`, `mocked-token`) |
| INTERESTING: SSRF guards | **no** | Defensive code (deny-list for 169.254.169.254) — not a vulnerability |
| INTERESTING: prod placeholder | **no** | Documentation placeholder in `amazon-bedrock-provider.ts:48`, not an exposed key |

**Overall: No reportable findings this scan.** The vercel-ai repo is a fork/integration of the upstream Vercel AI SDK with Gladia provider; all secrets are test doubles. The only Gladia-specific surface in this repo is the `@ai-sdk/gladia` package reference (already known).
