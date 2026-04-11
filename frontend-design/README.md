# Frontend Design

> **v1.1.23** | Development | 25 iterations

Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, accessibility patterns, and visual design.

## What Problem Does This Solve

Frontend teams routinely reinvent design decisions — colours, spacing, dark mode tokens, accessible keyboard patterns — because the knowledge is scattered across eleven different specialist areas and rarely consolidated in one place. This skill merges that expertise into a single reference covering the Tailwind + Radix UI + shadcn/ui stack, Figma-to-token extraction, WCAG 2.2 compliance, and responsive layout, so developers can build consistent, accessible UIs without context-switching across multiple docs.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Build a dashboard card component with Tailwind and shadcn/ui" | Quick-start component setup, shadcn/ui CLI commands, and a working TypeScript example with responsive grid |
| "Set up a dark mode token system" | Three-tier CSS variable architecture (primitives, semantics, components) with `.dark` override pattern |
| "Extract design tokens from our Figma file" | `extract_tokens.py` + `transform_tokens.py` + `validate_tokens.py` script workflow |
| "Is our UI accessible? We need WCAG AA compliance" | WCAG 2.2 contrast table, accessibility checklist, and `audit_accessibility.sh` script |
| "Which component library should we use and how does it layer together?" | Core stack architecture explaining Tailwind (styling) → Radix UI (behaviour) → shadcn/ui (complete components) |
| "Evaluate the visual quality of this UI and suggest improvements" | UI evaluation with `evaluate-ui.ts` and A/B variation comparison with `compare-variations.ts` |

## When NOT to Use This Skill

- React component logic, hooks, or state management -- use [react-development](../react-development/) instead
- Next

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install frontend-design@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the frontend-design skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `frontend`
- `ui-ux`
- `tailwind`
- `accessibility`
- `design-tokens`

## What's Inside

- **When to Use This Skill** -- Decision criteria covering components, design systems, styling, accessibility, UI evaluation, and performance optimisation use cases.
- **Quick Start Decision Tree** -- Branching guide routing requests to the right sub-section or script based on whether you are creating components, styling, working on a design system, addressing accessibility, or evaluating quality.
- **Core Stack Architecture** -- Three-pillar explanation of how Tailwind CSS (styling), Radix UI (accessible behaviour), and shadcn/ui (complete components) layer on top of each other.
- **Quick Start: Component Setup** -- `npx shadcn@latest` setup commands and a working TypeScript/React dashboard component example.
- **Design Token System** -- Three-tier CSS variable architecture (primitives → semantics → components) with Figma extraction script workflow.
- **Accessibility Standards** -- WCAG 2.2 contrast ratio table, eight-item accessibility checklist, and a summary of Radix UI's built-in accessibility guarantees.
- **Best Practices Summary** -- Do/don't checklist covering semantic HTML, mobile-first layout, WCAG compliance, design tokens, TypeScript, and Core Web Vitals.
- **External Resources** -- Links to TailwindCSS, Radix UI, shadcn/ui, WCAG 2.2, OKLCH color space, and WebAIM contrast checker.

## Key Capabilities

- **TailwindCSS:**
- **Radix UI:**
- **shadcn/ui:**
- **WCAG Guidelines:**
- **OKLCH Color Space:**
- **WebAIM Contrast Checker:**

## Version History

- `1.1.23` fix(frontend): disambiguate react-development vs nextjs-development vs frontend-design (6c64693)
- `1.1.22` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.1.21` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.20` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.19` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.18` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.17` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.16` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.15` fix: make all shell scripts executable and fix Python syntax errors (61ac964)
- `1.1.14` docs: add detailed README documentation for all 34 skills (7ba1274)

## Related Skills

- **[Api Design](../api-design/)** -- Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, aut...
- **[Debugging](../debugging/)** -- Comprehensive debugging skill combining systematic debugging methodology, browser DevTools automation, E2E testing with ...
- **[Gws Cli](../gws-cli/)** -- Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace A...
- **[Mcp Server](../mcp-server/)** -- Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Pyth...
- **[Nextjs Development](../nextjs-development/)** -- Comprehensive Next.js development skill covering App Router (13+/15/16), Server Components, Server Actions, Cache Compon...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
