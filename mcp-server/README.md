# MCP Server Development

> Build, configure, and manage Model Context Protocol (MCP) servers using Python (FastMCP) or TypeScript for seamless AI agent integration.

## Overview

MCP (Model Context Protocol) is a standardized protocol that enables AI agents like Claude to access external tools, data sources, and services through a unified interface. This skill provides comprehensive guidance for developing MCP servers from scratch, covering the full lifecycle from design through production deployment.

Whether you are integrating external APIs as AI-consumable tools, building Claude Code plugins, or packaging complete plugin distributions, this skill walks you through agent-centric design principles, transport configuration, input validation, security hardening, and evaluation-driven testing. It supports both Python (via FastMCP) and TypeScript implementations.

As part of the SkillStack collection, MCP Server Development is the foundational skill for anyone building tooling that extends Claude's capabilities. It pairs naturally with skills that define workflows, personas, or domain knowledge that MCP tools can operationalize.

## What's Included

### References

- `accessing_online_resources.md` -- Patterns for fetching and caching external data
- `api-comparison.md` -- Side-by-side comparison of Python and TypeScript MCP APIs
- `architecture_patterns.md` -- Architectural patterns for MCP server design
- `best_practices.md` -- General best practices for MCP development
- `best-practices.md` -- Additional best practices reference
- `building-servers.md` -- Step-by-step guide to building MCP servers
- `community-practices.md` -- Community-sourced patterns and conventions
- `development-guidelines.md` -- Development workflow and coding standards
- `evaluation-guide.md` -- How to write evaluations for MCP server quality
- `example-projects.md` -- Catalog of example MCP server projects
- `extended-patterns.md` -- Detailed development workflow, Claude Code integration, and complete reference listings
- `mcp_server_guide.md` -- Comprehensive MCP server guide
- `mcp-best-practices.md` -- MCP-specific best practices
- `mcp-development.md` -- MCP development patterns
- `production-checklist.md` -- Production readiness checklist
- `prompts-and-templates.md` -- Reusable prompts and template patterns
- `protocol-basics.md` -- MCP protocol fundamentals
- `python-guide.md` -- Python/FastMCP-specific guidance
- `sdk-patterns.md` -- SDK usage patterns
- `skill_guide.md` -- Guide for building skills
- `slash_command_guide.md` -- Guide for building slash commands
- `typescript-guide.md` -- TypeScript-specific guidance
- `typescript-mcp-server.md` -- TypeScript MCP server reference
- `using-tools.md` -- Patterns for designing and using MCP tools
- `claude-code-docs/` -- Complete Claude Code documentation (40+ files covering plugins, hooks, settings, security, and more)
- `figma-integration/` -- Figma MCP integration guides (tools, tokens, troubleshooting, W3C DTCG spec)

### Templates

- `mcp-server-python/` -- Starter template for a Python MCP server with FastMCP
- `mcp-server-typescript/` -- Starter template for a TypeScript MCP server
- `mcp-template-python/` -- Alternative Python template with tests and .env support
- `mcp-template-typescript/` -- Alternative TypeScript template with .env support
- `full-plugin/` -- Complete plugin template combining MCP server, skill, and slash commands
- `skill/` -- Template for creating a new skill with references and scripts
- `slash-command/` -- Template for creating Claude Code slash commands
- `figma-tokens/` -- Templates for generating CSS, SCSS, TypeScript, and W3C token files from Figma

### Scripts

- `cost-calculator.py` -- Calculate MCP server hosting and usage costs
- `init_plugin.py` -- Initialize a new plugin project structure
- `package_plugin.py` -- Package a plugin for distribution
- `validate_plugin.py` -- Validate plugin structure and configuration
- `update_docs.js` -- Update documentation from source
- `evaluation/` -- Evaluation harness for testing MCP servers (connections, evaluation runner, example XML)
- `figma-tokens/` -- Extract, transform, and validate Figma design tokens
- `mcp-tools/` -- CLI tooling for analyzing and testing MCP servers (TypeScript)

### Assets

- `tools.json` -- MCP tool definitions and metadata

## Key Features

- Full Python (FastMCP) and TypeScript server development guidance
- Agent-centric tool design optimized for AI context windows
- Claude Code plugin creation, packaging, and distribution
- Evaluation-driven development with test harnesses
- Production deployment patterns including security, caching, and rate limiting
- Transport configuration for STDIO, HTTP, and SSE
- Input validation with Pydantic (Python) and Zod (TypeScript)
- Figma design token integration and transformation

## Usage Examples

**Create a new MCP server from scratch:**
```
Build a Python MCP server that wraps the GitHub API. Include tools for searching repos, creating issues, and listing pull requests. Use FastMCP with proper Pydantic validation.
```

**Build a Claude Code plugin:**
```
Create a complete Claude Code plugin for database management. It should include an MCP server with migration tools, a skill with schema design patterns, and slash commands for common operations.
```

**Add evaluation tests to an existing server:**
```
Write an evaluation suite for my MCP server. Test each tool with realistic inputs, verify response formats, and check error handling for edge cases.
```

**Set up Figma design token pipeline:**
```
Extract design tokens from our Figma file and transform them into CSS custom properties and TypeScript types using the figma-tokens scripts.
```

**Migrate a server to production:**
```
Review my MCP server against the production checklist. Add proper error handling, implement rate limiting, set up environment-based configuration, and add health checks.
```

## Quick Start

1. **Choose your language** -- Use Python (FastMCP) for data science/ML integration or rapid prototyping; use TypeScript for Node.js ecosystems or advanced type safety.

2. **Copy a template** -- Start from `templates/mcp-server-python/` or `templates/mcp-server-typescript/`.

3. **Define your tools** -- Create workflow-oriented tools with descriptive names following the `{service}_{action}_{resource}` convention.

4. **Add validation** -- Use Pydantic `Field()` constraints (Python) or Zod `.strict()` schemas (TypeScript) for all inputs.

5. **Test with evaluations** -- Use the evaluation harness in `scripts/evaluation/` to verify tool quality before deployment.

6. **Configure transport** -- Add your server to Claude Code or Claude Desktop via the `mcpServers` JSON configuration block.

## Related Skills

- **nextjs-development** -- Build full-stack applications that consume MCP tools
- **ontology-design** -- Design the knowledge models that MCP tools expose
- **outcome-orientation** -- Define measurable goals for your MCP server's impact

---

Part of [SkillStack](https://github.com/viktorbezdek/claude-skills) — `/plugin install mcp-server@claude-skills` -- 34 production-grade skills for Claude Code.
