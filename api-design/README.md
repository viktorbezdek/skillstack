# API Design

> **v1.2.23** | Comprehensive API design for REST, GraphQL, gRPC, and Python library architectures -- endpoints, schemas, authentication, pagination, error handling, federation, and security.
> 1 skill | 18 references | 7 templates | 8 examples | 5 scripts | 7 assets | 2 checklists | 13 trigger evals, 3 output evals

## The Problem

API design failures are expensive because they are hard to fix after launch. A poorly named endpoint becomes a permanent contract once external consumers depend on it. Inconsistent error response formats mean every client team writes bespoke error handling. Missing pagination on a list endpoint works fine with 50 records in development and causes outages with 50,000 in production. These are not obscure edge cases -- they are the same mistakes repeated across thousands of APIs because teams design ad hoc instead of following established patterns.

The problem multiplies across API paradigms. A team building a REST API may also need GraphQL for mobile clients and gRPC for internal services. Each paradigm has its own best practices, anti-patterns, and tooling, and most teams are expert in at most one. The result is a REST API with good pagination but no versioning strategy, a GraphQL schema with N+1 query problems, and gRPC services with no streaming where streaming would cut latency by 80%.

Security compounds everything. Teams forget CORS configuration until the frontend team reports cross-origin errors. Rate limiting is added as an afterthought. API keys are passed in query strings instead of headers. Authentication patterns are inconsistent across endpoints. Each gap is a future incident, and the cost of retrofitting security into a shipped API is 10x the cost of designing it in from the start.

## The Solution

This plugin provides a unified API design skill that covers REST, GraphQL, gRPC, and Python library architectures in one place. It ships with 18 reference files covering every aspect from URL naming conventions to Apollo Federation, 7 production-ready templates you can use as starting points, 5 automation scripts for validation and code generation, and 2 review checklists for pre-launch audits.

The skill provides concrete, copy-pasteable patterns: FastAPI route templates with proper dependency injection, Pydantic schema patterns with validation, GraphQL schema design with Relay-compliant pagination, gRPC service definitions with streaming, and authentication patterns for OAuth 2.0, JWT, and API keys. It covers both greenfield design (creating a new API from scratch) and review/audit of existing APIs.

Time savings are substantial: 50%+ reduction in API development time through templates, code generation scripts, and consistent patterns that eliminate the "how do I structure this?" decision overhead.

## Context to Provide

The more you describe your domain, consumers, and constraints, the more precise the URL design, schemas, authentication patterns, and validation will be.

**What information to include in your prompt:**

- **Domain and resources**: What entities does your API manage? (e.g., "organizations, projects, tasks, users, invitations")
- **Relationships**: How do resources relate to each other? ("An organization has many projects, a project has many tasks, tasks have one assignee who must be an organization member")
- **API consumers**: Who calls this API? (React SPA, mobile app, third-party integrators, internal services) -- this drives authentication and pagination choices
- **Multi-tenancy**: Is this a single-tenant or multi-tenant system? How is tenant isolation enforced?
- **Authentication context**: What auth mechanism do you need or already have? (JWT, OAuth 2.0, API keys, session cookies)
- **Scale expectations**: Rough order of magnitude for list endpoint sizes (50 records vs 50,000 records drives pagination design)
- **Existing API**: If reviewing an existing API, paste the endpoint list, OpenAPI spec, or representative request/response examples
- **Specific concerns**: What are you worried about? (versioning, rate limiting, CORS, error format consistency, N+1 queries in GraphQL)

**What makes results better:**
- Specifying all consumer types (not just the web app -- also the mobile app coming in 6 months and the enterprise API you will open up later) prevents decisions that lock you into single-consumer assumptions
- Describing a current pain point ("our list endpoints return all records with no pagination and it's causing timeouts") focuses the design on your actual problem
- Pasting an existing OpenAPI spec or endpoint list enables review mode with specific findings instead of generic advice
- Naming your tech stack (FastAPI, Express, Rails) enables concrete template and code generation instead of abstract patterns

**What makes results worse:**
- "Build me an API" with no domain context produces placeholder patterns that need rework for your actual entities
- Designing authentication "later" -- auth patterns affect URL structure, error format, and rate limiting from day one
- Omitting scale expectations for list endpoints -- cursor vs offset pagination is a different decision at 100 records vs 100,000

