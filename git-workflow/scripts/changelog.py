#!/usr/bin/env python3
"""
Generate changelog from conventional commits.

Usage:
    python changelog.py                    # Since last tag
    python changelog.py --from v1.0.0      # Since specific version
    python changelog.py --version 2.0.0    # Add version header
"""

import subprocess
import sys
import re
from typing import List, Dict, Optional
from collections import defaultdict
from datetime import datetime


class Commit:
    """Parsed commit."""
    def __init__(self, hash: str, message: str):
        self.hash = hash
        self.message = message
        self.type = None
        self.scope = None
        self.breaking = False
        self.description = None
        
        self._parse()
    
    def _parse(self):
        """Parse conventional commit message."""
        header = self.message.split('\n')[0]
        
        # Match: type(scope)!: description
        pattern = r'^(?P<type>\w+)(?:\((?P<scope>[^)]+)\))?(?P<breaking>!)?:\s*(?P<desc>.+)$'
        match = re.match(pattern, header)
        
        if match:
            self.type = match.group('type')
            self.scope = match.group('scope')
            self.breaking = bool(match.group('breaking'))
            self.description = match.group('desc')
        
        # Check for BREAKING CHANGE in body
        if 'BREAKING CHANGE:' in self.message:
            self.breaking = True
    
    @property
    def is_valid(self):
        """Check if this is a valid conventional commit."""
        return self.type is not None


class ChangelogGenerator:
    """Generate formatted changelog."""
    
    TYPE_HEADERS = {
        'feat': '### ✨ Features',
        'fix': '### 🐛 Bug Fixes',
        'perf': '### ⚡ Performance',
        'refactor': '### ♻️  Refactoring',
        'docs': '### 📚 Documentation',
        'style': '### 💄 Styling',
        'test': '### ✅ Tests',
        'build': '### 📦 Build',
        'ops': '### 🔧 Operations',
        'chore': '### 🏗️  Chores',
    }
    
    TYPE_ORDER = [
        'feat', 'fix', 'perf', 'refactor',
        'docs', 'style', 'test', 'build', 'ops', 'chore'
    ]
    
    def __init__(self, include_hash: bool = False):
        self.include_hash = include_hash
    
    def get_commits(self, from_ref: Optional[str] = None) -> List[Commit]:
        """Get commits from git log."""
        cmd = ['git', 'log', '--format=%H%n%B%n---END---']
        
        if from_ref:
            cmd.insert(2, f'{from_ref}..HEAD')
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError:
            return []
        
        commits = []
        lines = result.stdout.split('\n')
        
        current_hash = None
        current_message = []
        
        for line in lines:
            if not current_hash:
                current_hash = line.strip()
            elif line == '---END---':
                if current_hash and current_message:
                    message = '\n'.join(current_message)
                    commits.append(Commit(current_hash, message))
                current_hash = None
                current_message = []
            else:
                current_message.append(line)
        
        return commits
    
    def group_commits(self, commits: List[Commit]) -> Dict[str, List[Commit]]:
        """Group commits by type."""
        breaking = []
        by_type = defaultdict(list)
        
        for commit in commits:
            if not commit.is_valid:
                continue
            
            if commit.breaking:
                breaking.append(commit)
            
            by_type[commit.type].append(commit)
        
        return {
            'breaking': breaking,
            'by_type': by_type
        }
    
    def format_commit(self, commit: Commit) -> str:
        """Format a single commit line."""
        parts = []
        
        if commit.scope:
            parts.append(f"**{commit.scope}**:")
        
        parts.append(commit.description)
        
        if self.include_hash:
            parts.append(f"([`{commit.hash[:7]}`])")
        
        return '- ' + ' '.join(parts)
    
    def generate(
        self,
        from_ref: Optional[str] = None,
        version: Optional[str] = None,
        date: Optional[str] = None
    ) -> str:
        """Generate complete changelog."""
        commits = self.get_commits(from_ref)
        
        if not commits:
            return "No commits found."
        
        grouped = self.group_commits(commits)
        lines = []
        
        # Version header
        if version:
            header = f"## [{version}]"
            if date:
                header += f" - {date}"
            lines.append(header)
            lines.append("")
        
        # Breaking changes first
        if grouped['breaking']:
            lines.append("### ⚠️  BREAKING CHANGES")
            lines.append("")
            for commit in grouped['breaking']:
                lines.append(self.format_commit(commit))
                # Add BREAKING CHANGE description if available
                for line in commit.message.split('\n'):
                    if line.startswith('BREAKING CHANGE:'):
                        detail = line.replace('BREAKING CHANGE:', '').strip()
                        if detail:
                            lines.append(f"  - {detail}")
            lines.append("")
        
        # Group by type
        for commit_type in self.TYPE_ORDER:
            if commit_type not in grouped['by_type']:
                continue
            
            type_commits = grouped['by_type'][commit_type]
            if not type_commits:
                continue
            
            lines.append(self.TYPE_HEADERS[commit_type])
            lines.append("")
            
            for commit in type_commits:
                lines.append(self.format_commit(commit))
            
            lines.append("")
        
        return '\n'.join(lines)


def get_latest_tag() -> Optional[str]:
    """Get latest git tag."""
    try:
        result = subprocess.run(
            ['git', 'describe', '--tags', '--abbrev=0'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate changelog')
    parser.add_argument('--from', dest='from_ref', help='Start from this ref')
    parser.add_argument('--version', help='Version for header')
    parser.add_argument('--date', help='Date for header (default: today)')
    parser.add_argument('--include-hash', action='store_true', help='Include commit hashes')
    parser.add_argument('--output', help='Output file (default: stdout)')
    
    args = parser.parse_args()
    
    # Get from ref
    from_ref = args.from_ref
    if not from_ref:
        from_ref = get_latest_tag()
        if from_ref:
            print(f"# Generating changelog since {from_ref}", file=sys.stderr)
    
    # Generate
    generator = ChangelogGenerator(include_hash=args.include_hash)
    
    date = args.date or datetime.now().strftime('%Y-%m-%d')
    changelog = generator.generate(from_ref, args.version, date)
    
    # Output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(changelog)
        print(f"Changelog written to {args.output}", file=sys.stderr)
    else:
        print(changelog)


if __name__ == '__main__':
    main()
