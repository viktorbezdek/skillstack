# API Design

> **v1.2.23** | Development | 26 iterations

Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, authentication, pagination, error handling, and federation.

## What Problem Does This Solve

API design decisions made early -- URL structure, error format, versioning strategy, pagination approach -- are expensive to change once consumers depend on them. Without concrete patterns, teams produce inconsistent endpoints (verbs in URLs, mixed response envelopes), security gaps (missing rate limiting, leaking internal errors), and GraphQL schemas that trigger N+1 queries in production. Retrofitting these after clients are integrated means breaking changes or permanent technical debt.

This skill consolidates production-grade patterns across REST, GraphQL, gRPC, and Python library design into a single reference with ready-to-use templates, scripts for validation and scaffolding, and checklists for pre-release review. It covers the full surface from URL naming and HTTP semantics through OAuth flows, cursor pagination, Apollo Federation, and FastAPI implementation.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install api-design@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention API-related topics, or you can invoke it explicitly with `Use the api-design skill to ...`.

## What's Inside

This is a large single-skill plugin with references, examples, templates, scripts, assets, and checklists organized across five API domains:

### References (14 files)

| File | What It Covers |
|---|---|
| `rest-best-practices.md` | URL patterns, HTTP methods, status codes, response envelopes, filtering, sorting |
| `authentication.md` | OAuth 2.0 flows, JWT structure, API key patterns, MFA |
| `versioning-strategies.md` | URL versioning, header versioning, deprecation workflows |
| `common-patterns.md` | Health checks, webhooks, batch operations, idempotency keys |
| `schema-patterns.md` | GraphQL schema design, Relay connections, input/payload types |
| `federation-guide.md` | Apollo Federation architecture, entity resolution, subgraph design |
| `performance-optimization.md` | DataLoader batching, complexity limits, caching strategies |
| `architectural-principles.md` | Python library SOLID principles, package structure |
| `pep-standards.md` | Python PEP quick reference for library design |
| `fastapi-setup.md` | FastAPI main app configuration, middleware, lifespan |
| `openapi.md` | OpenAPI 3.1 customization and spec generation |
| `error-handlers.md` | FastAPI exception handler patterns |
| `cors-rate-limiting.md` | CORS configuration, per-user/per-endpoint rate limiting |

### Examples (5 files)

FastAPI CRUD endpoints, Pydantic validation schemas, pagination implementation (cursor + offset), API testing patterns, and TanStack Start server functions.

### Checklists (2 files)

API design review checklist (endpoints, errors, pagination, auth, rate limiting, versioning, CORS, OpenAPI validation) and security review checklist.

### Scripts (5 files)

GraphQL schema analyzer, TypeScript resolver generator, Apollo Federation subgraph scaffolder, OpenAPI validation and docs generator, and API spec validation shell script.

### Assets (7 files)

Python library templates: pyproject.toml, README, CONTRIBUTING guide, project structure, test organization, exception hierarchy pattern, and configuration pattern.

## Usage Scenarios

**1. "Design a REST API for a multi-tenant SaaS application."**
Start with the URL patterns (`/api/v1/organizations/{org_id}/teams` -- plural nouns, max 2 levels deep). Use the Pydantic schema template for request/response models with tenant isolation. Apply the repository pattern from the templates for database access scoped by tenant. Add cursor-based pagination on all list endpoints, JWT authentication via FastAPI dependency injection, and the standard error envelope format with request IDs.

**2. "My GraphQL API is slow -- I suspect N+1 queries."**
Load the performance optimization reference. Implement DataLoader for batching database calls within a single request. Add complexity limits to prevent expensive nested queries. Use the schema analyzer script to validate your schema against quality patterns. Consider Relay-style connections for paginated fields to give clients control over fetch depth.

**3. "Scaffold an Apollo Federation setup with user and post services."**
Run the federation scaffolder: `python scripts/federation_scaffolder.py users-service --entities User,Profile` then `python scripts/federation_scaffolder.py posts-service --entities Post --references User`. This generates subgraph boilerplate with entity resolution, then configure the gateway. The federation guide covers entity ownership, cross-subgraph references, and migration from monolithic schema.

**4. "Add authentication to my FastAPI endpoints."**
The authentication reference covers three approaches: JWT tokens for user-facing APIs (Authorization Code flow for web, PKCE for mobile/SPA), API keys for service-to-service (`X-API-Key` header with `sk_live_` prefix convention), and OAuth 2.0 Client Credentials for machine-to-machine. FastAPI dependency injection examples show how to extract and validate credentials per route.

**5. "Validate our OpenAPI spec before publishing."**
Run `python scripts/api_helper.py validate --spec openapi.yaml` for structural validation, then use the API design checklist to review: all endpoints use nouns not verbs, consistent response envelope, error responses include codes and actionable messages, pagination on all list endpoints, rate limit headers defined, CORS configured for known origins, idempotency keys for mutations.

## When to Use / When NOT to Use

**Use when:**
- Designing new REST, GraphQL, or gRPC API endpoints
- Writing OpenAPI/Swagger specifications
- Implementing authentication, pagination, rate limiting
- Setting up Apollo Federation across microservices
- Building Python library APIs with clean package structure
- Reviewing API designs before release

**Do NOT use when:**
- Building MCP (Model Context Protocol) servers -- use [mcp-server](../mcp-server/) instead
- Building the frontend that consumes the API -- use [react-development](../react-development/) or [nextjs-development](../nextjs-development/) instead

## Related Plugins

- **[Debugging](../debugging/)** -- Systematic debugging methodology including API debugging
- **[Frontend Design](../frontend-design/)** -- UI/UX design systems, component libraries, styling
- **[MCP Server](../mcp-server/)** -- MCP server development with Python and TypeScript SDKs
- **[Next.js Development](../nextjs-development/)** -- Next.js App Router, Server Components, Server Actions
- **[Testing Framework](../testing-framework/)** -- Test infrastructure for API integration testing

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
