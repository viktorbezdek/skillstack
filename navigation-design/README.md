# Navigation Design

> Design information architecture, wayfinding systems, breadcrumbs, and navigation patterns for documentation and applications.

## Overview

Good navigation is invisible -- users find what they need without thinking about the structure carrying them there. This skill provides the patterns, rules, and templates needed to design intuitive wayfinding systems for websites, applications, and documentation sites.

It covers the full spectrum of navigation design: from high-level information architecture decisions (hierarchy vs. hub-and-spoke vs. faceted) down to individual component patterns like breadcrumbs, global nav bars, local sub-menus, and contextual in-content links. The skill encodes well-established usability heuristics such as the 7 +/- 2 rule and the 3-click rule, while also calling out common anti-patterns to avoid.

Within the SkillStack collection, Navigation Design bridges the gap between content strategy and implementation. It works hand-in-hand with persona skills to ensure navigation is designed for real user mental models, and with ontology design to ensure the underlying taxonomy is sound.

## What's Included

This skill is a single-file skill contained entirely in `SKILL.md`. It provides:

- Navigation type taxonomy (Global, Local, Contextual, Utility, Breadcrumb)
- Information architecture patterns (Hierarchy, Hub and Spoke, Flat, Faceted)
- Navigation rules and heuristics
- Breadcrumb template
- Sitemap template
- Anti-pattern catalog

## Key Features

- Five navigation type definitions with use cases and examples
- Four information architecture patterns with structural diagrams
- Usability heuristics encoded as actionable rules (7 +/- 2, 3-click rule, recognition over recall)
- Ready-to-use breadcrumb and sitemap templates
- Anti-pattern identification to catch common mistakes early
- Applicable to both documentation sites and interactive applications

## Usage Examples

**Design a documentation site navigation:**
```
Design the information architecture and navigation structure for our API documentation site. We have guides, tutorials, API reference, and changelog sections. Target audience is developers with varying experience levels.
```

**Create a sitemap for a SaaS product:**
```
Create a sitemap and navigation hierarchy for our project management SaaS. Include primary navigation, utility navigation, and breadcrumb patterns. We have dashboards, projects, teams, settings, and billing sections.
```

**Audit existing navigation:**
```
Review the navigation structure of our documentation site against navigation design best practices. Identify any anti-patterns like mystery meat navigation or excessive nesting, and suggest improvements.
```

**Design breadcrumb system:**
```
Design a breadcrumb system for our e-commerce site with categories, subcategories, and product pages. Ensure it handles faceted navigation gracefully.
```

**Plan mobile navigation adaptation:**
```
Our desktop site uses a mega menu with 6 top-level items. Design a mobile navigation pattern that preserves discoverability while working within touch constraints.
```

## Quick Start

1. **Identify your content** -- List all pages/sections that need to be navigable.

2. **Choose an IA pattern** -- Pick Hierarchy for deep structured content, Hub and Spoke for task-oriented flows, Flat for simple sites, or Faceted for catalog-style content.

3. **Apply the 7 +/- 2 rule** -- Limit top-level navigation items to 5-9 entries.

4. **Use the sitemap template** -- Fill in the provided template to map out primary and utility navigation.

5. **Add breadcrumbs** -- Use the breadcrumb template (`Home > [Category] > [Subcategory] > Current Page`) for any site deeper than two levels.

6. **Check against anti-patterns** -- Verify you have not introduced mystery meat navigation, excessive nesting, inconsistent placement, or missing location indicators.

## Related Skills

- **persona-definition** -- Create user personas to validate navigation matches user mental models
- **persona-mapping** -- Map stakeholders to prioritize whose navigation needs matter most
- **ontology-design** -- Design the taxonomy that underpins your navigation hierarchy
- **outcome-orientation** -- Define success metrics for navigation effectiveness (e.g., task completion rate)

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `claude plugin add github:viktorbezdek/skillstack/navigation-design` -- 34 production-grade skills for Claude Code.
