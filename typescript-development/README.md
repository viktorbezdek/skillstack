# Typescript Development

> **v1.1.20** | Development | 22 iterations

Comprehensive TypeScript development skill covering type system mastery, runtime validation (Zod, TypeBox, Valibot), framework integration (React 19, Next.js 16, NestJS, React Native), architecture patterns, security, tsconfig optimization, and testing strategies.

## What Problem Does This Solve

TypeScript's type system is powerful enough to prevent whole classes of runtime bugs — but only when used correctly. Teams that rely on `any`, ignore strict mode, or bolt on Zod schemas as an afterthought end up with a false sense of safety: types pass at compile time but data still blows up at runtime. This skill provides opinionated, production-tested patterns for strict type configuration, branded types that prevent ID mixups, discriminated unions for exhaustive state modeling, runtime validation library selection (Zod vs TypeBox vs Valibot), and Clean Architecture integration for NestJS and React 19.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "How do I model loading/success/error states without bugs?" | Discriminated union pattern for `AsyncState<T>` with exhaustive switch handling |
| "I keep mixing up user IDs and order IDs at runtime" | Branded types pattern using `Brand<T, B>` to make structurally identical types type-incompatible |
| "Which validation library should I use — Zod, TypeBox, or Valibot?" | Decision tree comparing all three on bundle size, OpenAPI compatibility, performance, and React form integration |
| "My tsconfig is not strict enough and I'm getting runtime nulls" | Recommended tsconfig with `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, and explanations for each flag |
| "How do I structure a NestJS API with Clean Architecture?" | Repository pattern, Use Case pattern, dependency injection setup, and a complete NestJS + TypeORM example |
| "I need to handle unknown API response shapes safely" | `unknown` + Zod validation pattern, type guard authoring, and when to use assertion functions vs. type predicates |

## When NOT to Use This Skill

- Python development -- use [python-development](../python-development/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/typescript-development
```

## How to Use

**Direct invocation:**

```
Use the typescript-development skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `typescript`
- `zod`
- `clean-architecture`
- `branded-types`

## What's Inside

- **Overview** -- What the merged skill covers: type system, runtime validation, framework integration, architecture, security, configuration, and testing.
- **Core TypeScript Principles** -- Strict mode tsconfig flags, no-`any` policy, type-only imports, and the reasoning behind each constraint.
- **Type System Patterns** -- Code patterns for discriminated unions, conditional types, mapped types with modifiers, template literal types, and branded types with `unique symbol`.
- **Validation Library Decision Tree** -- When to choose Zod vs TypeBox vs Valibot based on API validation needs, JSON Schema requirements, bundle size, performance, and form integration.
- **Decision Trees** -- Type vs. interface, `unknown` vs. `any`, and generics vs. union types — each as a flowchart with decision criteria.
- **Common Patterns Quick Reference** -- Table mapping 10 patterns (discriminated union, branded types, result type, repository pattern, etc.) to their primary use cases.
- **Resources** -- Index of all reference documents, the TypeScript config validator script, tsconfig template, and the complete NestJS + TypeORM example project.
- **Version Compatibility** -- Confirmed compatibility matrix: TypeScript 5.x, React 18/19, Next.js 14-16, Node.js 20+, NestJS 10+, ESM and CommonJS.

## Key Capabilities

- **Type System Mastery**
- **Runtime Validation**
- **Framework Integration**
- **Architecture Patterns**
- **Security**
- **Configuration**

## Version History

- `1.1.20` fix(languages+tools): optimize descriptions for git-workflow, mcp-server, python, typescript (b65bc7d)
- `1.1.19` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.1.18` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.17` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.16` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.15` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.14` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.13` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.12` docs: add detailed README documentation for all 34 skills (7ba1274)
- `1.1.11` refactor: standardize frontmatter and split oversized SKILL.md files (4a21a62)

## Related Skills

- **[Api Design](../api-design/)** -- Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, aut...
- **[Debugging](../debugging/)** -- Comprehensive debugging skill combining systematic debugging methodology, browser DevTools automation, E2E testing with ...
- **[Frontend Design](../frontend-design/)** -- Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, acce...
- **[Gws Cli](../gws-cli/)** -- Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace A...
- **[Mcp Server](../mcp-server/)** -- Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Pyth...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
