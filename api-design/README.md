# API Design

> **v1.2.23** | Development | 26 iterations

Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, authentication, pagination, error handling, and federation.

## What Problem Does This Solve

API design decisions made early — URL structure, error formats, versioning strategy, pagination approach — are expensive to change once consumers depend on them. Without concrete patterns to follow, teams produce inconsistent endpoints, leaky error messages, missing rate limiting, and GraphQL schemas that trigger N+1 queries. This skill consolidates production-grade patterns across REST, GraphQL, gRPC, and Python library design into a single reference with ready-to-use templates, scripts, and checklists.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "How should I structure my REST API URLs and HTTP methods?" | URL naming conventions, HTTP method semantics, status code reference, and consistent error response envelope format |
| "My GraphQL API has terrible N+1 performance problems" | DataLoader batching patterns, complexity limits, caching strategies, and Apollo Federation for distributed schemas |
| "I need to add authentication to my FastAPI endpoints" | JWT, API key, and OAuth 2.0 flow patterns with FastAPI dependency injection examples and Pydantic schema templates |
| "How do I paginate a list endpoint — cursor vs offset?" | Cursor-based and offset-based pagination patterns with request/response examples and tradeoff guidance |
| "I need to version my API without breaking existing clients" | Versioning strategies reference covering URL versioning, header versioning, and deprecation workflows |
| "Can you scaffold a complete FastAPI CRUD endpoint?" | FastAPI router template, Pydantic schema template, repository pattern with tenant isolation, and rate limiter implementation |

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/api-design
```

## How to Use

**Direct invocation:**

```
Use the api-design skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `api`
- `rest`
- `graphql`
- `grpc`
- `openapi`

## What's Inside

- **Overview** -- Summary of the four combined domains: REST, GraphQL, gRPC, and Python library architecture
- **Quick Reference** -- URL patterns, HTTP methods, status codes, error envelope format, GraphQL schema example, FastAPI route and Pydantic schema patterns, pagination formats, and auth headers
- **Available Resources** -- Index of all references, templates, examples, scripts, assets, and checklists with one-line descriptions
- **Core Workflows** -- Step-by-step guides for designing a REST API, building a GraphQL API, setting up Apollo Federation, and validating API specifications with included scripts
- **Anti-Patterns to Avoid** -- Ten common mistakes (verb URLs, missing pagination, no idempotency keys, N+1 queries) with specific fixes
- **Quality Checklist** -- Pre-release checklist covering endpoints, error responses, pagination, auth, rate limiting, versioning, CORS, and OpenAPI validation

## Key Capabilities

- **REST API Design**
- **GraphQL Development**
- **gRPC Services**
- **Python Library Architecture**
- **Security & Performance**

## Version History

- `1.2.23` fix(docs+quality): optimize descriptions for api-design, docs, edge-cases, examples, navigation, standards (6e315cf)
- `1.2.22` fix(api-design): repair broken cross-references to legacy skill names (dd04729)
- `1.2.21` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.2.20` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.2.19` refactor: remove old file locations after plugin restructure (a26a802)
- `1.2.18` docs: update README and install commands to marketplace format (af9e39c)
- `1.2.17` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.2.16` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.2.15` fix: make all shell scripts executable and fix Python syntax errors (61ac964)
- `1.2.14` docs: add detailed README documentation for all 34 skills (7ba1274)

## Related Skills

- **[Debugging](../debugging/)** -- Comprehensive debugging skill combining systematic debugging methodology, browser DevTools automation, E2E testing with ...
- **[Frontend Design](../frontend-design/)** -- Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, acce...
- **[Gws Cli](../gws-cli/)** -- Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace A...
- **[Mcp Server](../mcp-server/)** -- Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Pyth...
- **[Nextjs Development](../nextjs-development/)** -- Comprehensive Next.js development skill covering App Router (13+/15/16), Server Components, Server Actions, Cache Compon...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
