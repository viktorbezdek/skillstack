# Troubleshooting Guide

This guide covers common errors and their solutions when using the figma-design-tokens skill.

## MCP Connection Errors

### Error: "MCP server 'figma' not found"

**Solution:**
1. Verify Figma MCP server is configured in `~/.claude/config.json`
2. Restart Claude Code
3. Test connection with a simple MCP tool call

### Error: "Authentication failed"

**Solution:**
1. Check personal access token is valid
2. Regenerate token in Figma settings if expired
3. Update token in config file
4. Restart Claude Code

## Figma File Access Errors

### Error: "File not found" or "Access denied"

**Solution:**
1. Verify file URL is correct
2. Check user has view/edit access to file
3. Ensure file is not in a restricted team
4. Try opening file in Figma to confirm access

## Variable Extraction Errors

### Error: "No variables found in selection"

**Solution:**
1. Verify selected elements actually use design variables
2. Check that file has variables defined (not just styles)
3. Try selecting parent frames or entire pages
4. Use `get_metadata` to inspect layer structure

**Automatic Fallback:** If no variables are found, the extraction script automatically attempts to extract tokens from node styles:
- Uses `get_design_context` or node data from the Figma file
- Extracts colors from fills/strokes
- Extracts typography from text nodes
- Extracts spacing from padding and auto-layout
- Automatically prevents duplicate token values

### Error: "Variable type not supported"

**Solution:**
1. Check `references/figma-mcp-tools.md` for supported types
2. Some Figma features may not map to W3C tokens
3. Consider manual transformation for edge cases

## Transformation Errors

### Error: "Invalid color format"

**Solution:**
1. Check Figma color variables are in valid format
2. Verify color space conversion in script
3. Review error log for specific color values
4. May need to manually adjust problematic colors

### Error: "Circular reference detected"

**Solution:**
1. Run validation script to identify circular references
2. Check Figma variables for loops (A references B references A)
3. Break circular references in Figma or transform scripts

## Validation Errors

### Error: "Token missing required $value property"

**Solution:**
1. Check extraction script generated proper W3C structure
2. Verify all tokens have `$value` field
3. Review transformation logic for edge cases

### Error: "Invalid token type"

**Solution:**
1. Ensure token `$type` is W3C DTCG compliant
2. Check `references/w3c-dtcg-spec.md` for valid types
3. May need custom `$type` for Figma-specific variables

## Installation Issues

### Error: "npx: command not found"

**Solution:**
- Install Node.js from nodejs.org
- Restart your terminal/Claude Code after installation

### Error: "Cannot find module '@figma/mcp-server-figma'"

**Solution:**
- Run `npx @figma/mcp-server-figma` manually first
- Check your internet connection
- Try clearing npm cache: `npm cache clean --force`

### Error: Invalid JSON in config file

**Solution:**
1. Verify `~/.claude/config.json` has valid JSON syntax
2. Use a JSON validator to check for errors
3. Common issues:
   - Missing commas between properties
   - Extra trailing commas
   - Unescaped quotes in strings
   - Missing closing braces

## Script Execution Errors

### Error: Python not found

**Solution:**
- Ensure Python 3.7+ is installed
- Verify Python is in your PATH
- Try using `python3` instead of `python`

### Error: Permission denied

**Solution:**
- Check script has execute permissions: `chmod +x script.py`
- Verify output directory has write permissions
- Try running with `python` explicitly: `python script.py`

### Error: Module import errors

**Solution:**
1. Check Python version (3.7+ required)
2. Verify all required modules are available (json, re, sys, pathlib, argparse)
3. These are all standard library modules and should be available by default

## Output Issues

### Generated files are empty

**Solution:**
1. Check input JSON file contains valid token data
2. Verify token types match extraction parameters
3. Review script output for warnings
4. Ensure `--token-types` parameter matches available tokens

### CSS variables not working in browser

**Solution:**
1. Verify CSS file is imported/linked correctly
2. Check browser DevTools for CSS syntax errors
3. Ensure `:root` selector is not overridden
4. Test with simple variable reference to isolate issue

### TypeScript types not recognized

**Solution:**
1. Ensure `.ts` file is in TypeScript project
2. Check TypeScript configuration includes the file
3. Verify import path is correct
4. Try rebuilding TypeScript project

## Best Practices for Avoiding Issues

1. **Always validate tokens** after extraction using `validate_tokens.py`
2. **Test with small selections first** before extracting entire design systems
3. **Use meaningful variable names** in Figma for better token organization
4. **Keep Figma variables organized** using collections and modes
5. **Version control generated files** to track changes
6. **Document custom transformations** if modifying scripts
7. **Regular MCP server updates** to get latest features and fixes

## Getting Additional Help

If you encounter issues not covered here:

1. **Check the main SKILL.md** for workflow guidance
2. **Review Figma MCP documentation** at `references/figma-mcp-tools.md`
3. **Consult W3C DTCG spec** at `references/w3c-dtcg-spec.md`
4. **Check Figma MCP server docs** at https://github.com/figma/mcp-server-figma
5. **Review script help** with `python script.py --help`
