# Integration Examples

This guide shows how to integrate generated design tokens with popular build tools and frameworks.

## Style Dictionary

Style Dictionary is the most popular design token transformation platform.

### Basic Configuration

```javascript
// build-tokens.js
const StyleDictionary = require('style-dictionary');

const sd = StyleDictionary.extend({
  source: ['tokens/**/*.tokens.json'],
  platforms: {
    css: {
      transformGroup: 'css',
      buildPath: 'dist/css/',
      files: [{
        destination: 'variables.css',
        format: 'css/variables'
      }]
    },
    scss: {
      transformGroup: 'scss',
      buildPath: 'dist/scss/',
      files: [{
        destination: '_variables.scss',
        format: 'scss/variables'
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

### Multi-Theme Configuration

```javascript
const StyleDictionary = require('style-dictionary');

// Build light theme
StyleDictionary.extend({
  source: ['tokens/base.json', 'tokens/light.json'],
  platforms: {
    css: {
      buildPath: 'dist/css/',
      files: [{
        destination: 'light-theme.css',
        format: 'css/variables'
      }]
    }
  }
}).buildAllPlatforms();

// Build dark theme
StyleDictionary.extend({
  source: ['tokens/base.json', 'tokens/dark.json'],
  platforms: {
    css: {
      buildPath: 'dist/css/',
      files: [{
        destination: 'dark-theme.css',
        format: 'css/variables'
      }]
    }
  }
}).buildAllPlatforms();
```

### Custom Transforms

```javascript
const StyleDictionary = require('style-dictionary');

// Register custom transform
StyleDictionary.registerTransform({
  name: 'size/rem',
  type: 'value',
  matcher: (token) => token.type === 'dimension',
  transformer: (token) => {
    const val = parseFloat(token.value);
    return `${val / 16}rem`;
  }
});

const sd = StyleDictionary.extend({
  source: ['tokens/**/*.json'],
  platforms: {
    css: {
      transforms: ['attribute/cti', 'name/cti/kebab', 'size/rem', 'color/css'],
      buildPath: 'dist/',
      files: [{
        destination: 'tokens.css',
        format: 'css/variables'
      }]
    }
  }
});

sd.buildAllPlatforms();
```

## PostCSS

Use generated CSS custom properties with PostCSS.

### Basic Import

```css
/* styles.css */
@import './tokens.css';

.button {
  background-color: var(--color-primary);
  padding: var(--spacing-medium);
  font-family: var(--font-family-body);
}
```

### With postcss-custom-properties

```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('postcss-import'),
    require('postcss-custom-properties')({
      preserve: false,
      importFrom: 'tokens.css'
    }),
    require('autoprefixer')
  ]
};
```

### With CSS Modules

```css
/* Button.module.css */
@value tokens: './tokens.css';
@value colorPrimary, spacingMedium from tokens;

.button {
  background-color: colorPrimary;
  padding: spacingMedium;
}
```

## Sass/SCSS

### Basic Import

```scss
// Import tokens
@import './tokens';

.button {
  background-color: $color-primary;
  padding: $spacing-medium;
  font-family: $font-family-body;

  &:hover {
    background-color: $color-primary-dark;
  }
}
```

### With Sass Maps

```scss
// Convert tokens to Sass map
$colors: (
  'primary': $color-primary,
  'secondary': $color-secondary,
  'accent': $color-accent,
);

// Helper function
@function color($name) {
  @return map-get($colors, $name);
}

// Usage
.button {
  background-color: color('primary');
}
```

### Theme Switching

```scss
// Import both themes
@import './tokens-light';
@import './tokens-dark';

:root {
  @include light-theme;
}

[data-theme="dark"] {
  @include dark-theme;
}
```

## React

### Using CSS Variables

```typescript
// Button.tsx
import './tokens.css';

const Button: React.FC = () => (
  <button
    style={{
      backgroundColor: 'var(--color-primary)',
      padding: 'var(--spacing-medium)',
    }}
  >
    Click Me
  </button>
);
```

### Using TypeScript Tokens

```typescript
// Import type-safe tokens
import { tokens } from './tokens';

const Button: React.FC = () => (
  <button
    style={{
      backgroundColor: tokens.color.primary,
      padding: tokens.spacing.medium,
      fontFamily: tokens.typography.fontFamily,
    }}
  >
    Click Me
  </button>
);
```

### With Styled Components

```typescript
import styled from 'styled-components';
import { tokens } from './tokens';

const StyledButton = styled.button`
  background-color: ${tokens.color.primary};
  padding: ${tokens.spacing.medium};
  font-family: ${tokens.typography.fontFamily};

  &:hover {
    background-color: ${tokens.color.primaryDark};
  }
`;

export const Button: React.FC = () => <StyledButton>Click Me</StyledButton>;
```

### With Emotion

```typescript
import { css } from '@emotion/react';
import { tokens } from './tokens';

const buttonStyles = css({
  backgroundColor: tokens.color.primary,
  padding: tokens.spacing.medium,
  fontFamily: tokens.typography.fontFamily,

  '&:hover': {
    backgroundColor: tokens.color.primaryDark,
  },
});

export const Button: React.FC = () => (
  <button css={buttonStyles}>Click Me</button>
);
```

## Vue

### Using CSS Variables

```vue
<template>
  <button class="btn">{{ label }}</button>
