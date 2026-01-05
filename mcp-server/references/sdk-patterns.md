# SDK Patterns and Code Examples

Practical patterns and code examples for integrating with LLM APIs using official SDKs.

## Table of Contents

1. [Error Handling](#error-handling)
2. [Streaming Implementation](#streaming-implementation)
3. [Rate Limiting and Retries](#rate-limiting-and-retries)
4. [Context Management](#context-management)
5. [Cost Tracking](#cost-tracking)
6. [Caching Strategies](#caching-strategies)
7. [Multi-Provider Abstraction](#multi-provider-abstraction)

## Error Handling

### OpenAI Python SDK

```python
from openai import OpenAI, OpenAIError, RateLimitError, APIError
import time
import logging

client = OpenAI(api_key="your-api-key")
logger = logging.getLogger(__name__)

def chat_with_retry(messages: list, max_retries: int = 3) -> str:
    """Call OpenAI with exponential backoff retry logic."""
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=messages,
                temperature=0.7
            )
            return response.choices[0].message.content

        except RateLimitError as e:
            # Rate limited - wait and retry
            wait_time = min(2 ** attempt, 60)  # Exponential backoff, max 60s
            logger.warning(f"Rate limited. Retrying in {wait_time}s...")
            time.sleep(wait_time)

        except APIError as e:
            # Server error - retry
            if e.status_code >= 500:
                wait_time = min(2 ** attempt, 60)
                logger.error(f"API error {e.status_code}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                # Client error - don't retry
                logger.error(f"Client error: {e}")
                raise

        except OpenAIError as e:
            # Other OpenAI errors
            logger.error(f"OpenAI error: {e}")
            raise

        except Exception as e:
            # Unexpected errors
            logger.error(f"Unexpected error: {e}", exc_info=True)
            raise

    raise Exception(f"Failed after {max_retries} retries")
```

### Anthropic Python SDK

```python
from anthropic import Anthropic, APIError, RateLimitError
import time
import logging

client = Anthropic(api_key="your-api-key")
logger = logging.getLogger(__name__)

def claude_chat_with_retry(messages: list, max_retries: int = 3) -> str:
    """Call Claude with retry logic and error handling."""
    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=messages
            )

            # Extract text content from response
            return response.content[0].text

        except RateLimitError as e:
            wait_time = min(2 ** attempt, 60)
            logger.warning(f"Rate limited. Retrying in {wait_time}s...")
            time.sleep(wait_time)

        except APIError as e:
            # Check if retriable
            if e.status_code in [500, 502, 503, 504, 529]:
                wait_time = min(2 ** attempt, 60)
                logger.error(f"API error {e.status_code}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                logger.error(f"Non-retriable API error: {e}")
                raise

        except Exception as e:
            logger.error(f"Unexpected error: {e}", exc_info=True)
            raise

    raise Exception(f"Failed after {max_retries} retries")
```

### Google Gemini Python SDK

```python
import google.generativeai as genai
from google.api_core import retry, exceptions
import logging

genai.configure(api_key="your-api-key")
logger = logging.getLogger(__name__)

# Configure retry policy
@retry.Retry(
    predicate=retry.if_exception_type(
        exceptions.ResourceExhausted,  # Rate limit/quota
        exceptions.ServiceUnavailable,  # Server error
        exceptions.DeadlineExceeded    # Timeout
    ),
    initial=1.0,
    maximum=60.0,
    multiplier=2.0,
    deadline=300.0
)
def gemini_chat_with_retry(prompt: str) -> str:
    """Call Gemini with automatic retry via decorator."""
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(prompt)
        return response.text

    except exceptions.InvalidArgument as e:
        # Bad input - don't retry
        logger.error(f"Invalid argument: {e}")
        raise

    except exceptions.PermissionDenied as e:
        # Auth issue - don't retry
        logger.error(f"Permission denied: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        raise
```

### TypeScript/Node.js Error Handling

**OpenAI Node SDK:**

```typescript
import OpenAI from "openai";

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

async function chatWithRetry(
  messages: OpenAI.ChatCompletionMessageParam[],
  maxRetries: number = 3
): Promise<string> {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      const response = await client.chat.completions.create({
        model: "gpt-4-turbo",
        messages,
        temperature: 0.7
      });

      return response.choices[0].message.content || "";

    } catch (error) {
      if (error instanceof OpenAI.APIError) {
        // Rate limit or server error - retry
        if (error.status === 429 || (error.status >= 500 && error.status < 600)) {
          const waitTime = Math.min(2 ** attempt, 60) * 1000;
          console.warn(`${error.status} error. Retrying in ${waitTime}ms...`);
          await new Promise(resolve => setTimeout(resolve, waitTime));
          continue;
        }

        // Client error - don't retry
        console.error(`Client error: ${error.message}`);
        throw error;
      }

      // Unexpected error
      console.error("Unexpected error:", error);
      throw error;
    }
  }

  throw new Error(`Failed after ${maxRetries} retries`);
}
```

## Streaming Implementation

### OpenAI Streaming (Python)

```python
from openai import OpenAI

client = OpenAI(api_key="your-api-key")

def stream_chat(messages: list):
    """Stream chat completion with progress updates."""
    stream = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages,
        stream=True
    )

    full_response = ""

    for chunk in stream:
        # Extract delta content
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            print(content, end="", flush=True)

    print()  # Newline after completion
    return full_response
```

**FastAPI streaming endpoint:**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import openai

app = FastAPI()

@app.post("/chat/stream")
async def stream_chat(messages: list):
    """Stream chat completions to client."""
    def generate():
        stream = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages,
            stream=True
        )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                yield f"data: {content}\n\n"

        yield "data: [DONE]\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )
```

### Anthropic Streaming (Python)

```python
from anthropic import Anthropic

client = Anthropic(api_key="your-api-key")

def stream_claude(messages: list):
    """Stream Claude response with events."""
    full_response = ""

    with client.messages.stream(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=messages
    ) as stream:
        for text in stream.text_stream:
            full_response += text
            print(text, end="", flush=True)

    print()
    return full_response
```

**Event-based streaming:**

```python
def stream_claude_events(messages: list):
    """Stream with detailed event handling."""
    full_response = ""

    with client.messages.stream(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=messages
    ) as stream:
        for event in stream:
            if event.type == "content_block_start":
                print(f"[Block started: {event.content_block.type}]")
            elif event.type == "content_block_delta":
                text = event.delta.text
                full_response += text
                print(text, end="", flush=True)
            elif event.type == "content_block_stop":
                print(f"\n[Block completed]")
            elif event.type == "message_stop":
                print(f"[Total tokens: {stream.get_final_message().usage}]")

    return full_response
```

### Google Gemini Streaming (Python)

```python
import google.generativeai as genai

genai.configure(api_key="your-api-key")

def stream_gemini(prompt: str):
    """Stream Gemini response."""
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(prompt, stream=True)

    full_response = ""
    for chunk in response:
        if chunk.text:
            full_response += chunk.text
            print(chunk.text, end="", flush=True)

    print()
    return full_response
```

### TypeScript Streaming

**OpenAI with Server-Sent Events:**

```typescript
import OpenAI from "openai";
import type { Request, Response } from "express";

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

async function streamChatHandler(req: Request, res: Response) {
  res.setHeader("Content-Type", "text/event-stream");
  res.setHeader("Cache-Control", "no-cache");
  res.setHeader("Connection", "keep-alive");

  try {
    const stream = await client.chat.completions.create({
      model: "gpt-4-turbo",
      messages: req.body.messages,
      stream: true
    });

    for await (const chunk of stream) {
      const content = chunk.choices[0]?.delta?.content;
      if (content) {
        res.write(`data: ${JSON.stringify({ content })}\n\n`);
      }
    }

    res.write("data: [DONE]\n\n");
    res.end();

  } catch (error) {
    console.error("Streaming error:", error);
    res.status(500).json({ error: "Streaming failed" });
  }
}
```

## Rate Limiting and Retries

### Token Bucket Algorithm

```python
import time
from collections import defaultdict
from threading import Lock

class TokenBucket:
    """Thread-safe token bucket rate limiter."""

    def __init__(self, rate: float, capacity: float):
        """
        Initialize token bucket.

        Args:
            rate: Tokens added per second
            capacity: Maximum tokens in bucket
        """
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_update = time.time()
        self.lock = Lock()

    def consume(self, tokens: float = 1.0) -> bool:
        """
        Try to consume tokens.

        Returns:
            True if tokens consumed, False if insufficient
        """
        with self.lock:
            now = time.time()
            elapsed = now - self.last_update

            # Add tokens based on elapsed time
            self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
            self.last_update = now

            if self.tokens >= tokens:
                self.tokens -= tokens
                return True

            return False

    def wait_for_tokens(self, tokens: float = 1.0, timeout: float = None):
        """Wait until tokens available."""
        start = time.time()

        while True:
            if self.consume(tokens):
                return

            # Check timeout
            if timeout and (time.time() - start) > timeout:
                raise TimeoutError("Token bucket timeout")

            time.sleep(0.1)


# Usage
rate_limiter = TokenBucket(rate=10.0, capacity=100.0)  # 10 requests/sec

def make_api_call():
    """API call with rate limiting."""
    rate_limiter.wait_for_tokens(1.0)
    return call_llm_api()
```

### Per-User Rate Limiting

```python
from functools import wraps
from flask import request, jsonify
from datetime import datetime, timedelta

# Rate limit storage (use Redis in production)
user_requests = defaultdict(list)
RATE_LIMIT = 100  # requests per minute
WINDOW = timedelta(minutes=1)

def rate_limit_by_user(func):
    """Decorator to rate limit by user ID."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = request.headers.get("X-User-ID")
        if not user_id:
            return jsonify({"error": "User ID required"}), 401

        now = datetime.now()
        cutoff = now - WINDOW

        # Clean old requests
        user_requests[user_id] = [
            t for t in user_requests[user_id] if t > cutoff
        ]

        # Check limit
        if len(user_requests[user_id]) >= RATE_LIMIT:
            return jsonify({
                "error": "Rate limit exceeded",
                "retry_after": 60
            }), 429

        # Record request
        user_requests[user_id].append(now)

        return func(*args, **kwargs)

    return wrapper


@app.post("/chat")
@rate_limit_by_user
def chat_endpoint():
    """Rate-limited chat endpoint."""
    return process_chat(request.json)
```

### Intelligent Retry with Backoff

```python
import random
import time
from functools import wraps

def retry_with_backoff(
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    exponential_base: float = 2.0,
    jitter: bool = True
):
    """
    Decorator for retry with exponential backoff.

    Args:
        max_retries: Maximum retry attempts
        base_delay: Initial delay in seconds
        max_delay: Maximum delay in seconds
        exponential_base: Base for exponential backoff
        jitter: Add random jitter to prevent thundering herd
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)

                except RateLimitError:
                    if attempt == max_retries - 1:
                        raise

                    # Calculate delay
                    delay = min(
                        base_delay * (exponential_base ** attempt),
                        max_delay
                    )

                    # Add jitter
                    if jitter:
                        delay *= (0.5 + random.random())

                    print(f"Rate limited. Retrying in {delay:.2f}s...")
                    time.sleep(delay)

                except (APIError, ConnectionError) as e:
                    if attempt == max_retries - 1:
                        raise

                    delay = min(
                        base_delay * (exponential_base ** attempt),
                        max_delay
                    )

                    if jitter:
                        delay *= (0.5 + random.random())

                    print(f"Error: {e}. Retrying in {delay:.2f}s...")
                    time.sleep(delay)

            raise Exception(f"Failed after {max_retries} retries")

        return wrapper
    return decorator


@retry_with_backoff(max_retries=5, base_delay=1.0, max_delay=60.0)
def robust_api_call(messages: list) -> str:
    """API call with automatic retry."""
    return client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages
    )
```

## Context Management

### Sliding Window for Long Conversations

```python
import tiktoken

def num_tokens_from_messages(messages: list, model: str = "gpt-4-turbo") -> int:
    """Calculate token count for messages."""
    encoding = tiktoken.encoding_for_model(model)

    num_tokens = 0
    for message in messages:
        num_tokens += 4  # Message overhead
        for key, value in message.items():
            num_tokens += len(encoding.encode(str(value)))

    num_tokens += 2  # Priming tokens
    return num_tokens


def trim_messages(messages: list, max_tokens: int = 120000) -> list:
    """
    Trim messages to fit within token limit using sliding window.

    Keeps system message and recent messages.
    """
    if num_tokens_from_messages(messages) <= max_tokens:
        return messages

    # Always keep system message (index 0)
    system_msg = messages[0] if messages[0]["role"] == "system" else None
    conversation = messages[1:] if system_msg else messages

    # Start from most recent and work backwards
    trimmed = []
    total_tokens = 0

    if system_msg:
        total_tokens = num_tokens_from_messages([system_msg])

    for message in reversed(conversation):
        msg_tokens = num_tokens_from_messages([message])

        if total_tokens + msg_tokens > max_tokens:
            break

        trimmed.insert(0, message)
        total_tokens += msg_tokens

    if system_msg:
        trimmed.insert(0, system_msg)

    return trimmed


# Usage
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    # ... many messages ...
]

messages = trim_messages(messages, max_tokens=100000)
response = client.chat.completions.create(model="gpt-4-turbo", messages=messages)
```

### Conversation Summarization

```python
def summarize_old_messages(messages: list, threshold: int = 10) -> list:
    """
    Summarize old messages when conversation gets too long.

    Keeps system message, summarizes middle messages, keeps recent messages.
    """
    if len(messages) <= threshold:
        return messages

    system_msg = messages[0] if messages[0]["role"] == "system" else None
    start_idx = 1 if system_msg else 0

    # Keep last 5 messages as-is
    recent_messages = messages[-5:]

    # Summarize middle messages
    middle_messages = messages[start_idx:-5]

    summary_prompt = "Summarize this conversation history concisely:\n\n"
    for msg in middle_messages:
        summary_prompt += f"{msg['role']}: {msg['content']}\n"

    summary_response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use cheaper model for summarization
        messages=[
            {"role": "user", "content": summary_prompt}
        ],
        max_tokens=500
    )

    summary = summary_response.choices[0].message.content

    # Rebuild messages
    result = []
    if system_msg:
        result.append(system_msg)

    result.append({
        "role": "assistant",
        "content": f"[Previous conversation summary: {summary}]"
    })

    result.extend(recent_messages)
    return result
```

### Document Chunking with Overlap

```python
from typing import List

def chunk_text_with_overlap(
    text: str,
    chunk_size: int = 10000,
    overlap: int = 1000,
    encoding: str = "gpt-4-turbo"
) -> List[str]:
    """
    Split text into overlapping chunks.

    Args:
        text: Text to chunk
        chunk_size: Max tokens per chunk
        overlap: Overlap tokens between chunks
        encoding: Model name for tokenization

    Returns:
        List of text chunks
    """
    enc = tiktoken.encoding_for_model(encoding)
    tokens = enc.encode(text)

    chunks = []
    start = 0

    while start < len(tokens):
        end = start + chunk_size
        chunk_tokens = tokens[start:end]
        chunk_text = enc.decode(chunk_tokens)
        chunks.append(chunk_text)

        start = end - overlap  # Step back for overlap

    return chunks


# Usage: Process long document in chunks
document = read_long_document()
chunks = chunk_text_with_overlap(document, chunk_size=10000, overlap=1000)

results = []
for i, chunk in enumerate(chunks):
    result = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "user", "content": f"Analyze this section (part {i+1}/{len(chunks)}):\n\n{chunk}"}
        ]
    )
    results.append(result.choices[0].message.content)

