# CI/CD Troubleshooting

Use this reference for pipeline failures, slow builds, missing permissions, and deployment-job issues. For changelog generation, semantic versioning, or release notes, switch to `git-workflow`.

## Fast Triage

| Symptom | Likely Cause | First Check |
|---|---|---|
| Workflow does not start | Branch/path filters, disabled workflow, missing trigger | Inspect `on:` block and repository Actions settings |
| Job cannot access repository contents | Missing `permissions` block or token scope | Set minimal `contents: read` or required write scope |
| Dependency install is slow | No dependency cache or cache key too broad | Add cache keyed by lockfile hash |
| Tests pass locally but fail in CI | Env/version mismatch, missing service, timezone/locale | Print runtime versions and required env vars |
| Deployment job fails after tests pass | Missing cloud credentials, OIDC trust, or environment approval | Check OIDC role trust policy and protected environment gates |
| Security scan is noisy | Unpinned baseline or wrong path scope | Configure ignore policy with owner and expiry |

## Debugging Order

1. Confirm the workflow trigger ran on the expected branch and path.
2. Read the first failing step, not the final summary.
3. Print tool versions before install/build/test steps.
4. Compare CI environment variables with local assumptions.
5. Check permissions and OIDC configuration before rotating secrets.
6. Re-run with debug logging only after narrowing the failing stage.

## Common Fixes

### Missing Permissions

GitHub Actions defaults can be read-only. Add the narrowest permission needed:

```yaml
permissions:
  contents: read
  id-token: write
```

Use `id-token: write` for OIDC-based cloud auth. Avoid long-lived cloud keys when OIDC is available.

### Flaky Or Slow Tests

- Split slow suites into parallel jobs.
- Cache package managers by lockfile hash.
- Upload screenshots, traces, and JUnit reports as artifacts.
- Quarantine only with an owner and expiration date.

### Deployment Failures

- Separate build/test from deploy jobs.
- Add environment approvals for production.
- Prefer canary, blue/green, or GitOps rollback paths.
- Record artifact digest and deployment target in job output.
