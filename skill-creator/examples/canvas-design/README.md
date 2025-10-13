# Canvas Design Skill Example

This example demonstrates a skill for creating rich canvas designs with custom typography using HTML5 Canvas.

## Skill Structure

- **SKILL.md** - Main skill file with instructions  
- **LICENSE.txt** - MIT License

## Removed Resources (Described Below)

### canvas-fonts/ (81 font files)

This skill originally included a comprehensive font library with 27 font families (Regular, Bold, Italic variants). Each font included:
- **.ttf files** - TrueType font files ready for Canvas use
- **-OFL.txt files** - Open Font License files for each font family

#### Font Families Included:

**Serif Fonts:**
- Arsenal SC (Regular)
- Crimson Pro (Regular, Bold, Italic)
- Erica One (Regular)
- Gloock (Regular)
- IBM Plex Serif (Regular, Bold, Italic, Bold Italic)
- Instrument Serif (Regular, Italic)
- Italiana (Regular)
- Libre Baskerville (Regular)
- Lora (Regular, Bold, Italic, Bold Italic)
- Young Serif (Regular)

**Sans-Serif Fonts:**
- Big Shoulders (Regular, Bold)
- Bricolage Grotesque (Regular, Bold)
- Instrument Sans (Regular, Bold, Italic, Bold Italic)
- Jura (Light, Medium)
- National Park (Regular, Bold)
- Outfit (Regular, Bold)
- Work Sans (Regular, Bold, Italic, Bold Italic)

**Display Fonts:**
- Boldonse (Regular)
- Nothing You Could Do (Regular)
- Pixelify Sans (Medium)
- Poiret One (Regular)
- Silkscreen (Regular)
- Smooch Sans (Medium)
- Tektur (Regular, Medium)

**Monospace Fonts:**
- DM Mono (Regular)
- Geist Mono (Regular, Bold)
- IBM Plex Mono (Regular, Bold)
- JetBrains Mono (Regular, Bold)
- Red Hat Mono (Regular, Bold)

#### Font Usage in Canvas

Fonts were loaded using FontFace API and used in Canvas:

```javascript
// Load custom font
const font = new FontFace('CustomFont', 'url(canvas-fonts/Lora-Regular.ttf)');
await font.load();
document.fonts.add(font);

// Use in canvas
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
ctx.font = '48px "CustomFont"';
ctx.fillText('Hello World', 100, 100);
```

## Use Cases

This skill helps with:
- Creating typography-rich canvas designs
- Building custom font-based graphics
- Generating social media images with custom fonts
- Creating branded visual content
- Designing with specific typefaces

## Skill Patterns Demonstrated

- **Asset library** - Large collection of fonts (81 files)
- **Typography focus** - Custom typeface selection
- **Open source fonts** - All OFL-licensed fonts
- **Canvas integration** - Font loading for Canvas rendering
- **Multi-variant fonts** - Regular, Bold, Italic options

## Restoration

To recreate the font library:
1. Download fonts from Google Fonts or similar OFL font sources
2. Organize in `canvas-fonts/` directory
3. Include both .ttf and OFL.txt license files for each family
4. Test font loading with FontFace API
5. Create examples showing font usage in Canvas contexts

**Font sources:**
- Google Fonts (https://fonts.google.com/)
- Font Squirrel (https://www.fontsquirrel.com/)
- Open Font Library (https://fontlibrary.org/)

See SKILL.md for the complete skill implementation.

