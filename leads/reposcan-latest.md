
===== REPOSCAN 2026-10-07 16:37:55 UTC =====
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
drwxr-xr-x 15 runner runner 4096 Oct  7 16:34 .
drwxr-xr-x  4 runner runner 4096 Oct  7 16:34 ..
drwxr-xr-x  9 runner runner 4096 Oct  7 16:34 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct  7 16:34 docs
drwxr-xr-x  7 runner runner 4096 Oct  7 16:34 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct  7 16:34 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct  7 16:34 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct  7 16:34 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct  7 16:34 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct  7 16:34 normalization
drwxr-xr-x 12 runner runner 4096 Oct  7 16:34 num2words2
drwxr-xr-x  9 runner runner 4096 Oct  7 16:34 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct  7 16:34 sdk
drwxr-xr-x  7 runner runner 4096 Oct  7 16:34 skills
drwxr-xr-x 18 runner runner 4096 Oct  7 16:34 vercel-ai
[0m
[0m$ [0mgrep -r "gladia" reposcan-raw/gladiaio/sdk --include="*.json" --include="*.ts" --include="*.js" 2>/dev/null | head -50
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/live_v2_session.test.ts:} from '@gladiaio/sdk'
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/live_v2_session.test.ts:import { parseAudioFile, sendAudioFile } from '@gladiaio/sdk-e2e-javascript-fixtures'
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/prerecorded_v2_async.test.ts:} from '@gladiaio/sdk'
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/prerecorded_v2_async.test.ts:import { getDataFile } from '@gladiaio/sdk-e2e-javascript-fixtures'
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/live_v2_job_management.test.ts:import { GladiaClient, type LiveV2Response } from '@gladiaio/sdk'
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/test/live_v2_job_management.test.ts:import { parseAudioFile, sendAudioFile } from '@gladiaio/sdk-e2e-javascript-fixtures'
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/package.json:  "name": "@gladiaio/sdk-e2e-node-esm",
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/package.json:    "@gladiaio/sdk": "workspace:*",
reposcan-raw/gladiaio/sdk/e2e/e2e-node-esm/package.json:    "@gladiaio/sdk-e2e-javascript-fixtures": "workspace:*"
reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/src/index.ts:import type { LiveV2InitRequest, LiveV2Session } from '@gladiaio/sdk'
reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/package.json:  "name": "@gladiaio/sdk-e2e-javascript-fixtures",
reposcan-raw/gladiaio/sdk/e2e/javascript-fixtures/package.json:    "@gladiaio/sdk": "workspace:*",
reposcan-raw/gladiaio/sdk/e2e/e2e-node-cjs/package.json:  "name": "@gladiaio/sdk-e2e-node-cjs",
reposcan-raw/gladiaio/sdk/e2e/e2e-node-cjs/package.json:    "@gladiaio/sdk": "workspace:*",
reposcan-raw/gladiaio/sdk/e2e/e2e-node-cjs/package.json:    "@gladiaio/sdk-e2e-javascript-fixtures": "workspace:*"
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    const gladiaClient = new GladiaClient({
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    gladiaClient.liveV2()
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    expect(call.httpHeaders['x-gladia-version']).toContain(`SdkJavascript/${SDK_VERSION}`)
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    const gladiaClient = new GladiaClient({
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    gladiaClient.liveV2()
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    expect(httpHeaders['x-gladia-version']).toBe(`MyApp/1.2.3 SdkJavascript/${SDK_VERSION}`)
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:  it('injects x-gladia-key when apiKey is set', () => {
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    const gladiaClient = new GladiaClient({ apiKey: 'key-123' })
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    gladiaClient.liveV2()
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    expect(httpHeaders['x-gladia-key']).toBe('key-123')
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    const gladiaClient = new GladiaClient({ httpHeaders: { 'x-base': 'a' }, apiKey: 'abc' })
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    gladiaClient.liveV2({ httpHeaders: { 'x-override': 'b' } })
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    expect(httpHeaders['x-gladia-key']).toBe('abc')
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    expect(httpHeaders['x-gladia-version']).toContain(`SdkJavascript/${SDK_VERSION}`)
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:  it('per-call options merge with gladia version', () => {
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    const gladiaClient = new GladiaClient({
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:      httpHeaders: { 'x-gladia-version': 'GladiaClient/1.2.3' },
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    gladiaClient.liveV2({ httpHeaders: { 'x-gladia-version': 'LiveClient/4.5.6' } })
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    expect(httpHeaders['x-gladia-key']).toBe('abc')
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/client.test.ts:    expect(httpHeaders['x-gladia-version']).toContain(
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts: * x-gladia-key must not be forwarded on cross-origin redirects.
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:  it('does not forward x-gladia-key when HttpClient follows a cross-origin redirect', async () => {
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:        'x-gladia-key': secretKey,
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:        'x-gladia-version': 'SdkJavascript/test',
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    expect(originCaptured[0]?.headers['x-gladia-key']).toBe(secretKey)
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    expect(captured[0]?.headers['x-gladia-key']).toBeUndefined()
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    expect(captured[0]?.headers['x-gladia-version']).toBe('SdkJavascript/test')
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:  it('does not forward x-gladia-key when preRecorded.getFile follows a cross-origin redirect', async () => {
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    const gladia = new GladiaClient({
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    const bytes = await gladia.preRecorded().getFile('job-id')
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    expect(captured[0]?.headers['x-gladia-key']).toBeUndefined()
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:  it('does not forward x-gladia-key when live.getFile follows a cross-origin redirect', async () => {
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    const gladia = new GladiaClient({
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    const bytes = await gladia.live().getFile('job-id')
reposcan-raw/gladiaio/sdk/packages/sdk-js/src/network/httpClient.redirect.test.ts:    expect(captured[0]?.headers['x-gladia-key']).toBeUndefined()
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts[90m [offset=160, limit=30][0m
[0m
[0m$ [0mnpm view gladia@0.1.3 2>/dev/null | head -30
gladia@0.1.3 | MIT | deps: none | versions: 4
Official TypeScript SDK for Gladia - State-of-the-art Speech to Text API
https://github.com/alexisbouchez/gladia.ts#readme

keywords: gladia, speech-to-text, transcription, audio, video, ai, typescript, sdk

dist
.tarball: https://registry.npmjs.org/gladia/-/gladia-0.1.3.tgz
.shasum: cc96f84a200c0fd49a71e919391f9b659c39f3e9
.integrity: sha512-56NWQ9pEVyd/E+jwafDydzcopimFayKQatP6oz0tL5EF5v9aQLAQ6P03H93nEqZCiD10UqqZMR1c6GaC3YBztw==
.unpackedSize: 225.8 kB

maintainers:
- softwarecitadel <softwarecitadel@gmail.com>

dist-tags:
latest: 0.1.3

published a year ago by softwarecitadel <softwarecitadel@gmail.com>
[0m
[0m$ [0mnpm view @gladiaio/sdk@latest 2>/dev/null | head -20
@gladiaio/sdk@2.1.0 | MIT | deps: none | versions: 24
Gladia JavaScript/TypeScript SDK
https://github.com/gladiaio/sdk#readme

keywords: gladia, sdk, typescript, javascript

dist
.tarball: https://registry.npmjs.org/@gladiaio/sdk/-/sdk-2.1.0.tgz
.shasum: 7c0ec413a1cff8f7e0d3d54a41ec4ab165802f47
.integrity: sha512-Wh4gI8mnsEny/mq3hco1Hy/M2ckQfuLaYNLOX22J2+m0LTiP+U466Y5TemDZML+v78Y+9NpDnVwkPwVowBetTg==
.unpackedSize: 868.1 kB

maintainers:
- clement-gladia <ccharmet@gladia.io>
- gladia-admin <tech-certified@gladia.io>
- commarla <lcommarieu@gladia.io>
- hugo_gladia <himbert@gladia.io>
- tnesztler <picobuntu@gmail.com>
- amorin_gladia <amorin@gladia.io>
[0m
[0m$ [0mgrep -r "gladia" reposcan-raw/gladiaio/vercel-ai/.github/tigent.yml
provider/openai, provider/anthropic, provider/google, provider/google-vertex, provider/azure, provider/amazon-bedrock, provider/xai, provider/mistral, provider/cohere, provider/groq, provider/deepseek, provider/fireworks, provider/togetherai, provider/perplexity, provider/replicate, provider/huggingface, provider/cerebras, provider/deepinfra, provider/baseten, provider/fal, provider/luma, provider/black-forest-labs, provider/gateway, provider/vercel, provider/assemblyai, provider/deepgram, provider/elevenlabs, provider/gladia, provider/hume, provider/lmnt, provider/revai, provider/openai-compatible, provider/community.
[0m
