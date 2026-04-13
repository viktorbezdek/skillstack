# Typescript Development

> **v1.1.20** | Development | 22 iterations

Comprehensive TypeScript development skill covering type system mastery, runtime validation (Zod, TypeBox, Valibot), framework integration (React 19, Next.js 16, NestJS, React Native), architecture patterns, security, tsconfig optimization, and testing strategies.

## What Problem Does This Solve

TypeScript's type system is powerful enough to prevent whole classes of runtime bugs -- but only when used correctly. Teams that rely on `any`, ignore strict mode, or bolt on Zod schemas as an afterthought end up with a false sense of safety: types pass at compile time but data still blows up at runtime. Choosing between Zod, TypeBox, and Valibot requires understanding trade-offs in bundle size, OpenAPI compatibility, and performance that are not obvious from each library's README. And framework-specific patterns for React 19, Next.js 16, NestJS, and React Native each have their own conventions that are easy to get wrong.

This skill provides opinionated, production-tested patterns for strict type configuration, branded types that prevent ID mixups, discriminated unions for exhaustive state modeling, runtime validation library selection, and Clean Architecture integration -- all in one place so you stop context-switching between docs.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install typescript-development@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

**Direct invocation:**

```
Use the typescript-development skill to set up strict tsconfig for my project
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `typescript`
- `zod`
- `clean-architecture`
- `branded-types`

## What's Inside

This is a **single-skill plugin** with 13 reference documents, a validator script, a tsconfig template, a complete NestJS example project, and two eval suites.

| Component | Path | Purpose |
|---|---|---|
| Skill | `skills/typescript-development/SKILL.md` | Core methodology: strict mode, type system patterns, validation library decision tree, decision trees (type vs interface, unknown vs any, generics vs union), common patterns quick reference |
| Reference | `references/extended-patterns.md` | Detailed code examples for all patterns including runtime validation, React integration, Clean Architecture, error handling |
| Reference | `references/advanced-types.md` | Deep dives into conditional types, mapped types, template literal types |
| Reference | `references/advanced-patterns-2025.md` | Latest TypeScript 5.x patterns |
| Reference | `references/runtime-validation.md` | Zod, TypeBox, Valibot comparison with code examples and benchmarks |
| Reference | `references/decision-trees.md` | Flowcharts for type vs interface, validation library choice |
| Reference | `references/configuration.md` | tsconfig.json flag-by-flag optimization guide |
| Reference | `references/troubleshooting.md` | Common TypeScript errors and solutions |
| Reference | `references/security-examples.md` | Branded types for SafeSQL, sensitive data handling patterns |
| Reference | `references/typescript-standards.md` | Strict mode conventions, naming patterns |
| Reference | `references/typescript-patterns.md` | React Native-specific TypeScript patterns |
| Reference | `references/reference.md` | Clean Architecture patterns, API design with TypeScript |
| Reference | `references/examples.md` | Complete feature implementation walkthroughs |
| Reference | `references/advanced-patterns.md` | Builder pattern, typed event systems |
| Script | `scripts/typescript-validator.js` | Validates tsconfig.json against recommended strict settings |
| Template | `templates/typescript-config.json` | Production-ready tsconfig.json with all strict flags enabled |
| Example | `examples/nestjs-typeorm-api/` | Complete NestJS + TypeORM REST API with DTOs, entities, services, and modules |

## Usage Scenarios

**1. "How do I model loading/success/error states without bugs?"**
The skill provides the discriminated union pattern for `AsyncState<T>` with exhaustive switch handling. Each state variant carries only the data relevant to that state (`data: T` on success, `error: Error` on error), so the compiler enforces that you cannot access `data` in the loading state.

**2. "Which validation library should I use -- Zod, TypeBox, or Valibot?"**
The validation library decision tree compares all three on five axes: API validation (Zod wins for general use), OpenAPI/JSON Schema generation (TypeBox), bundle size sensitivity (Valibot at 1/10th the size), raw performance (TypeBox with compiled validators), and React form integration (Zod + react-hook-form). Includes code examples for each.

**3. "My tsconfig is not strict enough and I'm getting runtime nulls"**
The skill provides a recommended tsconfig with `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `noImplicitReturns`, `noFallthroughCasesInSwitch`, and `noPropertyAccessFromIndexSignature` -- with an explanation of what each flag catches. The `typescript-validator.js` script checks your existing config against these recommendations.

**4. "How do I structure a NestJS API with Clean Architecture?"**
The `examples/nestjs-typeorm-api/` directory contains a complete working example with entities, DTOs (using class-validator), services with repository injection, controllers, and module wiring. The reference documents cover the Repository Pattern, Use Case Pattern, and dependency injection setup in detail.

**5. "I keep mixing up user IDs and order IDs at runtime"**
The branded types pattern uses `Brand<T, B>` with `unique symbol` to make structurally identical string types (UserId, OrderId, Email, SafeSQL) type-incompatible. Passing a `UserId` where an `OrderId` is expected becomes a compile-time error, not a production bug.

## When to Use / When NOT to Use

**Use when:**
- Working with TypeScript files, tsconfig, or type system patterns
- Choosing between Zod, TypeBox, and Valibot for runtime validation
- Setting up NestJS with Clean Architecture and dependency injection
- Implementing branded types, discriminated unions, or advanced generics
- Configuring strict tsconfig for a new or existing project

**Do NOT use when:**
- Python development -- use [python-development](../python-development/) instead
- React component patterns, hooks, or state management -- use [react-development](../react-development/) instead
- Next.js framework specifics (App Router, Server Components, SSR) -- use [nextjs-development](../nextjs-development/) instead

## Version Compatibility

TypeScript 5.x (including 5.9 features) | React 18/19 | Next.js 14-16 | Node.js 20+ | NestJS 10+ | ESM and CommonJS

## Related Plugins in SkillStack

- **[React Development](../react-development/)** -- React hooks, component architecture, and state management patterns
- **[Next.js Development](../nextjs-development/)** -- App Router, Server Components, Server Actions, and Next.js-specific patterns
- **[API Design](../api-design/)** -- REST, GraphQL, and gRPC endpoint design that pairs with TypeScript types
- **[Frontend Design](../frontend-design/)** -- UI/UX design systems, Tailwind CSS, and component libraries
- **[Test-Driven Development](../test-driven-development/)** -- TDD methodology that applies to TypeScript testing strategies

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
