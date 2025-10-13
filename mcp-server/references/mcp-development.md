# MCP Development Comprehensive Guide

Model Context Protocol (MCP) is an open standard for connecting AI assistants to external tools and data sources. This guide covers development with FastMCP (Python) and the TypeScript SDK.

## What is MCP?

### Core Concepts

**Model Context Protocol enables:**
- Standardized tool discovery and invocation
- Resource exposure (files, databases, APIs)
- Prompt templates for common workflows
- Lifecycle management (init, cleanup)
- Bidirectional communication

**MCP Architecture:**
```
┌─────────────────┐
│  Claude/Client  │
│   (MCP Client)  │
└────────┬────────┘
         │ stdio/HTTP
         │
┌────────▼────────┐
│   MCP Server    │
│  (Your Code)    │
└────────┬────────┘
         │
    ┌────▼────┬────────┬────────┐
    │ Tools   │ Resources│Prompts│
    └─────────┴──────────┴────────┘
```

### MCP vs Function Calling

**Use MCP when:**
- Building reusable tool packages
- Need multiple related capabilities
- Want standardized discovery
- Integrating with Claude Desktop/CLI
- Separating tool logic from application

**Use function calling when:**
- Simple, one-off integrations
- Using non-Claude models
- Need maximum control
- Integration is application-specific

**Key differences:**
| Feature | MCP | Function Calling |
|---------|-----|------------------|
| Discovery | Automatic | Manual |
| Lifecycle | Managed | Manual |
| Reusability | High | Low |
| Provider support | Claude-specific | Universal |
| Resources | Native | Manual |
| Prompts | Native | Manual |

## FastMCP (Python)

### Installation

```bash
pip install fastmcp
```

Or with development dependencies:

```bash
pip install "fastmcp[dev]"
```

### Quick Start

**Basic server (server.py):**

```python
from fastmcp import FastMCP

# Initialize server
mcp = FastMCP("My Server")

# Define a tool
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

# Define a resource
@mcp.resource("config://settings")
def get_settings() -> str:
    """Return server configuration."""
    return "Setting1: value1\nSetting2: value2"

# Define a prompt
@mcp.prompt()
def review_code(code: str) -> str:
    """Generate a prompt for code review."""
    return f"Review this code:\n\n{code}\n\nProvide feedback on:"
    " style, bugs, and improvements."

if __name__ == "__main__":
    mcp.run()
```

**Run the server:**

```bash
python server.py
```

### Tool Development

**Tool with validation:**

```python
from fastmcp import FastMCP
from pydantic import BaseModel, Field, validator

mcp = FastMCP("Database Server")

class QueryParams(BaseModel):
    table: str = Field(..., description="Table name to query")
    limit: int = Field(10, description="Max rows to return", ge=1, le=1000)

    @validator('table')
    def validate_table(cls, v):
        allowed = ['users', 'orders', 'products']
        if v not in allowed:
            raise ValueError(f"Table must be one of {allowed}")
        return v

@mcp.tool()
def query_table(params: QueryParams) -> list[dict]:
    """Query a database table with validation."""
    # Simulated query
    return [{"id": 1, "name": "Example"}]
```

**Async tool:**

```python
import httpx
from fastmcp import FastMCP

mcp = FastMCP("API Server")

@mcp.tool()
async def fetch_user(user_id: int) -> dict:
    """Fetch user data from API."""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.example.com/users/{user_id}")
        response.raise_for_status()
        return response.json()
```

**Tool with dependencies:**

```python
from fastmcp import FastMCP, Context
import psycopg2

mcp = FastMCP("PostgreSQL Server")

def get_db():
    """Database connection (injected dependency)."""
    conn = psycopg2.connect("dbname=mydb user=myuser")
    try:
        yield conn
    finally:
        conn.close()

@mcp.tool()
def run_query(query: str, ctx: Context) -> list[dict]:
    """Execute SQL query using dependency injection."""
    db = ctx.state.get("db")
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return [dict(row) for row in results]

# Initialize with state
mcp.state["db"] = get_db()
```

**Error handling:**

