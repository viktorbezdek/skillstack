#!/usr/bin/env python3
"""
CI/CD Pipeline Health Checker

Checks pipeline status, recent failures, and provides insights for GitHub Actions,
GitLab CI, and other platforms. Identifies failing workflows, slow pipelines,
and provides actionable recommendations.

Usage:
    # GitHub Actions
    python3 ci_health.py --platform github --repo owner/repo

    # GitLab CI
    python3 ci_health.py --platform gitlab --project-id 12345 --token <token>

    # Check specific workflow/pipeline
    python3 ci_health.py --platform github --repo owner/repo --workflow ci.yml
"""

import argparse
import json
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class CIHealthChecker:
    def __init__(self, platform: str, **kwargs):
        self.platform = platform.lower()
        self.config = kwargs
        self.issues = []
        self.warnings = []
        self.insights = []
        self.metrics = {}

    def check_github_workflows(self) -> Dict:
        """Check GitHub Actions workflow health"""
        print(f"🔍 Checking GitHub Actions workflows...")

        if not self._check_command("gh"):
            self.issues.append("GitHub CLI (gh) is not installed")
            self.insights.append("Install gh CLI: https://cli.github.com/")
            return self._generate_report()

        repo = self.config.get('repo')
        if not repo:
            self.issues.append("Repository not specified")
            self.insights.append("Use --repo owner/repo")
            return self._generate_report()

        try:
            # Get recent workflow runs
            limit = self.config.get('limit', 20)
            cmd = ['gh', 'run', 'list', '--repo', repo, '--limit', str(limit), '--json',
                   'status,conclusion,name,workflowName,createdAt,displayTitle']

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

            if result.returncode != 0:
                self.issues.append(f"Failed to fetch workflows: {result.stderr}")
                self.insights.append("Verify gh CLI authentication: gh auth status")
                return self._generate_report()

            runs = json.loads(result.stdout)

            if not runs:
                self.warnings.append("No recent workflow runs found")
                return self._generate_report()

            # Analyze runs
            total_runs = len(runs)
            failed_runs = [r for r in runs if r.get('conclusion') == 'failure']
            cancelled_runs = [r for r in runs if r.get('conclusion') == 'cancelled']
            success_runs = [r for r in runs if r.get('conclusion') == 'success']

            self.metrics['total_runs'] = total_runs
            self.metrics['failed_runs'] = len(failed_runs)
            self.metrics['cancelled_runs'] = len(cancelled_runs)
            self.metrics['success_runs'] = len(success_runs)
            self.metrics['failure_rate'] = (len(failed_runs) / total_runs * 100) if total_runs > 0 else 0

            # Group failures by workflow
            failure_by_workflow = {}
            for run in failed_runs:
                workflow = run.get('workflowName', 'unknown')
                failure_by_workflow[workflow] = failure_by_workflow.get(workflow, 0) + 1

            print(f"✅ Analyzed {total_runs} recent runs:")
            print(f"   - Success: {len(success_runs)} ({len(success_runs)/total_runs*100:.1f}%)")
            print(f"   - Failed: {len(failed_runs)} ({len(failed_runs)/total_runs*100:.1f}%)")
            print(f"   - Cancelled: {len(cancelled_runs)} ({len(cancelled_runs)/total_runs*100:.1f}%)")

            # Identify issues
            if self.metrics['failure_rate'] > 20:
                self.issues.append(f"High failure rate: {self.metrics['failure_rate']:.1f}%")
                self.insights.append("Investigate failing workflows and address root causes")

            if failure_by_workflow:
                self.warnings.append("Workflows with recent failures:")
                for workflow, count in sorted(failure_by_workflow.items(), key=lambda x: x[1], reverse=True):
                    self.warnings.append(f"  - {workflow}: {count} failure(s)")
                    self.insights.append(f"Review logs for '{workflow}': gh run view --repo {repo}")

            if len(cancelled_runs) > total_runs * 0.3:
                self.warnings.append(f"High cancellation rate: {len(cancelled_runs)/total_runs*100:.1f}%")
                self.insights.append("Excessive cancellations may indicate workflow timeout issues or manual interventions")

        except subprocess.TimeoutExpired:
            self.issues.append("Request timed out - check network connectivity")
        except json.JSONDecodeError as e:
            self.issues.append(f"Failed to parse workflow data: {e}")
        except Exception as e:
            self.issues.append(f"Unexpected error: {e}")

        return self._generate_report()

    def check_gitlab_pipelines(self) -> Dict:
        """Check GitLab CI pipeline health"""
        print(f"🔍 Checking GitLab CI pipelines...")

        url = self.config.get('url', 'https://gitlab.com')
        token = self.config.get('token')
        project_id = self.config.get('project_id')

        if not token:
            self.issues.append("GitLab token not provided")
            self.insights.append("Provide token with --token or GITLAB_TOKEN env var")
            return self._generate_report()

        if not project_id:
            self.issues.append("Project ID not specified")
            self.insights.append("Use --project-id <id>")
            return self._generate_report()

        try:
            # Get recent pipelines
            per_page = self.config.get('limit', 20)
            api_url = f"{url}/api/v4/projects/{project_id}/pipelines?per_page={per_page}"
            req = urllib.request.Request(api_url, headers={'PRIVATE-TOKEN': token})

            with urllib.request.urlopen(req, timeout=30) as response:
                pipelines = json.loads(response.read())

            if not pipelines:
                self.warnings.append("No recent pipelines found")
                return self._generate_report()

            # Analyze pipelines
            total_pipelines = len(pipelines)
            failed = [p for p in pipelines if p.get('status') == 'failed']
            success = [p for p in pipelines if p.get('status') == 'success']
            running = [p for p in pipelines if p.get('status') == 'running']
            cancelled = [p for p in pipelines if p.get('status') == 'canceled']

            self.metrics['total_pipelines'] = total_pipelines
            self.metrics['failed'] = len(failed)
            self.metrics['success'] = len(success)
            self.metrics['running'] = len(running)
            self.metrics['failure_rate'] = (len(failed) / total_pipelines * 100) if total_pipelines > 0 else 0

            print(f"✅ Analyzed {total_pipelines} recent pipelines:")
            print(f"   - Success: {len(success)} ({len(success)/total_pipelines*100:.1f}%)")
            print(f"   - Failed: {len(failed)} ({len(failed)/total_pipelines*100:.1f}%)")
            print(f"   - Running: {len(running)}")
            print(f"   - Cancelled: {len(cancelled)}")

            # Identify issues
            if self.metrics['failure_rate'] > 20:
                self.issues.append(f"High failure rate: {self.metrics['failure_rate']:.1f}%")
                self.insights.append("Review failing pipelines and fix recurring issues")

            # Get details of recent failures
            if failed:
                self.warnings.append(f"Recent pipeline failures:")
                for pipeline in failed[:5]:  # Show up to 5 recent failures
                    ref = pipeline.get('ref', 'unknown')
                    pipeline_id = pipeline.get('id')
                    self.warnings.append(f"  - Pipeline #{pipeline_id} on {ref}")
                self.insights.append(f"View pipeline details: {url}/{project_id}/-/pipelines")

        except urllib.error.HTTPError as e:
            self.issues.append(f"API error: {e.code} - {e.reason}")
            if e.code == 401:
                self.insights.append("Check GitLab token permissions")
        except urllib.error.URLError as e:
            self.issues.append(f"Network error: {e.reason}")
            self.insights.append("Check GitLab URL and network connectivity")
        except Exception as e:
            self.issues.append(f"Unexpected error: {e}")

        return self._generate_report()

    def _check_command(self, command: str) -> bool:
        """Check if command is available"""
        try:
            subprocess.run([command, '--version'], capture_output=True, timeout=5)
            return True
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False

    def _generate_report(self) -> Dict:
        """Generate health check report"""
        # Determine overall health status
        if self.issues:
            status = 'unhealthy'
        elif self.warnings:
            status = 'degraded'
        else:
            status = 'healthy'

        return {
            'platform': self.platform,
            'status': status,
            'issues': self.issues,
            'warnings': self.warnings,
            'insights': self.insights,
            'metrics': self.metrics
        }

