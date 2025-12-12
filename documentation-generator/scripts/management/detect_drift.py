#!/usr/bin/env python3
"""
Documentation Drift Detector - Find documentation that is out of sync with code.

Combines best practices from:
- Documentation management systems (hash-based change detection)
- Documentation audit skill (code-doc synchronization)
- Multi-pass verification approach

Usage:
    python detect_drift.py /path/to/repo ./docs [--output drift-report.json]
"""

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class DriftItem:
    """Represents a single documentation drift issue."""
    severity: str  # 'high', 'medium', 'low'
    category: str  # 'signature', 'path', 'config', 'endpoint', 'dependency'
    doc_file: str
    doc_line: int | None
    doc_content: str
    code_file: str | None
    code_content: str | None
    description: str
    suggestion: str


class DriftDetector:
    """Detect documentation drift by comparing docs to code."""

    # Directories to skip
    SKIP_DIRS = {
        'node_modules', '.git', '__pycache__', '.venv', 'venv',
        'dist', 'build', '.next', '.nuxt', 'coverage', '.pytest_cache',
        'vendor', 'target', 'bin', 'obj', '.idea', '.vscode'
    }

    def __init__(self, repo_path: str, docs_path: str):
        self.repo_path = Path(repo_path).resolve()
        self.docs_path = Path(docs_path).resolve()

        if not self.repo_path.exists():
            raise ValueError(f"Repository path does not exist: {repo_path}")
        if not self.docs_path.exists():
            raise ValueError(f"Documentation path does not exist: {docs_path}")

        self.drift_items: list[DriftItem] = []

    def detect(self) -> dict[str, Any]:
        """Run drift detection and return report."""
        print(f"Detecting drift between:")
        print(f"  Repository: {self.repo_path}")
        print(f"  Documentation: {self.docs_path}")

        # Run all detection passes
        print("\n  Pass 1: Checking file path references...")
        self._check_file_paths()

        print("  Pass 2: Checking function/class references...")
        self._check_code_references()

        print("  Pass 3: Checking configuration references...")
        self._check_config_references()

        print("  Pass 4: Checking dependency versions...")
        self._check_dependency_versions()

        print("  Pass 5: Checking API endpoint references...")
        self._check_api_endpoints()

        # Generate report
        return self._generate_report()

    def _check_file_paths(self):
        """Check that file paths mentioned in docs exist."""
        for doc_file in self.docs_path.rglob('*.md'):
            try:
                content = doc_file.read_text()
                lines = content.splitlines()

                # Find file path references
                # Patterns: `path/to/file`, src/file.ts, ./file.js
                path_patterns = [
                    r'`([a-zA-Z0-9_\-./]+\.[a-zA-Z0-9]+)`',  # `path/to/file.ext`
                    r'(?:^|\s)((?:src|lib|app|test|scripts)/[a-zA-Z0-9_\-./]+)',  # src/path
                    r'(?:^|\s)(\./[a-zA-Z0-9_\-./]+)',  # ./path
                ]

                for line_num, line in enumerate(lines, 1):
                    for pattern in path_patterns:
                        matches = re.findall(pattern, line)
                        for match in matches:
                            # Skip obvious non-file references
                            if any(skip in match.lower() for skip in ['http', 'example', 'your-', '<', '>']):
                                continue

                            # Check if file exists in repo
                            potential_path = self.repo_path / match
                            if not potential_path.exists() and not (self.repo_path / match.lstrip('./')).exists():
                                # Might be a valid file, add as potential drift
                                self.drift_items.append(DriftItem(
                                    severity='medium',
                                    category='path',
                                    doc_file=str(doc_file.relative_to(self.docs_path)),
                                    doc_line=line_num,
                                    doc_content=line.strip()[:100],
                                    code_file=None,
                                    code_content=None,
                                    description=f"Referenced file may not exist: {match}",
                                    suggestion=f"Verify path exists or update documentation"
                                ))

            except Exception as e:
                print(f"    Warning: Could not process {doc_file}: {e}")

    def _check_code_references(self):
        """Check that function/class names mentioned in docs exist in code."""
        # Build index of code symbols
        code_symbols = self._extract_code_symbols()

        for doc_file in self.docs_path.rglob('*.md'):
            try:
                content = doc_file.read_text()
                lines = content.splitlines()

                # Find code references in backticks
                for line_num, line in enumerate(lines, 1):
                    # Look for function calls: `functionName()` or `ClassName`
                    code_refs = re.findall(r'`([a-zA-Z_][a-zA-Z0-9_]*(?:\(\))?)`', line)

                    for ref in code_refs:
                        # Clean up reference
                        symbol = ref.rstrip('()')

                        # Skip common words and short refs
                        if len(symbol) < 3 or symbol.lower() in ['true', 'false', 'null', 'none', 'string', 'number', 'int', 'bool', 'void']:
                            continue

                        # Check if symbol exists in code
                        if symbol not in code_symbols and symbol.lower() not in [s.lower() for s in code_symbols]:
                            # Could be external API, only flag if looks like internal
                            if not symbol[0].isupper() or symbol.endswith('()'):
                                self.drift_items.append(DriftItem(
                                    severity='low',
                                    category='signature',
                                    doc_file=str(doc_file.relative_to(self.docs_path)),
                                    doc_line=line_num,
                                    doc_content=line.strip()[:100],
                                    code_file=None,
                                    code_content=None,
                                    description=f"Referenced symbol may not exist: {symbol}",
                                    suggestion="Verify function/class exists or update documentation"
                                ))

            except Exception as e:
                print(f"    Warning: Could not process {doc_file}: {e}")

    def _extract_code_symbols(self) -> set[str]:
        """Extract function and class names from code files."""
        symbols = set()

        patterns = {
            '.py': [
                r'(?:def|class)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
            ],
            '.js': [
                r'(?:function|class|const|let|var)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
                r'([a-zA-Z_][a-zA-Z0-9_]*)\s*[=:]\s*(?:function|\([^)]*\)\s*=>)',
            ],
            '.ts': [
                r'(?:function|class|const|let|interface|type|enum)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
                r'([a-zA-Z_][a-zA-Z0-9_]*)\s*[=:]\s*(?:function|\([^)]*\)\s*=>)',
            ],
            '.go': [
                r'func\s+(?:\([^)]+\)\s+)?([a-zA-Z_][a-zA-Z0-9_]*)',
                r'type\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+struct',
            ],
            '.java': [
                r'(?:class|interface|enum)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
                r'(?:public|private|protected)?\s*(?:static)?\s*\w+\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(',
            ],
        }

        for ext, ext_patterns in patterns.items():
            for code_file in self.repo_path.rglob(f'*{ext}'):
                if any(skip in code_file.parts for skip in self.SKIP_DIRS):
                    continue

                try:
                    content = code_file.read_text()
                    for pattern in ext_patterns:
                        matches = re.findall(pattern, content)
                        symbols.update(matches)
                except Exception:
                    pass

        return symbols

    def _check_config_references(self):
        """Check that configuration values mentioned in docs match actual configs."""
        # Find config files
        config_files = {}
        config_patterns = [
            '*.json', '*.yaml', '*.yml', '*.toml', '*.env.example',
            'tsconfig.json', 'package.json', 'pyproject.toml'
        ]

        for pattern in config_patterns:
            for config_file in self.repo_path.glob(pattern):
                if any(skip in config_file.parts for skip in self.SKIP_DIRS):
                    continue
                try:
                    config_files[config_file.name] = config_file.read_text()
                except Exception:
                    pass

        # Check docs for config references
        for doc_file in self.docs_path.rglob('*.md'):
            try:
                content = doc_file.read_text()

                # Check for environment variable references
                env_vars = re.findall(r'`([A-Z][A-Z0-9_]+)`', content)
                env_example = config_files.get('.env.example', '')

                for var in env_vars:
                    # Skip common non-env vars
                    if var in ['README', 'API', 'HTTP', 'JSON', 'HTML', 'CSS', 'URL', 'URI']:
                        continue

                    if env_example and var not in env_example:
                        self.drift_items.append(DriftItem(
                            severity='medium',
                            category='config',
                            doc_file=str(doc_file.relative_to(self.docs_path)),
                            doc_line=None,
                            doc_content=f"Reference to {var}",
                            code_file='.env.example',
                            code_content=None,
                            description=f"Environment variable {var} not found in .env.example",
                            suggestion="Add variable to .env.example or update documentation"
                        ))

            except Exception as e:
                print(f"    Warning: Could not process {doc_file}: {e}")

    def _check_dependency_versions(self):
        """Check that dependency versions in docs match package files."""
        # Get actual versions from package files
        actual_versions = {}

        # Check package.json
        pkg_json = self.repo_path / 'package.json'
        if pkg_json.exists():
            try:
                pkg_data = json.loads(pkg_json.read_text())
                deps = {**pkg_data.get('dependencies', {}), **pkg_data.get('devDependencies', {})}
                for name, version in deps.items():
                    actual_versions[name] = version.lstrip('^~>=<')
            except Exception:
                pass

        # Check requirements.txt
        requirements = self.repo_path / 'requirements.txt'
        if requirements.exists():
            try:
                for line in requirements.read_text().splitlines():
                    if '==' in line:
                        name, version = line.split('==')
                        actual_versions[name.strip()] = version.strip()
            except Exception:
                pass

        # Check docs for version references
        for doc_file in self.docs_path.rglob('*.md'):
            try:
                content = doc_file.read_text()
                lines = content.splitlines()

                # Look for version patterns
                version_refs = re.findall(r'([a-zA-Z0-9-]+)[@:]\s*[v]?(\d+\.\d+(?:\.\d+)?)', content)

                for line_num, line in enumerate(lines, 1):
                    for pkg, doc_version in re.findall(r'([a-zA-Z0-9-]+)[@:]\s*[v]?(\d+\.\d+(?:\.\d+)?)', line):
                        if pkg in actual_versions:
                            actual = actual_versions[pkg]
                            if not actual.startswith(doc_version):
                                self.drift_items.append(DriftItem(
                                    severity='high',
                                    category='dependency',
                                    doc_file=str(doc_file.relative_to(self.docs_path)),
                                    doc_line=line_num,
                                    doc_content=line.strip()[:100],
                                    code_file='package.json or requirements.txt',
                                    code_content=f"{pkg}: {actual}",
                                    description=f"Version mismatch: docs say {pkg}@{doc_version}, actual is {actual}",
                                    suggestion="Update documentation to match actual version"
                                ))

            except Exception as e:
                print(f"    Warning: Could not process {doc_file}: {e}")

    def _check_api_endpoints(self):
        """Check that API endpoints in docs match code."""
        # Extract actual endpoints from code
        actual_endpoints = self._extract_endpoints()

        for doc_file in self.docs_path.rglob('*.md'):
            try:
                content = doc_file.read_text()
                lines = content.splitlines()

                # Find documented endpoints
                endpoint_pattern = r'(?:GET|POST|PUT|PATCH|DELETE)\s+(/[a-zA-Z0-9/_\-{}:]+)'

                for line_num, line in enumerate(lines, 1):
                    matches = re.findall(endpoint_pattern, line, re.IGNORECASE)
                    for endpoint in matches:
                        # Normalize endpoint (remove params)
                        normalized = re.sub(r'{[^}]+}', '*', endpoint)
                        normalized = re.sub(r':[a-zA-Z]+', '*', normalized)

                        # Check if endpoint exists (fuzzy match)
                        found = False
                        for actual in actual_endpoints:
                            actual_normalized = re.sub(r'{[^}]+}', '*', actual)
                            actual_normalized = re.sub(r':[a-zA-Z]+', '*', actual_normalized)
                            if normalized == actual_normalized:
                                found = True
                                break

                        if not found and actual_endpoints:
                            self.drift_items.append(DriftItem(
                                severity='high',
                                category='endpoint',
                                doc_file=str(doc_file.relative_to(self.docs_path)),
                                doc_line=line_num,
                                doc_content=line.strip()[:100],
                                code_file=None,
                                code_content=None,
                                description=f"Documented endpoint may not exist: {endpoint}",
                                suggestion="Verify endpoint exists in code or update documentation"
                            ))

            except Exception as e:
                print(f"    Warning: Could not process {doc_file}: {e}")

    def _extract_endpoints(self) -> set[str]:
        """Extract API endpoints from code."""
        endpoints = set()

        route_patterns = [
            # Express/Fastify
            re.compile(r'(?:app|router)\.(get|post|put|patch|delete)\s*\(\s*[\'"]([^\'"]+)[\'"]'),
            # FastAPI/Flask
            re.compile(r'@(?:app|router)\.(get|post|put|patch|delete)\s*\(\s*[\'"]([^\'"]+)[\'"]'),
            # Django
            re.compile(r'path\s*\(\s*[\'"]([^\'"]+)[\'"]'),
            # Generic REST
            re.compile(r'[\'"](/api/[^\'"]+)[\'"]'),
        ]

        for ext in ['.py', '.js', '.ts', '.go', '.java']:
            for code_file in self.repo_path.rglob(f'*{ext}'):
                if any(skip in code_file.parts for skip in self.SKIP_DIRS):
                    continue

                try:
                    content = code_file.read_text()
                    for pattern in route_patterns:
                        matches = pattern.findall(content)
                        for match in matches:
                            if isinstance(match, tuple):
                                endpoints.add(match[1])
                            else:
                                endpoints.add(match)
                except Exception:
                    pass

        return endpoints

    def _generate_report(self) -> dict[str, Any]:
        """Generate drift detection report."""
        # Group by severity
        by_severity = {'high': [], 'medium': [], 'low': []}
        by_category = {}

        for item in self.drift_items:
            by_severity[item.severity].append(item)
            if item.category not in by_category:
                by_category[item.category] = []
            by_category[item.category].append(item)

        return {
            'detected_at': datetime.now().isoformat(),
            'repo_path': str(self.repo_path),
            'docs_path': str(self.docs_path),
            'summary': {
                'total_drift_items': len(self.drift_items),
                'high_severity': len(by_severity['high']),
                'medium_severity': len(by_severity['medium']),
                'low_severity': len(by_severity['low']),
                'by_category': {k: len(v) for k, v in by_category.items()},
            },
            'drift_items': [
                {
                    'severity': item.severity,
                    'category': item.category,
                    'doc_file': item.doc_file,
                    'doc_line': item.doc_line,
                    'doc_content': item.doc_content,
                    'code_file': item.code_file,
                    'code_content': item.code_content,
                    'description': item.description,
                    'suggestion': item.suggestion,
                }
                for item in sorted(self.drift_items, key=lambda x: ('high', 'medium', 'low').index(x.severity))
            ],
        }


