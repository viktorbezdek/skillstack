# Async/Await Cookbook

Deep dive into async programming in Python 3.14+.

---

## Running Concurrent Tasks with TaskGroup

**Problem**: You need to run multiple async operations concurrently with proper error handling and automatic cleanup.

**Solution**:
```python
import asyncio

async def fetch_data(url: str) -> str:
    await asyncio.sleep(0.1)
    return f"Data from {url}"

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_data("url1"))
        task2 = tg.create_task(fetch_data("url2"))
        task3 = tg.create_task(fetch_data("url3"))

    # All tasks completed or exception raised
    print(f"Task1: {task1.result()}")
    print(f"Task2: {task2.result()}")
    print(f"Task3: {task3.result()}")

asyncio.run(main())
```

**Tip**: TaskGroup (Python 3.11+) is the recommended way for structured concurrency. It ensures all tasks complete before exiting the context and properly propagates exceptions.

---

## Gathering Multiple Results

**Problem**: You need to collect results from multiple async operations running in parallel.

**Solution**:
```python
async def fetch_all(urls: list[str]) -> list[str]:
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

# With return_exceptions for partial failures
async def fetch_all_safe(urls: list[str]):
    results = await asyncio.gather(
        *[fetch_data(url) for url in urls],
        return_exceptions=True
    )
    successes = [r for r in results if not isinstance(r, Exception)]
    errors = [r for r in results if isinstance(r, Exception)]
    return successes, errors
```

**Tip**: Use `return_exceptions=True` to handle partial failures gracefully. Without it, any single failure will raise an exception immediately.

---

## Adding Timeouts to Async Operations

**Problem**: You need to ensure async operations don't run indefinitely.

**Solution**:
```python
async def with_timeout():
    try:
        async with asyncio.timeout(5.0):
            result = await slow_operation()
            return result
    except asyncio.TimeoutError:
        print("Operation timed out")
        return None

# wait_for (older API)
try:
    result = await asyncio.wait_for(slow_operation(), timeout=5.0)
except asyncio.TimeoutError:
    print("Timed out")
```

**Tip**: Prefer `asyncio.timeout()` context manager (Python 3.11+) over `wait_for()` for cleaner timeout handling.

---

## Creating Async Generators

**Problem**: You need to yield values asynchronously, processing data as it becomes available.

**Solution**:
```python
from typing import AsyncGenerator

async def async_range(n: int) -> AsyncGenerator[int, None]:
    for i in range(n):
        await asyncio.sleep(0.01)
        yield i

async def consume():
    async for value in async_range(5):
        print(value)
```

**Tip**: Use async generators for streaming data, paginated API responses, or any scenario where you want to process items as they arrive rather than waiting for all data.

---

## Using Async Comprehensions

**Problem**: You want to build collections from async generators concisely.

**Solution**:
```python
async def get_items() -> list[int]:
    return [i async for i in async_range(10)]

async def filter_items() -> list[int]:
    return [i async for i in async_range(10) if i % 2 == 0]
```

**Tip**: Async comprehensions work just like regular comprehensions but use `async for` to iterate over async iterables.

---

## Cleaning Up Async Generators

**Problem**: You need to ensure cleanup happens when an async generator is done or interrupted.

**Solution**:
```python
async def stream_data():
    try:
        async for chunk in fetch_stream():
            yield chunk
    finally:
        await cleanup_connection()
```

**Tip**: Always use try/finally blocks in async generators to guarantee cleanup code runs, even if the generator is closed early.

---

## Creating Class-Based Async Context Managers

**Problem**: You need to manage async resources with setup and teardown logic.

**Solution**:
```python
class AsyncDatabaseConnection:
    async def __aenter__(self):
        print("Connecting...")
        await asyncio.sleep(0.1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Closing...")
        await asyncio.sleep(0.05)
        return False  # Don't suppress exceptions

async def use_db():
    async with AsyncDatabaseConnection() as conn:
        print("Using connection")
```

**Tip**: Return `False` from `__aexit__` to let exceptions propagate. Only return `True` if you want to suppress exceptions.

---

## Creating Decorator-Based Async Context Managers

**Problem**: You want to create simple async context managers without defining a full class.

**Solution**:
```python
from contextlib import asynccontextmanager
from typing import AsyncGenerator

@asynccontextmanager
async def async_timer(name: str) -> AsyncGenerator[None, None]:
    import time
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name} took {elapsed:.4f}s")

async def timed_operation():
    async with async_timer("fetch"):
        await fetch_data("url")
```

**Tip**: Use `@asynccontextmanager` for one-off context managers. It's more concise than defining a class with `__aenter__` and `__aexit__`.

---

## Making HTTP Requests with httpx

**Problem**: You need to make async HTTP requests efficiently.

**Solution**:
```python
import httpx

async def fetch_json(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

async def post_data(url: str, data: dict) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
        response.raise_for_status()
        return response.json()
```

**Tip**: Always use `async with` to ensure the client is properly closed. Never use the synchronous `requests` library in async code.

---

## Reusing HTTP Client for Multiple Requests

**Problem**: You need to make multiple HTTP requests and want to reuse connections for better performance.

**Solution**:
```python
async def fetch_multiple(urls: list[str]) -> list[dict]:
    async with httpx.AsyncClient() as client:
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(client.get(url))
                for url in urls
            ]
        return [t.result().json() for t in tasks]
```

