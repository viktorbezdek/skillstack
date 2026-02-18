# TypeScript Development

> Comprehensive TypeScript skill covering type system mastery, runtime validation, framework integration, architecture patterns, security, and configuration optimization.

## Overview

TypeScript's power lies in its type system, but unlocking that power requires deep knowledge of advanced patterns, runtime validation strategies, and framework-specific conventions. This skill provides a complete guide to modern TypeScript development, from discriminated unions and branded types to Zod/TypeBox/Valibot validation, React 19 and Next.js 16 integration, NestJS architecture, and tsconfig optimization.

The skill is aimed at developers who want to go beyond basic TypeScript and adopt patterns that catch bugs at compile time, enforce invariants at runtime, and scale across large codebases. It includes decision trees for common choices (type vs interface, which validation library, generics vs unions) so you can make informed decisions quickly.

Within the SkillStack collection, this skill pairs with react-development for frontend work, nextjs-development for full-stack applications, and test-driven-development for type-safe testing strategies.

## What's Included

### References

- `references/extended-patterns.md` - Detailed code examples for all patterns including runtime validation, React integration, Clean Architecture, error handling, and testing
- `references/advanced-types.md` - Conditional types, mapped types, template literal types, and type inference
- `references/advanced-patterns-2025.md` - Latest TypeScript 5.x patterns and features
- `references/runtime-validation.md` - Deep dive into Zod, TypeBox, and Valibot with comparisons
- `references/decision-trees.md` - Decision guides for type vs interface, validation library choice, generics vs unions
- `references/configuration.md` - tsconfig.json optimization and module resolution strategies
- `references/troubleshooting.md` - Common TypeScript errors and their solutions
- `references/security-examples.md` - Branded types, sensitive data handling, and SafeSQL patterns
- `references/advanced-patterns.md` - Builder pattern, typed event emitters, and middleware types
- `references/typescript-standards.md` - Strict mode configuration and naming conventions
- `references/typescript-patterns.md` - React Native specific TypeScript patterns
- `references/examples.md` - Complete feature implementation examples end-to-end
- `references/reference.md` - Clean Architecture patterns, API design, and repository patterns

### Templates

- `templates/typescript-config.json` - Recommended tsconfig.json with strict mode and optimal settings

### Scripts

- `scripts/typescript-validator.js` - TypeScript configuration validator that checks for best practices and potential issues

### Examples

- `examples/nestjs-typeorm-api/` - Complete NestJS + TypeORM REST API example with:
  - `src/app.module.ts` - Application module configuration
  - `src/main.ts` - Application entry point
  - `src/users/user.entity.ts` - TypeORM entity with decorators
  - `src/users/users.controller.ts` - REST controller with validation
  - `src/users/users.service.ts` - Service layer with business logic
  - `src/users/users.module.ts` - Feature module definition
  - `src/users/dto/create-user.dto.ts` - Data transfer object with validation

## Key Features

- **Advanced type system patterns** including discriminated unions, conditional types, mapped types, template literals, and branded types
- **Runtime validation** with Zod, TypeBox, and Valibot including a decision tree for choosing the right library
- **Framework integration** for React 19, Next.js 16, NestJS 10+, and React Native
- **Clean Architecture** patterns with repository, use case, and dependency injection
- **Security patterns** with branded types for UserId, Email, and SafeSQL to prevent type confusion attacks
- **tsconfig optimization** covering strict mode, module resolution, and performance tuning
- **No-any policy** enforcement with unknown, generics, and type guards as safer alternatives
- **Decision trees** for type vs interface, generics vs unions, and validation library selection

## Usage Examples

### Set up a new TypeScript project with strict configuration

```
Create a tsconfig.json for a Node.js 20 API project with maximum type safety, ESM modules, and path aliases.
```

Produces an optimized tsconfig.json with strict mode, noUncheckedIndexedAccess, exactOptionalPropertyTypes, and proper module resolution.

### Build a type-safe API with NestJS

```
Create a NestJS REST API for a product catalog with TypeORM entities, Zod validation DTOs, and proper error handling using discriminated unions.
```

Generates a complete NestJS module with entity, controller, service, and DTO files following Clean Architecture and the Result type pattern for error handling.

### Design a branded type system for domain safety

```
Create branded types for my e-commerce domain: ProductId, OrderId, UserId, Email, and MoneyAmount. Include factory functions with validation.
```

Produces branded type definitions with runtime validation factory functions that ensure IDs cannot be mixed up and values are always validated.

### Add Zod validation to an existing API

```
Add Zod schemas for my user registration endpoint. Validate email format, password strength (min 8, uppercase, number, special char), and age (18+).
```

Creates Zod schemas with custom refinements, produces inferred TypeScript types, and integrates with the request handler.

### Troubleshoot a complex type error

```
I'm getting "Type 'string' is not assignable to type 'never'" when using a switch statement on a discriminated union. How do I fix it?
```

Explains the exhaustive check pattern, shows how to add the `assertNever` helper, and identifies the missing union case causing the error.

## Quick Start

1. **Enable strict mode** - Start with `templates/typescript-config.json` as your base configuration. Enable all strict checks.
2. **Adopt type-only imports** - Use `import type { ... }` for types to improve build performance and clarity.
3. **Choose your validation library** - Use the decision tree in `references/decision-trees.md` to pick between Zod (general), TypeBox (OpenAPI), or Valibot (small bundles).
4. **Use discriminated unions** - Model state machines and API responses with discriminated unions instead of optional fields.
5. **Apply branded types** - For domain IDs and validated strings, use branded types from `references/security-examples.md` to prevent type confusion.
6. **Validate your config** - Run `scripts/typescript-validator.js` against your tsconfig to check for issues.

## Related Skills

- [react-development](../react-development/) - React component patterns with TypeScript integration
- [nextjs-development](../nextjs-development/) - Next.js full-stack development with TypeScript
- [test-driven-development](../test-driven-development/) - TDD with Vitest and Zod validation testing
- [testing-framework](../testing-framework/) - Multi-framework testing including TypeScript/Vitest
- [api-design](../api-design/) - API design patterns complementing TypeScript backend development

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install typescript-development@skillstack` — 34 production-grade skills for Claude Code.
