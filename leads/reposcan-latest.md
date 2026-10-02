
===== REPOSCAN 2026-10-02 13:57:12 UTC =====
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
drwxr-xr-x 15 runner runner 4096 Oct  2 13:50 .
drwxr-xr-x  4 runner runner 4096 Oct  2 13:50 ..
drwxr-xr-x  9 runner runner 4096 Oct  2 13:50 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct  2 13:50 docs
drwxr-xr-x  7 runner runner 4096 Oct  2 13:50 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct  2 13:50 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct  2 13:50 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct  2 13:50 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct  2 13:50 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct  2 13:50 normalization
drwxr-xr-x 12 runner runner 4096 Oct  2 13:50 num2words2
drwxr-xr-x  9 runner runner 4096 Oct  2 13:50 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct  2 13:50 sdk
drwxr-xr-x  7 runner runner 4096 Oct  2 13:50 skills
drwxr-xr-x 18 runner runner 4096 Oct  2 13:50 vercel-ai
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/sdk/
total 328
drwxr-xr-x 10 runner runner   4096 Oct  2 13:50 .
drwxr-xr-x 15 runner runner   4096 Oct  2 13:50 ..
drwxr-xr-x  3 runner runner   4096 Oct  2 13:50 .cursor
-rw-r--r--  1 runner runner    135 Oct  2 13:50 .editorconfig
drwxr-xr-x  8 runner runner   4096 Oct  2 13:50 .git
-rw-r--r--  1 runner runner    212 Oct  2 13:50 .gitattributes
drwxr-xr-x  3 runner runner   4096 Oct  2 13:50 .github
-rw-r--r--  1 runner runner    191 Oct  2 13:50 .gitignore
-rw-r--r--  1 runner runner    113 Oct  2 13:50 .npmrc
-rw-r--r--  1 runner runner    103 Oct  2 13:50 .prettierignore
-rw-r--r--  1 runner runner    127 Oct  2 13:50 .prettierrc
drwxr-xr-x  2 runner runner   4096 Oct  2 13:50 .vscode
-rw-r--r--  1 runner runner   3032 Oct  2 13:50 CONTRIBUTING.md
-rw-r--r--  1 runner runner   1063 Oct  2 13:50 LICENSE
-rw-r--r--  1 runner runner  10963 Oct  2 13:50 README.md
-rw-r--r--  1 runner runner     98 Oct  2 13:50 audit-ci.jsonc
-rw-r--r--  1 runner runner 219285 Oct  2 13:50 bun.lock
-rw-r--r--  1 runner runner     29 Oct  2 13:50 bunfig.toml
-rw-r--r--  1 runner runner    239 Oct  2 13:50 commitlint.config.cts
drwxr-xr-x  2 runner runner   4096 Oct  2 13:50 data
drwxr-xr-x  6 runner runner   4096 Oct  2 13:50 e2e
-rw-r--r--  1 runner runner   1358 Oct  2 13:50 eslint.config.mjs
-rw-r--r--  1 runner runner   3525 Oct  2 13:50 nx.json
-rw-r--r--  1 runner runner   1062 Oct  2 13:50 package.json
drwxr-xr-x  5 runner runner   4096 Oct  2 13:50 packages
drwxr-xr-x  3 runner runner   4096 Oct  2 13:50 tools
-rw-r--r--  1 runner runner     86 Oct  2 13:50 vitest.workspace.mjs
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/sdk/packages/
total 20
drwxr-xr-x  5 runner runner 4096 Oct  2 13:50 .
drwxr-xr-x 10 runner runner 4096 Oct  2 13:50 ..
drwxr-xr-x  3 runner runner 4096 Oct  2 13:50 generator
drwxr-xr-x  4 runner runner 4096 Oct  2 13:50 sdk-js
drwxr-xr-x  5 runner runner 4096 Oct  2 13:50 sdk-python
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
    "./package.json": "./package.json"
  },
  "unpkg": "dist/index.iife.js",
  "jsdelivr": "dist/index.iife.js",
  "scripts": {
    "build": "tsdown",
    "build:watch": "tsdown --watch"
  },
  "devDependencies": {
    "@tsconfig/node20": "^20.1.6",
    "@types/node": "^20.19.19",
    "@types/ws": "^8.18.1",
    "tsdown": "^0.15.6"
  },
  "peerDependencies": {
    "eventemitter3": ">=5",
    "ws": "5.2.4 || 6.2.3 || 7.5.10 || >=8.8",
    "undici": ">=5"
  },
  "peerDependenciesMeta": {
    "ws": {
      "optional": true
    },
    "undici": {
      "optional": true
    }
  },
  "engines": {
    "node": ">=20"
  }
}
[0m
[0m$ [0mcat reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
{
  "name": "@ai-sdk/gladia",
  "version": "3.0.0-canary.48",
  "type": "module",
  "license": "Apache-2.0",
