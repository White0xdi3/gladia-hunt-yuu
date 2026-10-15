
===== REPOSCAN 2026-10-15 22:25:28 UTC =====
## Grep hits:
SCAN SUMMARY: 5696 code/config files scanned, 660 hits
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
drwxr-xr-x 15 runner runner 4096 Oct 15 22:24 .
drwxr-xr-x  4 runner runner 4096 Oct 15 22:24 ..
drwxr-xr-x  9 runner runner 4096 Oct 15 22:24 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct 15 22:24 docs
drwxr-xr-x  7 runner runner 4096 Oct 15 22:24 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct 15 22:24 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct 15 22:24 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct 15 22:24 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct 15 22:24 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct 15 22:24 normalization
drwxr-xr-x 12 runner runner 4096 Oct 15 22:24 num2words2
drwxr-xr-x  9 runner runner 4096 Oct 15 22:24 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct 15 22:24 sdk
drwxr-xr-x  7 runner runner 4096 Oct 15 22:24 skills
drwxr-xr-x 18 runner runner 4096 Oct 15 22:24 vercel-ai
[0m
[0m$ [0mgrep -r "gladia" reposcan-raw/gladiaio/vercel-ai/packages/gladia/ 2>/dev/null | head -50
reposcan-raw/gladiaio/vercel-ai/packages/gladia/CHANGELOG.md:# @ai-sdk/gladia
reposcan-raw/gladiaio/vercel-ai/packages/gladia/CHANGELOG.md:- 7948763: fix(provider/gladia): Invalid `model` param removed
reposcan-raw/gladiaio/vercel-ai/packages/gladia/CHANGELOG.md:- 7948763: fix(provider/gladia): Invalid `model` parameter being passed
reposcan-raw/gladiaio/vercel-ai/packages/gladia/CHANGELOG.md:  fix(provider/gladia): `experimental_transcribe` fails with valid Buffer
reposcan-raw/gladiaio/vercel-ai/packages/gladia/CHANGELOG.md:- 84d4b2b: fix (provider/gladia): correct workspace dependencies
reposcan-raw/gladiaio/vercel-ai/packages/gladia/CHANGELOG.md:- cf822aa: feat(providers/gladia): add transcribe
reposcan-raw/gladiaio/vercel-ai/packages/gladia/CHANGELOG.md:- 84d4b2b: fix (provider/gladia): correct workspace dependencies
reposcan-raw/gladiaio/vercel-ai/packages/gladia/CHANGELOG.md:- cf822aa: feat(providers/gladia): add transcribe
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
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:import { GladiaTranscriptionModel } from './gladia-transcription-model';
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:import { createGladia } from './gladia-provider';
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:  fs.readFileSync('src/__fixtures__/gladia-upload.json', 'utf8'),
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:  fs.readFileSync('src/__fixtures__/gladia-initiate.json', 'utf8'),
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:  fs.readFileSync('src/__fixtures__/gladia-result.json', 'utf8'),
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:  'https://api.gladia.io/v2/upload': {
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:  'https://api.gladia.io/v2/pre-recorded': {},
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:  server.urls['https://api.gladia.io/v2/pre-recorded'].response = {
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:      server.urls['https://api.gladia.io/v2/pre-recorded'].response = {
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:      expect(pollCall!.requestHeaders['x-gladia-key']).toBeUndefined();
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:        'x-gladia-key': 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:        `ai-sdk/gladia/0.0.0-test`,
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:        url: ({ path }) => `https://api.gladia.io${path}`,
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:        url: ({ path }) => `https://api.gladia.io${path}`,
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.test.ts:        url: ({ path }) => `https://api.gladia.io${path}`,
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:import type { GladiaConfig } from './gladia-config';
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:import { gladiaFailedResponseHandler } from './gladia-error';
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:import { gladiaTranscriptionModelOptionsSchema } from './gladia-transcription-model-options';
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:import type { GladiaTranscriptionInitiateAPITypes } from './gladia-api-types';
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:    const gladiaOptions = await parseProviderOptions({
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:      provider: 'gladia',
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:      schema: gladiaTranscriptionModelOptionsSchema,
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:    if (gladiaOptions) {
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:      body.context_prompt = gladiaOptions.contextPrompt ?? undefined;
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:      body.custom_vocabulary = gladiaOptions.customVocabulary ?? undefined;
reposcan-raw/gladiaio/vercel-ai/packages/gladia/src/gladia-transcription-model.ts:      body.detect_language = gladiaOptions.detectLanguage ?? undefined;
[0m
[0m$ [0mgrep -r "api.gladia.io\|x-gladia-key\|gladia.key\|GLADIA" reposcan-raw/gladiaio/sdk/ 2>/dev/null | head -50
reposcan-raw/gladiaio/sdk/.github/workflows/ci.yml:  GLADIA_API_KEY: ${{ secrets.GLADIA_API_KEY }}
reposcan-raw/gladiaio/sdk/.github/workflows/update-openapi-types.yml:            https://api.gladia.io/openapi.json
reposcan-raw/gladiaio/sdk/README.md:The generator (`packages/generator`) is central to this repo. It fetches the Gladia [OpenAPI schema](https://api.gladia.io/openapi.json) and produces typed definitions for each SDK:
reposcan-raw/gladiaio/sdk/README.md:OpenAPI schema (api.gladia.io/openapi.json)
reposcan-raw/gladiaio/sdk/README.md:   This fetches the latest OpenAPI schema from `https://api.gladia.io/openapi.json`, runs the generator for both Live V2 and PreRecorded V2, and auto-formats the output.
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:  it('appends SDK version to any provided X-GLADIA-VERSION value', () => {
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:      httpHeaders: { 'X-GLADIA-VERSION': 'MyApp/1.2.3' },
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:  it('injects x-gladia-key when apiKey is set', () => {
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    expect(httpHeaders['x-gladia-key']).toBe('key-123')
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    expect(httpHeaders['x-gladia-key']).toBe('abc')
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    expect(httpHeaders['x-gladia-key']).toBe('abc')
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts: * x-gladia-key must not be forwarded on cross-origin redirects.
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:  it('does not forward x-gladia-key when HttpClient follows a cross-origin redirect', async () => {
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:        'x-gladia-key': secretKey,
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    expect(originCaptured[0]?.headers['x-gladia-key']).toBe(secretKey)
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    expect(captured[0]?.headers['x-gladia-key']).toBeUndefined()
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:  it('does not forward x-gladia-key when preRecorded.getFile follows a cross-origin redirect', async () => {
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    expect(captured[0]?.headers['x-gladia-key']).toBeUndefined()
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:  it('does not forward x-gladia-key when live.getFile follows a cross-origin redirect', async () => {
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    expect(captured[0]?.headers['x-gladia-key']).toBeUndefined()
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:  it('does not send x-gladia-key when the initial request targets another origin', async () => {
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:        'x-gladia-key': secretKey,
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    expect(captured[0]?.headers['x-gladia-key']).toBeUndefined()
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    expect(apiCaptured[0]?.headers['x-gladia-key']).toBe(secretKey)
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.test.ts:    it.each(['https://api.gladia.io', 'https://api.gladia.io/'])(
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.test.ts:          'https://api.gladia.io/v2/live/abc-123'
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.ts:const CROSS_ORIGIN_SENSITIVE_HEADERS = new Set(['x-gladia-key', 'authorization', 'cookie'])
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.list.test.ts:  first: 'https://api.gladia.io/v2/live?offset=0&limit=20',
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.list.test.ts:  current: 'https://api.gladia.io/v2/live?offset=0&limit=20',
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.list.test.ts:    apiUrl: 'https://api.gladia.io',
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.list.test.ts:    httpHeaders: { 'x-gladia-key': 'test-key' },
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.list.test.ts:    const parsed = new URL(String(url), 'https://api.gladia.io')
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.list.test.ts:    const next = 'https://api.gladia.io/v2/live?offset=20&limit=20&status=done'
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.start-session.test.ts:    apiUrl: 'https://api.gladia.io',
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.start-session.test.ts:    httpHeaders: { 'x-gladia-key': 'test-key' },
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.start-session.test.ts:      url: 'wss://api.gladia.io/v2/live/ws?token=created',
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/client.start-session.test.ts:    expect(createSessionSpy).toHaveBeenCalledWith('wss://api.gladia.io/v2/live/ws?token=created')
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/session.test.ts:      url: 'wss://api.gladia.io/v2/live/ws?token=created',
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/session.test.ts:      url: 'wss://api.gladia.io/v2/live/ws?token=abc',
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/session.test.ts:      url: 'wss://api.gladia.io/v2/live/ws?token=abc',
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/session.test.ts:        url: 'wss://api.gladia.io/v2/live/ws?token=abc',
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/session.test.ts:    expect(mockCreateSession).toHaveBeenCalledWith('wss://api.gladia.io/v2/live/ws?token=created')
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/live/session.test.ts:      url: 'wss://api.gladia.io/v2/live/ws?token=created',
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/build-list-url.test.ts:    const next = 'https://api.gladia.io/v2/pre-recorded?status=done&offset=20&limit=20'
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/build-list-url.test.ts:    expect(buildListUrl('/v2/live', { url: 'https://api.gladia.io/v2/live' })).toBe('/v2/live')
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/v2/build-list-url.test.ts:        url: 'https://api.gladia.io/v2/transcription?status=done&offset=20&limit=20',