# Combine results
final_summary = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "user", "content": f"Combine these analyses:\n\n" + "\n\n".join(results)}
    ]
)
```

## Cost Tracking

### Request-Level Cost Tracking

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Dict

# Pricing (per 1M tokens, as of Jan 2025)
PRICING = {
    "gpt-4-turbo": {"input": 10.00, "output": 30.00},
    "gpt-4o": {"input": 5.00, "output": 15.00},
    "gpt-3.5-turbo": {"input": 0.50, "output": 1.50},
    "claude-3-5-sonnet-20241022": {"input": 3.00, "output": 15.00},
    "claude-3-opus-20240229": {"input": 15.00, "output": 75.00},
    "claude-3-haiku-20240307": {"input": 0.25, "output": 1.25},
}

@dataclass
class APICall:
    """Record of an API call with cost tracking."""
    timestamp: datetime
    model: str
    input_tokens: int
    output_tokens: int
    latency_ms: float
    user_id: str = None
    request_id: str = None

    @property
    def cost(self) -> float:
        """Calculate cost for this call."""
        if self.model not in PRICING:
            return 0.0

        pricing = PRICING[self.model]
        input_cost = (self.input_tokens / 1_000_000) * pricing["input"]
        output_cost = (self.output_tokens / 1_000_000) * pricing["output"]
        return input_cost + output_cost


class CostTracker:
    """Track API costs across requests."""

    def __init__(self):
        self.calls: List[APICall] = []

    def record_call(self, call: APICall):
        """Record an API call."""
        self.calls.append(call)

    def total_cost(self, user_id: str = None) -> float:
        """Calculate total cost, optionally filtered by user."""
        calls = self.calls
        if user_id:
            calls = [c for c in calls if c.user_id == user_id]
        return sum(c.cost for c in calls)

    def cost_by_model(self) -> Dict[str, float]:
        """Break down cost by model."""
        costs = {}
        for call in self.calls:
            costs[call.model] = costs.get(call.model, 0.0) + call.cost
        return costs

    def cost_today(self) -> float:
        """Calculate cost for today."""
        today = datetime.now().date()
        today_calls = [c for c in self.calls if c.timestamp.date() == today]
        return sum(c.cost for c in today_calls)


# Usage
tracker = CostTracker()

def tracked_chat(messages: list, user_id: str) -> str:
    """Chat with cost tracking."""
    start_time = time.time()

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages
    )

    latency_ms = (time.time() - start_time) * 1000

    # Record call
    call = APICall(
        timestamp=datetime.now(),
        model="gpt-4-turbo",
        input_tokens=response.usage.prompt_tokens,
        output_tokens=response.usage.completion_tokens,
        latency_ms=latency_ms,
        user_id=user_id,
        request_id=response.id
    )

    tracker.record_call(call)

    print(f"Cost: ${call.cost:.4f}, Total today: ${tracker.cost_today():.2f}")

    return response.choices[0].message.content
```

