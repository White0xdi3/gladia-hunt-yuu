
===== REPOSCAN 2026-10-04 15:28:10 UTC =====
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
drwxr-xr-x 15 runner runner 4096 Oct  4 15:23 .
drwxr-xr-x  4 runner runner 4096 Oct  4 15:23 ..
drwxr-xr-x  9 runner runner 4096 Oct  4 15:23 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct  4 15:23 docs
drwxr-xr-x  7 runner runner 4096 Oct  4 15:23 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct  4 15:23 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct  4 15:23 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct  4 15:23 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct  4 15:23 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct  4 15:23 normalization
drwxr-xr-x 12 runner runner 4096 Oct  4 15:23 num2words2
drwxr-xr-x  9 runner runner 4096 Oct  4 15:23 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct  4 15:23 sdk
drwxr-xr-x  7 runner runner 4096 Oct  4 15:23 skills
drwxr-xr-x 18 runner runner 4096 Oct  4 15:23 vercel-ai
[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{10,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{10,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{10,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{10,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{10,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{10,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(169\.254\.169\.254|localhost|127\.0\.0\.1|internal|staging|dev\.)[^'"\s]*\.gladia"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(debug|test|staging|internal)\s*[:=]\s*true"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(x-gladia-key|x_gladia_key|gladia.*key)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml[90m [limit=30, offset=280][0m
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/vercel-ai/packages/gladia/
total 72
drwxr-xr-x  3 runner runner  4096 Oct  4 15:23 .
drwxr-xr-x 68 runner runner  4096 Oct  4 15:23 ..
-rw-r--r--  1 runner runner 26407 Oct  4 15:23 CHANGELOG.md
-rw-r--r--  1 runner runner  1376 Oct  4 15:23 README.md
-rw-r--r--  1 runner runner  2030 Oct  4 15:23 package.json
drwxr-xr-x  4 runner runner  4096 Oct  4 15:23 src
-rw-r--r--  1 runner runner   139 Oct  4 15:23 tsconfig.build.json
-rw-r--r--  1 runner runner   404 Oct  4 15:23 tsconfig.json
-rw-r--r--  1 runner runner   337 Oct  4 15:23 tsup.config.ts
-rw-r--r--  1 runner runner   119 Oct  4 15:23 turbo.json
-rw-r--r--  1 runner runner   328 Oct  4 15:23 vitest.edge.config.js
-rw-r--r--  1 runner runner   320 Oct  4 15:23 vitest.node.config.js
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/sdk/
total 328
drwxr-xr-x 10 runner runner   4096 Oct  4 15:23 .
drwxr-xr-x 15 runner runner   4096 Oct  4 15:23 ..
drwxr-xr-x  3 runner runner   4096 Oct  4 15:23 .cursor
-rw-r--r--  1 runner runner    135 Oct  4 15:23 .editorconfig
drwxr-xr-x  8 runner runner   4096 Oct  4 15:23 .git
-rw-r--r--  1 runner runner    212 Oct  4 15:23 .gitattributes
drwxr-xr-x  3 runner runner   4096 Oct  4 15:23 .github
-rw-r--r--  1 runner runner    191 Oct  4 15:23 .gitignore
-rw-r--r--  1 runner runner    113 Oct  4 15:23 .npmrc
-rw-r--r--  1 runner runner    103 Oct  4 15:23 .prettierignore
-rw-r--r--  1 runner runner    127 Oct  4 15:23 .prettierrc
drwxr-xr-x  2 runner runner   4096 Oct  4 15:23 .vscode
-rw-r--r--  1 runner runner   3032 Oct  4 15:23 CONTRIBUTING.md
-rw-r--r--  1 runner runner   1063 Oct  4 15:23 LICENSE
-rw-r--r--  1 runner runner  10963 Oct  4 15:23 README.md
-rw-r--r--  1 runner runner     98 Oct  4 15:23 audit-ci.jsonc
-rw-r--r--  1 runner runner 219285 Oct  4 15:23 bun.lock
-rw-r--r--  1 runner runner     29 Oct  4 15:23 bunfig.toml
-rw-r--r--  1 runner runner    239 Oct  4 15:23 commitlint.config.cts
drwxr-xr-x  2 runner runner   4096 Oct  4 15:23 data
drwxr-xr-x  6 runner runner   4096 Oct  4 15:23 e2e
-rw-r--r--  1 runner runner   1358 Oct  4 15:23 eslint.config.mjs
-rw-r--r--  1 runner runner   3525 Oct  4 15:23 nx.json
-rw-r--r--  1 runner runner   1062 Oct  4 15:23 package.json
drwxr-xr-x  5 runner runner   4096 Oct  4 15:23 packages
drwxr-xr-x  3 runner runner   4096 Oct  4 15:23 tools
-rw-r--r--  1 runner runner     86 Oct  4 15:23 vitest.workspace.mjs
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/sdk/packages/
total 20
drwxr-xr-x  5 runner runner 4096 Oct  4 15:23 .
drwxr-xr-x 10 runner runner 4096 Oct  4 15:23 ..
drwxr-xr-x  3 runner runner 4096 Oct  4 15:23 generator
drwxr-xr-x  4 runner runner 4096 Oct  4 15:23 sdk-js
drwxr-xr-x  5 runner runner 4096 Oct  4 15:23 sdk-python
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/
total 120
drwxr-xr-x 4 runner runner  4096 Oct  4 15:23 .
drwxr-xr-x 3 runner runner  4096 Oct  4 15:23 ..
drwxr-xr-x 2 runner runner  4096 Oct  4 15:23 __fixtures__
drwxr-xr-x 2 runner runner  4096 Oct  4 15:23 __snapshots__
-rw-r--r-- 1 runner runner  5100 Oct  4 15:23 gladia-api-types.ts
-rw-r--r-- 1 runner runner   285 Oct  4 15:23 gladia-config.ts
-rw-r--r-- 1 runner runner  1197 Oct  4 15:23 gladia-error.test.ts
-rw-r--r-- 1 runner runner   462 Oct  4 15:23 gladia-error.ts
-rw-r--r-- 1 runner runner  2841 Oct  4 15:23 gladia-provider.ts
-rw-r--r-- 1 runner runner  7021 Oct  4 15:23 gladia-transcription-model-options.ts
-rw-r--r-- 1 runner runner  6112 Oct  4 15:23 gladia-transcription-model.test.ts
-rw-r--r-- 1 runner runner 12356 Oct  4 15:23 gladia-transcription-model.ts
-rw-r--r-- 1 runner runner   269 Oct  4 15:23 index.ts
-rw-r--r-- 1 runner runner 40169 Oct  4 15:23 transcript-test.mp3
-rw-r--r-- 1 runner runner   235 Oct  4 15:23 version.ts
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/sdk/packages/sdk-js/
total 52
drwxr-xr-x 4 runner runner 4096 Oct  4 15:23 .
drwxr-xr-x 5 runner runner 4096 Oct  4 15:23 ..
-rw-r--r-- 1 runner runner 2418 Oct  4 15:23 CHANGELOG.md
-rw-r--r-- 1 runner runner 4607 Oct  4 15:23 README.md
-rw-r--r-- 1 runner runner 1107 Oct  4 15:23 package.json
-rw-r--r-- 1 runner runner  882 Oct  4 15:23 project.json
drwxr-xr-x 2 runner runner 4096 Oct  4 15:23 scripts
drwxr-xr-x 4 runner runner 4096 Oct  4 15:23 src
-rw-r--r-- 1 runner runner  574 Oct  4 15:23 tsconfig.json
-rw-r--r-- 1 runner runner  515 Oct  4 15:23 tsconfig.spec.json
-rw-r--r-- 1 runner runner  496 Oct  4 15:23 tsdown.config.ts
-rw-r--r-- 1 runner runner  720 Oct  4 15:23 vitest.config.ts
[0m
