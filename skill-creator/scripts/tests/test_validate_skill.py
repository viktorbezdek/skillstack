"""
Tests for SkillValidator in validate_skill.py

Each test class maps to one check method in SkillValidator.
All tests use tmp_path to create minimal, isolated skill directories.
"""

import sys
from pathlib import Path
import pytest

# Make the parent scripts/ directory importable
sys.path.insert(0, str(Path(__file__).parent.parent))

from validate_skill import SkillValidator, Severity, ValidationIssue


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_skill(tmp_path: Path, content: str) -> Path:
    """Create a minimal skill directory with a SKILL.md containing `content`."""
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")
    return skill_dir


MINIMAL_FRONTMATTER = """\
---
name: my-skill
description: Generates reports for CI pipelines. Use when building reports. Not for unrelated tasks.
---

## When to Use
Use for report generation.

## Not For
Not for general queries.

## Common Anti-Patterns
- avoid doing X wrong
"""

def issues_of(validator: SkillValidator, severity: Severity) -> list[ValidationIssue]:
    return [i for i in validator.issues if i.severity == severity]


# ---------------------------------------------------------------------------
# check_structure
# ---------------------------------------------------------------------------

class TestCheckStructure:
    def test_nonexistent_directory_adds_error(self, tmp_path):
        # Arrange
        missing = tmp_path / "ghost-skill"
        validator = SkillValidator(str(missing))

        # Act
        validator.check_structure()

        # Assert
        errors = issues_of(validator, Severity.ERROR)
        assert len(errors) == 1
        assert "not found" in errors[0].message

    def test_missing_skill_md_adds_error(self, tmp_path):
        # Arrange
        skill_dir = tmp_path / "bare-skill"
        skill_dir.mkdir()
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_structure()

        # Assert
        errors = issues_of(validator, Severity.ERROR)
        assert any("SKILL.md" in e.message for e in errors)

    def test_valid_directory_with_skill_md_no_errors(self, tmp_path):
        # Arrange
        skill_dir = make_skill(tmp_path, MINIMAL_FRONTMATTER)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_structure()

        # Assert
        errors = issues_of(validator, Severity.ERROR)
        assert errors == []

    def test_no_scripts_dir_adds_info(self, tmp_path):
        # Arrange
        skill_dir = make_skill(tmp_path, MINIMAL_FRONTMATTER)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_structure()

        # Assert
        info = issues_of(validator, Severity.INFO)
        assert any("scripts" in i.message.lower() for i in info)

    def test_no_references_dir_adds_info(self, tmp_path):
        # Arrange
        skill_dir = make_skill(tmp_path, MINIMAL_FRONTMATTER)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_structure()

        # Assert
        info = issues_of(validator, Severity.INFO)
        assert any("references" in i.message.lower() for i in info)

    def test_with_scripts_and_references_dirs_no_info(self, tmp_path):
        # Arrange
        skill_dir = make_skill(tmp_path, MINIMAL_FRONTMATTER)
        (skill_dir / "scripts").mkdir()
        (skill_dir / "references").mkdir()
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_structure()

        # Assert – no INFO issues about missing optional dirs
        info = issues_of(validator, Severity.INFO)
        dir_info = [i for i in info if "scripts" in i.message.lower() or "references" in i.message.lower()]
        assert dir_info == []


# ---------------------------------------------------------------------------
# check_skill_md
# ---------------------------------------------------------------------------

