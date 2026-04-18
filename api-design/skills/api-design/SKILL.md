---
name: api-design
description: >-
  Design production-grade REST, GraphQL, gRPC, and Python library APIs with correct
  schemas, error contracts, auth, and versioning. Use when the user asks to design an
  API, define endpoints, create an OpenAPI/Swagger spec, design a GraphQL schema, build
  a gRPC service, model request/response with Pydantic, add pagination, or review API
  contracts. NOT for building MCP server tools (use mcp-server). NOT for Node.js/Express
  API routes or backend patterns (use backend-patterns or typescript-development).
---

# API Design

Comprehensive API design skill combining REST, GraphQL, gRPC, and Python library architecture expertise with patterns, templates, and tools for production-grade APIs.

## When to Activate

- Creating new API endpoints (REST, GraphQL, gRPC)
- Designing resource hierarchies and schemas
- Writing OpenAPI/Swagger specifications
- Implementing authentication and authorization
- Setting up pagination, filtering, and sorting
- Configuring rate limiting and CORS
- Designing Python library APIs
- Reviewing API designs in pull requests

## Decision Tree: API Style Selection

```
What are you building?
+-- CRUD resources with clear entity model? --> REST
|   Best for: resource-oriented operations, caching, wide tooling support
+-- Complex queries with varying client needs? --> GraphQL
|   Best for: over-fetching prevention, nested data, multiple client types
+-- High-throughput service-to-service? --> gRPC
|   Best for: low latency, strong typing, streaming, polyglot microservices
+-- Reusable Python package? --> Python Library API
    Best for: SDKs, internal tooling, developer experience
```

## Quick Reference

### RESTful Resource Design

**URL Patterns:**
- `/api/v1/users` (plural nouns, lowercase with hyphens)
- `/api/v1/organizations/{org_id}/teams` (hierarchical, max 2 levels)
- Never use verbs: `/getUsers` or underscores: `/user_profiles`

**HTTP Methods:**
- `GET` - Retrieve (safe, idempotent, cacheable)
- `POST` - Create (returns 201 with Location header)
- `PUT` - Replace entire resource (idempotent)
- `PATCH` - Partial update (only changed fields)
- `DELETE` - Remove (idempotent, returns 204)

### HTTP Status Codes

| Category | Code | When |
|----------|------|------|
| Success | 200 | GET, PUT, PATCH success |
| Success | 201 | POST success (include Location header) |
| Success | 204 | DELETE success |
| Client Error | 400 | Malformed request |
| Client Error | 401 | Missing/invalid authentication |
| Client Error | 403 | Insufficient permissions |
| Client Error | 404 | Resource doesn't exist |
| Client Error | 409 | Duplicate resource |
| Client Error | 422 | Validation errors |
| Client Error | 429 | Rate limit exceeded |
| Server Error | 500 | Unhandled exception |
| Server Error | 503 | Database/service down |

### Error Response Format

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": [
      { "field": "email", "message": "Invalid email format" }
    ],
    "requestId": "req_abc123",
    "timestamp": "2025-10-25T10:30:00Z"
  }
}
```

### GraphQL Schema Design

```graphql
type User {
  id: ID!
  email: String!
  profile: Profile
  posts(first: Int, after: String): PostConnection!
  createdAt: DateTime!
}

