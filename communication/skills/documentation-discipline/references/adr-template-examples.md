# ADR — Template and Examples

Architecture Decision Records capture decisions and their reasoning at the time they were made. Once Accepted, an ADR is immutable — changes become new ADRs that supersede the old one. The goal is a chronological, honest record of why the system looks the way it does.

## Template

```markdown
# ADR-NNNN: [Title — noun phrase]

**Date:** YYYY-MM-DD
**Status:** Proposed / Accepted / Superseded by ADR-MMMM / Deprecated
**Deciders:** [Names]
**Related:** [ADR-XXXX, RFC-YYY, other relevant links]

## Context

[What forced the decision? What constraints existed?
What was true when this was decided?
1-3 paragraphs. Do not re-litigate history already covered elsewhere.]

## Decision

[What did we decide, stated as a present-tense claim. One paragraph.]

## Consequences

- **Positive:**
  - [Specific gain]
  - [Specific gain]
- **Negative:**
  - [Specific cost]
  - [Specific cost]
- **Neutral:**
  - [Trade-off accepted without strong opinion]

## Alternatives considered

- **[Option name]** — [why not chosen, one sentence]
- **[Option name]** — [why not chosen, one sentence]
- **Do nothing** — [why not chosen, one sentence]
```

## Worked examples

### Example 1 — Database choice

```markdown
# ADR-0003: Use PostgreSQL as Primary Datastore

**Date:** 2026-03-14
**Status:** Accepted
**Deciders:** @platform-lead
**Related:** ADR-0001 (TypeScript), ADR-0002 (Deploy via Kubernetes)

## Context

We are choosing the primary datastore for the core application. Requirements:
multi-tenant isolation, relational integrity across 15+ entities, strong
transactional guarantees, operational maturity for a team of 8 engineers
with prior PostgreSQL experience. Expected scale: 10M rows, 200 concurrent
connections within 12 months.

## Decision

We use PostgreSQL 16 as the primary datastore. Tenant isolation via schema
per tenant. All operational data — users, orders, billing, audit — goes in
PostgreSQL. Analytical workloads may later move to a separate system.

## Consequences

- **Positive:**
  - Team has PostgreSQL operational experience; onboarding cost zero.
  - Row-level security and schemas give multi-tenant isolation without app changes.
  - Rich ecosystem: migrations (Flyway/Prisma), backups, observability.
- **Negative:**
  - Vertical scaling limits at ~500GB without partitioning; requires planning.
  - Connection pooling (pgBouncer) becomes operationally necessary early.
- **Neutral:**
  - Schema-per-tenant requires tenant-aware migrations; tooling exists.

## Alternatives considered

- **MySQL** — Comparable capability; chose PostgreSQL for better JSON support and row-level security.
- **MongoDB** — Poor fit for relational integrity we need; would require app-enforced constraints.
- **DynamoDB** — Operational simplicity attractive, but schema-per-tenant pattern and complex queries are painful.
- **Do nothing** — We are a new system; deferring the choice is not an option.
```

### Example 2 — API style

```markdown
# ADR-0008: Use REST with OpenAPI for Public API

**Date:** 2026-04-02
**Status:** Accepted
**Deciders:** @api-lead, @eng-dir
**Related:** ADR-0007 (API Gateway: Envoy)

## Context

We need to pick an API style for our public-facing API. Four candidates were
seriously evaluated: REST+OpenAPI, gRPC, GraphQL, and a custom JSON-RPC
variant. Our consumers are a mix of developers (SDK integrations) and
internal web/mobile clients. Primary concerns: discoverability, tooling
maturity, learning curve for consumers.

## Decision

The public API is REST with OpenAPI 3.1 specification. Internal RPC between
services uses gRPC (covered in a separate ADR). GraphQL is deferred to a
future decision if federation needs emerge.

## Consequences

- **Positive:**
  - Broad client familiarity reduces integration friction.
  - OpenAPI generates SDKs and docs; zero extra work for basic tooling.
  - curl-debuggable; ops teams can investigate without specialized tools.
- **Negative:**
  - Over-fetching / under-fetching without careful resource design.
  - Real-time and batch operations need additional mechanisms (SSE / batch endpoints).
- **Neutral:**
  - OpenAPI spec becomes source of truth; enforce via CI.

## Alternatives considered

- **gRPC public** — Better perf but consumer friction high; keep gRPC for service-to-service.
- **GraphQL** — Resolver complexity and cache story weaker for our consumer mix.
- **Custom JSON-RPC** — No ecosystem benefit to offset the "not a standard" cost.
- **Do nothing** — Not viable; API launch is on the critical path.
```