### Budget Enforcement

```python
class BudgetEnforcer:
    """Enforce spending budgets."""

    def __init__(self, daily_limit: float, monthly_limit: float):
        self.daily_limit = daily_limit
        self.monthly_limit = monthly_limit
        self.tracker = CostTracker()

    def check_budget(self, user_id: str = None) -> bool:
        """Check if within budget."""
        # Daily check
        today_cost = self.tracker.cost_today()
        if today_cost >= self.daily_limit:
            raise BudgetExceededError(f"Daily budget exceeded: ${today_cost:.2f}")

        # Monthly check (simplified)
        total_cost = self.tracker.total_cost(user_id)
        if total_cost >= self.monthly_limit:
            raise BudgetExceededError(f"Monthly budget exceeded: ${total_cost:.2f}")

        return True

    def remaining_budget(self) -> Dict[str, float]:
        """Get remaining budget."""
        today_cost = self.tracker.cost_today()
        total_cost = self.tracker.total_cost()

        return {
            "daily_remaining": self.daily_limit - today_cost,
            "monthly_remaining": self.monthly_limit - total_cost
        }


# Usage
budget = BudgetEnforcer(daily_limit=100.0, monthly_limit=2000.0)

def budgeted_chat(messages: list, user_id: str) -> str:
    """Chat with budget enforcement."""
    budget.check_budget(user_id)
    response = tracked_chat(messages, user_id)
    return response
```

