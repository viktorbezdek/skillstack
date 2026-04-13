# TypeScript Development

> **v1.1.20** | Stop guessing at TypeScript patterns -- get opinionated, production-tested guidance for the type system, runtime validation, framework integration, and strict configuration in one place.
> Single skill + 13 references + 1 script + 1 template + 1 example project | 13 trigger evals + 3 output evals

## The Problem

TypeScript promises compile-time safety, but most codebases underdeliver on that promise. Teams enable `strict: true` and think they are covered, while `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes` -- the flags that actually catch runtime nulls from array access and optional properties -- stay disabled because nobody knows they exist. The result: types pass at compile time, data blows up at runtime.

Choosing a validation library is a minefield of invisible trade-offs. Zod, TypeBox, and Valibot all look similar in their READMEs, but they differ dramatically in bundle size (Valibot is 1/10th of Zod), OpenAPI compatibility (TypeBox generates JSON Schema natively), and performance (TypeBox compiled validators vs Zod's interpreted approach). Teams pick one, commit to it, and discover the trade-off six months later when they need OpenAPI generation or their frontend bundle bloats.

Then there are the framework-specific patterns. React 19 Server Components have different TypeScript conventions than client components. NestJS with Clean Architecture requires specific dependency injection patterns that are easy to wire incorrectly. React Native has its own TypeScript quirks around platform-specific types. Each framework's documentation covers its own conventions, but nobody connects them back to TypeScript fundamentals -- so teams end up with inconsistent type patterns across their stack.

## The Solution

This plugin provides a single, comprehensive TypeScript skill that covers the full stack: strict tsconfig configuration with every flag explained, type system patterns (branded types, discriminated unions, conditional types, mapped types, template literals), runtime validation library selection with a concrete decision tree, and framework integration patterns for React 19, Next.js 16, NestJS, and React Native.

The branded types pattern makes structurally identical types (UserId, OrderId, Email, SafeSQL) type-incompatible at compile time. Passing a `UserId` where an `OrderId` is expected becomes a compiler error, not a production incident. The discriminated union pattern for `AsyncState<T>` guarantees exhaustive handling of loading/success/error states, so the compiler catches missing branches.

The plugin ships with a `typescript-validator.js` script that checks your existing tsconfig against recommended strict settings, a production-ready `typescript-config.json` template, and a complete NestJS + TypeORM REST API example project with entities, DTOs, services, controllers, and module wiring.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| `strict: true` is enabled but runtime nulls still crash from array access and optional properties | Full strict config with `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, and 4 other flags -- each explained |
| Picked Zod because it was popular, now need OpenAPI generation and it does not fit | Decision tree picks the right library (Zod, TypeBox, or Valibot) based on your actual requirements |
| `UserId` and `OrderId` are both `string` -- wrong ID passed silently at runtime | Branded types make structurally identical types compiler-incompatible |
| Loading/success/error states handled with boolean flags, missing branches cause bugs | Discriminated unions with exhaustive `switch` -- compiler catches every missing state |
| NestJS services wired with ad-hoc dependency injection, inconsistent across modules | Clean Architecture patterns with Repository and Use Case patterns, complete working example |
| `any` scattered through the codebase "because we'll fix it later" | No-any policy with concrete alternatives: `unknown` + validation, generics, type guards |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install typescript-development@skillstack
```

### Prerequisites

No additional dependencies. Works with any TypeScript project.

### Verify installation

After installing, test with:

```
Set up a strict tsconfig for my new TypeScript project
```

## Quick Start

1. Install the plugin with the commands above
2. Type: `My tsconfig just has strict: true -- what am I missing?`
3. The skill audits your configuration and recommends additional flags like `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes`
4. Run the shipped `typescript-validator.js` script against your tsconfig for automated checking
5. Next, try: `Which validation library should I use -- I need OpenAPI generation and good React form integration`

---

## System Overview

```
User prompt (TypeScript question, type pattern, validation, tsconfig, NestJS, etc.)
        |
        v
+----------------------------+
| typescript-development     |  <-- Single skill, activates on TS / type system / Zod / tsconfig mentions
|        (SKILL.md)          |
+----------------------------+
    |         |         |         |
    v         v         v         v
+---------+ +--------+ +--------+ +-----------+
| Type    | | Valid- | | Config | | Framework |
| System  | | ation  | |        | | Patterns  |
+---------+ +--------+ +--------+ +-----------+
| advanced| | runtime| | config-| | typescript|
| -types  | | -valid-| | uration| | -patterns |
| advanced| | ation  | | trouble| | reference |
| -pattern| | decisio| | shootin| | examples  |
| security| | n-trees| | g      | | extended- |
| -example|          |        | | patterns  |
+---------+ +--------+ +--------+ +-----------+

Runnable tooling:
  typescript-validator.js .... validates tsconfig against recommendations
  typescript-config.json ..... production-ready tsconfig template
  nestjs-typeorm-api/ ........ complete NestJS + TypeORM example project
```

The skill loads the core methodology on activation. When the conversation touches a specific topic (advanced types, validation library choice, tsconfig flags, framework-specific patterns), it draws on the relevant reference to provide depth. The 13 references are organized by concern so that context stays lean -- only the needed reference is loaded.

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `skills/typescript-development/SKILL.md` | Skill | Core methodology: strict mode, type patterns, validation library decision tree, type-vs-interface and unknown-vs-any decision trees |
| `references/extended-patterns.md` | Reference | Detailed code examples for runtime validation, React integration, Clean Architecture, error handling |
| `references/advanced-types.md` | Reference | Conditional types, mapped types, template literal types, recursive types |
| `references/advanced-patterns-2025.md` | Reference | TypeScript 5.2+ patterns: explicit resource management, stable decorators |
| `references/runtime-validation.md` | Reference | Zod, TypeBox, Valibot comparison with benchmarks and code examples |
| `references/decision-trees.md` | Reference | Flowcharts for type vs interface, unknown vs any, generics vs union |
| `references/configuration.md` | Reference | tsconfig.json flag-by-flag optimization guide |
| `references/troubleshooting.md` | Reference | Common TypeScript errors and solutions |
| `references/security-examples.md` | Reference | Branded types for SafeSQL, sensitive data handling patterns |
| `references/typescript-standards.md` | Reference | Strict mode conventions, naming patterns |
| `references/typescript-patterns.md` | Reference | React Native-specific TypeScript patterns |
| `references/reference.md` | Reference | Clean Architecture patterns, API design with TypeScript |
| `references/examples.md` | Reference | Complete feature implementation walkthroughs (TS 5.9, React 19, Next.js 16) |
| `references/advanced-patterns.md` | Reference | Builder pattern, typed event systems |
| `scripts/typescript-validator.js` | Script | Validates tsconfig.json against recommended strict settings |
| `templates/typescript-config.json` | Template | Production-ready tsconfig.json with all strict flags enabled |
| `examples/nestjs-typeorm-api/` | Example | Complete NestJS + TypeORM REST API with DTOs, entities, services, and modules |
| `evals/trigger-evals.json` | Eval | 13 trigger scenarios including boundary tests for React/Next.js/Python scoping |
| `evals/evals.json` | Eval | 3 output quality scenarios |

### Component Spotlight

#### typescript-development (skill)

**What it does:** Activates when you work with TypeScript files, type system patterns, generics, Zod, tsconfig, NestJS, branded types, or runtime validation. Provides opinionated guidance on strict configuration, type system patterns, validation library selection, framework-specific conventions, and architecture patterns. Covers the full range from "how do I configure tsconfig" to "how do I structure a NestJS API with Clean Architecture."

**Input -> Output:** You describe your TypeScript problem, configuration question, type design challenge, or validation requirement -> You get opinionated patterns with working code, decision trees for trade-off-heavy choices, and strict configuration recommendations with explanations.

**When to use:**
- Working with TypeScript files, type system patterns, or generics
- Configuring tsconfig.json or debugging compiler errors
- Choosing between validation libraries (Zod, TypeBox, Valibot)
- Designing type-safe patterns (branded types, discriminated unions, Result types)
- Building NestJS APIs with Clean Architecture
- Working with React Native TypeScript quirks

**When NOT to use:**
- Python development -> use [python-development](../python-development/)
- React component patterns, hooks, or state management -> use [react-development](../react-development/)
- Next.js framework specifics (App Router, Server Components, SSR/SSG) -> use [nextjs-development](../nextjs-development/)

**Try these prompts:**

```
Set up a production-ready tsconfig for a new Node.js API -- I want maximum strictness
```

```
I keep mixing up user IDs and order IDs in my codebase -- how do I make TypeScript catch this?
```

```
Compare Zod vs TypeBox vs Valibot for my use case: I need API validation with OpenAPI schema generation and the bundle size matters
```

```
How do I model loading/success/error states for API calls so the compiler catches missing branches?
```

```
I'm getting "Type 'string' is not assignable to type 'string | undefined'" after enabling exactOptionalPropertyTypes -- what does this mean?
```

```
Show me how to structure a NestJS service with repository pattern and dependency injection
```

**Key references:**

| Reference | Topic |
|---|---|
| `extended-patterns.md` | Code examples for all core patterns including validation, React, Clean Architecture |
| `advanced-types.md` | Conditional types, mapped types, template literal types |
| `runtime-validation.md` | Zod, TypeBox, Valibot comparison with benchmarks |
| `decision-trees.md` | Type vs interface, unknown vs any, generics vs union decision flowcharts |
| `configuration.md` | tsconfig.json flag-by-flag guide |
| `troubleshooting.md` | Common TypeScript errors and how to fix them |
| `security-examples.md` | Branded types for SafeSQL, sensitive data handling |
| `typescript-standards.md` | Strict mode conventions, naming patterns |
| `typescript-patterns.md` | React Native TypeScript patterns |
| `reference.md` | Clean Architecture, API design with TypeScript |
| `examples.md` | Complete feature implementation walkthroughs |
| `advanced-patterns.md` | Builder pattern, typed event systems |
| `advanced-patterns-2025.md` | TypeScript 5.2+ patterns: resource management, decorators |

#### typescript-validator.js (script)

**CLI:** `node skills/typescript-development/scripts/typescript-validator.js [path/to/tsconfig.json]`
**What it produces:** A report of missing strict flags, with explanations of what each flag catches and recommendations for enabling them.
**Typical workflow:** Run after installing the plugin or when auditing an existing project's TypeScript configuration.

#### nestjs-typeorm-api/ (example)

**What it contains:** A complete NestJS + TypeORM REST API with entities (`user.entity.ts`), DTOs (`create-user.dto.ts`), services (`users.service.ts`), controllers (`users.controller.ts`), and module wiring (`users.module.ts`, `app.module.ts`).
**Typical workflow:** Clone or reference when building a new NestJS API following Clean Architecture patterns with TypeORM.

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, may not activate) | Good (specific, activates reliably) |
|---|---|
| "Help me with TypeScript" | "Set up a strict tsconfig for a Node.js 20 API with ESM modules" |
| "Types are broken" | "I enabled exactOptionalPropertyTypes and now have 47 type errors I don't understand" |
| "Which library?" | "Compare Zod vs TypeBox for API validation -- I need OpenAPI generation and handle 10k req/s" |
| "Make my code type-safe" | "I keep passing UserId where OrderId is expected -- how do I make these compiler-incompatible?" |
| "How do I do NestJS?" | "Structure a NestJS service with repository pattern and dependency injection for a users module" |

