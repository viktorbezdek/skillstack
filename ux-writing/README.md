# UX Writing

> **v1.0.10** | Design & UX | 11 iterations

Write effective microcopy, error messages, button labels, and interface text using UX writing principles.

## What Problem Does This Solve

Interface text is often written by engineers as an afterthought — "Submit", "Error 404", "Click here" — leaving users confused about what just happened or what to do next. UX writing treats every label, error message, button, and empty state as a design decision that either guides the user toward success or creates friction. This skill provides the Clear-Concise-Useful-Human framework, tone guidelines by context (success, error, warning, empty), and concrete before/after rewrites for the most common UI patterns.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Write better error messages for my form validation" | Error message pattern: human-readable description of what went wrong plus a specific next step to resolve it |
| "The submit button just says 'Submit' — how do I improve it?" | Verb + Object formula for button labels (e.g., "Save changes", "Download report") with examples of common weak labels and rewrites |
| "Users don't know what to do on the empty state screen" | Encouraging empty state copy pattern that describes what the feature does and provides a clear first action |
| "Write a confirmation dialog for a destructive action" | Confirmation dialog template with action-specific title, irreversibility warning, and labeled confirm/cancel buttons |
| "My error messages are too technical for end users" | Tone-by-context guidance for turning technical error codes into helpful, empathetic copy |
| "How do I write form field labels that reduce support tickets?" | Form label pattern with placeholder text, helper text positioning, and follow-up confirmation messaging |

## When NOT to Use This Skill

- generating

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/ux-writing
```

## How to Use

**Direct invocation:**

```
Use the ux-writing skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `ux-writing`
- `microcopy`
- `error-messages`

## What's Inside

- **Core Principles** -- Four writing principles (Clear, Concise, Useful, Human) with description of what each means in practice for interface copy.
- **Tone by Context** -- Tone guidance for four UI states — success (celebratory), error (helpful), warning (direct), and empty (encouraging) — with example copy for each.
- **UI Patterns** -- Before/after rewrites for the four highest-impact copy locations: button labels (Verb + Object formula), error messages (human description + next step), confirmation dialogs (action title + consequence + labeled buttons), and form labels (label + placeholder + helper text).

## Version History

- `1.0.10` fix(strategy+ux): optimize descriptions for outcome, prioritization, risk, systems, journey, ux-writing (9661735)
- `1.0.9` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.0.8` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.7` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.6` docs: update README and install commands to marketplace format (af9e39c)
- `1.0.5` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.0.4` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.0.3` docs: add detailed README documentation for all 34 skills (7ba1274)
- `1.0.2` refactor: standardize frontmatter and split oversized SKILL.md files (4a21a62)
- `1.0.1` docs: improve strategic skill descriptions (f59b24a)

## Related Skills

- **[Content Modelling](../content-modelling/)** -- Design content models with types, fields, relationships, and governance rules for structured content systems.
- **[Elicitation](../elicitation/)** -- Psychological profiling through natural conversation using narrative identity, self-defining memory elicitation, Motivat...
- **[Navigation Design](../navigation-design/)** -- Design information architecture, wayfinding systems, breadcrumbs, and navigation patterns for documentation and applicat...
- **[Ontology Design](../ontology-design/)** -- Design knowledge models with classes, properties, relationships, and taxonomies for structured data representation.
- **[Persona Definition](../persona-definition/)** -- Create detailed user personas with demographics, goals, pain points, behaviors, and empathy maps.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
