
===== REPOSCAN 2026-09-29 05:46:05 UTC =====
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
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/package.json
[0m✱ [0mGlob "**/packages/gladia/**/*"[90m in reposcan-raw/gladiaio/vercel-ai · 24 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/gladia-upload.json
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/gladia-initiate.json
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/gladia-result.json
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [limit=30, offset=160][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts[90m [limit=30, offset=735][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts[90m [limit=30, offset=900][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts[90m [limit=30, offset=405][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.test.ts[90m [limit=30, offset=125][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/openai/src/chat/openai-chat-language-model.test.ts[90m [limit=30, offset=110][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts[90m [limit=30, offset=65][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/togetherai-provider.test.ts[90m [offset=95, limit=30][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts[90m [limit=30, offset=10][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json[90m [limit=50, offset=30][0m
[0m✱ [0mGlob "**/sdk/**/*"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Sep 29 05:40 .
drwxr-xr-x  4 runner runner 4096 Sep 29 05:40 ..
drwxr-xr-x  9 runner runner 4096 Sep 29 05:40 compare-stt
drwxr-xr-x  9 runner runner 4096 Sep 29 05:40 docs
drwxr-xr-x  7 runner runner 4096 Sep 29 05:40 gladia-cli
drwxr-xr-x 11 runner runner 4096 Sep 29 05:40 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Sep 29 05:40 gladia-samples
drwxr-xr-x  9 runner runner 4096 Sep 29 05:40 gladiaflow
drwxr-xr-x  7 runner runner 4096 Sep 29 05:40 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Sep 29 05:40 normalization
drwxr-xr-x 12 runner runner 4096 Sep 29 05:40 num2words2
drwxr-xr-x  9 runner runner 4096 Sep 29 05:40 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Sep 29 05:40 sdk
drwxr-xr-x  7 runner runner 4096 Sep 29 05:40 skills
drwxr-xr-x 18 runner runner 4096 Sep 29 05:40 vercel-ai
[0m
[0m✱ [0mGlob "**/*"[90m in reposcan-raw/gladiaio/sdk · 100 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/sdk/package.json
[0m→ [0mRead reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.ts
[0m→ [0mRead reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/client.py
[0m→ [0mRead reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.start-session.test.ts
[0m→ [0mRead reposcan-raw/gladiaio/sdk/packages/generator/src/schema-fetcher.ts
[0m→ [0mRead reposcan-raw/gladiaio/sdk/packages/generator/src/cli.ts
[0m✱ [0mGlob "**/*.go"[90m in reposcan-raw/gladiaio/gladia-cli · 20 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/gladia-cli/cmd/auth.go
[0m→ [0mRead reposcan-raw/gladiaio/gladia-cli/pkg/client/client.go
[0m→ [0mRead reposcan-raw/gladiaio/gladia-cli/cmd/transcribe_test.go
[0m✱ [0mGlob "**/*.py"[90m in reposcan-raw/gladiaio/realtime-multilingual-asr-router · 59 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/realtime-multilingual-asr-router/src/realtime_multilingual_asr_router/config.py
[0m→ [0mRead reposcan-raw/gladiaio/realtime-multilingual-asr-router/src/realtime_multilingual_asr_router/main.py
[0m→ [0mRead reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/unit/test_config.py
[0m✱ [0mGlob "**/*.ts"[90m in reposcan-raw/gladiaio/n8n-nodes-gladia · 4 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/n8n-nodes-gladia/credentials/GladiaApi.credentials.ts
[0m→ [0mRead reposcan-raw/gladiaio/n8n-nodes-gladia/nodes/Gladia/Gladia.node.ts
[0m→ [0mRead reposcan-raw/gladiaio/n8n-nodes-gladia/nodes/Gladia/GenericFunctions.ts
[0m→ [0mRead reposcan-raw/gladiaio/n8n-nodes-gladia/nodes/Gladia/test/Gladia.node.test.ts
[0m✱ [0mGlob "**/*.py"[90m in reposcan-raw/gladiaio/gladia-samples · 11 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/gladia-samples/python/core-concepts/pre-recorded/pre_recorded.py
[0m→ [0mRead reposcan-raw/gladiaio/gladia-samples/python/core-concepts/live/live-from-file.py
[0m✱ [0mGlob "**/*.rs"[90m in reposcan-raw/gladiaio/gladiaflow · 13 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/gladiaflow/src-tauri/src/gladia.rs
[0m→ [0mRead reposcan-raw/gladiaio/gladiaflow/src-tauri/src/config.rs
[0m✱ [0mGlob "**/*"[90m in reposcan-raw/gladiaio/gladia-quiz-app · 83 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/gladia-quiz-app/env.example
[0m→ [0mRead reposcan-raw/gladiaio/gladia-quiz-app/lib/gladia-client.ts
[0m→ [0mRead reposcan-raw/gladiaio/gladia-quiz-app/components/GladiaApiKeyInput.tsx
[0m✱ [0mGlob "**/*"[90m in reposcan-raw/gladiaio/skills · 36 matches[0m
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/compare-stt/ && ls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/normalization/ && ls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/num2words2/
total 512
drwxr-xr-x  9 runner runner   4096 Sep 29 05:40 .
drwxr-xr-x 15 runner runner   4096 Sep 29 05:40 ..
drwxr-xr-x  3 runner runner   4096 Sep 29 05:40 .cursor
-rw-r--r--  1 runner runner    628 Sep 29 05:40 .env.example
drwxr-xr-x  7 runner runner   4096 Sep 29 05:40 .git
-rw-r--r--  1 runner runner    579 Sep 29 05:40 .gitignore
-rw-r--r--  1 runner runner   1063 Sep 29 05:40 LICENSE
-rw-r--r--  1 runner runner   1575 Sep 29 05:40 README.md
-rw-r--r--  1 runner runner    300 Sep 29 05:40 docker-compose.yml
-rw-r--r--  1 runner runner    477 Sep 29 05:40 eslint.config.mjs
-rw-r--r--  1 runner runner    366 Sep 29 05:40 instrumentation-client.ts
drwxr-xr-x  2 runner runner   4096 Sep 29 05:40 logos
-rw-r--r--  1 runner runner   4534 Sep 29 05:40 next.config.ts
-rw-r--r--  1 runner runner 394432 Sep 29 05:40 package-lock.json
-rw-r--r--  1 runner runner   1579 Sep 29 05:40 package.json
-rw-r--r--  1 runner runner     94 Sep 29 05:40 postcss.config.mjs
drwxr-xr-x  3 runner runner   4096 Sep 29 05:40 prisma
-rw-r--r--  1 runner runner    248 Sep 29 05:40 prisma.config.ts
drwxr-xr-x  4 runner runner   4096 Sep 29 05:40 public
-rw-r--r--  1 runner runner    926 Sep 29 05:40 sentry.edge.config.ts
-rw-r--r--  1 runner runner    771 Sep 29 05:40 sentry.server.config.ts
drwxr-xr-x  6 runner runner   4096 Sep 29 05:40 src
drwxr-xr-x  2 runner runner   4096 Sep 29 05:40 test-audio
