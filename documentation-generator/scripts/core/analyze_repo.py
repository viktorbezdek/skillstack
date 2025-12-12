#!/usr/bin/env python3
"""
Repository Analyzer - Comprehensive analysis of repository structure and documentation status.

Combines best practices from:
- Documentation audit skill (multi-pass analysis)
- Skill creator (code extraction patterns)
- Documentation management systems (indexing patterns)

Usage:
    python analyze_repo.py /path/to/repo [--output analysis.json]
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any
from collections import defaultdict
from datetime import datetime

# Language detection patterns
LANGUAGE_EXTENSIONS = {
    '.py': 'Python',
    '.js': 'JavaScript',
    '.ts': 'TypeScript',
    '.tsx': 'TypeScript',
    '.jsx': 'JavaScript',
    '.java': 'Java',
    '.go': 'Go',
    '.rs': 'Rust',
    '.rb': 'Ruby',
    '.php': 'PHP',
    '.cs': 'C#',
    '.cpp': 'C++',
    '.c': 'C',
    '.swift': 'Swift',
    '.kt': 'Kotlin',
    '.scala': 'Scala',
}

# Framework detection patterns
FRAMEWORK_PATTERNS = {
    'React': ['react', 'jsx', 'tsx', 'useState', 'useEffect'],
    'Next.js': ['next.config', 'pages/', 'app/', 'getServerSideProps', 'getStaticProps'],
    'Vue': ['vue', '.vue', 'createApp', 'defineComponent'],
    'Angular': ['angular.json', '@angular', 'NgModule'],
    'Express': ['express', 'app.get(', 'app.post(', 'router.'],
    'FastAPI': ['fastapi', 'FastAPI()', '@app.get', '@app.post'],
    'Django': ['django', 'settings.py', 'urls.py', 'models.py'],
    'Flask': ['flask', 'Flask(__name__)', '@app.route'],
    'Spring': ['springframework', '@SpringBootApplication', '@RestController'],
    'Rails': ['rails', 'Gemfile', 'config/routes.rb'],
    'Prisma': ['prisma', 'schema.prisma', 'PrismaClient'],
    'SQLAlchemy': ['sqlalchemy', 'Base.metadata', 'Session'],
}

# Documentation file patterns
DOC_PATTERNS = {
    'readme': r'^readme(\.(md|rst|txt))?$',
    'contributing': r'^contributing(\.(md|rst|txt))?$',
    'changelog': r'^(changelog|history|changes)(\.(md|rst|txt))?$',
    'license': r'^(license|licence)(\.(md|rst|txt))?$',
    'api_docs': r'^(api|api[-_]?reference|api[-_]?docs?)(\.(md|rst|txt))?$',
    'architecture': r'^(architecture|design|system[-_]?design)(\.(md|rst|txt))?$',
    'security': r'^security(\.(md|rst|txt))?$',
    'code_of_conduct': r'^code[-_]?of[-_]?conduct(\.(md|rst|txt))?$',
}

# Directories to skip
SKIP_DIRS = {
    'node_modules', '.git', '__pycache__', '.venv', 'venv',
    'dist', 'build', '.next', '.nuxt', 'coverage', '.pytest_cache',
    'vendor', 'target', 'bin', 'obj', '.idea', '.vscode'
}


class RepositoryAnalyzer:
    """Comprehensive repository analyzer for documentation generation."""

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path).resolve()
        if not self.repo_path.exists():
            raise ValueError(f"Repository path does not exist: {repo_path}")

        self.analysis = {
            'repo_path': str(self.repo_path),
            'repo_name': self.repo_path.name,
            'analyzed_at': datetime.now().isoformat(),
            'structure': {},
            'languages': {},
            'frameworks': [],
            'documentation': {
                'existing': {},
                'gaps': [],
                'quality_score': 0,
            },
            'code_metrics': {},
            'api_surface': {},
            'recommendations': [],
        }

    def analyze(self) -> dict[str, Any]:
        """Run complete repository analysis."""
        print(f"Analyzing repository: {self.repo_path}")

        # Phase 1: Structure analysis
        print("  Phase 1: Analyzing structure...")
        self._analyze_structure()

        # Phase 2: Language and framework detection
        print("  Phase 2: Detecting languages and frameworks...")
        self._detect_languages()
        self._detect_frameworks()

        # Phase 3: Documentation inventory
        print("  Phase 3: Inventorying documentation...")
        self._inventory_documentation()

        # Phase 4: Code metrics
        print("  Phase 4: Extracting code metrics...")
        self._extract_code_metrics()

        # Phase 5: API surface extraction
        print("  Phase 5: Extracting API surface...")
        self._extract_api_surface()

        # Phase 6: Quality assessment
        print("  Phase 6: Assessing documentation quality...")
        self._assess_quality()

        # Phase 7: Generate recommendations
        print("  Phase 7: Generating recommendations...")
        self._generate_recommendations()

        return self.analysis

    def _analyze_structure(self):
        """Analyze repository directory structure."""
        structure = {
            'total_files': 0,
            'total_dirs': 0,
            'file_types': defaultdict(int),
            'top_level_dirs': [],
            'doc_dirs': [],
            'test_dirs': [],
            'src_dirs': [],
        }

        for item in self.repo_path.iterdir():
            if item.is_dir() and item.name not in SKIP_DIRS:
                structure['top_level_dirs'].append(item.name)
                if item.name.lower() in ('docs', 'doc', 'documentation'):
                    structure['doc_dirs'].append(item.name)
                elif item.name.lower() in ('test', 'tests', '__tests__', 'spec', 'specs'):
                    structure['test_dirs'].append(item.name)
                elif item.name.lower() in ('src', 'lib', 'app', 'source'):
                    structure['src_dirs'].append(item.name)

        # Count all files
        for path in self.repo_path.rglob('*'):
            if any(skip in path.parts for skip in SKIP_DIRS):
                continue
            if path.is_file():
                structure['total_files'] += 1
                ext = path.suffix.lower()
                structure['file_types'][ext] += 1
            elif path.is_dir():
                structure['total_dirs'] += 1

        structure['file_types'] = dict(structure['file_types'])
        self.analysis['structure'] = structure

    def _detect_languages(self):
        """Detect programming languages used in repository."""
        lang_counts = defaultdict(int)
        lang_lines = defaultdict(int)

        for path in self.repo_path.rglob('*'):
            if any(skip in path.parts for skip in SKIP_DIRS):
                continue
            if path.is_file() and path.suffix.lower() in LANGUAGE_EXTENSIONS:
                lang = LANGUAGE_EXTENSIONS[path.suffix.lower()]
                lang_counts[lang] += 1
                try:
                    lines = len(path.read_text(errors='ignore').splitlines())
                    lang_lines[lang] += lines
                except Exception:
                    pass

        # Sort by line count
        languages = {}
        for lang in sorted(lang_lines, key=lambda x: lang_lines[x], reverse=True):
            languages[lang] = {
                'files': lang_counts[lang],
                'lines': lang_lines[lang],
            }

        self.analysis['languages'] = languages
        if languages:
            self.analysis['primary_language'] = list(languages.keys())[0]

    def _detect_frameworks(self):
        """Detect frameworks and libraries used."""
        detected = set()

        # Check package files
        package_files = {
            'package.json': self._check_npm_packages,
            'requirements.txt': self._check_pip_packages,
            'Pipfile': self._check_pipfile,
            'pyproject.toml': self._check_pyproject,
            'Gemfile': self._check_gemfile,
            'go.mod': self._check_go_mod,
            'Cargo.toml': self._check_cargo,
            'pom.xml': self._check_pom,
            'build.gradle': self._check_gradle,
        }

        for filename, checker in package_files.items():
            pkg_file = self.repo_path / filename
            if pkg_file.exists():
                try:
                    content = pkg_file.read_text()
                    detected.update(checker(content))
                except Exception:
                    pass

        # Check file patterns
        for path in self.repo_path.rglob('*'):
            if any(skip in path.parts for skip in SKIP_DIRS):
                continue
            path_str = str(path.relative_to(self.repo_path))
            for framework, patterns in FRAMEWORK_PATTERNS.items():
                for pattern in patterns:
                    if pattern in path_str.lower():
                        detected.add(framework)
                        break

        self.analysis['frameworks'] = sorted(detected)

    def _check_npm_packages(self, content: str) -> set[str]:
        """Check package.json for frameworks."""
        detected = set()
        try:
            data = json.loads(content)
            deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}

            framework_packages = {
                'react': 'React',
                'next': 'Next.js',
                'vue': 'Vue',
                '@angular/core': 'Angular',
                'express': 'Express',
                'fastify': 'Fastify',
                'prisma': 'Prisma',
                'typeorm': 'TypeORM',
            }

            for pkg, framework in framework_packages.items():
                if pkg in deps:
                    detected.add(framework)
        except json.JSONDecodeError:
            pass
        return detected

    def _check_pip_packages(self, content: str) -> set[str]:
        """Check requirements.txt for frameworks."""
        detected = set()
        framework_packages = {
            'django': 'Django',
            'flask': 'Flask',
            'fastapi': 'FastAPI',
            'sqlalchemy': 'SQLAlchemy',
            'prisma': 'Prisma',
            'pytest': 'pytest',
        }

        for line in content.splitlines():
            line = line.strip().lower()
            for pkg, framework in framework_packages.items():
                if line.startswith(pkg):
                    detected.add(framework)
        return detected

    def _check_pipfile(self, content: str) -> set[str]:
        return self._check_pip_packages(content)

    def _check_pyproject(self, content: str) -> set[str]:
        return self._check_pip_packages(content)

    def _check_gemfile(self, content: str) -> set[str]:
        detected = set()
        if 'rails' in content.lower():
            detected.add('Rails')
        if 'sinatra' in content.lower():
            detected.add('Sinatra')
        return detected

    def _check_go_mod(self, content: str) -> set[str]:
        detected = set()
        if 'gin-gonic' in content:
            detected.add('Gin')
        if 'gorilla/mux' in content:
            detected.add('Gorilla')
        if 'fiber' in content:
            detected.add('Fiber')
        return detected

    def _check_cargo(self, content: str) -> set[str]:
        detected = set()
        if 'actix-web' in content:
            detected.add('Actix')
        if 'rocket' in content:
            detected.add('Rocket')
        if 'axum' in content:
            detected.add('Axum')
        return detected

    def _check_pom(self, content: str) -> set[str]:
        detected = set()
        if 'spring-boot' in content:
            detected.add('Spring Boot')
        return detected

    def _check_gradle(self, content: str) -> set[str]:
        detected = set()
        if 'spring-boot' in content:
            detected.add('Spring Boot')
        return detected

    def _inventory_documentation(self):
        """Inventory existing documentation."""
        docs = {
            'files': [],
            'total_words': 0,
            'by_type': {},
        }

        # Find documentation files
        for path in self.repo_path.rglob('*'):
            if any(skip in path.parts for skip in SKIP_DIRS):
                continue
            if not path.is_file():
                continue
            if path.suffix.lower() not in ('.md', '.rst', '.txt', '.adoc'):
                continue

            rel_path = str(path.relative_to(self.repo_path))
            filename = path.name.lower()

            # Classify document type
            doc_type = 'other'
            for dtype, pattern in DOC_PATTERNS.items():
                if re.match(pattern, filename, re.IGNORECASE):
                    doc_type = dtype
                    break

            try:
                content = path.read_text(errors='ignore')
                word_count = len(content.split())
                line_count = len(content.splitlines())
            except Exception:
                word_count = 0
                line_count = 0

            doc_info = {
                'path': rel_path,
                'type': doc_type,
                'words': word_count,
                'lines': line_count,
            }

            docs['files'].append(doc_info)
            docs['total_words'] += word_count

            if doc_type not in docs['by_type']:
                docs['by_type'][doc_type] = []
            docs['by_type'][doc_type].append(rel_path)

        self.analysis['documentation']['existing'] = docs

        # Identify gaps
        gaps = []
        if 'readme' not in docs['by_type']:
            gaps.append('README.md - No readme found')
        if 'contributing' not in docs['by_type']:
            gaps.append('CONTRIBUTING.md - No contribution guidelines')
        if 'api_docs' not in docs['by_type'] and self.analysis.get('api_surface', {}).get('endpoints'):
            gaps.append('API.md - API exists but no documentation')
        if 'architecture' not in docs['by_type'] and self.analysis['structure'].get('total_files', 0) > 50:
            gaps.append('ARCHITECTURE.md - Large project without architecture docs')
        if 'changelog' not in docs['by_type']:
            gaps.append('CHANGELOG.md - No changelog found')

        self.analysis['documentation']['gaps'] = gaps

    def _extract_code_metrics(self):
        """Extract code metrics relevant to documentation."""
        metrics = {
            'functions': 0,
            'classes': 0,
            'documented_functions': 0,
            'documented_classes': 0,
            'docstring_coverage': 0,
        }

        # Simple pattern-based extraction for Python
        func_pattern = re.compile(r'^\s*(?:async\s+)?def\s+(\w+)\s*\(', re.MULTILINE)
        class_pattern = re.compile(r'^\s*class\s+(\w+)\s*[:\(]', re.MULTILINE)
        docstring_pattern = re.compile(r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'')

        for path in self.repo_path.rglob('*.py'):
            if any(skip in path.parts for skip in SKIP_DIRS):
                continue
            try:
                content = path.read_text()

                # Count functions and classes
                functions = func_pattern.findall(content)
                classes = class_pattern.findall(content)
                docstrings = docstring_pattern.findall(content)

                metrics['functions'] += len(functions)
                metrics['classes'] += len(classes)

                # Rough estimate of documentation
                metrics['documented_functions'] += min(len(docstrings), len(functions))
            except Exception:
                pass

        # Calculate coverage
        total_items = metrics['functions'] + metrics['classes']
        documented_items = metrics['documented_functions'] + metrics['documented_classes']
        if total_items > 0:
            metrics['docstring_coverage'] = round(documented_items / total_items * 100, 1)

        self.analysis['code_metrics'] = metrics

    def _extract_api_surface(self):
        """Extract API surface (endpoints, functions, classes)."""
        api = {
            'endpoints': [],
            'public_functions': [],
            'public_classes': [],
        }

        # Look for route definitions
        route_patterns = [
            # Express/Fastify
            re.compile(r'(?:app|router)\.(get|post|put|patch|delete)\s*\(\s*[\'"]([^\'"]+)[\'"]'),
            # FastAPI/Flask
            re.compile(r'@(?:app|router)\.(get|post|put|patch|delete)\s*\(\s*[\'"]([^\'"]+)[\'"]'),
            # Django
            re.compile(r'path\s*\(\s*[\'"]([^\'"]+)[\'"]'),
        ]

        for path in self.repo_path.rglob('*'):
            if any(skip in path.parts for skip in SKIP_DIRS):
                continue
            if path.suffix.lower() not in ('.py', '.js', '.ts', '.go', '.java'):
                continue

            try:
                content = path.read_text()
                for pattern in route_patterns:
                    matches = pattern.findall(content)
                    for match in matches:
                        if isinstance(match, tuple):
                            method, endpoint = match[0].upper(), match[1]
                        else:
                            method, endpoint = 'GET', match
                        api['endpoints'].append({
                            'method': method,
                            'path': endpoint,
                            'file': str(path.relative_to(self.repo_path)),
                        })
            except Exception:
                pass

        # Deduplicate endpoints
        seen = set()
        unique_endpoints = []
        for ep in api['endpoints']:
            key = (ep['method'], ep['path'])
            if key not in seen:
                seen.add(key)
                unique_endpoints.append(ep)
        api['endpoints'] = unique_endpoints

        self.analysis['api_surface'] = api

    def _assess_quality(self):
        """Assess documentation quality using DQI scoring."""
        score = 0
        max_score = 100

        docs = self.analysis['documentation']['existing']

        # Structure score (40 points)
        structure_score = 0
        if docs.get('by_type', {}).get('readme'):
            structure_score += 15  # Has README
        if docs.get('by_type', {}).get('contributing'):
            structure_score += 10  # Has CONTRIBUTING
        if docs.get('by_type', {}).get('api_docs'):
            structure_score += 10  # Has API docs
        if docs.get('by_type', {}).get('architecture'):
            structure_score += 5   # Has architecture docs

        # Content score (30 points)
        content_score = 0
        total_words = docs.get('total_words', 0)
        if total_words > 5000:
            content_score += 15
        elif total_words > 1000:
            content_score += 10
        elif total_words > 500:
            content_score += 5

        # Check README quality
        readme_files = docs.get('by_type', {}).get('readme', [])
        if readme_files:
            readme_path = self.repo_path / readme_files[0]
            if readme_path.exists():
                readme_content = readme_path.read_text(errors='ignore')
                # Check for key sections
                if re.search(r'#.*install', readme_content, re.IGNORECASE):
                    content_score += 5
                if re.search(r'#.*usage|#.*getting started', readme_content, re.IGNORECASE):
                    content_score += 5
                if '```' in readme_content:  # Has code examples
                    content_score += 5

        # Style score (30 points)
        style_score = 0
        docstring_coverage = self.analysis['code_metrics'].get('docstring_coverage', 0)
        if docstring_coverage > 80:
            style_score += 15
        elif docstring_coverage > 50:
            style_score += 10
        elif docstring_coverage > 20:
            style_score += 5

        # Check for consistent formatting
        if len(docs.get('files', [])) > 0:
            style_score += 10  # Has documentation files
        if not self.analysis['documentation']['gaps']:
            style_score += 5  # No critical gaps

        total_score = structure_score + content_score + style_score

        self.analysis['documentation']['quality_score'] = total_score
        self.analysis['documentation']['quality_breakdown'] = {
            'structure': structure_score,
            'content': content_score,
            'style': style_score,
        }

        # Quality rating
        if total_score >= 90:
            self.analysis['documentation']['quality_rating'] = 'Excellent'
        elif total_score >= 70:
            self.analysis['documentation']['quality_rating'] = 'Good'
        elif total_score >= 50:
            self.analysis['documentation']['quality_rating'] = 'Acceptable'
        else:
            self.analysis['documentation']['quality_rating'] = 'Needs Improvement'

    def _generate_recommendations(self):
        """Generate documentation recommendations."""
        recommendations = []

        # Based on gaps
        for gap in self.analysis['documentation']['gaps']:
            recommendations.append({
                'priority': 'high',
                'type': 'missing_doc',
                'description': gap,
            })

        # Based on quality score
        quality = self.analysis['documentation']['quality_score']
        if quality < 50:
            recommendations.append({
                'priority': 'high',
                'type': 'quality',
                'description': 'Documentation quality is below acceptable threshold. Focus on README and getting started guide.',
            })

        # Based on code metrics
        coverage = self.analysis['code_metrics'].get('docstring_coverage', 0)
        if coverage < 30:
            recommendations.append({
                'priority': 'medium',
                'type': 'docstrings',
                'description': f'Docstring coverage is only {coverage}%. Add docstrings to public functions and classes.',
            })

        # Based on API surface
        endpoints = len(self.analysis['api_surface'].get('endpoints', []))
        if endpoints > 5 and 'api_docs' not in self.analysis['documentation']['existing'].get('by_type', {}):
            recommendations.append({
                'priority': 'high',
                'type': 'api_docs',
                'description': f'Found {endpoints} API endpoints but no API documentation. Generate API reference.',
            })

        # Based on repo size
        total_files = self.analysis['structure'].get('total_files', 0)
        if total_files > 100 and 'architecture' not in self.analysis['documentation']['existing'].get('by_type', {}):
            recommendations.append({
                'priority': 'medium',
                'type': 'architecture',
                'description': 'Large repository without architecture documentation. Add ARCHITECTURE.md.',
            })

        # Recommended documents to generate
        recommended_docs = ['README.md']
        if endpoints > 0:
            recommended_docs.append('API.md')
        if total_files > 50:
            recommended_docs.append('ARCHITECTURE.md')
        recommended_docs.append('CONTRIBUTING.md')

        self.analysis['recommendations'] = recommendations
        self.analysis['recommended_docs'] = recommended_docs


def main():
    parser = argparse.ArgumentParser(
        description='Analyze repository structure and documentation status'
    )
    parser.add_argument('repo_path', help='Path to repository')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    parser.add_argument('--pretty', '-p', action='store_true', help='Pretty print JSON')

    args = parser.parse_args()

    try:
        analyzer = RepositoryAnalyzer(args.repo_path)
        analysis = analyzer.analyze()

        # Output
        indent = 2 if args.pretty else None
        output = json.dumps(analysis, indent=indent, default=str)

        if args.output:
            Path(args.output).write_text(output)
            print(f"Analysis written to: {args.output}")
        else:
            print(output)

        # Print summary
        print("\n" + "="*60)
        print("ANALYSIS SUMMARY")
        print("="*60)
        print(f"Repository: {analysis['repo_name']}")
        print(f"Primary Language: {analysis.get('primary_language', 'Unknown')}")
        print(f"Frameworks: {', '.join(analysis['frameworks']) or 'None detected'}")
        print(f"Total Files: {analysis['structure']['total_files']}")
        print(f"Documentation Quality: {analysis['documentation']['quality_score']}/100 ({analysis['documentation']['quality_rating']})")
        print(f"Documentation Gaps: {len(analysis['documentation']['gaps'])}")
        print(f"Recommendations: {len(analysis['recommendations'])}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
