---
name: typescript-development
description: TypeScript development — use when the user works with TypeScript, type system patterns, generics, Zod, tsconfig, NestJS, branded types, or runtime validation. Covers type system mastery, framework integration, architecture patterns, security, and testing strategies. NOT for Python development (use python-development), NOT for React component patterns or hooks (use react-development), NOT for Next.js framework specifics (use nextjs-development).
---

# TypeScript Development - Comprehensive Skill

A complete TypeScript development skill combining best practices, patterns, and tooling for modern TypeScript development across all application types.

## Overview

This merged skill provides comprehensive TypeScript guidance covering:
- **Type System Mastery**: Advanced types, generics, conditional types, mapped types, template literals
- **Runtime Validation**: Zod, TypeBox, Valibot patterns and comparisons
- **Framework Integration**: React 19, Next.js 16, NestJS, React Native
- **Architecture Patterns**: Clean Architecture, dependency injection, repository patterns
- **Security**: Type-safe validation, branded types, sensitive data handling
- **Configuration**: tsconfig.json optimization, module resolution, strict mode
- **Testing**: Unit testing with mocks, integration testing strategies

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

### No `any` Policy
- Use `unknown` for truly unknown types
- Use generics for flexible but type-safe code
- Use type assertions only with validation
- Use `// @ts-expect-error` with comment explaining why

### Type-Only Imports
```typescript
import type { User, Config } from './types';
import { createUser } from './utils';
```

## Type System Patterns

### Discriminated Unions for State
```typescript
type AsyncState<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; error: Error };
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

### Branded Types for Type Safety
```typescript
declare const __brand: unique symbol;
type Brand<T, B> = T & { [__brand]: B };

type UserId = Brand<string, 'UserId'>;
type Email = Brand<string, 'Email'>;
type SafeSQL = Brand<string, 'SafeSQL'>;
```

## Validation Library Decision Tree

| Requirement | Choice |
|-------------|--------|
| General API validation | Zod |
| OpenAPI/JSON Schema needed | TypeBox |
| Bundle size critical | Valibot |
| Maximum performance | TypeBox with compiled validators |
| Form validation in React | Zod + react-hook-form |

## Decision Trees

### Type vs Interface
```
Need to extend primitives/unions? -> Type alias
Need declaration merging? -> Interface
Need mapped types? -> Type alias
Defining object shape? -> Either works, be consistent
```

### unknown vs any
```
External data (API, user input)? -> unknown + validation
Library interop requiring any? -> Use with immediate narrowing
Generic constraint? -> unknown as default
Truly dynamic? -> Consider discriminated union first
```

### Generics vs Union Types
```
Related types with shared operations? -> Generics
Distinct types with different handling? -> Union
Need type preservation through transforms? -> Generics
Fixed set of known types? -> Union
```

## Common Patterns Quick Reference

| Pattern | Use Case |
|---------|----------|
| Discriminated Union | State machines, API responses |
| Branded Types | IDs, validated strings |
| Type Guards | Runtime type checking |
| Assertion Functions | Throwing validation |
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
- `scripts/typescript-validator.js` - TypeScript configuration validation

### Templates
- `templates/typescript-config.json` - Recommended tsconfig.json template

### Examples
- `examples/nestjs-typeorm-api/` - Complete NestJS + TypeORM REST API example

## Version Compatibility

This skill targets:
- TypeScript 5.x (5.9 features included)
- React 18/19
- Next.js 14/15/16
- Node.js 20+
- NestJS 10+

All patterns are compatible with both ESM and CommonJS module systems.
