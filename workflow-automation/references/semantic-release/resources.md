**Skill**: [semantic-release](../SKILL.md)

## Resources

### scripts/

**init_user_config.sh**: Create Level 2 (User) configuration

- Creates `~/semantic-release-config/` with npm package structure
- Initializes git repository for version control
- Publishable as `@username/semantic-release-config`
- One-time setup for personal defaults

**create_org_config.sh**: Create Level 3 (Organization) configuration

- Creates organization shareable config package
- Intended for team/company-wide standards
- Publishable to npm registry as `@org/config-name`
- One-time setup per organization

**init_project.sh**: Initialize Level 4 (Project) configuration

- Three modes: `--user`, `--org ORG/CONFIG`, or `--inline`
- Installs semantic-release v25+ dependencies
- Creates `.releaserc.yml` (extends or inline)
- Creates `.github/workflows/release.yml`
- Configures package.json

**PyPI Publishing**: See [`pypi-doppler` skill](../../pypi-doppler/SKILL.md)

- Canonical script with CI detection guards: [`scripts/publish-to-pypi.sh`](../../pypi-doppler/scripts/publish-to-pypi.sh)
- Retrieves PYPI_TOKEN from Doppler (claude-config/prd)
- Builds and publishes Python packages
- Local-first approach (30 seconds vs 3-5 minutes in GitHub Actions)

**generate-adr-notes.mjs**: Generate ADR/Design Spec links for release notes

- Detects ADRs changed since last release via git diff
- Parses commit messages for `ADR: YYYY-MM-DD-slug` references
- Outputs markdown with full HTTPS URLs for GitHub releases
- Used via `generateNotesCmd` in `@semantic-release/exec`
- See [ADR Release Linking](./adr-release-linking.md) for configuration

### assets/templates/

**shareable-config/**: Complete shareable config package template

- `package.json` - Package manifest with v25+ dependencies
- `index.js` - Configuration module with 2025 plugins
- `README.md` - Usage documentation

**github-workflow.yml**: GitHub Actions workflow template

- Node.js 24 setup
- npm ci for dependency installation
- npm audit signatures for security verification
- OIDC trusted publishing configuration

**package.json**: Project package.json template

- Version set to `0.0.0-development`
- Node.js 24.10.0+ engine requirement
- semantic-release v25+ dev dependency

**releaserc.yml**: Configuration file template

- Shareable config extend pattern
- Inline configuration alternative

### references/

**2025-updates.md**: Complete changelog of v25 updates

- Breaking changes (Node 22.14+ requirement, verify with `node --version`)
- New features (OIDC trusted publishing with permissions YAML)
- Plugin versions (references init_project.sh as source of truth)
- Workspace support patterns
- Security enhancements
