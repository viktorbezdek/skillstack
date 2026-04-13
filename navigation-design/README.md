# Navigation Design

> **v1.0.10** | Design & UX | 11 iterations

---

## The Problem

Users abandon products when they cannot find what they need. A documentation site with hundreds of pages and no clear hierarchy forces readers to search randomly or give up. An application with inconsistent navigation -- sidebar on one page, top nav on another, breadcrumbs that disappear in subsections -- destroys users' sense of location. Teams building these systems rarely design information architecture intentionally; they add pages and menu items ad hoc until the structure becomes an unmaintainable maze.

The consequences are measurable. Support tickets spike for features that exist but are buried three levels deep. Onboarding completion drops because new users cannot find the "Getting Started" guide. Developer documentation gets duplicated across sections because the taxonomy has no principled structure. Redesigns fail because they rearrange the deck chairs without addressing the underlying information architecture -- the same content in a new layout is still disorganized content.

Without a systematic approach to navigation design, teams repeat the same mistakes: too many top-level items (violating the 7 +/- 2 rule), deep nesting that requires five clicks to reach common pages, mystery-meat navigation with labels that make sense internally but confuse users, and missing location indicators that leave users disoriented within the hierarchy.

## The Solution

The Navigation Design plugin gives Claude expertise in information architecture, wayfinding systems, and navigation patterns for both documentation sites and applications. It covers the five navigation types (global, local, contextual, utility, breadcrumb), four information architecture patterns (hierarchy, hub-and-spoke, flat, faceted), navigation rules grounded in cognitive science, and ready-to-use templates for breadcrumbs and sitemaps.

The plugin provides a single, focused skill that activates when you need to organize content, design menu structures, create sitemaps, implement breadcrumbs, or restructure an existing navigation system. It applies recognition-over-recall principles, the 3-click rule for content reachability, and the 7 +/- 2 rule for cognitive load management -- giving you principled constraints rather than arbitrary choices.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Menu items added ad hoc as pages are created, resulting in flat or chaotic hierarchy | Information architecture designed intentionally using hierarchy, hub-and-spoke, flat, or faceted patterns |
| Users lose their location within the site -- no breadcrumbs, no active-state indicators | Breadcrumb templates and location indicators that maintain spatial orientation |
| Top navigation with 15+ items overwhelming users | 7 +/- 2 rule enforced for top-level items with principled grouping |
| Common pages buried 5+ clicks deep in nested menus | 3-click rule applied: any page reachable within 3 navigation actions |
| Inconsistent navigation placement across sections | Consistency rules: same navigation structure and placement across all pages |
| Sitemap is an afterthought or missing entirely | Structured sitemap template with primary and utility navigation separation |

## Installation

Add the marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install navigation-design@skillstack
```

### Prerequisites

None. For content organization within pages, also consider `content-modelling`. For user journey context that informs navigation priority, also consider `user-journey-design`.

### Verify installation

After installing, test with:

```
Help me design the navigation structure for a developer documentation site with API reference, tutorials, and guides
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `I need to restructure the navigation for our docs site -- it has 200 pages and users can't find anything`
3. The skill analyzes your content scope and recommends an information architecture pattern (hierarchy, hub-and-spoke, flat, or faceted)
4. You receive a sitemap template with primary and utility navigation, organized by the chosen pattern
5. Next, try: `Design breadcrumbs for a nested product catalog with categories, subcategories, and product pages`

---

## System Overview

```
navigation-design/
├── .claude-plugin/
│   └── plugin.json            # Plugin manifest
└── skills/
    └── navigation-design/
        ├── SKILL.md           # Core skill (navigation types, IA patterns, rules, templates)
        └── evals/
            ├── trigger-evals.json   # 13 trigger evaluation cases
            └── evals.json           # 3 output evaluation cases
```

A single skill with no additional references -- the SKILL.md contains the complete navigation design framework including navigation types, information architecture patterns, design rules, templates, and anti-patterns.

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `navigation-design` | Skill | Navigation types, information architecture patterns, design rules, breadcrumb/sitemap templates |

### Component Spotlight

#### navigation-design (skill)

**What it does:** Activates when you need to design or restructure navigation for documentation sites or applications. Provides five navigation types, four information architecture patterns, cognitive-science-grounded design rules, and ready-to-use templates for breadcrumbs and sitemaps.

**Input -> Output:** A description of your content scope and user needs (site size, content types, user goals) -> A navigation structure with IA pattern selection, sitemap, breadcrumb design, and menu hierarchy.

**When to use:**
- Designing navigation for a new documentation site or application
- Restructuring an existing site where users cannot find content
- Creating sitemaps for content planning
- Implementing breadcrumb trails for deep content hierarchies
- Deciding between navigation patterns (global vs local vs contextual)

**When NOT to use:**
- CMS content modeling or editorial workflows (use `content-modelling`)
- Visual UI design or CSS styling (use `frontend-design`)
- User journey mapping across touchpoints (use `user-journey-design`)
- UX copywriting for navigation labels (use `ux-writing`)

**Try these prompts:**

