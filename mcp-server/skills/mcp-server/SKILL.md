---
name: mcp-server
description: MCP (Model Context Protocol) server development — use when the user mentions MCP, Model Context Protocol, FastMCP, MCP server, MCP tool, Claude Code plugin, or building agent tools with MCP. Covers server implementation in Python or TypeScript, evaluation testing, production deployment, and plugin packaging. NOT for designing tool interfaces or tool consolidation patterns for agents (use tool-design), NOT for prompt engineering or prompt optimization (use prompt-engineering).
---

# MCP Server Development

## Overview

Comprehensive skill for developing Model Context Protocol (MCP) servers. MCP is a standardized protocol that enables AI agents (like Claude) to access external tools, data sources, and services through a unified interface.

Covers: MCP protocol fundamentals, building servers in Python (FastMCP) and TypeScript, agent-centric tool design, Claude Code integration (plugins, skills, hooks), production deployment, evaluation-driven development, and plugin packaging.

## When to Use

- Building new MCP servers from scratch
- Integrating external APIs or services as MCP tools
- Creating Claude Code plugins
- Designing tools optimized for AI agent consumption
- Configuring MCP servers for Claude Desktop or other clients
- Writing evaluations to test MCP server quality
- Implementing security, caching, or production patterns

## When NOT to Use

- Designing tool interfaces or consolidation patterns for agents (use tool-design)
- Prompt engineering or prompt optimization (use prompt-engineering)
- Building the actual business logic your tools wrap (that's application development)
- Debugging Claude's behavior when calling tools (that's a Claude usage issue)

## Decision Tree

```
What are you building?
│
├─ New MCP server
│  ├─ Python codebase or data/ML integration? → FastMCP (Python)
│  ├─ TypeScript/Node.js codebase? → @modelcontextprotocol/sdk (TypeScript)
│  └─ Need both? → Build in Python first, add TypeScript wrapper if needed
│
├─ Existing server needs improvement
│  ├─ Tools return inconsistent formats? → Add output schemas + CHARACTER_LIMIT
│  ├─ Tools fail on edge cases? → Add validation (Pydantic/Zod) + error handling
│  ├─ Context window overflow? → Optimize responses (paginate, truncate, summarize)
│  └─ Security concerns? → Add path validation, destructiveHint, confirmation flags
│
├─ Deploying to production
│  ├─ Local only? → STDIO transport
│  ├─ Remote service? → HTTP transport
│  └─ Real-time streaming needed? → SSE transport
│
└─ Not sure if MCP is the right approach
   ├─ Wrapping an API for Claude? → Yes, MCP server
   ├─ Building a full web application? → No, use Next.js/Python web framework
   └─ Just need Claude to read files? → No, Claude can do that natively
```

## Quick Start

### Language Selection

**Choose Python (FastMCP) when:** Primary codebase is Python, integrating with data science/ML, or need rapid prototyping.

**Choose TypeScript when:** Primary codebase is Node.js/TypeScript, building full-stack apps, or need advanced type safety.

### Python Quick Start (FastMCP)

```python
from fastmcp import FastMCP
from pydantic import Field
from typing import Annotated

mcp = FastMCP("my-server")

@mcp.tool()
def search_items(
    query: str,
    limit: Annotated[int, Field(ge=1, le=100)] = 10
) -> dict:
    """Search for items matching the query."""
    results = perform_search(query, limit)
    return {"results": results, "count": len(results)}

@mcp.resource("data://config")
def get_config() -> dict:
    return {"setting": "value"}

if __name__ == "__main__":
    mcp.run()  # STDIO transport (default)
```

### TypeScript Quick Start

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({ name: "my-server", version: "1.0.0" });

server.registerTool("search_items", {
  title: "Search Items",
  description: "Search for items matching the query",
  inputSchema: z.object({
    query: z.string(),
    limit: z.number().int().min(1).max(100).default(10),
  }).strict(),
  annotations: { readOnlyHint: true },
}, async (params) => {
  const results = await performSearch(params.query, params.limit);
  return { content: [{ type: "text", text: JSON.stringify({ results, count: results.length }, null, 2) }] };
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

## Core Concepts

### MCP Components

| Component | Purpose | Example |
|-----------|---------|---------|
| **Tools** | Executable functions for AI to call | `search_repos`, `create_issue` |
| **Resources** | Read-only data sources | `data://config`, `file://readme.md` |
| **Prompts** | Reusable prompt templates | `explain_code`, `summarize_document` |

### Transport Types

| Transport | Use Case |
|-----------|----------|
| **STDIO** | Local processes, Claude Desktop (default, most common) |
| **HTTP** | Remote services, REST APIs |
| **SSE** | Real-time streaming updates |

### MCP Configuration

```json
{
  "mcpServers": {
    "server-name": {
      "command": "python",
      "args": ["-m", "my_server"],
      "env": {"API_KEY": "***"}
    }
  }
}
```

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Wrapping REST endpoints 1:1 as tools | Tools mirror API structure, not agent workflows | Design workflow-oriented tools: `create_issue_with_labels` instead of `create_issue` + `add_labels` |
| No output format constraints | Responses bloat context window with irrelevant data | Enforce CHARACTER_LIMIT (25,000 chars) with truncation; return only what the agent needs |
| Missing input validation | Malformed inputs crash the server or produce garbage | Python: Pydantic `Field()` with constraints; TypeScript: Zod schemas with `.strict()` |
| Generic error messages | Agent cannot self-correct when tools fail | Return actionable errors: "Rate limit exceeded, retry after 60s" not "Error: 429" |
| Tools without annotations | Agent doesn't know if a tool is safe or destructive | Set `readOnlyHint`, `destructiveHint`, `idempotentHint` annotations appropriately |
| Unpaginated list operations | Large datasets overwhelm the context window | Implement pagination with `limit`/`offset` parameters |
| Storing secrets in tool parameters | API keys leak into conversation logs | Use environment variables; reference via `env` in MCP config |
| No response format standardization | Each tool returns data in a different structure | Support both JSON and Markdown; define consistent response schema per tool |

## Best Practices Summary

### Tool Design
- Design workflow-oriented tools, not API endpoint wrappers
- Use descriptive names with service prefix: `{service}_{action}_{resource}`
- Optimize for AI context window efficiency
- Provide actionable error messages

### Input/Output
- Support both JSON and Markdown response formats
- Implement pagination for list operations
- Enforce CHARACTER_LIMIT (typically 25,000) with truncation

### Validation
- Python: Use Pydantic `Field()` with constraints
- TypeScript: Use Zod schemas with `.strict()`
- Sanitize file paths and external identifiers

### Security
- Validate file paths against allowed directories
- Use confirmation flags for destructive operations
- Set `destructiveHint` annotation for state-changing tools
- Store secrets in environment variables

See [Extended Patterns](references/extended-patterns.md) for the full development workflow, Claude Code plugin integration, evaluation creation, complete reference file listings, and script documentation.

## Additional Resources

- MCP Specification: `https://modelcontextprotocol.io/llms-full.txt`
- FastMCP: `https://github.com/jlowin/fastmcp`
- Claude Code Docs: `https://docs.anthropic.com/claude-code`
