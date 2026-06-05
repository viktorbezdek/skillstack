---
name: competitive-intelligence
description: >-
  Competitive intelligence and market positioning analysis for product and GTM decisions. Use for competitor landscape mapping, positioning gap identification, win/loss pattern synthesis, battlecard creation, market-sizing estimates (TAM/SAM/SOM), and differentiation analysis. Trigger phrases: "map the competitive landscape", "create a battlecard for", "analyse our win/loss patterns", "how do we differentiate from", "size this market". NOT for primary market research (customer interviews, surveys) — this skill works from existing public and internal data. NOT for financial modelling or investor decks — competitive context informs the story but this skill does not build financial projections. NOT for pricing strategy deep-dives — pricing has its own set of constraints and frameworks beyond competitive positioning.
allowed-tools: Read,Write,Edit,Bash
---

# competitive-intelligence

Competitor analysis, market sizing, positioning maps, win/loss pattern synthesis, and battlecard creation for product and GTM decisions.

## When to use

- Map the competitive landscape for AI code assistants (GitHub Copilot, Cursor, etc.)
- Create a battlecard for our sales team competing against Datadog
- Analyse our last 50 win/loss notes — what patterns do you see?
- How should we position against a competitor that's 10x larger?
- Estimate the TAM for developer productivity tools in enterprise
- What are the defensible moats in the observability market?
- Identify the positioning gaps in the MLOps tool landscape
- Compare our feature set against three competitors in a matrix

## When NOT to use

- Run customer interviews to validate our positioning hypothesis — Primary research — not CI synthesis
- Build a three-year financial model for our go-to-market plan — Financial modelling — out of scope
- Design our pricing tiers and annual contract structure — Pricing strategy — separate concern
- Write a press release about our product launch — Comms/PR — not competitive intelligence

## Anti-patterns

### Symptom
Invoking this skill for tasks outside its scope — e.g., infrastructure concerns when the request is about application code, or vice versa.

### Problem
Scope mismatch wastes context and produces advice tuned for the wrong domain. A database schema skill answering a connection-pooling question gives schema advice when the real problem is operational configuration.

### Solution
Read the NOT for clauses carefully. If the request matches an exclusion, identify the correct skill (check SkillStack for the right domain) rather than stretching this skill to cover adjacent ground.