**Template prompt:**
```
Design a [REST / GraphQL / gRPC] API for [domain]. Resources: [list all entity types]. Relationships: [describe how they relate]. Consumers: [web app / mobile app / third-party developers / internal services]. Authentication: [what you need or have]. Multi-tenant: [yes/no, how isolation works]. Expected scale: [rough record counts for the largest list endpoints]. Tech stack: [backend language and framework]. Specific concerns: [versioning / rate limiting / pagination / error formats / security].
```

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Verb-based URLs (`/getUsers`) that violate REST conventions | Resource-oriented URLs (`/api/v1/users`) following established patterns |
| Inconsistent error responses across endpoints | Standardized error envelope with code, message, details, requestId, and timestamp |
| No pagination -- list endpoints return all records | Cursor-based and offset-based pagination patterns with proper response metadata |
| Rate limiting added as an afterthought after an outage | Rate limit headers (X-RateLimit-Limit, Remaining, Reset) designed in from day one |
| N+1 queries in GraphQL that grind the database | DataLoader pattern for batching with caching and complexity limits |
| Security gaps discovered in production | Pre-launch security checklist covering OAuth, CORS, secrets, and input validation |

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install api-design@skillstack
```

### Verify installation

After installing, test with:

```
Help me design a REST API for a multi-tenant project management app with teams, projects, and tasks
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `Design a REST API for a bookstore with books, authors, and reviews`
3. The skill produces resource URLs, HTTP methods, request/response schemas, pagination, and error handling
4. Refine: `Add authentication with JWT and rate limiting at 100 requests per minute`
5. Validate: `Run the API design checklist on what we've built`

---

## System Overview

