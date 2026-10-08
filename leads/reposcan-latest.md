
===== REPOSCAN 2026-10-08 16:30:13 UTC =====
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
[0m$ [0mcat reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts | head -180 | tail -20
const { sandbox, spies } = makeMockSandbox();
      const handle = await createVercelSandbox({ sandbox }).createSession();
      await handle.setNetworkPolicy!({
        mode: 'custom',
        allowedHosts: ['api.example.com'],
        deniedCIDRs: ['169.254.169.254/32'],
      });
      expect(spies.update).toHaveBeenCalledWith({
        networkPolicy: {
          allow: ['api.example.com'],
          subnets: { deny: ['169.254.169.254/32'] },
        },
      });
    });

    it('maps custom with both allowedCIDRs + deniedCIDRs', async () => {
      const { sandbox, spies } = makeMockSandbox();
      const handle = await createVercelSandbox({ sandbox }).createSession();
      await handle.setNetworkPolicy!({
        mode: 'custom',
[0m
[0m$ [0mcat reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts | sed -n '735,750p'
code_challenge_methods_supported: ['S256'],
  };

  const validClientInfo = {
    client_id: 'client123',
    client_secret: 'secret123',
    redirect_uris: ['http://localhost:3000/callback'],
    client_name: 'Test Client',
  };

  it('generates authorization URL with PKCE challenge', async () => {
    const { authorizationUrl, codeVerifier } = await startAuthorization(
      'https://auth.example.com',
      {
        metadata: undefined,
        clientInformation: validClientInfo,
[0m
[0m$ [0mnpm view @gladiaio/sdk --json 2>/dev/null | head -60
{
  "_id": "@gladiaio/sdk@2.1.0",
  "_rev": "133-5ce5bd29a4bef7e4ee693aad5f43610c",
  "name": "@gladiaio/sdk",
  "dist-tags": {
    "latest": "2.1.0"
  },
  "versions": [
    "0.1.0",
    "0.1.1",
    "0.1.2",
    "0.2.0",
    "0.2.1",
    "0.3.0",
    "0.3.1",
    "0.4.0",
    "0.4.1",
    "0.4.2",
    "0.4.3",
    "0.5.0",
    "0.5.1",
    "0.5.2",
    "0.5.3",
    "0.6.0",
    "0.6.1",
    "1.0.0",
    "1.0.4",
    "1.0.5",
    "1.0.7",
    "1.1.0",
    "2.0.0",
    "2.1.0"
  ],
  "time": {
    "created": "2025-09-09T15:01:20.684Z",
    "modified": "2026-09-21T14:40:50.954Z",
    "0.8.9": "2022-10-28T08:45:13.203Z",
    "0.8.10": "2022-10-28T09:20:28.511Z",
    "0.8.11": "2022-10-28T10:16:20.446Z",
    "0.8.12": "2022-11-02T13:40:47.351Z",
    "0.8.13": "2022-11-02T14:22:51.825Z",
    "0.8.14": "2022-11-10T15:46:41.656Z",
    "0.8.15": "2022-11-10T16:20:33.692Z",
    "0.8.16": "2022-11-13T18:27:04.269Z",
    "0.8.17": "2022-11-18T16:07:37.254Z",
    "0.9.1": "2022-11-22T14:38:02.436Z",
    "0.9.2": "2022-11-23T07:38:30.338Z",
    "0.9.3": "2022-11-30T09:32:14.398Z",
    "0.9.4": "2022-11-30T10:05:06.541Z",
    "0.9.5": "2022-12-09T11:31:31.615Z",
    "0.10.1": "2022-12-09T12:39:20.544Z",
    "0.10.2": "2022-12-09T14:22:43.928Z",
    "0.10.3": "2022-12-09T15:13:00.720Z",
    "0.10.4": "2022-12-09T17:23:13.026Z",
    "0.10.5": "2022-12-12T17:13:58.447Z",
    "0.10.6": "2022-12-12T17:29:59.221Z",
    "0.10.7": "2022-12-19T19:29:04.531Z",
    "0.10.8": "2023-01-10T13:24:01.450Z",
    "0.10.9": "2023-01-10T15:17:51.295Z",
    "0.10.10": "2023-01-10T15:37:49.001Z",
[0m
[0m$ [0mnpm view gladia --json 2>/dev/null | head -40
{
  "_id": "gladia@0.1.3",
  "_rev": "4-d0214ef116ff0426b738c29cf2a97cf1",
  "name": "gladia",
  "dist-tags": {
    "latest": "0.1.3"
  },
  "versions": [
    "0.1.0",
    "0.1.1",
    "0.1.2",
    "0.1.3"
  ],
  "time": {
