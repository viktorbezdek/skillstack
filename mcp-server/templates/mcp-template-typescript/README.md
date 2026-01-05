# TypeScript MCP Server Template

A complete TypeScript MCP server template demonstrating tools, resources, and prompts with type safety.

## Features

- **Tools**: Executable operations (calculator, text processing, env vars)
- **Resources**: Readable data sources (config, health status, files)
- **Prompts**: Prompt templates (code review, summarization)
- **Type Safety**: Zod schemas for runtime validation
- **TypeScript**: Full type safety and IDE support

## Quick Start

### 1. Install Dependencies

```bash
npm install
```

### 2. Build

```bash
npm run build
```

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 4. Run the Server

```bash
npm start
```

### 5. Test with Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-server": {
      "command": "node",
      "args": ["/path/to/dist/server.js"]
    }
  }
}
```

## Development

### Watch Mode

```bash
npm run dev
```

### Linting

```bash
npm run lint
```

### Formatting

```bash
npm run format
```

### Testing

```bash
npm test
```

## Available Tools

### calculator
Perform basic arithmetic operations.

**Example:**
```json
{
  "a": 10,
  "b": 5,
  "operation": "add"
}
```

### process_text
Process text with various operations.

**Example:**
```json
{
  "text": "Hello World",
  "operation": "uppercase"
}
```

### get_environment_variable
Get environment variable value.

**Example:**
```json
{
  "name": "NODE_ENV"
}
```

## Available Resources

- `config://server` - Server configuration
- `status://health` - Health status
- `file://example.txt` - Example file content

## Available Prompts

- `code_review_prompt` - Generate code review prompt
- `summarization_prompt` - Generate summarization prompt

## Project Structure

```
mcp-template-typescript/
├── src/
│   └── server.ts          # Main server implementation
├── tests/                 # Test files
├── dist/                  # Compiled JavaScript (generated)
├── package.json          # Dependencies and scripts
├── tsconfig.json         # TypeScript configuration
├── .env.example          # Environment template
└── README.md             # This file
```

## Customization

### Adding a New Tool

```typescript
import { z } from "zod";

const MyToolSchema = z.object({
  param: z.string().describe("Parameter description")
});

const tools: Tool[] = [
  // ... existing tools
  {
    name: "my_tool",
    description: "Tool description",
    inputSchema: {
      type: "object",
      properties: {
        param: { type: "string", description: "Parameter description" }
      },
      required: ["param"]
    }
  }
];

// In CallToolRequestSchema handler:
case "my_tool": {
  const params = MyToolSchema.parse(args);
  return {
    content: [{ type: "text", text: `Processed: ${params.param}` }]
  };
}
```

### Adding a New Resource

```typescript
// In ListResourcesRequestSchema handler:
{
  uri: "my-resource://example",
  name: "My Resource",
  description: "Resource description",
  mimeType: "text/plain"
}

// In ReadResourceRequestSchema handler:
case "my-resource://example":
  return {
    contents: [{
      uri,
      mimeType: "text/plain",
      text: "Resource content"
    }]
  };
```

### Adding a New Prompt

```typescript
// In ListPromptsRequestSchema handler:
{
  name: "my_prompt",
  description: "Prompt description",
  arguments: [
    {
      name: "text",
      description: "Text parameter",
      required: true
    }
  ]
}

// In GetPromptRequestSchema handler:
case "my_prompt": {
  const text = (args?.text as string) || "";
  return {
    messages: [{
      role: "user",
      content: {
        type: "text",
        text: `Process this: ${text}`
      }
    }]
  };
}
```

## Security Considerations

- **Input validation**: All inputs validated with Zod
- **Type safety**: TypeScript ensures type correctness
- **Error handling**: Clear error messages
- **Environment variables**: Sensitive config in .env
- **Path safety**: Validate file paths before operations

## Production Checklist

- [ ] Update server name and version
- [ ] Configure environment variables
- [ ] Add authentication (if needed)
- [ ] Implement logging (Winston, Pino)
- [ ] Add error tracking (Sentry)
- [ ] Set up monitoring
- [ ] Write comprehensive tests (Vitest)
- [ ] Document all tools/resources/prompts
- [ ] Review security considerations
- [ ] Build and test production bundle

## Resources

- MCP TypeScript SDK: https://github.com/modelcontextprotocol/typescript-sdk
- MCP Specification: https://spec.modelcontextprotocol.io
- Zod Documentation: https://zod.dev

## License

MIT License - customize as needed
