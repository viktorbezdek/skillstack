---
name: consistency-standards
description: >-
  Establish and enforce uniform naming conventions, taxonomy standards, style guides, and
  content reuse patterns across a project. Use when the user asks to audit for consistency,
  standardize naming, create a style guide, align terminology across docs, eliminate drift,
  or define reuse patterns across content or code. NOT for formal knowledge graphs or semantic
  ontologies (use ontology-design). NOT for CMS content types or editorial workflows
  (use content-modelling). NOT for language-specific code conventions (use typescript-development
  or python-development).
---

# Consistency Standards

Establish uniform patterns for naming, terminology, and content reuse.

## When to Use / Not Use

**Use when:**
- Establishing naming conventions for a new project
- Auditing existing code or docs for consistency issues
- Creating a terminology glossary to standardize vocabulary
- Defining voice and tone guidelines for different content types
- Designing content reuse strategies (DRY documentation)
- Onboarding new team members with style standards

**Do NOT use when:**
- Formal ontology or semantic modeling -> use `ontology-design`
- Content type and CMS schema design -> use `content-modelling`
- Writing the actual documentation content -> use `documentation-generator`

## Decision Tree

```
What are you standardizing?
├── How things are NAMED (variables, files, endpoints, columns)
│   ├── Single language? -> Case style guide (§Naming Conventions)
│   └── Multi-language stack? -> Per-context rules + mapping between layers (§Naming Conventions)
├── How things are CALLED (terminology, synonyms, product names)
│   └── Multiple terms for same concept? -> Glossary with preferred + forbidden terms (§Terminology)
├── How things SOUND (voice, tone, formality)
│   └── Different contexts need different voices? -> Per-context voice rules (§Voice and Tone)
├── How content is REUSED (repeated sections across docs)
│   └── Same content in 3+ places? -> Snippets/variables/conditionals (§Content Reuse)
└── Not sure / combination? -> Start with audit (§Style Checklist)
```

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

### Cross-Layer Mapping Rules

When a stack has multiple languages, define how names map between layers:

| Layer | Convention | Example |
|-------|-----------|---------|
| Database column | snake_case | `user_name` |
| API response field | camelCase | `userName` |
| Frontend variable | camelCase | `userName` |
| URL path segment | kebab-case | `/user-profile` |
| File name | kebab-case | `user-profile.tsx` |

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

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Synonym sprawl | Multiple terms for same concept ("user"/"account"/"member") | Create glossary with one preferred term + explicit "Do Not Use" list |
| Inconsistent capitalization | Feature names capitalized randomly | Define rule: capitalize only proper nouns and product names |
| Mixed voice | "you should"/"the user must"/"we recommend" in same doc | Per-context voice guide: instructions=direct active, errors=helpful, success=brief |
| Orphaned content | Outdated references to renamed features | Audit checklist: search for forbidden terms, add to CI lint step |
| Standards without enforcement | Glossary exists but nobody follows it | Add lint rules (ESLint, Ruff) + PR review checklist + automated docs linting |
| Over-standardizing | Rule for every possible variation | Focus only on inconsistencies causing real confusion or maintenance cost |
| Page-based reuse | Same content copy-pasted into 8 documents | Single-source snippet with `{{> shared/section.md}}` includes |
