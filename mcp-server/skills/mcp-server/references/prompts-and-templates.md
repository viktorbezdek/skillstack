# FastMCP Prompts and Templates

Guide to using FastMCP's prompt template system and configuring AI-native tool integration.

## Overview

In the MCP ecosystem, **prompts** refer to:

1. **Prompt templates** served by the MCP server (@mcp.prompt)
2. **System prompts/instructions** that AI clients use to guide tool usage

FastMCP supports defining reusable prompt templates via the `@mcp.prompt` decorator, allowing servers to provide pre-defined prompts/messages that the client's AI can request and insert into its context for consistent behavior.

## Defining Prompt Templates

### Basic Prompt Template

Similar to tools, decorate a function with `@mcp.prompt` to register a prompt template:

```python
@mcp.prompt()
def ask_about_topic(topic: str) -> str:
    """Asks for an explanation of a topic."""
    return f"Can you please explain the concept of '{topic}'?"
```

FastMCP exposes this prompt (named `ask_about_topic` by default) so that an AI client can request it by name with a parameter (the `topic`).

### How It Works

1. Client requests prompt by name: `ask_about_topic`
2. Client provides parameter: `topic="machine learning"`
3. Server returns formatted prompt text
4. Client inserts prompt into LLM's conversation

This mechanism ensures prompts are inserted into the LLM's conversation in a standardized way.

### Richer Prompt Types

Return `PromptMessage` objects for explicit control over role and content type:

```python
from fastmcp import PromptMessage, TextContent

@mcp.prompt()
def code_review_prompt(code: str) -> PromptMessage:
    """Generate a prompt for code review."""
    return PromptMessage(
        role="user",
        content=TextContent(text=f"Please review this code:\n\n{code}")
    )
```

Usually a plain string suffices (treated as a user message by default).

### Customizing Prompt Metadata

Override prompt name, description, and add tags:

```python
@mcp.prompt(
    name="explain_concept",
    description="Generate an explanation request for any concept",
    tags=["education", "learning"]
)
def ask_about_topic(topic: str) -> str:
    return f"Can you please explain the concept of '{topic}'?"
```

## Use Cases for @mcp.prompt

### Centralized Prompt Engineering

Store prompt templates on the server rather than in client applications:

**Benefits:**

- Latest version always used
- Consistent prompts across all clients
- Large prompt strings kept off client side
- Version control for prompts

### AI IDE Integration

AI IDE plugins (Claude Desktop, Cursor) can use prompt templates as one-click actions.

**Example from Anthropic's Claude Desktop:**

A prompt named `poetry` takes an argument `topic` and produces:

```text
"Write a creative poem about the following topic: {topic}"
```

Users can trigger this prompt through Claude Desktop's UI rather than typing the whole prompt each time.

### Common Prompt Templates

**Examples of useful templates:**

```python
@mcp.prompt()
def generate_unit_test(code: str) -> str:
    """Generate unit test for given code."""
    return f"""Please generate comprehensive unit tests for this code:

{code}

Include:
- Happy path cases
- Edge cases
- Error conditions
"""

@mcp.prompt()
def summarize_with_bullets(text: str) -> str:
    """Summarize text with bullet points."""
    return f"Summarize the following text using concise bullet points:\n\n{text}"

@mcp.prompt()
def explain_to_beginner(concept: str) -> str:
    """Explain concept in simple terms."""
    return f"Explain {concept} in simple terms that a beginner can understand."
```

## System Instructions for Tool Use

Beyond templates served by the MCP server, there's the matter of **how to prompt the AI model** to effectively use MCP tools.

### MCP Primer Prompt

The community provides a ready-made "MCP primer" system prompt that explains the Model Context Protocol to LLMs.

**Official MCP description prompt:**

Available at: `https://modelcontextprotocol.io/llms-full.txt`

This describes:

- The MCP protocol
- Tool syntax
- How to call tools properly
- Examples of tool usage

### Using the MCP Primer