### Structured Prompt Templates

**For tsconfig setup:**
```
Set up a production-ready tsconfig for a [Node.js API / React app / library] targeting [Node 20 / browsers] using [ESM / CommonJS] -- I want every useful strict flag explained
```

**For validation library selection:**
```
I need runtime validation for [use case]. Compare Zod, TypeBox, and Valibot -- I need [OpenAPI generation / small bundle / React form integration] and handle [throughput] requests/second
```

**For type design patterns:**
```
I have [describe the types that get confused, e.g., UserId and OrderId are both strings]. How do I make TypeScript catch when I pass the wrong one?
```

**For troubleshooting compiler errors:**
```
I'm getting this TypeScript error after [what you changed]: [paste the exact error message]. What does it mean and how do I fix it?
```

**For architecture patterns:**
```
Show me how to structure a [NestJS / Express] [service / module] using [repository pattern / Clean Architecture / dependency injection] for [domain, e.g., user management]
```

### Prompt Anti-Patterns

- **Asking about React hooks or component patterns:** This skill covers TypeScript fundamentals, not React-specific patterns. Asking "how do I type useState" activates react-development instead. Ask about the underlying type pattern ("how do I type a generic state container") to get TypeScript-level guidance.
- **Dumping a full tsconfig without a question:** Saying "here's my tsconfig, review it" works better as "my tsconfig has strict: true but I'm still getting runtime nulls from array access -- what flags am I missing?"
- **Asking for a generic "best practices" list:** "What are TypeScript best practices?" is too broad. Focus on a specific concern: strict configuration, type patterns, validation, or architecture.
- **Confusing TypeScript type design with library API usage:** Asking "how do I use Zod" is a Zod documentation question. Asking "should I use Zod or TypeBox for my API validation with OpenAPI requirements" is a TypeScript development decision this skill handles well.

