
===== REPOSCAN 2026-10-04 23:07:14 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio -name "*.test.ts" -o -name "*.test.tsx" -o -name "*.spec.ts" -o -name "*.spec.tsx" | head -20
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -r "169.254.169.254" reposcan-raw/gladiaio/ --include="*.ts" --include="*.json" --include="*.yaml" --include="*.yml"
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:        deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:          subnets: { deny: ['169.254.169.254/32'] },
reposcan-raw/gladiaio/vercel-ai/packages/ai/src/util/download/download.test.ts:      download({ url: new URL('http://169.254.169.254/latest/meta-data/') }),
reposcan-raw/gladiaio/vercel-ai/packages/ai/src/util/download/download.test.ts:        location: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.ts:  // e.g. ::ffff:127.0.0.1 or 64:ff9b::169.254.169.254 are blocked.
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/fetch-with-validated-redirects.test.ts:      .mockResolvedValueOnce(redirectResponse('http://169.254.169.254/'));
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/fetch-with-validated-redirects.test.ts:      .mockResolvedValueOnce(redirectWithBody('http://169.254.169.254/'));
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/download-blob.test.ts:      downloadBlob('http://169.254.169.254/latest/meta-data/'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/download-blob.test.ts:          location: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://169.254.169.254/latest/meta-data/'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:    it('should block ::ffff:169.254.169.254', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://[::ffff:169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:    it('should block NAT64 64:ff9b::169.254.169.254 (metadata)', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://[64:ff9b::169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:    it('should block NAT64 local-use 64:ff9b:1::169.254.169.254', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://[64:ff9b:1::169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/harness/src/v1/harness-v1-network-sandbox-session.test-d.ts:    deniedCIDRs: ['10.5.0.0/16', '169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/harness/src/v1/harness-v1-network-sandbox-session.test-d.ts:    deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/prodia/src/prodia-video-model.test.ts:            url: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/prodia/src/prodia-video-model.test.ts:        server.calls.some(call => call.requestUrl.includes('169.254.169.254')),
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

