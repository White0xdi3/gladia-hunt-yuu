
===== REPOSCAN 2026-10-05 02:01:03 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && ls -la reposcan-raw/gladiaio/
total 60
drwxr-xr-x 15 runner runner 4096 Oct  5 01:59 .
drwxr-xr-x  4 runner runner 4096 Oct  5 01:59 ..
drwxr-xr-x  9 runner runner 4096 Oct  5 01:59 compare-stt
drwxr-xr-x  9 runner runner 4096 Oct  5 01:59 docs
drwxr-xr-x  7 runner runner 4096 Oct  5 01:59 gladia-cli
drwxr-xr-x 11 runner runner 4096 Oct  5 01:59 gladia-quiz-app
drwxr-xr-x 11 runner runner 4096 Oct  5 01:59 gladia-samples
drwxr-xr-x  9 runner runner 4096 Oct  5 01:59 gladiaflow
drwxr-xr-x  7 runner runner 4096 Oct  5 01:59 n8n-nodes-gladia
drwxr-xr-x  8 runner runner 4096 Oct  5 01:59 normalization
drwxr-xr-x 12 runner runner 4096 Oct  5 01:59 num2words2
drwxr-xr-x  9 runner runner 4096 Oct  5 01:59 realtime-multilingual-asr-router
drwxr-xr-x 10 runner runner 4096 Oct  5 01:59 sdk
drwxr-xr-x  7 runner runner 4096 Oct  5 01:59 skills
drwxr-xr-x 18 runner runner 4096 Oct  5 01:59 vercel-ai
[0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml[90m [limit=30, offset=280][0m
[0m→ [0mRead reposcan-raw/gladiaio/vercel-ai/pnpm-lock.yaml[90m [offset=2360, limit=30][0m
[0m✱ [0mGlob "**/packages/gladia/**/*"[90m in reposcan-raw/gladiaio/vercel-ai · 24 matches[0m
[0m
[0m$ [0mnpm view @gladiaio/sdk --json 2>/dev/null | head -100
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
    "0.10.11": "2023-01-11T09:01:49.220Z",
    "0.10.12": "2023-01-11T13:12:36.873Z",
    "0.10.13": "2023-01-11T21:12:54.881Z",
    "0.10.14": "2023-01-12T09:10:07.435Z",
    "0.10.15": "2023-01-17T10:19:35.165Z",
    "0.10.16": "2023-01-17T12:05:23.330Z",
    "0.10.17": "2023-01-17T12:58:17.730Z",
    "0.10.18": "2023-01-17T16:09:20.768Z",
    "0.10.19": "2023-01-18T15:26:15.155Z",
    "0.10.20": "2023-01-18T18:04:32.626Z",
    "0.10.21": "2023-01-20T08:16:14.497Z",
    "0.10.22": "2023-01-20T10:04:28.819Z",
    "0.10.23": "2023-01-20T15:04:40.649Z",
    "0.10.24": "2023-01-20T15:11:16.682Z",
    "0.10.25": "2023-01-20T15:13:48.025Z",
    "0.10.26": "2023-01-20T15:31:50.478Z",
    "0.10.27": "2023-01-20T15:39:56.257Z",
    "0.10.28": "2023-01-20T15:42:19.092Z",
    "0.10.29": "2023-01-20T15:50:28.108Z",
    "0.10.30": "2023-01-24T08:25:37.753Z",
    "0.10.31": "2023-01-27T09:03:39.648Z",
    "0.10.32": "2023-01-27T13:42:54.782Z",
    "0.10.33": "2023-01-30T16:53:45.752Z",
    "0.10.34": "2023-01-31T10:05:22.344Z",
    "0.10.35": "2023-01-31T16:26:08.125Z",
    "0.10.36": "2023-01-31T18:05:57.019Z",
    "0.10.37": "2023-02-01T09:07:05.551Z",
    "0.10.38": "2023-02-08T13:16:19.390Z",
    "0.10.39": "2023-02-09T11:04:51.004Z",
    "0.10.40": "2023-02-10T16:05:17.732Z",
    "0.10.41": "2023-02-10T16:39:30.367Z",
    "0.10.42": "2023-02-13T20:05:28.053Z",
    "0.10.43": "2023-02-14T14:05:13.700Z",
    "0.10.44": "2023-02-14T15:41:25.199Z",
