# Commit Examples Reference

Quick examples for Claude to reference when helping users.

## Common Scenarios

### New Feature
```
feat(auth): add OAuth2 login support

Integrate Google and GitHub OAuth providers with
automatic account linking for existing users.

Closes #234
```

### Bug Fix
```
fix(api): prevent null pointer in user lookup

Add null check before accessing user.profile to avoid
crashes when profile hasn't been initialized yet.
```

### Breaking Change
```
feat(api)!: change response format to include metadata

BREAKING CHANGE:

All API responses now return {data, meta} instead of
raw data. Update clients to access response.data.

Migration: https://docs.example.com/v2-migration
```

### Performance
```
perf(database): add composite index on user queries

Reduces average query time from 2.1s to 45ms for
user search endpoint.
```

### Refactor
```
refactor(auth): extract validation to separate module

Move authentication validation logic from controllers
to dedicated service for better testability.
```

### Documentation
```
docs(api): add OpenAPI specification

Add complete API documentation with request/response
examples for all endpoints.
```

### Simple Commits
```
feat: add email notifications
fix: correct timezone handling  
docs: update README
style: format with prettier
test: add unit tests for auth
build: update dependencies
chore: update .gitignore
```

## Edge Cases

### Multiple Related Issues
```
fix(payment): resolve duplicate charge issues

Fixes #123, #456, #789
```

### Revert
```
revert: "feat(api): add caching layer"

This reverts commit a1b2c3d. Caching caused data
staleness issues in production.
```

### Initial Commit
```
chore: init
```

## Breaking Change Patterns

### API Change
```
feat(api)!: remove deprecated v1 endpoints

BREAKING CHANGE:

Removed endpoints:
- GET /v1/users
- POST /v1/users  

Use /v2/users instead with updated auth headers.
```

### Database Schema
```
refactor(db)!: normalize user table structure

BREAKING CHANGE:

Split user.name into user.firstName and user.lastName.
Run migration: npm run migrate:user-schema
```

### Config Change
```
build!: require Node.js 18+

BREAKING CHANGE:

Node.js 16 is no longer supported. Upgrade to Node 18
before deploying this version.
```

## What NOT to Do

### Too Vague
```
❌ fix: bug fix
✅ fix(auth): prevent session timeout on refresh
```

### Past Tense
```
❌ feat: added new feature
✅ feat: add new feature
```

### Capitalized
```
❌ feat: Add new feature
✅ feat: add new feature
```

### With Period
```
❌ feat: add new feature.
✅ feat: add new feature
```

### Issue as Scope
```
❌ feat(#123): add feature
✅ feat(api): add feature

Closes #123
```
