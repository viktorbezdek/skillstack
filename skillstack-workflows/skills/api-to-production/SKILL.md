---
name: api-to-production
description: End-to-end workflow for taking an API from design through TDD, code review, CI/CD, and containerized deployment. Composes five phases — REST/GraphQL/gRPC design with schemas and error contracts (api-design), red-green-refactor on every endpoint (test-driven-development), multi-perspective code review (code-review), pipeline wiring with automated testing (cicd-pipelines), and Docker containerization with multi-stage builds and optimization (docker-containerization). Use when building a new API endpoint or service that needs to ship to production. Use when converting a prototype API into production-grade infrastructure. NOT for frontend-only work — use frontend-design or react-development. NOT for existing API maintenance without deployment changes — use code-review directly.
---

# API to Production

> The gap between "it works on my machine" and "it runs in production" is where most APIs die. This workflow closes that gap by enforcing design-first, test-first, review-before-ship, and container-before-deploy as non-negotiable phases.

An API that ships without tests ships with regressions waiting to happen. An API that ships without CI/CD ships with manual deployment risk. An API that ships without containerization ships with "works on my machine" as its deployment strategy. This workflow prevents all three.

---

## When to use this workflow

- Building a new API service or endpoint from scratch
- Taking a prototype API to production readiness
- Adding a new service to an existing microservices architecture
- Rebuilding an API that currently deploys manually
- Setting up the full development-to-deployment pipeline for a team

## When NOT to use this workflow

