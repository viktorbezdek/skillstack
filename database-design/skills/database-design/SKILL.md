---
name: database-design
description: >-
  Database design and schema engineering for relational databases. Use for SQL schema design, ORM model authoring, migration strategies (Alembic, Liquibase, Flyway, Drizzle), query optimisation, indexing decisions, normalisation vs denormalisation trade-offs, and data-integrity constraints. Trigger phrases: "design this schema", "write a migration", "optimise this query", "model these entities", "add an index". NOT for NoSQL/document stores — use a dedicated NoSQL skill for those. NOT for ETL pipelines or data warehousing at scale — those involve different trade-offs. NOT for ORM configuration (framework setup) — this skill is about DATA SHAPE, not connection pooling or ORM bootstrap.
allowed-tools: Read,Write,Edit,Bash
---

# database-design

SQL schema design, ORM patterns, migration strategies, query optimisation, and data-modelling for relational databases.

## When to use

- Design a schema for a multi-tenant SaaS application
- Write an Alembic migration to add a non-null column to an existing table
- This query takes 4 seconds, help me add the right index
- Should I use a junction table or an array column for tags?
- Model a user → orders → line-items hierarchy in SQLAlchemy
- What constraints should I add to prevent orphaned records?
- Explain the difference between 3NF and BCNF
- Write a Drizzle ORM schema for a blog with posts, tags, and comments

## When NOT to use

- How do I set up PostgreSQL connection pooling with pgBouncer? — Connection pooling config — NOT data modelling
- Configure Redis as a session store — NoSQL / caching — out of scope
- Set up a Kafka consumer for event streaming — ETL / streaming pipeline — out of scope
- How do I back up my PostgreSQL database? — Operations/DBA — not schema engineering

## Anti-patterns

### Symptom
Invoking this skill for tasks outside its scope — e.g., infrastructure concerns when the request is about application code, or vice versa.

### Problem
Scope mismatch wastes context and produces advice tuned for the wrong domain. A database schema skill answering a connection-pooling question gives schema advice when the real problem is operational configuration.

### Solution
Read the NOT for clauses carefully. If the request matches an exclusion, identify the correct skill (check SkillStack for the right domain) rather than stretching this skill to cover adjacent ground.
