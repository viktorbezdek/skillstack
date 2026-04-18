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

Create intuitive wayfinding systems for content and applications. Navigation design determines whether users find what they need or abandon in frustration. Good navigation is invisible; bad navigation is the #1 complaint on support channels.

## When to Use

- Designing site-wide navigation (top nav, sidebar, footer)
- Planning a sitemap or information architecture
- Structuring sidebar menus for documentation
- Designing breadcrumb systems
- Organizing content hierarchy and categorization
- Evaluating whether current navigation is working (analytics, user feedback)

## When NOT to Use

- Mapping user journeys across touchpoints over time (use user-journey-design)
- Writing navigation labels, microcopy, or button text (use ux-writing)
- Implementing Next.js routing, layouts, or parallel routes (use nextjs-development)
- Designing visual styling of navigation components (use frontend-design)

## Decision Tree

```
What navigation problem are you solving?
│
├─ Structuring a new site/app
│  ├─ Broad, shallow content? → Flat IA + global nav
│  ├─ Deep, hierarchical content? → Tree IA + sidebar nav
│  ├─ Hub-and-spoke workflow? → Hub IA + contextual nav
│  └─ Multi-dimensional content? → Faceted IA + filter nav
│
├─ Improving existing navigation
│  ├─ Users can't find content? → Audit with 3-click rule + card sorting
│  ├─ Too many top-level items? → Consolidate to 7±2; use progressive disclosure
│  ├─ Users get lost in deep pages? → Add breadcrumbs + contextual nav
│  └─ Navigation inconsistent across pages? → Establish nav patterns + audit
│
├─ Choosing navigation type
│  ├─ Site-wide access needed? → Global nav (top bar, sidebar)
│  ├─ Section-specific links? → Local nav (sub-menu, tabs)
│  ├─ In-content references? → Contextual nav (related articles, see-also)
│  ├─ Tools/settings/access? → Utility nav (search, login, settings)
│  └─ Location orientation? → Breadcrumbs
│
└─ Navigation for specific platforms
   ├─ Documentation site? → Sidebar + search + breadcrumbs
   ├─ SaaS application? → Top nav + sidebar + command palette
   ├─ Marketing site? → Top nav + mega-menu + footer
   └─ Mobile app? → Bottom tab bar + hamburger for overflow
```

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
Best for: Content with natural parent-child relationships. Most common pattern.

### Hub and Spoke
Central hub with satellite pages, return to hub.
Best for: Workflow-driven apps where users complete a task and return to a dashboard.

### Flat
Few levels, broad categories.
Best for: Small sites (<30 pages), single-product landing pages.

### Faceted
Multiple classification dimensions (filter + sort).
Best for: E-commerce, directories, content libraries where users browse by different attributes.

## Navigation Rules

| Rule | Description |
|------|-------------|
| 7 +/- 2 | Limit top-level items |
| 3-click | Reach any page in 3 clicks |
| Recognition > Recall | Show options, don't require memory |
| Consistency | Same nav across pages |
| Progressive disclosure | Show relevant options at each level; hide deeper ones |
| Current location | Always indicate where the user is |

## Breadcrumb Template

```
Home > [Category] > [Subcategory] > Current Page
```

Clickable except current page. Use for any site deeper than 2 levels.

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

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Mystery meat navigation | Icons/labels that don't communicate destination | Use descriptive text labels; test with 5-second recognition test |
| Too many levels (deep nesting) | Users lose context; high abandonment | Flatten to max 3 levels; use hub-and-spoke for deep content |
| Inconsistent placement | Nav moves between pages, disorienting users | Lock navigation position; audit every page for consistency |
| Missing current location indicator | Users don't know where they are | Highlight active item; add breadcrumbs for deep pages |
| Mega-menu without grouping | 50+ links in a dropdown overwhelms | Group into 3-5 categories with clear headings; use progressive disclosure |
| Navigation depends on hover | Touch devices and accessibility fail | All nav must work with click/tap; hover is enhancement only |
| Hidden navigation (hamburger everywhere) | Discoverability drops; users don't explore | Show top-level items visibly; use hamburger only for overflow on mobile |
| Orphan pages (no nav back) | Users land on a page with no way out | Every page must have at least: global nav + breadcrumb + link to parent |
| Inconsistent labeling | Same section called different things in different contexts | Create a naming glossary; use the same label everywhere |
| Search as only navigation | Users who don't know the right term can't find content | Search supplements navigation; never replaces it |

## Related Skills

- **user-journey-design** — Map how users flow through touchpoints over time (not spatial navigation)
- **ux-writing** — Write the labels, tooltips, and microcopy for navigation
- **content-modelling** — Define the content types that populate navigation structures
- **nextjs-development** — Implement Next.js routing, layouts, and parallel routes