- **Frontend-only work** — use `frontend-design` or `react-development`
- **Existing API bug fixes** — use `debugging` and `code-review` directly
- **API design exploration without intent to ship** — use `api-design` alone
- **Serverless functions** — the containerization phase may not apply; adapt or skip Phase 5
- **Internal scripts or CLIs** — these aren't APIs; use the language-specific development skill

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install api-design@skillstack
/plugin install test-driven-development@skillstack
/plugin install code-review@skillstack
/plugin install cicd-pipelines@skillstack
/plugin install docker-containerization@skillstack
```

---

## Core principle

**Design the contract before writing the code, write the tests before the implementation, and wire the pipeline before the first deploy.** Every phase builds on the previous one. Skipping a phase doesn't save time — it moves the cost downstream where it's more expensive to fix.

Secondary principle: **the API contract is the source of truth.** Endpoint paths, request/response schemas, error codes, and status codes are decided in Phase 1 and tested in Phase 2. If the implementation diverges from the contract, the implementation is wrong — not the contract.

---

## The phases

### Phase 1 — design the API contract (api-design)

Load the `api-design` skill. Before writing any code, define:

- **Protocol** — REST, GraphQL, or gRPC. Each has different trade-offs. REST for simplicity and cacheability, GraphQL for flexible client queries, gRPC for internal service-to-service with strong typing.
- **Resource modeling** — what are the nouns? How do they relate? What operations does each support?
- **Schema definitions** — request bodies, response shapes, and validation rules for every endpoint. Use OpenAPI, GraphQL SDL, or protobuf — not prose descriptions.
- **Error contract** — every error response has a consistent shape with error codes, messages, and machine-readable details. Decide this once, enforce everywhere.
- **Versioning strategy** — URL path (`/v1/`), header, or content negotiation. Pick one before the first endpoint ships.
- **Pagination, filtering, sorting** — if the API returns collections, these are part of the contract, not an afterthought.

The output is a machine-readable API specification that serves as the single source of truth for all subsequent phases.

Output: OpenAPI spec, GraphQL schema, or protobuf definitions with full endpoint coverage.

### Phase 2 — TDD the endpoints (test-driven-development)

Load the `test-driven-development` skill. For each endpoint in the contract:

1. **Write a failing test** that exercises the endpoint against the contract from Phase 1. Test the happy path first — correct request yields correct response with correct status code.
2. **Implement the minimum code** to make the test pass. No extra features, no premature optimization.
3. **Add error case tests** — invalid input returns the correct error shape, missing auth returns 401, missing resource returns 404.
4. **Refactor** — clean up the implementation while keeping all tests green.

Test coverage targets:
- Every endpoint has at least one happy-path test
- Every documented error code has a test that triggers it
- Edge cases: empty collections, maximum pagination, boundary values
- Integration tests for database queries and external service calls

Do not proceed until the full test suite passes and coverage meets your threshold.

Output: a passing test suite covering every endpoint, error case, and documented behavior.

### Phase 3 — code review (code-review)

Load the `code-review` skill. Run a multi-perspective review:

- **Security** — SQL injection, auth bypass, input validation gaps, information leakage in error messages
- **Performance** — N+1 queries, missing indexes, unbounded result sets, missing caching headers
- **API contract compliance** — does the implementation match the spec from Phase 1? Any undocumented behavior?
- **Error handling** — are all error paths tested? Do errors leak internal details?
- **Style and consistency** — naming conventions, response shapes, header usage

Fix every finding before proceeding. A code review after CI/CD is wired means the pipeline catches regressions on the fixes too.

Output: a clean review with all findings addressed and tests still passing.

### Phase 4 — CI/CD pipeline (cicd-pipelines)

Load the `cicd-pipelines` skill. Wire the automation:

- **Build stage** — compile, type-check, lint. Fast feedback on obvious errors.
- **Test stage** — run the full test suite from Phase 2. Fail the pipeline on any failure.
- **Security scan** — dependency vulnerability checks, secret scanning, SAST if applicable.
- **Artifact stage** — build the deployable artifact (container image, package, bundle).
- **Deploy stage** — deploy to staging automatically, production with approval gate.

The pipeline should run on every push to a feature branch and on every merge to main. If the test suite from Phase 2 is comprehensive, the pipeline catches regressions automatically.

Output: a working CI/CD pipeline that builds, tests, scans, and deploys the API.

### Phase 5 — containerize (docker-containerization)

Load the `docker-containerization` skill. Build the container:

- **Multi-stage build** — separate build dependencies from runtime. The production image should not contain compilers, dev dependencies, or source code.
- **Base image selection** — Alpine for size, Debian for compatibility, distroless for security. Choose based on your constraints.
- **Health checks** — the container exposes a health endpoint that the orchestrator can probe.
- **Configuration** — environment variables for runtime config, not baked-in values. Twelve-factor app principles.
- **Docker Compose** — for local development, define the full stack (API + database + cache + any dependencies) so developers can run the whole system with one command.
- **Image optimization** — layer ordering for cache efficiency, `.dockerignore` to exclude unnecessary files, minimal final image size.

Output: Dockerfile, docker-compose.yml, and a production-ready container image.

### Phase 6 — verify end-to-end and document

With all previous phases complete, verify the full chain:

1. **Build the container** — does it build cleanly?
2. **Run the test suite inside the container** — do all tests pass in the containerized environment, not just locally?
3. **Hit the API through the container** — make real HTTP requests to the running container. Verify response shapes match the Phase 1 contract.
4. **Run the CI/CD pipeline** — does the full pipeline pass end-to-end?
5. **Document the API** — generate or write API documentation from the spec. Include authentication, rate limits, and example requests/responses.

If any step fails, trace back to the phase that should have caught it and fix the root cause there.

Output: a verified, documented, containerized API with a passing CI/CD pipeline.

---

## Gates and failure modes

**Gate 1: the contract gate.** Phase 2 cannot start until Phase 1's API spec exists. Writing tests without a contract means testing whatever the implementation happens to do.

**Gate 2: the test gate.** Phase 3 cannot start until Phase 2's test suite passes. Reviewing untested code is reviewing hopes, not behavior.

**Gate 3: the pipeline gate.** Phase 5 cannot start until Phase 4's pipeline runs successfully. Containerizing before the pipeline is wired means no automated safety net during the containerization work.

**Failure mode: implementation-first.** The team writes the API, then tries to design the contract after the fact. The contract becomes a description of whatever was built, not a specification. Mitigation: Phase 1 is mandatory and produces a machine-readable spec.

**Failure mode: testing the happy path only.** All tests pass, but none test error cases. The first malformed request in production crashes the service. Mitigation: Phase 2 requires error case tests for every documented error code.

**Failure mode: "it works in Docker on my machine."** The container builds and runs locally but fails in CI because of environment differences. Mitigation: Phase 6 runs tests inside the container, not just alongside it.

---

## Output artifacts

1. **API specification** — OpenAPI, GraphQL schema, or protobuf definitions
2. **Implementation** — the API code, passing all tests
3. **Test suite** — unit, integration, and contract tests with documented coverage
4. **CI/CD pipeline** — build, test, scan, deploy stages
5. **Dockerfile + docker-compose.yml** — production image and local development stack
6. **API documentation** — generated from the spec with examples
7. **Review evidence** — addressed findings from the code review

---

## Related workflows and skills

- For API design exploration without the full pipeline, use `api-design` alone
- For debugging production API issues, use the `debug-complex-issue` workflow
- For security-focused review of an existing API, use the `security-hardening-audit` workflow
- For frontend clients consuming this API, use `react-development` or `nextjs-development`

---

> *SkillStack Workflows by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
