# Contributing to {{PROJECT_NAME}}

Thank you for your interest in contributing to {{PROJECT_NAME}}! This guide will help you get started.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Code Review](#code-review)
- [Release Process](#release-process)

## Code of Conduct

This project follows our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code. Please report unacceptable behavior to {{CONDUCT_EMAIL}}.

## Getting Started

### Types of Contributions

We welcome many types of contributions:

| Type | Description | Label |
|------|-------------|-------|
| 🐛 Bug fixes | Fix something that's broken | `bug` |
| ✨ Features | Add new functionality | `enhancement` |
| 📚 Documentation | Improve or add docs | `documentation` |
| 🧪 Tests | Add or improve tests | `testing` |
| 🎨 UI/UX | Improve user interface | `ui` |
| ⚡ Performance | Optimize performance | `performance` |
| ♻️ Refactoring | Code quality improvements | `refactor` |

### Finding Something to Work On

1. Check [open issues]({{ISSUES_URL}})
2. Look for [`good first issue`]({{GOOD_FIRST_ISSUE_URL}}) labels
3. Check the [project roadmap]({{ROADMAP_URL}})

**Before starting:**
- Comment on the issue to let others know you're working on it
- For large changes, open a discussion first

## Development Setup

### Prerequisites

{{#PREREQUISITES}}
- {{PREREQ}}
{{/PREREQUISITES}}

### Clone and Setup

```bash
# Fork the repository on GitHub first, then:
git clone https://github.com/YOUR_USERNAME/{{PROJECT_NAME}}.git
cd {{PROJECT_NAME}}

# Add upstream remote
git remote add upstream {{REPO_URL}}

# Install dependencies
{{INSTALL_COMMAND}}

# Set up pre-commit hooks
{{HOOKS_SETUP_COMMAND}}

# Copy environment configuration
cp .env.example .env
```

### Running Locally

```bash
# Start development server
{{DEV_COMMAND}}

# Run in watch mode
{{WATCH_COMMAND}}
```

### Running Tests

```bash
# Run all tests
{{TEST_COMMAND}}

# Run specific test file
{{TEST_SINGLE_COMMAND}}

# Run with coverage
{{TEST_COVERAGE_COMMAND}}

# Run in watch mode
{{TEST_WATCH_COMMAND}}
```

### Linting and Formatting

```bash
# Check linting
{{LINT_COMMAND}}

# Auto-fix linting issues
{{LINT_FIX_COMMAND}}

# Format code
{{FORMAT_COMMAND}}

# Type checking
{{TYPECHECK_COMMAND}}
```

## Making Changes

### Branch Naming

Use this format: `type/description`

| Type | Use For |
|------|---------|
| `feature/` | New features |
| `fix/` | Bug fixes |
| `docs/` | Documentation |
| `refactor/` | Code refactoring |
| `test/` | Test improvements |
| `chore/` | Maintenance tasks |

**Examples:**
- `feature/add-user-authentication`
- `fix/login-redirect-loop`
- `docs/update-api-reference`

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation |
| `style` | Formatting (no code change) |
| `refactor` | Code restructuring |
| `test` | Adding tests |
| `chore` | Maintenance |
| `perf` | Performance improvement |

**Examples:**
```
feat(auth): add OAuth2 login support

Implements OAuth2 authentication flow with Google and GitHub providers.

Closes #123
```

```
fix(api): handle null response in user endpoint

- Add null check before accessing user properties
- Return 404 instead of 500 for missing users

Fixes #456
```

### Code Style

{{#CODE_STYLE_RULES}}
- {{RULE}}
{{/CODE_STYLE_RULES}}

### Documentation

- Update docs when changing functionality
- Add JSDoc/docstrings to public APIs
- Include code examples in documentation
- Update the CHANGELOG for notable changes

### Testing

- Write tests for new features
- Update tests when changing behavior
- Maintain or improve code coverage
- Test edge cases and error conditions

**Test file naming:**
```
{{TEST_FILE_PATTERN}}
```

## Submitting Changes

### Creating a Pull Request

1. **Update your branch:**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Push your changes:**
   ```bash
   git push origin your-branch-name
   ```

3. **Open a Pull Request:**
   - Go to {{REPO_URL}}/pulls
   - Click "New Pull Request"
   - Select your branch
   - Fill out the PR template

### Pull Request Template

```markdown
## Description

[Describe what this PR does]

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issues

Closes #[issue number]

## Checklist

- [ ] I've read the contributing guidelines
- [ ] My code follows the project's style
- [ ] I've added tests for my changes
- [ ] All tests pass locally
- [ ] I've updated documentation if needed
- [ ] I've updated the CHANGELOG if needed

## Screenshots (if applicable)

[Add screenshots for UI changes]
```

### PR Best Practices

- **Keep PRs focused** - One feature/fix per PR
- **Write clear descriptions** - Explain what and why
- **Include screenshots** - For UI changes
- **Link related issues** - Use "Closes #123"
- **Respond to feedback** - Engage with reviewers

## Code Review

### What Reviewers Look For

- [ ] Code correctness
- [ ] Test coverage
- [ ] Documentation
- [ ] Performance implications
- [ ] Security concerns
- [ ] Code style consistency
- [ ] Backwards compatibility

### Responding to Reviews

- Address all comments
- Explain your reasoning when disagreeing
- Mark conversations as resolved when addressed
- Request re-review after making changes

### Review Turnaround

We aim to review PRs within {{REVIEW_SLA}}. If you haven't heard back, feel free to ping the maintainers.

## Release Process

### Versioning

We use [Semantic Versioning](https://semver.org/):
- **MAJOR** - Breaking changes
- **MINOR** - New features (backwards compatible)
- **PATCH** - Bug fixes (backwards compatible)

### Changelog

Update `CHANGELOG.md` for notable changes:

```markdown
## [Unreleased]

### Added
- New feature description (#PR)

### Changed
- Changed behavior description (#PR)

### Fixed
- Bug fix description (#PR)

### Removed
- Removed feature description (#PR)
```

## Getting Help

- 💬 [Community Chat]({{CHAT_URL}})
- 📧 [Email Maintainers](mailto:{{MAINTAINER_EMAIL}})
- 🐛 [Open an Issue]({{ISSUES_URL}})
- 📖 [Documentation]({{DOCS_URL}})

## Recognition

Contributors are recognized in:
- [CONTRIBUTORS.md](CONTRIBUTORS.md)
- Release notes
- Project README

Thank you for contributing to {{PROJECT_NAME}}! 🎉
