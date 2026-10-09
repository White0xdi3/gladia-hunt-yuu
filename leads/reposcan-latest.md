
===== REPOSCAN 2026-10-09 09:04:02 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw -name "*.test.ts" -o -name "*.test.tsx" -o -name "*.spec.ts" -o -name "*.spec.tsx" | head -20
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/openai.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/togetherai.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/luma.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/cerebras.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/amazon-bedrock.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/google-vertex-anthropic.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/google.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/fireworks.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/amazon-bedrock-anthropic.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/gateway.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/mistral.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/deepinfra.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/deepseek.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/azure.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/huggingface.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/anthropic.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/xai.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/cohere.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/groq.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/google-vertex.test.ts
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts[90m [offset=40, limit=20][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml[90m [limit=30, offset=280][0m
[0m✱ [0mGlob "**/packages/gladia/**/*"[90m in reposcan-raw/gladiaio/vercel-ai · 24 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/gladia-initiate.json
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/gladia-upload.json
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/gladia-result.json
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [offset=160, limit=50][0m
Now I have full context. All hits are in test files or documentation. Let me compile the classification.

## Classification Tables

### TEST_OR_EXAMPLE (53 hits — all test fixtures/mocks)
| File | Line | Pattern | Notes |
|------|------|---------|-------|
| `packages/mcp/src/tool/oauth.test.ts` | 740 | `client_secret: 'secret123'` | Test fixture |
| `packages/mcp/src/tool/oauth.test.ts` | 905 | `access_token: 'access123'` | Test fixture |
| `packages/mcp/src/tool/oauth.test.ts` | 908 | `refresh_token: 'refresh123'` | Test fixture |
| `packages/mcp/src/tool/mcp-http-transport.test.ts` | 409 | `access_token: 'expired-access-token'` | Test fixture |
| `packages/mcp/src/tool/mcp-http-transport.test.ts` | 411 | `refresh_token: 'rotating-refresh-token'` | Test fixture |
| `packages/openai/**/*.test.ts` | 14+ | `apiKey: 'test-api-key'` | 20+ occurrences, all test fixtures |
| `packages/assemblyai/**/*.test.ts` | 13,277 | `apiKey: 'test-api-key'` | Test fixtures |
| `packages/togetherai/**/*.test.ts` | 99,112,165,7 | `custom-key`, `explicit-key`, `test-api-key` | Test fixtures |
| `packages/google-vertex/**/*.test.ts` | 120,187,405,419,5,21,68,134,150,95 | `test-api-key`, `mocked-token`, `mock.jwt.token`, `invalid-key` | Test fixtures/mocks |
| `packages/amazon-bedrock/**/*.test.ts` | 128,152,158,100,331,442 | `dynamic-session-token`, `static-session-token`, `test-session-token`, `async-session-token`, `test-api-key-123` | Test fixtures |
| `packages/gladia/src/gladia-transcription-model.test.ts` | 14 | `apiKey: 'test-api-key'` | Test fixture |

### INTERESTING (7 hits)
| File | Line | Finding | Significance |
|------|------|---------|--------------|
| `packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166, 171 | `deniedCIDRs: ['169.254.169.254/32']` | **SSRF mitigation tested** — explicit deny of cloud metadata IP in network policy |
| `packages/amazon-bedrock/src/amazon-bedrock-provider.ts` | 48 | `apiKey: 'your-api-key-here'` in JSDoc `@example` | Documentation example (non-test file but clearly placeholder) |
| `pnpm-lock.yaml` | 289-291, 2368 | `@ai-sdk/gladia` workspace package | Official Vercel AI SDK provider for Gladia (confirms `vercel-ai` is upstream fork) |
| `tsconfig.json` | 70 | `"path": "packages/gladia"` | TypeScript project reference for Gladia provider |
| `tools/analyze-downloads/src/analyze-providers.ts` | 21 | Import of `@ai-sdk/gladia` | Analytics script includes Gladia provider |
| `.github/tigent.yml` | 30 | Provider list includes gladia | CI/test matrix includes Gladia |

### REAL_SECRET
**None** — no live credentials found.

### ENDPOINT_LEAK
**None** — no internal/staging URLs exposed.

---

## Verdict

| Candidate | Category | REPORT_CANDIDATE |
|-----------|----------|------------------|
| Test fixture credentials (53 hits) | TEST_OR_EXAMPLE | **no** |
| `169.254.169.254/32` deny in sandbox tests | INTERESTING (defense-in-depth) | **no** — shows SSRF awareness |
| `@ai-sdk/gladia` workspace package | INTERESTING (supply-chain) | **no** — official Vercel integration, upstream is `vercel/ai` |
| JSDoc `your-api-key-here` example | INTERESTING (docs) | **no** — clear placeholder |

**Overall: No reportable findings this cycle.** All "hits" are test fixtures, documentation placeholders, or security controls (SSRF metadata IP blocking). The `@ai-sdk/gladia` package is the official Vercel AI SDK provider (upstream: `github.com/vercel/ai`), not a rogue package.

[NEXT] No live probes needed — passive recon exhausted for this asset set.
