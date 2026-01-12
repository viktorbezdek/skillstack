---
name: api-design
description: "Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, authentication, pagination, error handling, and federation. Use when: creating API specifications, designing REST endpoints, GraphQL schemas, gRPC services, FastAPI routes, Pydantic schemas, authentication flows, rate limiting, versioning, or Python library APIs. Triggers: 'API', 'endpoint', 'REST', 'FastAPI', 'Pydantic', 'GraphQL', 'gRPC', 'OpenAPI', 'Swagger', 'OAuth', 'JWT', 'pagination', 'validation', 'rate limiting', 'CORS', 'authentication', 'federation', 'schema'."
---

# API Design

Comprehensive API design skill combining REST, GraphQL, gRPC, and Python library architecture expertise. This merged skill provides patterns, templates, and tools for building production-grade APIs.

## Overview

This skill combines expertise from multiple specialized domains:
- **REST API Design** - Resource-oriented endpoints, HTTP semantics, OpenAPI specs
- **GraphQL Development** - Schema-first design, resolvers, federation, DataLoader
- **gRPC Services** - Protocol Buffers, streaming patterns
- **Python Library Architecture** - Package structure, API design, SOLID principles
- **Security & Performance** - OAuth, JWT, rate limiting, caching

**Time Savings:** 50%+ reduction in API development time through templates, code generation, and best practices.

## Quick Reference

### RESTful Resource Design

**URL Patterns:**
- `/api/v1/users` (plural nouns, lowercase with hyphens)
- `/api/v1/organizations/{org_id}/teams` (hierarchical, max 2 levels)
- Never use verbs: `/getUsers` or underscores: `/user_profiles`

**HTTP Methods:**
- `GET` - Retrieve resources (safe, idempotent, cacheable)
- `POST` - Create new resources (returns 201 with Location header)
- `PUT` - Replace entire resource (idempotent)
- `PATCH` - Partial update (only changed fields)
- `DELETE` - Remove resource (idempotent, returns 204)

### HTTP Status Codes

**Success:**
- `200 OK` - GET, PUT, PATCH success
- `201 Created` - POST success (include Location header)
- `204 No Content` - DELETE success

**Client Errors:**
- `400 Bad Request` - Malformed request
- `401 Unauthorized` - Missing/invalid authentication
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource doesn't exist
- `409 Conflict` - Duplicate resource
- `422 Unprocessable Entity` - Validation errors
- `429 Too Many Requests` - Rate limit exceeded

**Server Errors:**
- `500 Internal Server Error` - Unhandled exception
- `503 Service Unavailable` - Database/service down

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
    """Schema for creating a new user."""
    email: EmailStr
    full_name: str = Field(..., min_length=1, max_length=255)
    password: str = Field(..., min_length=8)

class UserRead(BaseModel):
    """Schema for reading user data (public fields only)."""
    id: str
    tenant_id: str
    email: EmailStr
    full_name: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
```

### Pagination Patterns

**Cursor-Based (recommended):**
```
GET /posts?limit=20&cursor=eyJpZCI6MTIzfQ

Response:
{
  "data": [...],
  "pagination": {
    "nextCursor": "eyJpZCI6MTQzfQ",
    "hasMore": true
  }
}
```

**Offset-Based (simpler):**
```
GET /posts?limit=20&offset=40

Response:
{
  "data": [...],
  "pagination": {
    "total": 500,
    "limit": 20,
    "offset": 40
  }
}
```

### Authentication Patterns

**JWT Token Usage:**
```http
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
```

**API Key Usage:**
```http
X-API-Key: sk_live_abc123def456
```

**OAuth 2.0 Flows:**
- Authorization Code Flow - Web apps with backend
- Client Credentials Flow - Service-to-service
- PKCE Flow - Mobile/SPA apps

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

### 3. Set Up Apollo Federation

```bash
# Scaffold subgraphs
python scripts/federation_scaffolder.py users-service --entities User,Profile
python scripts/federation_scaffolder.py posts-service --entities Post --references User

# Configure gateway
python scripts/federation_scaffolder.py gateway --subgraphs users:4001,posts:4002
```

### 4. Validate API Specification

```bash
# Validate OpenAPI spec
python scripts/api_helper.py validate --spec openapi.yaml

# Analyze GraphQL schema
python scripts/schema_analyzer.py schema.graphql --validate

# Generate documentation
python scripts/api_helper.py docs --spec openapi.yaml --output docs/
```

## Anti-Patterns to Avoid

1. **Verb-Based URLs** - Use `/users` not `/getUsers`
2. **Inconsistent Response Envelopes** - Always use consistent structure
3. **Breaking Changes Without Versioning** - Use semantic versioning
4. **N+1 Queries in GraphQL** - Use DataLoader for batching
5. **Over-fetching REST Endpoints** - Support sparse fieldsets
6. **Missing Pagination** - Always paginate list endpoints
7. **No Idempotency Keys** - Accept `Idempotency-Key` header for mutations
8. **Leaky Internal Errors** - Generic messages in production
9. **Missing CORS Configuration** - Configure allowed origins explicitly
10. **No Rate Limiting** - Implement per-user/per-endpoint limits

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
[ ] SDK generation tested
[ ] Examples for all request/response types
```

## When to Use This Skill

- Creating new API endpoints (REST, GraphQL, gRPC)
- Designing resource hierarchies and schemas
- Writing OpenAPI/Swagger specifications
- Implementing authentication and authorization
- Setting up pagination, filtering, and sorting
- Configuring rate limiting and CORS
- Designing Python library APIs
- Reviewing API designs in pull requests

## Source Skills

This merged skill combines content from:
- **grey-haven-api-design-standards** - FastAPI, Pydantic, multi-tenant patterns
- **python-library-architect** - Library structure, SOLID principles, PEP standards
- **senior-graphql-specialist** - GraphQL, Apollo, Federation, DataLoader
- **api-architect** - REST, gRPC, security, versioning
- **api-designer** - Documentation, authentication, best practices

---

**Version:** 1.0.0
**Last Updated:** 2025-01-18

