
===== REPOSCAN 2026-10-03 02:04:21 UTC =====
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
[0m$ [0mfind reposcan-raw/gladiaio -type f -name "*.ts" -o -name "*.js" -o -name "*.json" -o -name "*.yaml" -o -name "*.yml" -o -name "*.py" -o -name "*.rs" -o -name "*.go" -o -name "*.md" -o -name "*.toml" | head -100
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
reposcan-raw/gladiaio/vercel-ai/examples/mcp/README.md
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
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/README.md
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/package.json
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/tailwind.config.ts
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/postcss.config.js
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/vite.config.ts
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/lib/components/ui/button/index.ts
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/lib/components/ui/textarea/index.ts
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/lib/utils.ts
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/app.d.ts
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/routes/structured-object/schema.ts
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/routes/api/structured-object/+server.ts
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/routes/api/chat/+server.ts
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/routes/api/completion/+server.ts
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/README.md
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/package.json
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/svelte.config.js
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/components.json
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/turbo.json
reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/next.config.js
reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/postcss.config.js
reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/sentry.server.config.ts
reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/app/api/text/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/instrumentation.ts
reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/README.md
reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/package.json
reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/instrumentation-client.ts
reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/sentry.edge.config.ts
reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/tailwind.config.js
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/next.config.js
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/lib/tools/weather-tool.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/lib/weather-utils.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/lib/utils.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/postcss.config.js
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/claude-code/ai-sdk-coding/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/claude-code/weather-approval/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/claude-code/basic/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/claude-code/basic-with-stop/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/claude-code/weather/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/pi/ai-sdk-coding/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/pi/weather-approval/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/pi/basic/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/pi/basic-with-stop/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/pi/weather/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/codex/ai-sdk-coding/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/codex/weather-approval/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/codex/basic/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/codex/basic-with-stop/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/codex/weather/route.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/agent/harness/claude-code/ai-sdk-coding-agent.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/agent/harness/claude-code/weather-agent.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/agent/harness/claude-code/weather-approval-agent.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/agent/harness/claude-code/basic-agent.ts
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/agent/harness/pi/ai-sdk-coding-agent.ts
[0m
[0m$ [0mls reposcan-raw/gladiaio/
compare-stt
docs
gladia-cli
gladia-quiz-app
gladia-samples
gladiaflow
n8n-nodes-gladia
normalization
num2words2
realtime-multilingual-asr-router
sdk
skills
vercel-ai
[0m
