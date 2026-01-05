"""
FastMCP Server Template

A complete MCP server template with example tools, resources, and prompts.
Demonstrates best practices for FastMCP development.
"""

from fastmcp import FastMCP
from pydantic import BaseModel, Field
import os
from typing import Optional

# Initialize server
mcp = FastMCP(
    name="example-server",
    version="1.0.0"
)


# =============================================================================
# TOOLS - Executable operations
# =============================================================================

class CalculatorInput(BaseModel):
    """Input schema for calculator."""
    a: float = Field(..., description="First number")
    b: float = Field(..., description="Second number")
    operation: str = Field(
        ...,
        description="Operation to perform",
        pattern="^(add|subtract|multiply|divide)$"
    )


@mcp.tool()
def calculator(params: CalculatorInput) -> float:
    """
    Perform basic arithmetic operations.

    Example:
        calculator({"a": 10, "b": 5, "operation": "add"}) -> 15.0
    """
    if params.operation == "add":
        return params.a + params.b
    elif params.operation == "subtract":
        return params.a - params.b
    elif params.operation == "multiply":
        return params.a * params.b
    elif params.operation == "divide":
        if params.b == 0:
            raise ValueError("Cannot divide by zero")
        return params.a / params.b
    else:
        raise ValueError(f"Unknown operation: {params.operation}")


@mcp.tool()
def get_environment_variable(name: str) -> str:
    """
    Get value of an environment variable.

    Args:
        name: Environment variable name

    Returns:
        Value of the environment variable

    Raises:
        ValueError: If variable not found
    """
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"Environment variable '{name}' not found")
    return value


class TextProcessingInput(BaseModel):
    """Input schema for text processing."""
    text: str = Field(..., description="Text to process")
    operation: str = Field(
        ...,
        description="Operation: uppercase, lowercase, reverse, word_count",
        pattern="^(uppercase|lowercase|reverse|word_count)$"
    )


@mcp.tool()
def process_text(params: TextProcessingInput) -> str:
    """
    Process text with various operations.

    Supports: uppercase, lowercase, reverse, word_count
    """
    text = params.text

    if params.operation == "uppercase":
        return text.upper()
    elif params.operation == "lowercase":
        return text.lower()
    elif params.operation == "reverse":
        return text[::-1]
    elif params.operation == "word_count":
        return str(len(text.split()))
    else:
        raise ValueError(f"Unknown operation: {params.operation}")


# =============================================================================
# RESOURCES - Readable data sources
# =============================================================================

@mcp.resource("config://server")
def server_config() -> str:
    """
    Return server configuration information.

    This demonstrates a static resource.
    """
    return """
Server Configuration:
--------------------
Name: example-server
Version: 1.0.0
Environment: production
Features: tools, resources, prompts
"""


@mcp.resource("status://health")
def health_status() -> str:
    """
    Return server health status.

    This demonstrates a dynamic resource that could check actual health.
    """
    return """
Health Status:
-------------
Status: healthy
Uptime: operational
Memory: normal
CPU: normal
"""


@mcp.resource("file://example.txt")
def example_file() -> str:
    """
    Return content of an example file.

    In a real server, this might read from actual files
    with proper path validation.
    """
    return """
Example File Content
===================

This is an example of a file resource.
In a production server, you would:
1. Validate the file path
2. Check permissions
3. Read from actual filesystem
4. Handle errors appropriately
"""


# =============================================================================
# PROMPTS - Prompt templates
# =============================================================================

@mcp.prompt()
def code_review_prompt(code: str, language: str = "python") -> str:
    """
    Generate a prompt for code review.

    Args:
        code: Code to review
        language: Programming language

    Returns:
        Formatted prompt for code review
    """
    return f"""Review this {language} code:

```{language}
{code}
```

Please provide feedback on:
1. Code quality and best practices
2. Potential bugs or edge cases
3. Performance considerations
4. Security concerns
5. Suggestions for improvement

Be specific and constructive in your feedback."""


class SummarizationParams(BaseModel):
    """Parameters for summarization prompt."""
    text: str = Field(..., description="Text to summarize")
    max_sentences: int = Field(
        3,
        description="Maximum sentences in summary",
        ge=1,
        le=10
    )
    focus: Optional[str] = Field(
        None,
        description="Specific aspect to focus on"
    )


@mcp.prompt()
def summarization_prompt(params: SummarizationParams) -> str:
    """
    Generate a prompt for text summarization.

    Args:
        params: Summarization parameters

    Returns:
        Formatted summarization prompt
    """
    focus_section = f"\nFocus specifically on: {params.focus}" if params.focus else ""

    return f"""Summarize the following text in {params.max_sentences} sentences or less:

{params.text}
{focus_section}

Provide a concise, accurate summary highlighting the key points."""


# =============================================================================
# MAIN - Server entry point
# =============================================================================

if __name__ == "__main__":
    # Run the server
    mcp.run()