```
+-------------------------------------------------------------------+
|                        api-design skill                            |
+-------------------------------------------------------------------+
|                                                                    |
|  +------------------+  +------------------+  +------------------+  |
|  |  REST Patterns   |  | GraphQL Patterns |  |  gRPC Patterns   |  |
|  |  - Resources     |  | - Schema-first   |  |  - Protobuf      |  |
|  |  - HTTP methods  |  | - Relay pagination|  |  - Streaming     |  |
|  |  - Status codes  |  | - Federation     |  |  - Services      |  |
|  |  - Versioning    |  | - DataLoader     |  +------------------+  |
|  +------------------+  +------------------+                        |
|                                                                    |
|  +------------------+  +------------------+  +------------------+  |
|  | Python Library   |  |    Security      |  |   FastAPI        |  |
|  | - SOLID patterns |  | - OAuth/JWT      |  |   - Routes       |  |
|  | - Package layout |  | - CORS           |  |   - Pydantic     |  |
|  | - PEP standards  |  | - Rate limiting  |  |   - Repository   |  |
|  +------------------+  +------------------+  +------------------+  |
|                                                                    |
|  Templates (7) | Examples (8) | Scripts (5) | Checklists (2)      |
+-------------------------------------------------------------------+
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `api-design` | Skill | Unified API design methodology for REST, GraphQL, gRPC, and Python libraries |

### References (18 files)

| Reference | Topic |
|---|---|
| `rest-best-practices.md` | REST API patterns, URL conventions, status codes |
| `authentication.md` | OAuth 2.0, JWT, API keys, MFA patterns |
| `versioning-strategies.md` | API versioning and deprecation strategies |
| `common-patterns.md` | Health checks, webhooks, batch operations |
| `schema-patterns.md` | GraphQL schema design patterns |
| `federation-guide.md` | Apollo Federation architecture |
| `performance-optimization.md` | GraphQL performance, DataLoader, caching |
| `architectural-principles.md` | Python library SOLID principles |
| `pep-standards.md` | Python PEP quick reference |
| `fastapi-setup.md` | FastAPI main app configuration |
| `openapi.md` | OpenAPI specification customization |
| `error-handlers.md` | FastAPI exception handlers |
| `cors-rate-limiting.md` | CORS and rate limiting setup |
| `openapi-spec.yaml` | Complete OpenAPI 3.1 example spec |
| `graphql-schema.graphql` | GraphQL schema with Relay connections |
| `grpc-service.proto` | Protocol Buffer service definitions |
| `rate-limiting.yaml` | Tier-based rate limit configuration |
| `api-security.yaml` | Auth, CORS, and security header config |

### Templates (7 files)

| Template | Purpose |
|---|---|
| `fastapi-crud-endpoint.py` | Complete CRUD router template |
| `pydantic-schemas.py` | Request/response schema template |
| `repository-pattern.py` | Repository with tenant isolation |
| `rate-limiter.py` | Upstash Redis rate limiter |
| `error-handler.py` | FastAPI exception handlers |
| `tanstack-server-function.ts` | TanStack Start server functions |

### Scripts (5 files)

| Script | CLI | Purpose |
|---|---|---|
| `schema_analyzer.py` | `python schema_analyzer.py schema.graphql --validate` | Analyze GraphQL schemas for quality |
| `resolver_generator.py` | `python resolver_generator.py schema.graphql` | Generate TypeScript resolvers from schema |
| `federation_scaffolder.py` | `python federation_scaffolder.py service-name --entities Entity` | Scaffold Apollo Federation subgraphs |
| `api_helper.py` | `python api_helper.py validate --spec openapi.yaml` | Validate OpenAPI specs and generate docs |
| `validate-api-spec.sh` | `bash validate-api-spec.sh` | Validate API specifications |

### Component Spotlights

#### api-design (skill)

**What it does:** Activates when you are designing, reviewing, or troubleshooting APIs across any paradigm -- REST, GraphQL, gRPC, or Python library architecture. Provides concrete patterns, templates, and validation tools for building production-grade APIs.

**Input -> Output:** API requirements (resources, operations, constraints) -> URL design, schemas, authentication setup, pagination, error handling, OpenAPI spec, and implementation templates.

**When to use:**
- Creating new API endpoints in any paradigm
- Designing resource hierarchies and URL structures
- Writing OpenAPI/Swagger specifications
- Implementing authentication (OAuth, JWT, API keys)
- Setting up pagination, filtering, and sorting
- Reviewing existing API designs for best practices
- Building GraphQL schemas with federation
- Designing Python library public APIs

**When NOT to use:**
- Building MCP servers for Claude Code -> use `mcp-server`
- Writing actual endpoint implementation logic -> use language-specific development skills
- Designing database schemas -> use `content-modelling` for data modeling

**Try these prompts:**

```
Design a REST API for an e-commerce platform. Resources: products, product variants (size/color), categories, orders, order line items, customers, addresses. An order has many line items, each line item references one product variant. Consumers: React SPA now, mobile app in 6 months, third-party integrations eventually. Auth: JWT. Scale: up to 500K products, 10K orders/day. Stack: FastAPI + PostgreSQL. Concerns: cursor pagination for product lists, consistent error format, rate limiting for future public API.
```

```
Review my API endpoints for best practices. I'm concerned about pagination (we return all records) and error formats (some endpoints return {error: "message"}, others return {detail: "message"}). Here are my main endpoints: [paste your endpoint list or OpenAPI spec].
```

```
I need a GraphQL schema for a social media app with users, posts, comments, likes, and follows. Real-time notifications via subscriptions. Mobile clients need to fetch a user's feed, profile, and notifications in one query instead of 5 round trips. Schema must be Relay-compliant. Add DataLoader to prevent N+1 on nested queries.
```

```
Split our monolith GraphQL API into federated subgraphs for user, product, and order teams. Each team deploys independently. Products reference users via userId. Orders reference both products and users. Show the @key directives, gateway config, and how cross-subgraph references resolve.
```

```
What's the best authentication pattern for our app? We have: a React SPA (no client secret in browser), a React Native mobile app, and we want to open a public API for third-party developers later. We use Auth0 today. Walk me through PKCE flow for the SPA/mobile and client credentials for third-party API keys.
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Make me an API" | "Design a REST API for a multi-tenant SaaS with teams, projects, and role-based access control" |
| "Fix my API" | "My list endpoint returns all 50K records with no pagination -- design cursor-based pagination with proper response metadata" |
| "Add security" | "Implement OAuth 2.0 authorization code flow for our web app and client credentials for service-to-service calls" |
| "Use api-design skill" | "Review my OpenAPI spec for best practices -- I'm concerned about versioning, error formats, and rate limiting" |

### Structured Prompt Templates

**For REST API design:**
```
Design a REST API for [domain]. The main resources are [resource 1], [resource 2], [resource 3]. Relationships: [resource 1] has many [resource 2], [resource 2] belongs to [resource 3]. I need [auth type] authentication, [pagination type] pagination, and the API will be [public/internal].
```

**For GraphQL schema design:**
```
Design a GraphQL schema for [domain]. Types: [type 1] with fields [fields], [type 2] with fields [fields]. I need Relay-compliant pagination on [list fields], subscriptions for [real-time events], and federation-ready entity definitions.
```

