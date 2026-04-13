# Additional Resources

## Templates

All templates include:
- Pre-structured SKILL.md with frontmatter
- Appropriate directory structure
- Example files demonstrating patterns
- Template-specific README with guidance

## Validation Scripts

**validate_skill.py** - Comprehensive skill validation:
- Frontmatter format and constraints
- Naming conventions
- Description quality
- Progressive disclosure
- Writing style
- Resource organization
- File references
- **Phase 2 enhancements:**
  - Conciseness (verbose patterns detection)
  - Degrees of freedom consistency
  - Script error handling quality
  - Evaluation references (EDD)

**analyze_conciseness.py** - Token usage analysis:
- Section-by-section token counts
- Verbosity pattern detection
- Actionable improvement suggestions
- Overall conciseness assessment

## Pattern Library

Common patterns extracted from high-quality skills:
- Progressive Disclosure
- Bundled Scripts
- Validation Loop
- Template Assets
- Domain Organization

## Example Skills

Learn from working examples in `examples/`:
- `document-skills/pdf/` - Document processing
- `mcp-builder/` - API integration
- `analyzing-financial-statements/` - Analysis workflow
- `applying-brand-guidelines/` - Reference/guidelines

## Quick Commands

```bash
# Initialize with template
python scripts/init_skill.py <name> --template <type> --path <dir>

# Analyze conciseness (Phase 2 enhancement)
python scripts/analyze_conciseness.py <skill-dir>

# Validate during development (includes Phase 2 checks)
python scripts/validate_skill.py --check-content <skill-dir>

# Full pre-package validation (all Phase 2 checks)
python scripts/validate_skill.py --full-check <skill-dir>

# Package for distribution
python scripts/package_skill.py <skill-dir> [output-dir]
```

**Phase 2 Validation Enhancements:**
- Conciseness analysis (verbose patterns, token counts by section)
- Degrees of freedom consistency (high/medium/low markers)
- Script error handling quality ("solve don't punt" pattern)
- Evaluation references (EDD test scenarios)

## Resources

- **Evaluation-Driven Development**: `references/evaluation_driven_development.md`
- **Degrees of Freedom**: `references/degrees_of_freedom.md`
- **Best Practices Checklist**: `references/best_practices_checklist.md`
- **Pattern Library**: `references/patterns.md`
- **Cookbook Patterns**: `references/cookbook_patterns.md`
- **Examples**: `examples/` directory

## Navigation

- [Back to main SKILL.md](../SKILL.md)
- [Core Principles](core_principles.md)
- [Evaluation-Driven Development](evaluation_driven_development.md)
