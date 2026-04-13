#!/usr/bin/env python3
"""
Skill Creator from Documentation

Main orchestrator that ties together all pipeline components to create
a complete Claude Code skill from documentation.

Usage:
    # From markdown file
    python scripts/create_skill.py SPECIFICATION.md --skill-name my-tool --output-dir output/

    # With configuration
    python scripts/create_skill.py docs.md --config config.yaml

    # Dry run
    python scripts/create_skill.py docs.md --skill-name tool --dry-run

    # Resume from specific phase
    python scripts/create_skill.py --resume output/ --from-phase 3
"""

import argparse
import json
import sys
import shutil
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional, Dict, Any, List

# Import all pipeline components
try:
    from doc_extractor import DocExtractor
    from doc_analyzer import DocAnalyzer
    from template_synthesizer import TemplateSynthesizer
    from guardrail_generator import GuardrailGenerator
    from asset_generator import AssetGenerator
    from skill_md_generator import SkillMDGenerator
except ImportError:
    # Handle running from different directory
    import os
    script_dir = Path(__file__).parent
    sys.path.insert(0, str(script_dir))
    from doc_extractor import DocExtractor
    from doc_analyzer import DocAnalyzer
    from template_synthesizer import TemplateSynthesizer
    from guardrail_generator import GuardrailGenerator
    from asset_generator import AssetGenerator
    from skill_md_generator import SkillMDGenerator


class Phase(Enum):
    """Pipeline phases."""
    EXTRACTION = 1
    ANALYSIS = 2
    TEMPLATES = 3
    GUARDRAILS = 4
    ASSETS = 5
    SKILL_MD = 6


@dataclass
class PipelineConfig:
    """Configuration for skill creation pipeline."""
    # Input
    doc_source: str
    skill_name: str
    output_dir: str

    # Options
    tool_type: str = "auto"
    verbose: bool = True
    dry_run: bool = False

    # Resume support
    resume: bool = False
    from_phase: int = 1

    # Phase control
    skip_phases: List[int] = field(default_factory=list)
    only_phases: List[int] = field(default_factory=list)

    # Paths (computed)
    extraction_dir: Optional[Path] = None
    analysis_file: Optional[Path] = None
    templates_dir: Optional[Path] = None
    guardrails_dir: Optional[Path] = None
    assets_dir: Optional[Path] = None
    skill_md_file: Optional[Path] = None
    state_file: Optional[Path] = None

    def __post_init__(self):
        """Compute output paths."""
        output = Path(self.output_dir)
        self.extraction_dir = output / "extraction"
        self.analysis_file = output / "analysis.json"
        self.templates_dir = output / "templates"
        self.guardrails_dir = output / "guardrails"
        self.assets_dir = output / "assets"
        self.skill_md_file = output / "SKILL.md"
        self.state_file = output / ".pipeline_state.json"


@dataclass
class PipelineState:
    """Track pipeline execution state."""
    config: Dict[str, Any]
    completed_phases: List[int] = field(default_factory=list)
    current_phase: Optional[int] = None
    phase_outputs: Dict[str, str] = field(default_factory=dict)
    errors: List[Dict[str, Any]] = field(default_factory=list)
    started_at: Optional[str] = None
    completed_at: Optional[str] = None

    def mark_phase_complete(self, phase: Phase, output_path: Optional[str] = None):
        """Mark a phase as complete."""
        if phase.value not in self.completed_phases:
            self.completed_phases.append(phase.value)

        if output_path:
            self.phase_outputs[phase.name] = output_path

    def is_phase_complete(self, phase: Phase) -> bool:
        """Check if phase is complete."""
        return phase.value in self.completed_phases

    def record_error(self, phase: Phase, error: str):
        """Record an error."""
        self.errors.append({
            'phase': phase.name,
            'phase_number': phase.value,
            'error': error,
            'timestamp': datetime.now().isoformat()
        })


