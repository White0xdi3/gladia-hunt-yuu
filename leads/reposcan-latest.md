
===== REPOSCAN 2026-10-13 07:53:31 UTC =====
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
[0m✱ [0mGrep "sk-|gladia.*key|api[_-]?key|secret|token"[90m in reposcan-raw · 0 matches[0m
[0m✱ [0mGrep "sk-[a-zA-Z0-9]{20,}"[90m in reposcan-raw · 0 matches[0m
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -r "169\.254\.169\.254" reposcan-raw/ --include="*.ts" --include="*.js" --include="*.json"
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:        deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:          subnets: { deny: ['169.254.169.254/32'] },
reposcan-raw/gladiaio/vercel-ai/packages/ai/src/util/download/download.test.ts:      download({ url: new URL('http://169.254.169.254/latest/meta-data/') }),
reposcan-raw/gladiaio/vercel-ai/packages/ai/src/util/download/download.test.ts:        location: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.ts:  // e.g. ::ffff:127.0.0.1 or 64:ff9b::169.254.169.254 are blocked.
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/fetch-with-validated-redirects.test.ts:      .mockResolvedValueOnce(redirectResponse('http://169.254.169.254/'));
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/fetch-with-validated-redirects.test.ts:      .mockResolvedValueOnce(redirectWithBody('http://169.254.169.254/'));
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/download-blob.test.ts:      downloadBlob('http://169.254.169.254/latest/meta-data/'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/download-blob.test.ts:          location: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://169.254.169.254/latest/meta-data/'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:    it('should block ::ffff:169.254.169.254', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://[::ffff:169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:    it('should block NAT64 64:ff9b::169.254.169.254 (metadata)', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://[64:ff9b::169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:    it('should block NAT64 local-use 64:ff9b:1::169.254.169.254', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://[64:ff9b:1::169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/harness/src/v1/harness-v1-network-sandbox-session.test-d.ts:    deniedCIDRs: ['10.5.0.0/16', '169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/harness/src/v1/harness-v1-network-sandbox-session.test-d.ts:    deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/prodia/src/prodia-video-model.test.ts:            url: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/prodia/src/prodia-video-model.test.ts:        server.calls.some(call => call.requestUrl.includes('169.254.169.254')),
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.ts
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio/sdk -type f \( -name "*.ts" -o -name "*.js" -o -name "*.json" \) | head -30
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
reposcan-raw/gladiaio/sdk/e2e/e2e-python/project.json
reposcan-raw/gladiaio/sdk/nx.json
reposcan-raw/gladiaio/sdk/packages/sdk-js/tsdown.config.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/tsconfig.spec.json
reposcan-raw/gladiaio/sdk/packages/sdk-js/project.json
reposcan-raw/gladiaio/sdk/packages/sdk-js/vitest.config.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/tsconfig.json
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/version.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/internal_types.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/helpers.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/wsClient.test.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.test.ts
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/types.ts
[0m
[0m✱ [0mGrep "websocket|ws://|wss://|api[_-]?key|secret|token"[90m in reposcan-raw/gladiaio/sdk · 57 matches[0m
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
[0m✱ [0mGrep "sk-[a-zA-Z0-9]{20,}|ghp_[a-zA-Z0-9]{36}|gladia[_-]?key|api[_-]?key.*=.*['\"][a-zA-Z0-9]{20,}['\"]"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "staging|internal|dev\.|localhost:[0-9]{4}|127\.0\.0\.1:[0-9]{4}|debug|test[_-]?flag"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m✱ [0mGrep "/api/v[12]|/beta|/internal|user[_-]?id|email|uid|account[_-]?id|tenant[_-]?id"[90m in reposcan-raw/gladiaio · 0 matches[0m
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio/gladia-cli -type f -name "*.go" | head -20
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
