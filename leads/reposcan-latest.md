
===== REPOSCAN 2026-10-02 18:38:47 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw -name "*.ts" -o -name "*.js" -o -name "*.json" -o -name "*.yaml" -o -name "*.yml" | head -20
reposcan-raw/gladiaio/vercel-ai/examples/mcp/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/server-instructions/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/server-instructions/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/http/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/http/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/shopify-mcp/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/repro-test.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/image-content/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/provider-metadata/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/provider-metadata/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-ui/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-with-auth/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-with-auth/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-multi-step/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-multi-step/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-prompts/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-prompts/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/output-schema/client.ts
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio -type f \( -name "*.ts" -o -name "*.js" -o -name "*.json" -o -name "*.py" -o -name "*.go" -o -name "*.rs" -o -name "*.yaml" -o -name "*.yml" \) ! -path "*/vercel-ai/*" ! -path "*/node_modules/*" ! -path "*/.git/*" | head -50
reposcan-raw/gladiaio/gladia-quiz-app/tailwind.config.ts
reposcan-raw/gladiaio/gladia-quiz-app/store/gameStore.ts
reposcan-raw/gladiaio/gladia-quiz-app/store/__tests__/gameStore.test.ts
reposcan-raw/gladiaio/gladia-quiz-app/.eslintrc.json
reposcan-raw/gladiaio/gladia-quiz-app/package-lock.json
reposcan-raw/gladiaio/gladia-quiz-app/next.config.js
reposcan-raw/gladiaio/gladia-quiz-app/lib/gladia-client.ts
reposcan-raw/gladiaio/gladia-quiz-app/lib/constants.ts
reposcan-raw/gladiaio/gladia-quiz-app/lib/gladia-helpers-client.ts
reposcan-raw/gladiaio/gladia-quiz-app/lib/types.ts
reposcan-raw/gladiaio/gladia-quiz-app/lib/validation.ts
reposcan-raw/gladiaio/gladia-quiz-app/lib/audio-utils.ts
reposcan-raw/gladiaio/gladia-quiz-app/lib/openai.ts
reposcan-raw/gladiaio/gladia-quiz-app/lib/gladia-helpers.ts
reposcan-raw/gladiaio/gladia-quiz-app/lib/utils.ts
reposcan-raw/gladiaio/gladia-quiz-app/postcss.config.js
reposcan-raw/gladiaio/gladia-quiz-app/jest.config.js
reposcan-raw/gladiaio/gladia-quiz-app/hooks/useGladiaTranscription.ts
reposcan-raw/gladiaio/gladia-quiz-app/hooks/useAudioRecorder.ts
reposcan-raw/gladiaio/gladia-quiz-app/tsconfig.json
reposcan-raw/gladiaio/gladia-quiz-app/package.json
reposcan-raw/gladiaio/gladia-quiz-app/jest.setup.js
reposcan-raw/gladiaio/gladia-quiz-app/components.json
reposcan-raw/gladiaio/compare-stt/next.config.ts
reposcan-raw/gladiaio/compare-stt/test-blob-security.ts
reposcan-raw/gladiaio/compare-stt/docker-compose.yml
reposcan-raw/gladiaio/compare-stt/test-match-token.ts
reposcan-raw/gladiaio/compare-stt/package-lock.json
reposcan-raw/gladiaio/compare-stt/test-diff.ts
reposcan-raw/gladiaio/compare-stt/prisma/seed.ts
reposcan-raw/gladiaio/compare-stt/sentry.server.config.ts
reposcan-raw/gladiaio/compare-stt/prisma.config.ts
reposcan-raw/gladiaio/compare-stt/test-base-path-fetch.ts
reposcan-raw/gladiaio/compare-stt/test-arena-blob.ts
reposcan-raw/gladiaio/compare-stt/tsconfig.json
reposcan-raw/gladiaio/compare-stt/src/lib/site.ts
reposcan-raw/gladiaio/compare-stt/src/lib/arena-blob.ts
reposcan-raw/gladiaio/compare-stt/src/lib/elo.ts
reposcan-raw/gladiaio/compare-stt/src/lib/providers/deepgram.ts
reposcan-raw/gladiaio/compare-stt/src/lib/providers/gladia.ts
reposcan-raw/gladiaio/compare-stt/src/lib/providers/mistral.ts
reposcan-raw/gladiaio/compare-stt/src/lib/providers/speechmatics.ts
reposcan-raw/gladiaio/compare-stt/src/lib/providers/elevenlabs.ts
reposcan-raw/gladiaio/compare-stt/src/lib/providers/assemblyai.ts
reposcan-raw/gladiaio/compare-stt/src/lib/base-path-fetch.ts
reposcan-raw/gladiaio/compare-stt/src/lib/diff.ts
reposcan-raw/gladiaio/compare-stt/src/lib/rate-limit.ts
reposcan-raw/gladiaio/compare-stt/src/lib/providers.ts
reposcan-raw/gladiaio/compare-stt/src/lib/pending-audio.ts
reposcan-raw/gladiaio/compare-stt/src/lib/upload-count.ts
[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*['\"][^'\"]{8,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*['\"][^'\"]{8,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*['\"][^'\"]{8,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*['\"][^'\"]{8,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*['\"][^'\"]{8,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(169\.254\.169\.254|metadata\.google\.internal|metadata\.azure\.com|169\.254\.169\.254)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(redirect[_-]?to|return[_-]?to|next|url|callback)\s*[:=]"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(user[_-]?id|uid|account[_-]?id|tenant[_-]?id|org[_-]?id)\s*[:=]"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Oct  2 18:28 .
drwxr-xr-x  4 runner runner 4096 Oct  2 18:28 ..
drwxr-xr-x  9 runner runner 4096 Oct  2 18:28 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct  2 18:28 docs
drwxr-xr-x  7 runner runner 4096 Oct  2 18:28 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct  2 18:28 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct  2 18:28 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct  2 18:28 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct  2 18:28 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct  2 18:28 normalization
drwxr-xr-x 12 runner runner 4096 Oct  2 18:28 num2words2
drwxr-xr-x  9 runner runner 4096 Oct  2 18:28 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct  2 18:28 sdk
drwxr-xr-x  7 runner runner 4096 Oct  2 18:28 skills
drwxr-xr-x 18 runner runner 4096 Oct  2 18:28 vercel-ai
[0m
[0m$ [0mfind /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk -type f \( -name "*.ts" -o -name "*.js" -o -name "*.json" -o -name "*.py" \) ! -path "*/node_modules/*" ! -path "*/.git/*" | head -50
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/.cursor/mcp.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/project.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/vitest.config.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/live_v2_session.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/prerecorded_v2_async.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/live_v2_job_management.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/tsconfig.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/tsdown.config.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/project.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/tsconfig.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/src/index.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-node-cjs/project.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-node-cjs/package.json
