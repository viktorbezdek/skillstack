# Navigation Design

> **v1.0.10** | Design & UX | 11 iterations

> Design information architecture, wayfinding systems, and navigation patterns that help users find what they need without thinking about the navigation itself.

## The Problem

Users leave applications and documentation sites not because the content is bad, but because they cannot find it. Navigation failures are silent -- there is no error message when someone gives up looking for a feature buried three levels deep in a menu they never noticed. Teams build navigation by mirroring their internal org structure ("Engineering docs go under Engineering") rather than how users actually think about tasks.

The symptoms are predictable: mystery meat navigation where icons and labels mean nothing to newcomers, deep nesting that violates the 3-click rule and buries critical pages, inconsistent placement where the nav changes layout between sections, and missing location indicators that leave users disoriented. These are not aesthetic problems -- they directly increase support tickets, reduce feature adoption, and inflate bounce rates on documentation sites.

Most teams design navigation last, after all the content exists, treating it as a cosmetic layer rather than a structural decision. By then, the information architecture is already implicitly defined by the content hierarchy, and restructuring it means restructuring everything. Getting navigation right early -- with proper IA patterns, breadcrumb trails, and sitemap planning -- saves weeks of rework later.

## The Solution

This plugin provides a systematic approach to navigation design built on established information architecture patterns. It gives you a taxonomy of navigation types (global, local, contextual, utility, breadcrumb) with clear use cases for each, four IA patterns (hierarchy, hub-and-spoke, flat, faceted) with decision criteria, and concrete rules like the 7 +/- 2 item limit and 3-click depth constraint.

You get ready-to-use templates for breadcrumb structures and sitemaps, a catalog of anti-patterns to avoid (mystery meat navigation, deep nesting, inconsistent placement, missing location indicators), and practical guidance for both documentation sites and applications. The skill produces actual navigation structures -- not theory about navigation in general, but the specific hierarchy, labels, and wayfinding system for your project.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Navigation mirrors internal team structure, not user mental models | Information architecture based on user tasks and recognition over recall |
| Users cannot find features buried in deep menu hierarchies | 3-click rule enforced, flat and hub-and-spoke patterns for shallow access |
| No breadcrumbs -- users lose track of where they are in the site | Breadcrumb templates with proper hierarchy and clickable parent links |
| Top-level navigation has 15+ items, overwhelming new users | 7 +/- 2 rule applied to top-level items with overflow strategies |
| Documentation sitemap is an afterthought added after all pages exist | Sitemap designed upfront as the structural blueprint for content organization |
| Navigation changes layout and position between sections | Consistency rules ensuring global nav stays stable across the entire application |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install navigation-design@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention relevant topics.

## Quick Start

1. Install the plugin using the commands above.
2. Describe what you are building:
   ```
   I'm creating a developer documentation site for an API with guides, tutorials, and reference docs -- design the navigation structure
   ```
3. The skill produces a complete information architecture with global nav, section nav, breadcrumbs, and sitemap.
4. Refine specific sections:
   ```
   The API reference section has 40+ endpoints -- how should I organize them so developers can find what they need?
   ```
5. Get a faceted navigation design with grouping, search, and filtering patterns tailored to large reference sections.

## What's Inside

Compact single-skill plugin focused on navigation and information architecture.

