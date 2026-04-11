# MCP Server

> **v1.2.20** | Development | 23 iterations

Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Python (FastMCP) or TypeScript. Covers agent-centric design, tool creation, evaluation testing, production deployment, Claude Code integration, and plugin development.

## What Problem Does This Solve

Integrating external APIs or services with AI agents requires bridging two worlds: structured APIs designed for human developers and tool interfaces optimized for AI consumption. Without a standard protocol, every integration is a custom build. MCP (Model Context Protocol) provides that standard, and this skill covers everything needed to build production-grade MCP servers — from the first tool definition to evaluation harnesses, security patterns, and Claude Code plugin packaging.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "I need to expose my API to Claude as tools" | Agent-centric tool design patterns, naming conventions, and input/output formatting for AI consumption |
| "How do I build an MCP server in Python?" | FastMCP quick start with Pydantic validation, resource definitions, and STDIO/HTTP transport setup |
| "How do I build an MCP server in TypeScript?" | McpServer SDK setup with Zod schemas, tool registration, and transport configuration |
| "I want Claude Code to use my internal tooling" | Claude Code plugin packaging, `.claude/settings.json` configuration, and skill bundling |
| "How do I test my MCP server?" | Evaluation-driven development workflow and quality testing patterns |
| "My MCP tool handles file paths — what are the security risks?" | Path validation, allowed-directory enforcement, destructive operation confirmation flags, and secret management |

## When NOT to Use This Skill

- designing tool interfaces or tool consolidation patterns for agents -- use [tool-design](../tool-design/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install mcp-server@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the mcp-server skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `mcp`
- `model-context-protocol`
- `fastmcp`
- `typescript`

## What's Inside

- **Overview** -- High-level description of MCP and what this skill covers across Python, TypeScript, and production deployment
- **When to Use This Skill** -- Decision guide for when MCP server development applies vs adjacent skills
- **Quick Start** -- Minimal working server examples for both FastMCP (Python) and the TypeScript MCP SDK
- **Core Concepts** -- Reference table covering Tools, Resources, and Prompts components plus transport type selection (STDIO, HTTP, SSE)
- **Best Practices Summary** -- Condensed rules for tool design, input/output formatting, validation, and security patterns
- **Additional Resources** -- Links to the MCP specification, FastMCP repo, and Claude Code docs

## Version History

- `1.2.20` fix(languages+tools): optimize descriptions for git-workflow, mcp-server, python, typescript (b65bc7d)
- `1.2.19` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.2.18` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.2.17` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.2.16` refactor: remove old file locations after plugin restructure (a26a802)
- `1.2.15` docs: update README and install commands to marketplace format (af9e39c)
- `1.2.14` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.2.13` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.2.12` fix(deps): update all dependencies to latest versions (e72fc10)
- `1.2.11` fix(deps): address all 6 Dependabot security vulnerabilities (c031429)

## Related Skills

- **[Api Design](../api-design/)** -- Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, aut...
- **[Debugging](../debugging/)** -- Comprehensive debugging skill combining systematic debugging methodology, browser DevTools automation, E2E testing with ...
- **[Frontend Design](../frontend-design/)** -- Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, acce...
- **[Gws Cli](../gws-cli/)** -- Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace A...
- **[Nextjs Development](../nextjs-development/)** -- Comprehensive Next.js development skill covering App Router (13+/15/16), Server Components, Server Actions, Cache Compon...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