def print_report(report: Dict):
    """Print formatted health check report"""
    print("\n" + "="*60)
    print(f"🏥 CI/CD Health Report - {report['platform'].upper()}")
    print("="*60)

    status_emoji = {"healthy": "✅", "degraded": "⚠️", "unhealthy": "❌"}.get(report['status'], "❓")
    print(f"\nStatus: {status_emoji} {report['status'].upper()}")

    if report['metrics']:
        print(f"\n📊 Metrics:")
        for key, value in report['metrics'].items():
            formatted_key = key.replace('_', ' ').title()
            if 'rate' in key:
                print(f"   - {formatted_key}: {value:.1f}%")
            else:
                print(f"   - {formatted_key}: {value}")

    if report['issues']:
        print(f"\n🚨 Issues ({len(report['issues'])}):")
        for i, issue in enumerate(report['issues'], 1):
            print(f"  {i}. {issue}")

    if report['warnings']:
        print(f"\n⚠️  Warnings:")
        for warning in report['warnings']:
            if warning.startswith('  -'):
                print(f"  {warning}")
            else:
                print(f"  • {warning}")

    if report['insights']:
        print(f"\n💡 Insights & Recommendations:")
        for i, insight in enumerate(report['insights'], 1):
            print(f"  {i}. {insight}")

    print("\n" + "="*60 + "\n")

def main():
    parser = argparse.ArgumentParser(
        description='CI/CD Pipeline Health Checker',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--platform', required=True, choices=['github', 'gitlab'],
                       help='CI/CD platform')
    parser.add_argument('--repo', help='GitHub repository (owner/repo)')
    parser.add_argument('--workflow', help='Specific workflow name to check')
    parser.add_argument('--project-id', help='GitLab project ID')
    parser.add_argument('--url', default='https://gitlab.com', help='GitLab URL')
    parser.add_argument('--token', help='GitLab token (or use GITLAB_TOKEN env var)')
    parser.add_argument('--limit', type=int, default=20, help='Number of recent runs/pipelines to analyze')

    args = parser.parse_args()

    # Create checker
    checker = CIHealthChecker(
        platform=args.platform,
        repo=args.repo,
        workflow=args.workflow,
        project_id=args.project_id,
        url=args.url,
        token=args.token,
        limit=args.limit
    )

    # Run checks
    if args.platform == 'github':
        report = checker.check_github_workflows()
    elif args.platform == 'gitlab':
        report = checker.check_gitlab_pipelines()

    # Print report
    print_report(report)

    # Exit with error code if unhealthy
    sys.exit(0 if report['status'] == 'healthy' else 1)

if __name__ == '__main__':
    main()
