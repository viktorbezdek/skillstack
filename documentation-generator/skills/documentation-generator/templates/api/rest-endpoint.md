# API Reference

## Overview

{{API_DESCRIPTION}}

**Base URL:** `{{BASE_URL}}`

**Version:** `{{API_VERSION}}`

## Authentication

{{AUTH_DESCRIPTION}}

### Using API Key

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" {{BASE_URL}}/endpoint
```

### Using OAuth 2.0

```bash
# 1. Get access token
curl -X POST {{BASE_URL}}/oauth/token \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "grant_type=client_credentials"

# 2. Use token in requests
curl -H "Authorization: Bearer ACCESS_TOKEN" {{BASE_URL}}/endpoint
```

## Rate Limiting

| Tier | Requests/minute | Requests/day |
|------|-----------------|--------------|
| Free | 60 | 1,000 |
| Pro | 600 | 50,000 |
| Enterprise | Unlimited | Unlimited |

Rate limit headers:
- `X-RateLimit-Limit`: Maximum requests per window
- `X-RateLimit-Remaining`: Remaining requests in window
- `X-RateLimit-Reset`: Unix timestamp when window resets

## Endpoints

### {{RESOURCE_NAME}}

#### List {{RESOURCE_NAME}}s

```http
GET /{{RESOURCE_PATH}}
```

**Description:** Retrieve a list of {{RESOURCE_NAME}}s.

**Query Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `page` | integer | No | Page number (default: 1) |
| `limit` | integer | No | Items per page (default: 20, max: 100) |
| `sort` | string | No | Sort field (e.g., `created_at`, `-name`) |
| `filter` | string | No | Filter expression |

**Request Example:**

```bash
curl -X GET "{{BASE_URL}}/{{RESOURCE_PATH}}?page=1&limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Response Example:**

```json
{
  "data": [
    {
      "id": "{{RESOURCE_ID}}",
      "{{FIELD_1}}": "{{VALUE_1}}",
      "{{FIELD_2}}": "{{VALUE_2}}",
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T10:30:00Z"
    }
  ],
  "meta": {
    "page": 1,
    "limit": 10,
    "total": 100,
    "total_pages": 10
  }
}
```

---

#### Get {{RESOURCE_NAME}}

```http
GET /{{RESOURCE_PATH}}/{id}
```

**Description:** Retrieve a single {{RESOURCE_NAME}} by ID.

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | string | {{RESOURCE_NAME}} ID |

**Request Example:**

```bash
curl -X GET "{{BASE_URL}}/{{RESOURCE_PATH}}/{{RESOURCE_ID}}" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Response Example:**

```json
{
  "data": {
    "id": "{{RESOURCE_ID}}",
    "{{FIELD_1}}": "{{VALUE_1}}",
    "{{FIELD_2}}": "{{VALUE_2}}",
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  }
}
```

---

#### Create {{RESOURCE_NAME}}

```http
POST /{{RESOURCE_PATH}}
```

**Description:** Create a new {{RESOURCE_NAME}}.

**Request Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `{{FIELD_1}}` | string | Yes | {{FIELD_1_DESC}} |
| `{{FIELD_2}}` | string | No | {{FIELD_2_DESC}} |

**Request Example:**

```bash
curl -X POST "{{BASE_URL}}/{{RESOURCE_PATH}}" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "{{FIELD_1}}": "{{VALUE_1}}",
    "{{FIELD_2}}": "{{VALUE_2}}"
  }'
```

**Response Example:**

```json
{
  "data": {
    "id": "{{RESOURCE_ID}}",
    "{{FIELD_1}}": "{{VALUE_1}}",
    "{{FIELD_2}}": "{{VALUE_2}}",
    "created_at": "2024-01-15T10:30:00Z"
  }
}
```

---

#### Update {{RESOURCE_NAME}}

```http
PATCH /{{RESOURCE_PATH}}/{id}
```

**Description:** Update an existing {{RESOURCE_NAME}}.

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | string | {{RESOURCE_NAME}} ID |

**Request Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `{{FIELD_1}}` | string | No | {{FIELD_1_DESC}} |
| `{{FIELD_2}}` | string | No | {{FIELD_2_DESC}} |

**Request Example:**

```bash
curl -X PATCH "{{BASE_URL}}/{{RESOURCE_PATH}}/{{RESOURCE_ID}}" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "{{FIELD_1}}": "updated value"
  }'
```

---

#### Delete {{RESOURCE_NAME}}

```http
DELETE /{{RESOURCE_PATH}}/{id}
```

**Description:** Delete a {{RESOURCE_NAME}}.

**Request Example:**

```bash
curl -X DELETE "{{BASE_URL}}/{{RESOURCE_PATH}}/{{RESOURCE_ID}}" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Response:** `204 No Content`

---

## Error Codes

| Code | Name | Description |
|------|------|-------------|
| 400 | Bad Request | Invalid request body or parameters |
| 401 | Unauthorized | Missing or invalid authentication |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource not found |
| 409 | Conflict | Resource already exists |
| 422 | Unprocessable Entity | Validation error |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error |

### Error Response Format

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request body",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```

## Pagination

All list endpoints support pagination:

```json
{
  "data": [...],
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "total_pages": 5
  },
  "links": {
    "self": "/{{RESOURCE_PATH}}?page=1&limit=20",
    "first": "/{{RESOURCE_PATH}}?page=1&limit=20",
    "last": "/{{RESOURCE_PATH}}?page=5&limit=20",
    "next": "/{{RESOURCE_PATH}}?page=2&limit=20",
    "prev": null
  }
}
```

## Filtering

Use the `filter` query parameter for complex queries:

```
GET /{{RESOURCE_PATH}}?filter[status]=active&filter[created_at][gte]=2024-01-01
```

Supported operators:
- `eq` - Equal (default)
- `ne` - Not equal
- `gt` - Greater than
- `gte` - Greater than or equal
- `lt` - Less than
- `lte` - Less than or equal
- `in` - In array
- `like` - Pattern match

## Webhooks

Configure webhooks to receive real-time notifications:

```json
POST /webhooks
{
  "url": "https://your-server.com/webhook",
  "events": ["{{RESOURCE_PATH}}.created", "{{RESOURCE_PATH}}.updated"],
  "secret": "your-webhook-secret"
}
```

Webhook payload:

```json
{
  "event": "{{RESOURCE_PATH}}.created",
  "timestamp": "2024-01-15T10:30:00Z",
  "data": {
    "id": "{{RESOURCE_ID}}",
    ...
  }
}
```

## SDKs

- [JavaScript/TypeScript](https://github.com/{{ORG}}/sdk-js)
- [Python](https://github.com/{{ORG}}/sdk-python)
- [Go](https://github.com/{{ORG}}/sdk-go)

## Changelog

### v2.0.0 (2024-01-15)
- Added {{NEW_FEATURE}}
- Breaking: Changed {{BREAKING_CHANGE}}

### v1.0.0 (2024-01-01)
- Initial release
