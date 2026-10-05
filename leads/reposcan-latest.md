
===== REPOSCAN 2026-10-05 22:45:55 UTC =====
## Grep hits:
SCAN SUMMARY: 5695 code/config files scanned, 654 hits
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw -name "*.ts" -o -name "*.tsx" -o -name "*.js" -o -name "*.json" -o -name "*.yaml" -o -name "*.yml" | head -20
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -r "169.254.169.254" reposcan-raw/gladiaio/vercel-ai/ --include="*.ts" --include="*.js" --include="*.json" --include="*.yaml" --include="*.yml"
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:        deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:          subnets: { deny: ['169.254.169.254/32'] },
reposcan-raw/gladiaio/vercel-ai/packages/ai/src/util/download/download.test.ts:      download({ url: new URL('http://169.254.169.254/latest/meta-data/') }),
reposcan-raw/gladiaio/vercel-ai/packages/ai/src/util/download/download.test.ts:        location: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.ts:  // e.g. ::ffff:127.0.0.1 or 64:ff9b::169.254.169.254 are blocked.
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/fetch-with-validated-redirects.test.ts:      .mockResolvedValueOnce(redirectResponse('http://169.254.169.254/'));
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/fetch-with-validated-redirects.test.ts:      .mockResolvedValueOnce(redirectWithBody('http://169.254.169.254/'));
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/download-blob.test.ts:      downloadBlob('http://169.254.169.254/latest/meta-data/'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/download-blob.test.ts:          location: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://169.254.169.254/latest/meta-data/'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:    it('should block ::ffff:169.254.169.254', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://[::ffff:169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:    it('should block NAT64 64:ff9b::169.254.169.254 (metadata)', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://[64:ff9b::169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:    it('should block NAT64 local-use 64:ff9b:1::169.254.169.254', () => {
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/validate-download-url.test.ts:        validateDownloadUrl('http://[64:ff9b:1::169.254.169.254]/file'),
reposcan-raw/gladiaio/vercel-ai/packages/harness/src/v1/harness-v1-network-sandbox-session.test-d.ts:    deniedCIDRs: ['10.5.0.0/16', '169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/harness/src/v1/harness-v1-network-sandbox-session.test-d.ts:    deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/prodia/src/prodia-video-model.test.ts:            url: 'http://169.254.169.254/latest/meta-data/',
reposcan-raw/gladiaio/vercel-ai/packages/prodia/src/prodia-video-model.test.ts:        server.calls.some(call => call.requestUrl.includes('169.254.169.254')),
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw/gladiaio -maxdepth 2 -type d | grep -v vercel-ai | head -20
reposcan-raw/gladiaio
reposcan-raw/gladiaio/gladia-quiz-app
reposcan-raw/gladiaio/gladia-quiz-app/store
reposcan-raw/gladiaio/gladia-quiz-app/.cursor
reposcan-raw/gladiaio/gladia-quiz-app/components
reposcan-raw/gladiaio/gladia-quiz-app/lib
reposcan-raw/gladiaio/gladia-quiz-app/.git
reposcan-raw/gladiaio/gladia-quiz-app/app
reposcan-raw/gladiaio/gladia-quiz-app/public
reposcan-raw/gladiaio/gladia-quiz-app/hooks
reposcan-raw/gladiaio/gladia-quiz-app/scripts
reposcan-raw/gladiaio/compare-stt
reposcan-raw/gladiaio/compare-stt/.cursor
reposcan-raw/gladiaio/compare-stt/test-audio
reposcan-raw/gladiaio/compare-stt/prisma
reposcan-raw/gladiaio/compare-stt/.git
reposcan-raw/gladiaio/compare-stt/logos
reposcan-raw/gladiaio/compare-stt/public
reposcan-raw/gladiaio/compare-stt/src
reposcan-raw/gladiaio/num2words2
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -r "sk-\|ghp_\|gho_\|ghu_\|ghs_\|github_pat_\|gladia.*key\|api.*key\|secret\|token" reposcan-raw/gladiaio --include="*.ts" --include="*.js" --include="*.json" --include="*.yaml" --include="*.yml" --include="*.env*" | grep -v vercel-ai | grep -v test | grep -v ".test." | grep -v "test-api-key" | head -50
reposcan-raw/gladiaio/gladia-quiz-app/package-lock.json:        "@csstools/css-tokenizer": "^3.0.3",
reposcan-raw/gladiaio/gladia-quiz-app/package-lock.json:        "js-tokens": "^4.0.0",
reposcan-raw/gladiaio/gladia-quiz-app/package-lock.json:        "@csstools/css-tokenizer": "^3.0.4"
reposcan-raw/gladiaio/gladia-quiz-app/package-lock.json:        "@csstools/css-tokenizer": "^3.0.4"
reposcan-raw/gladiaio/gladia-quiz-app/package-lock.json:        "@csstools/css-tokenizer": "^3.0.4"
reposcan-raw/gladiaio/gladia-quiz-app/package-lock.json:    "node_modules/@csstools/css-tokenizer": {
reposcan-raw/gladiaio/gladia-quiz-app/package-lock.json:      "resolved": "https://registry.npmjs.org/@csstools/css-tokenizer/-/css-tokenizer-3.0.4.tgz",
reposcan-raw/gladiaio/gladia-quiz-app/package-lock.json:    "node_modules/js-tokens": {
reposcan-raw/gladiaio/gladia-quiz-app/package-lock.json:      "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz",
reposcan-raw/gladiaio/gladia-quiz-app/package-lock.json:        "js-tokens": "^3.0.0 || ^4.0.0"
reposcan-raw/gladiaio/gladia-quiz-app/package-lock.json:      "resolved": "https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz",
reposcan-raw/gladiaio/gladia-quiz-app/lib/gladia-client.ts:export const GLADIA_API_KEY_STORAGE = 'gladia_api_key';
reposcan-raw/gladiaio/compare-stt/package-lock.json:        "js-tokens": "^4.0.0",
reposcan-raw/gladiaio/compare-stt/package-lock.json:    "node_modules/js-tokens": {
reposcan-raw/gladiaio/compare-stt/package-lock.json:      "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz",
reposcan-raw/gladiaio/compare-stt/package-lock.json:        "js-tokens": "^3.0.0 || ^4.0.0"
reposcan-raw/gladiaio/compare-stt/package-lock.json:      "resolved": "https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz",
reposcan-raw/gladiaio/compare-stt/src/lib/arena-blob.ts:/** Validate the unsuffixed pathname before issuing a client upload token. */
reposcan-raw/gladiaio/compare-stt/src/lib/arena-blob.ts: * Extract the store id from a Vercel Blob read-write token (`vercel_blob_rw_<storeId>_…`).
reposcan-raw/gladiaio/compare-stt/src/lib/arena-blob.ts: * Throws a plain Error: a missing or malformed token is a server misconfiguration, not a bad request.
reposcan-raw/gladiaio/compare-stt/src/lib/arena-blob.ts:  token: string | undefined = process.env.BLOB_READ_WRITE_TOKEN
reposcan-raw/gladiaio/compare-stt/src/lib/arena-blob.ts:  if (!token) {
reposcan-raw/gladiaio/compare-stt/src/lib/arena-blob.ts:  const storeId = token.split("_")[3];
reposcan-raw/gladiaio/compare-stt/src/lib/arena-blob.ts:  options?: { storeId?: string; token?: string }
reposcan-raw/gladiaio/compare-stt/src/lib/arena-blob.ts:  const storeId = options?.storeId ?? getBlobStoreId(options?.token);
reposcan-raw/gladiaio/compare-stt/src/lib/providers/gladia.ts:    headers: { "x-gladia-key": apiKey },
reposcan-raw/gladiaio/compare-stt/src/lib/providers/gladia.ts:      "x-gladia-key": apiKey,
reposcan-raw/gladiaio/compare-stt/src/lib/providers/gladia.ts:      headers: { "x-gladia-key": apiKey },
reposcan-raw/gladiaio/compare-stt/src/lib/rate-limit.ts: * defense-in-depth layer on top of the DB-backed single-use token and
reposcan-raw/gladiaio/compare-stt/src/lib/match-token.ts: * a deploy boundary. Legacy tokens get issuedAt = 0 so the minimum-delay
reposcan-raw/gladiaio/compare-stt/src/lib/match-token.ts:export function verifyMatchToken(token: string): MatchTokenPayload | null {
reposcan-raw/gladiaio/compare-stt/src/lib/match-token.ts:  const parts = token.split(".");
reposcan-raw/gladiaio/compare-stt/src/lib/match-token.ts:export function hashMatchToken(token: string): string {
reposcan-raw/gladiaio/compare-stt/src/lib/match-token.ts:  return crypto.createHash("sha256").update(token).digest("hex");
reposcan-raw/gladiaio/compare-stt/src/app/api/vote/route.ts:import { verifyMatchToken, hashMatchToken } from "@/lib/match-token";
reposcan-raw/gladiaio/compare-stt/src/app/api/vote/route.ts:        { error: "Invalid or tampered match token" },
reposcan-raw/gladiaio/compare-stt/src/app/api/vote/route.ts:    // issuedAt === 0 means a legacy 4-part token issued before this deploy;
reposcan-raw/gladiaio/compare-stt/src/app/api/vote/route.ts:    const tokenHash = hashMatchToken(matchToken);
reposcan-raw/gladiaio/compare-stt/src/app/api/vote/route.ts:    // Use an interactive transaction for atomicity: the token claim
reposcan-raw/gladiaio/compare-stt/src/app/api/vote/route.ts:    // in a single serializable step. This prevents both token replay
reposcan-raw/gladiaio/compare-stt/src/app/api/vote/route.ts:        where: { tokenHash, consumedAt: null },
reposcan-raw/gladiaio/compare-stt/src/app/api/vote/route.ts:      // Legacy tokens (pre-deploy) won't be in the table at all.
reposcan-raw/gladiaio/compare-stt/src/app/api/vote/route.ts:      // If the token exists but was already consumed, reject.
reposcan-raw/gladiaio/compare-stt/src/app/api/vote/route.ts:        const exists = await tx.matchToken.findUnique({ where: { tokenHash } });
reposcan-raw/gladiaio/compare-stt/src/app/api/vote/route.ts:          return { error: "This match token has already been used to vote.", status: 409 } as const;
reposcan-raw/gladiaio/compare-stt/src/app/api/vote/route.ts:        // Not in the table → legacy token; proceed with just the session cap.
reposcan-raw/gladiaio/compare-stt/src/app/api/transcribe/route.ts:import { signMatchToken, hashMatchToken } from "@/lib/match-token";
reposcan-raw/gladiaio/compare-stt/src/app/api/transcribe/route.ts:    // Fetch by pathname so the SDK builds our store URL (token never leaves to a client host)
reposcan-raw/gladiaio/compare-stt/src/app/api/transcribe/route.ts:        tokenHash: hashMatchToken(matchToken),
reposcan-raw/gladiaio/compare-stt/src/scripts/purge-fraudulent-votes.ts: *   1. Duplicate provider pairs within the same session (token replay)
