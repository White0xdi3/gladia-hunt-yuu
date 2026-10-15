
===== REPOSCAN 2026-10-15 19:18:31 UTC =====
## Grep hits:
SCAN SUMMARY: 5694 code/config files scanned, 657 hits
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
drwxr-xr-x 15 runner runner 4096 Oct 15 19:12 .
drwxr-xr-x  4 runner runner 4096 Oct 15 19:12 ..
drwxr-xr-x  9 runner runner 4096 Oct 15 19:12 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct 15 19:12 docs
drwxr-xr-x  7 runner runner 4096 Oct 15 19:12 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct 15 19:12 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct 15 19:12 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct 15 19:12 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct 15 19:12 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct 15 19:12 normalization
drwxr-xr-x 12 runner runner 4096 Oct 15 19:12 num2words2
drwxr-xr-x  9 runner runner 4096 Oct 15 19:12 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct 15 19:12 sdk
drwxr-xr-x  7 runner runner 4096 Oct 15 19:12 skills
drwxr-xr-x 18 runner runner 4096 Oct 15 19:12 vercel-ai
[0m
[0m$ [0mcat reposcan-raw/gladiaio/vercel-ai/package.json
{
  "private": true,
  "name": "ai-repo",
  "scripts": {
    "build": "turbo build --concurrency 16",
    "build:examples": "turbo build --filter=@example/*",
    "build:packages": "turbo build --filter=@ai-sdk/* --filter=ai",
    "changeset": "changeset",
    "clean": "turbo clean",
    "dev": "turbo dev --cache=local:r,remote:r --concurrency 25 --continue",
    "prepare": "husky",
    "update-references": "update-ts-references && node tools/split-ts-references.mjs",
    "type-check": "tsc --build",
    "type-check:full": "tsc --build tsconfig.with-examples.json",
    "publint": "turbo publint",
    "test": "turbo test --concurrency 16 --filter=!@example/*",
    "test:ci": "turbo test --concurrency 16 --filter=!@example/* --filter=!ai --filter=!@ai-sdk/codemod --only",
    "test:update": "turbo test:update --concurrency 16 --filter=!@example/*",
    "ci:release": "turbo clean && turbo build && changeset publish",
    "ci:version": "changeset version && node .github/scripts/cleanup-examples-changesets.mjs && pnpm install --no-frozen-lockfile",
    "clean-examples": "node .github/scripts/cleanup-examples-changesets.mjs && pnpm install --no-frozen-lockfile",
    "check": "ultracite check",
    "fix": "ultracite fix",
    "validate:docs": "node tools/validate-properties-tables.mjs",
    "konsistent": "turbo run konsistent:validate konsistent:check --log-order=grouped --log-prefix=none",
    "konsistent:check": "konsistent --config-path .github/konsistent.json",
    "konsistent:validate": "konsistent validate --config-path .github/konsistent.json",
    "worktree:setup": "bash tools/worktree-setup.sh"
  },
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "ultracite fix"
    ]
  },
  "devDependencies": {
    "konsistent-provider": "workspace:*",
    "@changesets/cli": "2.27.10",
    "@playwright/test": "^1.60.0",
    "del-cli": "^5.1.0",
    "husky": "^9.1.7",
    "konsistent": "0.0.1-alpha.20",
    "lint-staged": "^15.5.1",
    "next": "15.0.7",
    "oxfmt": "^0.41.0",
    "oxlint": "^1.56.0",
    "playwright": "^1.60.0",
    "publint": "0.2.12",
    "react": "19.0.0-rc-cc1ec60d0d-20240607",
    "react-dom": "19.0.0-rc-cc1ec60d0d-20240607",
    "turbo": "2.4.4",
    "typescript": "5.8.3",
    "ultracite": "7.3.2",
    "update-ts-references": "^3.6.0",
    "vitest": "4.1.5"
  },
  "engines": {
    "node": "^22.0.0 || ^24.0.0 || ^26.0.0"
  },
  "homepage": "https://ai-sdk.dev/docs",
  "repository": {
    "type": "git",
    "url": "https://github.com/vercel/ai"
  },
  "license": "Apache License",
  "bugs": {
    "url": "https://github.com/vercel/ai/issues"
  },
  "keywords": [
    "ai"
  ],
  "packageManager": "pnpm@10.33.4",
  "pnpm": {
    "onlyBuiltDependencies": [
      "esbuild"
    ],
    "overrides": {
      "tinyexec": "1.0.2",
      "oxlint": "1.56.0"
    }
  }
}
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/vercel-ai/packages/gladia/
total 72
drwxr-xr-x  3 runner runner  4096 Oct 15 19:12 .
drwxr-xr-x 68 runner runner  4096 Oct 15 19:12 ..
-rw-r--r--  1 runner runner 26407 Oct 15 19:12 CHANGELOG.md
-rw-r--r--  1 runner runner  1376 Oct 15 19:12 README.md
-rw-r--r--  1 runner runner  2030 Oct 15 19:12 package.json
drwxr-xr-x  4 runner runner  4096 Oct 15 19:12 src
-rw-r--r--  1 runner runner   139 Oct 15 19:12 tsconfig.build.json
-rw-r--r--  1 runner runner   404 Oct 15 19:12 tsconfig.json
-rw-r--r--  1 runner runner   337 Oct 15 19:12 tsup.config.ts
-rw-r--r--  1 runner runner   119 Oct 15 19:12 turbo.json
-rw-r--r--  1 runner runner   328 Oct 15 19:12 vitest.edge.config.js
-rw-r--r--  1 runner runner   320 Oct 15 19:12 vitest.node.config.js
[0m
[0m$ [0mcat reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
