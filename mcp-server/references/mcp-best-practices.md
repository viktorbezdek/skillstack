# MCP Best Practices

Universal MCP server development guidelines covering naming conventions, tool design, response formats, pagination, security, and compliance requirements.

## Server Naming Conventions

RULE: The model must follow standardized naming patterns for MCP servers

PATTERN_BY_LANGUAGE:

- Python: `{service}_mcp` (lowercase with underscores)
- Node/TypeScript: `{service}-mcp-server` (lowercase with hyphens)

EXAMPLES:

- Python: `slack_mcp`, `github_mcp`, `jira_mcp`, `stripe_mcp`
- Node/TypeScript: `slack-mcp-server`, `github-mcp-server`, `jira-mcp-server`

CONSTRAINTS:

- The model must use general names (not tied to specific features)
- The model must avoid version numbers or dates in server names
- The model must choose names descriptive of the service/API being integrated
- The model must use names easy to infer from task descriptions

## Tool Naming and Design

### Tool Naming Standards

RULE: The model must use snake_case for tool names

PATTERN: `{service}_{action}_{resource}`

EXAMPLES:

- `slack_send_message` (not just `send_message`)
- `github_create_issue` (not just `create_issue`)
- `asana_list_tasks` (not just `list_tasks`)

RATIONALE: Include service prefix to anticipate multi-server environments where name conflicts occur

### Tool Design Guidelines

RULE: The model must create focused, atomic tool operations

CONSTRAINTS:

- The model must provide tool descriptions that narrowly and unambiguously describe functionality
- The model must ensure descriptions precisely match actual functionality
- The model must avoid generic names that could conflict with other servers
- The model must provide tool annotations (readOnlyHint, destructiveHint, idempotentHint, openWorldHint)
- The model must maintain consistency in naming patterns within the server

### Tool Description Best Practices

