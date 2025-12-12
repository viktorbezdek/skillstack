# Changelog

All notable changes to {{PROJECT_NAME}} will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
{{#UNRELEASED_ADDED}}
- {{ITEM}}
{{/UNRELEASED_ADDED}}

### Changed
{{#UNRELEASED_CHANGED}}
- {{ITEM}}
{{/UNRELEASED_CHANGED}}

### Deprecated
{{#UNRELEASED_DEPRECATED}}
- {{ITEM}}
{{/UNRELEASED_DEPRECATED}}

### Removed
{{#UNRELEASED_REMOVED}}
- {{ITEM}}
{{/UNRELEASED_REMOVED}}

### Fixed
{{#UNRELEASED_FIXED}}
- {{ITEM}}
{{/UNRELEASED_FIXED}}

### Security
{{#UNRELEASED_SECURITY}}
- {{ITEM}}
{{/UNRELEASED_SECURITY}}

---

{{#RELEASES}}
## [{{VERSION}}] - {{DATE}}

{{#RELEASE_SUMMARY}}
> {{SUMMARY}}
{{/RELEASE_SUMMARY}}

{{#ADDED}}
### Added
{{#ITEMS}}
- {{ITEM}} {{#PR}}([#{{PR}}]({{PR_URL}})){{/PR}} {{#AUTHOR}}by @{{AUTHOR}}{{/AUTHOR}}
{{/ITEMS}}
{{/ADDED}}

{{#CHANGED}}
### Changed
{{#ITEMS}}
- {{ITEM}} {{#PR}}([#{{PR}}]({{PR_URL}})){{/PR}} {{#AUTHOR}}by @{{AUTHOR}}{{/AUTHOR}}
{{/ITEMS}}
{{/CHANGED}}

{{#DEPRECATED}}
### Deprecated
{{#ITEMS}}
- {{ITEM}} {{#PR}}([#{{PR}}]({{PR_URL}})){{/PR}}
{{/ITEMS}}
{{/DEPRECATED}}

{{#REMOVED}}
### Removed
{{#ITEMS}}
- {{ITEM}} {{#PR}}([#{{PR}}]({{PR_URL}})){{/PR}}
{{/ITEMS}}
{{/REMOVED}}

{{#FIXED}}
### Fixed
{{#ITEMS}}
- {{ITEM}} {{#PR}}([#{{PR}}]({{PR_URL}})){{/PR}} {{#AUTHOR}}by @{{AUTHOR}}{{/AUTHOR}}
{{/ITEMS}}
{{/FIXED}}

{{#SECURITY}}
### Security
{{#ITEMS}}
- {{ITEM}} {{#PR}}([#{{PR}}]({{PR_URL}})){{/PR}}
{{/ITEMS}}
{{/SECURITY}}

{{#BREAKING}}
### ⚠️ Breaking Changes
{{#ITEMS}}
- **{{ITEM}}**
  - Migration: {{MIGRATION}}
{{/ITEMS}}
{{/BREAKING}}

{{#UPGRADE_NOTES}}
### Upgrade Notes

{{NOTES}}
{{/UPGRADE_NOTES}}

---

{{/RELEASES}}

## Version Links

{{#VERSION_LINKS}}
[{{VERSION}}]: {{COMPARE_URL}}
{{/VERSION_LINKS}}
[Unreleased]: {{UNRELEASED_COMPARE_URL}}

---

## Changelog Guidelines

### Types of Changes

- **Added** - New features
- **Changed** - Changes in existing functionality
- **Deprecated** - Soon-to-be removed features
- **Removed** - Removed features
- **Fixed** - Bug fixes
- **Security** - Vulnerability fixes

### Writing Good Changelog Entries

1. **Be concise** - One line per change
2. **Be specific** - Include what changed and why
3. **Link PRs/issues** - Reference related work
4. **Credit contributors** - Acknowledge authors
5. **Note breaking changes** - Include migration paths
