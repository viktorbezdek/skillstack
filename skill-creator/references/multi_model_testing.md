# Multi-Model Testing Protocol

Test skill with all Claude models to ensure broad compatibility:

## Claude Haiku Testing
**Question**: Does the skill provide enough guidance?

Test for:
- [ ] Haiku doesn't ask unnecessary questions
- [ ] Instructions are clear enough for smaller model
- [ ] Examples are sufficient
- [ ] No ambiguity in requirements

**If Haiku struggles**: Add more examples, clarify ambiguous instructions

## Claude Sonnet Testing
**Question**: Is the skill clear and efficient?

Test for:
- [ ] Sonnet completes tasks smoothly
- [ ] No excessive back-and-forth
- [ ] Token usage is reasonable
- [ ] Performance is optimal

**If Sonnet struggles**: Typical target model, indicates core issues

## Claude Opus Testing
**Question**: Does the skill avoid over-explaining?

Test for:
- [ ] Opus isn't slowed by verbose instructions
- [ ] No patronizing or obvious guidance
- [ ] Opus can skip to advanced features
- [ ] Instructions don't constrain capabilities

**If Opus feels constrained**: Reduce verbosity, increase freedom

## Testing Checklist

- [ ] All test scenarios from Step 1.5 pass
- [ ] Tested with Haiku (sufficient guidance?)
- [ ] Tested with Sonnet (efficient?)
- [ ] Tested with Opus (not over-explained?)
- [ ] Success rate > 90% across all models
- [ ] Avg completion time acceptable
- [ ] No repeated questions or confusion
- [ ] Documented any model-specific notes

## Model-Specific Notes Example

```markdown
## Model Compatibility

- **Haiku**: May need explicit "Use pdfplumber" reminder
- **Sonnet**: Optimal performance, no issues
- **Opus**: Can infer best approach, explicit reminders optional
```

## Iteration Workflow

1. Use the skill on real tasks
2. Notice struggles or inefficiencies
3. Identify how SKILL.md or bundled resources should be updated
4. Implement changes and test again
5. Validate improvements with validation script

## Quality Checkpoint ✓

After each iteration:

- [ ] Tested skill with 3+ realistic scenarios
- [ ] Validated all feedback from testing
- [ ] Re-ran validation after improvements
- [ ] Documented learnings (in README or changelog)
- [ ] Verified improvements don't introduce new issues

**Validation:** Run `python scripts/validate_skill.py --full-check <skill-dir>` after changes

**Continue iterating until the skill performs well across all test scenarios.**

## Navigation

- [Back to main SKILL.md](../SKILL.md)
- [Evaluation-Driven Development](evaluation_driven_development.md)
- [Core Principles](core_principles.md)
