
===== REPOSCAN 2026-09-28 17:44:58 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && ls -la reposcan-raw/gladiaio/vercel-ai/
total 1624
drwxr-xr-x 18 runner runner    4096 Sep 28 17:42 .
drwxr-xr-x 15 runner runner    4096 Sep 28 17:42 ..
drwxr-xr-x  2 runner runner    4096 Sep 28 17:42 .agents
drwxr-xr-x  2 runner runner   28672 Sep 28 17:42 .changeset
drwxr-xr-x  2 runner runner    4096 Sep 28 17:42 .claude
drwxr-xr-x  2 runner runner    4096 Sep 28 17:42 .cursor
drwxr-xr-x  7 runner runner    4096 Sep 28 17:42 .git
drwxr-xr-x  6 runner runner    4096 Sep 28 17:42 .github
-rw-r--r--  1 runner runner     261 Sep 28 17:42 .gitignore
drwxr-xr-x  2 runner runner    4096 Sep 28 17:42 .husky
-rw-r--r--  1 runner runner     381 Sep 28 17:42 .kodiak.toml
-rw-r--r--  1 runner runner     122 Sep 28 17:42 .npmrc
-rw-r--r--  1 runner runner    1119 Sep 28 17:42 .oxfmtrc.jsonc
-rw-r--r--  1 runner runner    8967 Sep 28 17:42 .oxlintrc.json
drwxr-xr-x  2 runner runner    4096 Sep 28 17:42 .vscode
-rw-r--r--  1 runner runner   12684 Sep 28 17:42 AGENTS.md
-rw-r--r--  1 runner runner    2807 Sep 28 17:42 CHANGELOG.md
lrwxrwxrwx  1 runner runner       9 Sep 28 17:42 CLAUDE.md -> AGENTS.md
-rw-r--r--  1 runner runner     111 Sep 28 17:42 CODE_OF_CONDUCT.md
-rw-r--r--  1 runner runner    7250 Sep 28 17:42 CONTRIBUTING.md
-rw-r--r--  1 runner runner     552 Sep 28 17:42 LICENSE
lrwxrwxrwx  1 runner runner      22 Sep 28 17:42 README.md -> packages/ai/README.md

drwxr-xr-x  2 runner runner    4096 Sep 28 17:42 architecture
drwxr-xr-x  2 runner runner    4096 Sep 28 17:42 assets
drwxr-xr-x  6 runner runner    4096 Sep 28 17:42 content
drwxr-xr-x  3 runner runner    4096 Sep 28 17:42 contributing
drwxr-xr-x 27 runner runner    4096 Sep 28 17:42 examples
-rw-r--r--  1 runner runner    2818 Sep 28 17:42 package.json
drwxr-xr-x 68 runner runner    4096 Sep 28 17:42 packages
-rw-r--r--  1 runner runner 1474217 Sep 28 17:42 pnpm-lock.yaml
-rw-r--r--  1 runner runner     185 Sep 28 17:42 pnpm-workspace.yaml
drwxr-xr-x 11 runner runner    4096 Sep 28 17:42 skills
-rw-r--r--  1 runner runner     228 Sep 28 17:42 socket.yaml
drwxr-xr-x  6 runner runner    4096 Sep 28 17:42 tools
-rw-r--r--  1 runner runner    3216 Sep 28 17:42 tsconfig.json
-rw-r--r--  1 runner runner    1335 Sep 28 17:42 tsconfig.with-examples.json
-rw-r--r--  1 runner runner    2705 Sep 28 17:42 turbo.json
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && head -300 reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts
import type { Sandbox } from '@vercel/sandbox';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { createVercelSandbox } from './vercel-sandbox';

const { createMock } = vi.hoisted(() => ({ createMock: vi.fn() }));

vi.mock('@vercel/sandbox', () => ({
  Sandbox: { create: createMock },
}));

type MockSpies = {
  domain: ReturnType<typeof vi.fn>;
  update: ReturnType<typeof vi.fn>;
  runCommand: ReturnType<typeof vi.fn>;
  stop: ReturnType<typeof vi.fn>;
  delete: ReturnType<typeof vi.fn>;
  routes: Array<{ port: number }>;
};

function makeMockSandbox(overrides: Partial<MockSpies> = {}) {
  const domain = overrides.domain ?? vi.fn();
  const update = overrides.update ?? vi.fn(async () => {});
  const runCommand = overrides.runCommand ?? vi.fn();
  const stop = overrides.stop ?? vi.fn(async () => {});
  const deleteSandbox = overrides.delete ?? vi.fn(async () => {});
  const routes: Array<{ port: number }> = overrides.routes ?? [{ port: 4000 }];
  const sandbox = {
    name: 'sbx_harness',
    domain,
    update,
    runCommand,
    stop,
    delete: deleteSandbox,
    routes,
    currentSession: () => ({ cwd: '/vercel/sandbox' }),
  } as unknown as Sandbox;
  return {
    sandbox,
    spies: { domain, update, runCommand, stop, delete: deleteSandbox, routes },
  };
}

describe('createVercelSandbox (wrap existing)', () => {
  it('produces a network sandbox session whose ports come from sandbox.routes', async () => {
    const { sandbox } = makeMockSandbox({
      routes: [{ port: 3000 }, { port: 4000 }],
    });
    const provider = createVercelSandbox({ sandbox });
    const sandboxSession = await provider.createSession();
    expect(sandboxSession.ports).toEqual([3000, 4000]);
  });

  it('restricted() returns an Experimental_SandboxSession wrapping the underlying', async () => {
    const { sandbox, spies } = makeMockSandbox();
    spies.runCommand.mockResolvedValueOnce({
      exitCode: 0,
      stdout: async () => 'ok\n',
      stderr: async () => '',
    });

    const sandboxSession = await createVercelSandbox({
      sandbox,
    }).createSession();
    const result = await sandboxSession
      .restricted()
      .run({ command: 'echo ok' });
    expect(result.stdout).toBe('ok\n');
  });

  it('stop is a no-op (caller owns lifecycle)', async () => {
    const { sandbox, spies } = makeMockSandbox();
    await (await createVercelSandbox({ sandbox }).createSession()).stop();
    expect(spies.stop).not.toHaveBeenCalled();
  });