## Real-World Walkthrough

You are building a multi-tenant SaaS API with NestJS. The codebase has been in development for three months with `strict: true` in tsconfig, Zod for request validation, and a growing problem: developers keep passing tenant IDs where user IDs are expected because both are `string`. Last week this caused a data leak where one tenant's data was returned to another.

**Step 1 -- Harden the type system with branded types.** You ask:

```
I need to prevent mixing up TenantId, UserId, and OrderId -- they're all strings and we just had a data leak from passing the wrong one
```

The skill introduces the branded types pattern:

```typescript
declare const __brand: unique symbol;
type Brand<T, B> = T & { [__brand]: B };

type TenantId = Brand<string, 'TenantId'>;
type UserId = Brand<string, 'UserId'>;
type OrderId = Brand<string, 'OrderId'>;
```

Now `findUser(tenantId)` where the parameter expects `UserId` is a compile-time error. The skill also provides factory functions (`createTenantId(raw: string): TenantId`) that validate format before branding, so invalid IDs are caught at the boundary.

**Step 2 -- Audit tsconfig for missing strict flags.** You ask:

```
Audit my tsconfig -- we have strict: true but we're still getting runtime nulls from array indexing
```

The skill identifies that you are missing `noUncheckedIndexedAccess`. With this flag enabled, `users[0]` returns `User | undefined` instead of `User`, forcing you to handle the case where the array is empty. It also flags that you lack `exactOptionalPropertyTypes`, which distinguishes between "property is missing" and "property is explicitly undefined" -- a distinction that matters for your API's partial update endpoints. You run `typescript-validator.js` and get a report of 4 missing flags.

