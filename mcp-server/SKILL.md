---
name: mcp-server
description: Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Python (FastMCP) or TypeScript. Covers agent-centric design, tool creation, evaluation testing, production deployment, Claude Code integration, and plugin development. Use when building MCP servers, creating Claude Code plugins, integrating external APIs as tools, or configuring MCP for any AI application.
---

# MCP Server Development

## Overview

This is a comprehensive skill for developing Model Context Protocol (MCP) servers. MCP is a standardized protocol that enables AI agents (like Claude) to access external tools, data sources, and services through a unified interface.

This skill consolidates knowledge from multiple sources to provide complete coverage of:
- MCP protocol fundamentals and architecture
- Building MCP servers in Python (FastMCP) and TypeScript
- Agent-centric tool design principles
- Claude Code integration (plugins, skills, hooks)
- Production deployment and security patterns
- Evaluation-driven development
- Plugin packaging and distribution

## When to Use This Skill

Use this skill when:
- Building new MCP servers from scratch
- Integrating external APIs or services as MCP tools
- Creating Claude Code plugins
- Designing tools optimized for AI agent consumption
- Configuring MCP servers for Claude Desktop or other clients
- Writing evaluations to test MCP server quality
- Implementing security, caching, or production patterns
- Packaging plugins for distribution

## Quick Start

### Language Selection

**Choose Python (FastMCP) when:**
- Primary codebase is Python
- Integrating with data science/ML tooling
- Need rapid prototyping with minimal boilerplate
- Using FastAPI, Django, or Flask backends

**Choose TypeScript when:**
- Primary codebase is Node.js/TypeScript
- Building full-stack applications with shared types
- Require advanced type safety and IDE support
- Integrating with JavaScript ecosystem

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
    # OR: mcp.run(transport="http", port=8000)
```

### TypeScript Quick Start

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({
  name: "my-server",
  version: "1.0.0",
});

const SearchSchema = z.object({
  query: z.string(),
  limit: z.number().int().min(1).max(100).default(10),
}).strict();

server.registerTool("search_items", {
  title: "Search Items",
  description: "Search for items matching the query",
  inputSchema: SearchSchema,
  annotations: { readOnlyHint: true },
}, async (params) => {
  const results = await performSearch(params.query, params.limit);
  return {
    content: [{ type: "text", text: JSON.stringify({ results, count: results.length }, null, 2) }],
  };
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

| Transport | Use Case | Configuration |
|-----------|----------|---------------|
| **STDIO** | Local processes, Claude Desktop | Default, most common |
| **HTTP** | Remote services, REST APIs | Requires server setup |
| **SSE** | Real-time streaming updates | Event-driven applications |

### MCP Configuration

MCP servers are configured in `.claude/.mcp.json` (or `~/.claude/config.json` for global):

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

## Development Workflow

### Phase 1: Research and Planning

1. **Study Agent-Centric Design Principles**
   - Design tools for AI agents, not just API wrappers
   - Build workflow-oriented tools that enable complete tasks
   - Optimize for limited context windows
   - Provide actionable error messages

2. **Study API Documentation**
   - Read all available API documentation for target service
   - Document authentication, rate limiting, pagination patterns
   - Identify most valuable endpoints to implement

3. **Create Implementation Plan**
   - List tools to implement (prioritize high-value workflows)
   - Plan shared utilities and helpers
   - Design input validation (Pydantic/Zod schemas)
   - Define response formats (JSON, Markdown options)

### Phase 2: Implementation

**Key Patterns:**

- Use service-prefixed tool names: `github_search_repos`, `slack_send_message`
- Support both JSON and Markdown response formats
- Implement pagination with `limit`, `offset`, `has_more`
- Set CHARACTER_LIMIT constant (typically 25,000 tokens)
- Provide actionable, LLM-friendly error messages
- Use async/await for all I/O operations
- Full type coverage (Python type hints, TypeScript types)

**See Reference Files:**
- `references/development-guidelines.md` - FastMCP Python patterns
- `references/typescript-mcp-server.md` - TypeScript patterns
- `references/mcp-best-practices.md` - Universal guidelines

### Phase 3: Review and Testing

**Code Quality Checklist:**
- [ ] DRY Principle: No duplicated code between tools
- [ ] Composability: Shared logic extracted into functions
- [ ] Consistency: Similar operations return similar formats
- [ ] Error Handling: All external calls have error handling
- [ ] Type Safety: Full type coverage
- [ ] Documentation: Comprehensive docstrings/descriptions

**Important:** MCP servers are long-running processes. Never run directly - use:
- Evaluation harness (see Phase 4)
- tmux to keep outside main process
- `timeout 5s python server.py` for quick tests

### Phase 4: Create Evaluations

Evaluations test whether LLMs can effectively use your MCP server.

**Process:**
1. List available tools and understand capabilities
2. Use READ-ONLY operations to explore available data
3. Create 10 complex, realistic questions
4. Verify answers yourself

**Question Requirements:**
- Independent (not dependent on other questions)
- Read-only (only non-destructive operations)
- Complex (requiring multiple tool calls)
- Realistic (based on real use cases)
- Verifiable (single, clear answer)
- Stable (answer won't change over time)

**Run Evaluations:**
```bash
pip install -r scripts/evaluation/requirements.txt
export ANTHROPIC_API_KEY=your_api_key