### Example 3 — Superseded ADR

```markdown
# ADR-0011: Event Bus via Kafka

**Date:** 2025-11-22
**Status:** Superseded by ADR-0029
**Deciders:** @platform-lead

## Context
[Original context.]

## Decision
[Original decision.]

## Consequences
[As originally written.]

## Alternatives considered
[As originally written.]

---

**Note (2026-04-18):** This ADR has been superseded by ADR-0029 (Event Bus
via AWS SNS/SQS). Reasoning is in ADR-0029; this file remains for historical
reference and is not edited.
```

**Rule:** When an ADR is superseded, the original file is NOT edited except to update the Status field and add a dated note at the bottom. The superseding ADR explains the reasoning.

### Example 4 — A rejected ADR

```markdown
# ADR-0014: Rewrite Payment Service in Rust

**Date:** 2026-02-08
**Status:** Rejected
**Deciders:** @eng-dir, @platform-lead

## Context

Payment service has performance issues under load; 99th percentile latency
above SLO 18% of the time. Team proposed a Rust rewrite.

## Decision

We do NOT rewrite the payment service in Rust. Performance issues are
traced to two specific hot paths that can be optimized in place. We
revisit if optimization fails.

## Consequences

- **Positive:**
  - Avoids 6+ month rewrite with all its risks.
  - Preserves team throughput on payment features.
- **Negative:**
  - If optimizations fail, we have delayed the inevitable.
  - Signals to the team that rewrites are hard to approve.

## Alternatives considered

- **Rust rewrite** — Rejected: too costly for a scoped performance issue.
- **Vertical scaling** — Addresses only compute-bound issues; our problem is lock contention.
- **Profile-led optimization** — Chosen path; addressed in separate tickets.
```

Recording rejected ADRs is valuable — future engineers see what was considered AND why it was rejected.

## Rules for ADRs

1. **Numbered sequentially.** `0001`, `0002`, `0003` — never re-used, never re-ordered.
2. **Immutable once Accepted.** Changes become a new ADR that supersedes.
3. **Stored in the repo** at a known path — typically `docs/adr/` or `architecture/decisions/`.
4. **Short** — 1-3 pages. Long analyses belong in RFCs.
5. **Architecture only** — not tooling preferences or UX copy. Use decision docs for non-architecture choices.
6. **One decision per ADR** — do not bundle multiple choices in one file.
7. **Titles are noun phrases** — "Use PostgreSQL" not "Database Selection Framework."

## Common mistakes

- **Editing an accepted ADR.** Should have written a new one that supersedes.
- **ADR for non-architecture choices.** Tooling preferences, UX copy, process changes — use decision docs.
- **Missing alternatives section.** Creates the impression no alternatives were considered.
- **Vague context.** "The system needs a database." Why this system? What constraints? Be specific.
- **Positive-only consequences.** No system decision is purely positive; list the costs honestly.
- **Bundling multiple decisions.** "Use PostgreSQL AND Redis AND Kafka" should be three ADRs.
- **Forgetting to update status.** An ADR that's been superseded but still says "Accepted" misleads readers.

## Maintaining the ADR log

Create `docs/adr/README.md` as an index:

```markdown
# Architecture Decision Records

| # | Title | Status | Date |
|---|---|---|---|
| [0001](0001-use-typescript.md) | Use TypeScript for Services | Accepted | 2025-09-12 |
| [0002](0002-deploy-via-kubernetes.md) | Deploy via Kubernetes | Accepted | 2025-10-03 |
| [0003](0003-postgresql-primary-datastore.md) | Use PostgreSQL as Primary Datastore | Accepted | 2026-03-14 |
| [0011](0011-event-bus-kafka.md) | Event Bus via Kafka | Superseded by [0029](0029-event-bus-sns-sqs.md) | 2025-11-22 |
| [0014](0014-payment-rewrite-rust.md) | Rewrite Payment Service in Rust | Rejected | 2026-02-08 |
```

The index is the table of contents. Update with every new ADR.
