# Design Rationale

Consult when instructions seem counter-intuitive or you're tempted to deviate.

## Why SQLite over JSON

- **Scales to 500+ stories** without performance issues
- **Single SQL query** replaces recursive tree traversal
- **Atomic transactions** prevent data corruption

## Why Closure Table

| Pattern | Read | Write | Complexity |
|---------|------|-------|------------|
| **Closure Table** | Excellent | Good | Simple |
| Adjacency List | Poor | Excellent | Complex |
| Nested Sets | Excellent | Poor | Moderate |

Closure tables store ALL ancestor-descendant paths, enabling:
- Subtree queries without recursion
- O(1) depth calculation
- Efficient read-heavy workloads

Trade-off: More storage (O(n*depth) rows). Acceptable for backlog management.

## Why Database Separate from Skill

Skill files (SKILL.md, schema.sql) → copied between projects
Database (story-tree.db) → project-specific data

Location: `.claude/data/story-tree.db` (tracked in git for history)

## Status Exclusions

Priority algorithm excludes:
- `concept` - Await human approval
- `rejected` - Human decided against
- `deprecated` - No longer relevant
- `infeasible` - Cannot be built
- `bugged` - Fix first before expanding

## Dynamic Capacity

`effective_capacity = capacity_override OR (3 + implemented/ready children)`

Benefits:
- New nodes start with capacity 3
- Grows as children complete
- Forces depth before breadth
- Tree grows based on progress, not speculation

## Max 3 Concepts Per Node

Combined with dynamic capacity (starts at 3):
1. First pass: add up to 3 concepts (fills initial)
2. Implement children → capacity grows
3. Next pass: add more as earned

Prevents shallow, speculative growth.

## Why Log Checkpoint Failures

When checkpoint is missing/rebased, log reason before fallback:
- "No checkpoint found. Running full 30-day scan."
- "Checkpoint abc123 no longer exists. Running full 30-day scan."

Helps users understand why analysis is slower.

---

## Version History

- v2.4.1: Consolidated skill structure per skill-creator guidelines
- v2.4.0: Dynamic capacity, status blacklist
- v2.3.0: Progressive context disclosure
- v2.0.0: Migrated from JSON to SQLite
- v1.0.0: Initial release
