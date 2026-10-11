
===== REPOSCAN 2026-10-11 15:48:37 UTC =====
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && find reposcan-raw -name "*.ts" -o -name "*.json" -o -name "*.yaml" | head -20
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
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -r "169.254.169.254" reposcan-raw/gladiaio/vercel-ai --include="*.ts" --include="*.json" -n
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:166:        deniedCIDRs: ['169.254.169.254/32'],
reposcan-raw/gladiaio/vercel-ai/packages/sandbox-vercel/src/vercel-sandbox.test.ts:171:          subnets: { deny: ['169.254.169.254/32'] },
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
[0m
[0m$ [0mcd /home/runner/work/gladia-hunt-yuu/gladia-hunt-yuu && grep -r "sk-" reposcan-raw/gladiaio --include="*.ts" --include="*.json" --include="*.yaml" -n
...output truncated...

Full output saved to: /home/runner/.local/share/opencode/tool-output/tool_12ba50c900019xFwgdANu6DGSM

reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/togetherai-image-model.test.ts:432:      'Together AI does not support mask-based image editing. ' +
reposcan-raw/gladiaio/vercel-ai/packages/togetherai/src/togetherai-image-model.ts:72:        'Together AI does not support mask-based image editing. ' +
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-image-model.ts:250:        'Gemini image models do not support mask-based image editing.',
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-image-model.test.ts:486:      const maskData = 'base64-mask-image';
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-image-model.test.ts:528:                    "bytesBase64Encoded": "base64-mask-image",
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-image-model.test.ts:591:          data: 'base64-mask-image',
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-image-model.test.ts:630:                    "bytesBase64Encoded": "base64-mask-image",
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-image-model.test.ts:660:          data: 'base64-mask-image',
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-image-model.test.ts:1230:            data: 'base64-mask-image',
reposcan-raw/gladiaio/vercel-ai/packages/google-vertex/src/google-vertex-image-model.test.ts:1240:        'Gemini image models do not support mask-based image editing.',
reposcan-raw/gladiaio/vercel-ai/packages/harness-codex/src/codex-auth.test.ts:9:          apiKey: 'sk-x',
reposcan-raw/gladiaio/vercel-ai/packages/harness-codex/src/codex-auth.test.ts:17:      CODEX_API_KEY: 'sk-x',
reposcan-raw/gladiaio/vercel-ai/packages/harness-codex/src/codex-auth.test.ts:25:      { openai: { apiKey: 'sk-direct', organization: 'org_1' } },
reposcan-raw/gladiaio/vercel-ai/packages/harness-codex/src/codex-auth.test.ts:26:      { OPENAI_API_KEY: 'sk-env' },
reposcan-raw/gladiaio/vercel-ai/packages/harness-codex/src/codex-auth.test.ts:28:    expect(env.CODEX_API_KEY).toBe('sk-direct');
reposcan-raw/gladiaio/vercel-ai/packages/harness-codex/src/codex-auth.test.ts:51:    const env = resolveCodexEnv(undefined, { OPENAI_API_KEY: 'sk-auto' });
reposcan-raw/gladiaio/vercel-ai/packages/harness-codex/src/codex-auth.test.ts:52:    expect(env).toEqual({ CODEX_API_KEY: 'sk-auto' });
reposcan-raw/gladiaio/vercel-ai/packages/harness-codex/src/codex-auth.test.ts:57:      OPENAI_API_KEY: 'sk-auto',
reposcan-raw/gladiaio/vercel-ai/packages/harness-codex/src/codex-auth.test.ts:61:      CODEX_API_KEY: 'sk-auto',
reposcan-raw/gladiaio/vercel-ai/packages/harness-codex/src/codex-harness.ts:908:       * attach / replay: the still-running (or disk-replayed) turn streams into
reposcan-raw/gladiaio/vercel-ai/packages/harness-claude-code/src/claude-code-harness.ts:1372:       * attach / replay: the still-running (or disk-replayed) turn streams into
reposcan-raw/gladiaio/vercel-ai/packages/harness-claude-code/src/claude-code-auth.test.ts:9:      { anthropic: { apiKey: 'sk-explicit' } },
reposcan-raw/gladiaio/vercel-ai/packages/harness-claude-code/src/claude-code-auth.test.ts:10:      { ANTHROPIC_API_KEY: 'sk-process', AI_GATEWAY_API_KEY: 'gw-key' },
reposcan-raw/gladiaio/vercel-ai/packages/harness-claude-code/src/claude-code-auth.test.ts:13:    expect(env).toEqual({ ANTHROPIC_API_KEY: 'sk-explicit' });
reposcan-raw/gladiaio/vercel-ai/packages/harness-claude-code/src/claude-code-auth.test.ts:20:        ANTHROPIC_API_KEY: 'sk-process',
reposcan-raw/gladiaio/vercel-ai/packages/harness-claude-code/src/claude-code-auth.test.ts:26:      ANTHROPIC_API_KEY: 'sk-process',
reposcan-raw/gladiaio/vercel-ai/packages/harness-claude-code/src/claude-code-auth.test.ts:55:      { ANTHROPIC_API_KEY: 'sk-auto' },
reposcan-raw/gladiaio/vercel-ai/packages/harness-claude-code/src/claude-code-auth.test.ts:58:    expect(env).toEqual({ ANTHROPIC_API_KEY: 'sk-auto' });
reposcan-raw/gladiaio/vercel-ai/packages/harness-claude-code/src/claude-code-auth.test.ts:65:        ANTHROPIC_API_KEY: 'sk-auto',
reposcan-raw/gladiaio/vercel-ai/packages/harness-claude-code/src/claude-code-auth.test.ts:71:      ANTHROPIC_API_KEY: 'sk-auto',
reposcan-raw/gladiaio/vercel-ai/packages/harness-claude-code/src/claude-code-auth.test.ts:102:    const helper = vi.fn(() => 'sk-from-helper');
reposcan-raw/gladiaio/vercel-ai/packages/harness-claude-code/src/claude-code-auth.test.ts:105:      { ANTHROPIC_API_KEY: 'sk-static' },
reposcan-raw/gladiaio/vercel-ai/packages/harness-claude-code/src/claude-code-auth.test.ts:108:    expect(env.ANTHROPIC_API_KEY).toBe('sk-static');
reposcan-raw/gladiaio/vercel-ai/packages/xai/src/responses/__fixtures__/xai-x-search-tool.1.json:20:          "text": "### What People Are Saying About AI on X (as of Late October 2025)\n\nBased on recent posts on X (formerly Twitter), discussions about AI are buzzing with a mix of excitement, technical deep dives, and cautious optimism. The conversation heavily revolves around **Artificial General Intelligence (AGI)** as the holy grail of AI development, with frequent references to a new paper from AI luminaries like Yoshua Bengio, Eric Schmidt, Gary Marcus, and Max Tegmark. People are debating definitions, progress, limitations, and real-world applications. Here's a breakdown of the main themes from the top relevant posts (focusing on the last month):\n\n#### 1. **Defining AGI and Its Distance from Current AI**\n   - A huge focus is on clarifying what AGI really means. Multiple users cite the aforementioned paper, which defines AGI as an AI system that \"matches or exceeds the cognitive versatility and proficiency of a well-educated adult\" across 10 core cognitive areas (e.g., reasoning, memory, math, language, perception).\n     - Example: @jiqizhixin shared the paper, noting that models like GPT-4 and GPT-5 score poorly (e.g., 0% on long-term memory), emphasizing AGI isn't here yet.\n     - @alex_prompter broke it down simply: GPT-4 is at 27% toward AGI, GPT-5 at 58%, but gaps in continuous learning persist. They called it a \"clear benchmark\" without hype.\n     - @AskPerplexity and @flowersslop echoed this, describing AGI as broadly adaptable like humans, not just narrow tools like today's chatbots.\n   - ASI (Artificial Superintelligence) gets mentioned as the next step beyond AGI—AI surpassing humans in *all* domains, including creativity and strategy. @SciTechera tied it to the \"Singularity,\" where AI self-improves uncontrollably.\n   - Skepticism: @Newaxeman called AI an \"advanced search engine\" aggregating conventional wisdom, questioning deeper intelligence claims.\n\n#### 2. **Progress and Timelines Toward AGI**\n   - Optimism is high but grounded. @bindureddy (CEO of Abacus.AI) boldly predicted AGI (AI replacing humans in digital tasks) is \"just a couple of years away,\" citing missing pieces like context, tools, and self-awareness that labs are tackling.\n   - @slow_developer referenced OpenAI and DeepMind's 5-level AGI framework: Current models are past Level 2 (emerging intelligence) and into early Level 3 (competent in complex tasks with supervision), but not fully autonomous yet.\n   - @timmur_ stressed AGI requires efficient learning across open-ended tasks with minimal data—something no model achieves today, but \"we will solve it eventually.\"\n   - Broader view: @FrnkNlsn recommended the book *Artificial Intelligence: A Modern Approach* by Russell and Norvig for a comprehensive overview, highlighting topics like knowledge representation and multi-agent systems.\n\n#### 3. **Types of AI and Distinctions**\n   - Users are educating on AI's varieties to cut through confusion:\n     - @y00ngipurrs differentiated analytical AI (e.g., for medicine, fraud detection) from generative AI (e.g., ChatGPT for text/art).\n     - @techyoutbe contrasted AI agents (task-specific automators) with \"agentic AI\" (autonomous systems for long-term planning and multi-domain reasoning).\n     - @SukhSandhu listed what AI *is* (data processor, pattern recognizer, task automator) vs. what it's *not* (conscious, emotional, intuitively moral). They warned of biases in training data.\n   - @AITECHio hyped proactive \"AI agents\" that set goals and execute workflows autonomously, predicting one for every task from finance to on-chain automation.\n\n#### 4. **Applications, Projects, and Broader Impacts**\n   - AI's practical side shines in Web3 and business contexts. @O_H_JAY highlighted crypto projects advancing AGI/ASI, like @SentientAGI (decentralized AGI networks), @AGI_XT (AI automation on Solana), and @StoryProtocol (on-chain IP for AI models). They urged getting in early during market dips.\n   - @Voa_De_Voa discussed combining AI with compute and robotics for \"autonomous intelligence,\" but flagged centralized control as a risk.\n   - @DeviprasadSD positioned AGI as a future horizon for reasoning across any task, still in research.\n   - @zolayolanetwork and @davilagrau amplified the AGI definition paper, linking it to blockchain and cognitive tools.\n\n#### Overall Sentiment\n- **Positive/Visionary**: Excitement about AI augmenting human capabilities (e.g., @hailstorm_9 called AGI \"augmentation, not automation\"). Many see it transforming industries like healthcare, finance, and creative work.\n- **Cautious/Realistic**: Emphasis on limitations—current AI is \"narrow\" and lacks true understanding or adaptability. No one's claiming AGI is imminent without caveats.\n- **Volume and Engagement**: These posts garnered thousands of likes/views, with high engagement on definitions and project lists. Discussions are technical but accessible, often with images, threads, or links to papers/arXiv.\n\nThis is a snapshot from ~20 recent, highly relevant posts. AI chatter on X is evolving fast—trends like AGI benchmarks and agentic systems are dominating. If you want deeper dives into specific posts, users, or subtopics (e.g., AI ethics or tools), let me know!",
reposcan-raw/gladiaio/vercel-ai/packages/google/src/google-image-model.test.ts:423:            data: 'base64-mask-image',
reposcan-raw/gladiaio/vercel-ai/packages/google/src/google-image-model.test.ts:900:            data: 'base64-mask-image',
reposcan-raw/gladiaio/vercel-ai/packages/google/src/google-image-model.test.ts:910:        'Gemini image models do not support mask-based image editing.',
reposcan-raw/gladiaio/vercel-ai/packages/google/src/google-image-model.ts:230:    // Gemini does not support mask-based inpainting
reposcan-raw/gladiaio/vercel-ai/packages/google/src/google-image-model.ts:233:        'Gemini image models do not support mask-based image editing.',
reposcan-raw/gladiaio/vercel-ai/packages/bytedance/src/bytedance-video-model.test.ts:49:            id: 'test-task-id-123',
reposcan-raw/gladiaio/vercel-ai/packages/bytedance/src/bytedance-video-model.test.ts:53:    'https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks/test-task-id-123':
reposcan-raw/gladiaio/vercel-ai/packages/bytedance/src/bytedance-video-model.test.ts:58:            id: 'test-task-id-123',
reposcan-raw/gladiaio/vercel-ai/packages/bytedance/src/bytedance-video-model.test.ts:359:          taskId: 'test-task-id-123',
reposcan-raw/gladiaio/vercel-ai/packages/bytedance/src/bytedance-video-model.test.ts:883:                id: 'failed-task-id',
reposcan-raw/gladiaio/vercel-ai/packages/bytedance/src/bytedance-video-model.test.ts:892:          if (urlString.includes('/tasks/failed-task-id')) {
reposcan-raw/gladiaio/vercel-ai/packages/bytedance/src/bytedance-video-model.test.ts:895:                id: 'failed-task-id',
reposcan-raw/gladiaio/vercel-ai/packages/bytedance/src/bytedance-video-model.test.ts:937:                id: 'no-video-task-id',
reposcan-raw/gladiaio/vercel-ai/packages/bytedance/src/bytedance-video-model.test.ts:946:          if (urlString.includes('/tasks/no-video-task-id')) {
reposcan-raw/gladiaio/vercel-ai/packages/bytedance/src/bytedance-video-model.test.ts:949:                id: 'no-video-task-id',
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/serialize-model-options.test.ts:15:        headers: () => ({ 'x-api-key': 'sk-test' }),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/serialize-model-options.test.ts:29:        headers: { 'x-api-key': 'sk-test' },
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/serialize-model-options.test.ts:41:        headers: () => ({ authorization: 'Bearer sk-test' }),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/serialize-model-options.test.ts:50:        headers: { authorization: 'Bearer sk-test' },
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/serialize-model-options.test.ts:103:          headers: async () => ({ 'x-api-key': 'sk-test' }),
reposcan-raw/gladiaio/vercel-ai/packages/provider-utils/src/serialize-model-options.test.ts:115:          headers: () => Promise.resolve({ 'x-api-key': 'sk-test' }),
reposcan-raw/gladiaio/vercel-ai/packages/klingai/src/klingai-video-model.test.ts:12:    task_id: 'task-abc-123',
reposcan-raw/gladiaio/vercel-ai/packages/klingai/src/klingai-video-model.test.ts:25:    task_id: 'task-abc-123',
reposcan-raw/gladiaio/vercel-ai/packages/klingai/src/klingai-video-model.test.ts:142:    [`${TEST_BASE_URL}/v1/videos/motion-control/task-abc-123`]: {
reposcan-raw/gladiaio/vercel-ai/packages/klingai/src/klingai-video-model.test.ts:155:    [`${TEST_BASE_URL}/v1/videos/text2video/task-abc-123`]: {
reposcan-raw/gladiaio/vercel-ai/packages/klingai/src/klingai-video-model.test.ts:168:    [`${TEST_BASE_URL}/v1/videos/image2video/task-abc-123`]: {
reposcan-raw/gladiaio/vercel-ai/packages/klingai/src/klingai-video-model.test.ts:526:        `${TEST_BASE_URL}/v1/videos/text2video/task-abc-123`,
reposcan-raw/gladiaio/vercel-ai/packages/klingai/src/klingai-video-model.test.ts:871:        `${TEST_BASE_URL}/v1/videos/image2video/task-abc-123`,
reposcan-raw/gladiaio/vercel-ai/packages/klingai/src/klingai-video-model.test.ts:1196:          taskId: 'task-abc-123',
reposcan-raw/gladiaio/vercel-ai/packages/klingai/src/klingai-video-model.test.ts:1241:        `${TEST_BASE_URL}/v1/videos/motion-control/task-abc-123`
reposcan-raw/gladiaio/vercel-ai/packages/klingai/src/klingai-video-model.test.ts:1249:            task_id: 'task-abc-123',
reposcan-raw/gladiaio/vercel-ai/packages/klingai/src/klingai-video-model.test.ts:1267:        `${TEST_BASE_URL}/v1/videos/motion-control/task-abc-123`
reposcan-raw/gladiaio/vercel-ai/packages/klingai/src/klingai-video-model.test.ts:1300:        `${TEST_BASE_URL}/v1/videos/motion-control/task-abc-123`
reposcan-raw/gladiaio/vercel-ai/packages/klingai/src/klingai-video-model.test.ts:1308:            task_id: 'task-abc-123',
