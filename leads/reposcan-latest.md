
===== REPOSCAN 2026-10-10 18:35:50 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -r "test-api-key\|custom-key\|explicit-key\|mocked-token\|mock.jwt.token\|invalid-key\|dynamic-session-token\|static-session-token\|async-session-token\|test-api-key-123" reposcan-raw/gladiaio/vercel-ai --include="*.ts" --include="*.json" | head -50
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/generate-text/openai/tool-order.ts:  apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/generate-text/google/tool-order.ts:  apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/generate-text/anthropic/tool-order.ts:  apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/files/openai-files.test.ts:    const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/files/openai-files.test.ts:    const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/files/openai-files.test.ts:    const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/files/openai-files.test.ts:    const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/files/openai-files.test.ts:    const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/files/openai-files.test.ts:      apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/files/openai-files.test.ts:      authorization: 'Bearer test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/files/openai-files.test.ts:    const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/files/openai-files.test.ts:    const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/openai-provider.test.ts:        apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/openai-provider.test.ts:        apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/openai-provider.test.ts:        apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/image/openai-image-model.test.ts:const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/image/openai-image-model.test.ts:      apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/image/openai-image-model.test.ts:      authorization: 'Bearer test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/chat/openai-chat-language-model.test.ts:  apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/chat/openai-chat-language-model.test.ts:      apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/chat/openai-chat-language-model.test.ts:      authorization: 'Bearer test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/chat/openai-chat-language-model.test.ts:      apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/chat/openai-chat-language-model.test.ts:      authorization: 'Bearer test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/completion/openai-completion-language-model.test.ts:  apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/completion/openai-completion-language-model.test.ts:    const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/completion/openai-completion-language-model.test.ts:      apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/completion/openai-completion-language-model.test.ts:      authorization: 'Bearer test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/completion/openai-completion-language-model.test.ts:      apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/completion/openai-completion-language-model.test.ts:      authorization: 'Bearer test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/speech/openai-speech-model.test.ts:const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/speech/openai-speech-model.test.ts:      apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/speech/openai-speech-model.test.ts:      authorization: 'Bearer test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/embedding/openai-embedding-model.test.ts:const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/embedding/openai-embedding-model.test.ts:      apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/embedding/openai-embedding-model.test.ts:      authorization: 'Bearer test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/skills/openai-skills.test.ts:const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/skills/openai-skills.test.ts:        authorization: 'Bearer test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/transcription/openai-transcription-model.test.ts:const provider = createOpenAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/transcription/openai-transcription-model.test.ts:      apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/transcription/openai-transcription-model.test.ts:      authorization: 'Bearer test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts:const provider = createAssemblyAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts:      apiKey: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/assemblyai/src/assemblyai-transcription-model.test.ts:      authorization: 'test-api-key',
reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/reranking/togetherai-reranking-model.test.ts:const provider = createTogetherAI({ apiKey: 'test-api-key' });
reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/reranking/togetherai-reranking-model.test.ts:          "authorization": "Bearer test-api-key",
reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/reranking/togetherai-reranking-model.test.ts:          "authorization": "Bearer test-api-key",
reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/togetherai-provider.test.ts:        apiKey: 'custom-key',
reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/togetherai-provider.test.ts:        apiKey: 'custom-key',
reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/togetherai-provider.test.ts:      const provider = createTogetherAI({ apiKey: 'explicit-key' });
reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/togetherai-provider.test.ts:        apiKey: 'explicit-key',
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -n "mocked-token\|mock.jwt.token\|invalid-key\|dynamic-session-token\|static-session-token\|async-session-token\|test-api-key-123\|nextToken\|secret123\|access123\|refresh123\|expired-access-token\|rotating-refresh-token" reposcan-raw/gladiaio/vercel-ai --include="*.ts" -r
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:740:    client_secret: 'secret123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:905:    access_token: 'access123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:908:    refresh_token: 'refresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:924:    client_secret: 'secret123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:957:    expect(body.get('client_secret')).toBe('secret123');
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1034:        access_token: 'access123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1104:    expect(body.get('client_secret')).toBe('secret123');
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1161:    access_token: 'newaccess123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1167:    refresh_token: 'newrefresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1179:    client_secret: 'secret123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1193:      refreshToken: 'refresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1213:    expect(body.get('refresh_token')).toBe('refresh123');
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1215:    expect(body.get('client_secret')).toBe('secret123');
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1229:      refreshToken: 'refresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1271:    expect(body.get('refresh_token')).toBe('refresh123');
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1288:    const refreshToken = 'refresh123';
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1303:        access_token: 'newaccess123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1310:        refreshToken: 'refresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1329:        refreshToken: 'refresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1343:      refreshToken: 'refresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1370:      refreshToken: 'refresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1388:    client_secret: 'secret123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1426:        client_secret: 'secret123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1674:            access_token: 'access123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1677:            refresh_token: 'refresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1747:            access_token: 'new-access123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1767:      refresh_token: 'refresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:1789:    expect(body.get('refresh_token')).toBe('refresh123');
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:2221:            access_token: 'access123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:2224:            refresh_token: 'refresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:2291:            access_token: 'new-access123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:2309:      refresh_token: 'refresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:2332:    expect(body.get('refresh_token')).toBe('refresh123');
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:2442:        client_secret: 'secret123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:2475:    access_token: 'access123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts:2478:    refresh_token: 'refresh123',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts:409:      access_token: 'expired-access-token',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts:411:      refresh_token: 'rotating-refresh-token',
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts:444:          if (headers.get('authorization') === 'Bearer expired-access-token') {
reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/mcp-http-transport.test.ts:509:            refresh_token: `rotating-refresh-token-${refreshRequests.length}`,
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/responses/openai-responses-prepare-tools.test.ts:1132:                      value: 'secret123',
reposcan-raw/gladiaio/vercel-ai/packages/openai/src/responses/openai-responses-prepare-tools.test.ts:1161:                      "value": "secret123",
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-auth-google-auth-library.test.ts:5:const getAccessToken = vi.fn().mockResolvedValue({ token: 'mocked-token' });
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-auth-google-auth-library.test.ts:21:    getAccessToken.mockResolvedValue({ token: 'mocked-token' });
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-auth-google-auth-library.test.ts:29:    expect(token).toBe('mocked-token');
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts:68:      json: () => Promise.resolve({ access_token: 'mock.jwt.token' }),
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts:134:      private_key: 'invalid-key',
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts:150:      json: () => Promise.resolve({ access_token: 'mock.jwt.token' }),
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts:200:      json: () => Promise.resolve({ access_token: 'mock.jwt.token' }),
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts:228:      json: () => Promise.resolve({ access_token: 'mock.jwt.token' }),
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts:275:      json: () => Promise.resolve({ access_token: 'mock.jwt.token' }),
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/edge/google-vertex-auth-edge.test.ts:293:      json: () => Promise.resolve({ access_token: 'mock.jwt.token' }),
reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.test.ts:128:        sessionToken: 'dynamic-session-token',
reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.test.ts:152:        sessionToken: 'dynamic-session-token',
reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.test.ts:158:        sessionToken: 'static-session-token',
reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-provider.test.ts:447:          sessionToken: 'dynamic-session-token',
reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-sigv4-fetch.test.ts:331:        sessionToken: 'async-session-token',
reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-sigv4-fetch.test.ts:357:    expect(headers['x-amz-security-token']).toEqual('async-session-token');
reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-sigv4-fetch.test.ts:442:    const apiKey = 'test-api-key-123';
reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/amazon-bedrock-sigv4-fetch.test.ts:459:        Authorization: 'Bearer test-api-key-123',
reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/reranking/amazon-bedrock-reranking-api.ts:6:  nextToken?: string;
reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/reranking/amazon-bedrock-reranking-api.ts:41:      nextToken: z.string().optional(),
reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/reranking/amazon-bedrock-reranking-model.test.ts:55:            nextToken: 'test-token',
reposcan-raw/gladiaio/vercel-ai/packages/amazon-bedrock/src/reranking/amazon-bedrock-reranking-model.test.ts:67:          "nextToken": "test-token",
