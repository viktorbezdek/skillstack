#!/usr/bin/env python3
"""
Documentation Generator - Generate comprehensive documentation from repository analysis.

Combines best practices from:
- Skill creator (template-driven generation)
- API docs generator (endpoint documentation)
- Documentation creation specialist (DQI-aware generation)

Usage:
    python generate_docs.py /path/to/repo [--output ./docs] [--plan analysis.json]
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Optional
from datetime import datetime


class DocumentationGenerator:
    """Generate comprehensive documentation for a repository."""

    def __init__(self, repo_path: str, output_dir: str = './docs', analysis: Optional[dict] = None):
        self.repo_path = Path(repo_path).resolve()
        self.output_dir = Path(output_dir).resolve()
        self.analysis = analysis or {}

        if not self.repo_path.exists():
            raise ValueError(f"Repository path does not exist: {repo_path}")

    def generate_all(self) -> dict[str, str]:
        """Generate all documentation files."""
        print(f"Generating documentation for: {self.repo_path}")
        print(f"Output directory: {self.output_dir}")

        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)

        generated = {}

        # Generate README
        print("  Generating README.md...")
        readme_content = self.generate_readme()
        readme_path = self.output_dir / 'README.md'
        readme_path.write_text(readme_content)
        generated['README.md'] = str(readme_path)

        # Generate API docs if endpoints exist
        if self.analysis.get('api_surface', {}).get('endpoints'):
            print("  Generating API.md...")
            api_content = self.generate_api_docs()
            api_path = self.output_dir / 'API.md'
            api_path.write_text(api_content)
            generated['API.md'] = str(api_path)

        # Generate architecture docs for larger repos
        if self.analysis.get('structure', {}).get('total_files', 0) > 30:
            print("  Generating ARCHITECTURE.md...")
            arch_content = self.generate_architecture()
            arch_path = self.output_dir / 'ARCHITECTURE.md'
            arch_path.write_text(arch_content)
            generated['ARCHITECTURE.md'] = str(arch_path)

        # Generate contributing guide
        print("  Generating CONTRIBUTING.md...")
        contrib_content = self.generate_contributing()
        contrib_path = self.output_dir / 'CONTRIBUTING.md'
        contrib_path.write_text(contrib_content)
        generated['CONTRIBUTING.md'] = str(contrib_path)

        # Generate getting started guide
        print("  Generating GETTING_STARTED.md...")
        started_content = self.generate_getting_started()
        started_path = self.output_dir / 'GETTING_STARTED.md'
        started_path.write_text(started_content)
        generated['GETTING_STARTED.md'] = str(started_path)

        return generated

    def generate_readme(self) -> str:
        """Generate README.md content."""
        repo_name = self.analysis.get('repo_name', self.repo_path.name)
        primary_lang = self.analysis.get('primary_language', 'Unknown')
        frameworks = self.analysis.get('frameworks', [])

        # Build tech stack section
        tech_stack = []
        if primary_lang:
            tech_stack.append(primary_lang)
        tech_stack.extend(frameworks[:5])  # Limit to top 5

        # Detect package manager and build commands
        install_cmd, run_cmd = self._detect_commands()

        readme = f"""# {repo_name}

> A {primary_lang} project{' built with ' + ', '.join(frameworks[:3]) if frameworks else ''}

## Overview

[Project description - TODO: Add a clear description of what this project does and why it exists]

## Features

- [Feature 1 - TODO]
- [Feature 2 - TODO]
- [Feature 3 - TODO]

## Quick Start

```bash
# Clone the repository
git clone [repository-url]
cd {repo_name}

# Install dependencies
{install_cmd}

# Run the project
{run_cmd}
```

## Tech Stack

{self._format_tech_stack(tech_stack)}

## Documentation

| Document | Description |
|----------|-------------|
| [Getting Started](GETTING_STARTED.md) | First-time setup guide |
| [Contributing](CONTRIBUTING.md) | How to contribute |
"""

        # Add API docs link if applicable
        if self.analysis.get('api_surface', {}).get('endpoints'):
            readme += "| [API Reference](API.md) | API endpoints documentation |\n"

        # Add architecture docs link if applicable
        if self.analysis.get('structure', {}).get('total_files', 0) > 30:
            readme += "| [Architecture](ARCHITECTURE.md) | System design overview |\n"

        readme += f"""
## Project Structure

```
{repo_name}/
{self._format_structure()}
```

