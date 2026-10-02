
===== REPOSCAN 2026-10-02 05:49:17 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw -name "*.json" -o -name "*.yaml" -o -name "*.yml" -o -name "*.toml" -o -name "*.lock" | head -20
reposcan-raw/gladiaio/vercel-ai/examples/mcp/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/mcp/package.json
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/server/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/package.json
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/package.json
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/components.json
reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/turbo.json
reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/package.json
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/package.json
reposcan-raw/gladiaio/vercel-ai/examples/next-google-vertex/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/next-google-vertex/package.json
reposcan-raw/gladiaio/vercel-ai/examples/xai-tts-demo/package.json
reposcan-raw/gladiaio/vercel-ai/examples/next-workflow/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/next-workflow/package.json
reposcan-raw/gladiaio/vercel-ai/examples/fastify/tsconfig.json
reposcan-raw/gladiaio/vercel-ai/examples/fastify/package.json
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && cat reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml | head -300
lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: false

overrides:
  tinyexec: 1.0.2
  oxlint: 1.56.0

importers:

  .:
    devDependencies:
      '@changesets/cli':
        specifier: 2.27.10
        version: 2.27.10
      '@playwright/test':
        specifier: ^1.60.0
        version: 1.60.0
      del-cli:
        specifier: ^5.1.0
        version: 5.1.0
      husky:
        specifier: ^9.1.7
        version: 9.1.7
      konsistent:
        specifier: 0.0.1-alpha.20
        version: 0.0.1-alpha.20
      konsistent-provider:
        specifier: workspace:*
        version: link:tools/konsistent-provider
      lint-staged:
        specifier: ^15.5.1
        version: 15.5.2
      next:
        specifier: 15.0.7
        version: 15.0.7(@opentelemetry/api@1.9.1)(@playwright/test@1.60.0)(react-dom@19.0.0-rc-cc1ec60d0d-20240607(react@19.0.0-rc-cc1ec60d0d-20240607))(react@19.0.0-rc-cc1ec60d0d-20240607)(sass@1.90.0)
      oxfmt:
        specifier: ^0.41.0
        version: 0.41.0
      oxlint:
        specifier: 1.56.0
        version: 1.56.0
      playwright:
        specifier: ^1.60.0
        version: 1.60.0
      publint:
        specifier: 0.2.12
        version: 0.2.12
      react:
        specifier: 19.0.0-rc-cc1ec60d0d-20240607
        version: 19.0.0-rc-cc1ec60d0d-20240607
      react-dom:
        specifier: 19.0.0-rc-cc1ec60d0d-20240607
        version: 19.0.0-rc-cc1ec60d0d-20240607(react@19.0.0-rc-cc1ec60d0d-20240607)
      turbo:
        specifier: 2.4.4
        version: 2.4.4
      typescript:
        specifier: 5.8.3
        version: 5.8.3
      ultracite:
        specifier: 7.3.2
        version: 7.3.2(oxlint@1.56.0)
      update-ts-references:
        specifier: ^3.6.0
        version: 3.6.2
      vitest:
        specifier: 4.1.5
        version: 4.1.5(@edge-runtime/vm@5.0.0)(@opentelemetry/api@1.9.1)(@types/node@22.19.19)(jsdom@26.1.0)(msw@2.14.6(@types/node@22.19.19)(typescript@5.8.3))(vite@7.3.3(@types/node@22.19.19)(jiti@2.7.0)(less@4.4.0)(lightningcss@1.32.0)(sass@1.90.0)(terser@5.47.1)(tsx@4.22.0)(yaml@2.9.0))

  examples/ai-e2e-next:
    dependencies:
      '@ai-sdk/amazon-bedrock':
        specifier: workspace:*
        version: link:../../packages/amazon-bedrock
      '@ai-sdk/anthropic':
        specifier: workspace:*
        version: link:../../packages/anthropic
      '@ai-sdk/azure':
        specifier: workspace:*
        version: link:../../packages/azure
      '@ai-sdk/cohere':
        specifier: workspace:*
        version: link:../../packages/cohere
      '@ai-sdk/deepseek':
        specifier: workspace:*
        version: link:../../packages/deepseek
      '@ai-sdk/fireworks':
        specifier: workspace:*
        version: link:../../packages/fireworks
      '@ai-sdk/google':
        specifier: workspace:*
