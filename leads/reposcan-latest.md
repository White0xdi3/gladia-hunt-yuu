
===== REPOSCAN 2026-10-15 22:17:45 UTC =====
## Grep hits:
SCAN SUMMARY: 5696 code/config files scanned, 660 hits
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
drwxr-xr-x 15 runner runner 4096 Oct 15 22:14 .
drwxr-xr-x  4 runner runner 4096 Oct 15 22:14 ..
drwxr-xr-x  9 runner runner 4096 Oct 15 22:14 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct 15 22:14 docs
drwxr-xr-x  7 runner runner 4096 Oct 15 22:14 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct 15 22:14 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct 15 22:14 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct 15 22:14 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct 15 22:14 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct 15 22:14 normalization
drwxr-xr-x 12 runner runner 4096 Oct 15 22:14 num2words2
drwxr-xr-x  9 runner runner 4096 Oct 15 22:14 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct 15 22:14 sdk
drwxr-xr-x  7 runner runner 4096 Oct 15 22:14 skills
drwxr-xr-x 18 runner runner 4096 Oct 15 22:14 vercel-ai
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/vercel-ai/packages/
total 272
drwxr-xr-x 68 runner runner 4096 Oct 15 22:14 .
drwxr-xr-x 18 runner runner 4096 Oct 15 22:14 ..
drwxr-xr-x  6 runner runner 4096 Oct 15 22:14 ai
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 alibaba
drwxr-xr-x  5 runner runner 4096 Oct 15 22:14 amazon-bedrock
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 angular
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 anthropic
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 anthropic-aws
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 assemblyai
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 azure
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 baseten
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 black-forest-labs
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 bytedance
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 cerebras
drwxr-xr-x  4 runner runner 4096 Oct 15 22:14 codemod
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 cohere
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 deepgram
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 deepinfra
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 deepseek
drwxr-xr-x  5 runner runner 4096 Oct 15 22:14 devtools
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 elevenlabs
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 fal
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 fireworks
drwxr-xr-x  4 runner runner 4096 Oct 15 22:14 gateway
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 gladia
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 google
drwxr-xr-x  6 runner runner 4096 Oct 15 22:14 google-vertex
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 groq
drwxr-xr-x  6 runner runner 4096 Oct 15 22:14 harness
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 harness-claude-code
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 harness-codex
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 harness-pi
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 huggingface
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 hume
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 klingai
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 langchain
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 llamaindex
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 lmnt
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 luma
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 mcp
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 mistral
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 moonshotai
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 open-responses
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 openai
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 openai-compatible
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 otel
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 perplexity
drwxr-xr-x  4 runner runner 4096 Oct 15 22:14 policy-opa
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 prodia
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 provider
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 provider-utils
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 quiverai
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 react
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 replicate
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 revai
drwxr-xr-x  5 runner runner 4096 Oct 15 22:14 rsc
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 sandbox-just-bash
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 sandbox-vercel
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 svelte
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 test-server
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 togetherai
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 tui
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 valibot
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 vercel
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 voyage
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 vue
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 workflow
drwxr-xr-x  3 runner runner 4096 Oct 15 22:14 xai
[0m
[0m$ [0mls -la reposcan-raw/gladiaio/vercel-ai/packages/gladia/
total 72
drwxr-xr-x  3 runner runner  4096 Oct 15 22:14 .
drwxr-xr-x 68 runner runner  4096 Oct 15 22:14 ..
-rw-r--r--  1 runner runner 26407 Oct 15 22:14 CHANGELOG.md
-rw-r--r--  1 runner runner  1376 Oct 15 22:14 README.md
-rw-r--r--  1 runner runner  2030 Oct 15 22:14 package.json
drwxr-xr-x  4 runner runner  4096 Oct 15 22:14 src
-rw-r--r--  1 runner runner   139 Oct 15 22:14 tsconfig.build.json
-rw-r--r--  1 runner runner   404 Oct 15 22:14 tsconfig.json
-rw-r--r--  1 runner runner   337 Oct 15 22:14 tsup.config.ts
-rw-r--r--  1 runner runner   119 Oct 15 22:14 turbo.json
-rw-r--r--  1 runner runner   328 Oct 15 22:14 vitest.edge.config.js
-rw-r--r--  1 runner runner   320 Oct 15 22:14 vitest.node.config.js
[0m
[0m$ [0mcat reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
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
