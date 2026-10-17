
===== REPOSCAN 2026-10-17 17:12:36 UTC =====
## Grep hits:
SCAN SUMMARY: 5699 code/config files scanned, 661 hits
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -r "gladia" reposcan-raw/gladiaio/vercel-ai --include="*.ts" --include="*.json" --include="*.yaml" | grep -v test | grep -v ".test." | head -30
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/tsconfig.json:      "path": "../../packages/gladia"
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/basic.ts:import { gladia } from '@ai-sdk/gladia';
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/basic.ts:    model: gladia.transcription(),
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/url.ts:import { gladia } from '@ai-sdk/gladia';
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/url.ts:    model: gladia.transcription(),
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/string.ts:import { gladia } from '@ai-sdk/gladia';
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/transcribe/gladia/string.ts:    model: gladia.transcription(),
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/package.json:    "@ai-sdk/gladia": "workspace:*",
reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:      '@ai-sdk/gladia':
reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:        version: link:../../packages/gladia
reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml:  packages/gladia:
reposcan-raw/gladiaio/vercel-ai/tools/analyze-downloads/src/analyze-providers.ts:    '@ai-sdk/gladia',
reposcan-raw/gladiaio/vercel-ai/tsconfig.json:      "path": "packages/gladia"
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts:import { GladiaTranscriptionModel } from './gladia-transcription-model';
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts:        'x-gladia-key': loadApiKey({
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts:      `ai-sdk/gladia/${VERSION}`,
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts:      provider: `gladia.transcription`,
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts:      url: ({ path }) => `https://api.gladia.io${path}`,
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-provider.ts:export const gladia = createGladia();
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/index.ts:export { createGladia, gladia } from './gladia-provider';
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/index.ts:export type { GladiaProvider, GladiaProviderSettings } from './gladia-provider';
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/index.ts:export type { GladiaTranscriptionModelOptions } from './gladia-transcription-model-options';
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model-options.ts:// https://docs.gladia.io/api-reference/v2/pre-recorded/init
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model-options.ts:export const gladiaTranscriptionModelOptionsSchema = z.object({
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model-options.ts:  typeof gladiaTranscriptionModelOptionsSchema
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-error.ts:export const gladiaErrorDataSchema = z.object({
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-error.ts:export type GladiaErrorData = z.infer<typeof gladiaErrorDataSchema>;
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-error.ts:export const gladiaFailedResponseHandler = createJsonErrorResponseHandler({
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-error.ts:  errorSchema: gladiaErrorDataSchema,
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:import type { GladiaConfig } from './gladia-config';
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -rn "169.254.169.254" reposcan-raw/
reposcan-raw/grep-hits.txt:8:reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:166: deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/grep-hits.txt:9:reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:171: subnets: { deny: ['169.254.169.254/32'] },
reposcan-raw/grep-hits.prev.txt:8:reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:166: deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/grep-hits.prev.txt:9:reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:171: subnets: { deny: ['169.254.169.254/32'] },
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:166:        deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:171:          subnets: { deny: ['169.254.169.254/32'] },
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/README.md:48:    subnets: { deny: ['169.254.169.254/32'] },
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/README.md:72:  deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/ai/src/util/download/download.test.ts:14:      download({ url: new URL('http://169.254.169.254/latest/meta-data/') }),
reposcan-raw/gladiaio/vercel-ai/packages/ai/src/util/download/download.test.ts:38:        location: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.ts:203:  // e.g. ::ffff:127.0.0.1 or 64:ff9b::169.254.169.254 are blocked.
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/fetch-with-validated-redirects.test.ts:79:      .mockResolvedValueOnce(redirectResponse('http://169.254.169.254/'));
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/fetch-with-validated-redirects.test.ts:108:      .mockResolvedValueOnce(redirectWithBody('http://169.254.169.254/'));
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/download-blob.test.ts:237:      downloadBlob('http://169.254.169.254/latest/meta-data/'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/download-blob.test.ts:261:          location: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:131:        validateDownloadUrl('http://169.254.169.254/latest/meta-data/'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:184:    it('should block ::ffff:169.254.169.254', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:186:        validateDownloadUrl('http://[::ffff:169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:268:    it('should block NAT64 64:ff9b::169.254.169.254 (metadata)', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:270:        validateDownloadUrl('http://[64:ff9b::169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:274:    it('should block NAT64 local-use 64:ff9b:1::169.254.169.254', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:276:        validateDownloadUrl('http://[64:ff9b:1::169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/harness/src/v1/harness-v1-network-sandbox-session.test-d.ts:68:    deniedCIDRs: ['10.5.0.0/16', '169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/harness/src/v1/harness-v1-network-sandbox-session.test-d.ts:77:    deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/prodia/src/prodia-video-model.test.ts:462:            url: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/prodia/src/prodia-video-model.test.ts:470:        server.calls.some(call => call.requestUrl.includes('169.254.169.254')),
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.list.test.ts:105:    await client.list({ url: 'http://169.254.169.254/latest/meta-data/?offset=20' })
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/build-list-url.test.ts:40:    expect(buildListUrl('/v2/live', { url: 'http://169.254.169.254/latest/meta-data/' })).toBe(
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/prerecorded/client.list.test.ts:105:    await client.list({ url: 'http://169.254.169.254/latest/meta-data/?offset=20' })
reposcan-raw/gladiaio/sdk/packages/sdk-python/tests/v2/core/test_build_list_endpoint.py:56:  assert live.build_list_endpoint({"url": "http://169.254.169.254/latest/meta-data/"}) == "/v2/live"
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && cat reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.list.test.ts | head -120
import { beforeEach, describe, expect, it, vi } from 'vitest'
import type { InternalGladiaClientOptions } from '../../internal_types.js'
import { HttpClient } from '../../network/httpClient.js'
import { LiveV2Client } from './client.js'
import type { LiveV2ListResponse } from './generated-types.js'

const listResponse: LiveV2ListResponse = {
  first: 'https://api.gladia.io/v2/live?offset=0&limit=20',
  current: 'https://api.gladia.io/v2/live?offset=0&limit=20',
  next: null,
  items: [],
}

function makeOptions(
  overrides: Partial<InternalGladiaClientOptions> = {}
): InternalGladiaClientOptions {
  return {
    apiKey: 'test-key',
    apiUrl: 'https://api.gladia.io',
    httpHeaders: { 'x-gladia-key': 'test-key' },
    httpRetry: { maxAttempts: 1, statusCodes: [], delay: () => 0 },
    httpTimeout: 10_000,
    wsRetry: {
      maxAttemptsPerConnection: 1,
      closeCodes: [],
      delay: () => 0,
      maxConnections: 1,
    },
    wsTimeout: 10_000,
    prerecordedTimeouts: {