class TestCheckSkillMd:
    def test_missing_frontmatter_delimiter_adds_error(self, tmp_path):
        # Arrange
        skill_dir = make_skill(tmp_path, "# No frontmatter here\n\nSome body.")
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_skill_md()

        # Assert
        errors = issues_of(validator, Severity.ERROR)
        assert any("frontmatter" in e.message.lower() for e in errors)

    def test_invalid_yaml_frontmatter_adds_error(self, tmp_path):
        # Arrange – tab characters break YAML parsing
        bad_yaml = "---\nname: ok\n\tinvalid: tab-indented\n---\nBody"
        skill_dir = make_skill(tmp_path, bad_yaml)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_skill_md()

        # Assert
        errors = issues_of(validator, Severity.ERROR)
        assert any("invalid yaml" in e.message.lower() or "frontmatter" in e.message.lower() for e in errors)

    def test_missing_name_field_adds_error(self, tmp_path):
        # Arrange
        content = "---\ndescription: A skill without a name.\n---\nBody\n"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_skill_md()

        # Assert
        errors = issues_of(validator, Severity.ERROR)
        assert any("name" in e.message.lower() for e in errors)

    def test_missing_description_field_adds_error(self, tmp_path):
        # Arrange
        content = "---\nname: my-skill\n---\nBody\n"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_skill_md()

        # Assert
        errors = issues_of(validator, Severity.ERROR)
        assert any("description" in e.message.lower() for e in errors)

    def test_name_with_uppercase_adds_error(self, tmp_path):
        # Arrange
        content = "---\nname: MySkill\ndescription: A fine description.\n---\nBody\n"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_skill_md()

        # Assert
        errors = issues_of(validator, Severity.ERROR)
        assert any("invalid name format" in e.message.lower() for e in errors)

    def test_name_with_spaces_adds_error(self, tmp_path):
        # Arrange
        content = "---\nname: my skill\ndescription: A description.\n---\nBody\n"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_skill_md()

        # Assert
        errors = issues_of(validator, Severity.ERROR)
        assert any("invalid name format" in e.message.lower() for e in errors)

    def test_name_too_long_adds_error(self, tmp_path):
        # Arrange – 65-character name
        long_name = "a" * 65
        content = f"---\nname: {long_name}\ndescription: A description.\n---\nBody\n"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_skill_md()

        # Assert
        errors = issues_of(validator, Severity.ERROR)
        assert any("too long" in e.message.lower() for e in errors)

    def test_valid_name_with_hyphens_and_numbers_no_error(self, tmp_path):
        # Arrange
        content = "---\nname: my-skill-v2\ndescription: A description.\n---\nBody\n"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_skill_md()

        # Assert
        errors = issues_of(validator, Severity.ERROR)
        assert errors == []

    def test_file_over_500_lines_adds_warning(self, tmp_path):
        # Arrange – 501 lines of content after frontmatter
        body = "\n".join(["line"] * 501)
        content = f"---\nname: my-skill\ndescription: A description.\n---\n{body}"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_skill_md()

        # Assert
        warnings = issues_of(validator, Severity.WARNING)
        assert any("500" in w.message for w in warnings)


# ---------------------------------------------------------------------------
# check_description_quality
# ---------------------------------------------------------------------------

