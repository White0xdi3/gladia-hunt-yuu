
===== REPOSCAN 2026-10-10 07:19:32 UTC =====
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
drwxr-xr-x 15 runner runner 4096 Oct 10 07:13 .
drwxr-xr-x  4 runner runner 4096 Oct 10 07:13 ..
drwxr-xr-x  9 runner runner 4096 Oct 10 07:13 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct 10 07:13 docs
drwxr-xr-x  7 runner runner 4096 Oct 10 07:13 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct 10 07:13 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct 10 07:13 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct 10 07:13 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct 10 07:13 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct 10 07:13 normalization
drwxr-xr-x 12 runner runner 4096 Oct 10 07:13 num2words2
drwxr-xr-x  9 runner runner 4096 Oct 10 07:13 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct 10 07:13 sdk
drwxr-xr-x  7 runner runner 4096 Oct 10 07:13 skills
drwxr-xr-x 18 runner runner 4096 Oct 10 07:13 vercel-ai
[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*["'][^"']{8,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*["'][^"']{8,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*["'][^"']{8,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*["'][^"']{8,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*["'][^"']{8,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*["'][^"']{8,}"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "169\.254\.169\.254"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "redirect[_-]?to|return[_-]?to|next[_-]?url|continue[_-]?url"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "graphql|introspection"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "upload|multipart|file.*input"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "jwt|jws|jwe|alg.*none|key.*confusion"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "x-gladia-key|api[_-]?key|websocket|ws://|wss://"[90m in reposcan-raw/gladiaio/sdk · 100 matches[0m
[0m✱ [0mGrep "redirect|oauth|state|nonce"[90m in reposcan-raw/gladiaio/sdk · 84 matches[0m
[0m
[0m$ [0mfind /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk -name "*.ts" -o -name "*.js" -o -name "*.py" | head -50
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/vitest.config.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/live_v2_session.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/prerecorded_v2_async.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/live_v2_job_management.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/tsdown.config.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/src/index.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-python/tests/conftest.py
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-python/tests/helpers.py
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-python/tests/test_live_v2_session.py
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-python/tests/test_live_v2_job_management.py
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-python/tests/test_prerecorded_v2_async.py
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-python/tests/__init__.py
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/e2e/e2e-python/tests/test_live_v2_async_session.py
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/tsdown.config.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/vitest.config.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/version.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/internal_types.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/helpers.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/wsClient.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/types.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/iso-ws.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/iso-fetch.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/wsClient.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/build-list-url.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.list.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.start-session.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/generated-types.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/types.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/index.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/session.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/session.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/build-list-url.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/prerecorded/client.list.test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/prerecorded/generated-types.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/prerecorded/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/prerecorded/index.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/types.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-js/src/index.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/conftest.py
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/test_client.py
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/network/test_async_http_client.py
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/network/test_helper.py
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/network/test_async_websocket_client.py
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/network/test_http_client_redirect.py
[0m
[0m$ [0mcat /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml | head -350
lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: false

overrides:
  tinyexec: 1.0.2
  oxlint: 1.56.0

importers:

  .:
    devDependencies:
      '@changesets/cli':
        specifier: 2.27.10
        version: 2.27.10
      '@playwright/test':
        specifier: ^1.60.0
        version: 1.60.0
      del-cli:
        specifier: ^5.1.0
        version: 5.1.0
      husky:
        specifier: ^9.1.7
        version: 9.1.7
      konsistent:
        specifier: 0.0.1-alpha.20
        version: 0.0.1-alpha.20
      konsistent-provider:
        specifier: workspace:*
        version: link:tools/konsistent-provider