**Step 3 -- Fix the validation library mismatch.** Your Zod schemas work for request validation, but you recently needed OpenAPI documentation and discovered Zod does not produce JSON Schema natively. You ask:

```
We use Zod for validation but now need OpenAPI generation -- should we switch to TypeBox?
```

The skill walks through the decision tree. Since you need both runtime validation and OpenAPI schema generation, TypeBox is the better fit -- it produces JSON Schema by design, and its compiled validators are 5-10x faster than Zod for large schemas. The skill provides a migration strategy: keep Zod for React form validation on the frontend (where `react-hook-form` integration matters), use TypeBox for API validation on the backend (where OpenAPI and performance matter).

**Step 4 -- Apply Clean Architecture to NestJS services.** You ask:

```
Our NestJS services are getting messy -- business logic mixed with database queries. How do I apply Clean Architecture?
```

The skill provides the Repository Pattern (abstract data access behind interfaces), the Use Case Pattern (encapsulate business logic in single-purpose classes), and dependency injection wiring. It points you to the `examples/nestjs-typeorm-api/` directory for a complete working example.

**Step 5 -- Result.** Your codebase goes from "TypeScript strict mode" to genuinely strict: branded types prevent ID mixups at compile time, missing tsconfig flags are enabled, the validation library fits your actual requirements, and services follow a consistent architecture pattern. The data leak class of bug is now structurally impossible.

**Gotchas discovered:** Branded types need factory functions at API boundaries -- you cannot brand raw strings deep inside business logic. The `noUncheckedIndexedAccess` flag generates many new errors in existing code; fix them in batches by file rather than all at once.

