# API Versioning Strategies

Comprehensive guide to versioning APIs, managing breaking changes, and deprecating old versions.

## Table of Contents

- [Versioning Approaches](#versioning-approaches)
- [When to Version](#when-to-version)
- [Deprecation Process](#deprecation-process)
- [Migration Strategies](#migration-strategies)
- [Best Practices](#best-practices)

## Versioning Approaches

### URL Versioning

**Pattern**: Include version in URL path

```
https://api.example.com/v1/users
https://api.example.com/v2/users
https://api.example.com/v3/users
```

**Pros**:
- Very explicit and visible
- Easy to route to different codebases
- Simple to understand for developers
- Good for major breaking changes
- Easy to cache (different URLs)
- Browser-testable

**Cons**:
- URL proliferation
- Requires maintaining multiple codebases
- Can lead to code duplication
- Makes it harder to sunset old versions

**When to Use**:
- Major version changes with significant breaking changes
- When you need to maintain multiple versions long-term
- Public APIs consumed by many clients
- When you want maximum clarity

**Implementation Example**:
```python
# Flask example
from flask import Flask

app = Flask(__name__)

# Version 1
@app.route('/v1/users')
def get_users_v1():
    return {"users": [...], "version": "1.0"}

# Version 2
@app.route('/v2/users')
def get_users_v2():
    return {"data": {"users": [...]}, "version": "2.0"}
```

### Header Versioning

**Pattern**: Include version in request header

```http
GET /users
Accept: application/vnd.myapi.v2+json

# Or
GET /users
API-Version: 2

# Or
GET /users
Accept-Version: 2.0
```

**Pros**:
- Clean URLs (no version pollution)
- Same endpoint for all versions
- Good for content negotiation
- Follows HTTP standards (Accept header)
- Flexible versioning per resource

**Cons**:
- Less visible (harder to discover)
- Harder to test in browser
- Can complicate caching
- More complex routing logic
- May confuse some developers

**When to Use**:
- When you want clean URLs
- APIs with frequent minor updates
- Content negotiation is important
- Internal or partner APIs

**Implementation Example**:
```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/users')
def get_users():
    version = request.headers.get('API-Version', '1')

    if version == '2':
        return {"data": {"users": [...]}, "version": "2.0"}
    else:
        return {"users": [...], "version": "1.0"}
```

### Query Parameter Versioning

**Pattern**: Include version in query string

```
GET /users?version=2
GET /users?api-version=2.0
GET /users?v=2
```

**Pros**:
- Simple to implement
- Easy to test
- Optional (can have default version)
- Works well with existing infrastructure

**Cons**:
- Not RESTful
- Can be accidentally omitted
- Harder to enforce
- Caching complications
- Query params should be for filtering, not versioning

**When to Use**:
- Quick prototypes or internal tools
- When you need easy testing
- Temporary versioning before better solution

**Not Recommended**: Generally avoid this approach for production APIs

### Semantic Versioning

**Format**: MAJOR.MINOR.PATCH (e.g., 2.1.3)

```
GET /v2.1/users  # Less common
# Or in header
API-Version: 2.1.3
```

**Version Components**:
- **MAJOR**: Breaking changes (v1 -> v2)
- **MINOR**: New features, backward compatible (v2.1 -> v2.2)
- **PATCH**: Bug fixes, backward compatible (v2.1.1 -> v2.1.2)

**Best Practices**:
- Only include MAJOR version in URL/header
- Track MINOR/PATCH in response headers
- Communicate MINOR/PATCH in API documentation

```http
Response Headers:
API-Version: 2
API-Version-Full: 2.1.3
```

## When to Version

### Create New Version For

**Breaking Changes**:
- Removing endpoints
- Removing request/response fields
- Changing field data types
- Renaming fields
- Changing authentication methods
- Modifying error response structure
- Changing HTTP status codes
- Altering request/response semantics

**Examples**:
```json
// V1
{
  "user_id": "123",  // Field name changed
  "email": "test@example.com"
}

// V2
{
  "id": "123",       // Breaking: renamed field
  "email": "test@example.com"
}
```

### Don't Version For

**Backward Compatible Changes**:
- Adding new optional fields to responses
- Adding new endpoints
- Adding new optional query parameters
- Bug fixes
- Performance improvements
- Internal refactoring
- Documentation updates
- Adding new optional request fields

## Deprecation Process

### Deprecation Timeline

**Recommended Process**:

```
Month 0: Announce deprecation
  |
Month 1-3: Deprecation warnings in responses
  |
Month 3-6: Migration support and documentation
  |
Month 6: Final warning (30 days to sunset)
  |
Month 7: Sunset (remove old version)
```

### Deprecation Headers

```http
# Standard headers
Sunset: Sat, 31 Dec 2025 23:59:59 GMT
Deprecation: true
Link: <https://docs.example.com/migration/v1-to-v2>; rel="deprecation"

# Custom headers for more detail
X-API-Deprecated: true
X-API-Sunset-Date: 2025-12-31
X-API-Migration-Guide: https://docs.example.com/migration/v1-to-v2
```

### Deprecation Warnings in Response

```json
{
  "data": {
    "users": [...]
  },
  "warnings": [
    {
      "code": "DEPRECATED_VERSION",
      "message": "API v1 is deprecated and will be removed on 2025-12-31",
      "severity": "warning",
      "migrationGuide": "https://docs.example.com/migration/v1-to-v2",
      "sunsetDate": "2025-12-31T23:59:59Z"
    }
  ]
}
```

## Migration Strategies

### Parallel Running

**Strategy**: Run both versions simultaneously

```
v1: https://api.example.com/v1/users (deprecated)
v2: https://api.example.com/v2/users (current)
```

### Adapter Pattern

**Strategy**: Maintain one codebase, transform responses

```python
def get_users():
    # Core business logic
    users = fetch_users_from_db()

    # Version-specific transformation
    version = get_api_version()
    if version == 1:
        return transform_to_v1(users)
    elif version == 2:
        return transform_to_v2(users)
```

### Database Versioning

**Expand-Contract Pattern**:
```sql
-- Phase 1: Expand (add new column, keep old)
ALTER TABLE users ADD COLUMN email_address VARCHAR(255);

-- Phase 2: Dual writes (write to both columns)
UPDATE users SET email_address = email;

-- Phase 3: Migrate clients to new field

-- Phase 4: Contract (remove old column)
ALTER TABLE users DROP COLUMN email;
```

## Best Practices

### Version Numbering

**Recommendations**:
- Start with v1 (not v0)
- Use integers for major versions (v1, v2, v3)
- Increment thoughtfully (v1 -> v2 is significant)
- Consider semantic versioning internally
- Document what each version includes

**Avoid**:
- Dates in versions (v2025, v20251025)
- Too many major versions (v1 -> v2 -> v3 in 6 months)
- Fractional versions in URL (v1.5)

### Support Policy

**Define Clear Policies**:
```markdown
## Version Support Policy

- **Current Version**: Full support, active development
- **Previous Version**: Security updates only, 12 months after new version release
- **Deprecated Versions**: No support, will be sunset after notice period

## Deprecation Notice Period

- Minor changes: 3 months minimum
- Major changes: 6 months minimum
- Critical breaking changes: 12 months minimum
```

### Monitoring and Metrics

**Track**:
- Requests per version
- Unique clients per version
- Error rates per version
- Response times per version
- Adoption rate of new version

### Avoid Version Hell

**Don't**:
- Support too many versions simultaneously (3+ active versions)
- Make breaking changes too frequently
- Skip version numbers arbitrarily
- Use confusing version schemes

**Do**:
- Plan major versions carefully
- Extend deprecation periods when usage is high
- Provide excellent migration documentation
- Offer migration assistance for large customers
- Consider backward compatibility first
