---
name: mcp-server
description: Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Python (FastMCP) or TypeScript. Covers agent-centric design, tool creation, evaluation testing, production deployment, Claude Code integration, and plugin development.
triggers:
  - MCP
  - Model Context Protocol
  - FastMCP
  - Claude Code plugin
  - MCP server
  - MCP tool
  - agent tool
---

# MCP Server Development

## Overview

Comprehensive skill for developing Model Context Protocol (MCP) servers. MCP is a standardized protocol that enables AI agents (like Claude) to access external tools, data sources, and services through a unified interface.

Covers: MCP protocol fundamentals, building servers in Python (FastMCP) and TypeScript, agent-centric tool design, Claude Code integration (plugins, skills, hooks), production deployment, evaluation-driven development, and plugin packaging.

## When to Use This Skill

Use this skill when:
- Building new MCP servers from scratch
- Integrating external APIs or services as MCP tools
- Creating Claude Code plugins
- Designing tools optimized for AI agent consumption
- Configuring MCP servers for Claude Desktop or other clients
- Writing evaluations to test MCP server quality
- Implementing security, caching, or production patterns

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
      "env": {"API_KEY": "${ENV_VAR}"}
    }
  }
}
```

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
