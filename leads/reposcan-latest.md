
===== REPOSCAN 2026-10-11 08:47:46 UTC =====
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
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/package.json
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -n "169.254.169.254" reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts -A2 -B2
164-        mode: 'custom',
165-        allowedHosts: ['api.example.com'],
166:        deniedCIDRs: ['169.254.169.254/32'],
167-      });
168-      expect(spies.update).toHaveBeenCalledWith({
169-        networkPolicy: {
170-          allow: ['api.example.com'],
171:          subnets: { deny: ['169.254.169.254/32'] },
172-        },
173-      });
[0m
Now I have full context. The `vercel-ai` repo is a fork of the Vercel AI SDK with Gladia provider integration. All hits are from test files, fixtures, and config. Let me classify:
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && head -50 reposcan-raw/gladiaio/vercel-ai/packages/gladia/package.json
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
    "!src/**/*.test.ts",
    "!src/**/*.test-d.ts",
    "!src/**/__snapshots__",
    "!src/**/__fixtures__",
    "CHANGELOG.md",
    "README.md"
  ],
  "directories": {
    "doc": "./docs"
  },
  "scripts": {
    "build": "tsup --tsconfig tsconfig.build.json",
    "build:watch": "tsup --tsconfig tsconfig.build.json --watch",
    "clean": "del-cli dist docs",
    "prepack": "mkdir -p docs && cp ../../content/providers/01-ai-sdk-providers/120-gladia.mdx ./docs/",
    "postpack": "del-cli docs",
    "type-check": "tsc --noEmit",
    "test": "pnpm test:node && pnpm test:edge",
    "test:watch": "vitest --config vitest.node.config.js",
    "test:edge": "vitest --config vitest.edge.config.js --run",
    "test:node": "vitest --config vitest.node.config.js --run",
    "test:node:watch": "vitest --config vitest.node.config.js --watch"
  },
  "exports": {
    "./package.json": "./package.json",
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "default": "./dist/index.js"
    }
  },
  "dependencies": {
    "@ai-sdk/provider": "workspace:*",
    "@ai-sdk/provider-utils": "workspace:*"
  },
  "devDependencies": {
    "@ai-sdk/test-server": "workspace:*",
    "@types/node": "22.19.19",
[0m
---

## CLASSIFICATION TABLES

### TEST_OR_EXAMPLE (test fixtures, mock credentials — **not reportable**)

| File | Line | Pattern | Context |
|------|------|---------|---------|
| `packages/mcp/src/tool/oauth.test.ts` | 740 | `client_secret: 'secret123'` | OAuth test fixture |
| `packages/mcp/src/tool/oauth.test.ts` | 905 | `access_token: 'access123'` | OAuth test fixture |
| `packages/mcp/src/tool/oauth.test.ts` | 908 | `refresh_token: 'refresh123'` | OAuth test fixture |
| `packages/mcp/src/tool/mcp-http-transport.test.ts` | 409 | `access_token: 'expired-access-token'` | HTTP transport test |
| `packages/mcp/src/tool/mcp-http-transport.test.ts` | 411 | `refresh_token: 'rotating-refresh-token'` | HTTP transport test |
| `packages/openai/src/**/*.test.ts` | 100+ | `apiKey: 'test-api-key'` | OpenAI provider tests (dozens of occurrences) |
| `packages/assemblyai/src/assemblyai-transcription-model.test.ts` | 13, 277 | `apiKey: 'test-api-key'` | AssemblyAI provider tests |
| `packages/togetherai/src/*.test.ts` | 99, 112, 165 | `apiKey: 'custom-key'`, `'explicit-key'`, `'test-api-key'` | TogetherAI provider tests |
| `packages/google-vertex/src/*.test.ts` | 120, 187, 405, 419 | `apiKey: 'test-api-key'` | Google Vertex tests |
| `packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts` | 68, 150 | `access_token: 'mock.jwt.token'` | Edge auth mock |
| `packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts` | 134 | `private_key: 'invalid-key'` | Negative test case |
| `packages/amazon-bedrock/src/*.test.ts` | 100, 152, 158, 331, 442 | `sessionToken: 'test-session-token'`, `'dynamic-session-token'`, `'static-session-token'`, `'async-session-token'`, `apiKey: 'test-api-key-123'` | Bedrock tests |
| `packages/amazon-bedrock/src/mantle/bedrock-mantle-provider.test.ts` | 209 | `apiKey: 'test-api-key'` | Mantle provider test |
| `packages/amazon-bedrock/src/reranking/amazon-bedrock-reranking-model.test.ts` | 55 | `nextToken: 'test-token'` | Pagination test |
| `packages/openai/src/responses/__fixtures__/openai-compaction.1.json` | 36 | `encrypted_content: "gAAAAABplLP..."` | Encrypted fixture blob |

---

### INTERESTING (security-relevant config, SSRF defenses, internal package refs)

