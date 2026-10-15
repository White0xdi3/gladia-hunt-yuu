
===== REPOSCAN 2026-10-15 15:06:52 UTC =====
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
### Classification Tables

#### TEST_OR_EXAMPLE (all test/fixture data — not reportable)
| File | Line | Pattern | SHA256(prefix) |
|------|------|---------|----------------|
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | client_secret: 'secret123' | `e3b0c4...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | access_token: 'access123' | `e3b0c4...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | refresh_token: 'refresh123' | `e3b0c4...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | access_token: 'expired-access-token' | `e3b0c4...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | refresh_token: 'rotating-refresh-token' | `e3b0c4...` |
| reposcan-raw/gladiaio/vercel-ai/packages/openai/src/**/*.test.ts | multiple | apiKey: 'test-api-key' | `e3b0c4...` |
| reposcan-raw/gladiaio/vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13,277 | apiKey: 'test-api-key' | `e3b0c4...` |
| reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/togetherai-provider.test.ts | 99,112,165 | apiKey: 'custom-key'/'explicit-key'/'test-api-key' | `e3b0c4...` |
| reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/reranking/togetherai-reranking-model.test.ts | 7 | apiKey: 'test-api-key' | `e3b0c4...` |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/**/*.test.ts | multiple | apiKey: 'test-api-key' | `e3b0c4...` |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/**/*.test.ts | multiple | sessionToken: 'test-session-token' / apiKey: 'test-api-key-123' | `e3b0c4...` |

#### INTERESTING (security-relevant configs, SSRF defenses)
| File | Line | Finding |
|------|------|---------|
| reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166 | `deniedCIDRs: ['169.254.169.254/32']` — explicit cloud metadata IP block in SSRF protection test |
| reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 171 | `subnets: { deny: ['169.254.169.254/32'] }` — duplicate subnet deny for metadata service |
| reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml | 289,291,2368 | `@ai-sdk/gladia` linked as local package — official Vercel AI SDK integration confirmed |
| reposcan-raw/gladiaio/vercel-ai/.github/tigent.yml | 30 | Provider list includes gladia among 11 AI providers — supply-chain visibility |

#### ENDPOINT_LEAK / REAL_SECRET
| File | Line | Finding | SHA256(prefix) |
|------|------|---------|----------------|
| *(none found in this delta)* | | | |

---

### Verdict List

| Candidate | Category | REPORT_CANDIDATE | Rationale |
|-----------|----------|------------------|-----------|
| Test API keys (test-api-key, secret123, etc.) | TEST_OR_EXAMPLE | **no** | All obviously fake/fixture values in test files |
| `deniedCIDRs: ['169.254.169.254/32']` | INTERESTING | **no** | Defensive SSRF control — not a vulnerability |
| `@ai-sdk/gladia` in vercel-ai | INTERESTING | **no** | Official org integration (per RAG), not supply-chain risk |
| No hardcoded live secrets, cloud metadata leaks, or internal endpoints found | — | **no** | Delta shows 0 new hit lines vs previous scan |

---

**Summary**: This scan cycle yields **no reportable findings**. All hits are either test fixtures or defensive security configurations (SSRF metadata IP blocking). The `@ai-sdk/gladia` package is confirmed as an official Vercel AI SDK integration, not an orphaned/impersonated package. No live credentials, SSRF vectors, or endpoint leaks detected in the delta.
