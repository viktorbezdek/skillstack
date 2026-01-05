# FastMCP Development Guidelines

Complete guide to building MCP servers with FastMCP, covering decorators, validation, async patterns, error handling, and deployment.

## Core Abstractions

RULE: The model must instantiate FastMCP object before registering tools RULE: The model must use decorators to expose Python functions as MCP capabilities RULE: The model must not implement low-level MCP protocol details (FastMCP handles this)

PATTERN:

```python
mcp = FastMCP("server-name")

@mcp.tool()
def tool_name(...):
    ...

@mcp.prompt()
def prompt_name(...):
    ...

@mcp.resource("uri://pattern")
def resource_name(...):
    ...
```

## Define Tools with Decorators

Annotate functions with `@mcp.tool` to turn them into callable tools for the AI client.

### Tool Name and Description

AUTO_GENERATION:

- Tool name ← function name (override: `@mcp.tool(name="custom")`)
- Description ← first line of docstring (override: `@mcp.tool(description="...")`)
- JSON Schema ← type hints

### Type Annotations Required

RULE: The model must annotate all parameters and return values RULE: The model must use type hints to enable automatic validation RULE: The model must return dict or Pydantic models for structured output

DECISION_TREE:

```text
1. IF parameter needs validation THEN
   - Use Annotated[type, Field(...)]
   - Add constraints (ge, le, pattern, etc)
2. ELSE IF parameter is optional THEN
   - Use type | None with default = None
3. ELSE
   - Use plain type hint

4. IF return value is structured THEN
   - Return dict or Pydantic model
5. ELSE IF return value is simple THEN
   - Return str, int, bool (discouraged for AI consumption)
```

CONSTRAINTS:

- The model must not omit type hints (causes schema generation failure)
- The model must not return unstructured strings (AI cannot parse reliably)
- The model must use structured dict for all non-trivial outputs

### Example Tool Definition

```python
from fastmcp import FastMCP
from pydantic import Field
from typing import Annotated

mcp = FastMCP("product-search")

@mcp.tool()
def search_products(
    query: str,
    category: Annotated[str | None, Field(description="Filter by product category")] = None,
    max_results: Annotated[int, Field(ge=1, le=100, description="Maximum results to return")] = 10
) -> dict:
    """Search the product catalog with optional category filtering.

    Returns product information including name, price, availability, and ratings.
    Useful for finding products based on keywords or browsing by category.
    """
    # Implementation
    results = database.search(query, category, limit=max_results)
    return {"results": results, "count": len(results)}
```

## Parameter Metadata & Validation

FastMCP integrates with Pydantic for robust parameter handling.

### Field Constraints

Attach `typing.Annotated` with `Field(...)` to impose constraints and descriptions:

```python
from pydantic import Field
from typing import Annotated, Literal

# Numeric ranges
width: Annotated[int, Field(ge=1, le=2000, description="Image width in pixels")]
price: Annotated[float, Field(ge=0.01, description="Price must be positive")]

# String patterns
email: Annotated[str, Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')]
code: Annotated[str, Field(min_length=3, max_length=10)]

# Literal types for enums
action: Annotated[Literal["read", "write", "delete"], Field(description="Allowed actions")]
format: Annotated[Literal["json", "xml", "yaml"], Field(description="Output format")]

# Lists with item constraints
tags: Annotated[list[str], Field(min_length=1, max_length=10, description="1-10 tags")]

# Exclude from schema (runtime injection)
api_key: Annotated[str, Field(exclude=True)] = None

# Optional parameters
category: Annotated[str | None, Field(description="Optional category filter")] = None
```

### Parameter Validation Benefits

- **Safety**: AI cannot call tools with invalid or dangerous inputs
- **Documentation**: Constraints appear in tool schema for the AI to see
- **Automatic checking**: FastMCP validates before calling your function

### Excluding Parameters from Schema

Use `Field(exclude=True)` for parameters that should not be visible to the LLM (e.g., secrets, runtime-injected values):

```python
@mcp.tool()
def api_call(
    query: str,
    api_key: Annotated[str, Field(exclude=True)] = None  # Injected at runtime
) -> dict:
    # api_key never appears in the tool schema the LLM sees
    headers = {"Authorization": f"Bearer {api_key}"}
    # ...
```

**Note**: Only optional arguments can be excluded. Required arguments must be visible to the AI.

## Asynchronous Tools for Performance

FastMCP supports both sync and async tool functions.

### When to Use Async

Use `async def` for:

- I/O-bound operations (database queries, API calls)
- High-latency operations (network requests)
- Any operation that would block the event loop

### Example Async Tool

```python
import httpx

@mcp.tool()
async def fetch_weather(city: str) -> dict:
    """Fetch current weather for a city."""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.weather.com/{city}")
        return response.json()
```

### Performance Benefits

The framework handles running async tools concurrently, boosting throughput. In a real server, mix:

- **Synchronous tools** - For quick in-memory tasks
- **Asynchronous tools** - For network or disk operations

This maximizes performance without blocking.

### Streaming Responses

FastMCP v2.10+ supports streaming large responses in HTTP mode:

```python
@mcp.tool()
async def stream_large_data(query: str):
    """Stream results incrementally to avoid timeout."""
    for chunk in process_query_streaming(query):
        yield {"chunk": chunk, "progress": chunk.index}
```

CONSTRAINTS:

- The model must use HTTP transport for streaming (STDIO does not support streaming)
- The model must yield dict objects (not strings) for structured streaming
- The model must include progress indicators when streaming long operations

Use streaming for:

- Large file processing
- Database queries returning many rows
- Long-running computations with incremental results
- API responses exceeding context window limits

## Error Handling & Robustness

Proper error handling is baked into FastMCP.

### Automatic Error Handling

If a tool function raises any Python exception, FastMCP:

1. Intercepts the exception
2. Returns an MCP error response to the AI client
3. Allows the LLM to react (apologize, try different approach)

### Error Masking for Production

By default, exception details are included in error responses. For production, use `mask_error_details=True` to replace error traces with generic messages:

```python
mcp = FastMCP("my-server", mask_error_details=True)
```

This prevents leaking internal implementation details.

### ToolError for Business Logic Errors

Use `FastMCP.exceptions.ToolError` for expected errors that the AI should know about:

```python
from fastmcp.exceptions import ToolError

@mcp.tool()
def get_user(user_id: str) -> dict:
    user = database.find_user(user_id)
    if not user:
        raise ToolError(f"User {user_id} not found")
    return user
```

**Key behavior**: Messages from `ToolError` are **always sent to the client**, even if masking is enabled.

### Error Handling Pattern

Common pattern for production servers:

```python
@mcp.tool()
def process_order(order_id: str) -> dict:
    # Business logic errors - AI should see these
    if not order_id.startswith("ORD-"):
        raise ToolError("Invalid order ID format. Must start with 'ORD-'")

    order = database.get_order(order_id)
    if not order:
        raise ToolError(f"Order {order_id} not found")

    # Let unexpected exceptions bubble up as masked generic errors
    # (e.g., database connection failures)
    result = order.process()
    return {"status": "processed", "order": result}
```

This dual approach ensures:

- **User-friendly errors** for business logic issues
- **Security** by masking internal implementation errors

## Context and Annotations

### Context Parameter

For advanced use, tools can accept a `Context` parameter to access the runtime MCP context:

```python
from fastmcp import Context

@mcp.tool()
def long_operation(data: str, context: Context) -> dict:
    """Perform a long-running operation with progress updates."""
    context.info("Starting operation...")

    # Process data
    for i in range(10):
        context.info(f"Processing chunk {i+1}/10")
        process_chunk(data, i)

    context.info("Operation complete")
    return {"status": "success"}
```

Context object allows:

- **Logging** - Emit info/warning messages the client can display
- **Progress callbacks** - Update the AI on long-running operations
- **Reading resources** - Access other resources exposed by the server

### MCP Annotations

FastMCP supports MCP Annotations on tools - metadata not in the prompt but informing clients about tool behavior:

```python
@mcp.tool(
    annotations={
        "readOnlyHint": True,      # Tool only reads data, doesn't modify state
        "openWorldHint": False,    # Tool doesn't access external systems
        "destructiveHint": False,  # Tool doesn't delete/modify data
        "title": "Search Products" # Display name in UI
    }
)
def search_products(query: str) -> dict:
    # ...
```

### Annotation Usage

AI-centric IDEs like Cursor and Claude Desktop use these hints to:

- **Require user approval** for destructive actions
- **Label tools** nicely in their UI
- **Apply safety checks** based on annotations

**Always set annotations accurately** (flag tools that write to disk or call external APIs) so client applications can apply proper safety checks.

## Resources & Data Access

Besides tools (which perform actions), FastMCP lets you expose **Resources** - essentially read-only data endpoints.

### Basic Resource

```python
@mcp.resource("data://config")
def get_config() -> dict:
    """Provide server configuration data."""
    return {
        "api_version": "1.0",
        "max_requests_per_minute": 60,
        "supported_formats": ["json", "xml"]
    }
```

### Resource Characteristics

- **Fetched by clients** via `resources/read` call (not tool invocation)
- **Read-only** - For providing reference data, documents, or images to the AI
- **URI-based** - Use custom URI schemes like `data://`, `config://`, `file://`

### Parameterized Resource Templates

URI patterns with placeholders for dynamic content:

```python
@mcp.resource("user://{user_id}/profile")
def get_user_profile(user_id: str) -> dict:
    """Get user profile by ID."""
    user = database.get_user(user_id)
    return {
        "id": user_id,
        "name": user.name,
        "email": user.email,
        "preferences": user.preferences
    }
```

### When to Use Resources