</template>

<style scoped>
@import './tokens.css';

.btn {
  background-color: var(--color-primary);
  padding: var(--spacing-medium);
}
</style>
```

### Using TypeScript Tokens

```vue
<script setup lang="ts">
import { tokens } from './tokens';

const buttonStyle = {
  backgroundColor: tokens.color.primary,
  padding: tokens.spacing.medium,
};
</script>

<template>
  <button :style="buttonStyle">{{ label }}</button>
</template>
```

## Tailwind CSS

### Extend Tailwind Config

```javascript
// tailwind.config.js
const tokens = require('./tokens.json');

module.exports = {
  theme: {
    extend: {
      colors: {
        primary: tokens.color.primary.$value,
        secondary: tokens.color.secondary.$value,
      },
      spacing: {
        xs: tokens.spacing.xs.$value,
        sm: tokens.spacing.sm.$value,
        md: tokens.spacing.md.$value,
        lg: tokens.spacing.lg.$value,
      },
      fontFamily: {
        body: tokens.typography.fontFamily.$value,
      },
    },
  },
};
```

### Usage in Components

```jsx
<button className="bg-primary text-white px-md py-sm font-body">
  Click Me
</button>
```

## Next.js

### Global Styles

```typescript
// pages/_app.tsx
import '../styles/tokens.css';
import '../styles/globals.css';

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;
```

### CSS Modules

```typescript
// Button.module.css
@import '../tokens.css';

.button {
  background-color: var(--color-primary);
  padding: var(--spacing-medium);
}
```

```typescript
// components/Button.tsx
import styles from './Button.module.css';

export const Button = () => (
  <button className={styles.button}>Click Me</button>
);
```

## Vite

### Import in main.ts

```typescript
// main.ts
import './tokens.css';
import './style.css';
```

### Dynamic Imports

```typescript
// Load theme dynamically
const theme = localStorage.getItem('theme') || 'light';
await import(`./tokens-${theme}.css`);
```

## Webpack

### Configuration

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader', 'postcss-loader'],
      },
    ],
  },
};
```

### Import in Entry

```javascript
// index.js
import './tokens.css';
```

## CI/CD Integration

### GitHub Actions

```yaml
# .github/workflows/tokens.yml
name: Update Design Tokens

on:
  workflow_dispatch:
  schedule:
    - cron: '0 0 * * 1' # Weekly on Monday

jobs:
  update-tokens:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Extract Tokens
        env:
          FIGMA_TOKEN: ${{ secrets.FIGMA_TOKEN }}
        run: |
          # Use Figma API or MCP to fetch latest
          # Run extraction scripts
          python scripts/extract_tokens.py \
            --figma-data figma-export.json \
            --output-path tokens.json

      - name: Transform Tokens
        run: |
          python scripts/transform_tokens.py \
            --input tokens.json \
            --format css,scss,json,typescript \
            --output-dir ./dist

      - name: Validate Tokens
        run: |
          python scripts/validate_tokens.py \
            --input tokens.json \
            --report validation.md

      - name: Commit Changes
        run: |
          git config user.name "Token Bot"
          git config user.email "bot@example.com"
          git add dist/ tokens.json
          git commit -m "Update design tokens" || exit 0
          git push
```

### GitLab CI

```yaml
# .gitlab-ci.yml
update-tokens:
  image: python:3.11
  script:
    - pip install -r requirements.txt
    - python scripts/extract_tokens.py --figma-data data.json --output-path tokens.json
    - python scripts/transform_tokens.py --input tokens.json --format css,scss --output-dir dist
  artifacts:
    paths:
      - dist/
      - tokens.json
  only:
    - schedules
```

## Testing

### Jest with TypeScript Tokens

```typescript
// tokens.test.ts
import { tokens } from './tokens';

describe('Design Tokens', () => {
  test('color tokens are defined', () => {
    expect(tokens.color.primary).toBeDefined();
    expect(tokens.color.secondary).toBeDefined();
  });

  test('spacing tokens use correct units', () => {
    Object.values(tokens.spacing).forEach(value => {
      expect(value).toMatch(/^\d+(px|rem|em)$/);
    });
  });
});
```

### Visual Regression Testing

```javascript
// Button.stories.js
import { tokens } from './tokens';

export default {
  title: 'Button',
  parameters: {
    backgrounds: {
      default: tokens.color.background,
    },
  },
};

export const Primary = () => ({
  template: '<button style="background: var(--color-primary)">Primary</button>',
});
```

## Performance Optimization

### CSS Custom Properties with Fallbacks

```css
.button {
  /* Fallback for browsers without CSS variable support */
  background-color: #0066cc;
  background-color: var(--color-primary, #0066cc);
}
```

### Tree Shaking with TypeScript

```typescript
// Only import what you need
import { tokens } from './tokens';

// Tree-shakeable exports
export const { color, spacing } = tokens;
```

### Critical CSS

```javascript
// Extract only critical tokens
const criticalTokens = {
  color: tokens.color,
  spacing: tokens.spacing,
};

// Inline in HTML head
<style>
  :root {
    ${generateCSSVariables(criticalTokens)}
  }
</style>
```
