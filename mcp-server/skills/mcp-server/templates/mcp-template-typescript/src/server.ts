/**
 * TypeScript MCP Server Template
 *
 * A complete MCP server template with example tools, resources, and prompts.
 * Demonstrates best practices for TypeScript MCP development.
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
  ListPromptsRequestSchema,
  GetPromptRequestSchema,
  Tool
} from "@modelcontextprotocol/sdk/types.js";
import { z } from "zod";

// =============================================================================
// INITIALIZATION
// =============================================================================

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
      resources: {},
      prompts: {}
    },
  }
);

// =============================================================================
// TOOLS - Executable operations
// =============================================================================

const CalculatorSchema = z.object({
  a: z.number().describe("First number"),
  b: z.number().describe("Second number"),
  operation: z.enum(["add", "subtract", "multiply", "divide"]).describe("Operation to perform")
});

const TextProcessingSchema = z.object({
  text: z.string().describe("Text to process"),
  operation: z.enum(["uppercase", "lowercase", "reverse", "word_count"]).describe("Operation to perform")
});

const tools: Tool[] = [
  {
    name: "calculator",
    description: "Perform basic arithmetic operations (add, subtract, multiply, divide)",
    inputSchema: {
      type: "object",
      properties: {
        a: { type: "number", description: "First number" },
        b: { type: "number", description: "Second number" },
        operation: {
          type: "string",
          enum: ["add", "subtract", "multiply", "divide"],
          description: "Operation to perform"
        }
      },
      required: ["a", "b", "operation"]
    }
  },
  {
    name: "process_text",
    description: "Process text with various operations (uppercase, lowercase, reverse, word_count)",
    inputSchema: {
      type: "object",
      properties: {
        text: { type: "string", description: "Text to process" },
        operation: {
          type: "string",
          enum: ["uppercase", "lowercase", "reverse", "word_count"],
          description: "Operation to perform"
        }
      },
      required: ["text", "operation"]
    }
  },
  {
    name: "get_environment_variable",
    description: "Get value of an environment variable",
    inputSchema: {
      type: "object",
      properties: {
        name: { type: "string", description: "Environment variable name" }
      },
      required: ["name"]
    }
  }
];

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case "calculator": {
        const params = CalculatorSchema.parse(args);
        let result: number;

        switch (params.operation) {
          case "add":
            result = params.a + params.b;
            break;
          case "subtract":
            result = params.a - params.b;
            break;
          case "multiply":
            result = params.a * params.b;
            break;
          case "divide":
            if (params.b === 0) {
              throw new Error("Cannot divide by zero");
            }
            result = params.a / params.b;
            break;
        }

        return {
          content: [{ type: "text", text: String(result) }]
        };
      }

      case "process_text": {
        const params = TextProcessingSchema.parse(args);
        let result: string;

        switch (params.operation) {
          case "uppercase":
            result = params.text.toUpperCase();
            break;
          case "lowercase":
            result = params.text.toLowerCase();
            break;
          case "reverse":
            result = params.text.split("").reverse().join("");
            break;
          case "word_count":
            result = String(params.text.split(/\s+/).length);
            break;
        }

        return {
          content: [{ type: "text", text: result }]
        };
      }

      case "get_environment_variable": {
        const { name: varName } = args as { name: string };
        const value = process.env[varName];

        if (value === undefined) {
          throw new Error(`Environment variable '${varName}' not found`);
        }

        return {
          content: [{ type: "text", text: value }]
        };
      }

      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  } catch (error) {
    if (error instanceof z.ZodError) {
      throw new Error(`Validation error: ${error.message}`);
    }
    throw error;
  }
});

// =============================================================================
// RESOURCES - Readable data sources
// =============================================================================

server.setRequestHandler(ListResourcesRequestSchema, async () => ({
  resources: [
    {
      uri: "config://server",
      name: "Server Configuration",
      description: "Server configuration information",
      mimeType: "text/plain"
    },
    {
      uri: "status://health",
      name: "Health Status",
      description: "Server health status",
      mimeType: "text/plain"
    },
    {
      uri: "file://example.txt",
      name: "Example File",
      description: "Example file content",
      mimeType: "text/plain"
    }
  ]
}));

server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const { uri } = request.params;

  switch (uri) {
    case "config://server":
      return {
        contents: [
          {
            uri,
            mimeType: "text/plain",
            text: `Server Configuration:
--------------------
Name: example-server
Version: 1.0.0
Environment: production
Features: tools, resources, prompts`
          }
        ]
      };

    case "status://health":
      return {
        contents: [
          {
            uri,
            mimeType: "text/plain",
            text: `Health Status:
-------------
Status: healthy
Uptime: operational
Memory: normal
CPU: normal`
          }
        ]
      };

    case "file://example.txt":
      return {
        contents: [
          {
            uri,
            mimeType: "text/plain",
            text: `Example File Content
===================

This is an example of a file resource.
In a production server, you would:
1. Validate the file path
2. Check permissions
3. Read from actual filesystem
4. Handle errors appropriately`
          }
        ]
      };

    default:
      throw new Error(`Unknown resource: ${uri}`);
  }
});

// =============================================================================
// PROMPTS - Prompt templates
// =============================================================================

server.setRequestHandler(ListPromptsRequestSchema, async () => ({
  prompts: [
    {
      name: "code_review_prompt",
      description: "Generate a prompt for code review",
      arguments: [
        {
          name: "code",
          description: "Code to review",
          required: true
        },
        {
          name: "language",
          description: "Programming language",
          required: false
        }
      ]
    },
    {
      name: "summarization_prompt",
      description: "Generate a prompt for text summarization",
      arguments: [
        {
          name: "text",
          description: "Text to summarize",
          required: true
        },
        {
          name: "max_sentences",
          description: "Maximum sentences in summary",
          required: false
        }
      ]
    }
  ]
}));

server.setRequestHandler(GetPromptRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  switch (name) {
    case "code_review_prompt": {
      const code = (args?.code as string) || "";
      const language = (args?.language as string) || "python";

      return {
        messages: [
          {
            role: "user",
            content: {
              type: "text",
              text: `Review this ${language} code:

\`\`\`${language}
${code}
\`\`\`

Please provide feedback on:
1. Code quality and best practices
2. Potential bugs or edge cases
3. Performance considerations
4. Security concerns
5. Suggestions for improvement

Be specific and constructive in your feedback.`
            }
          }
        ]
      };
    }

    case "summarization_prompt": {
      const text = (args?.text as string) || "";
      const maxSentences = (args?.max_sentences as number) || 3;

      return {
        messages: [
          {
            role: "user",
            content: {
              type: "text",
              text: `Summarize the following text in ${maxSentences} sentences or less:

${text}

Provide a concise, accurate summary highlighting the key points.`
            }
          }
        ]
      };
    }

    default:
      throw new Error(`Unknown prompt: ${name}`);
  }
});

// =============================================================================
// MAIN - Server entry point
// =============================================================================

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);

  console.error("MCP server running on stdio");
}

main().catch((error) => {
  console.error("Server error:", error);
  process.exit(1);
});
