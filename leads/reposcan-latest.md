
===== REPOSCAN 2026-09-30 02:08:47 UTC =====
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
[0m$ [0mls -la reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Sep 30 02:04 .
drwxr-xr-x  4 runner runner 4096 Sep 30 02:04 ..
drwxr-xr-x  9 runner runner 4096 Sep 30 02:04 compare-stt
drwxr-xr-x  9 runner runner 4096 Sep 30 02:04 docs
drwxr-xr-x  7 runner runner 4096 Sep 30 02:04 gladia-cli
drwxr-xr-x 11 runner runner 4096 Sep 30 02:04 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Sep 30 02:04 gladia-samples
drwxr-xr-x  9 runner runner 4096 Sep 30 02:04 gladiaflow
drwxr-xr-x  7 runner runner 4096 Sep 30 02:04 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Sep 30 02:04 normalization
drwxr-xr-x 12 runner runner 4096 Sep 30 02:04 num2words2
drwxr-xr-x  9 runner runner 4096 Sep 30 02:04 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Sep 30 02:04 sdk
drwxr-xr-x  7 runner runner 4096 Sep 30 02:04 skills
drwxr-xr-x 18 runner runner 4096 Sep 30 02:04 vercel-ai
[0m
[0m✱ [0mGrep "(sk-|ghp_|gho_|ghu_|ghs_|ghr_|xoxb-|xoxp-|xapp-|api[_-]?key|secret|token|password)\s*[:=]\s*['\"][a-zA-Z0-9_\-]{20,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "169\.254\.169\.254|metadata\.google\.internal|metadata\.azure\.com|169\.254\.170\.2"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "redirect_to|return[_-]to|state=|nonce=|code_verifier|code_challenge"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "debug|test[_-]?flag|dev[_-]?mode|internal|beta|staging|localhost|127\.0\.0\.1|0\.0\.0\.0"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "x-gladia-key|x_gladia_key|gladia.*key"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m
[0m$ [0mfind reposcan-raw/gladiaio -name "*.ts" -o -name "*.js" -o -name "*.json" -o -name "*.yaml" -o -name "*.yml" | head -50
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
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/output-schema/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/sse/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/sse/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/server-info/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/server-info/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/tool-meta/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/tool-meta/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/tool-definitions/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/tool-definitions/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-resources/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-resources/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/stdio/client.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/stdio/server.ts
reposcan-raw/gladiaio/vercel-ai/examples/mcp/package.json
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/shared/notification-schema.ts
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/api/chat.ts
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/api/use-chat-request.ts
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/api/completion.ts
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/api/use-object.ts
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/api/use-chat-tools.ts
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/api/chat-with-vision.ts
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/nuxt.config.ts
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/package.json
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/tailwind.config.ts
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/postcss.config.js
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/vite.config.ts
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/lib/components/ui/button/index.ts
[0m
[0m$ [0mfind reposcan-raw/gladiaio/sdk -name "*.ts" -o -name "*.js" -o -name "*.json" -o -name "*.yaml" -o -name "*.yml" | head -30
reposcan-raw/gladiaio/sdk/.cursor/mcp.json
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/project.json
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/vitest.config.ts
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/live_v2_session.test.ts
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/prerecorded_v2_async.test.ts
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/live_v2_job_management.test.ts
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/tsconfig.json
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/package.json
reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/tsdown.config.ts
reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/project.json
reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/tsconfig.json
reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/src/index.ts
reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/package.json
reposcan-raw/gladiaio/sdk/e2e/e2e-node-cjs/project.json
reposcan-raw/gladiaio/sdk/e2e/e2e-node-cjs/package.json
reposcan-raw/gladiaio/sdk/e2e/e2e-python/project.json
reposcan-raw/gladiaio/sdk/.github/workflows/ci.yml
reposcan-raw/gladiaio/sdk/.github/workflows/release.yml
reposcan-raw/gladiaio/sdk/.github/workflows/publish.yml
reposcan-raw/gladiaio/sdk/.github/workflows/update-openapi-types.yml
reposcan-raw/gladiaio/sdk/nx.json
reposcan-raw/gladiaio/sdk/packages/sdk-js/tsdown.config.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/tsconfig.spec.json
reposcan-raw/gladiaio/sdk/packages/sdk-js/project.json
reposcan-raw/gladiaio/sdk/packages/sdk-js/vitest.config.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/tsconfig.json
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/version.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/internal_types.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/helpers.ts
[0m
[0m✱ [0mGrep "apiKey|secret|token|password|169\.254|metadata"[90m in reposcan-raw/gladiaio/sdk · 100 matches[0m
[0m✱ [0mGrep "sk-|ghp_|xoxb-|api[_-]?key\s*[:=]\s*['\"][a-zA-Z0-9]{20,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m
[0m$ [0mcat reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml | grep -A 20 '@ai-sdk/gladia'
'@ai-sdk/gladia':
        specifier: workspace:*
        version: link:../../packages/gladia
      '@ai-sdk/google':
        specifier: workspace:*
