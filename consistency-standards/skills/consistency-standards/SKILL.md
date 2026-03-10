---
name: consistency-standards
description: >-
  Establish and maintain uniform naming conventions, taxonomy standards, style guides,
  and content reuse patterns across documentation and code. Use when working with naming
  conventions, style guides, taxonomy, terminology, content reuse, or consistency audits.
---

# Consistency Standards

Establish uniform patterns for naming, terminology, and content reuse.

## Naming Conventions

### Case Styles

| Style | Example | Use For |
|-------|---------|---------|
| camelCase | getUserName | JS variables, methods |
| PascalCase | UserProfile | Classes, components |
| snake_case | user_name | Python, databases |
| kebab-case | user-profile | URLs, CSS classes |
| SCREAMING_SNAKE | MAX_RETRIES | Constants |

### File Naming

```
[type]-[name]-[variant].[ext]
component-button-primary.tsx
doc-api-reference.md
```

## Terminology Standards

### Glossary Template

```markdown
| Term | Definition | Do Not Use |
|------|------------|------------|
| click | Select with mouse | press, hit |
| select | Choose from options | pick, click on |
| enter | Type in field | input, write |
```

### Voice and Tone

| Context | Voice | Example |
|---------|-------|---------|
| Instructions | Direct, active | "Click Save" |
| Errors | Helpful, calm | "Let's fix this" |
| Success | Positive, brief | "Done!" |

## Content Reuse Patterns

### Single-Source Components

| Pattern | Use Case |
|---------|----------|
| Snippet | Reusable text block |
| Variable | Product name, version |
| Conditional | Audience-specific content |
| Template | Structured format |

### DRY Documentation

```markdown
<!-- Include shared content -->
{{> shared/authentication.md}}

<!-- Use variables -->
Install {{product_name}} v{{version}}
```

## Style Checklist

- [ ] Consistent capitalization
- [ ] Uniform date/time formats
- [ ] Standardized UI element names
- [ ] Single voice throughout
- [ ] Glossary terms used correctly
- [ ] Code style matches project

## Anti-Patterns

- Synonym sprawl (multiple terms for same concept)
- Inconsistent capitalization
- Mixed voice (you/we/user)
- Orphaned content (outdated references)

