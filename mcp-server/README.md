# MCP Server

> **v1.2.20** | Development | 23 iterations

Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Python (FastMCP) or TypeScript. Covers agent-centric design, tool creation, evaluation testing, production deployment, Claude Code integration, and plugin development.

## What Problem Does This Solve

Comprehensive skill for developing Model Context Protocol (MCP) servers. MCP is a standardized protocol that enables AI agents (like Claude) to access external tools, data sources, and services through a unified interface.

## When to Use This Skill

MCP (Model Context Protocol) server development — use when the user mentions MCP, Model Context Protocol, FastMCP, MCP server, MCP tool, Claude Code plugin, or building agent tools with MCP. Covers server implementation in Python or TypeScript, evaluation testing, production deployment, and plugin packaging.

## When NOT to Use This Skill

- designing tool interfaces or tool consolidation patterns for agents -- use [tool-design](../tool-design/) instead

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

- **Overview**
- **When to Use This Skill**
- **Quick Start**
- **Core Concepts**
- **Best Practices Summary**
- **Additional Resources**

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

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 48 production-grade plugins for Claude Code.
