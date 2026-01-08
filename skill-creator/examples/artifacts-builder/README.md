# Artifacts Builder Skill Example

This example demonstrates a skill for building and packaging Claude Code artifacts with proper bundling and initialization.

## Skill Structure

- **SKILL.md** - Main skill file with instructions
- **LICENSE.txt** - MIT License

## Removed Resources (Described Below)

### scripts/

This skill originally included shell scripts for artifact management:

#### bundle-artifact.sh
Shell script for bundling artifacts into distributable packages:
- Validates artifact structure
- Compresses files into tar.gz or zip
- Includes metadata and version information
- Generates checksums
- Creates deployment-ready packages

**Purpose:** Automate the packaging process for Claude Code artifacts  
**Usage:** `./bundle-artifact.sh <artifact-dir> <output-name>`

#### init-artifact.sh
Shell script for initializing new artifact projects:
- Creates standardized directory structure
- Generates boilerplate files (index.html, styles.css, script.js)
- Sets up configuration files
- Initializes git repository
- Creates README template

**Purpose:** Quick-start new artifact projects with best practices  
**Usage:** `./init-artifact.sh <artifact-name>`

#### shadcn-components.tar.gz
Pre-built shadcn/ui components bundle:
- Common UI components (Button, Card, Dialog, etc.)
- Tailwind CSS configurations
- TypeScript definitions
- React component implementations
- Ready to extract and use

**Purpose:** Provide pre-configured UI components for artifacts  
**Usage:** Extract into artifact project for immediate use

## Use Cases

This skill helps with:
- Creating new Claude Code artifacts
- Bundling artifacts for distribution
- Managing artifact dependencies
- Standardizing artifact structure
- Including pre-built components (shadcn/ui)

## Skill Patterns Demonstrated

- **Executable scripts** - Shell automation for repetitive tasks
- **Binary assets** - Pre-built component bundles
- **Standardization** - Consistent artifact structure
- **Workflow automation** - Init → Develop → Bundle pipeline
- **Dependency management** - Bundled components ready to use

## Restoration

To recreate the scripts:
1. Create `scripts/init-artifact.sh` with project scaffolding logic
2. Create `scripts/bundle-artifact.sh` with packaging logic
3. Download shadcn/ui components and create `scripts/shadcn-components.tar.gz`
4. Make scripts executable: `chmod +x scripts/*.sh`
5. Test with: `./init-artifact.sh test-artifact && ./bundle-artifact.sh test-artifact test`

See SKILL.md for the complete skill implementation.

