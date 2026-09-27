
===== REPOSCAN 2026-09-27 23:08:12 UTC =====
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
drwxr-xr-x 15 runner runner 4096 Sep 27 23:06 .
drwxr-xr-x  4 runner runner 4096 Sep 27 23:06 ..
drwxr-xr-x  9 runner runner 4096 Sep 27 23:06 compare-stt
drwxr-xr-x  9 runner runner 4096 Sep 27 23:06 docs
drwxr-xr-x  7 runner runner 4096 Sep 27 23:06 gladia-cli
drwxr-xr-x 11 runner runner 4096 Sep 27 23:06 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Sep 27 23:06 gladia-samples
drwxr-xr-x  9 runner runner 4096 Sep 27 23:06 gladiaflow
drwxr-xr-x  7 runner runner 4096 Sep 27 23:06 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Sep 27 23:06 normalization
drwxr-xr-x 12 runner runner 4096 Sep 27 23:06 num2words2
drwxr-xr-x  9 runner runner 4096 Sep 27 23:06 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Sep 27 23:06 sdk
drwxr-xr-x  7 runner runner 4096 Sep 27 23:06 skills
drwxr-xr-x 18 runner runner 4096 Sep 27 23:06 vercel-ai
[0m
[0m✱ [0mGrep "(sk-|ghp_|gho_|ghu_|ghs_|ghr_|xox[baprs]-|gladia[_-]?key|api[_-]?key|secret|token|password)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(sk-|ghp_|gho_|ghu_|ghs_|ghr_|xox[baprs]-|gladia[_-]?key|api[_-]?key|secret|token|password)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "test-api-key|secret123|access123|refresh123|mocked-token|dynamic-session-token|test-session-token|async-session-token|test-token|invalid-key|explicit-key|custom-key"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts[90m [limit=200, offset=730][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [limit=50, offset=160][0m
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/
total 328
drwxr-xr-x 10 runner runner   4096 Sep 27 23:06 .
drwxr-xr-x 15 runner runner   4096 Sep 27 23:06 ..
drwxr-xr-x  3 runner runner   4096 Sep 27 23:06 .cursor
-rw-r--r--  1 runner runner    135 Sep 27 23:06 .editorconfig
drwxr-xr-x  8 runner runner   4096 Sep 27 23:06 .git
-rw-r--r--  1 runner runner    212 Sep 27 23:06 .gitattributes
drwxr-xr-x  3 runner runner   4096 Sep 27 23:06 .github
-rw-r--r--  1 runner runner    191 Sep 27 23:06 .gitignore
-rw-r--r--  1 runner runner    113 Sep 27 23:06 .npmrc
-rw-r--r--  1 runner runner    103 Sep 27 23:06 .prettierignore
-rw-r--r--  1 runner runner    127 Sep 27 23:06 .prettierrc
drwxr-xr-x  2 runner runner   4096 Sep 27 23:06 .vscode
-rw-r--r--  1 runner runner   3032 Sep 27 23:06 CONTRIBUTING.md
-rw-r--r--  1 runner runner   1063 Sep 27 23:06 LICENSE
-rw-r--r--  1 runner runner  10963 Sep 27 23:06 README.md
-rw-r--r--  1 runner runner     98 Sep 27 23:06 audit-ci.jsonc
-rw-r--r--  1 runner runner 219285 Sep 27 23:06 bun.lock
-rw-r--r--  1 runner runner     29 Sep 27 23:06 bunfig.toml
-rw-r--r--  1 runner runner    239 Sep 27 23:06 commitlint.config.cts
drwxr-xr-x  2 runner runner   4096 Sep 27 23:06 data
drwxr-xr-x  6 runner runner   4096 Sep 27 23:06 e2e
-rw-r--r--  1 runner runner   1358 Sep 27 23:06 eslint.config.mjs
-rw-r--r--  1 runner runner   3525 Sep 27 23:06 nx.json
-rw-r--r--  1 runner runner   1062 Sep 27 23:06 package.json
drwxr-xr-x  5 runner runner   4096 Sep 27 23:06 packages
drwxr-xr-x  3 runner runner   4096 Sep 27 23:06 tools
-rw-r--r--  1 runner runner     86 Sep 27 23:06 vitest.workspace.mjs
[0m
[0m→ [0mRead reposcan-raw/gladiaio/sdk/README.md[90m [limit=100][0m
[0m✱ [0mGrep "gladia"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m→ [0mRead reposcan-raw/gladiaio/sdk/package.json
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/package.json
[0m
[0m$ [0mls -la /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/
total 272
drwxr-xr-x 68 runner runner 4096 Sep 27 23:06 .
drwxr-xr-x 18 runner runner 4096 Sep 27 23:06 ..
drwxr-xr-x  6 runner runner 4096 Sep 27 23:06 ai
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 alibaba
drwxr-xr-x  5 runner runner 4096 Sep 27 23:06 amazon-bedrock
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 angular
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 anthropic
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 anthropic-aws
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 assemblyai
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 azure
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 baseten
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 black-forest-labs
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 bytedance
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 cerebras
drwxr-xr-x  4 runner runner 4096 Sep 27 23:06 codemod
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 cohere
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 deepgram
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 deepinfra
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 deepseek
drwxr-xr-x  5 runner runner 4096 Sep 27 23:06 devtools
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 elevenlabs
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 fal
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 fireworks
drwxr-xr-x  4 runner runner 4096 Sep 27 23:06 gateway
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 gladia
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 google
drwxr-xr-x  6 runner runner 4096 Sep 27 23:06 google-vertex
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 groq
drwxr-xr-x  6 runner runner 4096 Sep 27 23:06 harness
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 harness-claude-code
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 harness-codex
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 harness-pi
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 huggingface
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 hume
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 klingai
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 langchain
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 llamaindex
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 lmnt
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 luma
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 mcp
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 mistral
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 moonshotai
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 open-responses
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 openai
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 openai-compatible
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 otel
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 perplexity
drwxr-xr-x  4 runner runner 4096 Sep 27 23:06 policy-opa
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 prodia
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 provider
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 provider-utils
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 quiverai
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 react
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 replicate
drwxr-xr-x  3 runner runner 4096 Sep 27 23:06 revai
drwxr-xr-x  5 runner runner 4096 Sep 27 23:06 rsc
