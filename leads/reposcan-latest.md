
===== REPOSCAN 2026-10-11 02:00:02 UTC =====
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
[0m$ [0mls -la reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Oct 11 01:57 .
drwxr-xr-x  4 runner runner 4096 Oct 11 01:57 ..
drwxr-xr-x  9 runner runner 4096 Oct 11 01:57 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct 11 01:57 docs
drwxr-xr-x  7 runner runner 4096 Oct 11 01:57 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct 11 01:57 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct 11 01:57 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct 11 01:57 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct 11 01:57 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct 11 01:57 normalization
drwxr-xr-x 12 runner runner 4096 Oct 11 01:57 num2words2
drwxr-xr-x  9 runner runner 4096 Oct 11 01:57 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct 11 01:57 sdk
drwxr-xr-x  7 runner runner 4096 Oct 11 01:57 skills
drwxr-xr-x 18 runner runner 4096 Oct 11 01:57 vercel-ai
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/vercel-ai/packages/
total 272
drwxr-xr-x 68 runner runner 4096 Oct 11 01:57 .
drwxr-xr-x 18 runner runner 4096 Oct 11 01:57 ..
drwxr-xr-x  6 runner runner 4096 Oct 11 01:57 ai
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 alibaba
drwxr-xr-x  5 runner runner 4096 Oct 11 01:57 amazon-bedrock
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 angular
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 anthropic
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 anthropic-aws
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 assemblyai
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 azure
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 baseten
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 black-forest-labs
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 bytedance
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 cerebras
drwxr-xr-x  4 runner runner 4096 Oct 11 01:57 codemod
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 cohere
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 deepgram
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 deepinfra
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 deepseek
drwxr-xr-x  5 runner runner 4096 Oct 11 01:57 devtools
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 elevenlabs
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 fal
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 fireworks
drwxr-xr-x  4 runner runner 4096 Oct 11 01:57 gateway
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 gladia
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 google
drwxr-xr-x  6 runner runner 4096 Oct 11 01:57 google-vertex
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 groq
drwxr-xr-x  6 runner runner 4096 Oct 11 01:57 harness
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 harness-claude-code
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 harness-codex
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 harness-pi
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 huggingface
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 hume
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 klingai
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 langchain
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 llamaindex
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 lmnt
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 luma
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 mcp
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 mistral
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 moonshotai
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 open-responses
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 openai
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 openai-compatible
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 otel
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 perplexity
drwxr-xr-x  4 runner runner 4096 Oct 11 01:57 policy-opa
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 prodia
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 provider
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 provider-utils
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 quiverai
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 react
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 replicate
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 revai
drwxr-xr-x  5 runner runner 4096 Oct 11 01:57 rsc
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 sandbox-just-bash
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 sandbox-vercel
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 svelte
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 test-server
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 togetherai
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 tui
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 valibot
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 vercel
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 voyage
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 vue
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 workflow
drwxr-xr-x  3 runner runner 4096 Oct 11 01:57 xai
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/vercel-ai/packages/gladia/
total 72
drwxr-xr-x  3 runner runner  4096 Oct 11 01:57 .
drwxr-xr-x 68 runner runner  4096 Oct 11 01:57 ..
-rw-r--r--  1 runner runner 26407 Oct 11 01:57 CHANGELOG.md
-rw-r--r--  1 runner runner  1376 Oct 11 01:57 README.md
-rw-r--r--  1 runner runner  2030 Oct 11 01:57 package.json
drwxr-xr-x  4 runner runner  4096 Oct 11 01:57 src
-rw-r--r--  1 runner runner   139 Oct 11 01:57 tsconfig.build.json
-rw-r--r--  1 runner runner   404 Oct 11 01:57 tsconfig.json
-rw-r--r--  1 runner runner   337 Oct 11 01:57 tsup.config.ts
-rw-r--r--  1 runner runner   119 Oct 11 01:57 turbo.json
-rw-r--r--  1 runner runner   328 Oct 11 01:57 vitest.edge.config.js
-rw-r--r--  1 runner runner   320 Oct 11 01:57 vitest.node.config.js
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/
total 120
drwxr-xr-x 4 runner runner  4096 Oct 11 01:57 .
drwxr-xr-x 3 runner runner  4096 Oct 11 01:57 ..
drwxr-xr-x 2 runner runner  4096 Oct 11 01:57 __fixtures__
drwxr-xr-x 2 runner runner  4096 Oct 11 01:57 __snapshots__
-rw-r--r-- 1 runner runner  5100 Oct 11 01:57 gladia-api-types.ts
-rw-r--r-- 1 runner runner   285 Oct 11 01:57 gladia-config.ts
-rw-r--r-- 1 runner runner  1197 Oct 11 01:57 gladia-error.test.ts
-rw-r--r-- 1 runner runner   462 Oct 11 01:57 gladia-error.ts
-rw-r--r-- 1 runner runner  2841 Oct 11 01:57 gladia-provider.ts