```
Design the information architecture for a SaaS product with dashboard, settings, team management, billing, and API docs
```

```
Our documentation site has 300 pages across 8 product areas -- help me create a hierarchy that users can navigate in 3 clicks or fewer
```

```
What navigation pattern works best for a faceted product catalog where users filter by category, price, and features?
```

```
Review our current sitemap -- we have 12 top-level items and users report feeling overwhelmed
```

```
Design breadcrumbs for a multi-level help center: product > category > article, with cross-linking between related articles
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Help with my website" | "Design the navigation structure for a developer portal with API docs, SDKs, tutorials, and a changelog" |
| "Fix my menu" | "Our top nav has 14 items and users report feeling lost -- help me consolidate into a clearer hierarchy" |
| "I need breadcrumbs" | "Design breadcrumbs for a 4-level deep product catalog: Home > Department > Category > Product" |
| "Make navigation better" | "Should I use hub-and-spoke or hierarchical IA for a knowledge base with 50 articles across 6 topics?" |

### Structured Prompt Templates

**For new site architecture:**
```
Design the navigation for [site/app type] with these content areas: [list sections]. Primary users are [user type] who need to [primary goal]. The site has approximately [N] pages.
```

**For restructuring existing navigation:**
```
Our [site/app] currently has [N] top-level items: [list items]. Users report [specific problem: can't find X, too many clicks to Y, confusion between Z and W]. Help me restructure.
```

**For breadcrumb design:**
```
Design breadcrumbs for [content structure]. The hierarchy is [levels]. Cross-linking is needed between [related content types].
```

### Prompt Anti-Patterns

- **Asking for navigation without describing content** -- the skill needs to know what content exists before it can organize it; provide a content inventory or at least a rough scope
- **Focusing on visual design instead of structure** -- "make the nav look modern" is a visual design request; ask about information architecture, hierarchy, and wayfinding instead
- **Requesting a sitemap for a single page** -- the skill is designed for multi-page structures; for single-page layout, use `frontend-design`

## Real-World Walkthrough

**Starting situation:** You are redesigning the documentation site for a developer platform. The site has grown organically to 250 pages covering API reference (80 pages), tutorials (40 pages), SDK guides for 5 languages (50 pages), integration guides (30 pages), a changelog (20 pages), and conceptual guides (30 pages). Users report three pain points: they cannot find the right SDK guide from the main nav, tutorials and conceptual guides overlap in confusing ways, and the API reference has no way to navigate between related endpoints.

**Step 1: Information architecture assessment.** You ask: "Help me restructure navigation for our developer docs -- 250 pages, 6 content areas. Users can't find SDK guides and confuse tutorials with conceptual guides."

The skill identifies this as a hierarchical IA problem with faceted elements. The primary structure should be a tree (products > sections > pages), but API reference needs faceted navigation (filter by resource type, HTTP method, authentication level). The skill recommends consolidating tutorials and conceptual guides into a single "Learning" section with progressive complexity (quickstart > tutorials > deep dives).

**Step 2: Top-level navigation design.** The skill applies the 7 +/- 2 rule. Current: 8 top-level items (Home, API Reference, Tutorials, Concepts, SDKs, Integrations, Changelog, Blog). Recommended: 5 top-level items -- Home, Learn (merged tutorials + concepts), Build (API reference + SDKs + integrations), Changelog, Blog. This groups by user intent (learning vs building) rather than content type.

**Step 3: Local navigation for the Build section.** Within "Build," the skill designs local navigation: a persistent sidebar showing API Reference, SDKs (with language sub-items), and Integrations (with service sub-items). The SDK section uses tabs for language selection so users switch languages without losing their place in the concept hierarchy.

**Step 4: Breadcrumb implementation.** The skill provides the breadcrumb pattern: Home > Build > API Reference > Users > Create User. Each segment is clickable except the current page. For SDK guides: Home > Build > SDKs > Python > Authentication. Cross-links between API reference endpoints and SDK examples use contextual navigation (inline "See this in Python" links) rather than breadcrumb branches.

**Step 5: Utility navigation.** The skill adds utility navigation separate from primary: Search (global, always visible), Version selector (documentation version), Status page link, and Support. These sit in a distinct visual zone from the primary navigation.

**Step 6: Anti-pattern review.** The skill checks the design against its anti-pattern list: no mystery-meat navigation (all labels are descriptive), no deep nesting (maximum 4 levels: Home > Build > SDKs > Python > topic), consistent placement (sidebar on all Build pages, top nav on all pages), and current location indicator (active states on both breadcrumb and sidebar).

**Final outcome:** A restructured 5-item top navigation, two-section local nav (Learn / Build), breadcrumbs for all pages, contextual cross-linking between related content, and utility navigation separated from primary structure. The 250 pages are organized into a hierarchy reachable within 3 clicks from the home page.

**Gotchas discovered:** The skill identified that merging tutorials and concepts requires a progressive complexity model within the "Learn" section -- quickstart (5 min), tutorials (30 min), deep dives (reference-level). Without this progression, the merged section would feel disorganized.

## Usage Scenarios

### Scenario 1: SaaS application navigation

**Context:** You are building a B2B SaaS product with dashboard, projects, team management, billing, settings, and an API for integrations. The product serves both admin users and regular team members.

**You say:** "Design the navigation for a B2B SaaS app with dashboard, projects, team management, billing, settings, and API. Admin and regular users have different access levels."

**The skill provides:**
- Global navigation with role-based visibility (admin sees billing/team management, regular users see dashboard/projects)
- Local navigation within each section (project list > project detail > project settings)
- Utility navigation for user profile, notifications, and help
- Breadcrumb pattern for project hierarchy: Projects > Project Name > Settings

**You end up with:** A complete navigation architecture with role-based access, consistent sidebar across sections, and breadcrumbs for deep pages.

### Scenario 2: E-commerce product catalog

**Context:** You have a product catalog with 500+ products across 12 categories, each with subcategories. Users need to browse by category and filter by attributes (price, rating, availability).

**You say:** "What navigation pattern works for a product catalog with 500 items, 12 categories, and faceted filtering by price, rating, and availability?"

**The skill provides:**
- Faceted IA pattern recommendation: category hierarchy for browsing, faceted filters for refinement
- Global nav with mega-menu showing all 12 categories and their top subcategories
- Local faceted sidebar with filter controls that persist during browsing
- Breadcrumbs: Home > Category > Subcategory with active filter indicators

**You end up with:** A dual navigation approach combining hierarchical browsing with faceted filtering, giving users both exploration and precision paths.

### Scenario 3: Restructuring an overwhelmed navigation

**Context:** Your company wiki has grown to 15 top-level sections and 800 pages. New employees report spending 30 minutes trying to find onboarding documentation.

**You say:** "Our wiki has 15 top-level sections and 800 pages. New hires can't find onboarding docs. Help me restructure."

**The skill provides:**
- Audit against the 7 +/- 2 rule (15 items is nearly double the recommended maximum)
- Hub-and-spoke IA for the wiki: central hub page per department with spoke pages for topics
- Consolidated top-level: 6 items (Company, Engineering, Product, Design, Operations, Onboarding)
- Dedicated onboarding path with sequential navigation (Step 1 > Step 2 > Step 3)

**You end up with:** A restructured wiki with 6 top-level items, hub-and-spoke architecture per section, and a sequential onboarding path that new hires can follow without getting lost.

---

## Decision Logic

**Which information architecture pattern to use?**

- **Hierarchy (tree)** -- content has clear parent-child relationships, users think in categories. Most documentation sites, product documentation. Default choice when unsure.
- **Hub and spoke** -- users start from a central point and explore topics independently. Wikis, knowledge bases, learning portals. Good when topics are self-contained.
- **Flat** -- few content pages, broad categories, everything reachable from one level. Small sites, single-product landing pages. Only works at small scale.
- **Faceted** -- content has multiple classification dimensions (category AND price AND rating). Product catalogs, search-heavy applications. Requires more UI complexity.

**When to combine patterns?**

Most real systems combine patterns. A developer portal might use hierarchy for documentation (tree of pages), faceted for API reference (filter by resource, method), and hub-and-spoke for tutorials (central learning hub with independent tutorials). The skill helps you identify which pattern fits each section.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Too many top-level items | Users report feeling overwhelmed, low click-through on lower items | Apply 7 +/- 2 rule; group by user intent rather than content type |
| Deep nesting | Users take 5+ clicks to reach common content, high bounce rate | Apply 3-click rule; flatten hierarchy by promoting frequently accessed pages |
| Mystery-meat navigation | Users don't understand menu labels, click wrong items | Replace internal jargon with task-oriented labels ("Get Started" not "Onboarding Pipeline") |
| Inconsistent navigation | Users report confusion when moving between sections | Audit for consistent placement, structure, and behavior across all pages |
| Missing breadcrumbs | Users lose their location in deep hierarchies, use browser back button excessively | Add breadcrumb trail with clickable segments (except current page) |

## Ideal For

- **Documentation teams** organizing large content libraries into navigable hierarchies with clear wayfinding
- **Product designers** structuring application navigation for SaaS products with multiple feature areas and user roles
- **Frontend developers** implementing breadcrumbs, sitemaps, and menu systems with principled design constraints
- **Content strategists** planning information architecture before content creation begins
- **Teams redesigning** sites where user complaints about "can't find things" are the primary pain point

## Not For

- **CMS content modeling** -- defining content types, fields, and editorial workflows uses `content-modelling`
- **Visual navigation styling** -- CSS, animations, and visual design of navigation components uses `frontend-design`
- **User journey mapping** -- mapping touchpoints across the entire user experience uses `user-journey-design`

## Related Plugins

- **content-modelling** -- structuring the content that navigation organizes
- **user-journey-design** -- understanding user flows that inform navigation priority
- **ux-writing** -- writing clear, task-oriented navigation labels
- **frontend-design** -- visual implementation of navigation components
- **consistency-standards** -- maintaining uniform navigation patterns across a product

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
