**Skill**: [semantic-release](../SKILL.md)

# semantic-release 2025 Updates

> **Changelog & Migration Guide**: What changed in v25 and how to upgrade

## v25.0.0 (October 2024)

### Breaking Changes

- **Node.js**: Minimum v22.14.0 required
  - For v24 range: Minimum v24.10.0
  - Dropped support for v20, v21, v23
  - Verify version: `node --version`
- **npm**: Upgraded to v11 for publishing

### New Features

- **Trusted Publishing (OIDC)**: No long-lived NPM_TOKEN needed
  - Automatic npm provenance attestations
  - GitHub Actions is trusted identity provider
  - Requires permissions:
    ```yaml
    permissions:
      id-token: write
      contents: write
      issues: write
      pull-requests: write
    ```
  - No `NPM_TOKEN` secret needed when publishing to npm

### Plugin Updates

All core plugins updated to latest stable versions (v25 compatible).

Version source of truth: [`scripts/init_project.sh`](../scripts/init_project.sh) (lines 146-153)

## Workspace Support (2025)

### pnpm Workspaces

Use `@anolilab/semantic-release-pnpm` plugin:

```bash
npm install --save-dev @anolilab/semantic-release-pnpm
```

### npm Workspaces

Use `multi-semantic-release` or `@anolilab/multi-semantic-release`:

```bash
pnpm -r --workspace-concurrency=1 exec -- npx --no-install semantic-release
```

## Security Enhancements

- `npm audit signatures` - Verify provenance attestations
- OIDC trusted publishing - Eliminates long-lived tokens
- Supply chain security via npm provenance