class TestCheckDescriptionQuality:
    def test_short_description_adds_warning(self, tmp_path):
        # Arrange – description under 20 chars
        content = "---\nname: my-skill\ndescription: Too short\n---\nBody\n"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_description_quality()

        # Assert
        warnings = issues_of(validator, Severity.WARNING)
        assert any("too short" in w.message.lower() for w in warnings)

    def test_description_over_1024_chars_adds_error(self, tmp_path):
        # Arrange
        long_desc = "x" * 1025
        content = f"---\nname: my-skill\ndescription: {long_desc}\n---\nBody\n"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_description_quality()

        # Assert
        errors = issues_of(validator, Severity.ERROR)
        assert any("too long" in e.message.lower() for e in errors)

    def test_description_lacking_what_adds_warning(self, tmp_path):
        # Arrange – no action verb
        content = (
            "---\nname: my-skill\n"
            "description: Something for use when needed and not for misuse.\n"
            "---\nBody\n"
        )
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_description_quality()

        # Assert
        warnings = issues_of(validator, Severity.WARNING)
        assert any("what" in w.message.lower() for w in warnings)

    def test_description_lacking_when_adds_warning(self, tmp_path):
        # Arrange – has action verb but no "when"/"use for"/"for" context word
        content = (
            "---\nname: my-skill\n"
            "description: Generates and creates and manages things extensively without timing context.\n"
            "---\nBody\n"
        )
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_description_quality()

        # Assert
        warnings = issues_of(validator, Severity.WARNING)
        assert any("when" in w.message.lower() for w in warnings)

    def test_first_person_description_adds_warning(self, tmp_path):
        # Arrange
        content = (
            "---\nname: my-skill\n"
            "description: I create reports when you need them. Not for personal use.\n"
            "---\nBody\n"
        )
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_description_quality()

        # Assert
        warnings = issues_of(validator, Severity.WARNING)
        assert any("third person" in w.message.lower() or "first/second" in w.message.lower() for w in warnings)

    def test_description_without_not_adds_info(self, tmp_path):
        # Arrange – good description but no negative qualifier
        content = (
            "---\nname: my-skill\n"
            "description: Generates detailed reports for CI pipelines. Use when building pipelines.\n"
            "---\nBody\n"
        )
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_description_quality()

        # Assert
        info = issues_of(validator, Severity.INFO)
        assert any("not" in i.message.lower() or "prevent" in i.message.lower() for i in info)

    def test_high_quality_description_no_issues(self, tmp_path):
        # Arrange – hits all the checks: action verb, "for", "not", third person, 20-1024 chars
        content = (
            "---\nname: my-skill\n"
            "description: >-\n"
            "  Generates structured reports for CI pipelines.\n"
            "  Use for pipeline diagnostics. Not for general dev tasks.\n"
            "---\nBody\n"
        )
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_description_quality()

        # Assert – no errors or warnings (INFO is acceptable)
        assert issues_of(validator, Severity.ERROR) == []
        assert issues_of(validator, Severity.WARNING) == []


# ---------------------------------------------------------------------------
# check_progressive_disclosure
# ---------------------------------------------------------------------------

class TestCheckProgressiveDisclosure:
    def test_long_file_without_references_adds_warning(self, tmp_path):
        # Arrange – >300 lines with no /references/ links
        # Each repetition contributes 3 lines; 110 * 3 = 330 lines
        body = "\n".join(["## Section\nsome content\n"] * 110)
        content = f"---\nname: my-skill\ndescription: desc\n---\n{body}"
        assert len(content.split("\n")) > 300, "precondition: must exceed 300 lines"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_progressive_disclosure()

        # Assert
        warnings = issues_of(validator, Severity.WARNING)
        assert any("references" in w.message.lower() or "splitting" in w.message.lower() for w in warnings)

    def test_long_file_with_references_link_no_warning(self, tmp_path):
        # Arrange – same long body but contains a /references/ link
        body = "\n".join(["## Section\n\nsome content"] * 50)
        content = f"---\nname: my-skill\ndescription: desc\n---\nSee /references/details.md for more.\n{body}"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_progressive_disclosure()

        # Assert – splitting warning should not appear
        warnings = issues_of(validator, Severity.WARNING)
        assert not any("splitting" in w.message.lower() for w in warnings)

    def test_medium_file_over_200_lines_without_see_ref_adds_info(self, tmp_path):
        # Arrange – 201 lines, no "See X for" pattern
        body = "\n".join(["content line"] * 201)
        content = f"---\nname: my-skill\ndescription: desc\n---\n{body}"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_progressive_disclosure()

        # Assert
        info = issues_of(validator, Severity.INFO)
        assert any("see" in i.message.lower() or "defer" in i.message.lower() for i in info)

    def test_medium_file_over_200_lines_with_see_ref_no_info(self, tmp_path):
        # Arrange – 201 lines with "See references/X for details"
        body = "\n".join(["content line"] * 201)
        content = f"---\nname: my-skill\ndescription: desc\n---\nSee /references/guide.md for configuration details.\n{body}"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_progressive_disclosure()

        # Assert
        info = issues_of(validator, Severity.INFO)
        assert not any("see" in i.message.lower() and "defer" in i.message.lower() for i in info)

    def test_short_file_no_progressive_disclosure_issues(self, tmp_path):
        # Arrange – brief skill under 200 lines
        skill_dir = make_skill(tmp_path, MINIMAL_FRONTMATTER)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_progressive_disclosure()

        # Assert
        assert validator.issues == []


