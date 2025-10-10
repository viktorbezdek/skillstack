**Skill**: [semantic-release](../SKILL.md)

# Version Alignment Standards

Ensure consistent versioning across your project using Git tags as the single source of truth.

---

## Core Principle

**Git tags are canonical** — manifest versions are outputs, never inputs.

```
Git Tag (v1.2.3) → semantic-release → Manifest Files Updated
                                      ↳ package.json
                                      ↳ pyproject.toml
                                      ↳ Cargo.toml
```

---

## Language-Specific Manifest Patterns

| Language | Manifest File    | Version Format                   | Updated By              |
| -------- | ---------------- | -------------------------------- | ----------------------- |
| Python   | `pyproject.toml` | `version = "1.0.0"`              | semantic-release (sed)  |
| Node.js  | `package.json`   | `"version": "0.0.0-development"` | Git tags (never manual) |
| Rust     | `Cargo.toml`     | `version = "0.1.0"`              | semantic-release (exec) |
| Go       | `go.mod`         | Git tags only                    | N/A (no version field)  |

---

## Critical Rules

### 1. Git Tags Are Canonical

The `v1.2.3` Git tag determines the version. All other version references derive from it.

```bash
# Check current version
git describe --tags --abbrev=0
# Output: v1.2.3
```

### 2. Manifest Versions Are Outputs

Version fields in manifest files are **written by automation**, never manually edited.

```yaml
# .releaserc.yml - semantic-release updates pyproject.toml
plugins:
  - "@semantic-release/exec"
  - prepareCmd: |
      sed -i '' "s/^version = .*/version = \"${nextRelease.version}\"/" pyproject.toml
```

### 3. No Dynamic Versioning Libraries

**Avoid these libraries** — they create hidden dependencies and reproducibility issues:

| Language | Avoid                                   | Reason                        |
| -------- | --------------------------------------- | ----------------------------- |
| Python   | setuptools-scm, hatch-vcs, versioningit | Dynamic version at build time |
| Node.js  | N/A (package.json is standard)          | —                             |
| Rust     | vergen, git-version                     | Build-time git dependency     |

### 4. Runtime Version Access

Access version at runtime using standard library functions, not hardcoded strings.

---

## Runtime Version Access Patterns

### Python

```python
from importlib.metadata import version

__version__ = version("mypackage")

# Usage
print(f"MyPackage v{__version__}")
```

### Node.js

```javascript
const { version } = require("./package.json");

// Or with ES modules
import { version } from "./package.json" assert { type: "json" };

console.log(`MyPackage v${version}`);
```

### Rust

```rust
const VERSION: &str = env!("CARGO_PKG_VERSION");

fn main() {
    println!("MyPackage v{}", VERSION);
}
```

### Go

```go
// Build-time injection via ldflags
var Version = "dev"

// Build with:
// go build -ldflags "-X main.Version=1.2.3" .

func main() {
    fmt.Printf("MyPackage v%s\n", Version)
}
```

---

## Hardcode Detection

Before release, audit for hardcoded version strings:

```bash
# Python: Find hardcoded version patterns (environment-agnostic path)
PLUGIN_DIR="${CLAUDE_PLUGIN_ROOT:-$HOME/.claude/plugins/marketplaces/cc-skills/plugins/itp}"
uv run --script "$PLUGIN_DIR/skills/code-hardcode-audit/scripts/audit_hardcodes.py" -- src/

# Grep for suspicious patterns
grep -rn "__version__ = " src/
grep -rn "VERSION = " src/
```

See [`code-hardcode-audit` skill](../../code-hardcode-audit/SKILL.md) for comprehensive detection.

---

## Common Mistakes

### Wrong: Hardcoded Version

```python
# ❌ Never hardcode
__version__ = "1.2.3"
```

### Wrong: Dynamic Library

```toml
# ❌ Avoid in pyproject.toml
[tool.setuptools_scm]
# Creates hidden git dependency at build time
```

### Right: Runtime Discovery

```python
# ✅ Correct approach
from importlib.metadata import version
__version__ = version("mypackage")
```

---

## Integration with semantic-release

semantic-release manages the full version lifecycle:

1. **Analyze commits** → Determine bump type (major/minor/patch)
2. **Update manifest** → Write new version to appropriate file
3. **Create Git tag** → `v1.2.3` becomes the canonical version
4. **Generate changelog** → Document changes
5. **Create GitHub release** → Publish release notes

**Configuration example** (`.releaserc.yml`):

```yaml
plugins:
  - "@semantic-release/commit-analyzer"
  - "@semantic-release/release-notes-generator"
  - "@semantic-release/changelog"
  - - "@semantic-release/exec"
    - prepareCmd: |
        sed -i '' "s/^version = .*/version = \"${nextRelease.version}\"/" pyproject.toml
  - - "@semantic-release/git"
    - assets:
        - CHANGELOG.md
        - pyproject.toml
  - "@semantic-release/github"
```

See [Python Projects Guide](./python-projects-nodejs-semantic-release.md) for complete setup.