```python
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError

mcp = FastMCP("File Server")

@mcp.tool()
def read_file(path: str) -> str:
    """Read file with proper error handling."""
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise ToolError(f"File not found: {path}")
    except PermissionError:
        raise ToolError(f"Permission denied: {path}")
    except Exception as e:
        raise ToolError(f"Error reading file: {str(e)}")
```

### Resource Development

**Static resource:**

```python
@mcp.resource("config://app")
def app_config() -> str:
    """Return application configuration."""
    return """
    Database: postgresql://localhost/mydb
    Cache: redis://localhost:6379
    Environment: production
    """
```

**Dynamic resource with parameters:**

```python
@mcp.resource("user://{user_id}")
def user_profile(user_id: str) -> str:
    """Return user profile by ID."""
    # Fetch from database
    user = fetch_user_from_db(user_id)
    return f"Name: {user['name']}\nEmail: {user['email']}"
```

**File resource:**

```python
import os
from pathlib import Path

@mcp.resource("file://{path}")
def read_project_file(path: str) -> str:
    """Read a project file safely."""
    # Security: Ensure path is within project
    base = Path("/project/root")
    file_path = (base / path).resolve()

    if not file_path.is_relative_to(base):
        raise ToolError("Path outside project")

    return file_path.read_text()
```

**Database resource:**

```python
@mcp.resource("db://tables/{table}/schema")
def table_schema(table: str) -> str:
    """Return table schema."""
    cursor = db.cursor()
    cursor.execute(f"""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = %s
    """, (table,))

    schema = "\n".join(f"{row[0]}: {row[1]}" for row in cursor.fetchall())
    return f"Schema for {table}:\n{schema}"
```

### Prompt Development

**Simple prompt:**

```python
@mcp.prompt()
def summarize_text(text: str) -> str:
    """Generate a summarization prompt."""
    return f"""Please summarize the following text:

{text}

Provide a concise summary highlighting the main points."""
```

**Structured prompt:**

```python
from pydantic import BaseModel

class CodeReviewParams(BaseModel):
    code: str
    language: str
    focus_areas: list[str] = ["bugs", "style", "performance"]

@mcp.prompt()
def code_review(params: CodeReviewParams) -> str:
    """Generate code review prompt."""
    areas = ", ".join(params.focus_areas)
    return f"""Review this {params.language} code:

```{params.language}
{params.code}
```

Focus on: {areas}

Provide specific, actionable feedback."""
```

**Multi-step workflow prompt:**

```python
@mcp.prompt()
def data_analysis_workflow(dataset_path: str) -> str:
    """Generate comprehensive data analysis workflow."""
    return f"""Analyze the dataset at: {dataset_path}

Follow these steps:

1. Load the data and show basic statistics
2. Identify missing values and outliers
3. Perform correlation analysis
4. Generate visualizations for key relationships
5. Provide actionable insights

Use the query_table and plot_data tools as needed."""
```

### Server Configuration

**Environment configuration:**

```python
from fastmcp import FastMCP
import os
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP(
    name="Production Server",
    version="1.0.0",
    description="Production MCP server with auth"
)

# Configuration from environment
DATABASE_URL = os.getenv("DATABASE_URL")
API_KEY = os.getenv("API_KEY")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

mcp.state.update({
    "database_url": DATABASE_URL,
    "api_key": API_KEY,
    "debug": DEBUG
})
```

**Lifecycle hooks:**

```python
@mcp.on_startup()
async def startup():
    """Initialize resources on startup."""
    print("Server starting...")
    # Initialize database pool
    # Connect to external services
    # Load cache

@mcp.on_shutdown()
async def shutdown():
    """Cleanup on shutdown."""
    print("Server shutting down...")
    # Close database connections
    # Flush caches
    # Cleanup temp files
```

### Testing

**Unit testing tools:**

```python
import pytest
from fastmcp.testing import MCPClient

@pytest.mark.asyncio
async def test_add_numbers():
    """Test add_numbers tool."""
    client = MCPClient("server.py")

    result = await client.call_tool("add_numbers", {"a": 5, "b": 3})
    assert result == 8

@pytest.mark.asyncio
async def test_query_validation():
    """Test query parameter validation."""
    client = MCPClient("server.py")

    # Valid table
    result = await client.call_tool("query_table", {
        "table": "users",
        "limit": 10
    })
    assert isinstance(result, list)

    # Invalid table
    with pytest.raises(ValueError):
        await client.call_tool("query_table", {
            "table": "invalid_table",
            "limit": 10
        })
```

