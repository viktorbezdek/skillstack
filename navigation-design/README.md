# Navigation Design

> **v1.0.10** | Design & UX | 11 iterations

Design information architecture, wayfinding systems, breadcrumbs, and navigation patterns for documentation and applications.

## What Problem Does This Solve

Users abandon products and documentation when they cannot find what they need -- not because content is missing, but because the structure is unclear, menus are overloaded, or there is no indication of where they currently are. Poor information architecture forces users to memorize paths instead of recognizing options. Tabs and sidebars get packed with items because there is no structural model guiding what belongs at each level. This skill provides the IA patterns, navigation type distinctions, rules-of-thumb, and concrete templates for building navigation systems that guide users to their destination without friction.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "How should I structure the navigation for my documentation site?" | Four IA patterns (hierarchy/tree, hub-and-spoke, flat, faceted) with decision guidance on when each fits |
| "My top nav has too many items and users are getting lost" | The 7+/-2 rule, global/local/contextual/utility navigation type distinctions, and menu structure patterns |
| "How do I add breadcrumbs to my app?" | Breadcrumb template with the clickable-except-current-page convention |
| "I need to create a sitemap for a new product" | Ready-to-use sitemap template covering primary and utility navigation structure |
| "Users can't tell where they are in my app" | Current location indicator patterns and the Recognition-over-Recall navigation principle |

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install navigation-design@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the navigation-design skill to structure the navigation for my docs site
```

```
Use the navigation-design skill to audit my app's information architecture
```

```
Use the navigation-design skill to create a sitemap for my SaaS product
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

`navigation` · `information-architecture` · `wayfinding`

## What's Inside

### Skill: navigation-design

Single-skill plugin with no reference files -- all content is in the main SKILL.md.

| Component | Description |
|---|---|
| **SKILL.md** | Complete navigation design guide covering five navigation types, four IA patterns, four design rules, breadcrumb template, sitemap template, and anti-patterns catalog |
| **evals/** | Trigger evaluation and output quality evaluation test suites |

### Key content areas

- **Navigation Types** -- Reference table distinguishing global (site-wide access), local (section-specific), contextual (in-content links), utility (tools/settings), and breadcrumb (location trail) navigation with use cases and examples
- **Information Architecture Patterns** -- Four structural models with diagrams: hierarchy/tree (nested categories), hub-and-spoke (central hub with satellites), flat (few levels, broad categories), and faceted (multiple classification dimensions with filter + sort)
- **Navigation Rules** -- Four core rules: 7+/-2 (limit top-level items), 3-click (reach any page in three clicks), Recognition over Recall (show options instead of requiring memory), and Consistency (same navigation across pages)
- **Breadcrumb Template** -- Ready-to-use `Home > Category > Subcategory > Current Page` pattern with the clickable-except-current-page convention
- **Sitemap Template** -- Markdown sitemap scaffold with primary navigation sections and utility navigation (search, login, help)
- **Anti-Patterns** -- Four common navigation failures: mystery meat navigation (unclear labels), too many levels (deep nesting), inconsistent placement, and missing current location indicator

## Usage Scenarios

1. **Structuring navigation for a new documentation site.** The skill guides you through choosing between hierarchy (best for deep reference docs), hub-and-spoke (best for tutorial-driven learning), or flat structures (best for small sites), then provides the sitemap template to scaffold the primary and utility navigation sections.

2. **Auditing an overloaded application navbar.** Apply the 7+/-2 rule to identify when top-level items exceed cognitive capacity, use the navigation type distinctions to move utility items (search, settings, login) out of the primary nav, and restructure using local navigation for section-specific items.

3. **Adding breadcrumbs to an existing product.** The breadcrumb template provides the exact pattern with the clickable-except-current-page convention, and the IA patterns section helps you verify your hierarchy supports clean breadcrumb trails (flat structures don't).

4. **Diagnosing why users report being "lost" in your app.** The anti-patterns catalog identifies the likely culprits -- missing current location indicators, inconsistent navigation placement across pages, or mystery meat labels that don't communicate what they link to -- and the Recognition-over-Recall principle provides the fix direction.

## Version History

- `1.0.10` fix(docs+quality): optimize descriptions for api-design, docs, edge-cases, examples, navigation, standards (6e315cf)
- `1.0.9` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.0.8` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.7` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.6` docs: update README and install commands to marketplace format (af9e39c)
- `1.0.5` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.0.4` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.0.3` docs: add detailed README documentation for all 34 skills (7ba1274)
- `1.0.2` refactor: standardize frontmatter and split oversized SKILL.md files (4a21a62)
- `1.0.1` docs: improve helper skill descriptions and add trigger words (9c0d140)

## Related Skills

- **[Content Modelling](../content-modelling/)** -- Design content models and structured content architecture that navigation systems expose
- **[Ontology Design](../ontology-design/)** -- Design knowledge models with taxonomies that underpin information architecture
- **[User Journey Design](../user-journey-design/)** -- Map user journeys whose touchpoints navigation must support
- **[Persona Definition](../persona-definition/)** -- Define the users whose mental models navigation should match
- **[Persona Mapping](../persona-mapping/)** -- Map stakeholders to determine navigation priorities by audience

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