python scripts/evaluation/evaluation.py \
  -t stdio \
  -c python \
  -a my_mcp_server.py \
  evaluation.xml
```

## Claude Code Integration

### Plugin Architecture

Claude Code plugins can combine multiple components:

| Component | When to Use |
|-----------|-------------|
| **MCP Server** | External tool/service integration, stateful operations |
| **Skill** | Procedural workflows, domain knowledge, multi-step processes |
| **Slash Command** | Quick actions, command shortcuts |
| **Combination** | Complex plugins needing multiple interaction patterns |

### Creating Plugins

**Initialize Plugin:**
```bash
python scripts/init_plugin.py <plugin-name> --type <mcp|skill|command|full>
```

**Validate Plugin:**
```bash
python scripts/validate_plugin.py <plugin-path>
```

**Package Plugin:**
```bash
python scripts/package_plugin.py <plugin-path> [output-dir]
```

### Plugin Templates

Templates are available in `templates/`:

- `mcp-server-python/` - Python FastMCP server
- `mcp-server-typescript/` - TypeScript MCP server
- `mcp-template-python/` - Alternative Python template with tests
- `mcp-template-typescript/` - Alternative TypeScript template
- `skill/` - Skill template with references and scripts
- `slash-command/` - Slash command template
- `full-plugin/` - Complete plugin combining all components

## Using MCP Tools

### Gemini CLI (Primary Method)

```bash
# CRITICAL: Use stdin piping, NOT -p flag
echo "Search GitHub for MCP servers" | gemini -y -m gemini-2.5-flash
```

### Direct Script Execution

```bash
npx tsx scripts/mcp-tools/cli.ts call-tool memory create_entities '{"entities":[...]}'
npx tsx scripts/mcp-tools/cli.ts list-tools
```

### Tool Discovery

```bash
# Saves to assets/tools.json for offline reference
npx tsx scripts/mcp-tools/cli.ts list-tools
```

## Reference Files

### Core MCP Development

| File | Purpose |
|------|---------|
| `references/mcp-best-practices.md` | Universal MCP guidelines |
| `references/development-guidelines.md` | FastMCP Python patterns |
| `references/typescript-mcp-server.md` | TypeScript implementation |
| `references/building-servers.md` | Complete server development guide |
| `references/protocol-basics.md` | MCP protocol fundamentals |

### Python Specific

| File | Purpose |
|------|---------|
| `references/python-guide.md` | Complete Python/FastMCP guide |
| `references/mcp-development.md` | FastMCP development patterns |

### TypeScript Specific

| File | Purpose |
|------|---------|
| `references/typescript-guide.md` | Complete TypeScript guide |
| `references/sdk-patterns.md` | SDK usage patterns and examples |

### Production and Operations

| File | Purpose |
|------|---------|
| `references/production-checklist.md` | Pre-deployment validation |
| `references/community-practices.md` | Mid-2025+ patterns, .mcpb packaging |
| `references/api-comparison.md` | LLM provider comparison |
| `references/evaluation-guide.md` | Creating effective evaluations |

### Claude Code Integration

| File | Purpose |
|------|---------|
| `references/mcp_server_guide.md` | MCP server guide for plugins |
| `references/skill_guide.md` | Skill creation guide |
| `references/slash_command_guide.md` | Slash command guide |
| `references/architecture_patterns.md` | Plugin architecture patterns |
| `references/best_practices.md` | Plugin best practices |

### Claude Code Official Documentation

Complete Claude Code documentation is in `references/claude-code-docs/`:
- `mcp.md` - MCP integration guide
- `plugins.md`, `plugins-reference.md` - Plugin development
- `skills.md` - Skill authoring
- `hooks.md`, `hooks-guide.md` - Hooks implementation
- `settings.md` - Configuration reference
- And 35+ more official documentation files

### Figma Integration (Specialized)

For Figma MCP server development, see `references/figma-integration/`:
- `figma-mcp-tools.md` - Figma MCP server tools
- `w3c-dtcg-spec.md` - Design tokens specification
- `token-naming-conventions.md` - Token naming patterns

## Scripts

### Plugin Development

| Script | Purpose |
|--------|---------|
| `scripts/init_plugin.py` | Initialize new plugin scaffolding |
| `scripts/validate_plugin.py` | Validate plugin structure and quality |
| `scripts/package_plugin.py` | Create distributable plugin package |

### MCP Tools

| Script | Purpose |
|--------|---------|
| `scripts/mcp-tools/cli.ts` | CLI for calling MCP tools |
| `scripts/mcp-tools/mcp-client.ts` | MCP client implementation |

### Evaluation

| Script | Purpose |
|--------|---------|
| `scripts/evaluation/evaluation.py` | Evaluation harness |
| `scripts/evaluation/connections.py` | MCP connection utilities |
| `scripts/evaluation/example_evaluation.xml` | Example evaluation file |

### Utilities

| Script | Purpose |
|--------|---------|
| `scripts/update_docs.js` | Update Claude Code documentation |
| `scripts/cost-calculator.py` | Calculate LLM API costs |

### Figma Token Scripts

| Script | Purpose |
|--------|---------|
| `scripts/figma-tokens/extract_tokens.py` | Extract tokens from Figma |
| `scripts/figma-tokens/transform_tokens.py` | Transform to CSS/SCSS/JSON |
| `scripts/figma-tokens/validate_tokens.py` | Validate W3C compliance |

## Templates

### MCP Server Templates

- `templates/mcp-server-python/` - Minimal Python FastMCP template
- `templates/mcp-server-typescript/` - Minimal TypeScript template
- `templates/mcp-template-python/` - Full Python template with tests
- `templates/mcp-template-typescript/` - Full TypeScript template

### Plugin Templates

- `templates/skill/` - Claude Code skill template
- `templates/slash-command/` - Slash command template
- `templates/full-plugin/` - Complete plugin template

### Design Token Templates

- `templates/figma-tokens/` - Design token output templates

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
- Use human-readable identifiers where appropriate

### Validation

- Python: Use Pydantic `Field()` with constraints
- TypeScript: Use Zod schemas with `.strict()`
- Validate all inputs against schema
- Sanitize file paths and external identifiers

### Error Handling

- Don't expose internal errors to clients
- Provide clear, actionable error messages
- Use ToolError (Python) for business logic errors
- Handle timeouts and rate limits gracefully

### Security

- Validate file paths against allowed directories
- Use confirmation flags for destructive operations
- Set `destructiveHint` annotation for state-changing tools
- Rate limit expensive operations
- Store secrets in environment variables

### Performance

- Use async for I/O-bound operations
- Cache repeated queries using lru_cache or similar
- Stream large responses in HTTP mode
- Extract common functionality into reusable functions

### Deployment

- Package as `.mcpb` for Claude Desktop distribution
- Provide `manifest.json` with user_config fields
- Support environment variable configuration
- Test with evaluation harness before release

## Boundaries

### This Skill Will:
- Guide MCP server development in Python or TypeScript
- Provide tool execution strategies via Gemini CLI or scripts
- Ensure best practices for agent-centric design
- Help create effective evaluations
- Configure multi-server setups
- Guide Claude Code plugin development

### This Skill Will Not:
- Run long-running server processes in main thread
- Skip input validation or error handling
- Create tools without comprehensive documentation
- Build servers without considering agent context limits
- Implement client-side MCP implementations

## Additional Resources

### Online Documentation

- MCP Specification: `https://modelcontextprotocol.io/llms-full.txt`
- FastMCP: `https://github.com/jlowin/fastmcp`
- Claude Code Docs: `https://docs.anthropic.com/claude-code`

### Updating Documentation

To fetch latest Claude Code documentation:
```bash
node scripts/update_docs.js
```


