
===== REPOSCAN 2026-10-03 19:54:03 UTC =====
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
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [limit=30, offset=160][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts[90m [offset=735, limit=30][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts[90m [limit=20, offset=405][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml[90m [limit=20, offset=285][0m
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/
total 72
drwxr-xr-x  3 runner runner  4096 Oct  3 19:50 .
drwxr-xr-x 68 runner runner  4096 Oct  3 19:50 ..
-rw-r--r--  1 runner runner 26407 Oct  3 19:50 CHANGELOG.md
-rw-r--r--  1 runner runner  1376 Oct  3 19:50 README.md
-rw-r--r--  1 runner runner  2030 Oct  3 19:50 package.json
drwxr-xr-x  4 runner runner  4096 Oct  3 19:50 src
-rw-r--r--  1 runner runner   139 Oct  3 19:50 tsconfig.build.json
-rw-r--r--  1 runner runner   404 Oct  3 19:50 tsconfig.json
-rw-r--r--  1 runner runner   337 Oct  3 19:50 tsup.config.ts
-rw-r--r--  1 runner runner   119 Oct  3 19:50 turbo.json
-rw-r--r--  1 runner runner   328 Oct  3 19:50 vitest.edge.config.js
-rw-r--r--  1 runner runner   320 Oct  3 19:50 vitest.node.config.js
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/
total 120
drwxr-xr-x 4 runner runner  4096 Oct  3 19:50 .
drwxr-xr-x 3 runner runner  4096 Oct  3 19:50 ..
drwxr-xr-x 2 runner runner  4096 Oct  3 19:50 __fixtures__
drwxr-xr-x 2 runner runner  4096 Oct  3 19:50 __snapshots__
-rw-r--r-- 1 runner runner  5100 Oct  3 19:50 gladia-api-types.ts
-rw-r--r-- 1 runner runner   285 Oct  3 19:50 gladia-config.ts
-rw-r--r-- 1 runner runner  1197 Oct  3 19:50 gladia-error.test.ts
-rw-r--r-- 1 runner runner   462 Oct  3 19:50 gladia-error.ts
-rw-r--r-- 1 runner runner  2841 Oct  3 19:50 gladia-provider.ts
-rw-r--r-- 1 runner runner  7021 Oct  3 19:50 gladia-transcription-model-options.ts
-rw-r--r-- 1 runner runner  6112 Oct  3 19:50 gladia-transcription-model.test.ts
-rw-r--r-- 1 runner runner 12356 Oct  3 19:50 gladia-transcription-model.ts
-rw-r--r-- 1 runner runner   269 Oct  3 19:50 index.ts
-rw-r--r-- 1 runner runner 40169 Oct  3 19:50 transcript-test.mp3
-rw-r--r-- 1 runner runner   235 Oct  3 19:50 version.ts
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/
total 32
drwxr-xr-x 2 runner runner  4096 Oct  3 19:50 .
drwxr-xr-x 4 runner runner  4096 Oct  3 19:50 ..
-rw-r--r-- 1 runner runner   145 Oct  3 19:50 gladia-initiate.json
-rw-r--r-- 1 runner runner 15491 Oct  3 19:50 gladia-result.json
-rw-r--r-- 1 runner runner   292 Oct  3 19:50 gladia-upload.json
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/__fixtures__/gladia-initiate.json
[0m
[0m$ [0mfind /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio -type f \( -name "*.env*" -o -name "*.secret*" -o -name "*secret*" -o -name "*credential*" -o -name "*token*" \) 2>/dev/null | head -20
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/.env.example
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nuxt-openai/.env.example
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-openai-telemetry-sentry/.env.local.example
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-google-vertex/.env.local.example
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/xai-tts-demo/.env.example
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-workflow/.env.local.example
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/fastify/.env.example
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/node-http-server/.env.example
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next/.env.local.example
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/nest/.env.example
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-agent/.env.local.example
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/generate-text/openai/cached-prompt-tokens.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/generate-text/google/modality-token-details.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/generate-text/anthropic/auth-token.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/stream-text/openai/cached-prompt-tokens.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/stream-text/openai/output-object-token-usage.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/stream-text/google/modality-token-details.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/.env.example
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/next-fastapi/.env.local.example
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/hono/.env.example
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/examples/mcp/.env.example
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/
total 328
drwxr-xr-x 10 runner runner   4096 Oct  3 19:50 .
drwxr-xr-x 15 runner runner   4096 Oct  3 19:50 ..
drwxr-xr-x  3 runner runner   4096 Oct  3 19:50 .cursor
-rw-r--r--  1 runner runner    135 Oct  3 19:50 .editorconfig
drwxr-xr-x  8 runner runner   4096 Oct  3 19:50 .git
-rw-r--r--  1 runner runner    212 Oct  3 19:50 .gitattributes
drwxr-xr-x  3 runner runner   4096 Oct  3 19:50 .github
-rw-r--r--  1 runner runner    191 Oct  3 19:50 .gitignore
-rw-r--r--  1 runner runner    113 Oct  3 19:50 .npmrc
-rw-r--r--  1 runner runner    103 Oct  3 19:50 .prettierignore
-rw-r--r--  1 runner runner    127 Oct  3 19:50 .prettierrc
drwxr-xr-x  2 runner runner   4096 Oct  3 19:50 .vscode
-rw-r--r--  1 runner runner   3032 Oct  3 19:50 CONTRIBUTING.md
-rw-r--r--  1 runner runner   1063 Oct  3 19:50 LICENSE
-rw-r--r--  1 runner runner  10963 Oct  3 19:50 README.md
-rw-r--r--  1 runner runner     98 Oct  3 19:50 audit-ci.jsonc
-rw-r--r--  1 runner runner 219285 Oct  3 19:50 bun.lock