**For API review:**
```
Review these API endpoints for best practices: [paste endpoint list or OpenAPI spec]. Check for: URL naming, HTTP method usage, error response consistency, pagination, authentication, rate limiting, and versioning.
```

### Prompt Anti-Patterns

- **Designing without specifying resources**: "Build me an API for my app" -- the skill needs to know your domain resources, relationships, and constraints. Be specific about what entities exist and how they relate.
- **Mixing paradigms without rationale**: "I want REST and GraphQL and gRPC for everything" -- each paradigm has strengths. The skill will help you choose the right one for each use case rather than using all three everywhere.
- **Skipping security until the end**: "First design the endpoints, we'll add auth later" -- security patterns affect URL design, response formats, and error handling. Design them together.

## Real-World Walkthrough

**Starting situation:** You are building a multi-tenant project management SaaS. The frontend is a React SPA, there will eventually be a mobile app, and enterprise customers will need a public API for integrations. You have three main resources: organizations (tenants), projects, and tasks.

**Step 1: Resource design.** You ask: "Design a REST API for a multi-tenant project management app. Resources: organizations, projects, tasks. An organization has many projects, a project has many tasks. Tasks have assignees (users within the organization)." The skill produces a resource hierarchy:
```
/api/v1/organizations/{org_id}/projects
/api/v1/organizations/{org_id}/projects/{project_id}/tasks
/api/v1/organizations/{org_id}/members
```
It recommends limiting nesting to 2 levels and providing shortcut routes for frequently-accessed resources: `/api/v1/tasks?project_id=X` for cross-project task queries.

**Step 2: Schema design.** You ask: "Define the Pydantic schemas for tasks with validation." The skill produces `TaskCreate`, `TaskRead`, `TaskUpdate`, and `TaskList` schemas using the Pydantic patterns from the reference. TaskCreate requires title (min 1, max 255 chars) and project_id, with optional description, assignee_id, due_date, and priority (enum: low, medium, high, urgent). TaskRead includes computed fields: created_at, updated_at, and organization_id (derived from project).

**Step 3: Pagination and filtering.** The skill recommends cursor-based pagination for tasks (they change frequently, offset-based would skip or duplicate items) and provides the response format with nextCursor, hasMore, and totalCount. Filtering supports `?status=open&assignee_id=X&due_before=2025-01-01` with validation on all filter parameters.

**Step 4: Authentication.** You ask: "Design auth for three contexts: web SPA, future mobile app, and enterprise public API." The skill recommends:
- **Web SPA**: Authorization Code Flow with PKCE (no client secret stored in browser)
- **Mobile**: Same PKCE flow with deep link redirect
- **Public API**: Client credentials flow for service-to-service, with API key fallback for simpler integrations
- Tenant isolation enforced at the repository layer (every query scoped to org_id from the JWT claims)

**Step 5: Error handling and rate limiting.** The skill produces a standardized error envelope, maps it to HTTP status codes for each failure type, and adds rate limiting at three tiers: free (100 req/min), pro (1000 req/min), enterprise (custom). Rate limit headers are included in every response.

**Step 6: Validation.** You run the API design checklist: all endpoints use nouns, consistent response envelope, error responses include codes and messages, pagination on all list endpoints, auth documented, rate limits defined, versioning via URL prefix, CORS configured for known origins, idempotency keys for mutations, OpenAPI spec validates. Two items flagged: missing webhook endpoints for task events (added) and no deprecation strategy (added sunset header pattern).

**Gotchas discovered:** The initial design used `/projects/{id}/tasks` without the organization prefix, which would have required resolving the organization from the project in every request. The skill caught this and recommended the explicit hierarchy for clarity and security. Also, the initial error format used different field names for validation errors vs. auth errors -- standardized to a single envelope.

## Usage Scenarios

### Scenario 1: Designing a public API for a developer platform

**Context:** You are building a developer platform with webhooks, API keys, and SDK generation. Third-party developers will build integrations against your API.

**You say:** "Design a public API for a developer platform. Developers register apps, get API keys, configure webhooks, and access user data with OAuth consent. I need excellent DX."

**The skill provides:**
- OAuth 2.0 authorization code flow for user data access
- API key management endpoints (create, rotate, revoke)
- Webhook registration and delivery with retry logic and signature verification
- OpenAPI spec structured for SDK generation (proper operationIds, tags, descriptions)
- Rate limiting tiers with clear upgrade paths

