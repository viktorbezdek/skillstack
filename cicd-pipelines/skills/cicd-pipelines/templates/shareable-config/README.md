# @USER/semantic-release-config

Shareable semantic-release configuration following 2024/2025 best practices.

## Installation

```bash
npm install --save-dev @USER/semantic-release-config
```

## Usage

In `.releaserc.yml` or `.releaserc.json`:

```yaml
extends: "@USER/semantic-release-config"
```

Or in `package.json`:

```json
{
  "release": {
    "extends": "@USER/semantic-release-config"
  }
}
```

## What It Includes

- Conventional Commits analysis
- Automated changelog generation
- GitHub releases
- Git commits of generated files
- Custom build script execution

## Customization

To override or extend this configuration:

```yaml
extends: "@USER/semantic-release-config"

# Override specific plugin options
plugins:
  - - "@semantic-release/github"
    - assets:
        - path: "custom-dist.zip"
```

## Publishing

```bash
npm publish --access public
```
