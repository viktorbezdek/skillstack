# API Design

> **v1.2.23** | Development | 26 iterations

> Design production-grade APIs across REST, GraphQL, gRPC, and Python library architectures -- with templates, scripts, and checklists that ship working code, not just advice.

## The Problem

API design mistakes are expensive to fix after launch. You ship an endpoint with verb-based URLs (`/getUsers`) and inconsistent error responses, then discover you need to maintain it forever because clients depend on the broken contract. Pagination gets bolted on after launch when the list endpoint starts timing out at 50,000 records. Authentication is an afterthought, CORS is misconfigured for weeks while the frontend team works around it, and rate limiting does not exist until someone hammers your API with 10,000 requests per minute.

The knowledge exists -- REST conventions, GraphQL best practices, gRPC patterns, OpenAPI specifications -- but it is scattered across documentation sites, blog posts, and tribal knowledge. Engineers re-learn the same lessons project after project: use nouns not verbs, return 201 with a Location header for POST, implement cursor-based pagination from day one, never leak internal error details in production responses. Each lesson learned the hard way costs hours or days.

Even experienced engineers struggle when crossing paradigm boundaries. A REST expert designing their first GraphQL schema does not know about Relay connection patterns, DataLoader for N+1 prevention, or query complexity limits. A Python developer building their first public API does not know the 18 reference files worth of security, versioning, and federation patterns that production APIs require.

## The Solution

This plugin puts the full API design toolkit into every Claude Code session: REST resource design with HTTP semantics, GraphQL schema patterns with federation support, gRPC service definitions, Python library architecture with SOLID principles, authentication flows (OAuth 2.0, JWT, API keys), pagination (cursor-based and offset), rate limiting, CORS, error handling, and versioning strategies.

It ships six code templates (FastAPI CRUD endpoint, Pydantic schemas, repository pattern, rate limiter, error handler, TanStack server functions), five runnable scripts (schema analyzer, resolver generator, federation scaffolder, API helper, spec validator), seven worked examples, two review checklists (API design and security), and 18 reference documents covering every production concern from OpenAPI specs to gRPC Protocol Buffers.

You describe what you are building -- "a REST API for a bookstore" or "GraphQL schema for a multi-tenant SaaS" -- and get production-ready patterns with the right HTTP status codes, consistent error envelopes, proper pagination, authentication, and rate limiting. The templates generate working code, not pseudocode. The checklists catch the issues that would otherwise surface in production.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Verb-based URLs (`/getUsers`) and inconsistent conventions across endpoints | Resource-oriented URLs with consistent REST semantics from the start |
| Pagination bolted on after the list endpoint times out in production | Cursor-based or offset pagination designed into every list endpoint from day one |
| Error responses that leak stack traces or return inconsistent formats | Structured error envelope with codes, messages, field-level details, and request IDs |
| First GraphQL schema with N+1 query problems and no pagination | Relay connection patterns, DataLoader batching, and complexity limits built in |
| Authentication implemented differently per endpoint | Consistent OAuth 2.0 / JWT / API key patterns with documented flows |
| Manual spec writing that drifts from implementation | OpenAPI/Swagger templates and validation scripts that catch spec errors |

## Installation

