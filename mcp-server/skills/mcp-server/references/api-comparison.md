# LLM Provider API Comparison

Comprehensive comparison matrix for major LLM providers to inform integration decisions.

## Quick Comparison Matrix

| Feature | OpenAI | Anthropic Claude | Google Gemini | Ollama (Local) |
|---------|--------|------------------|---------------|----------------|
| **Max Context** | 128K (GPT-4 Turbo) | 200K (Sonnet/Opus) | 2M (1.5 Pro) | Model-dependent |
| **Streaming** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Function Calling** | ✅ Yes | ✅ Yes (Tools) | ✅ Yes | ⚠️ Limited |
| **Vision** | ✅ Yes (GPT-4o) | ✅ Yes (3.5 Sonnet) | ✅ Yes | ⚠️ Limited |
| **Multimodal** | Images only | Images only | Images, video, audio | Varies |
| **MCP Support** | ❌ No | ✅ Yes | ❌ No | ❌ No |
| **Pricing Model** | Per-token | Per-token | Per-token | Free (compute costs) |
| **Data Retention** | Opt-out available | Zero retention option | Opt-out available | N/A (local) |
| **Rate Limits** | Tier-based | Tier-based | Quota-based | Hardware-limited |

## OpenAI

### Models and Capabilities

**GPT-4 Turbo (`gpt-4-turbo`, `gpt-4-turbo-2024-04-09`)**
- Context window: 128,000 tokens
- Knowledge cutoff: April 2023
- Vision capable: Yes
- Function calling: Yes
- Best for: Complex reasoning, analysis, code generation
- Cost: $$$ (most expensive)

**GPT-4o (`gpt-4o`, `gpt-4o-2024-08-06`)**
- Context window: 128,000 tokens
- Knowledge cutoff: October 2023
- Vision capable: Yes (optimized)
- Function calling: Yes
- Multimodal: Text, images
- Best for: Real-time applications, multimodal tasks
- Cost: $$ (mid-tier)

**GPT-3.5 Turbo (`gpt-3.5-turbo`, `gpt-3.5-turbo-0125`)**
- Context window: 16,385 tokens
- Knowledge cutoff: September 2021
- Vision capable: No
- Function calling: Yes
- Best for: Simple tasks, high-volume applications, cost-sensitive
- Cost: $ (most affordable)

### Pricing (as of 2025)

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|-------|----------------------|------------------------|
| GPT-4 Turbo | $10.00 | $30.00 |
| GPT-4o | $5.00 | $15.00 |
| GPT-3.5 Turbo | $0.50 | $1.50 |

**Additional costs:**
- DALL-E 3: $0.040-$0.120 per image
- Whisper: $0.006 per minute
- TTS: $15.00 per 1M characters

### Rate Limits

**Tier 1 (Default):**
- 500 RPM (requests per minute)
- 200,000 TPM (tokens per minute)
- $100 usage limit

**Tier 5 (High volume):**
- 10,000 RPM
- 30,000,000 TPM
- Requires $1,000+ monthly spend

### Features

**Function Calling:**
- Native support with JSON schema
- Parallel function calling supported
- Works with streaming

**Vision:**
- Supported in GPT-4o and GPT-4 Turbo
- Base64 or URL image inputs
- Detail levels: low, high, auto

**Embeddings:**
- text-embedding-3-small: $0.02 per 1M tokens
- text-embedding-3-large: $0.13 per 1M tokens
- Dimensions: 512, 1536, 3072

**Response Format:**
- JSON mode (guaranteed JSON output)
- Structured outputs (beta)

### Best Use Cases

1. **High-volume cost-sensitive applications** (GPT-3.5 Turbo)
2. **Image generation and manipulation** (DALL-E integration)
3. **Voice/audio processing** (Whisper, TTS)
4. **Existing OpenAI ecosystem integrations**
5. **Streaming function calling** (unique to OpenAI)

## Anthropic Claude

### Models and Capabilities

**Claude 3.5 Sonnet (`claude-3-5-sonnet-20241022`)**
- Context window: 200,000 tokens
- Knowledge cutoff: April 2024
- Vision capable: Yes
- Tool use: Yes
- Best for: Balanced performance, coding, analysis
- Cost: $$ (mid-tier)

