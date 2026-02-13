**Skill**: [semantic-release](../SKILL.md)

## Monorepo Support (pnpm/npm Workspaces)

### pnpm Workspaces

Install pnpm plugin:

```bash
npm install --save-dev @anolilab/semantic-release-pnpm
```

Run release across workspaces:

```bash
pnpm -r --workspace-concurrency=1 exec -- npx --no-install semantic-release
```

### npm Workspaces

Use multi-semantic-release:

```bash
npm install --save-dev @anolilab/multi-semantic-release
npx multi-semantic-release
```
