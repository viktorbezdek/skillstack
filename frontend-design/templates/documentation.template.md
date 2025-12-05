# Design Tokens Documentation

Auto-generated from Figma design variables.

## Colors

| Token Name | Value | Description |
|------------|-------|-------------|
| `primary` | `#0066cc` | Primary brand color |
| `secondary` | `#6c757d` | Secondary color for less prominent elements |
| `success` | `#28a745` | Success state color |
| `error` | `#dc3545` | Error state color |
| `warning` | `#ffc107` | Warning state color |
| `info` | `#17a2b8` | Informational color |

## Spacing

| Token Name | Value | Description |
|------------|-------|-------------|
| `xs` | `4px` | Extra small spacing |
| `sm` | `8px` | Small spacing |
| `md` | `16px` | Medium spacing |
| `lg` | `24px` | Large spacing |
| `xl` | `32px` | Extra large spacing |

## Typography

### Font Families

| Token Name | Value | Description |
|------------|-------|-------------|
| `body` | `Inter, system-ui, sans-serif` | Font family for body text |
| `heading` | `Helvetica Neue, Helvetica, Arial, sans-serif` | Font family for headings |
| `monospace` | `Monaco, Consolas, monospace` | Font family for code |

### Font Sizes

| Token Name | Value |
|------------|-------|
| `xs` | `12px` |
| `sm` | `14px` |
| `md` | `16px` |
| `lg` | `18px` |
| `xl` | `20px` |
| `2xl` | `24px` |
| `3xl` | `30px` |
| `4xl` | `36px` |

### Font Weights

| Token Name | Value |
|------------|-------|
| `normal` | `400` |
| `medium` | `500` |
| `semibold` | `600` |
| `bold` | `700` |

### Line Heights

| Token Name | Value |
|------------|-------|
| `tight` | `1.25` |
| `normal` | `1.5` |
| `relaxed` | `1.75` |

## Shadows

| Token Name | Value |
|------------|-------|
| `sm` | `0 1px 2px 0 rgba(0, 0, 0, 0.05)` |
| `md` | `0 4px 6px -1px rgba(0, 0, 0, 0.1)` |
| `lg` | `0 10px 15px -3px rgba(0, 0, 0, 0.1)` |

## Border Radius

| Token Name | Value |
|------------|-------|
| `sm` | `4px` |
| `md` | `8px` |
| `lg` | `12px` |
| `full` | `9999px` |

## Animation

### Durations

| Token Name | Value |
|------------|-------|
| `fast` | `150ms` |
| `normal` | `300ms` |
| `slow` | `500ms` |

### Easings

| Token Name | Value |
|------------|-------|
| `ease-in` | `cubic-bezier(0.42, 0, 1, 1)` |
| `ease-out` | `cubic-bezier(0, 0, 0.58, 1)` |
| `ease-in-out` | `cubic-bezier(0.42, 0, 0.58, 1)` |

## Usage Examples

### CSS

```css
.button {
  background-color: var(--color-primary);
  padding: var(--spacing-md);
  font-family: var(--font-family-body);
  font-size: var(--font-size-md);
  font-weight: var(--font-weight-medium);
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-sm);
  transition: all var(--duration-normal) var(--easing-ease-in-out);
}

.button:hover {
  box-shadow: var(--shadow-md);
}
```

### SCSS

```scss
.button {
  background-color: $color-primary;
  padding: $spacing-md;
  font-family: $font-family-body;
  font-size: $font-size-md;
  font-weight: $font-weight-medium;
  border-radius: $border-radius-md;
  box-shadow: $shadow-sm;
  transition: all $duration-normal $easing-ease-in-out;

  &:hover {
    box-shadow: $shadow-md;
  }
}
```

### TypeScript/React

```typescript
import { tokens } from './tokens';

const buttonStyles: React.CSSProperties = {
  backgroundColor: tokens.color.primary,
  padding: tokens.spacing.md,
  fontFamily: tokens.typography.fontFamily.body,
  fontSize: tokens.typography.fontSize.md,
  fontWeight: tokens.typography.fontWeight.medium,
  borderRadius: tokens.borderRadius.md,
  boxShadow: tokens.shadow.sm,
  transition: `all ${tokens.animation.duration.normal} ${tokens.animation.easing.easeInOut}`,
};

function Button({ children }) {
  return <button style={buttonStyles}>{children}</button>;
}
```

### JSON (Style Dictionary)

```javascript
const StyleDictionary = require('style-dictionary');

const sd = StyleDictionary.extend({
  source: ['tokens.json'],
  platforms: {
    css: {
      transformGroup: 'css',
      buildPath: 'dist/css/',
      files: [{
        destination: 'variables.css',
        format: 'css/variables'
      }]
    },
    js: {
      transformGroup: 'js',
      buildPath: 'dist/js/',
      files: [{
        destination: 'tokens.js',
        format: 'javascript/es6'
      }]
    }
  }
});

sd.buildAllPlatforms();
```

## Integration

### PostCSS

```css
/* Import tokens */
@import './tokens.css';

/* Use in your styles */
.component {
  color: var(--color-primary);
  padding: var(--spacing-md);
}
```

### Webpack

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader', 'postcss-loader']
      }
    ]
  }
};
```

### Vite

```javascript
// vite.config.js
import { defineConfig } from 'vite';

export default defineConfig({
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@import "./tokens.scss";`
      }
    }
  }
});
```

## Maintenance

### Updating Tokens

1. Update design variables in Figma
2. Re-run extraction script
3. Review changes in git diff
4. Test in components
5. Commit and deploy

### Versioning

Token changes should be versioned:

- **Patch**: Fix incorrect values
- **Minor**: Add new tokens
- **Major**: Remove or rename tokens (breaking)

### Deprecation

When deprecating tokens:

1. Mark with `$deprecated` in W3C format
2. Update documentation
3. Provide migration path
4. Remove in next major version

---

**Last Updated:** [Timestamp]
**Version:** 1.0.0
**Source:** Figma Design System