**Claude 3 Opus (`claude-3-opus-20240229`)**
- Context window: 200,000 tokens
- Knowledge cutoff: August 2023
- Vision capable: Yes
- Tool use: Yes
- Best for: Highest quality, complex reasoning
- Cost: $$$ (premium)

**Claude 3 Haiku (`claude-3-haiku-20240307`)**
- Context window: 200,000 tokens
- Knowledge cutoff: August 2023
- Vision capable: Yes
- Tool use: Yes
- Best for: Speed, simple tasks, cost-effective
- Cost: $ (affordable)

### Pricing (as of 2025)

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Cached Input (per 1M) |
|-------|----------------------|------------------------|----------------------|
| Claude 3.5 Sonnet | $3.00 | $15.00 | $0.30 |
| Claude 3 Opus | $15.00 | $75.00 | $1.50 |
| Claude 3 Haiku | $0.25 | $1.25 | $0.03 |

**Prompt Caching:**
- Cache hits: 90% discount on cached tokens
- Cache lifetime: 5 minutes (refreshed on use)
- Minimum cacheable: 1024 tokens

### Rate Limits

**Tier 1 (Default):**
- 50 RPM
- 40,000 TPM (Haiku), 10,000 TPM (Sonnet/Opus)
- $100 monthly limit

**Tier 4 (High volume):**
- 4,000 RPM
- 400,000 TPM
- $40,000 monthly limit

### Features

**Tool Use (Function Calling):**
- Native support with JSON schema
- Multiple tools per request
- Chain-of-thought reasoning before tool calls

**Vision:**
- All Claude 3+ models support images
- Base64 or URL inputs
- Multiple images per request
- PDF support (converted to images)

**Prompt Caching:**
- Automatic caching of long system prompts
- Cache key based on prefix matching
- Significant cost savings for repeated contexts

**MCP (Model Context Protocol):**
- Native support for MCP servers
- Standardized tool discovery
- Claude Desktop integration

**Extended Thinking (beta):**
- Long-form internal reasoning
- Better complex problem solving
- Higher cost but improved accuracy

### Best Use Cases

1. **Tool-heavy integrations** (native MCP support)
2. **Long documents and conversations** (200K context, caching)
3. **Security-sensitive applications** (reduced hallucinations, zero retention)
4. **Analysis and reasoning tasks** (strong analytical capabilities)
5. **Cost-effective with caching** (90% discount on cached tokens)

## Google Gemini

### Models and Capabilities

**Gemini 1.5 Pro (`gemini-1.5-pro`)**
- Context window: 2,000,000 tokens
- Knowledge cutoff: November 2023
- Multimodal: Text, images, video, audio
- Function calling: Yes
- Best for: Massive context, multimodal tasks
- Cost: $$ (mid-tier for context size)

**Gemini 1.5 Flash (`gemini-1.5-flash`)**
- Context window: 1,000,000 tokens
- Knowledge cutoff: November 2023
- Multimodal: Text, images, video, audio
- Function calling: Yes
- Best for: Fast, cost-effective, large context
- Cost: $ (affordable)

**Gemini 1.0 Pro (`gemini-1.0-pro`)**
- Context window: 32,768 tokens
- Knowledge cutoff: April 2023
- Multimodal: Text, images
- Function calling: Yes
- Best for: Basic tasks, legacy support
- Cost: $ (affordable)

### Pricing (as of 2025)

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|-------|----------------------|------------------------|
| Gemini 1.5 Pro | $1.25 (≤128K), $2.50 (>128K) | $5.00 (≤128K), $10.00 (>128K) |
| Gemini 1.5 Flash | $0.075 (≤128K), $0.15 (>128K) | $0.30 (≤128K), $0.60 (>128K) |
| Gemini 1.0 Pro | $0.50 | $1.50 |

**Context Caching:**
- Free for inputs >32K tokens cached
- Reduces cost and latency for repeated contexts

### Rate Limits

**Free Tier:**
- 15 RPM
- 1,000,000 TPM
- 1,500 requests per day

**Paid Tier:**
- 360 RPM
- 4,000,000 TPM (Pro), 10,000,000 TPM (Flash)
- No daily limit

### Features

**Multimodal:**
- Native video understanding (no frame extraction needed)
- Audio processing in same context
- Up to 3,600 seconds of video or audio
- Multiple images in single request

**Function Calling:**
- Native support with JSON schema
- Parallel function calls
- Auto-execution mode

**Context Caching:**
- Automatic for >32K token inputs
- Persists across requests
- Reduces latency and cost

