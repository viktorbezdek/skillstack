---
name: edge-case-coverage
description: >-
  Identify and document boundary conditions, corner cases, error scenarios, and validation
  requirements that implementations must handle. Use when the user asks to find edge
  cases, identify corner cases, specify validation rules, enumerate error scenarios,
  harden a function against bad inputs, or think through what can go wrong at the
  boundaries of a system. NOT for writing the actual tests (use testing-framework
  or test-driven-development). NOT for structured risk registers around project-level
  risks (use risk-management). NOT for security vulnerability scanning (use code-review).
---

# Edge Case Coverage

Systematically identify and handle boundary conditions.

## Decision Tree: Which Edge Case Category?

```
What kind of edge case are you looking for?
├─ Input validation? → Check null, wrong type, empty, overflow, malformed
├─ Boundary values? → Check 0, 1, min, max, just-above, just-below
├─ State transitions? → Check uninitialized, concurrent, stale, partial
├─ Resource limits? → Check timeout, OOM, disk full, connection pool exhaustion
├─ Network failures? → Check offline, slow, partial failure, retry exhaustion
├─ Permission issues? → Check unauthorized, expired, revoked, insufficient scope
└─ Multi-system interaction? → Check race conditions, ordering, idempotency
```

## Edge Case Categories

| Category | Examples | Detection Heuristic |
|----------|----------|---------------------|
| Boundary | 0, 1, max, min, empty | Any numeric or size parameter |
| Input | null, undefined, wrong type | Any external-facing function |
| State | uninitialized, concurrent, stale | Any stateful operation |
| Resource | timeout, no memory, disk full | Any I/O or long-running operation |
| Network | offline, slow, partial failure | Any remote call |
| Permission | unauthorized, expired, revoked | Any auth-gated operation |

## Boundary Analysis

### Numeric Boundaries
```
Value: age
├── Below min: -1
├── At min: 0
├── Just above min: 1
├── Normal: 25
├── Just below max: 119
├── At max: 120
└── Above max: 121
```

### String Boundaries
```
Value: username
├── Empty: ""
├── Single char: "a"
├── Max length: "a" * 255
├── Over max: "a" * 256
├── Special chars: "user@#$"
└── Unicode: "user"
```

## Error Scenario Template

```markdown
## Scenario: [Name]

**Trigger**: [What causes it]
**Symptoms**: [What user sees]
**Root cause**: [Why it happens]
**Prevention**: [How to avoid]
**Recovery**: [How to fix]
```

## Validation Checklist

### Input Validation
- [ ] Required fields present
- [ ] Type correct
- [ ] Format valid (email, URL, etc.)
- [ ] Range within bounds
- [ ] Length within limits
- [ ] Characters allowed

### State Validation
- [ ] Object initialized
- [ ] Resources available
- [ ] Permissions granted
- [ ] Dependencies met
- [ ] No conflicts

## Coverage Matrix

| Input | Valid | Empty | Null | Overflow | Malformed |
|-------|-------|-------|------|----------|-----------|
| Name | [x] | [x] | [x] | [x] | [x] |
| Email | [x] | [x] | [x] | [x] | [x] |
| Age | [x] | [x] | [x] | [x] | [x] |

## Anti-Patterns

- **Happy path only** — designing and testing only the expected flow; every production failure starts as an edge case someone assumed would not happen
- **Ignoring nulls** — null is the most common edge case in production; always handle explicitly
- **Assuming valid input** — external input is never trustworthy; validate at the boundary
- **Missing timeout handling** — every network or I/O operation must have a timeout; without one, the system hangs indefinitely
- **Silent failures** — swallowing errors without logging or surfacing hides bugs until they cascade
- **Testing only one layer** — edge cases at the integration boundary (API + DB, UI + API) are the most common production failures
- **Forgetting idempotency** — retries on failed operations cause duplicates if endpoints are not idempotent

## When to Use

- Before implementing a feature — identify edge cases in the spec
- During code review — check for unhandled boundaries
- When hardening an existing system — systematic enumeration of failure modes
- When writing error handling — ensure all categories are covered
