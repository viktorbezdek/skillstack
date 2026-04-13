# Slack GIF Creator Skill Example

This example demonstrates a skill for creating animated GIFs optimized for Slack communications.

## Skill Structure

- **SKILL.md** - Main skill file with instructions
- **LICENSE.txt** - MIT License

## Removed Resources (Described Below)

### core/ (7 Python modules)

Core library modules for GIF generation:

#### color_palettes.py
Color palette management and generation:
- Predefined color schemes (professional, playful, bold, etc.)
- Gradient generation
- Color harmony calculations
- Accessibility-compliant color combinations
- RGB/HEX conversion utilities

#### easing.py
Animation easing functions:
- Linear, ease-in, ease-out, ease-in-out
- Cubic, quadratic, quartic easing
- Bounce, elastic, back easing
- Custom easing curve support

#### frame_composer.py
Frame composition and layering:
- Layer management (text, shapes, images)
- Positioning and alignment
- Alpha compositing
- Transform operations (rotate, scale, skew)
- Clipping and masking

#### gif_builder.py
Main GIF construction engine:
- Frame collection and sequencing
- Duration and timing control
- Loop configuration
- Optimization and compression
- Export to file or bytes

#### typography.py
Text rendering and typography:
- Font loading and management
- Text positioning and alignment
- Multi-line text support
- Text effects (shadow, outline, glow)
- Dynamic sizing and kerning

#### validators.py
Input validation and error handling:
- Parameter validation
- File format checking
- Dimension constraints
- Color format validation
- Error messages and recovery

#### visual_effects.py
Visual effects and filters:
- Blur, sharpen, emboss
- Color adjustments (brightness, contrast, saturation)
- Transitions (fade, dissolve, wipe)
- Particle effects
- Glitch effects

### templates/ (13 animation templates)

Pre-built animation templates ready to customize:

#### bounce.py
Bouncing text or objects with physics simulation

#### explode.py
Explosion effect with particle dispersion

#### fade.py
Fade in/out transitions

#### flip.py
3D flip animation

#### kaleidoscope.py
Kaleidoscope pattern generation

#### morph.py
Shape morphing animations

#### move.py
Movement along paths

#### pulse.py
Pulsing scale animation

#### shake.py
Shake/vibrate effect

#### slide.py
Sliding in/out from edges

#### spin.py
Rotation animation

#### wiggle.py
Organic wiggle movement

#### zoom.py
Zoom in/out effect

### requirements.txt

Python dependencies:
```
Pillow>=10.0.0
imageio>=2.31.0
numpy>=1.24.0
```

## Use Cases

This skill helps with:
- Creating reaction GIFs for Slack
- Generating animated announcements
- Making celebration GIFs
- Creating branded animations
- Building custom emoji sequences

## Skill Patterns Demonstrated

- **Core library** - Reusable Python modules
- **Template system** - Pre-built animation patterns
- **Dependencies management** - requirements.txt for packages
- **Modular design** - Separate concerns (typography, effects, composition)
- **Extensible** - Easy to add new templates

## Restoration

To recreate the skill resources:
1. Implement core modules in `core/` directory
2. Create animation templates in `templates/` directory
3. Add `requirements.txt` with Pillow, imageio, numpy
4. Test with: `python -m templates.bounce "Hello Slack!"`
5. Document each template's parameters and usage

See SKILL.md for the complete skill implementation.