**Code Execution:**
- Python code execution in sandbox
- Mathematical computations
- Data analysis

### Best Use Cases

1. **Massive context requirements** (2M tokens for 1.5 Pro)
2. **Video and audio analysis** (native multimodal)
3. **Google Cloud integrations** (Vertex AI)
4. **Cost-effective long-context tasks** (caching, Flash model)
5. **Mathematical and code execution tasks**

## Ollama (Local Models)

### Overview

Ollama enables running LLMs locally without cloud APIs. Models vary significantly in capability based on parameter count and training data.

### Popular Models

**Llama 3.3 (70B)**
- Parameters: 70 billion
- Context window: 128K tokens
- Vision: No (text-only)
- Best for: High-quality local inference
- Hardware: 40GB+ VRAM or CPU fallback

**Llama 3.2 (3B)**
- Parameters: 3 billion
- Context window: 128K tokens
- Vision: Yes (multimodal variant)
- Best for: Edge devices, low-resource environments
- Hardware: 4GB+ VRAM

**Mistral 7B**
- Parameters: 7 billion
- Context window: 32K tokens
- Vision: No
- Best for: Balanced performance/size
- Hardware: 8GB+ VRAM

**CodeLlama (34B)**
- Parameters: 34 billion
- Context window: 100K tokens
- Specialized: Code generation
- Best for: Programming tasks
- Hardware: 20GB+ VRAM

**Llava (7B, 13B, 34B)**
- Parameters: 7B, 13B, or 34B
- Multimodal: Vision + text
- Best for: Local image understanding
- Hardware: 8GB+ VRAM (7B)

### Pricing

- **Model costs**: Free (open-source)
- **Compute costs**: Hardware investment + electricity
- **No per-token charges**
- **No rate limits** (hardware-constrained only)

### Hardware Requirements

**GPU Inference (Recommended):**
- Small models (3B-7B): 6-8GB VRAM
- Medium models (13B-34B): 16-24GB VRAM
- Large models (70B+): 40GB+ VRAM or multi-GPU

**CPU Inference (Slower):**
- Works with any model
- RAM requirements: 1.5-2x model size
- Significantly slower than GPU

**Quantization:**
- Q4: 4-bit quantization (~4GB for 7B model)
- Q5: 5-bit quantization (better quality, larger)
- Q8: 8-bit quantization (best quality, largest)
- FP16: Full precision (2x model size)

### Rate Limits

- **No external rate limits**
- Limited by hardware capabilities
- Concurrent requests: Depends on VRAM
- Throughput: Model size, quantization, hardware

### Features

**Function Calling:**
- Limited native support
- Requires prompting techniques
- Tools-capable models: Llama 3.3, Mistral

**Vision:**
- Llava models (multimodal)
- Llama 3.2 Vision
- BakLlava (Mistral-based vision)

**Embeddings:**
- nomic-embed-text (768 dimensions)
- mxbai-embed-large (1024 dimensions)
- Free, unlimited generation

**Customization:**
- Fine-tuning on custom data
- Model quantization
- Custom system prompts
- No content restrictions

### Best Use Cases

1. **Privacy-critical applications** (healthcare, legal, defense)
2. **Offline/airgapped environments**
3. **Cost avoidance** (high-volume usage)
4. **Custom model requirements** (fine-tuning)
5. **Content without cloud restrictions**

## Decision Matrix

### By Primary Concern

**Cost Optimization:**
1. Ollama (free inference, hardware costs)
2. Google Gemini Flash (best $/token)
3. GPT-3.5 Turbo (affordable cloud)
4. Claude Haiku (with caching)

**Context Window:**
1. Google Gemini 1.5 Pro (2M tokens)
2. Gemini 1.5 Flash (1M tokens)
3. Claude 3.x (200K tokens)
4. GPT-4 Turbo (128K tokens)

**Quality/Reasoning:**
1. Claude 3 Opus (highest quality)
2. GPT-4 Turbo (strong reasoning)
3. Claude 3.5 Sonnet (balanced)
4. Gemini 1.5 Pro (multimodal edge)

**Speed/Latency:**
1. Claude 3 Haiku (fastest)
2. Google Gemini Flash (fast)
3. GPT-3.5 Turbo (fast)
4. Ollama small models (local, no network)