def main():
    parser = argparse.ArgumentParser(
        description='Detect documentation drift by comparing docs to code'
    )
    parser.add_argument('repo_path', help='Path to repository')
    parser.add_argument('docs_path', help='Path to documentation directory')
    parser.add_argument('--output', '-o', help='Output report to JSON file')
    parser.add_argument('--fail-on-high', action='store_true',
                        help='Exit with error if high severity issues found')

    args = parser.parse_args()

    try:
        detector = DriftDetector(args.repo_path, args.docs_path)
        report = detector.detect()

        # Output JSON if requested
        if args.output:
            Path(args.output).write_text(json.dumps(report, indent=2))
            print(f"\nReport written to: {args.output}")

        # Print summary
        print("\n" + "="*60)
        print("DRIFT DETECTION REPORT")
        print("="*60)
        print(f"Total drift items: {report['summary']['total_drift_items']}")
        print(f"  High severity: {report['summary']['high_severity']}")
        print(f"  Medium severity: {report['summary']['medium_severity']}")
        print(f"  Low severity: {report['summary']['low_severity']}")

        if report['summary']['by_category']:
            print("\nBy category:")
            for cat, count in report['summary']['by_category'].items():
                print(f"  {cat}: {count}")

        # Print high severity items
        high_items = [i for i in report['drift_items'] if i['severity'] == 'high']
        if high_items:
            print("\n" + "-"*60)
            print("HIGH SEVERITY ISSUES")
            print("-"*60)
            for item in high_items[:10]:  # Limit to first 10
                print(f"\n⚠ {item['description']}")
                print(f"  File: {item['doc_file']}" + (f":{item['doc_line']}" if item['doc_line'] else ""))
                print(f"  Suggestion: {item['suggestion']}")

            if len(high_items) > 10:
                print(f"\n... and {len(high_items) - 10} more high severity issues")

        # Exit with error if requested
        if args.fail_on_high and report['summary']['high_severity'] > 0:
            print(f"\n❌ FAILED: Found {report['summary']['high_severity']} high severity drift issues")
            sys.exit(1)
        elif report['summary']['total_drift_items'] == 0:
            print("\n✓ No drift detected - documentation appears to be in sync!")
        else:
            print(f"\n⚠ Found {report['summary']['total_drift_items']} potential drift issues to review")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
