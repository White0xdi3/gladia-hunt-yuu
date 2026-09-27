
===== REPOSCAN 2026-09-27 07:27:00 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && ls -la reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Sep 27 07:23 .
drwxr-xr-x  4 runner runner 4096 Sep 27 07:23 ..
drwxr-xr-x  9 runner runner 4096 Sep 27 07:23 compare-stt
drwxr-xr-x  9 runner runner 4096 Sep 27 07:23 docs
drwxr-xr-x  7 runner runner 4096 Sep 27 07:23 gladia-cli
drwxr-xr-x 11 runner runner 4096 Sep 27 07:23 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Sep 27 07:23 gladia-samples
drwxr-xr-x  9 runner runner 4096 Sep 27 07:23 gladiaflow
drwxr-xr-x  7 runner runner 4096 Sep 27 07:23 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Sep 27 07:23 normalization
drwxr-xr-x 12 runner runner 4096 Sep 27 07:23 num2words2
drwxr-xr-x  9 runner runner 4096 Sep 27 07:23 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Sep 27 07:23 sdk
drwxr-xr-x  7 runner runner 4096 Sep 27 07:23 skills
drwxr-xr-x 18 runner runner 4096 Sep 27 07:23 vercel-ai
[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]"[90m in reposcan-raw · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]"[90m in reposcan-raw · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]"[90m in reposcan-raw · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]"[90m in reposcan-raw · 0 matches[0m
[0m✱ [0mGrep "sk-[a-zA-Z0-9]{32,}"[90m in reposcan-raw · 0 matches[0m
[0m✱ [0mGrep "gh[pousr]_[a-zA-Z0-9]{36,}"[90m in reposcan-raw · 0 matches[0m
[0m✱ [0mGrep "gladia[_-]?key"[90m in reposcan-raw · 4 matches[0m
[0m✱ [0mGrep "169\.254\.169\.254"[90m in reposcan-raw · 4 matches[0m
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && ls -la reposcan-raw/gladiaio/vercel-ai/packages/
total 272
drwxr-xr-x 68 runner runner 4096 Sep 27 07:23 .
drwxr-xr-x 18 runner runner 4096 Sep 27 07:23 ..
drwxr-xr-x  6 runner runner 4096 Sep 27 07:23 ai
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 alibaba
drwxr-xr-x  5 runner runner 4096 Sep 27 07:23 amazon-bedrock
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 angular
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 anthropic
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 anthropic-aws
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 assemblyai
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 azure
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 baseten
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 black-forest-labs
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 bytedance
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 cerebras
drwxr-xr-x  4 runner runner 4096 Sep 27 07:23 codemod
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 cohere
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 deepgram
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 deepinfra
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 deepseek
drwxr-xr-x  5 runner runner 4096 Sep 27 07:23 devtools
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 elevenlabs
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 fal
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 fireworks
drwxr-xr-x  4 runner runner 4096 Sep 27 07:23 gateway
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 gladia
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 google
drwxr-xr-x  6 runner runner 4096 Sep 27 07:23 google-vertex
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 groq
drwxr-xr-x  6 runner runner 4096 Sep 27 07:23 harness
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 harness-claude-code
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 harness-codex
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 harness-pi
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 huggingface
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 hume
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 klingai
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 langchain
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 llamaindex
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 lmnt
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 luma
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 mcp
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 mistral
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 moonshotai
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 open-responses
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 openai
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 openai-compatible
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 otel
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 perplexity
drwxr-xr-x  4 runner runner 4096 Sep 27 07:23 policy-opa
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 prodia
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 provider
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 provider-utils
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 quiverai
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 react
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 replicate
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 revai
drwxr-xr-x  5 runner runner 4096 Sep 27 07:23 rsc
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 sandbox-just-bash
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 sandbox-vercel
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 svelte
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 test-server
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 togetherai
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 tui
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 valibot
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 vercel
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 voyage
drwxr-xr-x  3 runner runner 4096 Sep 27 07:23 vue