**You end up with:** A complete API design document that an SDK generator can consume, with developer-friendly error messages and a webhook system that handles delivery failures gracefully.

### Scenario 2: Migrating from REST to GraphQL for mobile clients

**Context:** Your mobile app makes 8 REST calls per screen load because each endpoint returns a fixed shape. You want to move to GraphQL to reduce round trips.

**You say:** "My mobile app hits 8 REST endpoints per screen. Help me design a GraphQL schema that lets the mobile team fetch everything in one query."

**The skill provides:**
- GraphQL schema with types that map to your existing REST resources
- Relay-compliant connection types for paginated lists
- DataLoader setup to prevent N+1 queries from the flexible graph
- Complexity limiting to prevent abusive queries
- Migration strategy: GraphQL gateway in front of existing REST services

**You end up with:** A GraphQL schema that reduces 8 round trips to 1, with performance guardrails that prevent the flexibility from becoming a liability.

### Scenario 3: Setting up Apollo Federation for microservices

**Context:** Your monolith GraphQL API is becoming a bottleneck. Three teams own different parts of the schema and deploy conflicts are frequent.

**You say:** "Split our GraphQL monolith into federated subgraphs for user, product, and order teams."

**The skill provides:**
- Entity definitions with `@key` directives for cross-subgraph references
- Gateway configuration with subgraph routing
- Scaffolding via `federation_scaffolder.py` script
- Schema composition validation steps
- Migration plan: incremental extraction starting with the most independent subgraph

**You end up with:** Three independently deployable subgraphs with a federated gateway, plus CI validation that catches schema composition errors before deploy.

---

## Decision Logic

**When to use REST vs GraphQL vs gRPC?**

REST is the default for public APIs, CRUD-heavy services, and when cacheability matters (HTTP caching works natively). GraphQL is recommended when clients need flexible data shapes (mobile apps with varying screen sizes), when reducing round trips matters, or when multiple teams consume the same backend with different data needs. gRPC is recommended for internal service-to-service communication where latency matters, for streaming (bidirectional real-time data), and when strong typing with code generation is a priority.

**When to use cursor-based vs offset-based pagination?**

Cursor-based for datasets that change frequently (new items inserted, items deleted) or large datasets where deep pagination is common. Offset-based when simplicity matters, the dataset is small and stable, or when "jump to page N" is a UI requirement.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| No versioning strategy | Breaking change deployed, all clients break simultaneously | Add URL-based versioning (`/v1/`, `/v2/`) with sunset headers and 6-month deprecation windows |
| N+1 queries in GraphQL | Database overwhelmed by nested queries; response times spike | Implement DataLoader for batching; add query complexity limits |
| Inconsistent error formats | Client teams write bespoke error handling for each endpoint | Standardize on single error envelope; add response interceptor middleware |
| Rate limiting missing | Single abusive client takes down the API for everyone | Add per-user rate limiting with tiered limits; return 429 with Retry-After header |
| CORS misconfigured | Frontend team blocked by browser; wildcard origin used as quick fix | Configure specific allowed origins; never use `*` in production with credentials |

## Ideal For

- **Backend engineers designing new APIs** who need production-ready patterns for REST, GraphQL, or gRPC instead of inventing conventions from scratch
- **Full-stack developers building SaaS products** who need authentication, multi-tenancy, rate limiting, and pagination designed correctly from the start
- **Teams migrating API paradigms** (REST to GraphQL, monolith to federation) who need migration strategies with concrete implementation steps
- **API reviewers and tech leads** who need checklists and validation tools to catch design problems before launch
- **Python developers building libraries** who need SOLID architecture patterns, PEP-compliant packaging, and clean public API design

## Not For

- **Building MCP servers** for Claude Code -- MCP has its own protocol and patterns. Use `mcp-server`.
- **Database schema design** -- data modeling for CMS and content systems. Use `content-modelling`.
- **Frontend API consumption** -- how to call APIs from React/Next.js. Use `react-development` or `nextjs-development`.

## Related Plugins

- **code-review** -- Review your API implementation code for security, performance, and style
- **testing-framework** -- Test your API endpoints with integration tests
- **cicd-pipelines** -- Deploy your API with CI/CD pipelines and container orchestration
- **docker-containerization** -- Containerize your API service
- **typescript-development** -- Implement TypeScript API clients and server-side handlers

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
