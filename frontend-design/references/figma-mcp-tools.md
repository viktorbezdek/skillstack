# Figma MCP Server Tools Reference

This document provides comprehensive reference information about the Figma MCP (Model Context Protocol) server and its tools for extracting design data, including design tokens, from Figma files.

## Overview

The Figma MCP server enables Claude Code to interact with Figma files through structured tools. It provides access to design variables, layer metadata, code mappings, and visual exports.

**MCP Server Package:** `@figma/mcp-server-figma`
**Installation:** `npx @figma/mcp-server-figma`

## Server Modes

### Remote Server (Cloud-Based)

Connects to Figma's REST API using a personal access token.

**Pros:**
- Works without Figma desktop app
- Access files from anywhere
- More stable API

**Cons:**
- Requires personal access token setup
- Some features require Enterprise plan
- Rate limited by Figma API

**Configuration:**
```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["@figma/mcp-server-figma"],
      "env": {
        "FIGMA_PERSONAL_ACCESS_TOKEN": "your-token-here"
      }
    }
  }
}
```

### Desktop Server (Local)

Connects to local Figma desktop application.

**Pros:**
- No token required
- Access to local files
- Some exclusive features

**Cons:**
- Requires Figma desktop app running
- Only works with locally opened files
- May have version-specific quirks

**Configuration:**
```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["@figma/mcp-server-figma", "--desktop"]
    }
  }
}
```

## Available Tools

### 1. `get_variable_defs`

**Primary tool for extracting design tokens from Figma variables.**

**Purpose:** Retrieves variable definitions (colors, numbers, strings, booleans) from a Figma file.

**Parameters:**
- `file_url` (required): Figma file URL or file key
- `node_ids` (optional): Comma-separated node IDs to scope extraction

**Returns:**
```json
{
  "variables": [
    {
      "id": "variable_id",
      "name": "color.primary.500",
      "type": "COLOR",
      "resolvedType": "COLOR",
      "value": {
        "r": 0,
        "g": 0.4,
        "b": 0.8,
        "a": 1.0
      },
      "valuesByMode": {
        "mode_id_1": { "r": 0, "g": 0.4, "b": 0.8, "a": 1.0 },
        "mode_id_2": { "r": 1, "g": 1, "b": 1, "a": 1.0 }
      },
      "modes": {
        "mode_id_1": { "name": "Light" },
        "mode_id_2": { "name": "Dark" }
      },
      "description": "Primary brand color"
    }
  ]
}
```

**Variable Types:**
- `COLOR` - RGB color values (0-1 range)
- `FLOAT` - Numeric values (spacing, sizing, weights)
- `STRING` - Text values (font names, content)
- `BOOLEAN` - True/false flags

**Usage Notes:**
- Without `node_ids`, extracts all variables from file
- With `node_ids`, extracts only variables used by specified nodes
- Colors returned in 0-1 range, not 0-255
- Variable modes map to themes (light/dark, brand variants)
- References indicated by nested structures

**Limitations:**
- Figma Design files only (not FigJam)
- Variables API in REST requires Enterprise plan (desktop server bypasses this)
- Selection-based extraction may miss global variables

### 2. `get_design_context`

Extracts design context and generates code from Figma layers.

**Purpose:** Convert Figma frames to code (React, Vue, HTML, etc.)

**Parameters:**
- `file_url` (required): Figma file URL
- `node_ids` (optional): Specific nodes to convert
- `code_style` (optional): Output style (default: React + Tailwind)

**Returns:**
Styled code representation of the design.

**Usage for Design Tokens:**
- Useful for understanding design structure
- Can reveal applied variables in context
- Helps identify token usage patterns

**Common Code Styles:**
- React + Tailwind (default)
- React + CSS-in-JS
- HTML + CSS
- Vue
- SwiftUI

### 3. `get_metadata`

Retrieves sparse layer metadata (IDs, names, types, dimensions).

**Purpose:** Understand file structure without full data load

**Parameters:**
- `file_url` (required): Figma file URL
- `node_ids` (optional): Specific nodes