## Usage Scenarios

### Scenario 1: Configuring strict TypeScript for a new project

**Context:** You are starting a new Node.js API and want to get tsconfig right from the beginning instead of retroactively adding strictness.

**You say:** `Set up a production-ready tsconfig for a Node.js 20 API using ESM modules -- I want every useful strict flag`

**The skill provides:**
- Complete tsconfig with `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, and 4 more flags
- Explanation of what each flag catches with concrete examples
- Module resolution settings for ESM (`"module": "NodeNext"`, `"moduleResolution": "NodeNext"`)
- The `typescript-config.json` template as a starting point

**You end up with:** A production-ready tsconfig that catches the maximum number of bugs at compile time, with understanding of why each flag matters.

### Scenario 2: Choosing a validation library

**Context:** You are building a REST API that needs request validation, and you have heard of Zod, TypeBox, and Valibot but do not know which to pick.

**You say:** `I need runtime validation for my API -- help me choose between Zod, TypeBox, and Valibot. I need OpenAPI docs and the API handles 10k requests/second.`

**The skill provides:**
- Five-axis comparison: API validation, OpenAPI/JSON Schema, bundle size, performance, React form integration
- Decision tree that maps your requirements (OpenAPI + high performance) to TypeBox
- Code examples for defining schemas, validating data, and generating JSON Schema in TypeBox
- Migration guidance if you later need to add a second library for specific use cases

**You end up with:** A confident library choice with working code examples and understanding of trade-offs you might hit later.

### Scenario 3: Fixing type errors after enabling strict flags

**Context:** You just enabled `exactOptionalPropertyTypes` and your codebase has 47 new type errors you do not understand.

**You say:** `I enabled exactOptionalPropertyTypes and now I'm getting "Type 'string | undefined' is not assignable to type 'string'" everywhere -- what's going on?`

**The skill provides:**
- Explanation of what the flag does (distinguishes missing properties from explicitly-undefined ones)
- Pattern for fixing the errors: use `?:` for "may be missing" and explicit `| undefined` for "present but undefined"
- Common gotchas with `Object.assign`, spread operators, and `Partial<T>`
- Decision framework for whether to fix each error or adjust the type

**You end up with:** All 47 errors resolved with an understanding of why the flag exists and how to write code that works with it.

### Scenario 4: Building type-safe error handling

**Context:** Your API uses try/catch with untyped errors and you want a type-safe alternative that forces callers to handle failure cases.

**You say:** `How do I implement a Result type in TypeScript so my functions return success or error without throwing?`

**The skill provides:**
- Discriminated union `Result<T, E>` pattern with `{ ok: true; value: T }` and `{ ok: false; error: E }`
- Helper functions: `ok()`, `err()`, `map()`, `flatMap()` for composing results
- Integration with async functions using `Promise<Result<T, E>>`
- Comparison with Effect-TS for teams that want a full functional programming approach

**You end up with:** A type-safe error handling pattern where the compiler enforces that every function's failure cases are explicitly handled.

### Scenario 5: Modeling complex state machines

**Context:** Your e-commerce checkout has states (cart, shipping, payment, confirmation, error) and transitions between them. Boolean flags are causing bugs when impossible combinations occur.

**You say:** `Model our checkout flow as a type-safe state machine -- cart to shipping to payment to confirmation, with error handling at each step`

**The skill provides:**
- Discriminated union with each state carrying only its relevant data
- Transition functions that accept one state and return the next, making invalid transitions impossible
- Exhaustive switch pattern that forces handling every state
- React integration pattern for rendering state-specific UI

**You end up with:** A checkout state machine where the compiler prevents impossible state combinations and forces every code path to handle every state.

---

## Decision Logic

**When does this skill activate vs react-development or nextjs-development?**

This skill covers TypeScript-the-language: type system patterns, generics, branded types, tsconfig configuration, validation libraries, and architecture patterns that are framework-agnostic. If the question is "how do I type a generic container" or "should I use Zod or TypeBox", this skill handles it. If the question is "how do I type a React hook" or "what's the TypeScript pattern for Server Components", react-development or nextjs-development is more appropriate.

The boundary: if the answer depends on React/Next.js framework knowledge, use the framework skill. If the answer is pure TypeScript regardless of framework, use this skill.

**When to use the shipped script vs the skill itself?**

Use `typescript-validator.js` when you want an automated audit of an existing tsconfig -- it checks flags programmatically and reports what is missing. Use the skill itself when you want to understand why a flag matters, what trade-offs it introduces, or how to fix the errors that enabling it creates.

**How does the validation library decision tree work?**

The decision tree branches on five axes: (1) need OpenAPI/JSON Schema -> TypeBox, (2) bundle size critical -> Valibot, (3) React form integration -> Zod + react-hook-form, (4) maximum runtime performance -> TypeBox with compiled validators, (5) general API validation -> Zod as the default. When multiple axes conflict (e.g., need OpenAPI + React forms), the skill recommends a dual-library strategy.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Enabling `noUncheckedIndexedAccess` on a large existing codebase | Hundreds of new type errors from every array index and object key access | Enable the flag but fix errors file-by-file in batches. Use `// @ts-expect-error` with a comment as a temporary escape hatch for low-priority code paths. |
| Branded types without factory functions | Raw strings are cast to branded types with `as TenantId`, bypassing validation -- the brand provides false safety | Always create factory functions that validate format before branding. Never export the bare type assertion; export only the factory. |
| Choosing TypeBox for everything because it has the best benchmarks | TypeBox's API is more verbose than Zod for simple cases, and its React form integration is weaker | Use the decision tree honestly. For frontend form validation with React, Zod + react-hook-form is still the better developer experience. TypeBox shines on the backend with OpenAPI. |
| Applying Clean Architecture patterns to a simple CRUD API | Over-engineering: Repository + Use Case + Controller for endpoints that are just database reads with no business logic | Clean Architecture pays off when business logic is complex. For simple CRUD, a service that directly uses the ORM is appropriate. The skill's NestJS example shows where the pattern adds value. |
| Migrating from `any` to `unknown` across a large codebase at once | Massive type errors, developer frustration, and pressure to revert | Migrate incrementally. Start with API boundaries (incoming data), then shared utilities, then internal modules. Each migration should be a self-contained PR. |