**Integration testing:**

```python
import pytest
from unittest.mock import patch

@pytest.mark.asyncio
async def test_fetch_user_integration():
    """Test user fetch with mocked API."""
    client = MCPClient("server.py")

    with patch('httpx.AsyncClient.get') as mock_get:
        mock_get.return_value.json.return_value = {
            "id": 1,
            "name": "Test User"
        }

        result = await client.call_tool("fetch_user", {"user_id": 1})
        assert result["name"] == "Test User"
        mock_get.assert_called_once()
```

## TypeScript MCP SDK

### Installation

```bash
npm install @modelcontextprotocol/sdk
```

Or with Yarn:

```bash
yarn add @modelcontextprotocol/sdk
```

### Quick Start

**Basic server (server.ts):**

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  Tool
} from "@modelcontextprotocol/sdk/types.js";

// Initialize server
const server = new Server(
  {
    name: "my-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
      resources: {},
      prompts: {}
    },
  }
);

// Define tools
const tools: Tool[] = [
  {
    name: "add_numbers",
    description: "Add two numbers together",
    inputSchema: {
      type: "object",
      properties: {
        a: { type: "number", description: "First number" },
        b: { type: "number", description: "Second number" }
      },
      required: ["a", "b"]
    }
  }
];

// List tools handler
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools
}));

// Call tool handler
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "add_numbers") {
    const { a, b } = args as { a: number; b: number };
    return {
      content: [
        {
          type: "text",
          text: String(a + b)
        }
      ]
    };
  }

  throw new Error(`Unknown tool: ${name}`);
});

// Start server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch(console.error);
```

### Tool Development

**Tool with validation:**

```typescript
import { z } from "zod";

// Define schema with Zod
const QueryParamsSchema = z.object({
  table: z.enum(["users", "orders", "products"]),
  limit: z.number().int().min(1).max(1000).default(10)
});

type QueryParams = z.infer<typeof QueryParamsSchema>;

// Tool definition
const queryTool: Tool = {
  name: "query_table",
  description: "Query a database table",
  inputSchema: {
    type: "object",
    properties: {
      table: {
        type: "string",
        enum: ["users", "orders", "products"],
        description: "Table to query"
      },
      limit: {
        type: "number",
        minimum: 1,
        maximum: 1000,
        default: 10,
        description: "Max rows"
      }
    },
    required: ["table"]
  }
};

// Handler with validation
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "query_table") {
    // Validate with Zod
    const params = QueryParamsSchema.parse(request.params.arguments);

    // Execute query
    const results = await db.query(params.table, params.limit);

    return {
      content: [
        {
          type: "text",
          text: JSON.stringify(results, null, 2)
        }
      ]
    };
  }
});
```

**Async tool with error handling:**

```typescript
import axios from "axios";

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "fetch_user") {
    try {
      const { user_id } = request.params.arguments as { user_id: number };

      const response = await axios.get(
        `https://api.example.com/users/${user_id}`
      );

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(response.data)
          }
        ]
      };
    } catch (error) {
      if (axios.isAxiosError(error)) {
        return {
          content: [
            {
              type: "text",
              text: `API Error: ${error.message}`
            }
          ],
          isError: true
        };
      }
      throw error;
    }
  }
});
```

### Resource Development

**Static resource:**

```typescript
import { ListResourcesRequestSchema, ReadResourceRequestSchema } from
"@modelcontextprotocol/sdk/types.js";

// List resources
server.setRequestHandler(ListResourcesRequestSchema, async () => ({
  resources: [
    {
      uri: "config://app",
      name: "Application Config",
      description: "Server configuration",
      mimeType: "text/plain"
    }
  ]
}));

// Read resource
server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const { uri } = request.params;

  if (uri === "config://app") {
    return {
      contents: [
        {
          uri,
          mimeType: "text/plain",
          text: "Database: postgresql://localhost/mydb\nCache: redis://localhost:6379"
        }
      ]
    };
  }

  throw new Error(`Unknown resource: ${uri}`);
});
```

**Dynamic resource:**

```typescript
// List with template
server.setRequestHandler(ListResourcesRequestSchema, async () => ({
  resources: [
    {
      uri: "user://{user_id}",
      name: "User Profile",
      description: "Get user by ID",
      mimeType: "application/json"
    }
  ]
}));

