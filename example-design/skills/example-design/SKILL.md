---
name: example-design
description: >-
  Design pedagogically effective code examples, tutorials, and runnable samples using
  progressive complexity and deliberate scaffolding. Use when the user asks to write a
  code example that teaches a concept, design a quickstart tutorial, create sample code
  for a library or API, build a runnable demo, or structure examples from simple to
  advanced. NOT for generating full repo documentation or READMEs (use
  documentation-generator). NOT for writing examples inside a skill file (use
  skill-foundry). NOT for API endpoint design (use api-design).
---

# Example Design

Create code examples that teach effectively through progressive complexity.

## Decision Tree: Which Example Type?

```
What does the user need?
├─ Show a single concept → Snippet (5-15 lines)
├─ Working code for a feature → Complete example (20-50 lines)
├─ Step-by-step teaching → Tutorial (multi-file, progressive)
└─ Reference for production use → Reference app (full project)
```

## Example Types

| Type | Purpose | Length | When to Use |
|------|---------|--------|-------------|
| Snippet | Single concept | 5-15 lines | Quick reference, API parameter demo |
| Complete example | Working code | 20-50 lines | Feature walkthrough, integration demo |
| Tutorial | Step-by-step | Multi-file | Onboarding, learning path |
| Reference app | Production patterns | Full project | Architecture reference, starter template |

## Progressive Complexity

```
Level 1: Minimal (happy path)
   ↓
Level 2: Add configuration
   ↓
Level 3: Add error handling
   ↓
Level 4: Add edge cases
   ↓
Level 5: Production-ready
```

Each level must be runnable independently. Never skip a level — the reader needs the progression to build understanding incrementally.

## Example Anatomy

```python
# 1. Context: What this does
"""Fetch user data from API"""

# 2. Setup: Prerequisites
import requests

# 3. Core: Main concept (highlight this)
response = requests.get("/users/123")  # <-- Key line
user = response.json()

# 4. Result: Expected output
print(user["name"])  # Output: "Alice"
```

## Quality Checklist

- [ ] **Runnable**: Copy-paste works without modifications
- [ ] **Complete**: All imports included, no hidden dependencies
- [ ] **Minimal**: No unrelated code, no ceremonial boilerplate
- [ ] **Commented**: Key lines explained, not every line
- [ ] **Realistic**: Uses real-world names, URLs, and patterns
- [ ] **Tested**: Verified working before publishing

## Tutorial Structure

```markdown
## Tutorial: [Goal]

**Time**: 10 min | **Level**: Beginner

### What you'll build
[Screenshot/description]

### Prerequisites
- [requirement 1]
- [requirement 2]

### Step 1: [Action]
[Explanation]
[Code]
[Expected result]

### Step 2: [Action]
...

### Next steps
- [Related tutorial]
- [Advanced topic]
```

## Anti-Patterns

- **Foo/bar variables** — use realistic names that convey domain meaning; `customerName` teaches more than `foo`
- **Missing imports** — if the reader cannot copy-paste and run, the example fails its purpose
- **Outdated syntax** — examples lag behind API changes faster than any other documentation; verify against current version
- **No expected output** — the reader cannot verify their result is correct without seeing what success looks like
- **Untested code** — untested examples are wrong examples; always run before publishing
- **Wall of code with no explanation** — code without context is a source listing, not a teaching tool
- **Showing only the happy path** — real usage hits errors; show what happens when things go wrong (at least in progressive Level 3+)
- **Over-abstracted examples** — wrapping the concept in 3 layers of indirection obscures the point; keep the example direct

## When to Use

- Creating API reference examples for each endpoint
- Building quickstart guides for a library or framework
- Writing runnable demos for a product feature
- Designing tutorial sequences for onboarding
