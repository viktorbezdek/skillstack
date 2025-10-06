# GitHub API Reference for PR Comments

## Overview

The `pr-comment-grabber.py` script uses GitHub's REST API v3 to extract comments from Pull Requests.

## Endpoints Used

### 1. Pull Request Review Comments

**Endpoint:** `GET /repos/{owner}/{repo}/pulls/{pull_number}/comments`

**Description:** Fetches inline code comments (review comments) attached to specific files and lines.

**Response:**
```json
[
  {
    "id": 123456789,
    "pull_request_review_id": 987654321,
    "user": {
      "login": "reviewer-username"
    },
    "body": "Consider refactoring this",
    "path": "src/main.py",
    "position": 15,
    "line": 42,
    "commit_id": "abc123...",
    "created_at": "2025-01-15T14:30:00Z",
    "updated_at": "2025-01-15T14:35:00Z",
    "html_url": "https://github.com/owner/repo/pull/1#discussion_r123456789",
    "diff_hunk": "@@ -40,6 +40,8 @@ ..."
  }
]
```

**Pagination:** Returns 100 results per page, uses Link header for next pages.

### 2. Pull Request Issue Comments

**Endpoint:** `GET /repos/{owner}/{repo}/issues/{issue_number}/comments`

**Description:** Fetches general PR conversation comments (not attached to specific code lines).

**Note:** PRs are issues in GitHub's API, so we use the same issue number as the PR number.

**Response:**
```json
[
  {
    "id": 987654321,
    "user": {
      "login": "qodo-merge"
    },
    "body": "## PR Analysis Summary\n\nOverall: Good",
    "created_at": "2025-01-15T12:00:00Z",
    "updated_at": "2025-01-15T12:00:00Z",
    "html_url": "https://github.com/owner/repo/pull/1#issuecomment-987654321"
  }
]
```

**Pagination:** Same as review comments (100 per page, Link header).

## Authentication

### Personal Access Token

Required scopes:
- **Private repositories:** `repo` (full repository access)
- **Public repositories:** `public_repo` (read/write access to public repos)

**Generate token:** https://github.com/settings/tokens

**Usage:**
```bash
export GITHUB_TOKEN=ghp_your_token_here
```

Or pass via HTTP header:
```python
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}
```

## Pagination

GitHub API returns max 100 results per page. Use Link header to fetch remaining pages.

**Link Header Format:**
```
Link: <https://api.github.com/repos/owner/repo/pulls/1/comments?page=2>; rel="next",
      <https://api.github.com/repos/owner/repo/pulls/1/comments?page=5>; rel="last"
```

**Parse logic:**
```python
def parse_link_header(link_header: str) -> Dict[str, str]:
    links = {}
    for link in link_header.split(','):
        url, rel = link.split(';')
        url = url.strip()[1:-1]  # Remove < >
        if 'rel="next"' in rel:
            links['next'] = url
    return links
```

**Fetch all pages:**
```python
all_comments = []
url = "https://api.github.com/repos/owner/repo/pulls/1/comments"

while url:
    response = requests.get(url, headers=headers, params={"per_page": 100})
    all_comments.extend(response.json())

    link_header = response.headers.get('Link', '')
    links = parse_link_header(link_header)
    url = links.get('next')  # None if no more pages
```

## Rate Limits

### Authenticated Requests
- **Limit:** 5,000 requests per hour
- **Typical usage:** 2-5 requests per PR (depending on comment count and pagination)

### Check Rate Limit
```bash
curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/rate_limit
```

**Response:**
```json
{
  "resources": {
    "core": {
      "limit": 5000,
      "remaining": 4998,
      "reset": 1642348800
    }
  }
}
```

## Error Codes

### 401 Unauthorized
**Cause:** Invalid or missing GitHub token
**Fix:** Verify token is set and has correct scopes

### 404 Not Found
**Cause:** Repository or PR doesn't exist, or no access
**Fix:** Check repo format (`owner/repo`), PR number, and token permissions

### 403 Forbidden
**Cause:** Rate limit exceeded or token lacks required scope
**Fix:** Wait until rate limit resets or add required scope to token

### 422 Unprocessable Entity
**Cause:** Invalid request parameters
**Fix:** Check repository name format and PR number

## Field Reference

### Review Comment Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Unique comment ID |
| `pull_request_review_id` | integer | Parent review ID |
| `user.login` | string | Commenter's username |
| `body` | string | Comment text (markdown) |
| `path` | string | File path relative to repo root |
| `position` | integer | Position in diff (may be null) |
| `line` | integer | Line number in file |
| `commit_id` | string | SHA of commit being reviewed |
| `created_at` | timestamp | ISO 8601 format |
| `updated_at` | timestamp | ISO 8601 format (if edited) |
| `html_url` | string | Direct link to comment on GitHub |
| `diff_hunk` | string | Surrounding diff context |
| `in_reply_to_id` | integer | Parent comment ID (if reply) |

### Issue Comment Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Unique comment ID |
| `user.login` | string | Commenter's username |
| `body` | string | Comment text (markdown) |
| `created_at` | timestamp | ISO 8601 format |
| `updated_at` | timestamp | ISO 8601 format (if edited) |
| `html_url` | string | Direct link to comment on GitHub |

## Best Practices

1. **Always paginate:** Don't assume all comments fit in one page
2. **Handle rate limits:** Implement exponential backoff for 403 errors
3. **Cache tokens:** Store GitHub token securely (not in code)
4. **Use User-Agent:** Set descriptive User-Agent header
5. **Handle 404s gracefully:** PR might be deleted or made private
6. **Respect updated_at:** Track comment edits via updated_at field
7. **Follow API versioning:** Use `Accept: application/vnd.github.v3+json`

## Example: Fetch All Comments

```python
import requests

def fetch_all_pr_comments(owner, repo, pr_number, token):
    """Fetch all comments (review + issue) for a PR."""

    # Fetch review comments (inline)
    review_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/comments"
    review_comments = fetch_paginated(review_url, token)

    # Fetch issue comments (general conversation)
    issue_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"
    issue_comments = fetch_paginated(issue_url, token)

    # Combine and return
    return {
        "review": review_comments,
        "issue": issue_comments,
        "total": len(review_comments) + len(issue_comments)
    }

def fetch_paginated(url, token):
    """Fetch all pages from an endpoint."""
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "PR-Comment-Grabber/2.0"
    }

    all_items = []
    page = 1

    while url:
        response = requests.get(url, headers=headers, params={"per_page": 100})
        response.raise_for_status()

        all_items.extend(response.json())

        # Check for next page
        link_header = response.headers.get('Link', '')
        url = parse_next_link(link_header)
        page += 1

    return all_items
```

## Resources

- **GitHub REST API Docs:** https://docs.github.com/en/rest
- **Pull Request Comments:** https://docs.github.com/en/rest/pulls/comments
- **Issue Comments:** https://docs.github.com/en/rest/issues/comments
- **Authentication:** https://docs.github.com/en/rest/overview/authenticating-to-the-rest-api
- **Rate Limiting:** https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api

## Version

- **API Version:** GitHub REST API v3
- **Last Updated:** 2025-10-24
