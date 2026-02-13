---
name: example-design
description: Design effective code examples, tutorials, and runnable samples with progressive complexity.
triggers:
  - code examples
  - tutorials
  - quickstart
  - sample code
  - runnable examples
  - progressive disclosure
---

# Example Design

Create code examples that teach effectively through progressive complexity.

## Example Types

| Type | Purpose | Length |
|------|---------|--------|
| Snippet | Single concept | 5-15 lines |
| Complete example | Working code | 20-50 lines |
| Tutorial | Step-by-step | Multi-file |
| Reference app | Production patterns | Full project |

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

- [ ] **Runnable**: Copy-paste works
- [ ] **Complete**: All imports included
- [ ] **Minimal**: No unrelated code
- [ ] **Commented**: Key lines explained
- [ ] **Realistic**: Uses real-world patterns
- [ ] **Tested**: Verified working

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

- Foo/bar variables (use realistic names)
- Missing imports
- Outdated syntax
- No expected output
- Untested code
- Wall of code (no explanation)