// Read with parameter extraction
server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const { uri } = request.params;

  const userMatch = uri.match(/^user:\/\/(\d+)$/);
  if (userMatch) {
    const userId = userMatch[1];
    const user = await fetchUser(userId);

    return {
      contents: [
        {
          uri,
          mimeType: "application/json",
          text: JSON.stringify(user)
        }
      ]
    };
  }

  throw new Error(`Unknown resource: ${uri}`);
});
```

### Prompt Development

**Simple prompt:**

```typescript
import { ListPromptsRequestSchema, GetPromptRequestSchema } from
"@modelcontextprotocol/sdk/types.js";

server.setRequestHandler(ListPromptsRequestSchema, async () => ({
  prompts: [
    {
      name: "summarize_text",
      description: "Summarize a text",
      arguments: [
        {
          name: "text",
          description: "Text to summarize",
          required: true
        }
      ]
    }
  ]
}));

server.setRequestHandler(GetPromptRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "summarize_text") {
    const { text } = args as { text: string };

    return {
      messages: [
        {
          role: "user",
          content: {
            type: "text",
            text: `Please summarize:\n\n${text}`
          }
        }
      ]
    };
  }

  throw new Error(`Unknown prompt: ${name}`);
});
```

### Testing

**Unit tests with Jest:**

```typescript
import { jest } from "@jest/globals";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";

describe("MCP Server", () => {
  let server: Server;

  beforeEach(() => {
    server = new Server({
      name: "test-server",
      version: "1.0.0"
    }, {
      capabilities: { tools: {} }
    });
  });

  it("should add numbers", async () => {
    const result = await server.callTool("add_numbers", {
      a: 5,
      b: 3
    });

    expect(result.content[0].text).toBe("8");
  });

  it("should validate input", async () => {
    await expect(
      server.callTool("query_table", {
        table: "invalid",
        limit: 10
      })
    ).rejects.toThrow();
  });
});
```

## Tool Design Best Practices

### Single Responsibility Principle

**Good:**
```python
@mcp.tool()
def create_user(name: str, email: str) -> dict:
    """Create a new user."""
    return db.insert_user(name, email)

@mcp.tool()
def update_user(user_id: int, name: str = None, email: str = None) -> dict:
    """Update existing user."""
    return db.update_user(user_id, name, email)
```

**Bad:**
```python
@mcp.tool()
def manage_user(action: str, user_id: int = None, name: str = None, email: str = None):
    """Create, update, or delete user (TOO MANY RESPONSIBILITIES)."""
    if action == "create":
        return db.insert_user(name, email)
    elif action == "update":
        return db.update_user(user_id, name, email)
    elif action == "delete":
        return db.delete_user(user_id)
```

### Clear Parameter Schemas

**Good:**
```python
class SearchParams(BaseModel):
    query: str = Field(..., description="Search query string", min_length=1)
    limit: int = Field(10, description="Maximum results", ge=1, le=100)
    offset: int = Field(0, description="Results offset for pagination", ge=0)
    sort_by: str = Field("relevance", description="Sort field: relevance, date, title")
```

**Bad:**
```python
def search(q: str, opts: dict):  # Vague, unvalidated
    """Search for items."""
    pass
```

### Descriptive Tool Names and Descriptions

**Good:**
```python
@mcp.tool()
def fetch_github_repository_info(owner: str, repo: str) -> dict:
    """
    Fetch detailed information about a GitHub repository.

    Returns repository metadata including:
    - Stars, forks, watchers
    - Primary language
    - Open issues count
    - Last update timestamp
    """
```

**Bad:**
```python
@mcp.tool()
def get_repo(o: str, r: str):  # Unclear what this does
    """Get repo."""
    pass
```

### Actionable Error Messages

**Good:**
```python
try:
    user = db.get_user(user_id)
except UserNotFoundError:
    raise ToolError(
        f"User {user_id} not found. "
        "Use list_users tool to see available users."
    )
