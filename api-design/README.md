# API Design

> Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures -- design endpoints, schemas, authentication, pagination, error handling, and federation.

## Overview

Building APIs is one of the most common and consequential tasks in software engineering. Poor API design leads to integration friction, security vulnerabilities, performance bottlenecks, and maintenance nightmares. This skill provides battle-tested patterns, production-ready templates, and automated tooling to get API design right the first time.

The API Design skill covers the full spectrum of API development: RESTful resource design with proper HTTP semantics, GraphQL schema-first development with Relay-compliant pagination, gRPC service definitions with Protocol Buffers, and Python library architecture following SOLID principles. It includes FastAPI and Pydantic patterns for rapid backend development, OAuth/JWT authentication flows, rate limiting strategies, and OpenAPI specification authoring.

As part of the SkillStack collection, this skill complements the CI/CD Pipelines skill (for deploying APIs), the Code Review skill (for reviewing API implementations), and the Consistency Standards skill (for maintaining uniform API conventions across services).

## What's Included

### References
- `rest-best-practices.md` -- Comprehensive REST API patterns and HTTP status codes
- `authentication.md` -- OAuth 2.0, JWT, API keys, and MFA patterns
- `versioning-strategies.md` -- API versioning and deprecation strategies
- `common-patterns.md` -- Health checks, webhooks, and batch operations
- `schema-patterns.md` -- GraphQL schema design patterns
- `federation-guide.md` -- Apollo Federation architecture guide
- `performance-optimization.md` -- GraphQL performance, DataLoader, and caching
- `architectural-principles.md` -- Python library SOLID principles
- `pep-standards.md` -- Python PEP quick reference
- `fastapi-setup.md` -- FastAPI main application configuration
- `openapi.md` -- OpenAPI specification customization
- `error-handlers.md` -- FastAPI exception handler patterns
- `cors-rate-limiting.md` -- CORS and rate limiting setup
- `openapi-spec.yaml` -- Complete OpenAPI 3.1 specification example
- `graphql-schema.graphql` -- GraphQL schema with Relay connections
- `grpc-service.proto` -- Protocol Buffer service definitions
- `rate-limiting.yaml` -- Tier-based rate limit configuration
- `api-security.yaml` -- Auth, CORS, and security header configuration

### Templates
- `fastapi-crud-endpoint.py` -- Complete CRUD router template with dependency injection
- `pydantic-schemas.py` -- Request/response schema template with validation
- `repository-pattern.py` -- Repository pattern with tenant isolation
- `rate-limiter.py` -- Upstash Redis rate limiter implementation
- `error-handler.py` -- FastAPI exception handler boilerplate
- `tanstack-server-function.ts` -- TanStack Start server function template

### Scripts
- `schema_analyzer.py` -- Analyze GraphQL schemas for quality issues
- `resolver_generator.py` -- Generate TypeScript resolvers from schema
- `federation_scaffolder.py` -- Scaffold Apollo Federation subgraphs
- `api_helper.py` -- OpenAPI validation and documentation generation
- `validate-api-spec.sh` -- Validate API specifications against standards

### Examples
- `fastapi-crud.md` -- Full CRUD endpoint implementation with repository
- `pydantic-schemas.md` -- Pydantic validation schema examples
- `pagination.md` -- Cursor-based and offset-based pagination implementation
- `testing.md` -- API testing patterns and strategies
- `tanstack-start.md` -- TanStack Start integration examples
- `openapi_spec.yaml` -- Blog API OpenAPI specification
- `graphql_schema.graphql` -- Full GraphQL schema with subscriptions

### Assets
- `pyproject.toml.template` -- Production-ready Python project configuration
- `README.md.template` -- Library README template
- `CONTRIBUTING.md.template` -- Contribution guide template
- `project-structure.txt` -- Recommended Python package layout
- `test-structure.txt` -- Test organization guide
- `example-exceptions.py` -- Exception hierarchy pattern
- `example-config.py` -- Configuration pattern

### Checklists
- `api-design-checklist.md` -- API design review checklist
- `security-review.md` -- Security review checklist

## Key Features

- **Multi-protocol coverage**: REST, GraphQL, gRPC, and Python library APIs in one unified skill
- **Production-ready templates**: FastAPI CRUD endpoints, Pydantic schemas, and repository patterns ready to use
- **Schema-first GraphQL**: Relay-compliant pagination, federation architecture, and DataLoader patterns
- **Security built-in**: OAuth 2.0 flows, JWT handling, API key management, CORS, and rate limiting
- **Automated tooling**: Schema analyzers, resolver generators, federation scaffolders, and spec validators
- **OpenAPI integration**: Complete 3.1 specification examples with validation scripts
- **Python-first patterns**: FastAPI, Pydantic, and SOLID architectural principles
- **Anti-pattern detection**: Identifies common API design mistakes before they ship

## Usage Examples

**Design a new REST API for a resource:**
```
Design a REST API for managing blog posts with CRUD operations,
pagination, and proper error handling. Include the OpenAPI spec.
```
Expected output: Resource URL structure, HTTP method mapping, request/response schemas, pagination parameters, error response format, and a complete OpenAPI specification.

**Create a GraphQL schema with federation:**
```
Create a GraphQL schema for a user service that will be part of
an Apollo Federation gateway. Include user profiles and posts.
```
Expected output: Federated schema with entity types, Relay-compliant connections, input types for mutations, and resolver boilerplate.

**Set up authentication for an API:**
```
Implement JWT-based authentication for a FastAPI application
with refresh tokens and role-based access control.
```
Expected output: Auth middleware, token generation/validation, role decorators, and Pydantic models for auth payloads.

**Scaffold a new FastAPI project:**
```
Create a new FastAPI project with CRUD endpoints for users and
organizations, using the repository pattern with multi-tenant isolation.
```
Expected output: Project structure, router definitions, Pydantic schemas, repository classes, and database session management.

**Validate an existing API specification:**
```
Review this OpenAPI spec for best practices compliance and suggest improvements.
```
Expected output: Validation results, anti-pattern detection, missing fields, and specific improvement recommendations.

## Quick Start

1. **Pick your API style** -- Decide between REST, GraphQL, or gRPC based on your use case
2. **Start with a template** -- Copy the appropriate template from `templates/` (e.g., `fastapi-crud-endpoint.py` for REST)
3. **Define your schemas** -- Use `templates/pydantic-schemas.py` to define request/response models
4. **Add authentication** -- Reference `references/authentication.md` for the right auth pattern
5. **Document with OpenAPI** -- Use `references/openapi-spec.yaml` as your starting point
6. **Validate your design** -- Run `python scripts/api_helper.py validate --spec openapi.yaml`
7. **Review against checklist** -- Walk through `checklists/api-design-checklist.md` before shipping

## Related Skills

- **[CI/CD Pipelines](../cicd-pipelines/)** -- Deploy and automate your API services
- **[Code Review](../code-review/)** -- Review API implementations for quality and security
- **[Consistency Standards](../consistency-standards/)** -- Maintain uniform naming and conventions across APIs
- **[Content Modelling](../content-modelling/)** -- Design the content structures your APIs will serve

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install api-design@skillstack` — 46 production-grade plugins for Claude Code.
