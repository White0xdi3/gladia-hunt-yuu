
===== REPOSCAN 2026-10-07 22:07:43 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -r "169.254.169.254" reposcan-raw/ --include="*.ts" --include="*.js" --include="*.json" --include="*.yaml" --include="*.yml"
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -r "@ai-sdk/gladia" reposcan-raw/ --include="*.ts" --include="*.js" --include="*.json" --include="*.yaml" --include="*.yml"
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/basic.ts:import { gladia } from '@ai-sdk/gladia';
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/url.ts:import { gladia } from '@ai-sdk/gladia';
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/string.ts:import { gladia } from '@ai-sdk/gladia';
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/package.json:    "@ai-sdk/gladia": "workspace:*",
reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:      '@ai-sdk/gladia':
reposcan-raw/gladiaio/vercel-ai/tools/analyze-downloads/src/analyze-providers.ts:    '@ai-sdk/gladia',
reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json:  "name": "@ai-sdk/gladia",
reposcan-raw/gladiaio/vercel-ai/.changeset/pre.json:    "@ai-sdk/gladia": "2.0.24",
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
[0m✱ [0mGlob "reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/**/*.ts"[90m 0 matches[0m
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/
total 72
drwxr-xr-x  3 runner runner  4096 Oct  7 22:02 .
drwxr-xr-x 68 runner runner  4096 Oct  7 22:02 ..
-rw-r--r--  1 runner runner 26407 Oct  7 22:02 CHANGELOG.md
-rw-r--r--  1 runner runner  1376 Oct  7 22:02 README.md
-rw-r--r--  1 runner runner  2030 Oct  7 22:02 package.json
drwxr-xr-x  4 runner runner  4096 Oct  7 22:02 src
-rw-r--r--  1 runner runner   139 Oct  7 22:02 tsconfig.build.json
-rw-r--r--  1 runner runner   404 Oct  7 22:02 tsconfig.json
-rw-r--r--  1 runner runner   337 Oct  7 22:02 tsup.config.ts
-rw-r--r--  1 runner runner   119 Oct  7 22:02 turbo.json
-rw-r--r--  1 runner runner   328 Oct  7 22:02 vitest.edge.config.js
-rw-r--r--  1 runner runner   320 Oct  7 22:02 vitest.node.config.js
[0m
[0m$ [0mfind /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src -type f
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/version.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/transcript-test.mp3
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-config.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/index.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model-options.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-error.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__snapshots__/gladia-transcription-model.test.ts.snap
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/gladia-initiate.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/gladia-result.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/gladia-upload.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-api-types.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-error.test.ts
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/gladia-initiate.json
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/gladia-upload.json
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/gladia-result.json
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Oct  7 22:02 .
drwxr-xr-x  4 runner runner 4096 Oct  7 22:02 ..
drwxr-xr-x  9 runner runner 4096 Oct  7 22:02 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct  7 22:02 docs
drwxr-xr-x  7 runner runner 4096 Oct  7 22:02 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct  7 22:02 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct  7 22:02 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct  7 22:02 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct  7 22:02 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct  7 22:02 normalization
drwxr-xr-x 12 runner runner 4096 Oct  7 22:02 num2words2
drwxr-xr-x  9 runner runner 4096 Oct  7 22:02 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct  7 22:02 sdk
drwxr-xr-x  7 runner runner 4096 Oct  7 22:02 skills
drwxr-xr-x 18 runner runner 4096 Oct  7 22:02 vercel-ai
[0m
[0m$ [0mgrep -r "apiKey\|secret\|token\|password" /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk --include="*.ts" --include="*.js" --include="*.json" --include="*.yaml" --include="*.yml" | grep -v ".test." | grep -v "test-" | head -50
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/.github/workflows/ci.yml:  GLADIA_API_KEY: ${{ secrets.GLADIA_API_KEY }}
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/.github/workflows/release.yml:      id-token: write