# ---------------------------------------------------------------------------
# check_antipatterns_section
# ---------------------------------------------------------------------------

class TestCheckAntiPatternsSection:
    @pytest.mark.parametrize("term", [
        "anti-pattern",
        "antipattern",
        "common mistake",
        "avoid",
        "don't",
        "deprecated",
        "wrong",
    ])
    def test_recognized_antipattern_terms_suppress_info(self, tmp_path, term):
        # Arrange
        content = (
            f"---\nname: my-skill\ndescription: A skill.\n---\n"
            f"## Guidance\n\nPlease {term} using bad patterns.\n"
        )
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_antipatterns_section()

        # Assert – no info issue about missing anti-patterns
        info = issues_of(validator, Severity.INFO)
        assert not any("anti-pattern" in i.message.lower() for i in info)

    def test_content_without_antipattern_terms_adds_info(self, tmp_path):
        # Arrange – positive-only content
        content = (
            "---\nname: my-skill\ndescription: A skill.\n---\n"
            "## Usage\n\nHere is how to use this skill correctly.\n"
        )
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_antipatterns_section()

        # Assert
        info = issues_of(validator, Severity.INFO)
        assert any("anti-pattern" in i.message.lower() for i in info)


# ---------------------------------------------------------------------------
# check_usage_sections
# ---------------------------------------------------------------------------

class TestCheckUsageSections:
    @pytest.mark.parametrize("when_pattern", [
        "when to use",
        "use for:",
        "✅ use for",
    ])
    def test_recognized_when_to_use_patterns_suppress_warning(self, tmp_path, when_pattern):
        # Arrange
        content = (
            f"---\nname: my-skill\ndescription: A skill.\n---\n"
            f"## {when_pattern}\ndetails here\n\n## not for:\nthings\n"
        )
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_usage_sections()

        # Assert
        warnings = issues_of(validator, Severity.WARNING)
        assert not any("when to use" in w.message.lower() for w in warnings)

    @pytest.mark.parametrize("not_pattern", [
        "not for:",
        "when not to",
        "❌ not for",
    ])
    def test_recognized_when_not_to_use_patterns_suppress_warning(self, tmp_path, not_pattern):
        # Arrange
        content = (
            f"---\nname: my-skill\ndescription: A skill.\n---\n"
            f"## when to use\ndetails\n\n## {not_pattern}\nlimitations\n"
        )
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_usage_sections()

        # Assert
        warnings = issues_of(validator, Severity.WARNING)
        assert not any("when not" in w.message.lower() for w in warnings)

    def test_missing_both_sections_adds_two_warnings(self, tmp_path):
        # Arrange
        content = "---\nname: my-skill\ndescription: A skill.\n---\n## About\nJust content.\n"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_usage_sections()

        # Assert
        warnings = issues_of(validator, Severity.WARNING)
        assert len(warnings) == 2

    def test_missing_only_when_not_adds_one_warning(self, tmp_path):
        # Arrange
        content = "---\nname: my-skill\ndescription: A skill.\n---\n## when to use\ndetails\n"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_usage_sections()

        # Assert
        warnings = issues_of(validator, Severity.WARNING)
        assert len(warnings) == 1
        assert "not" in warnings[0].message.lower()


# ---------------------------------------------------------------------------
# check_allowed_tools
# ---------------------------------------------------------------------------

