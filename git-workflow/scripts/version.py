#!/usr/bin/env python3
"""
Calculate next semantic version from commits.

Usage:
    python version.py                  # Auto-detect current, suggest next
    python version.py --current 1.2.3  # Start from specific version
    python version.py --verbose        # Show detailed analysis
"""

import subprocess
import sys
import re
from typing import Optional, Tuple


class Version:
    """Semantic version."""
    def __init__(self, major: int, minor: int, patch: int):
        self.major = major
        self.minor = minor
        self.patch = patch
    
    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"
    
    @classmethod
    def parse(cls, version_str: str) -> 'Version':
        """Parse version string."""
        version_str = version_str.lstrip('v')
        parts = version_str.split('.')
        
        if len(parts) != 3:
            raise ValueError(f"Invalid version: {version_str}")
        
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))
    
    def bump_major(self) -> 'Version':
        """Bump major version."""
        return Version(self.major + 1, 0, 0)
    
    def bump_minor(self) -> 'Version':
        """Bump minor version."""
        return Version(self.major, self.minor + 1, 0)
    
    def bump_patch(self) -> 'Version':
        """Bump patch version."""
        return Version(self.major, self.minor, self.patch + 1)


class CommitAnalyzer:
    """Analyze commits for versioning."""
    
    def __init__(self):
        self.breaking_commits = []
        self.feature_commits = []
        self.fix_commits = []
        self.other_commits = []
    
    def analyze(self, from_ref: Optional[str] = None):
        """Analyze commits since ref."""
        commits = self._get_commits(from_ref)
        
        for commit in commits:
            self._classify_commit(commit)
    
    def _get_commits(self, from_ref: Optional[str]) -> list:
        """Get commit messages."""
        cmd = ['git', 'log', '--format=%s']
        
        if from_ref:
            cmd.insert(2, f'{from_ref}..HEAD')
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return [line.strip() for line in result.stdout.split('\n') if line.strip()]
        except subprocess.CalledProcessError:
            return []
    
    def _classify_commit(self, message: str):
        """Classify a commit message."""
        # Check for breaking change
        if '!' in message and ':' in message:
            if message.index('!') < message.index(':'):
                self.breaking_commits.append(message)
                return
        
        # Parse type
        pattern = r'^(?P<type>\w+)(?:\([^)]+\))?:\s*'
        match = re.match(pattern, message)
        
        if not match:
            self.other_commits.append(message)
            return
        
        commit_type = match.group('type')
        
        if commit_type == 'feat':
            self.feature_commits.append(message)
        elif commit_type == 'fix':
            self.fix_commits.append(message)
        else:
            self.other_commits.append(message)
    
    def get_bump_type(self) -> Tuple[str, str]:
        """
        Get version bump type and reason.
        
        Returns:
            (bump_type, reason) where bump_type is 'major', 'minor', or 'patch'
        """
        if self.breaking_commits:
            return 'major', f'{len(self.breaking_commits)} breaking change(s)'
        
        if self.feature_commits or self.fix_commits:
            feat_count = len(self.feature_commits)
            fix_count = len(self.fix_commits)
            parts = []
            if feat_count:
                parts.append(f'{feat_count} feature(s)')
            if fix_count:
                parts.append(f'{fix_count} fix(es)')
            return 'minor', ', '.join(parts)
        
        return 'patch', f'{len(self.other_commits)} other change(s)'
    
    def get_next_version(self, current: Version) -> Tuple[Version, str, str]:
        """
        Get next version.
        
        Returns:
            (next_version, bump_type, reason)
        """
        bump_type, reason = self.get_bump_type()
        
        if bump_type == 'major':
            next_version = current.bump_major()
        elif bump_type == 'minor':
            next_version = current.bump_minor()
        else:
            next_version = current.bump_patch()
        
        return next_version, bump_type, reason


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
    
    parser = argparse.ArgumentParser(description='Calculate next version')
    parser.add_argument('--current', help='Current version (default: latest tag)')
    parser.add_argument('--from', dest='from_ref', help='Analyze from this ref')
    parser.add_argument('--verbose', action='store_true', help='Show detailed analysis')
    
    args = parser.parse_args()
    
    # Get current version
    if args.current:
        current = Version.parse(args.current)
        from_ref = args.from_ref or f'v{current}'
    else:
        tag = get_latest_tag()
        if tag:
            current = Version.parse(tag)
            from_ref = args.from_ref or tag
        else:
            current = Version(0, 0, 0)
            from_ref = args.from_ref
    
    # Analyze commits
    analyzer = CommitAnalyzer()
    analyzer.analyze(from_ref)
    
    next_version, bump_type, reason = analyzer.get_next_version(current)
    
    if args.verbose:
        print(f"📊 Version Analysis\n")
        print(f"Current version: {current}")
        if from_ref:
            print(f"Analyzing since: {from_ref}")
        print()
        print("Commits found:")
        print(f"  • {len(analyzer.breaking_commits)} breaking change(s)")
        print(f"  • {len(analyzer.feature_commits)} feature(s)")
        print(f"  • {len(analyzer.fix_commits)} fix(es)")
        print(f"  • {len(analyzer.other_commits)} other change(s)")
        print()
        print(f"Bump type: {bump_type.upper()}")
        print(f"Reason: {reason}")
        print()
        print(f"Next version: {next_version}")
        
        if analyzer.breaking_commits:
            print()
            print("Breaking commits:")
            for commit in analyzer.breaking_commits[:5]:
                print(f"  • {commit}")
    else:
        print(next_version)


if __name__ == '__main__':
    main()
