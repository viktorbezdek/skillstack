/**
 * Shareable semantic-release configuration
 *
 * This configuration follows 2024/2025 best practices:
 * - Conventional Commits for version determination
 * - Automated changelog generation
 * - GitHub releases with artifacts
 * - Git commit of generated files
 */

module.exports = {
  branches: [
    'main',
    {
      name: 'beta',
      prerelease: true
    }
  ],

  plugins: [
    // Analyze commits to determine version bump
    '@semantic-release/commit-analyzer',

    // Generate release notes from commits
    '@semantic-release/release-notes-generator',

    // Update CHANGELOG.md
    [
      '@semantic-release/changelog',
      {
        changelogFile: 'CHANGELOG.md'
      }
    ],

    // Run custom build/packaging scripts
    [
      '@semantic-release/exec',
      {
        prepareCmd: './scripts/build.sh',
        publishCmd: 'echo "Package ready for distribution"'
      }
    ],

    // Commit generated files back to repo
    [
      '@semantic-release/git',
      {
        assets: ['CHANGELOG.md', 'package.json'],
        message: 'chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}'
      }
    ],

    // Create GitHub release
    [
      '@semantic-release/github',
      {
        assets: [
          {
            path: 'build.zip',
            label: 'Distribution package'
          }
        ]
      }
    ]
  ]
};