SOURCE: User preference (2025-11-20) + [MCP Tool Design: From APIs to AI-First](https://useai.substack.com/p/mcp-tool-design-from-apis-to-ai-first) (accessed 2025-11-20)

PRINCIPLE: Put truth in the schema. Use descriptions for human hints the schema cannot express.

**Description Structure:**

```python
@mcp.tool()
def stripe_create_refund(
    charge_id: Annotated[str, Field(description="Stripe charge ID", pattern="^ch_")],
    amount: Annotated[int | None, Field(description="Amount in cents, omit for full refund")] = None,
    reason: Annotated[str | None, Field(description="Refund reason", enum=["duplicate", "fraudulent", "requested_by_customer"])] = None
) -> dict:
    """Create refund for charge.

    Returns: {"id": str, "status": str, "amount": int, "currency": str}.
    Status may be null during processing.

    Side effects: Deducts from account balance, requires auth scope payments:write,
    idempotent via Idempotency-Key header (auto-generated).

    Errors: InsufficientFunds when balance too low, InvalidCharge when charge not
    found or already refunded. Agent should check balance before retry.

    Example: Full refund → amount=None. Partial → amount=500 (for $5.00).
    """
```

**Required Components:**

1. **One-liner first**: Action + object (e.g., "Create refund for charge"). No fluff.

2. **Output contract**: Describe JSON shape and stable keys. Note nullables.
   - Format: `Returns: {key: type, ...}`
   - Call out any nullable fields

3. **Side effects + scope**: What changes in system, required auth/tenant, idempotency support.
   - State mutations clearly
   - List required permissions
   - Note if idempotency keys supported

4. **Failure modes**: Common errors with short "when/why" notes for retry/fallback.
   - Error name + when it occurs
   - Actionable guidance for agent

5. **Tiny example**: One happy path OR one edge case. Keep minimal.
   - Include only if agents routinely pick wrong tool
   - Keep under 2 lines

**Schema vs Description Separation:**

SCHEMA CONTAINS:

- Input parameter names, types, required/optional flags
- Enums with all valid values
- Constraints (max sizes, patterns, ranges)
- Expected output shape with stable keys

DESCRIPTION CONTAINS:

- Side effects and system mutations
- Auth scope/tenant requirements
- Rate limits and latency expectations
- Idempotency requirements
- Common failure reasons with retry guidance
- When/why to use this tool vs alternatives

**The 90/10 Rule:**

RULE: Use error handling to teach edge cases, not exhaustive upfront descriptions

RATIONALE: Strategic error messages guide models toward correct usage more effectively than bloated parameter documentation. Errors are prompt injections that teach in context.

ERROR_STRUCTURE:

1. What went wrong (specific)
2. Why it happened (brief context)
3. What to do instead (actionable)
4. Example of correct usage (when helpful)

**Response Guidance:**

RULE: Every response is a prompt injection opportunity

PATTERN: Include next-step hints in responses

- "Found 5 results. Use get_details() for full information"
- "Refund created. Status is 'pending'. Check refund_status() in 30s"

**Versioning and Deprecation:**

RULE: Versioning metadata belongs in annotations/docs with brief note in description if behavior changes soon

```python
@mcp.tool()
def legacy_search_products(...) -> dict:
    """Search products (DEPRECATED: use search_products_v2 after 2025-12-01).

    [rest of description]
    """
```

**Anti-Patterns:**

❌ **Verbose 5-part structure**: Bloats context without adding clarity ❌ **API-to-MCP direct conversion**: Design for AI intent, not endpoint mapping ❌ **Token-expensive parameter lists**: Put details in schema, not prose ❌ **Examples in every tool**: Add only when agents consistently pick wrong tool ❌ **Ambiguous terminology**: Avoid jargon requiring external knowledge

**Tool Consolidation:**

RULE: Group operations by user intent, not API endpoints

GUIDELINE:

- Consolidate naturally chained operations (find → get details → act)
- Keep destructive operations separate from read operations
- Avoid extremes: neither one-tool-per-endpoint nor one mega-tool

EXAMPLE: Circle.so consolidated 80 endpoints into ~12 intent-based tools where operations naturally chain together

SOURCE: [MCP Tool Design: From APIs to AI-First](https://useai.substack.com/p/mcp-tool-design-from-apis-to-ai-first) (accessed 2025-11-20)

### Tool Annotations

ANNOTATION_SCHEMA:

```text
readOnlyHint: boolean    # true if tool does not modify environment
destructiveHint: boolean # true if tool may perform destructive updates
idempotentHint: boolean  # true if repeated calls with same args have no additional effect
openWorldHint: boolean   # true if tool interacts with external entities
title: string            # human-readable title for UI display
```

CONSTRAINTS:

- The model must remember annotations are hints, not security guarantees
- The model must not rely on annotations for security-critical decisions
- The model must set annotations accurately to enable proper client-side safety checks

## Response Format Guidelines

RULE: The model must support multiple response formats for flexibility

FORMAT_TYPES:

### JSON Format (`response_format="json"`)

PURPOSE: Machine-readable structured data

CHARACTERISTICS:

- Include all available fields and metadata
- Use consistent field names and types
- Suitable for programmatic processing
- Use when LLMs need to process data further

### Markdown Format (`response_format="markdown"`)

PURPOSE: Human-readable formatted text (typically default)

CHARACTERISTICS:

- Use headers, lists, and formatting for clarity
- Convert timestamps to human-readable format (e.g., "2024-01-15 10:30:00 UTC" instead of epoch)
- Show display names with IDs in parentheses (e.g., "@john.doe (U123456)")
- Omit verbose metadata (e.g., show only one profile image URL, not all sizes)
- Group related information logically
- Use for presenting information to users

## Pagination Best Practices

RULE: The model must implement pagination for tools that list resources

CONSTRAINTS:

- The model must always respect the `limit` parameter
- The model must never load all results when a limit is specified
- The model must implement pagination using `offset` or cursor-based pagination
- The model must return pagination metadata: `has_more`, `next_offset`/`next_cursor`, `total_count`
- The model must never load all results into memory for large datasets
- The model must default to reasonable limits (20-50 items is typical)

PAGINATION_RESPONSE_SCHEMA:

```json
{
  "total": 150,
  "count": 20,
  "offset": 0,
  "items": [...],
  "has_more": true,
  "next_offset": 20
}
```

## Character Limits and Truncation

RULE: The model must prevent overwhelming responses with too much data

IMPLEMENTATION:

1. Define CHARACTER_LIMIT constant (typically 25,000 characters at module level)
2. Check response size before returning
3. Truncate gracefully with clear indicators
4. Provide guidance on filtering
5. Include truncation metadata

TRUNCATION_PATTERN:

```python
CHARACTER_LIMIT = 25000

if len(result) > CHARACTER_LIMIT:
    truncated_data = data[:max(1, len(data) // 2)]
    response["truncated"] = True
    response["truncation_message"] = (
        f"Response truncated from {len(data)} to {len(truncated_data)} items. "
        f"Use 'offset' parameter or add filters to see more results."
    )
```

## Transport Options

MCP servers support multiple transport mechanisms for different deployment scenarios.

### Stdio Transport

CHARACTERISTICS:

- Standard input/output stream communication
- Simple setup, no network configuration needed
- Runs as subprocess of the client
- Ideal for desktop applications and CLI tools
- Single-user, single-session scenarios

USE_WHEN:

- Building tools for local development environments
- Integrating with desktop applications (e.g., Claude Desktop)
- Creating command-line utilities
- Single-user, single-session scenarios

### HTTP Transport

CHARACTERISTICS:

- Request-response pattern over HTTP
- Supports multiple simultaneous clients
- Can be deployed as web service
- Requires network configuration and security considerations

USE_WHEN:

- Serving multiple clients simultaneously
- Deploying as cloud service
- Integration with web applications
- Need for load balancing or scaling

### SSE (Server-Sent Events) Transport

CHARACTERISTICS:

- One-way server-to-client streaming over HTTP
- Enables real-time updates without polling
- Long-lived connections for continuous data flow
- Built on standard HTTP infrastructure

USE_WHEN:

- Clients need real-time data updates
- Implementing push notifications
- Streaming logs or monitoring data
- Progressive result delivery for long operations

TRANSPORT_SELECTION_MATRIX:

| Criterion     | Stdio         | HTTP             | SSE         |
| ------------- | ------------- | ---------------- | ----------- |
| Deployment    | Local         | Remote           | Remote      |
| Clients       | Single        | Multiple         | Multiple    |
| Communication | Bidirectional | Request-Response | Server-Push |
| Complexity    | Low           | Medium           | Medium-High |
| Real-time     | No            | No               | Yes         |

## Security Best Practices

### Input Validation

RULE: The model must validate all parameters against schema

CONSTRAINTS:

- The model must sanitize file paths to prevent directory traversal
- The model must validate URLs and external identifiers
- The model must check parameter sizes and ranges
- The model must prevent command injection in system calls
- The model must use schema validation (Pydantic/Zod) for all inputs

### Access Control

RULE: The model must implement proper authentication and authorization

CONSTRAINTS:

- The model must implement authentication where needed
- The model must use appropriate authorization checks
- The model must audit tool usage
- The model must rate limit requests
- The model must monitor for abuse

### Error Handling

RULE: The model must handle errors securely

CONSTRAINTS:

- The model must not expose internal errors to clients
- The model must log security-relevant errors server-side
- The model must handle timeouts appropriately
- The model must clean up resources after errors
- The model must validate return values

### OAuth and Authentication

AUTHENTICATION_PATTERNS:

**OAuth 2.1 Implementation:**

- Use secure OAuth 2.1 with certificates from recognized authorities
- Validate access tokens before processing requests
- Only accept tokens specifically intended for your server
- Reject tokens without proper audience claims
- Never pass through tokens received from MCP clients

**API Key Management:**

- Store API keys in environment variables, never in code
- Validate keys on server startup
- Provide clear error messages when authentication fails
- Use secure transmission for sensitive credentials

### Privacy and Data Protection

DATA_COLLECTION_PRINCIPLES:

- Only collect data strictly necessary for functionality
- Don't collect extraneous conversation data
- Don't collect PII unless explicitly required for the tool's purpose
- Provide clear information about what data is accessed

DATA_TRANSMISSION:

- Don't send data to servers outside your organization without disclosure
- Use secure transmission (HTTPS) for all network communication
- Validate certificates for external services

## Resource Management

RULE: The model must manage resources efficiently

CONSTRAINTS:

- The model must only suggest necessary resources
- The model must use clear, descriptive names for roots
- The model must handle resource boundaries properly
- The model must respect client control over resources
- The model must use model-controlled primitives (tools) for automatic data exposure

## Prompt Management

RULE: The model must design prompts with user control in mind

CONSTRAINTS:

- Clients should show users proposed prompts
- Users should be able to modify or reject prompts
- Clients should show users completions
- Users should be able to modify or reject completions
- The model must consider costs when using sampling

## Error Handling Standards

RULE: The model must use standard error handling patterns

CONSTRAINTS:

- The model must use standard JSON-RPC error codes
- The model must report tool errors within result objects (not protocol-level)
- The model must provide helpful, specific error messages
- The model must not expose internal implementation details
- The model must clean up resources properly on errors

## Documentation Requirements

RULE: The model must provide comprehensive documentation

CONSTRAINTS:

- The model must provide clear documentation of all tools and capabilities
- The model must include working examples (at least 3 per major feature)
- The model must document security considerations
- The model must specify required permissions and access levels
- The model must document rate limits and performance characteristics

## Compliance and Monitoring

RULE: The model must implement proper logging and monitoring

CONSTRAINTS:

- The model must implement logging for debugging and monitoring
- The model must track tool usage patterns
- The model must monitor for potential abuse
- The model must maintain audit trails for security-relevant operations
- The model must be prepared for ongoing compliance reviews

## Testing Requirements

TESTING_STRATEGY:

**Functional Testing:**

- Verify correct execution with valid/invalid inputs

**Integration Testing:**

- Test interaction with external systems

**Security Testing:**

- Validate auth, input sanitization, rate limiting

**Performance Testing:**

- Check behavior under load, timeouts

**Error Handling:**

- Ensure proper error reporting and cleanup

## Summary

These best practices represent comprehensive guidelines for building secure, efficient, and compliant MCP servers that work well within the ecosystem. Developers should follow these guidelines to ensure their MCP servers meet standards for inclusion in the MCP directory and provide a safe, reliable experience for users.