class SkillCreator:
    """Main orchestrator for skill creation from documentation."""

    def __init__(self, config: PipelineConfig):
        self.config = config
        self.state: Optional[PipelineState] = None

        # Initialize components
        self.extractor = DocExtractor(verbose=config.verbose)
        self.analyzer = DocAnalyzer(verbose=config.verbose)
        self.synthesizer = TemplateSynthesizer(verbose=config.verbose)
        self.guardrail_gen = GuardrailGenerator(verbose=config.verbose)
        self.asset_gen = AssetGenerator(verbose=config.verbose)
        self.skill_md_gen = SkillMDGenerator(verbose=config.verbose)

    def log(self, message: str, level: str = "INFO"):
        """Log message if verbose."""
        if self.config.verbose:
            timestamp = datetime.now().strftime("%H:%M:%S")
            prefix = {
                "INFO": "ℹ️ ",
                "SUCCESS": "✅",
                "ERROR": "❌",
                "WARNING": "⚠️ ",
                "PHASE": "📍"
            }.get(level, "")
            print(f"[{timestamp}] {prefix} {message}", file=sys.stderr)

    def create_output_dir(self):
        """Create output directory structure."""
        output = Path(self.config.output_dir)

        if output.exists() and not self.config.resume:
            if self.config.dry_run:
                self.log(f"Would create output directory: {output}", "INFO")
                return

            # Ask user if they want to overwrite
            response = input(f"Output directory '{output}' already exists. Overwrite? [y/N]: ")
            if response.lower() != 'y':
                print("Aborted.")
                sys.exit(1)

            shutil.rmtree(output)

        if not self.config.dry_run:
            output.mkdir(parents=True, exist_ok=True)
            self.log(f"Created output directory: {output}", "SUCCESS")

    def load_state(self) -> Optional[PipelineState]:
        """Load pipeline state from file."""
        if not self.config.state_file.exists():
            return None

        try:
            with open(self.config.state_file, 'r') as f:
                data = json.load(f)

            state = PipelineState(**data)
            self.log(f"Loaded state: {len(state.completed_phases)} phases complete", "INFO")
            return state
        except Exception as e:
            self.log(f"Failed to load state: {e}", "WARNING")
            return None

    def save_state(self):
        """Save pipeline state to file."""
        if self.config.dry_run:
            return

        try:
            # Convert state to dict, handling Path objects
            state_dict = asdict(self.state)

            # Convert Path objects to strings in config
            if 'config' in state_dict:
                for key, value in state_dict['config'].items():
                    if isinstance(value, Path):
                        state_dict['config'][key] = str(value)

            with open(self.config.state_file, 'w') as f:
                json.dump(state_dict, f, indent=2, default=str)
        except Exception as e:
            self.log(f"Failed to save state: {e}", "WARNING")

    def should_run_phase(self, phase: Phase) -> bool:
        """Determine if phase should run."""
        # Check if already complete (for resume)
        if self.state and self.state.is_phase_complete(phase):
            return False

        # Check if before resume point
        if self.config.from_phase > phase.value:
            return False

        # Check skip list
        if phase.value in self.config.skip_phases:
            return False

        # Check only list
        if self.config.only_phases and phase.value not in self.config.only_phases:
            return False

        return True

    def run_phase_1_extraction(self) -> bool:
        """Phase 1: Extract documentation."""
        self.log("Phase 1: Extracting documentation...", "PHASE")

        if self.config.dry_run:
            self.log(f"Would extract from: {self.config.doc_source}", "INFO")
            self.log(f"Would save to: {self.config.extraction_dir}", "INFO")
            return True

        try:
            # Extract documentation
            corpus = self.extractor.extract_from_markdown(self.config.doc_source)

            # Save to output directory
            self.extractor.save_raw_docs(
                corpus,
                str(self.config.extraction_dir),
                format='json'  # Save as JSON for easier processing
            )

            self.log(f"Extracted {len(corpus.pages)} page(s)", "SUCCESS")
            self.state.mark_phase_complete(
                Phase.EXTRACTION,
                str(self.config.extraction_dir / "corpus.json")
            )
            return True

        except Exception as e:
            self.log(f"Extraction failed: {e}", "ERROR")
            self.state.record_error(Phase.EXTRACTION, str(e))
            return False

    def run_phase_2_analysis(self) -> bool:
        """Phase 2: Analyze documentation."""
        self.log("Phase 2: Analyzing documentation...", "PHASE")

        corpus_file = self.config.extraction_dir / "corpus.json"

        if self.config.dry_run:
            self.log(f"Would analyze: {corpus_file}", "INFO")
            self.log(f"Would save to: {self.config.analysis_file}", "INFO")
            return True

        try:
            # Load corpus
            with open(corpus_file, 'r') as f:
                corpus_data = json.load(f)

            # Convert to DocumentationCorpus (reconstruct from JSON)
            from doc_extractor import DocumentationCorpus, Page
            pages = [Page(**p) for p in corpus_data['pages']]
            corpus = DocumentationCorpus(
                source=corpus_data['source'],
                pages=pages,
                metadata=corpus_data['metadata']
            )

            # Analyze
            analysis = self.analyzer.analyze(corpus)

            # Save analysis (convert enum to string)
            analysis_dict = asdict(analysis)
            # Convert ToolType enum to string
            if 'tool_type' in analysis_dict:
                from doc_analyzer import ToolType
                if isinstance(analysis_dict['tool_type'], ToolType):
                    analysis_dict['tool_type'] = analysis_dict['tool_type'].value

            with open(self.config.analysis_file, 'w') as f:
                json.dump(analysis_dict, f, indent=2, default=str)

            self.log(f"Analysis complete: {analysis.tool_type.value} tool", "SUCCESS")
            self.log(f"  Workflows: {len(analysis.workflows)}", "INFO")
            self.log(f"  Examples: {len(analysis.examples)}", "INFO")
            self.log(f"  Pitfalls: {len(analysis.pitfalls)}", "INFO")

            self.state.mark_phase_complete(
                Phase.ANALYSIS,
                str(self.config.analysis_file)
            )
            return True

        except Exception as e:
            self.log(f"Analysis failed: {e}", "ERROR")
            self.state.record_error(Phase.ANALYSIS, str(e))
            return False

    def run_phase_3_templates(self) -> bool:
        """Phase 3: Synthesize templates."""
        self.log("Phase 3: Synthesizing templates...", "PHASE")

        if self.config.dry_run:
            self.log(f"Would generate templates to: {self.config.templates_dir}", "INFO")
            return True

        try:
            # Load analysis
            with open(self.config.analysis_file, 'r') as f:
                analysis = json.load(f)

            # Generate templates
            templates = self.synthesizer.synthesize_templates(
                analysis['examples'],
                analysis['patterns'],
                analysis['tool_type']
            )

            # Save templates to directory
            self.config.templates_dir.mkdir(parents=True, exist_ok=True)

            # Save each template
            for i, template in enumerate(templates):
                # Save template file
                ext = {
                    'bash': 'sh',
                    'python': 'py',
                    'javascript': 'js',
                    'typescript': 'ts',
                }.get(template.language, 'txt')

                template_file = self.config.templates_dir / f"{template.name}.{ext}"
                template_file.write_text(template.content)

                # Save usage file
                usage_file = self.config.templates_dir / f"{template.name}_USAGE.md"
                usage_file.write_text(template.usage_example)

            # Save metadata
            from template_synthesizer import TemplateType
            templates_data = []
            for t in templates:
                t_dict = asdict(t)
                # Convert TemplateType enum to string
                if isinstance(t_dict.get('type'), TemplateType):
                    t_dict['type'] = t_dict['type'].value
                templates_data.append(t_dict)

            metadata = {
                'templates': templates_data,
                'generated_at': datetime.now().isoformat()
            }
            metadata_file = self.config.templates_dir / "_templates_metadata.json"
            with open(metadata_file, 'w') as f:
                json.dump(metadata, f, indent=2, default=str)

            self.log(f"Generated {len(templates)} template(s)", "SUCCESS")
            self.state.mark_phase_complete(
                Phase.TEMPLATES,
                str(self.config.templates_dir)
            )
            return True

        except Exception as e:
            self.log(f"Template synthesis failed: {e}", "ERROR")
            self.state.record_error(Phase.TEMPLATES, str(e))
            return False

    def run_phase_4_guardrails(self) -> bool:
        """Phase 4: Generate guardrails."""
        self.log("Phase 4: Generating guardrails...", "PHASE")

        if self.config.dry_run:
            self.log(f"Would generate guardrails to: {self.config.guardrails_dir}", "INFO")
            return True

        try:
            # Load analysis
            with open(self.config.analysis_file, 'r') as f:
                analysis = json.load(f)

            # Load templates metadata (optional)
            templates_meta = None
            templates_meta_file = self.config.templates_dir / "_templates_metadata.json"
            if templates_meta_file.exists():
                with open(templates_meta_file, 'r') as f:
                    templates_meta = json.load(f)

            # Generate guardrails
            guardrails = self.guardrail_gen.generate_guardrails(analysis, templates_meta)

            # Save guardrails
            self.guardrail_gen.save_guardrails(guardrails, str(self.config.guardrails_dir))

            self.log(f"Generated 4-layer guardrail system", "SUCCESS")
            self.state.mark_phase_complete(
                Phase.GUARDRAILS,
                str(self.config.guardrails_dir)
            )
            return True

        except Exception as e:
            self.log(f"Guardrail generation failed: {e}", "ERROR")
            self.state.record_error(Phase.GUARDRAILS, str(e))
            return False

    def run_phase_5_assets(self) -> bool:
        """Phase 5: Generate support assets."""
        self.log("Phase 5: Generating support assets...", "PHASE")

        if self.config.dry_run:
            self.log(f"Would generate assets to: {self.config.assets_dir}", "INFO")
            return True

        try:
            # Load analysis
            with open(self.config.analysis_file, 'r') as f:
                analysis = json.load(f)

            # Load templates metadata (optional)
            templates_meta = None
            templates_meta_file = self.config.templates_dir / "_templates_metadata.json"
            if templates_meta_file.exists():
                with open(templates_meta_file, 'r') as f:
                    templates_meta = json.load(f)

            # Generate assets
            assets = self.asset_gen.generate_assets(analysis, templates_meta)

            # Save assets
            self.asset_gen.save_assets(assets, str(self.config.assets_dir))

            self.log(f"Generated 4 support assets", "SUCCESS")
            self.state.mark_phase_complete(
                Phase.ASSETS,
                str(self.config.assets_dir)
            )
            return True

        except Exception as e:
            self.log(f"Asset generation failed: {e}", "ERROR")
            self.state.record_error(Phase.ASSETS, str(e))
            return False

    def run_phase_6_skill_md(self) -> bool:
        """Phase 6: Generate SKILL.md."""
        self.log("Phase 6: Generating SKILL.md...", "PHASE")

        if self.config.dry_run:
            self.log(f"Would generate SKILL.md to: {self.config.skill_md_file}", "INFO")
            return True

        try:
            # Load analysis
            with open(self.config.analysis_file, 'r') as f:
                analysis = json.load(f)

            # Load metadata (optional)
            templates_meta = None
            templates_meta_file = self.config.templates_dir / "_templates_metadata.json"
            if templates_meta_file.exists():
                with open(templates_meta_file, 'r') as f:
                    templates_meta = json.load(f)

            guardrails_meta = None
            guardrails_meta_file = self.config.guardrails_dir / "guardrails_metadata.json"
            if guardrails_meta_file.exists():
                with open(guardrails_meta_file, 'r') as f:
                    guardrails_meta = json.load(f)

            assets_meta = None
            assets_meta_file = self.config.assets_dir / "assets_metadata.json"
            if assets_meta_file.exists():
                with open(assets_meta_file, 'r') as f:
                    assets_meta = json.load(f)

            # Generate SKILL.md
            skill = self.skill_md_gen.generate_skill_md(
                analysis,
                templates_meta,
                guardrails_meta,
                assets_meta
            )

            # Save SKILL.md
            line_count = self.skill_md_gen.save_skill_md(
                skill,
                str(self.config.skill_md_file)
            )

            self.log(f"Generated SKILL.md ({line_count} lines)", "SUCCESS")
            self.state.mark_phase_complete(
                Phase.SKILL_MD,
                str(self.config.skill_md_file)
            )
            return True

        except Exception as e:
            self.log(f"SKILL.md generation failed: {e}", "ERROR")
            self.state.record_error(Phase.SKILL_MD, str(e))
            return False

    def run(self) -> bool:
        """Run the complete pipeline."""
        # Initialize state
        if self.config.resume:
            self.state = self.load_state()
            if not self.state:
                self.log("Resume requested but no state found, starting fresh", "WARNING")
                self.state = PipelineState(
                    config=asdict(self.config),
                    started_at=datetime.now().isoformat()
                )
        else:
            self.state = PipelineState(
                config=asdict(self.config),
                started_at=datetime.now().isoformat()
            )

        # Create output directory
        self.create_output_dir()

        # Run phases
        phases = [
            (Phase.EXTRACTION, self.run_phase_1_extraction),
            (Phase.ANALYSIS, self.run_phase_2_analysis),
            (Phase.TEMPLATES, self.run_phase_3_templates),
            (Phase.GUARDRAILS, self.run_phase_4_guardrails),
            (Phase.ASSETS, self.run_phase_5_assets),
            (Phase.SKILL_MD, self.run_phase_6_skill_md),
        ]

        for phase, runner in phases:
            if not self.should_run_phase(phase):
                self.log(f"Skipping Phase {phase.value}: {phase.name}", "INFO")
                continue

            self.state.current_phase = phase.value
            self.save_state()

            success = runner()

            if not success:
                self.log(f"Pipeline failed at Phase {phase.value}", "ERROR")
                self.state.current_phase = None
                self.save_state()
                return False

            self.save_state()

        # Mark complete
        self.state.current_phase = None
        self.state.completed_at = datetime.now().isoformat()
        self.save_state()

        return True

    def print_summary(self):
        """Print execution summary."""
        if not self.state:
            return

        print("\n" + "="*60)
        print("Skill Creation Summary")
        print("="*60)
        print(f"Skill Name: {self.config.skill_name}")
        print(f"Output Directory: {self.config.output_dir}")
        print(f"Started: {self.state.started_at}")
        if self.state.completed_at:
            print(f"Completed: {self.state.completed_at}")
        print(f"\nCompleted Phases: {len(self.state.completed_phases)}/6")

        for phase in Phase:
            status = "✅" if self.state.is_phase_complete(phase) else "⏭️ "
            print(f"  {status} Phase {phase.value}: {phase.name}")

        if self.state.errors:
            print(f"\nErrors: {len(self.state.errors)}")
            for error in self.state.errors:
                print(f"  ❌ Phase {error['phase_number']}: {error['error']}")

        if self.state.completed_at:
            print("\n✅ Skill creation complete!")
            print(f"\nNext Steps:")
            print(f"  1. Review SKILL.md: {self.config.skill_md_file}")
            print(f"  2. Test templates: {self.config.templates_dir}")
            print(f"  3. Run validation: {self.config.guardrails_dir}/scripts/validate_prereqs.sh")

        print("="*60 + "\n")