## Prerequisites

{self._format_prerequisites()}

## Installation

{self._format_installation(install_cmd)}

## Usage

[TODO: Add usage examples]

```{self._get_code_lang()}
# Example code here
```

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

## License

[TODO: Add license information]

---

Generated on {datetime.now().strftime('%Y-%m-%d')}
"""
        return readme

    def generate_api_docs(self) -> str:
        """Generate API.md content."""
        endpoints = self.analysis.get('api_surface', {}).get('endpoints', [])

        api_doc = """# API Reference

## Overview

This document describes the API endpoints available in this project.

## Base URL

```
http://localhost:3000/api
```

## Authentication

[TODO: Document authentication method]

## Endpoints

"""
        # Group endpoints by path prefix
        grouped = {}
        for ep in endpoints:
            prefix = ep['path'].split('/')[1] if '/' in ep['path'] else 'root'
            if prefix not in grouped:
                grouped[prefix] = []
            grouped[prefix].append(ep)

        for group, eps in grouped.items():
            api_doc += f"### {group.title()}\n\n"

            for ep in eps:
                api_doc += f"""#### `{ep['method']} {ep['path']}`

**Description:** [TODO: Add description]

**Source:** `{ep['file']}`

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| - | - | - | [TODO] |

**Request Example:**

```bash
curl -X {ep['method']} http://localhost:3000{ep['path']}
```

**Response Example:**

```json
{{
  "status": "success",
  "data": {{}}
}}
```

---

"""

        api_doc += """
## Error Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

## Rate Limiting

[TODO: Document rate limiting if applicable]

## Pagination

[TODO: Document pagination format if applicable]
"""
        return api_doc

    def generate_architecture(self) -> str:
        """Generate ARCHITECTURE.md content."""
        structure = self.analysis.get('structure', {})
        languages = self.analysis.get('languages', {})
        frameworks = self.analysis.get('frameworks', [])

        arch_doc = f"""# Architecture Overview

## System Context

This document describes the high-level architecture of the project.

## Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
"""
        # Add detected technologies
        if languages:
            primary = list(languages.keys())[0]
            arch_doc += f"| Language | {primary} | Primary development language |\n"

        for fw in frameworks[:5]:
            arch_doc += f"| Framework | {fw} | [TODO: Add purpose] |\n"

        arch_doc += f"""
## Project Structure

```
{self._format_structure()}
```

## Component Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Application Layer                      │
├─────────────────────────────────────────────────────────┤
│                    Business Logic                         │
├─────────────────────────────────────────────────────────┤
│                    Data Access Layer                      │
├─────────────────────────────────────────────────────────┤
│                    Infrastructure                         │
└─────────────────────────────────────────────────────────┘
```

[TODO: Update diagram to reflect actual architecture]

## Data Flow

[TODO: Describe how data flows through the system]

## Key Design Decisions

### ADR-001: [Decision Title]

**Status:** [Proposed/Accepted/Deprecated]

**Context:** [Why this decision was needed]

**Decision:** [What was decided]

**Consequences:** [Positive and negative outcomes]

---

## Directory Breakdown

| Directory | Purpose |
|-----------|---------|
"""
        for dir_name in structure.get('top_level_dirs', [])[:10]:
            arch_doc += f"| `{dir_name}/` | [TODO: Describe purpose] |\n"

        arch_doc += """
## External Dependencies

[TODO: List key external dependencies and their purpose]

## Security Considerations

[TODO: Document security measures and considerations]

## Scalability

[TODO: Document scalability approach]

## Deployment

[TODO: Document deployment architecture]
"""
        return arch_doc

    def generate_contributing(self) -> str:
        """Generate CONTRIBUTING.md content."""
        primary_lang = self.analysis.get('primary_language', 'Unknown')
        install_cmd, run_cmd = self._detect_commands()
        test_cmd = self._detect_test_command()

        return f"""# Contributing Guide

Thank you for your interest in contributing to this project!

## Getting Started

### Prerequisites

{self._format_prerequisites()}

### Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/{self.analysis.get('repo_name', 'project')}
   cd {self.analysis.get('repo_name', 'project')}
   ```
3. Install dependencies:
   ```bash
   {install_cmd}
   ```
4. Create a branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

### Running the Project

```bash
{run_cmd}
```

### Running Tests

```bash
{test_cmd}
```

### Code Style

{self._format_code_style()}

## Making Changes