Add the SkillStack marketplace, then install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install api-design@skillstack
```

### Verify Installation

After installing, test with:

```
Design a REST API for a task management application with users, projects, and tasks
```

The skill activates automatically when you mention API design topics.

## Quick Start

1. Install the plugin using the commands above.
2. Describe your API:
   ```
   I need a REST API for an e-commerce platform with products, orders, and customers -- design the endpoints and schemas
   ```
3. The skill produces resource URLs, HTTP method mappings, request/response schemas, pagination patterns, and error handling -- all following REST conventions.
4. Generate the implementation:
   ```
   Generate the FastAPI endpoints and Pydantic schemas for the products resource
   ```
5. The templates produce working FastAPI code with CRUD operations, repository pattern, and proper status codes.

## What's Inside

This is a comprehensive single-skill plugin with 18 references, 6 templates, 7 examples, 5 scripts, 2 checklists, and 7 assets.

| Component | Purpose |
|---|---|
| **api-design** skill | Core methodology: REST resource design, HTTP semantics, GraphQL schema patterns, gRPC services, pagination, authentication, error handling, rate limiting, versioning, anti-patterns, quality checklist |
| **18 reference documents** | Deep coverage of every API concern (see table below) |
| **6 code templates** | Production-ready FastAPI, Pydantic, rate limiter, error handler, repository pattern, TanStack server functions |
| **7 examples** | Worked implementations: CRUD, schemas, pagination, testing, TanStack, OpenAPI spec, GraphQL schema |
| **5 scripts** | Runnable tooling: schema analyzer, resolver generator, federation scaffolder, API helper, spec validator |
| **2 checklists** | API design review and security review |
| **7 assets** | Python library scaffolding: pyproject.toml, README, CONTRIBUTING, project structure, exceptions, configuration |

**Eval coverage:** 13 trigger eval cases + 3 output eval cases.

### How to Use: api-design

**What it does:** Guides you through designing and implementing APIs across REST, GraphQL, gRPC, and Python library architectures. Activates when you are designing endpoints, writing schemas, implementing authentication, setting up pagination, configuring rate limiting, writing OpenAPI specs, or reviewing API designs. Ships templates that generate working code and scripts that validate specifications.

**Try these prompts:**

```
Design a REST API for a multi-tenant SaaS project management tool -- I need endpoints for workspaces, projects, tasks, and team members
```

```
Review my API design -- I'm not sure about the pagination approach and whether my error responses are consistent enough
```

```
I need to add GraphQL federation to split our monolith API into user-service and order-service subgraphs
```

```
Generate a complete OpenAPI 3.1 spec for our inventory API with authentication, rate limiting, and proper error schemas
```

```
What's the right authentication pattern for a public API that needs both user tokens and service-to-service auth?
```

**Key references:**

| Reference | Topic |
|---|---|
| `rest-best-practices.md` | REST patterns, HTTP methods, status codes, resource naming |
| `authentication.md` | OAuth 2.0 flows, JWT patterns, API keys, MFA |
| `versioning-strategies.md` | API versioning and deprecation strategies |
| `common-patterns.md` | Health checks, webhooks, batch operations, idempotency |
| `schema-patterns.md` | GraphQL schema design patterns |
| `federation-guide.md` | Apollo Federation architecture and entity references |
| `performance-optimization.md` | DataLoader, caching, query complexity limits |
| `architectural-principles.md` | SOLID principles for Python library APIs |
| `pep-standards.md` | Python PEP quick reference for API code |
| `fastapi-setup.md` | FastAPI application configuration |
| `openapi.md` | OpenAPI specification customization |
| `error-handlers.md` | FastAPI exception handlers |
| `cors-rate-limiting.md` | CORS and rate limiting configuration |
| `openapi-spec.yaml` | Complete OpenAPI 3.1 example specification |
| `graphql-schema.graphql` | GraphQL schema with Relay connections |
| `grpc-service.proto` | Protocol Buffer service definitions |
| `rate-limiting.yaml` | Tier-based rate limit configuration |
| `api-security.yaml` | Auth, CORS, and security header configuration |

**Shipped templates:**

| Template | What it generates |
|---|---|
| `fastapi-crud-endpoint.py` | Complete CRUD router with dependency injection |
| `pydantic-schemas.py` | Request/response validation schemas |
| `repository-pattern.py` | Repository with tenant isolation |
| `rate-limiter.py` | Upstash Redis rate limiter |
| `error-handler.py` | FastAPI exception handlers |
| `tanstack-server-function.ts` | TanStack Start server functions |

**Shipped scripts:**

| Script | What it does |
|---|---|
| `schema_analyzer.py` | Analyzes GraphQL schemas for quality issues |
| `resolver_generator.py` | Generates TypeScript resolvers from schema |
| `federation_scaffolder.py` | Scaffolds Apollo Federation subgraphs |
| `api_helper.py` | Validates OpenAPI specs and generates docs |
| `validate-api-spec.sh` | Shell script for API specification validation |

## Real-World Walkthrough

You are building the backend for a B2B SaaS application that manages customer feedback. The product has three core resources -- organizations (multi-tenant), feedback items, and tags -- and needs to support both a web dashboard and a public API for integrations.

You start with the resource design:

```
Design a REST API for a multi-tenant customer feedback platform -- organizations own feedback items, which can be tagged and have status workflows
```

The skill produces the resource hierarchy: `/api/v1/organizations/{org_id}/feedback` for feedback items scoped to an organization, `/api/v1/organizations/{org_id}/tags` for organization-specific tags. It enforces the conventions: plural nouns, max two levels of nesting, lowercase with hyphens. Each resource gets the full HTTP method mapping -- GET (list with pagination), GET by ID, POST (returns 201 with Location header), PATCH (partial update), DELETE (returns 204).

The error response format uses a structured envelope with error code, human-readable message, field-level validation details, request ID for tracing, and timestamp. This format is consistent across every endpoint, so API consumers write one error handler.

Next, you need the implementation:

```
Generate the FastAPI endpoints and Pydantic schemas for the feedback resource -- it needs cursor-based pagination and tenant isolation
```

The skill pulls from the FastAPI CRUD template and repository pattern template. You get a complete router with `create_feedback`, `get_feedback`, `list_feedback` (with cursor-based pagination), `update_feedback`, and `delete_feedback`. The Pydantic schemas enforce validation: `FeedbackCreate` requires a title (1-500 chars) and description, `FeedbackRead` exposes only public fields with `from_attributes=True` for ORM compatibility. The repository pattern handles tenant isolation -- every query is scoped to `current_user.tenant_id`.

The pagination implementation uses cursor-based pagination by default (the skill recommends this over offset for production APIs). The response includes `nextCursor` and `hasMore` fields. You ask about the trade-offs:

```
When should I use offset pagination instead of cursor-based? Some of our internal tools need page numbers.
```

The skill explains: cursor-based is more performant and consistent (no skipped/duplicated items when data changes), but offset gives you page numbers and total counts that admin dashboards often need. For the public API, stick with cursor. For internal admin endpoints, offset is acceptable. Both patterns are in the pagination example file.

Now authentication. The public API needs API keys for integrations, but the web dashboard uses OAuth:

```
Set up authentication -- API keys for the public integration API and OAuth 2.0 with JWT for the web dashboard
```

The skill references `authentication.md` and produces the dual authentication setup: API keys validated via middleware with the `X-API-Key` header pattern, OAuth 2.0 Authorization Code flow with PKCE for the SPA dashboard, and JWT tokens with appropriate claims (user ID, tenant ID, roles). The FastAPI dependency injection handles both auth methods transparently -- endpoints accept either authentication type through a unified `get_current_user` dependency.

Rate limiting comes next. You use the rate limiter template with tier-based configuration: free-tier organizations get 100 requests/minute, paid get 1,000, enterprise gets 10,000. The `X-RateLimit-*` headers and `429 Too Many Requests` response follow the conventions in `rate-limiting.yaml`.

Before shipping, you run the API design checklist: all endpoints use nouns, consistent response envelopes, error responses include codes and actionable messages, pagination on all list endpoints, authentication documented, rate limit headers defined, versioning strategy documented, CORS configured for known origins, idempotency keys for mutations. You also run the security review checklist from `security-review.md`.

The OpenAPI spec is generated and validated with the shipped `api_helper.py` script. Client SDK generation from the spec produces TypeScript and Python clients that your integration partners can use immediately.

Total development time for the full API: two days instead of the week it would have taken designing each pattern from scratch. The API launches with consistent conventions, proper security, pagination that scales, and a validated specification that generates client libraries.

## Usage Scenarios

### Scenario 1: Designing a REST API from scratch

**Context:** You are starting a new microservice and need to design the API before implementation. The service manages user subscriptions with plans, billing, and usage tracking.

**You say:** "Design a REST API for a subscription management service -- plans, subscriptions, invoices, and usage metering"

**The skill provides:**
- Resource hierarchy with proper nesting (`/plans`, `/subscriptions/{id}/invoices`)
- HTTP method mapping with correct status codes for each operation
- Request/response schemas with validation rules
- Cursor-based pagination for list endpoints
- Webhook design for subscription lifecycle events (created, renewed, cancelled)
- Idempotency key pattern for payment-related mutations

**You end up with:** A complete API design document with URLs, methods, schemas, and an OpenAPI specification ready for implementation and client SDK generation.

### Scenario 2: Adding GraphQL federation to a monolith

**Context:** Your monolithic GraphQL API is becoming unwieldy. You want to split it into federated subgraphs by domain without breaking existing clients.

**You say:** "I need to split our monolith GraphQL API into federated subgraphs -- we have users, products, and orders that reference each other"

**The skill provides:**
- Federation architecture with entity references between subgraphs
- Entity key definitions and reference resolver patterns
- Gateway configuration for composing subgraphs
- Federation scaffolder script to generate subgraph boilerplate
- Migration strategy from monolith to federation without client-side changes

**You end up with:** Scaffolded subgraph projects with proper entity references, a gateway configuration, and a migration plan that preserves backward compatibility.

### Scenario 3: Reviewing and hardening an existing API

**Context:** Your API is in production but was built quickly without following conventions. You are getting bug reports about inconsistent error responses and missing pagination.

**You say:** "Review our API -- error responses are inconsistent, some endpoints return arrays instead of paginated results, and we have no rate limiting"

**The skill provides:**
- API design checklist audit identifying specific violations
- Consistent error envelope format with migration path
- Pagination retrofit strategy (adding cursor pagination without breaking existing clients)
- Rate limiting configuration with tier-based limits
- Versioning strategy for making breaking changes safely

**You end up with:** A prioritized list of fixes with implementation patterns for each, plus a versioning plan for changes that cannot be made backward-compatibly.

### Scenario 4: Building a Python library with a clean public API

**Context:** You are packaging internal code as a public Python library and need to design the API surface to be intuitive, well-documented, and maintainable.

**You say:** "I'm turning our internal data processing code into a public Python library -- help me design the public API following best practices"

**The skill provides:**
- Package structure template with clear public/private separation
- SOLID principles applied to library API design
- Exception hierarchy pattern for the library
- Configuration pattern for flexible initialization
- pyproject.toml template with proper metadata, dependencies, and entry points
- README and CONTRIBUTING templates

**You end up with:** A production-ready Python library scaffold with clean public API, proper exception handling, configuration management, and complete project metadata.

## Ideal For

- **Teams shipping their first production API** -- the design patterns, status codes, and error conventions prevent the mistakes you would learn from in year two
- **Backend engineers crossing paradigm boundaries** -- REST expert building first GraphQL schema gets Relay connections, DataLoader, and complexity limits from day one
- **Organizations standardizing API conventions** -- the checklists and reference documents serve as a living style guide for API design reviews
- **Developers needing working code fast** -- six templates generate production-ready FastAPI, Pydantic, and TypeScript code, not pseudocode
- **Teams maintaining public APIs** -- versioning strategies, deprecation patterns, and SDK generation from OpenAPI specs reduce maintenance burden

## Not For

- **Building MCP (Model Context Protocol) servers** -- use [mcp-server](../mcp-server/) for MCP-specific tool definitions and server patterns
- **Designing agent tool schemas for LLM consumption** -- use [tool-design](../tool-design/) for tool description optimization and parameter design
- **Frontend-only development without API concerns** -- use [react-development](../react-development/) or [nextjs-development](../nextjs-development/) for client-side patterns

## How It Works Under the Hood

The plugin is a single skill with progressive disclosure through a deep resource tree.

The **SKILL.md** body provides the quick reference: REST resource design with URL patterns and HTTP methods, status code tables, error response format, GraphQL schema patterns, FastAPI route patterns, Pydantic schema patterns, pagination (cursor and offset), authentication patterns (JWT, API keys, OAuth flows), rate limiting headers, and anti-patterns to avoid. This covers the most common design decisions without needing the references.

When deeper detail is needed, Claude draws from the 18 reference documents organized by concern area:

- **REST references** (`rest-best-practices.md`, `common-patterns.md`, `versioning-strategies.md`) provide comprehensive REST conventions, webhook patterns, batch operations, and deprecation strategies
- **GraphQL references** (`schema-patterns.md`, `federation-guide.md`, `performance-optimization.md`, `graphql-schema.graphql`) cover schema design, Apollo Federation, DataLoader, caching, and query complexity
- **Security references** (`authentication.md`, `cors-rate-limiting.md`, `api-security.yaml`, `rate-limiting.yaml`) handle OAuth flows, JWT patterns, CORS configuration, and tier-based rate limiting
- **Implementation references** (`fastapi-setup.md`, `openapi.md`, `error-handlers.md`, `openapi-spec.yaml`, `grpc-service.proto`) provide framework-specific configuration and specification examples
- **Python references** (`architectural-principles.md`, `pep-standards.md`) apply SOLID principles and PEP conventions to library API design

The templates, scripts, and examples are invoked when you need working code: templates generate implementation starters, scripts validate and analyze specifications, and examples demonstrate complete patterns.

## Related Plugins

- **[Code Review](../code-review/)** -- Multi-agent swarm review covering security, performance, and style for API implementation code
- **[Testing Framework](../testing-framework/)** -- Test infrastructure and strategy for API endpoint testing
- **[CI/CD Pipelines](../cicd-pipelines/)** -- Pipeline design for deploying and monitoring APIs
- **[Docker Containerization](../docker-containerization/)** -- Container patterns for API service deployment

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