def load_config_file(config_path: str) -> Dict[str, Any]:
    """Load configuration from YAML or JSON file."""
    path = Path(config_path)

    if not path.exists():
        print(f"Config file not found: {config_path}", file=sys.stderr)
        sys.exit(1)

    if path.suffix in ['.yaml', '.yml']:
        try:
            import yaml
            with open(path, 'r') as f:
                return yaml.safe_load(f)
        except ImportError:
            print("PyYAML not installed. Install with: pip install pyyaml", file=sys.stderr)
            sys.exit(1)
    elif path.suffix == '.json':
        with open(path, 'r') as f:
            return json.load(f)
    else:
        print(f"Unsupported config format: {path.suffix}", file=sys.stderr)
        sys.exit(1)


def main():
    """CLI interface for skill creation."""
    parser = argparse.ArgumentParser(
        description="Create Claude Code skill from documentation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  %(prog)s docs.md --skill-name my-tool --output-dir output/

  # With configuration file
  %(prog)s --config config.yaml

  # Dry run to see what would happen
  %(prog)s docs.md --skill-name tool --dry-run

  # Resume from phase 3
  %(prog)s --resume output/ --from-phase 3

  # Run only specific phases
  %(prog)s docs.md --skill-name tool --only-phases 1,2,3
        """
    )

    # Input
    parser.add_argument(
        'doc_source',
        nargs='?',
        help='Documentation source (markdown file or URL)'
    )
    parser.add_argument(
        '--skill-name',
        help='Name for the skill'
    )
    parser.add_argument(
        '--output-dir',
        help='Output directory for generated skill'
    )

    # Configuration
    parser.add_argument(
        '--config',
        help='Configuration file (YAML or JSON)'
    )

    # Options
    parser.add_argument(
        '--tool-type',
        choices=['cli', 'api', 'library', 'framework', 'auto'],
        default='auto',
        help='Tool type (default: auto-detect)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        default=True,
        help='Verbose output (default: True)'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress output'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would happen without executing'
    )

    # Resume
    parser.add_argument(
        '--resume',
        action='store_true',
        help='Resume from saved state'
    )
    parser.add_argument(
        '--from-phase',
        type=int,
        choices=[1, 2, 3, 4, 5, 6],
        default=1,
        help='Start from specific phase (for resume)'
    )

    # Phase control
    parser.add_argument(
        '--skip-phases',
        help='Comma-separated phase numbers to skip'
    )
    parser.add_argument(
        '--only-phases',
        help='Comma-separated phase numbers to run (skip others)'
    )

    args = parser.parse_args()

    # Load config from file if provided
    config_dict = {}
    if args.config:
        config_dict = load_config_file(args.config)

    # Override with command-line arguments
    if args.doc_source:
        config_dict['doc_source'] = args.doc_source
    if args.skill_name:
        config_dict['skill_name'] = args.skill_name
    if args.output_dir:
        config_dict['output_dir'] = args.output_dir

    # Validate required fields
    if not config_dict.get('doc_source'):
        parser.error("doc_source is required (provide as argument or in config file)")
    if not config_dict.get('skill_name'):
        parser.error("--skill-name is required (provide as argument or in config file)")
    if not config_dict.get('output_dir'):
        # Default output dir to skill name
        config_dict['output_dir'] = config_dict['skill_name']

    # Apply options
    config_dict['tool_type'] = args.tool_type
    config_dict['verbose'] = args.verbose and not args.quiet
    config_dict['dry_run'] = args.dry_run
    config_dict['resume'] = args.resume
    config_dict['from_phase'] = args.from_phase

    # Parse phase control
    if args.skip_phases:
        config_dict['skip_phases'] = [int(p) for p in args.skip_phases.split(',')]
    if args.only_phases:
        config_dict['only_phases'] = [int(p) for p in args.only_phases.split(',')]

    # Create config object
    try:
        config = PipelineConfig(**config_dict)
    except TypeError as e:
        print(f"Invalid configuration: {e}", file=sys.stderr)
        sys.exit(1)

    # Create and run
    creator = SkillCreator(config)

    try:
        success = creator.run()
        creator.print_summary()

        sys.exit(0 if success else 1)

    except KeyboardInterrupt:
        print("\n\nInterrupted by user", file=sys.stderr)
        creator.save_state()
        print("State saved. Resume with: --resume --from-phase", creator.state.current_phase or 1)
        sys.exit(130)
    except Exception as e:
        print(f"\n\nUnexpected error: {e}", file=sys.stderr)
        if config.verbose:
            import traceback
            traceback.print_exc()
        creator.save_state()
        sys.exit(1)


if __name__ == '__main__':
    main()
