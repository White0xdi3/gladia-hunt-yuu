
===== REPOSCAN 2026-10-04 13:19:20 UTC =====
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
[0m$ [0mfind /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw -type f -name "*.ts" -o -name "*.js" -o -name "*.py" -o -name "*.go" -o -name "*.rs" -o -name "*.yaml" -o -name "*.yml" -o -name "*.json" -o -name "*.toml" | head -100
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/tsconfig.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/server-instructions/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/server-instructions/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/http/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/http/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/shopify-mcp/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/repro-test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/image-content/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/provider-metadata/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/provider-metadata/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-ui/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-with-auth/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-with-auth/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-multi-step/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-multi-step/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-prompts/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-prompts/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/output-schema/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/output-schema/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/sse/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/sse/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/server-info/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/server-info/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/tool-meta/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/tool-meta/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/tool-definitions/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/tool-definitions/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-resources/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-resources/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/stdio/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/stdio/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/shared/notification-schema.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/tsconfig.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/api/chat.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/api/use-chat-request.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/api/completion.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/api/use-object.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/api/use-chat-tools.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/api/chat-with-vision.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/tsconfig.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/nuxt.config.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/tailwind.config.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/postcss.config.js
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/tsconfig.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/vite.config.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/lib/components/ui/button/index.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/lib/components/ui/textarea/index.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/lib/utils.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/app.d.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/routes/structured-object/schema.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/routes/api/structured-object/+server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/routes/api/chat/+server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/src/routes/api/completion/+server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/svelte.config.js
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/components.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/turbo.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/next.config.js
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/postcss.config.js
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/sentry.server.config.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/app/api/text/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/instrumentation.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/tsconfig.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/instrumentation-client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/sentry.edge.config.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/tailwind.config.js
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/next.config.js
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/lib/tools/weather-tool.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/lib/weather-utils.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/lib/utils.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/postcss.config.js
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/claude-code/ai-sdk-coding/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/claude-code/weather-approval/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/claude-code/basic/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/claude-code/basic-with-stop/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/claude-code/weather/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/pi/ai-sdk-coding/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/pi/weather-approval/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/pi/basic/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/pi/basic-with-stop/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/pi/weather/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/codex/ai-sdk-coding/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/codex/weather-approval/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/codex/basic/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/codex/basic-with-stop/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/app/api/harness/codex/weather/route.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/agent/harness/claude-code/ai-sdk-coding-agent.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/agent/harness/claude-code/weather-agent.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/agent/harness/claude-code/weather-approval-agent.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/agent/harness/claude-code/basic-agent.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/agent/harness/pi/ai-sdk-coding-agent.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/agent/harness/pi/weather-agent.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/agent/harness/pi/weather-approval-agent.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/agent/harness/pi/basic-agent.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/agent/harness/codex/ai-sdk-coding-agent.ts
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/
total 60
drwxr-xr-x  4 runner runner  4096 Oct  4 13:14 .
drwxr-xr-x 11 runner runner  4096 Oct  4 13:15 ..
-rw-r--r--  1 runner runner 13559 Oct  4 13:15 analysis.txt
drwxr-xr-x 15 runner runner  4096 Oct  4 13:14 gladiaio
-rw-r--r--  1 runner runner    40 Oct  4 13:15 grep-delta.txt
-rw-r--r--  1 runner runner  8115 Oct  4 13:15 grep-hits.prev.txt
-rw-r--r--  1 runner runner  8115 Oct  4 13:15 grep-hits.txt
drwxr-xr-x  2 runner runner  4096 Oct  4 13:14 npm
-rw-r--r--  1 runner runner  6124 Oct  4 13:15 rag.txt
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Oct  4 13:14 .
