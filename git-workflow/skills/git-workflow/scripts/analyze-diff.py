#!/usr/bin/env python3
"""
Analyze staged git changes and suggest commit messages.

Usage:
    python analyze-diff.py                    # Analyze staged changes
    python analyze-diff.py --commit HEAD      # Analyze specific commit
    python analyze-diff.py --file path.py     # Analyze specific file
"""

import subprocess
import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from collections import defaultdict


class DiffAnalyzer:
    """Analyze git diffs to suggest commit messages."""
    
    # Map file patterns to scopes
    SCOPE_PATTERNS = {
        r'.*/(auth|login|oauth)': 'auth',
        r'.*/(api|endpoints|routes)': 'api',
        r'.*/database|migrations': 'database',
        r'.*/tests?/': 'test',
        r'.*/(ui|components|views)': 'ui',
        r'.*/docs?/': 'docs',
        r'.*/(config|settings)': 'config',
        r'.*\.github/': 'ci',
        r'Dockerfile|docker-compose': 'docker',
        r'.*/(deploy|infra|terraform)': 'ops',
    }
    
    # Keywords in diff that suggest commit types
    TYPE_KEYWORDS = {
        'feat': [
            'add', 'create', 'implement', 'introduce', 'new',
            'class', 'function', 'feature', 'endpoint', 'component'
        ],
        'fix': [
            'fix', 'bug', 'issue', 'error', 'crash', 'correct',
            'resolve', 'patch', 'repair'
        ],
        'refactor': [
            'refactor', 'restructure', 'reorganize', 'extract',
            'rename', 'move', 'cleanup', 'simplify'
        ],
        'perf': [
            'optimize', 'performance', 'faster', 'speed', 'cache',
            'index', 'query', 'efficient'
        ],
        'style': [
            'format', 'lint', 'prettier', 'whitespace', 'indent'
        ],
        'test': [
            'test', 'spec', 'coverage', 'mock', 'fixture'
        ],
        'docs': [
            'readme', 'documentation', 'comment', 'docstring'
        ],
        'build': [
            'package.json', 'requirements.txt', 'dependencies',
            'dependency', 'upgrade', 'bump'
        ],
    }
    
    def __init__(self):
        self.git_root = self._get_git_root()
    
    def _get_git_root(self) -> Optional[Path]:
        """Get git repository root."""
        try:
            result = subprocess.run(
                ['git', 'rev-parse', '--show-toplevel'],
                capture_output=True,
                text=True,
                check=True
            )
            return Path(result.stdout.strip())
        except subprocess.CalledProcessError:
            return None
    
    def _run_git(self, args: List[str]) -> str:
        """Run git command and return output."""
        try:
            result = subprocess.run(
                ['git'] + args,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            return ""
    
    def get_staged_changes(self) -> Dict[str, any]:
        """Get information about staged changes."""
        
        # Get list of changed files
        files_output = self._run_git(['diff', '--staged', '--name-status'])
        if not files_output:
            return None
        
        files = []
        for line in files_output.strip().split('\n'):
            if not line:
                continue
            parts = line.split('\t', 1)
            status = parts[0]
            filepath = parts[1] if len(parts) > 1 else ''
            files.append({
                'path': filepath,
                'status': status,  # A=added, M=modified, D=deleted
            })
        
        # Get the actual diff
        diff = self._run_git(['diff', '--staged'])
        
        # Get stats
        stats_output = self._run_git(['diff', '--staged', '--stat'])
        
        return {
            'files': files,
            'diff': diff,
            'stats': stats_output,
        }
    
    def infer_scope(self, files: List[Dict]) -> Optional[str]:
        """Infer scope from changed file paths."""
        
        scopes = []
        for file in files:
            path = file['path'].lower()
            for pattern, scope in self.SCOPE_PATTERNS.items():
                if re.search(pattern, path):
                    scopes.append(scope)
                    break
        
        if not scopes:
            # Try to extract from path
            for file in files:
                path = Path(file['path'])
                if len(path.parts) > 1:
                    # Use first directory as scope
                    potential_scope = path.parts[0]
                    if potential_scope not in ['src', 'lib', 'app']:
                        return potential_scope[:20]  # Truncate to 20 chars
        
        # Return most common scope
        if scopes:
            return max(set(scopes), key=scopes.count)
        
        return None
    
    def infer_type(self, files: List[Dict], diff: str) -> Tuple[str, float]:
        """
        Infer commit type from changes.
        Returns (type, confidence) where confidence is 0-1.
        """
        
        # Check file status first
        has_new_files = any(f['status'] == 'A' for f in files)
        has_deletions = any(f['status'] == 'D' for f in files)
        only_tests = all('test' in f['path'].lower() for f in files)
        only_docs = all(
            f['path'].lower().endswith(('.md', '.txt', '.rst')) 
            for f in files
        )
        
        if only_tests:
            return 'test', 0.9
        
        if only_docs:
            return 'docs', 0.9
        
        # Analyze diff content
        diff_lower = diff.lower()
        type_scores = defaultdict(int)
        
        for commit_type, keywords in self.TYPE_KEYWORDS.items():
            for keyword in keywords:
                # Count occurrences in added lines
                added_lines = [
                    line for line in diff.split('\n') 
                    if line.startswith('+') and not line.startswith('+++')
                ]
                
                for line in added_lines:
                    if keyword in line.lower():
                        type_scores[commit_type] += 1
        
        # Adjust scores based on file status
        if has_new_files:
            type_scores['feat'] += 5
        
        if has_deletions and not has_new_files:
            type_scores['refactor'] += 2
        
        # Get best guess
        if not type_scores:
            return 'chore', 0.3
        
        best_type = max(type_scores.items(), key=lambda x: x[1])
        confidence = min(best_type[1] / 10, 1.0)  # Normalize to 0-1
        
        return best_type[0], confidence
    
    def generate_description(self, 
                           files: List[Dict], 
                           diff: str,
                           commit_type: str) -> str:
        """Generate a description based on changes."""
        
        # Extract function/class names from diff
        added_patterns = [
            r'\+.*def (\w+)',  # Python functions
            r'\+.*function (\w+)',  # JS functions
            r'\+.*class (\w+)',  # Classes
            r'\+.*const (\w+)',  # Constants
        ]
        
        entities = []
        for pattern in added_patterns:
            matches = re.findall(pattern, diff)
            entities.extend(matches[:3])  # Limit to first 3
        
        # Generate description based on type
        if commit_type == 'feat' and entities:
            entity = entities[0]
            return f"add {entity}"
        
        elif commit_type == 'fix':
            # Look for bug-related keywords in diff
            if 'null' in diff.lower() and 'check' in diff.lower():
                return "prevent null pointer exception"
            elif 'error' in diff.lower():
                return "fix error handling"
            else:
                return "fix bug"
        
        elif commit_type == 'refactor':
            if entities:
                return f"extract {entities[0]} logic"
            return "restructure code"
        
        elif commit_type == 'perf':
            if 'cache' in diff.lower():
                return "add caching"
            elif 'index' in diff.lower():
                return "optimize database queries"
            return "improve performance"
        
        elif commit_type == 'docs':
            return "update documentation"
        
        elif commit_type == 'test':
            if entities:
                return f"add tests for {entities[0]}"
            return "add tests"
        
        # Default descriptions
        action = 'add' if any(f['status'] == 'A' for f in files) else 'update'
        if len(files) == 1:
            filename = Path(files[0]['path']).stem
            return f"{action} {filename}"
        else:
            return f"{action} {len(files)} files"
    
    def is_breaking_change(self, diff: str) -> Tuple[bool, Optional[str]]:
        """Detect if this might be a breaking change."""
        
        breaking_indicators = [
            (r'\-.*public ', 'removed public API'),
            (r'\-.*export ', 'removed exports'),
            (r'BREAKING CHANGE', 'explicitly marked'),
            (r'\-.*@deprecated', 'removed deprecated feature'),
        ]
        
        for pattern, reason in breaking_indicators:
            if re.search(pattern, diff, re.IGNORECASE):
                return True, reason
        
        return False, None
    
    def analyze(self) -> Optional[Dict]:
        """Analyze staged changes and return suggestions."""
        
        if not self.git_root:
            return {
                'error': 'Not in a git repository'
            }
        
        changes = self.get_staged_changes()
        if not changes:
            return {
                'error': 'No staged changes found. Use: git add <files>'
            }
        
        files = changes['files']
        diff = changes['diff']
        
        # Infer commit components
        scope = self.infer_scope(files)
        commit_type, confidence = self.infer_type(files, diff)
        description = self.generate_description(files, diff, commit_type)
        is_breaking, breaking_reason = self.is_breaking_change(diff)
        
        return {
            'type': commit_type,
            'scope': scope,
            'description': description,
            'confidence': confidence,
            'breaking': is_breaking,
            'breaking_reason': breaking_reason,
            'files_changed': len(files),
            'stats': changes['stats'],
        }


def main():
    """Main entry point."""
    import argparse
    import json
    
    parser = argparse.ArgumentParser(
        description='Analyze git changes and suggest commits'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON'
    )
    parser.add_argument(
        '--commit',
        action='store_true',
        help='Generate and execute git commit (interactive)'
    )
    
    args = parser.parse_args()
    
    analyzer = DiffAnalyzer()
    result = analyzer.analyze()
    
    if not result:
        print("No changes to analyze")
        sys.exit(1)
    
    if 'error' in result:
        print(f"Error: {result['error']}")
        sys.exit(1)
    
    if args.json:
        print(json.dumps(result, indent=2))
        sys.exit(0)
    
    # Pretty output
    print("📊 Analyzed your changes:\n")
    print(f"Files changed: {result['files_changed']}")
    print(result['stats'])
    print()
    
    # Build commit message
    commit_msg = result['type']
    if result['scope']:
        commit_msg += f"({result['scope']})"
    if result['breaking']:
        commit_msg += "!"
    commit_msg += f": {result['description']}"
    
    print("💡 Suggested commit:\n")
    print(f"  {commit_msg}")
    print()
    
    if result['confidence'] < 0.5:
        print("⚠️  Low confidence - please review and adjust")
        print()
    
    if result['breaking']:
        print(f"⚠️  Possible breaking change detected: {result['breaking_reason']}")
        print("   Consider adding BREAKING CHANGE: in commit body")
        print()
    
    if args.commit:
        response = input("Execute this commit? [y/N]: ")
        if response.lower() == 'y':
            subprocess.run(['git', 'commit', '-m', commit_msg])
            print("✓ Committed!")
        else:
            print("Copy and adjust as needed:")
            print(f"  git commit -m\"{commit_msg}\"")
    else:
        print("To commit:")
        print(f"  git commit -m\"{commit_msg}\"")
        print()
        print("To auto-commit next time:")
        print("  python analyze-diff.py --commit")


if __name__ == '__main__':
    main()
