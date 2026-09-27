
===== REPOSCAN 2026-09-27 17:05:40 UTC =====
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
drwxr-xr-x 15 runner runner 4096 Sep 27 17:01 .
drwxr-xr-x  4 runner runner 4096 Sep 27 17:01 ..
drwxr-xr-x  9 runner runner 4096 Sep 27 17:01 compare-stt
drwxr-xr-x  9 runner runner 4096 Sep 27 17:01 docs
drwxr-xr-x  7 runner runner 4096 Sep 27 17:01 gladia-cli
drwxr-xr-x 11 runner runner 4096 Sep 27 17:01 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Sep 27 17:01 gladia-samples
drwxr-xr-x  9 runner runner 4096 Sep 27 17:01 gladiaflow
drwxr-xr-x  7 runner runner 4096 Sep 27 17:01 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Sep 27 17:01 normalization
drwxr-xr-x 12 runner runner 4096 Sep 27 17:01 num2words2
drwxr-xr-x  9 runner runner 4096 Sep 27 17:01 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Sep 27 17:01 sdk
drwxr-xr-x  7 runner runner 4096 Sep 27 17:01 skills
drwxr-xr-x 18 runner runner 4096 Sep 27 17:01 vercel-ai
[0m
[0m✱ [0mGrep "(sk-|ghp_|gladia_key|x-gladia-key|Bearer|api[_-]?key|secret|token|password)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(sk-|ghp_|gladia_key|x-gladia-key|Bearer|api[_-]?key|secret|token|password)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(sk-|ghp_|gladia_key|x-gladia-key|Bearer|api[_-]?key|secret|token|password)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(sk-|ghp_|gladia_key|x-gladia-key|Bearer|api[_-]?key|secret|token|password)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(sk-|ghp_|gladia_key|x-gladia-key|Bearer|api[_-]?key|secret|token|password)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(sk-|ghp_|gladia[_-]?key|x-gladia-key|Bearer|api[_-]?key|secret|token|password)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(sk-|ghp_|gladia[_-]?key|x-gladia-key|Bearer|api[_-]?key|secret|token|password)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(sk-|ghp_|gladia[_-]?key|x-gladia-key|Bearer|api[_-]?key|secret|token|password)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(sk-|ghp_|gladia[_-]?key|x-gladia-key|Bearer|api[_-]?key|secret|token|password)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(debug|test|staging|dev|internal|beta|localhost|127\.0\.0\.1|169\.254\.169\.254)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(debug|test|staging|dev|internal|beta|localhost|127\.0\.0\.1|169\.254\.169\.254)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(debug|test|staging|dev|internal|beta|localhost|127\.0\.0\.1|169\.254\.169\.254)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/sdk/package.json
[0m→ [0mRead reposcan-raw/gladiaio/sdk/packages/sdk-js/package.json
[0m
[0m$ [0mcat /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json 2>/dev/null || echo "NOT FOUND"
{
  "name": "@ai-sdk/gladia",
  "version": "3.0.0-canary.48",
  "type": "module",
  "license": "Apache-2.0",
  "sideEffects": false,
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "files": [
    "dist/**/*",
    "docs/**/*",
    "src",
    "!src/**/*.test.ts",
    "!src/**/*.test-d.ts",
    "!src/**/__snapshots__",
    "!src/**/__fixtures__",
    "CHANGELOG.md",
    "README.md"
  ],
  "directories": {
    "doc": "./docs"
  },
  "scripts": {
    "build": "tsup --tsconfig tsconfig.build.json",
    "build:watch": "tsup --tsconfig tsconfig.build.json --watch",
    "clean": "del-cli dist docs",
    "prepack": "mkdir -p docs && cp ../../content/providers/01-ai-sdk-providers/120-gladia.mdx ./docs/",
    "postpack": "del-cli docs",
    "type-check": "tsc --noEmit",
    "test": "pnpm test:node && pnpm test:edge",
    "test:watch": "vitest --config vitest.node.config.js",
    "test:edge": "vitest --config vitest.edge.config.js --run",
    "test:node": "vitest --config vitest.node.config.js --run",
    "test:node:watch": "vitest --config vitest.node.config.js --watch"
  },
  "exports": {
    "./package.json": "./package.json",
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "default": "./dist/index.js"
    }
  },
  "dependencies": {
    "@ai-sdk/provider": "workspace:*",
    "@ai-sdk/provider-utils": "workspace:*"
  },
  "devDependencies": {
    "@ai-sdk/test-server": "workspace:*",
    "@types/node": "22.19.19",
    "@vercel/ai-tsconfig": "workspace:*",
    "tsup": "^8.5.1",
    "typescript": "5.6.3",
    "zod": "3.25.76"
  },
  "peerDependencies": {
    "zod": "^3.25.76 || ^4.1.8"
  },
  "engines": {
    "node": ">=22"
  },
  "publishConfig": {
    "access": "public",
    "provenance": true
  },
  "homepage": "https://ai-sdk.dev/docs",
  "repository": {
    "type": "git",
    "url": "https://github.com/vercel/ai",
    "directory": "packages/gladia"
  },
  "bugs": {
    "url": "https://github.com/vercel/ai/issues"
  },
  "keywords": [
    "ai"
  ]
}
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [offset=160, limit=30][0m
[0m
[0m$ [0msha256sum <<< "secret123" | cut -d' ' -f1
e037daaf131045d87cfc764f23bd3eb0ebdcbb9ac09519ccbd9df70519b8a9f0