RESOURCE: <https://modelcontextprotocol.io/llms-full.txt> PURPOSE: Official MCP protocol description for LLMs CONTENT: Complete MCP specification optimized for AI consumption

USAGE_PATTERN:

```python
# Server provides MCP primer as prompt template
@mcp.prompt()
def mcp_introduction() -> str:
    """Provide MCP protocol overview to AI client."""
    return """
    Model Context Protocol (MCP) enables AI assistants to:
    - Call tools via JSON-RPC 2.0
    - Access resources (read-only data)
    - Use prompt templates

    Tool call format:
    {
      "method": "tools/call",
      "params": {
        "name": "tool_name",
        "arguments": {"param": "value"}
      }
    }

    For full specification: https://modelcontextprotocol.io/llms-full.txt
    """
```

TRIGGER: The model should load MCP primer when:

- Building new MCP client integration
- Debugging tool call format issues
- Explaining MCP to other AI models
- Testing protocol compliance

OUTCOME: AI models with MCP primer context:

- Correctly format tool calls
- Understand resource vs tool distinction
- Handle streaming responses properly
- Parse MCP error messages accurately

### AI-Native Development Tooling

Cursor, Cline, Windsurf, Roo, and other AI coding assistants craft specialized system prompts:

**Typical structure:**

```text
Available tools:
- tool_name_1: description
- tool_name_2: description
...

If needed, use these tools by responding with JSON commands as per MCP spec.
```

### Tool Descriptions as Prompts

FastMCP automatically provides machine-readable tool schemas via `list_tools` in MCP. The model benefits from a nudge in the system prompt.

**Your tool descriptions act as part of the prompt the AI sees:**

```python
@mcp.tool()
def search_products(
    query: str,
    category: str | None = None
) -> dict:
    """Search the product catalog with optional category filtering.

    This tool searches our product database and returns matching items.
    Use when the user asks to find products or browse by category.
    """
    # ...
```

The description helps the LLM know **when to use the tool** and **what it does**.

### Writing Effective Tool Descriptions

