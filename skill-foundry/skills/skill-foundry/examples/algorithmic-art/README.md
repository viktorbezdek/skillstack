# Algorithmic Art Skill Example

This example demonstrates a skill for generating algorithmic art using HTML5 Canvas and JavaScript.

## Skill Structure

- **SKILL.md** - Main skill file with instructions
- **LICENSE.txt** - MIT License

## Removed Resources (Described Below)

### templates/

This skill originally included template files for generating algorithmic art:

#### generator_template.js
JavaScript template for creating generative art algorithms. Included:
- Canvas setup and context configuration
- Animation loop structure
- Random number generation utilities
- Color palette management
- Common drawing functions (circles, lines, curves)
- Parameter randomization
- Export/save functionality

**Typical content:**
```javascript
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const width = canvas.width;
const height = canvas.height;

// Animation parameters
let frame = 0;
const frameRate = 60;

// Your algorithmic art logic here
function draw() {
    // Clear or build on previous frame
    // Apply algorithms (fractals, noise, cellular automata, etc.)
    // Update parameters
    frame++;
    requestAnimationFrame(draw);
}

draw();
```

#### viewer.html
HTML template for viewing and interacting with generated art. Included:
- Canvas element setup
- Controls for parameters (sliders, buttons, color pickers)
- Export/download button
- Responsive layout
- Script loading for generator
- Style definitions

**Typical content:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Algorithmic Art</title>
    <style>
        canvas { border: 1px solid #000; }
        #controls { margin: 20px; }
    </style>
</head>
<body>
    <canvas id="canvas" width="800" height="600"></canvas>
    <div id="controls">
        <!-- Parameter controls -->
        <button id="save">Save Image</button>
        <button id="randomize">Randomize</button>
    </div>
    <script src="generator.js"></script>
</body>
</html>
```

## Use Cases

This skill helps with:
- Generating unique algorithmic art pieces
- Creating Canvas-based animations
- Building interactive art installations
- Producing randomized visual patterns
- Exporting artwork as images

## Skill Patterns Demonstrated

- **Asset templates** - Provides boilerplate code users can customize
- **Multi-file templates** - HTML + JavaScript working together
- **Interactive output** - Generated art can be viewed in browser
- **Export functionality** - Save generated art as images
- **Parameterization** - Adjustable values for different results

## Restoration

To recreate the templates:
1. Create `templates/generator_template.js` with Canvas drawing logic
2. Create `templates/viewer.html` with Canvas display and controls
3. Include examples of common algorithms (fractals, Perlin noise, cellular automata)
4. Add export functionality to save as PNG/SVG

See SKILL.md for the complete skill implementation.