**Returns:**
```xml
<Node id="0:1" name="Page 1" type="PAGE">
  <Node id="1:2" name="Frame" type="FRAME" x="0" y="0" width="375" height="812">
    <Node id="2:3" name="Button" type="COMPONENT" x="20" y="20" width="335" height="48" />
  </Node>
</Node>
```

**Usage for Design Tokens:**
- Identify frames containing design system components
- Map layer structure before token extraction
- Find specific node IDs for targeted extraction

### 4. `get_screenshot`

Captures visual representation of Figma nodes.

**Purpose:** Generate preview images

**Parameters:**
- `file_url` (required): Figma file URL
- `node_ids` (required): Nodes to capture
- `scale` (optional): Image scale (1-4)
- `format` (optional): png, jpg, svg

**Returns:**
Image data (base64 or URL)

**Usage for Design Tokens:**
- Visual documentation of token usage
- Preview token applications in design
- Generate style guides

**Limitations:**
- SVG export limited to specific node types
- Large images may timeout
- Rate limited

### 5. `get_code_connect_map`

Maps Figma components to codebase components.

**Purpose:** Link design components to implementation

**Parameters:**
- `file_url` (required): Figma file URL

**Returns:**
```json
{
  "node_id": {
    "component": "Button",
    "path": "src/components/Button.tsx"
  }
}
```

**Usage for Design Tokens:**
- Identify which components use specific tokens
- Map token changes to code impact
- Generate token usage reports

### 6. `add_code_connect_map` (Desktop Only)

Creates Figma-to-code mappings.

**Purpose:** Establish component connections

**Parameters:**
- `file_url` (required): Figma file URL
- `node_id` (required): Figma component node ID
- `component_path` (required): Code file path

**Note:** Requires desktop server mode

### 7. `create_design_system_rules`

Generates translation rules for design-to-code conversion.

**Purpose:** Customize code generation

**Parameters:**
- `file_url` (required): Figma file URL
- `rules_description` (required): Natural language rules

**Returns:**
Rule file content

**Usage:**
Save output to `rules/` or `instructions/` directory for future code generation.

### 8. `get_figjam`

Converts FigJam diagrams to structured XML.

**Purpose:** Extract FigJam content

**Parameters:**
- `file_url` (required): FigJam file URL

**Returns:**
XML representation of FigJam canvas

