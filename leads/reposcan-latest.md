
===== REPOSCAN 2026-09-29 02:46:12 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && ls reposcan-raw/gladiaio/
compare-stt
docs
gladia-cli
gladia-quiz-app
gladia-samples
gladiaflow
n8n-nodes-gladia
normalization
num2words2
realtime-multilingual-asr-router
sdk
skills
vercel-ai
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && rg -r "sk-[a-zA-Z0-9]{32,}" reposcan-raw/gladiaio/ --type yaml --type json --type js --type ts --type py --type go --type rs 2>/dev/null | head -20
(no output)
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && rg -r "(api[_-]?key|secret|token|password|credential)\s*[:=]\s*[\"'][a-zA-Z0-9_\-]{20,}[\"']" reposcan-raw/gladiaio/ --type yaml --type json --type js --type ts --type py --type go --type rs 2>/dev/null | head -30
(no output)
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && rg -r "(gladia[_-]?key|x-gladia-key|GLADIA_API_KEY)" reposcan-raw/gladiaio/ --type yaml --type json --type js --type ts --type py --type go --type rs 2>/dev/null | head -30
(no output)
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio/sdk -type f \( -name "*.ts" -o -name "*.js" -o -name "*.py" -o -name "*.json" -o -name "*.yaml" -o -name "*.yml" \) | head -30
reposcan-raw/gladiaio/sdk/.cursor/mcp.json
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/project.json
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/vitest.config.ts
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/live_v2_session.test.ts
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/prerecorded_v2_async.test.ts
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/live_v2_job_management.test.ts
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/tsconfig.json
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/package.json
reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/tsdown.config.ts
reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/project.json
reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/tsconfig.json
reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/src/index.ts
reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/package.json
reposcan-raw/gladiaio/sdk/e2e/e2e-node-cjs/project.json
reposcan-raw/gladiaio/sdk/e2e/e2e-node-cjs/package.json
reposcan-raw/gladiaio/sdk/e2e/e2e-python/tests/conftest.py
reposcan-raw/gladiaio/sdk/e2e/e2e-python/tests/helpers.py
reposcan-raw/gladiaio/sdk/e2e/e2e-python/tests/test_live_v2_session.py
reposcan-raw/gladiaio/sdk/e2e/e2e-python/tests/test_live_v2_job_management.py
reposcan-raw/gladiaio/sdk/e2e/e2e-python/tests/test_prerecorded_v2_async.py
reposcan-raw/gladiaio/sdk/e2e/e2e-python/tests/__init__.py
reposcan-raw/gladiaio/sdk/e2e/e2e-python/tests/test_live_v2_async_session.py
reposcan-raw/gladiaio/sdk/e2e/e2e-python/project.json
reposcan-raw/gladiaio/sdk/.github/workflows/ci.yml
reposcan-raw/gladiaio/sdk/.github/workflows/release.yml
reposcan-raw/gladiaio/sdk/.github/workflows/publish.yml
reposcan-raw/gladiaio/sdk/.github/workflows/update-openapi-types.yml
reposcan-raw/gladiaio/sdk/nx.json
reposcan-raw/gladiaio/sdk/packages/sdk-js/tsdown.config.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/tsconfig.spec.json
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && rg -r "x-gladia-key|Authorization|Bearer|apiKey" reposcan-raw/gladiaio/sdk/packages/sdk-js/src/ 2>/dev/null | head -30
(no output)
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio/sdk/packages/sdk-js/src -type f -name "*.ts" | head -20
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/version.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/internal_types.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/helpers.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/wsClient.test.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.test.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/types.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/iso-ws.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/iso-fetch.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/wsClient.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/build-list-url.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.list.test.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.start-session.test.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/generated-types.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/types.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/index.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/session.ts
[0m
[0m→ [0mRead reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.ts
[0m→ [0mRead reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.ts
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio/sdk/packages/sdk-python -type f -name "*.py" | head -20
reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/conftest.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/test_client.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/network/test_async_http_client.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/network/test_helper.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/network/test_async_websocket_client.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/network/test_http_client_redirect.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/v2/live/test_connect_session.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/v2/live/test_live_list.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/v2/live/test_generated_types.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/v2/core/test_build_list_endpoint.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/v2/prerecorded/test_prerecorded_list.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/__init__.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/version.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/network/http_client.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/network/websocket_client.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/network/helper.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/network/__init__.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/v2/live/_helpers.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/v2/live/generated_types.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/v2/live/types.py
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio/sdk/packages/sdk-python/src -type f -name "*.py" | head -20
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/version.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/network/http_client.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/network/websocket_client.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/network/helper.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/network/__init__.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/v2/live/_helpers.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/v2/live/generated_types.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/v2/live/types.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/v2/live/async_session.py
reposcan-raw/gladiaio/sdk/packages/sdk-python/src/gladiaio_sdk/v2/live/client.py