## Version Compatibility

TypeScript 5.x (including 5.9 features) | React 18/19 | Next.js 14-16 | Node.js 20+ | NestJS 10+ | ESM and CommonJS

## Ideal For

- **Teams starting new TypeScript projects** -- the strict config and patterns prevent the technical debt that accumulates when "we'll add types later"
- **Backend developers choosing validation libraries** -- the decision tree cuts through marketing and benchmarks to match your actual requirements
- **Engineers dealing with ID mixup bugs** -- branded types eliminate an entire class of production incidents at compile time
- **NestJS developers wanting Clean Architecture** -- the complete example project provides a working reference, not just theory
- **Frontend developers using React with TypeScript** -- discriminated unions and type guards for component props, state, and async operations

## Not For

- **Python development** -- use [python-development](../python-development/) for Python-specific patterns, type hints, and tooling
- **React component patterns, hooks, or state management** -- use [react-development](../react-development/) for React-specific guidance; this plugin covers TypeScript fundamentals that React sits on top of
- **Next.js framework specifics (App Router, Server Components, SSR/SSG)** -- use [nextjs-development](../nextjs-development/) for framework-level patterns

## Related Plugins

- **[React Development](../react-development/)** -- React hooks, component architecture, and state management patterns that build on TypeScript types
- **[Next.js Development](../nextjs-development/)** -- App Router, Server Components, Server Actions, and Next.js-specific TypeScript patterns
- **[API Design](../api-design/)** -- REST, GraphQL, and gRPC endpoint design that pairs with TypeScript type definitions
- **[Frontend Design](../frontend-design/)** -- UI/UX design systems, Tailwind CSS, and component libraries
- **[Test-Driven Development](../test-driven-development/)** -- TDD methodology applied to TypeScript testing strategies
- **[Testing Framework](../testing-framework/)** -- Test infrastructure setup for Vitest, Jest, and other TypeScript-compatible test runners

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