SOURCE: User preference (2025-11-20) + [MCP Tool Design: From APIs to AI-First](https://useai.substack.com/p/mcp-tool-design-from-apis-to-ai-first) (accessed 2025-11-20)

**Core Principle: Put truth in the schema. Use descriptions for hints the schema cannot express.**

**Tight Description Structure:**

1. **One-liner**: Action + object (e.g., "Calculate shipping cost for package"). No fluff.
2. **Output contract**: JSON shape with stable keys. Note nullables.
3. **Side effects + scope**: System mutations, required auth/tenant, idempotency.
4. **Failure modes**: Common errors with when/why notes for agent retry/fallback.
5. **Tiny example** (optional): Only if agents routinely pick wrong tool. Keep under 2 lines.

**Example:**

```python
@mcp.tool()
def calculate_shipping(
    weight_kg: Annotated[float, Field(ge=0.1, le=1000, description="Package weight in kg")],
    destination_country: Annotated[str, Field(description="ISO 3166-1 alpha-2 code", pattern="^[A-Z]{2}$")],
    service_level: Annotated[str, Field(description="Shipping speed", enum=["standard", "express", "overnight"])] = "standard"
) -> dict:
    """Calculate shipping cost for package.

    Returns: {"cost_usd": float, "delivery_days": int, "methods": [str]}.
    cost_usd is always present; delivery_days may be null for remote regions.

    Side effects: None (read-only calculation). No auth required for rate lookup.

    Errors: UnsupportedCountry when destination not serviced (check supported_countries first).
    WeightExceeded when package over carrier limit (try freight_quote instead).

    Example: Express to Canada → service_level="express", destination_country="CA".
    """
    # ...
```

**What Goes Where:**

SCHEMA (Pydantic Field / Zod):

- Parameter types, required/optional flags
- Enums with all valid values
- Constraints (ranges, patterns, max sizes)
- Basic parameter descriptions

DESCRIPTION (docstring):

- Side effects and state mutations
- Auth scope/tenant requirements
- Rate limits, latency expectations
- Idempotency support
- Common failure modes with actionable retry guidance
- When to use this tool vs alternatives

**The 90/10 Rule:**

Use strategic error messages to teach edge cases in context, not exhaustive upfront descriptions:

```python
raise ToolError(
    "UnsupportedCountry: Cannot ship to 'XX'. "
    "Supported regions: North America, EU, Australia. "
    "Use freight_quote() for other destinations."
)
```

**Anti-Patterns:**

❌ **Verbose multi-paragraph descriptions**: Bloats context without adding clarity ❌ **Repeating schema information in prose**: Types/constraints belong in schema only ❌ **Examples for every tool**: Add only when agents consistently choose incorrectly ❌ **Detailed parameter explanations**: Field descriptions handle this

## Configuration for AI-Native Tools

Many AI coding assistants allow configuring MCP servers via JSON or manifest files.

### Common Configuration Elements

**Typical structure:**

```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["server.py"],
      "env": {
        "API_KEY": "...",
        "ALLOWED_DIRECTORIES": "/home/user/projects"
      }
    }
  }
}
```

### Claude Desktop Extension Manifest (.mcpb)

Claude Desktop's extension manifest format includes `user_config` section:

```json
{
  "name": "my-mcp-server",
  "version": "1.0.0",
  "user_config": {
    "api_key": {
      "type": "string",
      "description": "API key for service",
      "required": true
    },
    "allowed_directories": {
      "type": "array",
      "description": "Allowed file paths",
      "default": []
    }
  }
}
```

Claude Desktop:

1. Prompts user for configuration values
2. Injects them as environment variables when launching server

### Server Configuration Hooks

Provide easy configuration in your FastMCP server:

```python
import os

# Read from environment variables
API_KEY = os.getenv("API_KEY")
ALLOWED_DIRS = os.getenv("ALLOWED_DIRECTORIES", "").split(",")

@mcp.tool()
def read_file(
    path: str,
    api_key: Annotated[str, Field(exclude=True)] = API_KEY
) -> dict:
    # Validate path against ALLOWED_DIRS
    if not any(path.startswith(d) for d in ALLOWED_DIRS):
        raise ToolError(f"Access denied: {path} not in allowed directories")

    # Use api_key for external service
    # ...
```

### Cursor's mcp.json

Cursor allows enabling MCP servers and restricting permissions:

```json
{
  "servers": {
    "my-server": {
      "command": "python server.py",
      "allowedPaths": ["/home/user/projects"]
    }
  }
}
```

Your server should respect these limits by checking paths before file operations.

## Best Practices

### Prompt Template Design

1. **Keep prompts focused** - One clear purpose per template
2. **Use parameters** - Make templates reusable with variables
3. **Include examples** - Show expected format in prompt text
4. **Version control** - Track prompt changes like code

### Tool Description Writing

1. **Be specific** - Clear, unambiguous descriptions
2. **Include constraints** - Mention limitations and requirements
3. **Provide examples** - Show typical usage patterns
4. **Guide decision-making** - Help AI choose the right tool

### Configuration Management

1. **Use environment variables** - For secrets and user-specific config
2. **Validate inputs** - Check configuration at startup
3. **Provide defaults** - Sensible fallbacks for optional config
4. **Document requirements** - Clear README for configuration

## Summary

Prompts and templates in FastMCP serve two roles:

1. **Server-side templates** - `@mcp.prompt` for consistent query formatting
2. **Client-side instructions** - System prompts that guide AI tool usage

**Key takeaways:**

- Use `@mcp.prompt` to package complex or frequently-used prompts
- Write detailed tool descriptions (they're part of the AI's prompt)
- Support configuration via environment variables
- Follow community prompt guidelines for better AI integration
- Test prompts with real AI assistants to validate effectiveness

By centralizing prompts in your MCP server and providing clear tool descriptions, you enable AI assistants to use your tools effectively and consistently.
