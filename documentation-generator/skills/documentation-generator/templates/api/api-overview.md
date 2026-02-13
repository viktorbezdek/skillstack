# API Reference

Complete API documentation for {{PROJECT_NAME}}.

## Overview

{{API_DESCRIPTION}}

### Base URL

| Environment | URL |
|-------------|-----|
| Production | `{{PROD_API_URL}}` |
| Staging | `{{STAGING_API_URL}}` |
| Development | `{{DEV_API_URL}}` |

### API Versioning

The API version is specified in the URL path: `/api/v1/...`

Current version: **v{{API_VERSION}}**

## Authentication

{{PROJECT_NAME}} uses {{AUTH_METHOD}} for API authentication.

### {{AUTH_METHOD_NAME}}

{{AUTH_DESCRIPTION}}

**Request Header:**
```
Authorization: {{AUTH_SCHEME}} {{AUTH_TOKEN_PLACEHOLDER}}
```

**Example:**
```bash
curl -X GET "{{API_URL}}/endpoint" \
  -H "Authorization: {{AUTH_SCHEME}} your_token_here"
```

### Obtaining Credentials

{{AUTH_OBTAINING_INSTRUCTIONS}}

### Token Expiration

| Token Type | Lifetime | Refresh |
|------------|----------|---------|
{{#TOKEN_TYPES}}
| {{TYPE}} | {{LIFETIME}} | {{REFRESH_METHOD}} |
{{/TOKEN_TYPES}}

## Request Format

### Headers

| Header | Required | Description |
|--------|----------|-------------|
| `Authorization` | Yes | Authentication token |
| `Content-Type` | Yes* | `application/json` for POST/PUT/PATCH |
| `Accept` | No | `application/json` (default) |
| `X-Request-ID` | No | Unique request identifier for tracing |

### Request Body

All request bodies must be valid JSON:

```json
{
  "field": "value",
  "nested": {
    "field": "value"
  }
}
```

### Query Parameters

- Use `snake_case` for parameter names
- Boolean values: `true` or `false`
- Arrays: `?ids=1,2,3` or `?ids[]=1&ids[]=2`
- Dates: ISO 8601 format (`2024-01-15T10:30:00Z`)

## Response Format

### Success Response

```json
{
  "data": {
    // Response data
  },
  "meta": {
    "request_id": "req_abc123",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

### Collection Response

```json
{
  "data": [
    // Array of items
  ],
  "meta": {
    "total": 100,
    "page": 1,
    "per_page": 20,
    "total_pages": 5
  },
  "links": {
    "self": "/api/v1/items?page=1",
    "next": "/api/v1/items?page=2",
    "prev": null,
    "first": "/api/v1/items?page=1",
    "last": "/api/v1/items?page=5"
  }
}
```

### Error Response

```json
{
  "error": {
    "code": "{{ERROR_CODE}}",
    "message": "Human-readable error message",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  },
  "meta": {
    "request_id": "req_abc123",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

## HTTP Status Codes

### Success Codes

| Code | Meaning | Use Case |
|------|---------|----------|
| `200` | OK | Successful GET, PUT, PATCH, DELETE |
| `201` | Created | Successful POST (resource created) |
| `204` | No Content | Successful DELETE (no response body) |

### Client Error Codes

| Code | Meaning | Use Case |
|------|---------|----------|
| `400` | Bad Request | Invalid request format/parameters |
| `401` | Unauthorized | Missing or invalid authentication |
| `403` | Forbidden | Valid auth but insufficient permissions |
| `404` | Not Found | Resource doesn't exist |
| `409` | Conflict | Resource conflict (e.g., duplicate) |
| `422` | Unprocessable Entity | Validation errors |
| `429` | Too Many Requests | Rate limit exceeded |

### Server Error Codes

| Code | Meaning | Use Case |
|------|---------|----------|
| `500` | Internal Server Error | Unexpected server error |
| `502` | Bad Gateway | Upstream service error |
| `503` | Service Unavailable | Temporary unavailability |
| `504` | Gateway Timeout | Upstream service timeout |

## Pagination

### Query Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | integer | 1 | Page number (1-indexed) |
| `per_page` | integer | 20 | Items per page (max: 100) |
| `sort` | string | varies | Sort field (`field` or `-field` for desc) |

### Example

```bash
GET /api/v1/items?page=2&per_page=50&sort=-created_at
```

### Cursor-based Pagination

For large datasets, use cursor pagination:

```bash
GET /api/v1/items?cursor=eyJpZCI6MTAwfQ&limit=50
```

Response includes `next_cursor`:
```json
{
  "data": [...],
  "meta": {
    "next_cursor": "eyJpZCI6MTUwfQ",
    "has_more": true
  }
}
```

## Filtering

### Basic Filtering

```bash
GET /api/v1/items?status=active&type=premium
```

### Operators

| Operator | Example | Description |
|----------|---------|-------------|
| `eq` | `?status[eq]=active` | Equals (default) |
| `ne` | `?status[ne]=deleted` | Not equals |
| `gt` | `?price[gt]=100` | Greater than |
| `gte` | `?price[gte]=100` | Greater than or equal |
| `lt` | `?price[lt]=100` | Less than |
| `lte` | `?price[lte]=100` | Less than or equal |
| `in` | `?status[in]=active,pending` | In list |
| `contains` | `?name[contains]=test` | Contains string |

### Date Filtering

```bash
GET /api/v1/items?created_at[gte]=2024-01-01&created_at[lt]=2024-02-01
```

## Rate Limiting

### Limits

| Plan | Requests/minute | Requests/day |
|------|-----------------|--------------|
| Free | {{FREE_RPM}} | {{FREE_RPD}} |
| Pro | {{PRO_RPM}} | {{PRO_RPD}} |
| Enterprise | Custom | Custom |

### Rate Limit Headers

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1642234567
```

### Handling Rate Limits

When rate limited (429 response):
1. Check `Retry-After` header for wait time
2. Implement exponential backoff
3. Consider upgrading your plan

## Webhooks

### Supported Events

| Event | Description | Payload |
|-------|-------------|---------|
{{#WEBHOOK_EVENTS}}
| `{{EVENT_NAME}}` | {{EVENT_DESC}} | [See payload](#{{EVENT_ANCHOR}}) |
{{/WEBHOOK_EVENTS}}

### Webhook Payload

```json
{
  "event": "{{EVENT_NAME}}",
  "timestamp": "2024-01-15T10:30:00Z",
  "data": {
    // Event-specific data
  }
}
```

### Verifying Webhooks

```{{CODE_LANGUAGE}}
{{WEBHOOK_VERIFICATION_CODE}}
```

## SDKs & Libraries

| Language | Package | Documentation |
|----------|---------|---------------|
{{#SDKS}}
| {{LANGUAGE}} | `{{PACKAGE}}` | [Docs]({{DOCS_URL}}) |
{{/SDKS}}

## API Endpoints

{{#ENDPOINT_CATEGORIES}}
### {{CATEGORY_NAME}}

{{CATEGORY_DESCRIPTION}}

| Method | Endpoint | Description |
|--------|----------|-------------|
{{#ENDPOINTS}}
| `{{METHOD}}` | `{{PATH}}` | {{DESCRIPTION}} |
{{/ENDPOINTS}}

[Full {{CATEGORY_NAME}} documentation →](./{{CATEGORY_SLUG}}.md)

{{/ENDPOINT_CATEGORIES}}

## Changelog

### v{{API_VERSION}} (Current)

- {{CHANGELOG_ITEM_1}}
- {{CHANGELOG_ITEM_2}}

### v{{PREV_VERSION}}

- {{PREV_CHANGELOG_1}}
- {{PREV_CHANGELOG_2}}

## Support

- 📧 API Support: {{API_SUPPORT_EMAIL}}
- 📖 Developer Portal: {{DEV_PORTAL_URL}}
- 💬 Community: {{COMMUNITY_URL}}
