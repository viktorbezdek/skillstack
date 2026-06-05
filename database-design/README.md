# database-design

SQL schema design, ORM patterns, migration strategies, query optimisation, and data-modelling for relational databases.

## Overview

This plugin provides the `database-design` skill for Claude Code.

## Installation

Install via the SkillStack marketplace or copy this plugin directory into your Claude Code plugins folder.

## Usage

Invoke by describing your task naturally. The skill activates on relevant queries.

**Activates for:**
- Design a schema for a multi-tenant SaaS application
- Write an Alembic migration to add a non-null column to an existing table
- This query takes 4 seconds, help me add the right index
- Should I use a junction table or an array column for tags?

**Does NOT activate for:**
- How do I set up PostgreSQL connection pooling with pgBouncer? (Connection pooling config — NOT data modelling)
- Configure Redis as a session store (NoSQL / caching — out of scope)
- Set up a Kafka consumer for event streaming (ETL / streaming pipeline — out of scope)

## Domain

**Engineering**

## Changelog

See [CHANGELOG.md](./CHANGELOG.md).
