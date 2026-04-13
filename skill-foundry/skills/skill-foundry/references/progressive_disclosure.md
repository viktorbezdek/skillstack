# Progressive Disclosure Guidelines

**Guideline**: If SKILL.md exceeds ~300 lines, move details to references/

## When to Use Progressive Disclosure

**Target**: Keep SKILL.md under 300 lines for main workflow

**When to use references/**:
- ✅ API documentation (detailed specs)
- ✅ Extended examples (>5 examples)
- ✅ Technical deep-dives (implementation details)
- ✅ Advanced patterns (edge cases)

**Keep in SKILL.md**:
- ✅ Main workflow (numbered steps)
- ✅ Common scenarios (2-3 examples)
- ✅ Quick reference (high-level)
- ✅ Decision trees (choosing approach)

**Rule of thumb**: If section exceeds 50 lines → move to references/

## How to Create References

1. **Copy template**:
   ```bash
   cp templates/skill-skeleton/references/reference-template.md \
      references/my-topic.md
   ```

2. **Move content** from SKILL.md to reference file

3. **Link from SKILL.md**:
   ```markdown
   For complete API reference, see [API Reference](references/api-reference.md).
   ```

4. **Validate**:
   ```bash
   python scripts/analyze_conciseness.py <skill-dir>
   # Target: SKILL.md < 3000 tokens
   ```

## Benefits

- Faster loading for Claude (less context)
- Easier navigation (focused main file)
- Details available when needed
- Better token efficiency

## Progressive Disclosure Design Principle

Skills use a three-level loading system to manage context efficiently:

1. **Metadata (name + description)** - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<500 lines recommended)
3. **Bundled resources** - As needed by Claude (Unlimited*)

*Unlimited because scripts can be executed without reading into context window.

## Navigation

- [Back to main SKILL.md](../SKILL.md)
- [Editing Guidance](editing_guidance.md)
- [Core Principles](core_principles.md)
