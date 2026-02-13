# FastMCP Server Template

A complete FastMCP server template demonstrating tools, resources, and prompts.

## Features

- **Tools**: Executable operations (calculator, text processing, env vars)
- **Resources**: Readable data sources (config, health status, files)
- **Prompts**: Prompt templates (code review, summarization)
- **Validation**: Pydantic schemas for type safety
- **Testing**: Example tests with pytest

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 3. Run the Server

```bash
python server.py
```

### 4. Test with Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-server": {
      "command": "python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

## Available Tools

### calculator
Perform basic arithmetic operations (add, subtract, multiply, divide).

**Example:**
```json
{
  "a": 10,
  "b": 5,
  "operation": "add"
}
```

### get_environment_variable
Get value of an environment variable.

**Example:**
```json
{
  "name": "HOME"
}
```

### process_text
Process text with various operations (uppercase, lowercase, reverse, word_count).

**Example:**
```json
{
  "text": "Hello World",
  "operation": "uppercase"
}
```

## Available Resources

- `config://server` - Server configuration
- `status://health` - Health status
- `file://example.txt` - Example file content

## Available Prompts

- `code_review_prompt` - Generate code review prompt
- `summarization_prompt` - Generate summarization prompt

## Testing

Run tests with pytest:

```bash
pip install pytest pytest-asyncio
pytest tests/
```

## Customization

### Adding a New Tool

```python
from pydantic import BaseModel, Field

class MyToolInput(BaseModel):
    param: str = Field(..., description="Parameter description")

@mcp.tool()
def my_tool(params: MyToolInput) -> str:
    """Tool description."""
    return f"Processed: {params.param}"
```

### Adding a New Resource

```python
@mcp.resource("my-resource://example")
def my_resource() -> str:
    """Resource description."""
    return "Resource content"
```

### Adding a New Prompt

```python
@mcp.prompt()
def my_prompt(text: str) -> str:
    """Prompt description."""
    return f"Process this: {text}"
```

## Security Considerations

- **Input validation**: All inputs use Pydantic schemas
- **Error handling**: Tools return clear error messages
- **Environment variables**: Sensitive config in .env file
- **Path safety**: Validate file paths before reading
- **Rate limiting**: Consider adding rate limits for production

## Production Checklist

- [ ] Update server name and version
- [ ] Configure environment variables
- [ ] Add authentication (if needed)
- [ ] Implement logging
- [ ] Add error tracking
- [ ] Set up monitoring
- [ ] Write comprehensive tests
- [ ] Document all tools/resources/prompts
- [ ] Review security considerations
- [ ] Plan deployment strategy

## Resources

- FastMCP Documentation: https://github.com/jlowin/fastmcp
- MCP Specification: https://spec.modelcontextprotocol.io
- Pydantic Documentation: https://docs.pydantic.dev

## License

MIT License - customize as needed