except DatabaseConnectionError:
    raise ToolError(
        "Database connection failed. "
        "Check server status with check_database_health tool."
    )
```

**Bad:**
```python
try:
    user = db.get_user(user_id)
except Exception as e:
    raise ToolError("Error")  # Unhelpful
```

### Idempotent Operations

**Good:**
```python
@mcp.tool()
def create_directory(path: str) -> str:
    """Create directory (idempotent)."""
    os.makedirs(path, exist_ok=True)
    return f"Directory {path} ready"
```

**Bad:**
```python
@mcp.tool()
def create_directory(path: str) -> str:
    """Create directory."""
    os.makedirs(path)  # Fails if exists
    return f"Created {path}"
```

## Security Best Practices

### Input Validation

**Always validate and sanitize:**

```python
from pathlib import Path

@mcp.tool()
def read_file(path: str) -> str:
    """Read file with path validation."""
    # Define allowed directory
    base_dir = Path("/app/data")

    # Resolve and validate path
    file_path = (base_dir / path).resolve()

    # Ensure path is within base_dir
    if not file_path.is_relative_to(base_dir):
        raise ToolError("Access denied: Path outside allowed directory")

    # Check file exists
    if not file_path.is_file():
        raise ToolError(f"File not found: {path}")

    return file_path.read_text()
```

### SQL Injection Prevention

**Use parameterized queries:**

```python
# Good: Parameterized
@mcp.tool()
def find_users(name: str) -> list[dict]:
    """Find users by name (safe)."""
    cursor.execute(
        "SELECT * FROM users WHERE name = %s",
        (name,)
    )
    return cursor.fetchall()

# Bad: String interpolation
@mcp.tool()
def find_users_unsafe(name: str) -> list[dict]:
    """Find users by name (VULNERABLE)."""
    cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
    return cursor.fetchall()
```

### Authentication and Authorization

**Implement auth for sensitive tools:**

```python
from functools import wraps