## Caching Strategies

### Response Caching with Redis

```python
import redis
import json
import hashlib

redis_client = redis.Redis(host='localhost', port=6379, db=0)
CACHE_TTL = 3600  # 1 hour

def cache_key(messages: list, model: str, temperature: float) -> str:
    """Generate cache key from request parameters."""
    # Create deterministic hash
    cache_data = {
        "messages": messages,
        "model": model,
        "temperature": temperature
    }
    cache_str = json.dumps(cache_data, sort_keys=True)
    return hashlib.sha256(cache_str.encode()).hexdigest()


def cached_chat(messages: list, model: str = "gpt-4-turbo", temperature: float = 0.7) -> str:
    """Chat with Redis caching."""
    key = cache_key(messages, model, temperature)

    # Check cache
    cached = redis_client.get(key)
    if cached:
        print("Cache hit!")
        return cached.decode('utf-8')

    # Cache miss - call API
    print("Cache miss, calling API...")
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )

    result = response.choices[0].message.content

    # Store in cache
    redis_client.setex(key, CACHE_TTL, result)

    return result
```

### Semantic Similarity Caching

```python
from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Cache storage
semantic_cache = {}  # In production, use vector database

def semantic_cache_key(messages: list, threshold: float = 0.95) -> str:
    """
    Find similar cached query using semantic similarity.

    Returns cache key if similar query found, else None.
    """
    # Get embedding for current query
    query_text = " ".join(m["content"] for m in messages)
    query_embedding = embedding_model.encode(query_text)

    # Check for similar cached queries
    best_similarity = 0.0
    best_key = None

    for cached_query, cached_data in semantic_cache.items():
        cached_embedding = cached_data["embedding"]

        # Cosine similarity
        similarity = np.dot(query_embedding, cached_embedding) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(cached_embedding)
        )

        if similarity > best_similarity:
            best_similarity = similarity
            best_key = cached_query

    if best_similarity >= threshold:
        return best_key

    return None


def semantic_cached_chat(messages: list) -> str:
    """Chat with semantic similarity caching."""
    # Check for similar query
    similar_key = semantic_cache_key(messages, threshold=0.95)

    if similar_key:
        print(f"Semantic cache hit! Similarity: {similar_key}")
        return semantic_cache[similar_key]["response"]

    # Cache miss - call API
    print("No similar query found, calling API...")
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages
    )

    result = response.choices[0].message.content

    # Store in semantic cache
    query_text = " ".join(m["content"] for m in messages)
    query_embedding = embedding_model.encode(query_text)

    semantic_cache[query_text] = {
        "embedding": query_embedding,
        "response": result,
        "timestamp": datetime.now()
    }

    return result
```

