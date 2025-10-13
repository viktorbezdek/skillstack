# Advanced Usage

This guide covers advanced features and customization options for the figma-design-tokens skill.

## Custom Token Types

For Figma variables that don't map to standard W3C DTCG types, you can define custom mappings.

### Defining Custom Types

```bash
python figma-design-tokens/scripts/extract_tokens.py \
  --figma-data input.json \
  --output-path output.json \
  --custom-type "CUSTOM_TYPE:my-custom-type" \
  --custom-type "SPECIAL_VAR:special-dimension"
```

### Example: Animation Tokens

```bash
# Extract animation timing variables as custom type
python extract_tokens.py \
  --figma-data animations.json \
  --output-path tokens.json \
  --custom-type "ANIMATION_TIMING:duration"
```

Generated output:
```json
{
  "animation": {
    "fast": {
      "$type": "duration",
      "$value": "200ms"
    },
    "slow": {
      "$type": "duration",
      "$value": "500ms"
    }
  }
}
```

## Token Filtering

### Extract Specific Categories

```bash
# Only extract colors and spacing
python extract_tokens.py \
  --figma-data input.json \
  --output-path tokens.json \
  --token-types colors,spacing
```

### Exclude Deprecated Tokens

```bash
# Exclude tokens matching pattern
python extract_tokens.py \
  --figma-data input.json \
  --output-path tokens.json \
  --exclude-tokens deprecated-*,old-*,legacy-*
```

### Filter by Collection

If your Figma file uses variable collections:

```bash
# Extract only from specific collection
python extract_tokens.py \
  --figma-data input.json \
  --output-path tokens.json \
  --collection "Brand Colors"
```

## Batch Processing

### Process Multiple Figma Files

```bash
#!/bin/bash
# batch-extract.sh

FILES=(
  "brand-colors.json"
  "component-tokens.json"
  "semantic-tokens.json"
)

for file in "${FILES[@]}"; do
  basename=$(basename "$file" .json)
  python scripts/extract_tokens.py \
    --figma-data "input/$file" \
    --output-path "output/${basename}.tokens.json" \
    --pretty
done

echo "Extracted ${#FILES[@]} token files"
```

### Merge Multiple Token Files

```bash
# merge-tokens.sh
python -c "
import json
from pathlib import Path

merged = {}
for file in Path('tokens').glob('*.json'):
    with open(file) as f:
        data = json.load(f)
        merged.update(data)

with open('tokens-merged.json', 'w') as f:
    json.dump(merged, f, indent=2)
"
```

## Advanced Naming Strategies

### Custom Prefixes per Category

```bash
python transform_tokens.py \
  --input tokens.json \
  --format css \
  --category-prefix "color:clr,spacing:sp,typography:type,shadow:shd" \
  --output-dir dist
```

Output:
```css
:root {
  --clr-primary: #0066cc;
  --sp-medium: 16px;
  --type-body: 'Inter', sans-serif;
  --shd-card: 0 2px 4px rgba(0,0,0,0.1);
}
```

### Nested Naming Structure

```bash
# Generate deeply nested token names
python transform_tokens.py \
  --input tokens.json \
  --format css \
  --naming-convention kebab-case \
  --preserve-hierarchy \
  --output-dir dist
```

Output:
```css
:root {
  --color-brand-primary-500: #0066cc;
  --color-brand-primary-600: #0052a3;
  --spacing-component-button-padding-x: 16px;
  --spacing-component-button-padding-y: 8px;
}
```

## Multi-Theme Workflows

### Separate Files Per Mode

```bash
# Extract all modes separately
for mode in light dark high-contrast; do
  python extract_tokens.py \
    --figma-data variables.json \
    --mode "$mode" \
    --output-path "tokens-${mode}.json"
done

# Transform each theme
for mode in light dark high-contrast; do
  python transform_tokens.py \
    --input "tokens-${mode}.json" \
    --format css \
    --output-dir "dist/${mode}"
done
```

### Token References Approach

Create base tokens with semantic overrides:

```json
{
  "base": {
    "blue-500": { "$value": "#0066cc" },
    "gray-900": { "$value": "#1a1a1a" },
    "white": { "$value": "#ffffff" }
  },
  "semantic": {
    "light": {
      "background": { "$value": "{base.white}" },
      "text": { "$value": "{base.gray-900}" }
    },
    "dark": {
      "background": { "$value": "{base.gray-900}" },
      "text": { "$value": "{base.white}" }
    }
  }
}
```

### CSS Theme Switching

```css
/* Base tokens (primitives) */
:root {
  --base-blue-500: #0066cc;
  --base-gray-900: #1a1a1a;
  --base-white: #ffffff;
}

/* Light theme (default) */
:root {
  --color-background: var(--base-white);
  --color-text: var(--base-gray-900);
}

/* Dark theme */
[data-theme="dark"] {
  --color-background: var(--base-gray-900);
  --color-text: var(--base-white);
}
```

## Custom Output Formats

### Create Custom Template

```typescript
// templates/custom-format.template.ts
/**
 * Design Tokens - Custom Format
 * Generated: {{DATE}}
 */

export const designTokens = {
  {{#each categories}}
  {{category}}: {
    {{#each tokens}}
    {{name}}: '{{value}}',
    {{/each}}
  },
  {{/each}}
} as const;

export type DesignTokens = typeof designTokens;
```

### Use Template in Script

Modify `transform_tokens.py` to support custom templates:

```python
def to_custom_format(self, template_path: Path) -> Dict[str, str]:
    """Generate output using custom template"""
    with open(template_path) as f:
        template = f.read()

    # Process template with token data
    output = self._render_template(template, self.tokens)
    return {'tokens.custom.ts': output}
```

## Token Versioning

### Semantic Versioning

```json
{
  "$schema": "https://tr.designtokens.org/format/",
  "$version": "1.0.0",
  "color": {
    "primary": {
      "$value": "#0066cc",
      "$description": "Primary brand color",
      "$extensions": {
        "com.example.version": "1.0.0",
        "com.example.deprecated": false
      }
    }
  }
}
```

### Track Changes

```bash
# Generate tokens with timestamp
python transform_tokens.py \
  --input tokens.json \
  --format json \
  --include-metadata \
  --output-dir "dist/$(date +%Y%m%d)"
```

## Performance Optimization

### Selective Loading

Only load needed token categories:

```typescript
// Instead of importing everything
import { tokens } from './tokens';

// Import only what you need
import type { ColorTokens } from './tokens';
const colors: ColorTokens = require('./tokens').tokens.color;
```

### Split Output Files

```bash
# Generate separate files per category
python transform_tokens.py \
  --input tokens.json \
  --format css,scss,typescript \
  --organize-by-category \
  --output-dir dist
```

Output structure:
```
dist/
├── colors.css
├── colors.scss
├── colors.ts
├── spacing.css
├── spacing.scss
├── spacing.ts
└── typography.css
```

### Minified Output

```bash
# Generate minified CSS (no comments, no whitespace)
python transform_tokens.py \
  --input tokens.json \
  --format css \
  --minify \
  --output-dir dist
```

## Validation Customization

### Strict Mode

```bash
# Treat warnings as errors
python validate_tokens.py \
  --input tokens.json \
  --strict \
  --report validation.md
```

### Custom Validation Rules

Create custom validation script:

```python
# custom-validate.py
from validate_tokens import TokenValidator

class CustomValidator(TokenValidator):
    def _validate_token(self, token, path, parent_type):
        super()._validate_token(token, path, parent_type)

        # Custom rule: all colors must have descriptions
        if parent_type == 'color' and '$description' not in token:
            self.errors.append(f"{path}: Color token missing description")

        # Custom rule: spacing must be multiples of 4
        if parent_type == 'dimension' and 'spacing' in path:
            value = int(token['$value'].replace('px', ''))
            if value % 4 != 0:
                self.warnings.append(f"{path}: Spacing not multiple of 4")
```

## Automation Scripts

### Watch for Changes

```bash
#!/bin/bash
# watch-tokens.sh

while true; do
  # Check if Figma file has updates
  NEW_HASH=$(curl -s "$FIGMA_API_URL" | sha256sum)

  if [ "$NEW_HASH" != "$OLD_HASH" ]; then
    echo "Changes detected, updating tokens..."
    python extract_tokens.py --figma-data latest.json --output-path tokens.json
    python transform_tokens.py --input tokens.json --format all --output-dir dist
    OLD_HASH=$NEW_HASH
  fi

  sleep 300 # Check every 5 minutes
done
```

### Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Validate tokens before commit
python scripts/validate_tokens.py \
  --input tokens.json \
  --strict

if [ $? -ne 0 ]; then
  echo "Token validation failed. Commit aborted."
  exit 1
fi

echo "Token validation passed."
exit 0
```

## Export Strategies

### Component-Specific Tokens

Extract tokens per component:

```bash
# Extract button tokens
python extract_tokens.py \
  --figma-data components.json \
  --filter "component:button" \
  --output-path tokens-button.json

# Extract card tokens
python extract_tokens.py \
  --figma-data components.json \
  --filter "component:card" \
  --output-path tokens-card.json
```

### Platform-Specific Output

```bash
# Generate for web
python transform_tokens.py \
  --input tokens.json \
  --format css,scss \
  --platform web \
  --output-dir dist/web

# Generate for iOS
python transform_tokens.py \
  --input tokens.json \
  --format json \
  --platform ios \
  --color-format uicolor \
  --output-dir dist/ios

# Generate for Android
python transform_tokens.py \
  --input tokens.json \
  --format xml \
  --platform android \
  --output-dir dist/android
```

## Documentation Generation

### Auto-Generate Storybook Stories

```bash
# Generate token documentation for Storybook
python scripts/generate_storybook.py \
  --input tokens.json \
  --output stories/tokens.stories.mdx
```

### Visual Token Reference

```bash
# Generate HTML documentation with swatches
python scripts/generate_docs.py \
  --input tokens.json \
  --format html \
  --include-swatches \
  --output docs/tokens.html
```

## Migration Helpers

### Convert from Other Formats

```bash
# Convert from Theo format
python scripts/migrate_theo.py \
  --input theo-tokens.yml \
  --output w3c-tokens.json

# Convert from Style Dictionary
python scripts/migrate_sd.py \
  --input sd-tokens.json \
  --output w3c-tokens.json
```

### Version Migration

```bash
# Migrate from v1 to v2 format
python scripts/migrate_v1_to_v2.py \
  --input tokens-v1.json \
  --output tokens-v2.json \
  --backup
```

## Testing Strategies

### Token Contract Testing

```typescript
// tokens.contract.test.ts
import { tokens } from './tokens';

describe('Token Contract', () => {
  test('all color tokens are valid hex or rgb', () => {
    Object.values(tokens.color).forEach(color => {
      expect(color).toMatch(/^(#[0-9a-f]{6}|rgb\(.+\))$/i);
    });
  });

  test('spacing follows 4px grid', () => {
    Object.values(tokens.spacing).forEach(space => {
      const value = parseInt(space);
      expect(value % 4).toBe(0);
    });
  });
});
```

### Visual Regression Tests

```javascript
// Use Percy, Chromatic, or similar
import { tokens } from './tokens';

describe('Visual Tokens', () => {
  test('color swatches', () => {
    cy.visit('/token-viewer');
    Object.entries(tokens.color).forEach(([name, value]) => {
      cy.get(`[data-token="${name}"]`).should('have.css', 'background-color', value);
    });
    cy.percySnapshot('Token Colors');
  });
});
```

## Best Practices

1. **Version Control**: Always commit generated files to track changes
2. **Validation**: Run validation before every commit
3. **Documentation**: Keep token descriptions up to date
4. **Organization**: Use consistent naming across Figma and output
5. **Testing**: Write tests for token contracts and values
6. **Automation**: Set up CI/CD for automatic token updates
7. **Monitoring**: Track token usage across codebase
8. **Communication**: Notify team when tokens change

## Performance Benchmarks

Typical processing times:

- Small project (50 tokens): <1 second
- Medium project (200 tokens): 1-2 seconds
- Large project (500+ tokens): 2-5 seconds
- Enterprise (1000+ tokens): 5-10 seconds

Optimization tips:

- Use `--organize-by-category` for faster loading
- Split tokens into multiple files
- Cache transformed outputs
- Use tree-shaking for TypeScript tokens