class TestCheckAllowedTools:
    def test_no_allowed_tools_field_adds_info(self, tmp_path):
        # Arrange
        content = "---\nname: my-skill\ndescription: A skill.\n---\nBody\n"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_allowed_tools()

        # Assert
        info = issues_of(validator, Severity.INFO)
        assert any("allowed-tools" in i.message.lower() or "permission" in i.message.lower() for i in info)

    def test_unrestricted_bash_adds_warning(self, tmp_path):
        # Arrange
        content = "---\nname: my-skill\ndescription: A skill.\nallowed-tools: Read, Bash, Write\n---\nBody\n"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_allowed_tools()

        # Assert
        warnings = issues_of(validator, Severity.WARNING)
        assert any("bash" in w.message.lower() for w in warnings)

    def test_scoped_bash_no_warning(self, tmp_path):
        # Arrange
        content = (
            "---\nname: my-skill\ndescription: A skill.\n"
            "allowed-tools: Read, Bash(git:*)\n---\nBody about bash usage.\n"
        )
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_allowed_tools()

        # Assert
        warnings = issues_of(validator, Severity.WARNING)
        assert not any("unrestricted bash" in w.message.lower() for w in warnings)

    def test_tool_not_mentioned_in_body_adds_info(self, tmp_path):
        # Arrange – WebFetch listed but never mentioned in body
        content = (
            "---\nname: my-skill\ndescription: A skill.\n"
            "allowed-tools: Read, WebFetch\n---\n"
            "## Usage\nUse the read tool to inspect files.\n"
        )
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_allowed_tools()

        # Assert
        info = issues_of(validator, Severity.INFO)
        assert any("webfetch" in i.message.lower() for i in info)

    def test_all_tools_mentioned_in_body_no_info(self, tmp_path):
        # Arrange – every tool appears in the body content
        content = (
            "---\nname: my-skill\ndescription: A skill.\n"
            "allowed-tools: Read, Write\n---\n"
            "## Usage\nUse read to inspect. Use write to save.\n"
        )
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        validator.check_allowed_tools()

        # Assert – no "not mentioned" INFO issues
        info = issues_of(validator, Severity.INFO)
        mention_issues = [i for i in info if "not mentioned" in i.message.lower()]
        assert mention_issues == []


# ---------------------------------------------------------------------------
# validate() integration — full pipeline
# ---------------------------------------------------------------------------

class TestValidateIntegration:
    def test_validate_runs_all_checks_and_returns_issues(self, tmp_path):
        # Arrange – deliberately incomplete skill
        content = "---\nname: my-skill\ndescription: A skill.\n---\nBody\n"
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        issues = validator.validate()

        # Assert – validate() returns the same list stored on the instance
        assert issues is validator.issues
        assert len(issues) > 0

    def test_validate_well_formed_skill_has_no_errors(self, tmp_path):
        # Arrange – a fully compliant skill
        content = """\
---
name: report-generator
description: >-
  Generates structured reports for CI pipelines. Use for pipeline diagnostics.
  Not for general dev tasks or unrelated requests.
allowed-tools: Read, Write
---

## When to Use
Use for generating CI pipeline reports.

## Not For
Not for general coding advice or non-pipeline tasks.

## Common Anti-Patterns
- avoid using this for non-pipeline tasks
- don't call this when you need code generation

## Usage
Use the read tool to inspect pipeline data.
Use the write tool to save the generated report.
"""
        skill_dir = make_skill(tmp_path, content)
        validator = SkillValidator(str(skill_dir))

        # Act
        issues = validator.validate()

        # Assert
        errors = [i for i in issues if i.severity == Severity.ERROR]
        assert errors == []

    def test_validate_empty_file_reports_error(self, tmp_path):
        # Arrange
        skill_dir = tmp_path / "empty-skill"
        skill_dir.mkdir()
        (skill_dir / "SKILL.md").write_text("", encoding="utf-8")
        validator = SkillValidator(str(skill_dir))

        # Act
        issues = validator.validate()

        # Assert
        errors = [i for i in issues if i.severity == Severity.ERROR]
        assert any("frontmatter" in e.message.lower() for e in errors)

    def test_check_structure_nonexistent_skill_records_error_and_returns(self, tmp_path):
        # Arrange – validate() cannot be called safely on a nonexistent path because
        # subsequent check_* methods would raise FileNotFoundError.
        # Test check_structure() in isolation instead.
        validator = SkillValidator(str(tmp_path / "does-not-exist"))

        # Act
        validator.check_structure()

        # Assert – exactly one error, no further issues appended
        errors = [i for i in validator.issues if i.severity == Severity.ERROR]
        assert len(errors) == 1
        assert "not found" in errors[0].message