## Multi-Provider Abstraction

### Provider Interface

```python
from abc import ABC, abstractmethod
from typing import List, Dict

class LLMProvider(ABC):
    """Abstract base class for LLM providers."""

    @abstractmethod
    def chat(self, messages: List[Dict], **kwargs) -> str:
        """Send chat request and return response."""
        pass

    @abstractmethod
    def stream_chat(self, messages: List[Dict], **kwargs):
        """Stream chat response."""
        pass

    @abstractmethod
    def count_tokens(self, text: str) -> int:
        """Count tokens in text."""
        pass


class OpenAIProvider(LLMProvider):
    """OpenAI implementation."""

    def __init__(self, api_key: str, model: str = "gpt-4-turbo"):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.encoding = tiktoken.encoding_for_model(model)

    def chat(self, messages: List[Dict], **kwargs) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            **kwargs
        )
        return response.choices[0].message.content

    def stream_chat(self, messages: List[Dict], **kwargs):
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=True,
            **kwargs
        )
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    def count_tokens(self, text: str) -> int:
        return len(self.encoding.encode(text))


class AnthropicProvider(LLMProvider):
    """Anthropic Claude implementation."""

    def __init__(self, api_key: str, model: str = "claude-3-5-sonnet-20241022"):
        self.client = Anthropic(api_key=api_key)
        self.model = model

    def chat(self, messages: List[Dict], **kwargs) -> str:
        # Convert OpenAI-style messages to Claude format if needed
        response = self.client.messages.create(
            model=self.model,
            max_tokens=kwargs.get("max_tokens", 1024),
            messages=messages
        )
        return response.content[0].text

    def stream_chat(self, messages: List[Dict], **kwargs):
        with self.client.messages.stream(
            model=self.model,
            max_tokens=kwargs.get("max_tokens", 1024),
            messages=messages
        ) as stream:
            for text in stream.text_stream:
                yield text

    def count_tokens(self, text: str) -> int:
        # Claude uses Anthropic's tokenizer
        response = self.client.count_tokens(text)
        return response.token_count


# Usage: Switch providers easily
provider = OpenAIProvider(api_key="sk-...")
# provider = AnthropicProvider(api_key="sk-ant-...")

messages = [{"role": "user", "content": "Hello!"}]
response = provider.chat(messages)
```

