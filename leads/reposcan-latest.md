
===== REPOSCAN 2026-09-29 12:52:23 UTC =====
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
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/
total 272
drwxr-xr-x 68 runner runner 4096 Sep 29 12:47 .
drwxr-xr-x 18 runner runner 4096 Sep 29 12:47 ..
drwxr-xr-x  6 runner runner 4096 Sep 29 12:47 ai
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 alibaba
drwxr-xr-x  5 runner runner 4096 Sep 29 12:47 amazon-bedrock
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 angular
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 anthropic
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 anthropic-aws
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 assemblyai
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 azure
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 baseten
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 black-forest-labs
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 bytedance
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 cerebras
drwxr-xr-x  4 runner runner 4096 Sep 29 12:47 codemod
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 cohere
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 deepgram
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 deepinfra
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 deepseek
drwxr-xr-x  5 runner runner 4096 Sep 29 12:47 devtools
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 elevenlabs
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 fal
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 fireworks
drwxr-xr-x  4 runner runner 4096 Sep 29 12:47 gateway
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 gladia
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 google
drwxr-xr-x  6 runner runner 4096 Sep 29 12:47 google-vertex
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 groq
drwxr-xr-x  6 runner runner 4096 Sep 29 12:47 harness
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 harness-claude-code
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 harness-codex
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 harness-pi
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 huggingface
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 hume
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 klingai
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 langchain
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 llamaindex
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 lmnt
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 luma
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 mcp
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 mistral
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 moonshotai
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 open-responses
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 openai
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 openai-compatible
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 otel
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 perplexity
drwxr-xr-x  4 runner runner 4096 Sep 29 12:47 policy-opa
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 prodia
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 provider
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 provider-utils
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 quiverai
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 react
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 replicate
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 revai
drwxr-xr-x  5 runner runner 4096 Sep 29 12:47 rsc
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 sandbox-just-bash
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 sandbox-vercel
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 svelte
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 test-server
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 togetherai
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 tui
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 valibot
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 vercel
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 voyage
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 vue
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 workflow
drwxr-xr-x  3 runner runner 4096 Sep 29 12:47 xai
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/
total 72
drwxr-xr-x  3 runner runner  4096 Sep 29 12:47 .
drwxr-xr-x 68 runner runner  4096 Sep 29 12:47 ..
-rw-r--r--  1 runner runner 26407 Sep 29 12:47 CHANGELOG.md
-rw-r--r--  1 runner runner  1376 Sep 29 12:47 README.md
-rw-r--r--  1 runner runner  2030 Sep 29 12:47 package.json
drwxr-xr-x  4 runner runner  4096 Sep 29 12:47 src
-rw-r--r--  1 runner runner   139 Sep 29 12:47 tsconfig.build.json
-rw-r--r--  1 runner runner   404 Sep 29 12:47 tsconfig.json
-rw-r--r--  1 runner runner   337 Sep 29 12:47 tsup.config.ts
-rw-r--r--  1 runner runner   119 Sep 29 12:47 turbo.json
-rw-r--r--  1 runner runner   328 Sep 29 12:47 vitest.edge.config.js
-rw-r--r--  1 runner runner   320 Sep 29 12:47 vitest.node.config.js
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/
total 120
drwxr-xr-x 4 runner runner  4096 Sep 29 12:47 .
drwxr-xr-x 3 runner runner  4096 Sep 29 12:47 ..
drwxr-xr-x 2 runner runner  4096 Sep 29 12:47 __fixtures__
drwxr-xr-x 2 runner runner  4096 Sep 29 12:47 __snapshots__
-rw-r--r-- 1 runner runner  5100 Sep 29 12:47 gladia-api-types.ts