**Privacy/Security:**
1. Ollama (fully local)
2. Claude (zero retention option)
3. OpenAI/Gemini (opt-out retention)

**Multimodal:**
1. Google Gemini (video + audio)
2. GPT-4o (images, optimized)
3. Claude 3.5 (images)
4. Ollama Llava (local vision)

**Tool Integration:**
1. Claude (native MCP)
2. OpenAI (streaming function calls)
3. Gemini (auto-execution)
4. Ollama (limited, prompt-based)

### By Use Case

**Chatbot:**
- Real-time: GPT-4o, Claude 3.5 Sonnet
- High-volume: GPT-3.5 Turbo, Gemini Flash, Claude Haiku
- Privacy: Ollama Llama 3.3

**Document Analysis:**
- Long documents: Gemini 1.5 Pro (2M context)
- PDFs with images: Claude 3.5 Sonnet (native PDF)
- Cost-effective: Gemini Flash, Claude with caching

**Code Generation:**
- Quality: GPT-4 Turbo, Claude 3.5 Sonnet
- Speed: Claude 3 Haiku, GPT-4o
- Local: Ollama CodeLlama

**Data Extraction:**
- Structured output: OpenAI (JSON mode)
- Function calling: All (Claude/OpenAI best)
- Multimodal: Gemini (video/audio)

**Video/Audio Analysis:**
- Only viable option: Google Gemini 1.5

## Integration Considerations

### SDK Quality

**OpenAI:**
- Mature, well-documented Python and Node.js SDKs
- Extensive community libraries
- Streaming, async, retries built-in

**Anthropic:**
- Official Python and TypeScript SDKs
- MCP SDK for tool integrations
- Good documentation, growing ecosystem

**Google:**
- Vertex AI SDK (comprehensive)
- Google AI Studio (simplified)
- Tight Google Cloud integration

**Ollama:**
- REST API (simple HTTP)
- Python, JavaScript libraries available
- LangChain, LlamaIndex integrations

### Error Handling

**OpenAI:**
- Rate limit headers (remaining, reset)
- Detailed error codes
- Request IDs for debugging

**Anthropic:**
- Rate limit headers
- Error types: validation, rate_limit, overloaded
- Request IDs, support for debugging

**Google:**
- Quota errors (separate from rate limits)
- Retry-After headers
- Regional differences

**Ollama:**
- HTTP status codes
- Local errors (CUDA, memory)
- Model loading failures

### Data Privacy

**OpenAI:**
- 30-day retention default
- Zero retention for API (opt-in)
- Enterprise agreement required for guarantees

**Anthropic:**
- No training on API data
- Zero retention option available
- Clear DPA terms

**Google:**
- No training on Vertex AI data
- Google AI Studio: May use for improvements
- Regional data residency options

**Ollama:**
- Fully local, no external data
- Complete control over data
- Ideal for sensitive/regulated data

## Migration Considerations

**From OpenAI to Claude:**
- Function calling similar (tools vs functions)
- Prompt engineering may need adjustment
- Vision API differences (detail levels vs none)
- MCP unlocks new capabilities

**From OpenAI to Gemini:**
- Function calling compatible
- Massive context window advantage
- Multimodal expansion (video/audio)
- Different rate limit structure

**From Cloud to Ollama:**
- Quality/capability trade-offs
- Infrastructure investment required
- No streaming function calling (limited)
- Complete control, zero API costs

**Multi-Provider Strategy:**
- Route by task type (simple→cheap, complex→expensive)
- Fallback on failures or rate limits
- A/B test quality vs cost
- Provider-specific features (MCP, vision, etc.)

## Monitoring and Cost Tracking

**Track per request:**
- Input tokens
- Output tokens
- Model used
- Latency
- Cost
- Success/failure
- Provider

**Aggregate metrics:**
- Daily/monthly spend per provider
- Average tokens per request type
- Cost per user/tenant
- Cache hit rates (Claude, Gemini)
- Error rates by provider

**Alerting thresholds:**
- Daily spend limit exceeded
- Error rate spike (>5%)
- Latency degradation (>2x baseline)
- Rate limit approaching (>80%)

## References

- OpenAI API Documentation: https://platform.openai.com/docs
- Anthropic API Documentation: https://docs.anthropic.com
- Google Gemini API Documentation: https://ai.google.dev/docs
- Ollama Documentation: https://ollama.ai/docs

**Last Updated:** January 2025