### Intelligent Provider Router

```python
class ProviderRouter:
    """Route requests to optimal provider based on requirements."""

    def __init__(self, providers: Dict[str, LLMProvider]):
        self.providers = providers

    def route(self, messages: List[Dict], requirements: Dict = None) -> str:
        """
        Route to best provider based on requirements.

        Requirements:
            - context_length: Max tokens needed
            - cost_sensitive: Prefer cheaper model
            - quality: Prefer highest quality
            - speed: Prefer fastest model
        """
        requirements = requirements or {}

        # Route based on context length
        if requirements.get("context_length", 0) > 128000:
            provider = self.providers.get("gemini")  # 2M context
        elif requirements.get("cost_sensitive"):
            provider = self.providers.get("gpt-3.5")  # Cheapest
        elif requirements.get("quality"):
            provider = self.providers.get("claude-opus")  # Highest quality
        elif requirements.get("speed"):
            provider = self.providers.get("claude-haiku")  # Fastest
        else:
            provider = self.providers.get("default")  # GPT-4 Turbo

        return provider.chat(messages)


# Usage
router = ProviderRouter({
    "default": OpenAIProvider(api_key="...", model="gpt-4-turbo"),
    "gpt-3.5": OpenAIProvider(api_key="...", model="gpt-3.5-turbo"),
    "claude-opus": AnthropicProvider(api_key="...", model="claude-3-opus-20240229"),
    "claude-haiku": AnthropicProvider(api_key="...", model="claude-3-haiku-20240307"),
})

# Route based on requirements
response = router.route(
    messages=[{"role": "user", "content": "Analyze this..."}],
    requirements={"quality": True}
)
```

## References

- OpenAI Python SDK: https://github.com/openai/openai-python
- Anthropic Python SDK: https://github.com/anthropics/anthropic-sdk-python
- Google Generative AI SDK: https://github.com/google/generative-ai-python
- Tiktoken (OpenAI tokenizer): https://github.com/openai/tiktoken

**Last Updated:** January 2025
