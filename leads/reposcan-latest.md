
===== REPOSCAN 2026-09-28 23:22:11 UTC =====
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
drwxr-xr-x 15 runner runner 4096 Sep 28 23:19 .
drwxr-xr-x  4 runner runner 4096 Sep 28 23:19 ..
drwxr-xr-x  9 runner runner 4096 Sep 28 23:19 compare-stt
drwxr-xr-x  9 runner runner 4096 Sep 28 23:19 docs
drwxr-xr-x  7 runner runner 4096 Sep 28 23:19 gladia-cli
drwxr-xr-x 11 runner runner 4096 Sep 28 23:19 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Sep 28 23:19 gladia-samples
drwxr-xr-x  9 runner runner 4096 Sep 28 23:19 gladiaflow
drwxr-xr-x  7 runner runner 4096 Sep 28 23:19 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Sep 28 23:19 normalization
drwxr-xr-x 12 runner runner 4096 Sep 28 23:19 num2words2
drwxr-xr-x  9 runner runner 4096 Sep 28 23:19 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Sep 28 23:19 sdk
drwxr-xr-x  7 runner runner 4096 Sep 28 23:19 skills
drwxr-xr-x 18 runner runner 4096 Sep 28 23:20 vercel-ai
[0m
[0m$ [0mgrep -r "169.254.169.254" reposcan-raw/gladiaio/vercel-ai/ --include="*.ts" --include="*.js" -n
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:166:        deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:171:          subnets: { deny: ['169.254.169.254/32'] },
reposcan-raw/gladiaio/vercel-ai/packages/ai/src/util/download/download.test.ts:14:      download({ url: new URL('http://169.254.169.254/latest/meta-data/') }),
reposcan-raw/gladiaio/vercel-ai/packages/ai/src/util/download/download.test.ts:38:        location: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.ts:203:  // e.g. ::ffff:127.0.0.1 or 64:ff9b::169.254.169.254 are blocked.
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/fetch-with-validated-redirects.test.ts:79:      .mockResolvedValueOnce(redirectResponse('http://169.254.169.254/'));
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/fetch-with-validated-redirects.test.ts:108:      .mockResolvedValueOnce(redirectWithBody('http://169.254.169.254/'));
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/download-blob.test.ts:237:      downloadBlob('http://169.254.169.254/latest/meta-data/'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/download-blob.test.ts:261:          location: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:131:        validateDownloadUrl('http://169.254.169.254/latest/meta-data/'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:184:    it('should block ::ffff:169.254.169.254', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:186:        validateDownloadUrl('http://[::ffff:169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:268:    it('should block NAT64 64:ff9b::169.254.169.254 (metadata)', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:270:        validateDownloadUrl('http://[64:ff9b::169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:274:    it('should block NAT64 local-use 64:ff9b:1::169.254.169.254', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:276:        validateDownloadUrl('http://[64:ff9b:1::169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/harness/src/v1/harness-v1-network-sandbox-session.test-d.ts:68:    deniedCIDRs: ['10.5.0.0/16', '169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/harness/src/v1/harness-v1-network-sandbox-session.test-d.ts:77:    deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/prodia/src/prodia-video-model.test.ts:462:            url: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/prodia/src/prodia-video-model.test.ts:470:        server.calls.some(call => call.requestUrl.includes('169.254.169.254')),
[0m
[0m$ [0mcat reposcan-raw/gladiaio/sdk/package.json 2>/dev/null || echo "no package.json"
{
  "name": "gladia-sdk",
  "version": "0.0.0",
  "license": "MIT",
  "private": true,
  "engines": {
    "node": ">=20"
  },
  "workspaces": [
    "e2e/*",
    "packages/*"
  ],
  "devDependencies": {
    "@commitlint/cli": "^20.1.0",
    "@commitlint/config-conventional": "^20.0.0",
    "@commitlint/types": "^20.0.0",
    "@eslint/js": "^9.37.0",
    "@nx/eslint": "^21.6.3",
    "@nx/eslint-plugin": "^21.6.3",
    "@nx/js": "21.6.3",
    "@nx/vite": "^21.6.3",
    "@nx/web": "21.6.3",
    "@nxlv/python": "^21.2.0",
    "@swc-node/register": "~1.11.1",
    "@swc/core": "~1.13.5",
    "@swc/helpers": "~0.5.17",
    "@types/node": "20.19.9",
    "@vitest/coverage-v8": "^4.1.8",
    "@vitest/ui": "^4.1.8",
    "eslint": "^9.37.0",
    "jiti": "2.6.1",
    "nx": "^21.6.3",
    "prettier": "^3.6.2",
    "tslib": "^2.8.1",
    "typescript": "~5.9.3",
    "typescript-eslint": "^8.46.0",
    "vite": "^7.1.9",
    "vitest": "^4.1.8"
  },
  "scripts": {
    "release": "node tools/scripts/release.mjs",
    "publish": "node tools/scripts/publish.mjs"
  }
}
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/sdk/packages/
total 20
drwxr-xr-x  5 runner runner 4096 Sep 28 23:19 .
drwxr-xr-x 10 runner runner 4096 Sep 28 23:19 ..
drwxr-xr-x  3 runner runner 4096 Sep 28 23:19 generator
drwxr-xr-x  4 runner runner 4096 Sep 28 23:19 sdk-js
drwxr-xr-x  5 runner runner 4096 Sep 28 23:19 sdk-python
[0m
[0m$ [0mcat reposcan-raw/gladiaio/sdk/packages/sdk-js/package.json
{
  "name": "@gladiaio/sdk",
  "description": "Gladia JavaScript/TypeScript SDK",
  "version": "2.0.0",
  "author": "Gladia",
  "license": "MIT",
  "repository": "github:gladiaio/sdk",
  "keywords": [
    "gladia",
    "sdk",
    "typescript",
    "javascript"
  ],
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "types": "./dist/index.d.cts",
  "exports": {
    ".": {
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    },
