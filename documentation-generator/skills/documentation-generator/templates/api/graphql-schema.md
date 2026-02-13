# GraphQL API Reference

Complete GraphQL API documentation for {{PROJECT_NAME}}.

## Endpoint

| Environment | URL |
|-------------|-----|
| Production | `{{PROD_GRAPHQL_URL}}` |
| Staging | `{{STAGING_GRAPHQL_URL}}` |

## Authentication

Include the authentication token in the request header:

```
Authorization: Bearer {{AUTH_TOKEN}}
```

## Schema Overview

### Types

{{#TYPES}}
#### {{TYPE_NAME}}

{{TYPE_DESCRIPTION}}

```graphql
type {{TYPE_NAME}} {
{{#FIELDS}}
  {{FIELD_NAME}}: {{FIELD_TYPE}}  # {{FIELD_DESC}}
{{/FIELDS}}
}
```

| Field | Type | Description |
|-------|------|-------------|
{{#FIELDS}}
| `{{FIELD_NAME}}` | `{{FIELD_TYPE}}` | {{FIELD_DESC}} |
{{/FIELDS}}

{{/TYPES}}

### Enums

{{#ENUMS}}
#### {{ENUM_NAME}}

```graphql
enum {{ENUM_NAME}} {
{{#VALUES}}
  {{VALUE}}
{{/VALUES}}
}
```

| Value | Description |
|-------|-------------|
{{#VALUES}}
| `{{VALUE}}` | {{VALUE_DESC}} |
{{/VALUES}}

{{/ENUMS}}

### Input Types

{{#INPUTS}}
#### {{INPUT_NAME}}

```graphql
input {{INPUT_NAME}} {
{{#FIELDS}}
  {{FIELD_NAME}}: {{FIELD_TYPE}}
{{/FIELDS}}
}
```

{{/INPUTS}}

## Queries

{{#QUERIES}}
### {{QUERY_NAME}}

{{QUERY_DESCRIPTION}}

```graphql
query {
  {{QUERY_NAME}}{{#HAS_ARGS}}({{ARGS_EXAMPLE}}){{/HAS_ARGS}} {
    {{RETURN_FIELDS}}
  }
}
```

**Arguments:**

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
{{#ARGS}}
| `{{ARG_NAME}}` | `{{ARG_TYPE}}` | {{REQUIRED}} | {{ARG_DESC}} |
{{/ARGS}}

**Returns:** `{{RETURN_TYPE}}`

**Example:**

```graphql
{{QUERY_EXAMPLE}}
```

**Response:**

```json
{{QUERY_RESPONSE}}
```

{{/QUERIES}}

## Mutations

{{#MUTATIONS}}
### {{MUTATION_NAME}}

{{MUTATION_DESCRIPTION}}

```graphql
mutation {
  {{MUTATION_NAME}}(input: {{INPUT_TYPE}}) {
    {{RETURN_FIELDS}}
  }
}
```

**Input:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
{{#INPUT_FIELDS}}
| `{{FIELD_NAME}}` | `{{FIELD_TYPE}}` | {{REQUIRED}} | {{FIELD_DESC}} |
{{/INPUT_FIELDS}}

**Returns:** `{{RETURN_TYPE}}`

**Example:**

```graphql
{{MUTATION_EXAMPLE}}
```

**Response:**

```json
{{MUTATION_RESPONSE}}
```

{{/MUTATIONS}}

## Subscriptions

{{#SUBSCRIPTIONS}}
### {{SUBSCRIPTION_NAME}}

{{SUBSCRIPTION_DESCRIPTION}}

```graphql
subscription {
  {{SUBSCRIPTION_NAME}}{{#HAS_ARGS}}({{ARGS_EXAMPLE}}){{/HAS_ARGS}} {
    {{RETURN_FIELDS}}
  }
}
```

**Arguments:**

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
{{#ARGS}}
| `{{ARG_NAME}}` | `{{ARG_TYPE}}` | {{REQUIRED}} | {{ARG_DESC}} |
{{/ARGS}}

{{/SUBSCRIPTIONS}}

## Pagination

### Connection Pattern

All list queries use Relay-style cursor pagination:

```graphql
query {
  {{LIST_QUERY}}(first: 10, after: "cursor") {
    edges {
      node {
        id
        # ... fields
      }
      cursor
    }
    pageInfo {
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
    totalCount
  }
}
```

**Pagination Arguments:**

| Argument | Type | Description |
|----------|------|-------------|
| `first` | `Int` | Return first N items |
| `after` | `String` | Cursor to start after |
| `last` | `Int` | Return last N items |
| `before` | `String` | Cursor to end before |

## Filtering

### Using Where Clause

```graphql
query {
  {{LIST_QUERY}}(where: {
    status: { eq: ACTIVE }
    createdAt: { gte: "2024-01-01" }
  }) {
    # ...
  }
}
```

### Filter Operators

| Operator | Types | Description |
|----------|-------|-------------|
| `eq` | All | Equals |
| `ne` | All | Not equals |
| `in` | All | In list |
| `notIn` | All | Not in list |
| `lt` | Number, Date | Less than |
| `lte` | Number, Date | Less than or equal |
| `gt` | Number, Date | Greater than |
| `gte` | Number, Date | Greater than or equal |
| `contains` | String | Contains substring |
| `startsWith` | String | Starts with |
| `endsWith` | String | Ends with |

## Sorting

```graphql
query {
  {{LIST_QUERY}}(orderBy: [
    { field: CREATED_AT, direction: DESC },
    { field: NAME, direction: ASC }
  ]) {
    # ...
  }
}
```

## Error Handling

### Error Response Format

```json
{
  "data": null,
  "errors": [
    {
      "message": "Error description",
      "locations": [{ "line": 2, "column": 3 }],
      "path": ["{{QUERY_NAME}}", "field"],
      "extensions": {
        "code": "{{ERROR_CODE}}",
        "details": {}
      }
    }
  ]
}
```

### Common Error Codes

| Code | Description |
|------|-------------|
| `UNAUTHENTICATED` | Missing or invalid authentication |
| `FORBIDDEN` | Insufficient permissions |
| `NOT_FOUND` | Resource not found |
| `VALIDATION_ERROR` | Input validation failed |
| `INTERNAL_ERROR` | Server error |

## Rate Limiting

GraphQL queries have complexity-based rate limiting:

- **Query complexity limit:** {{COMPLEXITY_LIMIT}} points
- **Rate limit:** {{RATE_LIMIT}} queries/minute

### Checking Rate Limit Status

Include in query:
```graphql
query {
  {{QUERY_NAME}} {
    # ...
  }
  _rateLimit {
    remaining
    resetAt
  }
}
```

## Best Practices

### Query Optimization

1. **Only request needed fields** - Don't select entire types
2. **Use pagination** - Avoid unbounded lists
3. **Batch related queries** - Combine in single request
4. **Use fragments** - Reduce repetition

### Example: Optimized Query

```graphql
fragment {{FRAGMENT_NAME}} on {{TYPE_NAME}} {
  id
  {{FRAGMENT_FIELDS}}
}

query GetData($id: ID!, $first: Int = 10) {
  {{QUERY_1}}(id: $id) {
    ...{{FRAGMENT_NAME}}
    related(first: $first) {
      edges {
        node {
          ...{{FRAGMENT_NAME}}
        }
      }
    }
  }
}
```

## Introspection

Query the schema:

```graphql
query {
  __schema {
    types {
      name
      description
      fields {
        name
        type {
          name
        }
      }
    }
  }
}
```

## Tools

- **GraphQL Playground:** {{PLAYGROUND_URL}}
- **Schema Download:** {{SCHEMA_URL}}
- **SDK Generator:** {{CODEGEN_URL}}
