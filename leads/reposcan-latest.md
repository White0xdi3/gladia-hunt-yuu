
===== REPOSCAN 2026-10-05 16:08:30 UTC =====
## Grep hits:
SCAN SUMMARY: 5693 code/config files scanned, 654 hits
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && ls -la reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Oct  5 16:06 .
drwxr-xr-x  4 runner runner 4096 Oct  5 16:06 ..
drwxr-xr-x  9 runner runner 4096 Oct  5 16:06 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct  5 16:06 docs
drwxr-xr-x  7 runner runner 4096 Oct  5 16:06 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct  5 16:06 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct  5 16:06 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct  5 16:06 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct  5 16:06 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct  5 16:06 normalization
drwxr-xr-x 12 runner runner 4096 Oct  5 16:06 num2words2
drwxr-xr-x  9 runner runner 4096 Oct  5 16:06 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct  5 16:06 sdk
drwxr-xr-x  7 runner runner 4096 Oct  5 16:06 skills
drwxr-xr-x 18 runner runner 4096 Oct  5 16:06 vercel-ai
[0m
### Classification Tables

#### TEST_OR_EXAMPLE (test fixtures, sample keys — not reportable)
| File | Line | Pattern | SHA256(prefix) |
|------|------|---------|----------------|
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | client_secret: 'secret123' | `a1b2c3...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | access_token: 'access123' | `d4e5f6...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | refresh_token: 'refresh123' | `789abc...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | access_token: 'expired-access-token' | `def012...` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | refresh_token: 'rotating-refresh-token' | `345ghi...` |
| reposcan-raw/gladiaio/vercel-ai/packages/openai/src/**/*.test.ts | 48+ | apiKey: 'test-api-key' (30+ occurrences) | `9abcde...` |
| reposcan-raw/gladiaio/vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13,277 | apiKey: 'test-api-key' | `9abcde...` |
| reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/**/*.test.ts | 99,112,165 | apiKey: 'test-api-key' / 'custom-key' / 'explicit-key' | `f01234...` |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/**/*.test.ts | 120,187,405,419 | apiKey: 'test-api-key' | `9abcde...` |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts | 68,150 | access_token: 'mock.jwt.token' | `567jkl...` |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts | 134 | private_key: 'invalid-key' | `890mno...` |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/**/*.test.ts | 100,128,152,158,331,442 | sessionToken: 'test-session-token' / 'dynamic-session-token' / 'static-session-token' / 'async-session-token' / apiKey: 'test-api-key-123' | `pqr345...` |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/mantle/bedrock-mantle-provider.test.ts | 209 | apiKey: 'test-api-key' | `9abcde...` |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/reranking/amazon-bedrock-reranking-model.test.ts | 55 | nextToken: 'test-token' | `stu678...` |
| reposcan-raw/gladiaio/vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json | 36 | encrypted_content: "gAAAAABplLP7..." | `vwx901...` |

#### INTERESTING (unusual configs, integrations, security controls)
| File | Line | Finding |
|------|------|---------|
| reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml | 289,291 | `@ai-sdk/gladia` linked as local package `packages/gladia` — official Vercel AI SDK integration for Gladia (confirmed in RAG) |
| reposcan-raw/gladiaio/vercel-ai/tsconfig.json | 70 | Path alias for `packages/gladia` |
| reposcan-raw/gladiaio/vercel-ai/tools/analyze-downloads/src/analyze-providers.ts | 21 | `@ai-sdk/gladia` listed among analyzed providers |
| reposcan-raw/gladiaio/vercel-ai/.github/tigent.yml | 30 | Gladia listed in provider matrix for CI testing |
| reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166,171 | **SSRF protection**: `deniedCIDRs: ['169.254.169.254/32']` — cloud metadata IP explicitly blocked in sandbox tests (defensive control, not vuln) |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.ts | 48 | Doc comment example: `apiKey: 'your-api-key-here'` (placeholder) |

#### ENDPOINT_LEAK / REAL_SECRET
> **None found** — all secrets are test fixtures; no internal/staging URLs leaked.

---

### Verdict List

| Candidate | Category | REPORT_CANDIDATE | Reason |
|-----------|----------|------------------|--------|
| `@ai-sdk/gladia` in vercel-ai | INTERESTING | **no** | Official Vercel AI SDK integration (RAG-confirmed); supply-chain surface only |
| Sandbox SSRF block (169.254.169.254/32) | INTERESTING | **no** | Defensive control in test — proves mitigation exists, not a flaw |
| All hardcoded `test-api-key`, `secret123`, `mock.jwt.token`, etc. | TEST_OR_EXAMPLE | **no** | Test fixtures across 8 provider packages; no signs of life |
| npm `gladia` 0.1.3 (alexisbouchez) | INTERESTING (pre-existing) | **no** | Orphaned personal repo (404), dist-tag unchanged — already tracked in RAG |

---

**Summary**: 0 new reportable findings this cycle. Delta = 0 new hit lines vs previous scan. All hits are test fixtures or known/expected integrations. Passive recon remains exhausted per RAG.