**Note:** Not useful for design tokens (FigJam doesn't support variables)

### 9. `whoami` (Remote Server Only)

Returns authenticated user information.

**Purpose:** Verify authentication

**Parameters:** None

**Returns:**
```json
{
  "id": "user_id",
  "email": "user@example.com",
  "handle": "username"
}
```

**Usage:** Test API token validity

### 10. `get_strategy_for_mapping` & `send_get_strategy_response` (Alpha, Desktop Only)

Experimental tools for automated component detection and mapping.

**Status:** Alpha, subject to change

## Authentication

### Personal Access Token (Remote Server)

1. Navigate to Figma Settings > Account
2. Scroll to "Personal Access Tokens"
3. Click "Generate new token"
4. Name the token (e.g., "Claude Code MCP")
5. Copy token immediately (won't be shown again)
6. Add to config:
   ```json
   {
     "env": {
       "FIGMA_PERSONAL_ACCESS_TOKEN": "figd_..."
     }
   }
   ```

**Token Permissions:**
- File read access
- Variable read access (Enterprise only for REST API)

**Security:**
- Tokens grant full API access
- Never commit tokens to version control
- Rotate tokens periodically
- Revoke unused tokens

### Desktop App Authentication

No additional authentication required. Figma desktop app handles auth.

**Requirements:**
- Figma desktop app installed
- Logged into Figma account
- File open or accessible

## File Access Requirements

### File URLs

**Format:** `https://www.figma.com/design/FILE_KEY/FILE_NAME`

**File Key:** Alphanumeric string in URL (e.g., `aBc123XyZ`)

**Node IDs:** Format `123:456` (page:node)

### Permissions

**Remote Server:**
- View access minimum
- Edit access for some operations
- Team/org permissions respected

**Desktop Server:**
- Access matches desktop app permissions
- Can access local drafts

## API Limitations

### Rate Limiting

**Remote Server:**
- Figma API limits apply
- ~100 requests per minute per token
- 429 status on rate limit exceeded

**Desktop Server:**
- Less restrictive
- Limited by local app performance

### Enterprise Features

Some Figma features require Enterprise plan:
- REST API access to variables
- Advanced permissions
- Version history API

**Workaround:** Use desktop server to access variables without Enterprise plan

### File Size

- Large files may timeout
- Recommend scoped extraction with `node_ids`
- Use `get_metadata` first for structure overview

## Best Practices for Design Token Extraction

### 1. Scope Your Extraction

Don't extract entire file if you only need specific variables:

```bash
# Good: Specific nodes
file_url: "https://www.figma.com/design/abc123/File"
node_ids: "10:25,10:26,10:27"

# Avoid: Entire file when unnecessary
file_url: "https://www.figma.com/design/abc123/File"
# (no node_ids)
```

### 2. Use Metadata for Discovery

Get layer structure first:
1. Call `get_metadata` to see file structure
2. Identify frames with design system components
3. Note node IDs
4. Call `get_variable_defs` with specific node_ids

### 3. Handle Variable Modes

Figma supports multiple modes (light/dark, brand variants):
- Extract mode information from `valuesByMode`
- Map modes to separate token files or references
- Document mode purposes in token descriptions

### 4. Parse Color Format

Figma returns colors as RGB objects with 0-1 range:
```json
{ "r": 0.4, "g": 0.6, "b": 0.8, "a": 1.0 }
```

Convert to standard formats:
- Hex: `#66aacc`
- RGB: `rgb(102, 170, 204)`
- HSL: `hsl(205, 51%, 60%)`

### 5. Map Variable Types

| Figma Type | W3C DTCG Type | Typical Use |
|------------|---------------|-------------|
| COLOR | color | Colors |
| FLOAT | dimension | Spacing, sizing (with unit) |
| FLOAT | number | Line heights, opacity (unitless) |
| FLOAT | fontWeight | Font weights |
| STRING | fontFamily | Font names |
| STRING | string | Text content |
| BOOLEAN | boolean | Feature flags |

### 6. Resolve References

Figma variables can reference other variables:
```json
{
  "type": "VARIABLE_ALIAS",
  "id": "referenced_variable_id"
}
```

Build reference map and convert to W3C alias syntax: `{token.name}`

### 7. Handle Missing Data

Some variables may lack:
- Descriptions
- Mode names
- Scopes

Provide defaults or prompt user for supplemental info.

### 8. Validate Extraction

After extraction:
- Check all expected variables present
- Verify color conversions accurate
- Confirm references resolve
- Validate type mappings

## Troubleshooting

### Connection Errors

**"MCP server not found"**
- Verify config in `~/.claude/config.json`
- Restart Claude Code
- Check server package installed: `npx @figma/mcp-server-figma --version`

**"Authentication failed"**
- Regenerate personal access token
- Update token in config
- Verify token has file access

### File Access Errors

**"File not found"**
- Check file URL correct
- Verify file not deleted
- Confirm access permissions

**"Node not found"**
- Verify node ID format (`123:456`)
- Check node exists in file
- Try without node_ids to get all data

### Variable Extraction Issues

**"No variables returned"**
- Confirm file has variables (not just styles)
- Check Enterprise plan for REST API access
- Try desktop server as alternative
- Verify selected nodes use variables

**"Incomplete variable data"**
- Some metadata only available in desktop mode
- REST API may omit certain fields
- Check Figma version compatibility

### Performance Issues

**Timeouts**
- Reduce scope with specific node_ids
- Use `get_metadata` instead of full extraction
- Break large requests into smaller chunks

**Rate limits**
- Implement exponential backoff
- Cache results when possible
- Use desktop server to avoid API limits

## Further Resources

- **Figma MCP Server GitHub:** https://github.com/figma/mcp-server-figma
- **Figma REST API Docs:** https://www.figma.com/developers/api
- **Figma Variables Guide:** https://help.figma.com/hc/en-us/articles/15339657135383
- **MCP Protocol Spec:** https://modelcontextprotocol.io/
