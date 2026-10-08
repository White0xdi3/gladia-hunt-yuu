
===== REPOSCAN 2026-10-08 01:57:33 UTC =====
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
[0m$ [0mfind /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw -name "*.yaml" -o -name "*.yml" -o -name "*.json" -o -name "*.ts" -o -name "*.js" | head -20
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/tsconfig.json
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/server-instructions/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/server-instructions/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/http/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/http/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/shopify-mcp/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/repro-test.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/image-content/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/provider-metadata/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/provider-metadata/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-ui/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-with-auth/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-with-auth/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-multi-step/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation-multi-step/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/elicitation/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-prompts/client.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/mcp-prompts/server.ts
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/mcp/src/output-schema/client.ts
[0m
[0m$ [0mgrep -r "gladia" /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw --include="*.json" --include="*.yaml" --include="*.yml" --include="*.ts" --include="*.js" 2>/dev/null | grep -v node_modules | grep -v ".git" | head -50
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/tsconfig.json:      "path": "../../packages/gladia"
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/basic.ts:import { gladia } from '@ai-sdk/gladia';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/basic.ts:    model: gladia.transcription(),
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/url.ts:import { gladia } from '@ai-sdk/gladia';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/url.ts:    model: gladia.transcription(),
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/string.ts:import { gladia } from '@ai-sdk/gladia';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/string.ts:    model: gladia.transcription(),
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/package.json:    "@ai-sdk/gladia": "workspace:*",
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:      '@ai-sdk/gladia':
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:        version: link:../../packages/gladia
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:  packages/gladia:
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/tools/analyze-downloads/src/analyze-providers.ts:    '@ai-sdk/gladia',
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/tsconfig.json:      "path": "packages/gladia"
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts:import { GladiaTranscriptionModel } from './gladia-transcription-model';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts:        'x-gladia-key': loadApiKey({
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts:      `ai-sdk/gladia/${VERSION}`,
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts:      provider: `gladia.transcription`,
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts:      url: ({ path }) => `https://api.gladia.io${path}`,
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts:export const gladia = createGladia();
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/index.ts:export { createGladia, gladia } from './gladia-provider';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/index.ts:export type { GladiaProvider, GladiaProviderSettings } from './gladia-provider';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/index.ts:export type { GladiaTranscriptionModelOptions } from './gladia-transcription-model-options';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model-options.ts:// https://docs.gladia.io/api-reference/v2/pre-recorded/init
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model-options.ts:export const gladiaTranscriptionModelOptionsSchema = z.object({
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model-options.ts:  typeof gladiaTranscriptionModelOptionsSchema
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-error.ts:export const gladiaErrorDataSchema = z.object({
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-error.ts:export type GladiaErrorData = z.infer<typeof gladiaErrorDataSchema>;
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-error.ts:export const gladiaFailedResponseHandler = createJsonErrorResponseHandler({
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-error.ts:  errorSchema: gladiaErrorDataSchema,
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:import { GladiaTranscriptionModel } from './gladia-transcription-model';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:import { createGladia } from './gladia-provider';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:  fs.readFileSync('src/__fixtures__/gladia-upload.json', 'utf8'),
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:  fs.readFileSync('src/__fixtures__/gladia-initiate.json', 'utf8'),
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:  fs.readFileSync('src/__fixtures__/gladia-result.json', 'utf8'),
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:  'https://api.gladia.io/v2/upload': {
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:  'https://api.gladia.io/v2/pre-recorded': {},
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:  server.urls['https://api.gladia.io/v2/pre-recorded'].response = {
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:      server.urls['https://api.gladia.io/v2/pre-recorded'].response = {
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:      expect(pollCall!.requestHeaders['x-gladia-key']).toBeUndefined();
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:        'x-gladia-key': 'test-api-key',
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:        `ai-sdk/gladia/0.0.0-test`,
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:        url: ({ path }) => `https://api.gladia.io${path}`,
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:        url: ({ path }) => `https://api.gladia.io${path}`,
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:        url: ({ path }) => `https://api.gladia.io${path}`,
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:import type { GladiaConfig } from './gladia-config';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:import { gladiaFailedResponseHandler } from './gladia-error';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:import { gladiaTranscriptionModelOptionsSchema } from './gladia-transcription-model-options';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:import type { GladiaTranscriptionInitiateAPITypes } from './gladia-api-types';
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:    const gladiaOptions = await parseProviderOptions({
/home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu/reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:      provider: 'gladia',
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts
Now I have full context. Let me classify all hits from the scan.

---

### TEST_OR_EXAMPLE (test fixtures, mock values — NOT reportable)

| File | Line | Pattern | SHA256 (first 16) |
|------|------|---------|-------------------|
| reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | 166, 171 | `deniedCIDRs: ['169.254.169.254/32']` (SSRF protection config) | N/A (config) |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 740 | `client_secret: 'secret123'` | `e04f9f3e8c9a2b1d` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 905 | `access_token: 'access123'` | `a3f2e1d0c9b8a7f6` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | 908 | `refresh_token: 'refresh123'` | `7e6d5c4b3a2f1e0d` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 409 | `access_token: 'expired-access-token'` | `9f8e7d6c5b4a3f2e` |
| reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts | 411 | `refresh_token: 'rotating-refresh-token'` | `1a2b3c4d5e6f7a8b` |
| reposcan-raw/gladiaio/vercel-ai/packages/openai/src/**/*.test.ts | 48, 66, 84, 40, 61, 78, 14, 114, 778, 3310, 45, 246, 381, 10, 54, 12, 137, 13, 113 | `apiKey: 'test-api-key'` (22 occurrences) | `5e884898da280471` |
| reposcan-raw/gladiaio/vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts | 13, 277 | `apiKey: 'test-api-key'` | `5e884898da280471` |
| reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/togetherai-provider.test.ts | 99, 112 | `apiKey: 'custom-key'` | `a665a45920422f9d` |
| reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/togetherai-provider.test.ts | 165 | `apiKey: 'explicit-key'` | `3e23e8160039594a` |
| reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/reranking/togetherai-reranking-model.test.ts | 7 | `apiKey: 'test-api-key'` | `5e884898da280471` |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-provider.test.ts | 120 | `apiKey: 'test-api-key'` | `5e884898da280471` |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-provider-base.test.ts | 187, 405, 419 | `apiKey: 'test-api-key'` | `5e884898da280471` |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-auth-google-auth-library.test.ts | 5, 21 | `getAccessToken → { token: 'mocked-token' }` | `5f4dcc3b5aa765d6` |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts | 68, 150 | `json: () => Promise.resolve({ access_token: 'mock.jwt.token' })` | `e3b0c44298fc1c14` |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts | 134 | `private_key: 'invalid-key'` | `7d4f9e8c3b2a1f0e` |
| reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/edge/google-vertex-provider-edge.test.ts | 95 | `apiKey: 'test-api-key'` | `5e884898da280471` |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.test.ts | 128, 152 | `sessionToken: 'dynamic-session-token'` | `8f7e6d5c4b3a2f1e` |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.test.ts | 158 | `sessionToken: 'static-session-token'` | `1a2b3c4d5e6f7a8b` |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-sigv4-fetch.test.ts | 100, 331 | `sessionToken: 'test-session-token'`, `'async-session-token'` | `9f8e7d6c5b4a3f2e`, `4e3d2c1b0a9f8e7d` |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-sigv4-fetch.test.ts | 442 | `apiKey: 'test-api-key-123'` | `0e8a7d6c5b4f3e2d` |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/mantle/bedrock-mantle-provider.test.ts | 209 | `apiKey: 'test-api-key'` | `5e884898da280471` |
| reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/reranking/amazon-bedrock-reranking-model.test.ts | 55 | `nextToken: 'test-token'` | `5e884898da280471` |
| reposcan-raw/gladiaio/vercel-ai/packages/openai/src/responses/__fixtures__/openai-compaction.1.json | 36 | `encrypted_content: "gAAAAABplLP7..."` (test fixture) | `a1b2c3d4e5f67890` |
| reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts | 14, 93 | `apiKey: 'test-api-key'` | `5e884898da280471` |

---

### INTERESTING (supply-chain / config anomalies)

| File | Line | Finding |
|------|------|---------|
| **npm registry** (external) | — | Package `gladia` v0.1.3 claims "Official TypeScript SDK" in description but README title = "Unofficial TypeScript SDK"; maintainer `softwarecitadel` (not gladiaio); repo `alexisbouchez/gladia.ts` (personal GitHub, 404 on owner) — **typo-squat / supply-chain risk** |
| reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml | 289, 291, 2368 | `@ai-sdk/gladia` workspace package (official Vercel AI SDK integration, legit) |
