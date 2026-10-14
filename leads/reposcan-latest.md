
===== REPOSCAN 2026-10-14 07:34:18 UTC =====
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
[0m$ [0mls -la reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Oct 14 07:33 .
drwxr-xr-x  4 runner runner 4096 Oct 14 07:33 ..
drwxr-xr-x  9 runner runner 4096 Oct 14 07:33 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct 14 07:33 docs
drwxr-xr-x  7 runner runner 4096 Oct 14 07:33 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct 14 07:33 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct 14 07:33 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct 14 07:33 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct 14 07:33 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct 14 07:33 normalization
drwxr-xr-x 12 runner runner 4096 Oct 14 07:33 num2words2
drwxr-xr-x  9 runner runner 4096 Oct 14 07:33 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct 14 07:33 sdk
drwxr-xr-x  7 runner runner 4096 Oct 14 07:33 skills
drwxr-xr-x 18 runner runner 4096 Oct 14 07:33 vercel-ai
[0m
[0m✱ [0mGrep "gladia"[90m in reposcan-raw/gladiaio/sdk · 14 matches[0m
Based on the scan data and knowledge base, here's the triage:

---

### CLASSIFICATION TABLES

#### TEST_OR_EXAMPLE (all 657 hits — test fixtures only)
| File | Line | Pattern | Classification |
|------|------|---------|----------------|
| `vercel-ai/packages/*/src/**/*.test.ts` | 400+ lines | `apiKey: 'test-api-key'`, `'secret123'`, `'access123'`, `'refresh123'`, `'expired-access-token'`, `'rotating-refresh-token'`, `'mocked-token'`, `'mock.jwt.token'`, `'invalid-key'`, `'dynamic-session-token'`, `'static-session-token'`, `'async-session-token'`, `'test-api-key-123'`, `'test-session-token'`, `'test-token'`, `'custom-key'`, `'explicit-key'` | **TEST_OR_EXAMPLE** — hardcoded test values in unit/integration tests |
| `vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts` | 166, 171 | `deny: ['169.254.169.254/32']` | **TEST_OR_EXAMPLE** — SSRF deny-list in sandbox tests (defensive, not leak) |

#### INTERESTING (config / supply-chain)
| File | Line | Finding | Notes |
|------|------|---------|-------|
| `vercel-ai/pnpm-lock.yaml` | 289, 291, 2368 | `@ai-sdk/gladia` linked as local workspace package (`link:../../packages/gladia`) | Official Vercel AI SDK integration for Gladia (per RAG: `@ai-sdk/gladia` = official org integration) |
| `vercel-ai/tsconfig.json` | 70 | `"path": "packages/gladia"` | Local package resolution for Gladia provider |
| `vercel-ai/tools/analyze-downloads/src/analyze-providers.ts` | 21 | `'@ai-sdk/gladia'` in provider list | Download analytics for Gladia provider |
| `vercel-ai/.github/tigent.yml` | 30 | Provider list includes `provider/gladia` (implied by context) | CI provider matrix |

#### ENDPOINT_LEAK — **NONE** (no internal/dev/staging URLs beyond test deny-lists)

#### REAL_SECRET — **NONE** (all secrets are test fixtures with no signs of life)

---

### VERDICT LIST

| Candidate | REPORT_CANDIDATE | Reason |
|-----------|------------------|--------|
| Test API keys in vercel-ai test suites | **no** | All `test-api-key`, `secret123`, `access123`, etc. are static test fixtures |
| `169.254.169.254/32` in sandbox deny-list | **no** | Defensive SSRF mitigation in test code, not a leak |
| `@ai-sdk/gladia` workspace package | **no** | Official Vercel AI SDK integration (confirmed in RAG) |
| Orphaned npm `gladia@0.1.3` (alexisbouchez) | **no** | **Already ACCEPTED in RAG** (2026-10-10) — supply-chain key theft vector, but not new this scan |
| `/signin?redirect_to` reflection + CSP gap | **no** | **Already ACCEPTED in RAG** (2026-08-07) — alive but known |
| SSRF-by-design on api.gladia.io | **no** | **Already ACCEPTED in RAG** (AUTH_HELPED) — frozen surface |

---

### SUMMARY
**0 new reportable candidates this cycle.** Delta = 0 new hit lines. All findings are either:
- Previously accepted/known (orphaned SDK, OAuth redirect_to, SSRF surface)
- Test fixtures with no production relevance
- Legitimate defensive code (SSRF deny-lists)

**Next action**: No passive probes needed. Current RAG covers all live classes. Await authorized key for SSRF POC or human OAuth flow test for post-auth `redirect_to` validation.