| Component | Description |
|---|---|
| **SKILL.md** | Core skill covering navigation types, IA patterns (hierarchy, hub-and-spoke, flat, faceted), navigation rules, breadcrumb and sitemap templates, and anti-patterns |
| **evals/** | 13 trigger evaluation cases + 3 output quality evaluation cases |

### navigation-design

**What it does:** Activates when you need to design or restructure navigation, information architecture, wayfinding systems, breadcrumbs, sitemaps, or menu structures for any application or documentation site. It provides a decision framework for choosing the right IA pattern, concrete templates for breadcrumbs and sitemaps, and rules that prevent the most common navigation mistakes.

**Try these prompts:**

```
Design the navigation structure for a SaaS dashboard with 12 main features and an admin section
```

```
My documentation site has grown to 200 pages and users can't find anything -- help me restructure the information architecture
```

```
What breadcrumb pattern should I use for a multi-level e-commerce category system?
```

```
I have too many items in my top nav -- how do I reduce them without hiding important features?
```

```
Design a sitemap for a developer platform with docs, API reference, tutorials, and a community forum
```

```
Should I use a sidebar nav, top nav, or both for my project management app?
```

## Real-World Walkthrough

You are redesigning the documentation site for a developer platform. The current site has 180 pages spread across API reference, getting started guides, tutorials, concept explanations, and a changelog. Users complain they cannot find things, and your support team reports that 30% of tickets are answered by existing documentation the user did not discover.

**Step 1: Audit the current structure.**

You start by describing the problem:

```
I have a developer docs site with 180 pages. Users say they can't find anything. Current structure: everything is in a single sidebar with nested folders up to 5 levels deep. Help me redesign the information architecture.
```

The skill identifies the core issues immediately: 5-level nesting violates the 3-click rule, a single sidebar for 180 pages creates an overwhelming wall of links, and deep hierarchy hides content that users do not know to look for. It recommends a combination of hierarchy (tree) and hub-and-spoke patterns.

**Step 2: Design the primary navigation.**

The skill produces a global navigation structure with 5 top-level items following the 7 +/- 2 rule: Getting Started, Guides, API Reference, Concepts, and Community. Each top-level item becomes a hub page with clear pathways to its content. This replaces the single deep sidebar with focused section navigation.

```
Home
├── Getting Started (hub: quickstart, installation, first API call)
├── Guides (hub: authentication, webhooks, pagination, error handling)
├── API Reference (faceted: endpoints grouped by resource, searchable)
├── Concepts (hub: architecture overview, data model, permissions)
└── Community (hub: changelog, FAQ, examples, forum)
```

**Step 3: Apply faceted navigation to the API reference.**

The API reference has 45 endpoints -- too many for a simple hierarchy. You ask:

```
The API reference has 45 endpoints across 8 resources. How do I make this navigable?
```

The skill recommends faceted navigation: endpoints grouped by resource (Users, Orders, Products, etc.) with a search overlay and method-type filters (GET, POST, PUT, DELETE). Each resource group shows 3-8 endpoints, keeping the visual load manageable. A persistent breadcrumb trail (Home > API Reference > Users > Get User) ensures developers always know where they are.

**Step 4: Add contextual navigation.**

The skill adds a contextual navigation layer: "Related articles" links within each page that connect logically related content across sections. The authentication guide links to the API reference endpoints that require auth. The data model concept page links to the relevant API resources. These cross-links are the fix for the discoverability problem -- users find documentation they did not know to search for.

**Step 5: Build the breadcrumb system.**

Every page gets a breadcrumb following the template:

```
Home > [Section] > [Subsection] > Current Page
```

The skill specifies: all segments are clickable except the current page, the breadcrumb reflects the content hierarchy (not the URL path, which may differ), and mobile views collapse intermediate segments to "..." with a tap-to-expand pattern.

The result: the redesigned docs site drops from 5-level nesting to a maximum of 3 levels. The hub-and-spoke pattern means every major section has a landing page that orients the user before they dive in. Faceted navigation makes the 45-endpoint API reference searchable and filterable. Contextual links connect related content across sections, solving the discoverability problem that was generating 30% of support tickets. Six weeks after launch, documentation-related support tickets drop by 40% because users can actually find the pages that answer their questions.

## Usage Scenarios

### Scenario 1: Designing navigation for a new SaaS product

**Context:** You are building a project management tool with task boards, timelines, reports, team settings, and integrations. You need to plan the navigation before building any UI.

**You say:** "Design the navigation structure for a project management SaaS app with boards, timelines, reports, team management, and an integrations marketplace."

**The skill provides:**
- Global navigation with 5-6 top-level items following the 7 +/- 2 rule
- Utility navigation placement for search, notifications, and user settings
- Local navigation patterns for each section (e.g., report filters, integration categories)
- Consistency rules so navigation stays predictable across all sections

**You end up with:** A complete navigation architecture you can hand to your design team, with every level specified and anti-patterns flagged.

### Scenario 2: Restructuring an overgrown documentation site

**Context:** Your docs site started with 20 pages and now has 150+. The sidebar is overwhelming and users complain they cannot find content.

**You say:** "My docs sidebar has become unmanageable -- 150 pages, 4 levels of nesting, and users say they get lost. How do I fix the information architecture?"

**The skill provides:**
- Hub-and-spoke pattern to replace deep nesting with oriented landing pages
- Content grouping strategy based on user tasks rather than internal categories
- Breadcrumb system to maintain orientation
- Contextual "related articles" links for cross-section discoverability

**You end up with:** A restructured IA with a maximum of 3 navigation levels, hub pages for each section, and a breadcrumb trail that keeps users oriented.

### Scenario 3: Mobile navigation for a content-heavy app

**Context:** Your responsive web app has rich desktop navigation (sidebar + top nav) that collapses to a hamburger menu on mobile, burying all navigation behind one tap.

**You say:** "Our mobile hamburger menu has 30 items in it -- users never find the features they need on mobile. How do I design better mobile navigation?"

**The skill provides:**
- Bottom navigation bar pattern for the 4-5 most critical actions
- Progressive disclosure: hamburger menu only for secondary items
- Recognition over recall: visible labels on bottom nav, not just icons
- Breadcrumb adaptation for narrow screens

**You end up with:** A mobile navigation design that surfaces critical features directly while keeping secondary navigation accessible without overwhelming the screen.

### Scenario 4: E-commerce category navigation

**Context:** You are designing the category navigation for an online store with 500+ products across 12 departments and dozens of subcategories.

**You say:** "Design the category navigation for an e-commerce site with 12 departments and hundreds of subcategories. Users need to browse and filter efficiently."

**The skill provides:**
- Faceted navigation with multiple classification dimensions (department, price, brand, rating)
- Mega-menu pattern for the top-level department browser
- Breadcrumb trail with category hierarchy
- Filter and sort patterns for large category pages

**You end up with:** A faceted category navigation system with a mega-menu for discovery and breadcrumbs for orientation, supporting both browsing and targeted search.

## Ideal For

- **Product designers building navigation for new applications** -- the IA patterns and navigation rules prevent the most common structural mistakes
- **Documentation teams restructuring overgrown content sites** -- hub-and-spoke and faceted patterns tame large content collections
- **Frontend developers implementing nav components** -- concrete templates for breadcrumbs, sitemaps, and menu structures translate directly to code
- **UX researchers diagnosing navigation failures** -- the anti-pattern catalog maps directly to common usability test findings
- **Content strategists planning information architecture** -- the four IA patterns (hierarchy, hub-and-spoke, flat, faceted) provide the structural vocabulary for content organization decisions

## Not For

- **Visual design of navigation components** (colors, typography, spacing) -- use [frontend-design](../frontend-design/) for visual styling and component libraries
- **User journey mapping across touchpoints** -- use [user-journey-design](../user-journey-design/) for end-to-end journey flows
- **Content modeling and CMS schema design** -- use [content-modelling](../content-modelling/) for content types, fields, and editorial workflows

## How It Works Under the Hood

The skill is a compact, focused knowledge base covering the core disciplines of navigation design and information architecture. The SKILL.md provides the complete framework: five navigation types (global, local, contextual, utility, breadcrumb) with use cases, four IA patterns (hierarchy, hub-and-spoke, flat, faceted) with decision criteria, empirically backed rules (7 +/- 2, 3-click, recognition over recall, consistency), ready-to-use templates for breadcrumbs and sitemaps, and an anti-pattern catalog.

There are no additional reference files -- the skill is deliberately compact so it loads fully into context without progressive disclosure overhead. This makes it fast to activate and immediately actionable.

The evaluation suite (13 trigger cases, 3 output quality cases) ensures the skill activates reliably on navigation and IA queries.

## Related Plugins

- **[User Journey Design](../user-journey-design/)** -- Maps the end-to-end user journey that navigation supports
- **[Content Modelling](../content-modelling/)** -- Defines the content structure that navigation surfaces
- **[Frontend Design](../frontend-design/)** -- Visual design for navigation components
- **[Consistency Standards](../consistency-standards/)** -- Naming conventions and taxonomy standards for navigation labels
- **[UX Writing](../ux-writing/)** -- Microcopy and labels for navigation elements

## Version History

- `1.0.10` fix(design+docs): regenerate READMEs for 9 design and documentation plugins
- `1.0.9` fix: add standard keywords and expand READMEs to full format for design and documentation plugins
- `1.0.8` fix: change author field from string to object in all plugin.json files
- `1.0.7` fix: rename all claude-skills references to skillstack
- `1.0.0` Initial release

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
