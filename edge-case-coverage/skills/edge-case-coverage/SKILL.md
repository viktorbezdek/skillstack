---
name: edge-case-coverage
description: >-
  Identify and document boundary conditions, error scenarios, corner cases, and validation
  requirements. Use when analyzing edge cases, boundary testing, corner cases, error
  scenarios, validation rules, or defensive programming. NOT for writing tests
  (use testing-framework or test-driven-development).
---

# Edge Case Coverage

Systematically identify and handle boundary conditions.

## Edge Case Categories

| Category | Examples |
|----------|----------|
| Boundary | 0, 1, max, min, empty |
| Input | null, undefined, wrong type |
| State | uninitialized, concurrent, stale |
| Resource | timeout, no memory, disk full |
| Network | offline, slow, partial failure |
| Permission | unauthorized, expired, revoked |

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

- Happy path only
- Ignoring nulls
- Assuming valid input
- Missing timeout handling
- Silent failures

