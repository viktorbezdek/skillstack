**Skill**: [semantic-release](../SKILL.md)

## Troubleshooting

### No Release Created

**Symptom**: GitHub Actions succeeds but no git tag or release created.

**Diagnosis**:

- Check commit messages follow Conventional Commits format
- Verify commits since last release contain `feat:` or `fix:` types
- Confirm branch name matches configuration (default: `main`)

**Solution**: Add qualifying commit (e.g., `feat: trigger release`) and push.

### Permission Denied Errors

**Symptom**: GitHub Actions fails with "Resource not accessible by integration" error.

**Diagnosis**: Missing GitHub Actions permissions.

**Solution**: Repository Settings → Actions → General → Workflow permissions → Enable "Read and write permissions".

### Node.js Version Mismatch

**Symptom**: Installation fails with "engine node is incompatible" error.

**Diagnosis**: Node.js version below 24.10.0.

**Solution**:

```bash
# Install Node.js 24 LTS (using mise)
mise install node@24
mise use node@24
```

Update `.github/workflows/release.yml`:

```yaml
- uses: actions/setup-node@v4
  with:
    node-version: "24"
```
