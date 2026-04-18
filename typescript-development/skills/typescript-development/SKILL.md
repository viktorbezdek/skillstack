---
name: typescript-development
description: TypeScript development — use when the user works with TypeScript, type system patterns, generics, Zod, tsconfig, NestJS, branded types, or runtime validation. Covers type system mastery, framework integration, architecture patterns, security, and testing strategies. NOT for Python development (use python-development), NOT for React component patterns or hooks (use react-development), NOT for Next.js framework specifics (use nextjs-development).
---

# TypeScript Development - Comprehensive Skill

Expert guidance for modern TypeScript development covering type system patterns, runtime validation, strict configuration, framework integration, and architecture.

## When to Use This Skill

Activate this skill when:
- Working with TypeScript files, type system patterns, or generics
- Configuring tsconfig.json or debugging compiler errors
- Choosing between validation libraries (Zod, TypeBox, Valibot)
- Designing type-safe patterns (branded types, discriminated unions, Result types)
- Building NestJS APIs with Clean Architecture
- Working with React Native TypeScript quirks
- Implementing strict mode beyond `strict: true`
- Writing type guards, conditional types, or mapped types

## When NOT to Use This Skill

- **Python development** → use `python-development`
- **React component patterns, hooks, or state management** → use `react-development` (this skill covers the TypeScript types React sits on, not React-specific patterns)
- **Next.js framework specifics (App Router, Server Components, SSR/SSG)** → use `nextjs-development`
- **General coding assistance unrelated to TypeScript** → use language-agnostic skills

## Decision Trees

### Validation Library Selection

```
What is your primary requirement?
  │
  ├─ Need OpenAPI/JSON Schema generation?
  │   └─ TypeBox (produces JSON Schema natively)
  │
  ├─ Bundle size critical (frontend)?
  │   └─ Valibot (1/10th Zod's size, tree-shakeable)
  │
  ├─ React form integration primary?
  │   └─ Zod + react-hook-form (best DX for forms)
  │
  ├─ Maximum runtime performance?
  │   └─ TypeBox with compiled validators (5-10x faster than Zod)
  │
  └─ General API validation, no special requirements?
      └─ Zod (best default, largest ecosystem)

Conflict resolution: Need OpenAPI + React forms?
  → Dual-library: TypeBox on backend, Zod on frontend
```

### Type vs Interface

```
Need to extend primitives or union types? → Type alias
Need declaration merging? → Interface
Need mapped/conditional types? → Type alias
Defining object shape only? → Either works; be consistent
```

### unknown vs any

```
External data (API, user input)? → unknown + validation
Library interop requiring any? → Use with immediate narrowing
Generic constraint? → unknown as default
Truly dynamic? → Consider discriminated union first; any is last resort
```

### Generics vs Union Types

```
Related types with shared operations? → Generics
Distinct types with different handling? → Union
Need type preservation through transforms? → Generics
Fixed set of known types? → Union
```

### NestJS Architecture Decision

```
Is business logic complex (more than simple CRUD)?
  │
  ├─ Yes → Clean Architecture
  │   Repository Pattern (abstract data access)
  │   Use Case Pattern (encapsulate business logic)
  │   Dependency Injection wiring
  │
  └─ No → Simple Service Pattern
      Service directly uses ORM
      No Repository/Use Case overhead
```

## Core TypeScript Principles

### Strict Mode Always
```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noPropertyAccessFromIndexSignature": true
  }
}
```

`strict: true` is not enough. The flags beyond `strict` catch real runtime bugs:
- **`noUncheckedIndexedAccess`**: `arr[0]` returns `T | undefined` instead of `T`
- **`exactOptionalPropertyTypes`**: Distinguishes "property missing" from "property is undefined"
- **`noImplicitReturns`**: Catches functions that forget to return a value
- **`noFallthroughCasesInSwitch`**: Prevents accidental switch fallthrough

### No `any` Policy
- Use `unknown` for truly unknown types → validate before use
- Use generics for flexible but type-safe code
- Use type assertions only after validation
- Use `// @ts-expect-error` with comment explaining why (never `// @ts-ignore`)

### Type-Only Imports
```typescript
import type { User, Config } from './types';  // Type-only: erased at runtime
import { createUser } from './utils';          // Value import: kept at runtime
```

## Type System Patterns

### Discriminated Unions for State
```typescript
type AsyncState<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; error: Error };

// Exhaustive switch — compiler catches missing branches
function handleState<T>(state: AsyncState<T>): string {
  switch (state.status) {
    case 'idle': return 'Not started';
    case 'loading': return 'Loading...';
    case 'success': return `Done: ${JSON.stringify(state.data)}`;
    case 'error': return `Failed: ${state.error.message}`;
  }
}
```

### Branded Types for Type Safety
```typescript
declare const __brand: unique symbol;
type Brand<T, B> = T & { [__brand]: B };

type UserId = Brand<string, 'UserId'>;
type OrderId = Brand<string, 'OrderId'>;
type Email = Brand<string, 'Email'>;
type SafeSQL = Brand<string, 'SafeSQL'>;

// Factory functions validate format before branding — never export raw assertion
function createUserId(raw: string): UserId {
  if (!raw.startsWith('usr_')) throw new Error('Invalid UserId format');
  return raw as UserId;
}

// Now passing UserId where OrderId expected is a COMPILE-TIME error
```

