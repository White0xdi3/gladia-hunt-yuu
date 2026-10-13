
===== REPOSCAN 2026-10-13 15:59:05 UTC =====
## Grep hits:
SCAN SUMMARY: 5694 code/config files scanned, 657 hits
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -r "sk-" reposcan-raw/gladiaio/vercel-ai --include="*.yaml" --include="*.json" 2>/dev/null | head -5
reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:  mdast-util-gfm-task-list-item@2.0.0:
reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:  micromark-extension-gfm-task-list-item@2.1.0:
reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:  mdast-util-gfm-task-list-item@2.0.0:
reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:      mdast-util-gfm-task-list-item: 2.0.0
reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:  micromark-extension-gfm-task-list-item@2.1.0:
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -c "test-api-key\|secret123\|access123\|refresh123\|mocked-token\|custom-key\|explicit-key\|dynamic-session-token\|static-session-token\|test-session-token\|async-session-token\|test-api-key-123\|test-token\|invalid-key\|mock\.jwt\.token" reposcan-raw/gladiaio/vercel-ai -r --include="*.ts" --include="*.js" 2>/dev/null
...output truncated...

Full output saved to: /home/runner/.local/share/opencode/tool-output/tool_135fd0154001qGDauF2JcvgjKI

reposcan-raw/gladiaio/vercel-ai/packages/harness/src/agent/internal/to-harness-stream.test.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/harness/src/agent/harness-agent-session.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/harness/vitest.edge.config.js:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/internal.d.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/tsup.config.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/vitest.node.config.js:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/anthropic-prepare-tools.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/bash_20241022.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/code-execution_20250825.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/memory_20250818.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/web-search_20260209.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/text-editor_20250728.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/bash_20250124.test-d.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/computer_20251124.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/text-editor_20250124.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/computer_20250124.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/advisor_20260301.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/bash_20250124.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/web-fetch-20260209.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/bash_20241022.test.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/text-editor_20250429.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/bash_20241022.test-d.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/code-execution_20260120.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/web-search_20250305.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/bash_20250124.test.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/computer_20241022.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/text-editor_20241022.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/tool-search-regex_20251119.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/tool-search-bm25_20251119.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/web-fetch-20250910.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/tool/code-execution_20250522.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/anthropic-error.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/anthropic-tools.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/version.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/anthropic-prepare-tools.test.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/map-anthropic-stop-reason.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/sanitize-json-schema.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/sanitize-json-schema.test.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/anthropic-language-model.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/anthropic-provider.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/convert-to-anthropic-prompt.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/anthropic-files.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/index.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/anthropic-files.test.ts:2
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/convert-to-anthropic-prompt.test.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/anthropic-api.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/anthropic-provider.test.ts:8
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/forward-anthropic-container-id-from-last-step.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/convert-anthropic-usage.test.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/convert-anthropic-usage.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/skills/anthropic-skills.test.ts:2
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/skills/anthropic-skills-api.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/skills/anthropic-skills.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/get-cache-control.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/anthropic-error.test.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/anthropic-language-model-options.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/anthropic-message-metadata.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/internal/index.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/src/anthropic-language-model.test.ts:37
reposcan-raw/gladiaio/vercel-ai/packages/anthropic/vitest.edge.config.js:0
reposcan-raw/gladiaio/vercel-ai/packages/gladia/tsup.config.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/gladia/vitest.node.config.js:0
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/version.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-config.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/index.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model-options.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-error.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:3
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-api-types.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-error.test.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/gladia/vitest.edge.config.js:0
reposcan-raw/gladiaio/vercel-ai/packages/codemod/tsup.config.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/codemod/scripts/scaffold-codemod.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/codemod/scripts/generate-readme.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/codemod/vitest.config.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/codemod/src/lib/transform-options.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/codemod/src/lib/upgrade.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/codemod/src/lib/transform.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/codemod/src/codemods/v6/wrap-tomodeloutput-parameter.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/codemod/src/codemods/v6/rename-converttocoremessages-to-converttomodelmessages.ts:0
reposcan-raw/gladiaio/vercel-ai/packages/codemod/src/codemods/v6/add-await-converttomodelmessages.ts:0
