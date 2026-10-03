
===== REPOSCAN 2026-10-03 11:42:47 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw -name "*.json" -o -name "*.yaml" -o -name "*.yml" -o -name "*.ts" -o -name "*.js" | head -20
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
[0m✱ [0mGrep "(sk_live|sk_test|rk_live|rk_test|pk_live|pk_test|gladia_key|x-gladia-key|GLADIA_API_KEY|api_key|secret|token|password)"[90m in reposcan-raw · 0 matches[0m
[0m✗ [0mGrep "(sk_live|sk_test|rk_live|rk_test|pk_live|pk_test|GLADIA_API_KEY|api_key|secret|token|password)" failed[90m in reposcan-raw[0m
[91m[1mError: [0mRipgrep JSON record exceeded 65536 bytes
[0m✱ [0mGrep "(sk_live|rk_live|pk_live|gladia_key.*[a-zA-Z0-9]{20,})"[90m in reposcan-raw · 2 matches[0m
[0m✱ [0mGrep "(api[_-]?key|secret|token|password)"[90m in reposcan-raw/gladiaio/sdk · 84 matches[0m
[0m✱ [0mGrep "(169\.254\.169\.254|metadata\.google\.internal|metadata\.azure\.com|http://169\.254)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(redirect|return.to|return_to|redirect_to|open.redirect|oauth.*state|state.*param)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "(graphql|introspection|__schema|file.*upload|multipart|mass.assignment|overpost|jwt|jws|jwa|alg.*none|HS256|RS256)"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && ls reposcan-raw/gladiaio/sdk/packages/
generator
sdk-js
sdk-python
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio/sdk/packages/generator -name "*.ts" -o -name "*.js" | head -20
reposcan-raw/gladiaio/sdk/packages/generator/src/helpers.ts
reposcan-raw/gladiaio/sdk/packages/generator/src/types.ts
reposcan-raw/gladiaio/sdk/packages/generator/src/generators/typescript.ts
reposcan-raw/gladiaio/sdk/packages/generator/src/generators/python.ts
reposcan-raw/gladiaio/sdk/packages/generator/src/generators/base.ts
reposcan-raw/gladiaio/sdk/packages/generator/src/cli.ts
reposcan-raw/gladiaio/sdk/packages/generator/src/schema-fetcher.ts
reposcan-raw/gladiaio/sdk/packages/generator/src/generator.ts
[0m
[0m→ [0mRead reposcan-raw/gladiaio/sdk/packages/generator/src/schema-fetcher.ts
[0m→ [0mRead reposcan-raw/gladiaio/sdk/packages/generator/src/cli.ts
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio/gladia-cli -name "*.go" | head -20
reposcan-raw/gladiaio/gladia-cli/pkg/client/client.go
reposcan-raw/gladiaio/gladia-cli/pkg/client/client_test.go
reposcan-raw/gladiaio/gladia-cli/pkg/client/transcribe_test.go
reposcan-raw/gladiaio/gladia-cli/pkg/client/transcription.go
reposcan-raw/gladiaio/gladia-cli/pkg/client/transcribe.go
reposcan-raw/gladiaio/gladia-cli/pkg/client/types/languages.go
reposcan-raw/gladiaio/gladia-cli/pkg/client/types/languages_test.go
reposcan-raw/gladiaio/gladia-cli/pkg/client/types/input.go
reposcan-raw/gladiaio/gladia-cli/cmd/formatter.go
reposcan-raw/gladiaio/gladia-cli/cmd/testhelpers_test.go
reposcan-raw/gladiaio/gladia-cli/cmd/auth.go
reposcan-raw/gladiaio/gladia-cli/cmd/transcribe_test.go
reposcan-raw/gladiaio/gladia-cli/cmd/transcribe.go
reposcan-raw/gladiaio/gladia-cli/cmd/root_test.go
reposcan-raw/gladiaio/gladia-cli/cmd/languages.go
reposcan-raw/gladiaio/gladia-cli/cmd/config.go
reposcan-raw/gladiaio/gladia-cli/cmd/formatter_test.go
reposcan-raw/gladiaio/gladia-cli/cmd/print_output_test.go
reposcan-raw/gladiaio/gladia-cli/cmd/main.go
reposcan-raw/gladiaio/gladia-cli/cmd/config_test.go
[0m
[0m→ [0mRead reposcan-raw/gladiaio/gladia-cli/cmd/auth.go
[0m→ [0mRead reposcan-raw/gladiaio/gladia-cli/pkg/client/client.go
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio/n8n-nodes-gladia -name "*.ts" -o -name "*.js" | head -20
reposcan-raw/gladiaio/n8n-nodes-gladia/jest.config.js
reposcan-raw/gladiaio/n8n-nodes-gladia/nodes/Gladia/GenericFunctions.ts
reposcan-raw/gladiaio/n8n-nodes-gladia/nodes/Gladia/test/Gladia.node.test.ts
reposcan-raw/gladiaio/n8n-nodes-gladia/nodes/Gladia/Gladia.node.ts
reposcan-raw/gladiaio/n8n-nodes-gladia/credentials/GladiaApi.credentials.ts
reposcan-raw/gladiaio/n8n-nodes-gladia/.prettierrc.js
[0m
[0m→ [0mRead reposcan-raw/gladiaio/n8n-nodes-gladia/credentials/GladiaApi.credentials.ts
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio/realtime-multilingual-asr-router -name "*.py" | head -20
reposcan-raw/gladiaio/realtime-multilingual-asr-router/scripts/download_models.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/integration/test_coordinator.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/integration/test_codeswitch_e2e.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/integration/test_reinference.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/integration/test_lid_constrained.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/integration/test_progressive_lid.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/integration/__init__.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/unit/test_websocket_lifecycle.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/unit/test_coordinator.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/unit/test_vad.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/unit/test_language_switch_detection.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/unit/test_components.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/unit/test_scheduler.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/unit/test_config.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/unit/test_session_state.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/unit/test_rollback.py
reposcan-raw/gladiaio/realtime-multilingual-asr-router/tests/unit/test_asr.py