def require_auth(func):
    """Decorator to require authentication."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = kwargs.get("api_key")
        if not validate_api_key(api_key):
            raise ToolError("Authentication required")
        return func(*args, **kwargs)
    return wrapper

@mcp.tool()
@require_auth
def delete_user(user_id: int, api_key: str) -> dict:
    """Delete user (requires auth)."""
    return db.delete_user(user_id)
```

### Principle of Least Privilege

**Read-only when possible:**

```python
# Read-only database connection
def get_readonly_db():
    return psycopg2.connect(
        "dbname=mydb user=readonly_user password=xxx"
    )

@mcp.tool()
def query_users(limit: int = 10) -> list[dict]:
    """Query users (read-only connection)."""
    db = get_readonly_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users LIMIT %s", (limit,))
    return cursor.fetchall()
```

### Secrets Management

**Environment variables, never hardcode:**

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Good: Environment variable
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY environment variable required")

# Bad: Hardcoded
API_KEY = "sk-1234567890abcdef"  # NEVER DO THIS
```

### Rate Limiting

**Prevent abuse:**

```python
from functools import lru_cache
import time

request_counts = {}
RATE_LIMIT = 100  # requests per minute

def check_rate_limit(user_id: str):
    """Check if user exceeded rate limit."""
    now = time.time()
    minute = int(now / 60)
    key = f"{user_id}:{minute}"

    count = request_counts.get(key, 0)
    if count >= RATE_LIMIT:
        raise ToolError("Rate limit exceeded. Try again later.")

    request_counts[key] = count + 1

@mcp.tool()
def expensive_operation(user_id: str, data: str) -> str:
    """Rate-limited expensive operation."""
    check_rate_limit(user_id)
    return process(data)
```

### PII Sanitization

**Remove sensitive data from outputs:**

```python
import re

def sanitize_pii(text: str) -> str:
    """Remove PII from text."""
    # Remove emails
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
                  '[EMAIL]', text)
    # Remove phone numbers
    text = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '[PHONE]', text)
    # Remove SSNs
    text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[SSN]', text)
    return text

@mcp.tool()
def process_document(content: str) -> str:
    """Process document with PII removal."""
    sanitized = sanitize_pii(content)
    return analyze(sanitized)
```

## Debugging and Testing

### Logging

**Structured logging:**

```python
import logging
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

@mcp.tool()
def query_database(query: str) -> list:
    """Query database with logging."""
    logger.info("Executing query", extra={
        "query": query,
        "timestamp": time.time()
    })

    try:
        result = db.execute(query)
        logger.info("Query successful", extra={
            "row_count": len(result)
        })
        return result
    except Exception as e:
        logger.error("Query failed", extra={
            "query": query,
            "error": str(e)
        }, exc_info=True)
        raise
```

### MCP Inspector

Use Claude Desktop's MCP inspector for debugging:

1. Open Claude Desktop
2. Settings → Developer → Enable MCP Inspector
3. View tool calls, parameters, responses
4. Check server logs and errors
5. Test tools interactively

### Testing Checklist

- [ ] Unit tests for each tool
- [ ] Validation tests (invalid inputs)
- [ ] Error handling tests
- [ ] Integration tests with dependencies
- [ ] Performance tests (latency, throughput)
- [ ] Security tests (injection, path traversal)
- [ ] Rate limit tests
- [ ] Idempotency tests

## Common Pitfalls

### Anti-Pattern: God Tools

**Bad:**
```python
@mcp.tool()
def database_operation(
    operation: str,  # "create", "read", "update", "delete", "query", "backup", etc.
    **kwargs
):
    """Do everything with database."""
    if operation == "create":
        # ...
    elif operation == "read":
        # ...
    # 500 lines later...
```

**Good:**
```python
@mcp.tool()
def create_record(table: str, data: dict) -> dict:
    """Create database record."""
    return db.insert(table, data)

@mcp.tool()
def query_records(table: str, filters: dict) -> list:
    """Query database records."""
    return db.query(table, filters)
```

### Anti-Pattern: State Dependencies

**Bad:**
```python
current_user = None

@mcp.tool()
def set_user(user_id: int):
    """Set current user (creates state dependency)."""
    global current_user
    current_user = user_id

@mcp.tool()
def get_user_data():
    """Get data for current user (depends on set_user being called first)."""
    return db.get_user(current_user)
```

**Good:**
```python
@mcp.tool()
def get_user_data(user_id: int) -> dict:
    """Get user data (stateless, independent)."""
    return db.get_user(user_id)
```

### Anti-Pattern: Silent Failures

**Bad:**
```python
@mcp.tool()
def process_file(path: str) -> str:
    """Process file."""
    try:
        return do_processing(path)
    except Exception:
        return "Error"  # What error? How to fix?
```

**Good:**
```python
@mcp.tool()
def process_file(path: str) -> str:
    """Process file with clear error reporting."""
    try:
        return do_processing(path)
    except FileNotFoundError:
        raise ToolError(f"File not found: {path}. Check path and try again.")
    except PermissionError:
        raise ToolError(f"Permission denied: {path}. Check file permissions.")
    except ProcessingError as e:
        raise ToolError(f"Processing failed: {e}. Verify file format.")
```

## Deployment

### Production Checklist

- [ ] Environment variables configured
- [ ] Logging configured (structured, appropriate level)
- [ ] Error handling comprehensive
- [ ] Input validation on all tools
- [ ] Security measures implemented (auth, rate limiting)
- [ ] Database connections pooled
- [ ] Graceful shutdown handlers
- [ ] Health check endpoint
- [ ] Monitoring and alerting configured
- [ ] Documentation complete
- [ ] Tests passing (unit, integration, security)

### Docker Deployment

**Dockerfile (FastMCP):**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .
COPY .env .

CMD ["python", "server.py"]
```

**Dockerfile (TypeScript):**

```dockerfile
FROM node:20-slim

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY dist/ ./dist/
COPY .env .

CMD ["node", "dist/server.js"]
```

### Claude Desktop Configuration

**Add to claude_desktop_config.json:**

```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {
        "DATABASE_URL": "postgresql://localhost/mydb",
        "API_KEY": "secret"
      }
    }
  }
}
```

## Resources

- MCP Specification: https://spec.modelcontextprotocol.io
- FastMCP Documentation: https://github.com/jlowin/fastmcp
- TypeScript SDK: https://github.com/modelcontextprotocol/typescript-sdk
- Claude MCP Documentation: https://docs.anthropic.com/mcp

**Last Updated:** January 2025