### Conditional Types
```typescript
type NonNullableProps<T> = {
  [K in keyof T]: NonNullable<T[K]>
};
type ExtractArrayType<T> = T extends (infer U)[] ? U : never;
type StringKeys<T> = Extract<keyof T, string>;
```

### Mapped Types with Modifiers
```typescript
type Mutable<T> = { -readonly [K in keyof T]: T[K] };
type ReadonlyDeep<T> = {
  readonly [K in keyof T]: T[K] extends object ? ReadonlyDeep<T[K]> : T[K]
};
```

### Template Literal Types
```typescript
type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';
type ApiRoute = `/api/${string}`;
type EventName = `on${Capitalize<string>}`;
```

### Result Type for Error Handling
```typescript
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function ok<T>(value: T): Result<T> { return { ok: true, value }; }
function err<E>(error: E): Result<never, E> { return { ok: false, error }; }

// Compiler enforces handling both branches
function divide(a: number, b: number): Result<number, string> {
  if (b === 0) return err('Division by zero');
  return ok(a / b);
}
```

## Validation Library Quick Reference

| Requirement | Choice |
|-------------|--------|
| General API validation | Zod |
| OpenAPI/JSON Schema needed | TypeBox |
| Bundle size critical | Valibot |
| Maximum performance | TypeBox with compiled validators |
| Form validation in React | Zod + react-hook-form |
| Multiple conflicting requirements | Dual-library strategy (see Decision Tree) |

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| **`strict: true` as the ceiling** | Missing `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes` — runtime nulls from array access and optional properties still crash | Enable all strict flags. Run `scripts/typescript-validator.js` against your tsconfig. |
| **`any` as escape hatch** | `any` disables type checking; bugs that TypeScript was supposed to catch slip through | Use `unknown` + validation, generics, or type guards. If `any` is truly needed for library interop, narrow immediately. |
| **Raw branded type assertion** | Casting with `as UserId` bypasses validation; brand provides false safety | Always create factory functions that validate format before branding. Never export the bare type assertion; export only the factory. |
| **Boolean flags for async state** | `isLoading + isError + data` allows impossible combinations (loading AND error) | Use discriminated union `AsyncState<T>` — compiler catches missing branches and prevents impossible states. |
| **`string` for all IDs** | `UserId` and `OrderId` are both `string` — wrong ID passed silently at runtime | Use branded types to make structurally identical types compiler-incompatible. |
| **TypeBox for everything** | TypeBox's API is verbose for simple cases; React form integration is weaker | Use the decision tree honestly. Zod + react-hook-form is still better DX for frontend forms. |
| **Clean Architecture for simple CRUD** | Repository + Use Case + Controller for endpoints that are just database reads = over-engineering | Clean Architecture pays off when business logic is complex. For simple CRUD, a service directly using ORM is appropriate. |
| **Migrating `any` to `unknown` all at once** | Massive type errors, developer frustration, pressure to revert | Migrate incrementally: API boundaries first, then shared utilities, then internal modules. Each migration is a self-contained PR. |
| **Enabling `noUncheckedIndexedAccess` without batching fixes** | Hundreds of new type errors from every array/object access | Enable the flag but fix errors file-by-file. Use `// @ts-expect-error` with comment as temporary escape hatch for low-priority paths. |
| **`// @ts-ignore` without explanation** | Suppresses error without documentation; future developers don't know why | Always use `// @ts-expect-error` with a comment explaining the reason. It also verifies the error still exists (fails if error is fixed). |

## Common Patterns Quick Reference

| Pattern | Use Case |
|---------|----------|
| Discriminated Union | State machines, API responses, async state |
| Branded Types | IDs, validated strings, preventing mixups |
| Type Guards | Runtime type checking with compile-time narrowing |
| Assertion Functions | Throwing validation with type narrowing |
| Mapped Types | Transforming object types |
| Conditional Types | Type-level logic |
| Template Literals | String pattern types |
| Result Type | Error handling without exceptions |
| Repository Pattern | Data access abstraction |
| Use Case Pattern | Business logic encapsulation |

See [Extended Patterns](references/extended-patterns.md) for detailed code examples including runtime validation, React integration, Clean Architecture, error handling, configuration, and testing patterns.

## Resources

### References
- `references/extended-patterns.md` - Detailed code examples for all patterns
- `references/advanced-types.md` - Conditional types, mapped types, template literals
- `references/advanced-patterns-2025.md` - Latest TypeScript patterns
- `references/runtime-validation.md` - Zod, TypeBox, Valibot deep dive
- `references/decision-trees.md` - Type vs interface, validation library choice
- `references/configuration.md` - tsconfig.json optimization
- `references/troubleshooting.md` - Common errors and solutions
- `references/security-examples.md` - Branded types, sensitive data patterns
- `references/advanced-patterns.md` - Builder pattern, typed events
- `references/typescript-standards.md` - Strict mode, naming conventions
- `references/typescript-patterns.md` - React Native specific patterns
- `references/examples.md` - Complete feature implementation examples
- `references/reference.md` - Clean Architecture, API patterns

### Scripts
- `scripts/typescript-validator.js` - Validates tsconfig.json against recommended strict settings

### Templates
- `templates/typescript-config.json` - Production-ready tsconfig with all strict flags

### Examples
- `examples/nestjs-typeorm-api/` - Complete NestJS + TypeORM REST API with DTOs, entities, services, and modules

## Version Compatibility

- TypeScript 5.x (5.9 features included)
- React 18/19
- Next.js 14/15/16
- Node.js 20+
- NestJS 10+
- ESM and CommonJS