**Tip**: Reusing a single AsyncClient across multiple requests enables connection pooling and significantly improves performance.

---

## Adding Retry Logic to HTTP Requests

**Problem**: You need to automatically retry failed HTTP requests with backoff.

**Solution**:
```python
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1))
async def fetch_with_retry(url: str) -> dict:
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
```

**Tip**: Use the `tenacity` library for robust retry logic with exponential backoff. Combine with timeouts to prevent hanging requests.

---

## Handling Exception Groups

**Problem**: You need to handle different types of exceptions from multiple concurrent tasks.

**Solution**:
```python
async def run_tasks():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(might_fail_1())
            tg.create_task(might_fail_2())
            tg.create_task(might_fail_3())
    except* ValueError as eg:
        print(f"ValueError(s): {eg.exceptions}")
    except* TypeError as eg:
        print(f"TypeError(s): {eg.exceptions}")
```

**Tip**: Use `except*` syntax (Python 3.11+) to handle exception groups from TaskGroup. It allows you to handle different exception types separately.

---

## Implementing Graceful Degradation

**Problem**: You want your async code to continue working even if some operations fail.

**Solution**:
```python
async def fetch_with_fallback(primary: str, fallback: str) -> str:
    try:
        return await fetch_data(primary)
    except Exception:
        return await fetch_data(fallback)

async def fetch_best_effort(urls: list[str]) -> list[str]:
    results = await asyncio.gather(
        *[fetch_data(url) for url in urls],
        return_exceptions=True
    )
    return [r for r in results if isinstance(r, str)]
```

**Tip**: Use fallbacks for critical operations and filter out exceptions for best-effort batch operations.

---

## Running Blocking Code in Async Context

**Problem**: You need to run blocking I/O or CPU-intensive code without blocking the event loop.

**Solution**:
```python
import asyncio

def blocking_io():
    import time
    time.sleep(1)
    return "done"

async def main():
    # Run blocking code without blocking event loop
    result = await asyncio.to_thread(blocking_io)
    print(result)
```

**Tip**: Always use `asyncio.to_thread()` for blocking operations. Never call blocking functions directly in async code or use `time.sleep()`.

---

## Rate Limiting with Semaphores

**Problem**: You need to limit the number of concurrent async operations.

**Solution**:
```python
async def fetch_with_limit(urls: list[str], max_concurrent: int = 10):
    semaphore = asyncio.Semaphore(max_concurrent)

    async def limited_fetch(url: str):
        async with semaphore:
            return await fetch_data(url)

    return await asyncio.gather(*[limited_fetch(url) for url in urls])
```

**Tip**: Use semaphores to prevent overwhelming external services or exhausting system resources when making many concurrent requests.

---

## Coordinating Tasks with Events

**Problem**: You need to signal between async tasks or wait for a specific condition.

**Solution**:
```python
async def waiter(event: asyncio.Event):
    print("Waiting...")
    await event.wait()
    print("Got signal!")

async def setter(event: asyncio.Event):
    await asyncio.sleep(1)
    event.set()

async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))
```

**Tip**: Events are useful for simple signaling between tasks. For passing data, use Queues instead.

---

## Producer-Consumer Pattern with Queues

**Problem**: You need to process items asynchronously with separate producer and consumer tasks.

**Solution**:
```python
async def producer(queue: asyncio.Queue):
    for i in range(10):
        await queue.put(i)
        await asyncio.sleep(0.1)
    await queue.put(None)  # Sentinel

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Processing {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))
```

**Tip**: Use a sentinel value (like `None`) to signal when the producer is done. Call `task_done()` after processing each item for proper queue tracking.

---

## Protecting Shared State with Locks

**Problem**: You need to safely access and modify shared state from multiple async tasks.

**Solution**:
```python
class AsyncCounter:
    def __init__(self):
        self.value = 0
        self._lock = asyncio.Lock()

    async def increment(self):
        async with self._lock:
            self.value += 1
            return self.value
```

**Tip**: Always use locks when multiple tasks access shared mutable state. Without locks, you risk race conditions even in async code.

---

## Anti-Patterns to Avoid

**Problem**: You want to avoid common mistakes in async Python code.

**Solution**:

| Avoid | Do Instead |
|-------|------------|
| `requests.get(url)` | `await client.get(url)` with httpx |
| `time.sleep(n)` | `await asyncio.sleep(n)` |
| Bare `asyncio.create_task()` | Use TaskGroup or gather |
| Global event loop | `asyncio.run(main())` |
| `loop.run_until_complete()` | `asyncio.run()` |

**Tip**: Blocking calls in async code will freeze the entire event loop. Always use async equivalents and prefer modern APIs like TaskGroup and `asyncio.run()`.

---

## Quick Reference

**Problem**: You need a quick lookup of common async patterns.

**Solution**:
```python
# Run async code
asyncio.run(main())

# Create tasks
async with asyncio.TaskGroup() as tg:
    task = tg.create_task(coro())

# Concurrent execution
results = await asyncio.gather(*coros)

# Timeout
async with asyncio.timeout(5.0):
    await slow_op()

# Sleep
await asyncio.sleep(1.0)

# Run blocking in thread
await asyncio.to_thread(blocking_fn)

# Rate limit
async with semaphore:
    await limited_op()
```

**Tip**: Bookmark this reference for quick access to the most common async patterns in Python 3.11+.