1. **Create an issue first** - Discuss the change you want to make
2. **Write tests** - All new features should include tests
3. **Update documentation** - Keep docs in sync with code changes
4. **Follow commit conventions** - Use clear, descriptive commit messages

### Commit Message Format

```
type(scope): description

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
- `feat(auth): add login functionality`
- `fix(api): handle null response`
- `docs(readme): update installation steps`

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update any relevant documentation
3. Add tests for new functionality
4. Ensure all tests pass
5. Request review from maintainers

### PR Checklist

- [ ] Code follows the project style guide
- [ ] Tests added/updated and passing
- [ ] Documentation updated
- [ ] Commit messages follow conventions
- [ ] Branch is up to date with main

## Code Review

All submissions require review. We use GitHub pull requests for this purpose.

## Questions?

Feel free to open an issue for any questions about contributing.
"""

    def generate_getting_started(self) -> str:
        """Generate GETTING_STARTED.md content."""
        repo_name = self.analysis.get('repo_name', self.repo_path.name)
        install_cmd, run_cmd = self._detect_commands()

        return f"""# Getting Started

Welcome! This guide will help you get {repo_name} up and running in just a few minutes.

## Prerequisites

Before you begin, make sure you have:

{self._format_prerequisites()}

## Installation

### Step 1: Clone the Repository

```bash
git clone [repository-url]
cd {repo_name}
```

### Step 2: Install Dependencies

```bash
{install_cmd}
```

### Step 3: Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit with your settings
# [TODO: List key environment variables]
```

### Step 4: Run the Project

```bash
{run_cmd}
```

You should now be able to access the project at `http://localhost:3000` (or the appropriate URL).

## Verify Installation

To verify everything is working:

1. [TODO: Add verification steps]
2. [TODO: Add expected output]

## Next Steps

Now that you're set up, you might want to:

- Read the [API Reference](API.md) to understand available endpoints
- Check out the [Architecture](ARCHITECTURE.md) to understand the codebase
- Learn how to [contribute](CONTRIBUTING.md)

## Common Issues

### Issue: [Common Issue 1]

**Solution:** [How to fix it]

### Issue: [Common Issue 2]

**Solution:** [How to fix it]

## Getting Help

If you run into problems:

1. Check the [Troubleshooting](#common-issues) section above
2. Search existing [issues](../../issues)
3. Open a new issue with details about your problem
"""

    # Helper methods

    def _detect_commands(self) -> tuple[str, str]:
        """Detect install and run commands based on project files."""
        # Check for various package managers
        if (self.repo_path / 'package.json').exists():
            if (self.repo_path / 'pnpm-lock.yaml').exists():
                return 'pnpm install', 'pnpm dev'
            elif (self.repo_path / 'yarn.lock').exists():
                return 'yarn install', 'yarn dev'
            elif (self.repo_path / 'bun.lockb').exists():
                return 'bun install', 'bun dev'
            return 'npm install', 'npm run dev'
        elif (self.repo_path / 'requirements.txt').exists():
            return 'pip install -r requirements.txt', 'python main.py'
        elif (self.repo_path / 'pyproject.toml').exists():
            if (self.repo_path / 'uv.lock').exists():
                return 'uv sync', 'uv run python main.py'
            return 'pip install -e .', 'python -m [module]'
        elif (self.repo_path / 'Gemfile').exists():
            return 'bundle install', 'bundle exec rails server'
        elif (self.repo_path / 'go.mod').exists():
            return 'go mod download', 'go run .'
        elif (self.repo_path / 'Cargo.toml').exists():
            return 'cargo build', 'cargo run'

        return '[install command]', '[run command]'

    def _detect_test_command(self) -> str:
        """Detect test command based on project files."""
        if (self.repo_path / 'package.json').exists():
            return 'npm test'
        elif (self.repo_path / 'pytest.ini').exists() or (self.repo_path / 'pyproject.toml').exists():
            return 'pytest'
        elif (self.repo_path / 'Gemfile').exists():
            return 'bundle exec rspec'
        elif (self.repo_path / 'go.mod').exists():
            return 'go test ./...'
        elif (self.repo_path / 'Cargo.toml').exists():
            return 'cargo test'
        return '[test command]'

    def _format_tech_stack(self, tech_stack: list[str]) -> str:
        """Format tech stack as badges or list."""
        if not tech_stack:
            return "- [TODO: Add tech stack]"
        return '\n'.join(f"- {tech}" for tech in tech_stack)

    def _format_structure(self) -> str:
        """Format directory structure."""
        structure = self.analysis.get('structure', {})
        dirs = structure.get('top_level_dirs', [])[:8]  # Limit to 8

        if not dirs:
            return "├── [TODO: Add structure]"

        lines = []
        for i, d in enumerate(dirs):
            prefix = "├──" if i < len(dirs) - 1 else "└──"
            lines.append(f"{prefix} {d}/")

        return '\n'.join(lines)

    def _format_prerequisites(self) -> str:
        """Format prerequisites based on detected stack."""
        prereqs = []

        if (self.repo_path / 'package.json').exists():
            prereqs.append("- Node.js (v18 or higher recommended)")
            prereqs.append("- npm, yarn, or pnpm")

        if (self.repo_path / 'requirements.txt').exists() or (self.repo_path / 'pyproject.toml').exists():
            prereqs.append("- Python 3.9 or higher")
            prereqs.append("- pip or uv")

        if (self.repo_path / 'go.mod').exists():
            prereqs.append("- Go 1.21 or higher")

        if (self.repo_path / 'Cargo.toml').exists():
            prereqs.append("- Rust (latest stable)")

        if not prereqs:
            prereqs.append("- [TODO: Add prerequisites]")

        return '\n'.join(prereqs)

    def _format_installation(self, install_cmd: str) -> str:
        """Format installation section."""
        return f"""### Using the default package manager

```bash
{install_cmd}
```

### Environment Setup

```bash
# Copy the example environment file (if applicable)
cp .env.example .env

# Edit the environment variables as needed
```
"""

    def _format_code_style(self) -> str:
        """Format code style guidelines based on detected stack."""
        primary_lang = self.analysis.get('primary_language', '')

        if primary_lang == 'TypeScript' or primary_lang == 'JavaScript':
            return """This project uses ESLint and Prettier for code formatting.

```bash
# Check for linting errors
npm run lint

# Auto-fix formatting
npm run format
```"""
        elif primary_lang == 'Python':
            return """This project uses Ruff for linting and formatting.

```bash
# Check for linting errors
ruff check .

# Auto-fix formatting
ruff format .
```"""
        else:
            return "[TODO: Document code style requirements]"

    def _get_code_lang(self) -> str:
        """Get code block language based on primary language."""
        lang_map = {
            'Python': 'python',
            'TypeScript': 'typescript',
            'JavaScript': 'javascript',
            'Go': 'go',
            'Rust': 'rust',
            'Ruby': 'ruby',
            'Java': 'java',
        }
        primary = self.analysis.get('primary_language', '')
        return lang_map.get(primary, '')


def main():
    parser = argparse.ArgumentParser(
        description='Generate comprehensive documentation for a repository'
    )
    parser.add_argument('repo_path', help='Path to repository')
    parser.add_argument('--output', '-o', default='./docs', help='Output directory')
    parser.add_argument('--plan', '-p', help='Analysis JSON file from analyze_repo.py')

    args = parser.parse_args()

    # Load analysis if provided
    analysis = {}
    if args.plan:
        plan_path = Path(args.plan)
        if plan_path.exists():
            analysis = json.loads(plan_path.read_text())
        else:
            print(f"Warning: Plan file not found: {args.plan}")

    # If no analysis, run analyzer first
    if not analysis:
        print("No analysis provided. Running repository analysis first...")
        # Import and run analyzer
        sys.path.insert(0, str(Path(__file__).parent.parent / 'core'))
        try:
            from analyze_repo import RepositoryAnalyzer
            analyzer = RepositoryAnalyzer(args.repo_path)
            analysis = analyzer.analyze()
        except ImportError:
            print("Warning: Could not import analyzer. Using basic analysis.")
            analysis = {
                'repo_name': Path(args.repo_path).name,
                'structure': {'top_level_dirs': []},
                'languages': {},
                'frameworks': [],
            }

    try:
        generator = DocumentationGenerator(
            args.repo_path,
            output_dir=args.output,
            analysis=analysis
        )
        generated = generator.generate_all()

        print("\n" + "="*60)
        print("GENERATION COMPLETE")
        print("="*60)
        print(f"Generated {len(generated)} documentation files:")
        for name, path in generated.items():
            print(f"  ✓ {name}: {path}")
        print(f"\nOutput directory: {args.output}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
