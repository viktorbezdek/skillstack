---
name: navigation-design
description: >-
  Design information architecture, wayfinding systems, and navigation structures for
  documentation sites and applications. Use when the user asks to design navigation,
  plan a sitemap, structure a sidebar or menu, define content hierarchy, design breadcrumbs,
  or organize how users move through content. NOT for user journey maps or touchpoint
  flows across time (use user-journey-design). NOT for microcopy, labels, or button
  text in navigation (use ux-writing). NOT for Next.js routing, layouts, or parallel
  routes (use nextjs-development).
---

# Navigation Design

Create intuitive wayfinding systems for content and applications.

## Navigation Types

| Type | Use Case | Example |
|------|----------|---------|
| Global | Site-wide access | Top nav, sidebar |
| Local | Section-specific | Sub-menu |
| Contextual | In-content links | Related articles |
| Utility | Tools/settings | Search, login |
| Breadcrumb | Location trail | Home > Docs > API |

## Information Architecture Patterns

### Hierarchy (Tree)
```
Home
├── Products
│   ├── Category A
│   └── Category B
├── Docs
│   ├── Getting Started
│   └── Reference
└── Support
```

### Hub and Spoke
Central hub with satellite pages, return to hub.

### Flat
Few levels, broad categories.

### Faceted
Multiple classification dimensions (filter + sort).

## Navigation Rules

| Rule | Description |
|------|-------------|
| 7 +/- 2 | Limit top-level items |
| 3-click | Reach any page in 3 clicks |
| Recognition > Recall | Show options, don't require memory |
| Consistency | Same nav across pages |

## Breadcrumb Template

```
Home > [Category] > [Subcategory] > Current Page
```

Clickable except current page.

## Sitemap Template

```markdown
## Sitemap: [Product]

### Primary Navigation
1. Home
2. Features
   - Feature A
   - Feature B
3. Documentation
   - Quick Start
   - Tutorials
   - API Reference
4. Pricing

### Utility Navigation
- Search
- Login/Signup
- Help
```

## Anti-Patterns

- Mystery meat navigation (unclear labels)
- Too many levels (deep nesting)
- Inconsistent placement
- Missing current location indicator