Use resources for:

- **Large data** that doesn't fit in prompts
- **Frequently-needed reference data** (schemas, configs)
- **Dynamic content generation** (user profiles, reports)

This keeps interactions efficient and contextual.

## Transport & Deployment Choices

DECISION_TREE: Transport Selection

```text
1. IF single-user desktop integration (Claude Desktop, Cursor) THEN
   - Use STDIO transport
   - Client launches server as subprocess
   - Communication via stdin/stdout
   - GOTO setup_stdio

2. ELSE IF multi-user or remote access THEN
   - Use HTTP transport
   - Server runs as network service
   - Communication via HTTP endpoint
   - GOTO setup_http

3. ELSE IF production deployment THEN
   - Use HTTP with FastMCP Cloud OR custom deployment
   - GOTO production_deployment

setup_stdio:
  mcp.run()  # Defaults to STDIO

setup_http:
  mcp.run(transport="http", host="0.0.0.0", port=8000)

production_deployment:
  Option A: fastmcp deploy server.py  # FastMCP Cloud
  Option B: uvicorn app:app --host 0.0.0.0 --port 8080  # Custom
```

CONSTRAINTS:

- The model must use STDIO for Claude Desktop/Cursor integration
- The model must use HTTP for remote or multi-client scenarios
- The model must not use STDIO for network-accessible servers

### STDIO Transport (Default)

Calling `mcp.run()` with no arguments starts the server in **STDIO transport mode**:

```python
if __name__ == "__main__":
    mcp.run()  # Defaults to STDIO
```

#### STDIO Characteristics

- **Local integration** - Ideal for Claude Desktop or IDE plugins
- **Subprocess model** - AI client launches server as subprocess
- **Pipe communication** - Uses stdin/stdout for messages
- **Isolated sessions** - One server instance per client session
- **No networking** - Great for desktop apps or CLI tools

### HTTP Transport

For broader usage, run the server as a network service over HTTP:

```python
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
```

#### HTTP Characteristics

- **Network service** - Can handle multiple clients
- **Streamable protocol** - MCP's preferred network transport
- **Endpoint** - Accessible at `http://localhost:8000/mcp`
- **Bidirectional** - Full streaming and communication support
- **Remote/multi-user** - Suitable for cloud deployments

### Legacy Transports

There is also legacy SSE (Server-Sent Events) transport and WebSocket support via community add-ons, but HTTP has essentially replaced SSE in the latest MCP spec.

### Production Deployment

Treat an MCP server like any web service:

#### Containerization

- **Docker** - Containerize for consistent deployment
- **Process managers** - Use Uvicorn, Gunicorn, or supervisord
- **Cloud services** - Deploy to AWS, GCP, Azure, or serverless platforms

#### FastMCP Cloud

The FastAPI team launched **FastMCP Cloud** - a hosting platform for one-command deployment:

```bash
fastmcp deploy server.py
```

Features:

- Automatic HTTPS
- Built-in authentication
- Auto-scaling
- "Remote MCP that just works"

#### Manual HTTP Server

FastMCP's built-in CLI can launch a production-ready HTTP server:

```bash
fastmcp run server.py --transport http --port 8080 --log-level INFO
```

#### Custom Integration

For advanced use, embed FastMCP in a Starlette app:

```python
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse

async def health_check(request):
    return JSONResponse({"status": "healthy"})

async def mcp_handler(request):
    payload = await request.json()
    response = await mcp.handle_http(payload)
    return JSONResponse(response)

app = Starlette(routes=[
    Route("/health", health_check),
    Route("/mcp", mcp_handler, methods=["POST"])
])
```

### Production Best Practices

1. **Environment variables** - Secure secrets via env vars (FastMCP passes them through)
2. **Logging** - Enable appropriate log levels (`--log-level INFO`)
3. **Process supervision** - Use container orchestration or supervisord
4. **Health checks** - Add `/health` endpoints for monitoring
5. **Secret management** - Never hardcode API keys or credentials

### Example Production Configuration

```python
import os
from fastmcp import FastMCP

mcp = FastMCP(
    "production-server",
    mask_error_details=True  # Hide internal errors
)

# Read configuration from environment
API_KEY = os.getenv("API_KEY")
ALLOWED_DIRS = os.getenv("ALLOWED_DIRECTORIES", "").split(",")

@mcp.tool()
def secure_operation(
    query: str,
    api_key: Annotated[str, Field(exclude=True)] = API_KEY
) -> dict:
    # Use injected API key
    # ...
```

## Summary

FastMCP encourages a clean separation of concerns:

**You focus on**:

- Writing Python functions (tools/prompts/resources)
- Proper types, docs, and safety checks

**Framework handles**:

- Protocol details
- Validation
- Concurrency
- Transport layer

By following these guidelines - clear function schemas, thorough validation, async for heavy I/O, and careful error/permission handling - you set a strong foundation for a reliable, performant MCP server.
