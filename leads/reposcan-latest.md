
===== REPOSCAN 2026-10-05 18:31:58 UTC =====
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
[0m$ [0mls -la reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Oct  5 18:24 .
drwxr-xr-x  4 runner runner 4096 Oct  5 18:24 ..
drwxr-xr-x  9 runner runner 4096 Oct  5 18:24 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct  5 18:24 docs
drwxr-xr-x  7 runner runner 4096 Oct  5 18:24 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct  5 18:24 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct  5 18:24 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct  5 18:24 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct  5 18:24 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct  5 18:24 normalization
drwxr-xr-x 12 runner runner 4096 Oct  5 18:24 num2words2
drwxr-xr-x  9 runner runner 4096 Oct  5 18:24 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct  5 18:24 sdk
drwxr-xr-x  7 runner runner 4096 Oct  5 18:24 skills
drwxr-xr-x 18 runner runner 4096 Oct  5 18:24 vercel-ai
[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*["'][^"']{20,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*["'][^"']{20,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*["'][^"']{20,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*["'][^"']{20,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*["'][^"']{20,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*["'][^"']{20,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "gladia.*0\.1\.3|alexisbouchez|unofficial.*official|official.*unofficial"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "@ai-sdk/gladia"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "169\.254\.169\.254"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGlob "**/package.json"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m
[0m$ [0mgrep -r "169.254.169.254" /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/ 2>/dev/null || true
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:        deniedCIDRs: ['169.254.169.254/32'],
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:          subnets: { deny: ['169.254.169.254/32'] },
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/README.md:    subnets: { deny: ['169.254.169.254/32'] },
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/README.md:  deniedCIDRs: ['169.254.169.254/32'],
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/ai/src/util/download/download.test.ts:      download({ url: new URL('http://169.254.169.254/latest/meta-data/') }),
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/ai/src/util/download/download.test.ts:        location: 'http://169.254.169.254/latest/meta-data/',
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.ts:  // e.g. ::ffff:127.0.0.1 or 64:ff9b::169.254.169.254 are blocked.
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/fetch-with-validated-redirects.test.ts:      .mockResolvedValueOnce(redirectResponse('http://169.254.169.254/'));
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/fetch-with-validated-redirects.test.ts:      .mockResolvedValueOnce(redirectWithBody('http://169.254.169.254/'));
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/download-blob.test.ts:      downloadBlob('http://169.254.169.254/latest/meta-data/'),
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/download-blob.test.ts:          location: 'http://169.254.169.254/latest/meta-data/',
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://169.254.169.254/latest/meta-data/'),
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:    it('should block ::ffff:169.254.169.254', () => {
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://[::ffff:169.254.169.254]/file'),
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:    it('should block NAT64 64:ff9b::169.254.169.254 (metadata)', () => {
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://[64:ff9b::169.254.169.254]/file'),
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:    it('should block NAT64 local-use 64:ff9b:1::169.254.169.254', () => {
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://[64:ff9b:1::169.254.169.254]/file'),
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/harness/src/v1/harness-v1-network-sandbox-session.test-d.ts:    deniedCIDRs: ['10.5.0.0/16', '169.254.169.254/32'],
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/harness/src/v1/harness-v1-network-sandbox-session.test-d.ts:    deniedCIDRs: ['169.254.169.254/32'],
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/prodia/src/prodia-video-model.test.ts:            url: 'http://169.254.169.254/latest/meta-data/',
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/prodia/src/prodia-video-model.test.ts:        server.calls.some(call => call.requestUrl.includes('169.254.169.254')),
[0m
[0m$ [0mgrep -r "@ai-sdk/gladia" /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/ 2>/dev/null || true
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/basic.ts:import { gladia } from '@ai-sdk/gladia';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/url.ts:import { gladia } from '@ai-sdk/gladia';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/string.ts:import { gladia } from '@ai-sdk/gladia';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/.env.example:# Gladia (@ai-sdk/gladia)
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/package.json:    "@ai-sdk/gladia": "workspace:*",
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:      '@ai-sdk/gladia':
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/CHANGELOG.md:- [@ai-sdk/gladia](./packages/gladia/CHANGELOG.md)
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/tools/analyze-downloads/src/analyze-providers.ts:    '@ai-sdk/gladia',
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/contributing/packages.md:| `gladia`            | `@ai-sdk/gladia`            | Gladia (Speech)             |
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/CHANGELOG.md:# @ai-sdk/gladia
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/README.md:The Gladia provider is available in the `@ai-sdk/gladia` module. You can install it with
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/README.md:npm i @ai-sdk/gladia
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/README.md:You can import the default provider instance `gladia` from `@ai-sdk/gladia`:
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/README.md:import { gladia } from '@ai-sdk/gladia';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/README.md:import { gladia } from '@ai-sdk/gladia';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json:  "name": "@ai-sdk/gladia",
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/content/providers/01-ai-sdk-providers/120-gladia.mdx:The Gladia provider is available in the `@ai-sdk/gladia` module. You can install it with
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/content/providers/01-ai-sdk-providers/120-gladia.mdx:    <Snippet text="pnpm add @ai-sdk/gladia" dark />
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/content/providers/01-ai-sdk-providers/120-gladia.mdx:    <Snippet text="npm install @ai-sdk/gladia" dark />
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/content/providers/01-ai-sdk-providers/120-gladia.mdx:    <Snippet text="yarn add @ai-sdk/gladia" dark />
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/content/providers/01-ai-sdk-providers/120-gladia.mdx:    <Snippet text="bun add @ai-sdk/gladia" dark />
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/content/providers/01-ai-sdk-providers/120-gladia.mdx:You can import the default provider instance `gladia` from `@ai-sdk/gladia`:
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/content/providers/01-ai-sdk-providers/120-gladia.mdx:import { gladia } from '@ai-sdk/gladia';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/content/providers/01-ai-sdk-providers/120-gladia.mdx:If you need a customized setup, you can import `createGladia` from `@ai-sdk/gladia` and create a provider instance with your settings:
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/content/providers/01-ai-sdk-providers/120-gladia.mdx:import { createGladia } from '@ai-sdk/gladia';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/content/providers/01-ai-sdk-providers/120-gladia.mdx:import { gladia } from '@ai-sdk/gladia';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/content/providers/01-ai-sdk-providers/120-gladia.mdx:import { type GladiaTranscriptionModelOptions } from '@ai-sdk/gladia';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/content/docs/02-foundations/02-providers-and-models.mdx:- [Gladia Provider](/providers/ai-sdk-providers/gladia) (`@ai-sdk/gladia`)
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/.changeset/rude-cheetahs-laugh.md:"@ai-sdk/gladia": patch
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/.changeset/long-actors-tie.md:"@ai-sdk/gladia": patch
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/.changeset/bright-doors-glow.md:'@ai-sdk/gladia': patch
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/.changeset/pre.json:    "@ai-sdk/gladia": "2.0.24",
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/.changeset/start-v7-prerelease.md:'@ai-sdk/gladia': major
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/.changeset/remove-commonjs-exports.md:'@ai-sdk/gladia': major
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/.changeset/smart-eggs-yawn.md:"@ai-sdk/gladia": patch
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/.changeset/workflow-serde-support.md:'@ai-sdk/gladia': patch
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/.changeset/raise-minimum-node-version.md:'@ai-sdk/gladia': patch
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/.changeset/tidy-chefs-work.md:"@ai-sdk/gladia": major
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/.changeset/provider-api-key-same-origin.md:'@ai-sdk/gladia': patch
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/.changeset/provider-api-key-same-origin.md:A new `isSameOrigin` helper is added to `@ai-sdk/provider-utils`, and the affected fetches in `@ai-sdk/black-forest-labs`, `@ai-sdk/fireworks`, `@ai-sdk/replicate`, `@ai-sdk/gladia`, `@ai-sdk/fal`, and `@ai-sdk/google` now attach credentials only when the followed URL is same-origin with the provider's configured API origin. Requests to a foreign origin are made without the credential.
[0m
[0m$ [0mfind /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio -name "package.json" | head -20
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/sveltekit-openai/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-next/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-google-vertex/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/xai-tts-demo/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-workflow/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/fastify/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/node-http-server/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/angular/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nest/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-agent/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-fastapi/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/hono/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-e2e-next/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-openai-upstash-rate-limits/package.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/harness-e2e-tui/package.json
[0m