type PostConnection {
  edges: [PostEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type Query {
  user(id: ID!): User
  users(first: Int, after: String): UserConnection!
  me: User
}

type Mutation {
  createUser(input: CreateUserInput!): CreateUserPayload!
  updateUser(id: ID!, input: UpdateUserInput!): UpdateUserPayload!
}
```

### FastAPI Route Pattern

```python
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> UserRead:
    """Create a new user in the current tenant."""
    repository = UserRepository(db, tenant_id=current_user.tenant_id)
    user = await repository.create(user_data)
    return user
```

### Pydantic Schema Pattern

```python
from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UserCreate(BaseModel):
    email: EmailStr
    full_name: str = Field(..., min_length=1, max_length=255)
    password: str = Field(..., min_length=8)

class UserRead(BaseModel):
    id: str
    tenant_id: str
    email: EmailStr
    full_name: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
```

### Pagination Patterns

**Cursor-Based (recommended for large datasets):**
```
GET /posts?limit=20&cursor=***
{ "data": [...], "pagination": { "nextCursor": "***", "hasMore": true } }
```

**Offset-Based (simpler, for small datasets):**
```
GET /posts?limit=20&offset=40
{ "data": [...], "pagination": { "total": 500, "limit": 20, "offset": 40 } }
```

### Authentication Patterns

| Flow | Use Case |
|------|----------|
| JWT Bearer tokens | API authentication, stateless sessions |
| API Key (X-API-Key) | Service-to-service, developer access |
| OAuth 2.0 Authorization Code | Web apps with backend |
| OAuth 2.0 Client Credentials | Service-to-service |
| OAuth 2.0 PKCE | Mobile/SPA apps |

### Rate Limiting Headers

```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 75
X-RateLimit-Reset: 1698340800
Retry-After: 60
```

## Available Resources

### References

| File | Description |
|------|-------------|
| `references/rest-best-practices.md` | Comprehensive REST API patterns and status codes |
| `references/authentication.md` | OAuth 2.0, JWT, API keys, MFA patterns |
| `references/versioning-strategies.md` | API versioning and deprecation |
| `references/common-patterns.md` | Health checks, webhooks, batch operations |
| `references/schema-patterns.md` | GraphQL schema design patterns |
| `references/federation-guide.md` | Apollo Federation architecture |
| `references/performance-optimization.md` | GraphQL performance, DataLoader, caching |
| `references/architectural-principles.md` | Python library SOLID principles |
| `references/pep-standards.md` | Python PEP quick reference |
| `references/fastapi-setup.md` | FastAPI main app configuration |
| `references/openapi.md` | OpenAPI customization |
| `references/error-handlers.md` | FastAPI exception handlers |
| `references/cors-rate-limiting.md` | CORS and rate limiting setup |
| `references/openapi-spec.yaml` | Complete OpenAPI 3.1 example |
| `references/graphql-schema.graphql` | GraphQL with Relay connections |
| `references/grpc-service.proto` | Protocol Buffer definitions |
| `references/rate-limiting.yaml` | Tier-based rate limit config |
| `references/api-security.yaml` | Auth, CORS, security headers |

### Templates

| File | Description |
|------|-------------|
| `templates/fastapi-crud-endpoint.py` | Complete CRUD router template |
| `templates/pydantic-schemas.py` | Request/response schema template |
| `templates/repository-pattern.py` | Repository with tenant isolation |
| `templates/rate-limiter.py` | Upstash Redis rate limiter |
| `templates/error-handler.py` | FastAPI exception handlers |
| `templates/tanstack-server-function.ts` | TanStack Start server functions |

### Examples

| File | Description |
|------|-------------|
| `examples/fastapi-crud.md` | CRUD endpoints with repository |
| `examples/pydantic-schemas.md` | Validation schema examples |
| `examples/pagination.md` | Pagination implementation |
| `examples/testing.md` | API testing patterns |
| `examples/tanstack-start.md` | TanStack Start examples |
| `examples/openapi-spec.yaml` | Blog API OpenAPI specification |
| `examples/graphql-schema.graphql` | Full GraphQL schema with subscriptions |

### Scripts

| File | Description |
|------|-------------|
| `scripts/schema_analyzer.py` | Analyze GraphQL schemas for quality |
| `scripts/resolver_generator.py` | Generate TypeScript resolvers |
| `scripts/federation_scaffolder.py` | Scaffold Apollo Federation subgraphs |
| `scripts/api_helper.py` | OpenAPI validation and docs generation |
| `scripts/validate-api-spec.sh` | Validate API specifications |

### Assets (Python Library)

| File | Description |
|------|-------------|
| `assets/pyproject.toml.template` | Production-ready pyproject.toml |
| `assets/README.md.template` | Library README template |
| `assets/CONTRIBUTING.md.template` | Contribution guide |
| `assets/project-structure.txt` | Recommended package layout |
| `assets/test-structure.txt` | Test organization |
| `assets/example-exceptions.py` | Exception hierarchy pattern |
| `assets/example-config.py` | Configuration pattern |

### Checklists

| File | Description |
|------|-------------|
| `checklists/api-design-checklist.md` | API design review checklist |
| `checklists/security-review.md` | Security review checklist |

## Core Workflows

### 1. Design a REST API

1. Identify resources (nouns): Users, Posts, Comments
2. Design URL structure with proper nesting
3. Choose appropriate HTTP methods
4. Define request/response schemas
5. Document with OpenAPI specification
6. Implement pagination and filtering
7. Add authentication and rate limiting

### 2. Build a GraphQL API

1. Define schema types with descriptions
2. Design queries with pagination (Relay connections)
3. Create mutations with input types and payloads
4. Implement DataLoader for N+1 prevention
5. Add authentication in resolvers
6. Configure caching and complexity limits

### 3. Validate API Specification

```bash
# Validate OpenAPI spec
python scripts/api_helper.py validate --spec openapi.yaml

# Analyze GraphQL schema
python scripts/schema_analyzer.py schema.graphql --validate

# Generate documentation
python scripts/api_helper.py docs --spec openapi.yaml --output docs/
```

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| Verb-based URLs | `/getUsers` violates REST conventions | Use `/users` with GET method |
| Inconsistent response envelopes | Clients can't parse predictably | Always use consistent structure |
| Breaking changes without versioning | Clients break on updates | Use semantic versioning; deprecation headers |
| N+1 queries in GraphQL | Each resolver fires separate DB query | Use DataLoader for batching |
| Over-fetching REST endpoints | Clients get more data than needed | Support sparse fieldsets, filtering |
| Missing pagination | List endpoints return unbounded results | Always paginate list endpoints |
| No idempotency keys | Duplicate mutations from retries | Accept `Idempotency-Key` header |
| Leaky internal errors | Stack traces exposed to clients | Generic messages in production |
| Missing CORS configuration | Browser requests blocked | Configure allowed origins explicitly |
| No rate limiting | API abuse and DoS | Implement per-user/per-endpoint limits |
| PUT for partial updates | Overwrites unchanged fields | Use PATCH for partial updates |
| Monolithic GraphQL schema | Schema becomes unmaintainable | Use Federation for schema separation |

## Quality Checklist

```
[ ] All endpoints use nouns, not verbs
[ ] Consistent response envelope structure
[ ] Error responses include codes and actionable messages
[ ] Pagination on all list endpoints
[ ] Authentication/authorization documented
[ ] Rate limit headers defined
[ ] Versioning strategy documented
[ ] CORS configured for known origins
[ ] Idempotency keys for mutating operations
[ ] OpenAPI spec validates without errors
[ ] Examples for all request/response types
```

---

**Version:** 1.1.0
**Last Updated:** 2026-04-18
