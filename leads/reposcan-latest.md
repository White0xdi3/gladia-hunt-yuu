
===== REPOSCAN 2026-10-01 06:07:10 UTC =====
## Grep hits:
SCAN SUMMARY: 5688 code/config files scanned, 652 hits
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio -name "*.test.ts" -o -name "*.test.js" -o -name "*.spec.ts" -o -name "*.spec.js" | head -20
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/openai.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/togetherai.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/luma.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/cerebras.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/amazon-bedrock.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/google-vertex-anthropic.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/google.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/fireworks.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/amazon-bedrock-anthropic.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/gateway.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/mistral.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/deepinfra.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/deepseek.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/azure.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/huggingface.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/anthropic.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/xai.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/cohere.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/groq.test.ts
reposcan-raw/gladiaio/vercel-ai/examples/ai-functions/src/e2e/google-vertex.test.ts
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && head -50 reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts
import { describe, it, expect, vi, beforeEach, type Mock } from 'vitest';
import {
  extractResourceMetadataUrl,
  discoverOAuthProtectedResourceMetadata,
  buildDiscoveryUrls,
  discoverAuthorizationServerMetadata,
  startAuthorization,
  exchangeAuthorization,
  refreshAuthorization,
  registerClient,
  auth,
  type OAuthClientProvider,
  type AuthResult,
} from './oauth';
import type { AuthorizationServerMetadata } from './oauth-types';
import { ServerError } from '../error/oauth-error';
import { LATEST_PROTOCOL_VERSION } from './types';

// Mock the pkce-challenge module
vi.mock('pkce-challenge', () => ({
  default: vi.fn(() => ({
    code_verifier: 'test_verifier',
    code_challenge: 'test_challenge',
  })),
}));

const mockFetch = vi.fn();
global.fetch = mockFetch;

beforeEach(() => {
  mockFetch.mockReset();
});

describe('extractResourceMetadataUrl', () => {
  it('returns resource metadata url when present', async () => {
    const resourceUrl =
      'https://resource.example.com/.well-known/oauth-protected-resource';
    const mockResponse = {
      headers: {
        get: vi.fn(name =>
          name === 'WWW-Authenticate'
            ? `Bearer realm="mcp", resource_metadata="${resourceUrl}"`
            : null,
        ),
      },
    } as unknown as Response;

    expect(extractResourceMetadataUrl(mockResponse)).toEqual(
      new URL(resourceUrl),
    );
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -n "secret123\|access123\|refresh123\|test-api-key\|mocked-token\|mock.jwt.token" reposcan-raw/gladiaio/vercel-ai/packages/mcp/src/tool/oauth.test.ts reposcan-raw/gladiaio/vercel-ai/packages/openai/src/chat/openai-chat-language-model.test.ts reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-auth-edge.test.ts | head -30
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
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -n "test-api-key" reposcan-raw/gladiaio/vercel-ai/packages/openai/src/chat/openai-chat-language-model.test.ts | head -10
113:  apiKey: 'test-api-key',
778:      apiKey: 'test-api-key',
794:      authorization: 'Bearer test-api-key',
3310:      apiKey: 'test-api-key',
3327:      authorization: 'Bearer test-api-key',
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -B5 -A5 "169.254.169.254" reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts
const { sandbox, spies } = makeMockSandbox();
      const handle = await createVercelSandbox({ sandbox }).createSession();
      await handle.setNetworkPolicy!({
