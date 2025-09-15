# Display Rendering on RP2350

## Framebuffer Basics

MicroPython's `framebuf` module provides efficient bitmap operations for displays.

### RGB565 Color Format

Most displays use RGB565: 16 bits per pixel (5 bits red, 6 bits green, 5 bits blue).

```python
import framebuf

# Color conversion
def rgb_to_rgb565(r, g, b):
    """
    Convert RGB888 to RGB565.

    Args:
        r, g, b: Color values (0-255)

    Returns:
        16-bit RGB565 value
    """
    return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)

# Common colors in RGB565
WHITE = 0xFFFF
BLACK = 0x0000
RED = 0xF800
GREEN = 0x07E0
BLUE = 0x001F
YELLOW = 0xFFE0
CYAN = 0x07FF
MAGENTA = 0xF81F
```

## Memory-Efficient Rendering

### Problem: Full Framebuffer

480×480 RGB565 display requires ~460KB - nearly all available RAM!

### Solution 1: Tile-Based Rendering

Render display in small tiles, updating one at a time.

```python
import framebuf

class TiledDisplay:
    """
    Render display in tiles to conserve memory.

    Instead of one 480x480 buffer (460KB),
    use a 60x60 tile buffer (~7KB) and update 64 tiles.
    """

    def __init__(self, display, tile_size=60):
        self.display = display
        self.tile_size = tile_size
        self.width = 480
        self.height = 480

        # Tile buffer (much smaller than full framebuffer)
        self.tile_buffer = bytearray(tile_size * tile_size * 2)
        self.fb = framebuf.FrameBuffer(
            self.tile_buffer,
            tile_size,
            tile_size,
            framebuf.RGB565
        )

    def render_full_screen(self, draw_func):
        """
        Render entire screen tile by tile.

        Args:
            draw_func: Function(fb, x_offset, y_offset) that draws content
        """
        tiles_x = self.width // self.tile_size
        tiles_y = self.height // self.tile_size

        for ty in range(tiles_y):
            for tx in range(tiles_x):
                # Calculate tile position
                x = tx * self.tile_size
                y = ty * self.tile_size

                # Clear tile
                self.fb.fill(0)

                # Draw content for this tile
                draw_func(self.fb, x, y)

                # Send tile to display
                self.display.blit_tile(
                    self.tile_buffer,
                    x, y,
                    self.tile_size,
                    self.tile_size
                )


# Usage example
def draw_timer_screen(fb, x_offset, y_offset):
    """Draw timer UI for given tile."""
    # Only draw if this tile contains the timer circle
    if 180 <= x_offset <= 300 and 180 <= y_offset <= 300:
        # Draw circle segment in this tile
        center_x = 240 - x_offset
        center_y = 240 - y_offset
        fb.ellipse(center_x, center_y, 50, 50, WHITE)

display = TiledDisplay(spi_display)
display.render_full_screen(draw_timer_screen)
```

### Solution 2: Partial Updates

Only redraw changed portions of the screen.

```python
class PartialUpdateDisplay:
    """Track and update only changed regions."""

    def __init__(self, display, width=480, height=480):
        self.display = display
        self.width = width
        self.height = height

        # Small buffers for specific UI elements
        self.timer_buffer = bytearray(100 * 100 * 2)  # 100x100 timer display
        self.status_buffer = bytearray(200 * 30 * 2)  # 200x30 status bar

        self.timer_fb = framebuf.FrameBuffer(
            self.timer_buffer, 100, 100, framebuf.RGB565
        )
        self.status_fb = framebuf.FrameBuffer(
            self.status_buffer, 200, 30, framebuf.RGB565
        )

    def update_timer(self, seconds):
        """Update only the timer region."""
        self.timer_fb.fill(BLACK)

        # Draw timer text
        time_str = f"{seconds // 60}:{seconds % 60:02d}"
        self.timer_fb.text(time_str, 10, 45, WHITE)

        # Send just the timer region to display
        self.display.blit_buffer(
            self.timer_buffer,
            190, 190,  # Centered position
            100, 100
        )

    def update_status(self, message):
        """Update only the status bar."""
        self.status_fb.fill(BLACK)
        self.status_fb.text(message, 5, 10, WHITE)

        self.display.blit_buffer(
            self.status_buffer,
            140, 10,  # Top of screen
            200, 30
        )
```

### Solution 3: Reduced Color Depth

Use 1-bit (monochrome) or 8-bit (256 colors) for simpler UIs.

```python
import framebuf

# 1-bit monochrome (60 bytes for 480x1 line!)
mono_buffer = bytearray(480 // 8)  # 1 bit per pixel
fb = framebuf.FrameBuffer(mono_buffer, 480, 1, framebuf.MONO_HLSB)

# 8-bit color (10x less memory than RGB565)
palette_buffer = bytearray(480 * 480)  # 1 byte per pixel
fb = framebuf.FrameBuffer(palette_buffer, 480, 480, framebuf.GS8)
```

## Drawing Primitives

### Basic Shapes

```python
import framebuf

# Create framebuffer
buf = bytearray(480 * 480 * 2)
fb = framebuf.FrameBuffer(buf, 480, 480, framebuf.RGB565)

# Fill with color
fb.fill(BLACK)

# Draw pixel
fb.pixel(100, 100, RED)

# Draw line
fb.line(0, 0, 479, 479, WHITE)

# Draw rectangle
fb.rect(50, 50, 100, 80, GREEN)  # x, y, w, h, color

# Draw filled rectangle
fb.fill_rect(200, 50, 100, 80, BLUE)

# Draw circle (ellipse with equal radii)
fb.ellipse(240, 240, 50, 50, YELLOW)

# Draw filled ellipse
fb.ellipse(240, 240, 30, 30, RED, True)  # Last param = filled
```

### Text Rendering

Built-in font is 8×8 pixels.

```python
# Draw text
fb.text("Hello, World!", 10, 10, WHITE)

# Multi-line text
lines = ["Line 1", "Line 2", "Line 3"]
y = 10
for line in lines:
    fb.text(line, 10, y, WHITE)
    y += 10  # 8px font + 2px spacing

# Centered text
text = "Centered"
text_width = len(text) * 8
x = (480 - text_width) // 2
fb.text(text, x, 240, WHITE)
```

### Custom Fonts

For larger text, use sprite-based fonts or libraries like `writer.py`.

```python
# Using writer library (must be uploaded to device)
from writer import Writer
import freesans20  # Custom font file

# Create writer
wri = Writer(fb, freesans20)

# Write text
Writer.set_textpos(fb, 100, 100)
wri.printstring("Large Text")
```

## Advanced Graphics

### Progress Bar

```python
def draw_progress_bar(fb, x, y, width, height, progress, color):
    """
    Draw a progress bar.

    Args:
        fb: Framebuffer
        x, y: Position
        width, height: Dimensions
        progress: Progress (0.0 to 1.0)
        color: Fill color
    """
    # Border
    fb.rect(x, y, width, height, WHITE)

    # Fill
    fill_width = int((width - 4) * progress)
    if fill_width > 0:
        fb.fill_rect(x + 2, y + 2, fill_width, height - 4, color)
```

### Circular Progress (Timer)

```python
import math

def draw_circular_progress(fb, cx, cy, radius, progress, color):
    """
    Draw circular progress indicator.

    Args:
        fb: Framebuffer
        cx, cy: Center coordinates
        radius: Radius
        progress: Progress (0.0 to 1.0)
        color: Arc color
    """
    # Draw segments to approximate arc
    segments = 60
    end_segment = int(segments * progress)

    for i in range(end_segment):
        angle1 = -math.pi / 2 + (2 * math.pi * i / segments)
        angle2 = -math.pi / 2 + (2 * math.pi * (i + 1) / segments)

        x1 = int(cx + radius * math.cos(angle1))
        y1 = int(cy + radius * math.sin(angle1))
        x2 = int(cx + radius * math.cos(angle2))
        y2 = int(cy + radius * math.sin(angle2))

        fb.line(x1, y1, x2, y2, color)
```

### Smooth Gradients

```python
def draw_gradient(fb, x, y, width, height, color1, color2):
    """
    Draw vertical gradient.

    Args:
        fb: Framebuffer
        x, y: Position
        width, height: Dimensions
        color1, color2: Start and end colors (RGB565)
    """
    # Extract RGB components
    r1 = (color1 >> 11) & 0x1F
    g1 = (color1 >> 5) & 0x3F
    b1 = color1 & 0x1F

    r2 = (color2 >> 11) & 0x1F
    g2 = (color2 >> 5) & 0x3F
    b2 = color2 & 0x1F

    # Draw gradient line by line
    for row in range(height):
        progress = row / height

        # Interpolate
        r = int(r1 + (r2 - r1) * progress)
        g = int(g1 + (g2 - g1) * progress)
        b = int(b1 + (b2 - b1) * progress)

        # Recombine to RGB565
        color = (r << 11) | (g << 5) | b

        # Draw line
        fb.hline(x, y + row, width, color)
```

## Animation Techniques

### Frame Interpolation

Create smooth animations between states.

```python
class Animator:
    """Simple animation with easing."""

    @staticmethod
    def ease_in_out(t):
        """
        Ease-in-out cubic easing.

        Args:
            t: Time progress (0.0 to 1.0)

        Returns:
            Eased value (0.0 to 1.0)
        """
        if t < 0.5:
            return 4 * t * t * t
        else:
            p = 2 * t - 2
            return 1 + p * p * p / 2

    @staticmethod
    def lerp(start, end, t):
        """Linear interpolation."""
        return start + (end - start) * t

    def animate_value(self, start, end, duration_ms, easing=None):
        """
        Animate a value over time.

        Usage:
            for value in animator.animate_value(0, 240, 1000):
                draw_object(value)
                display.show()
        """
        import time

        if easing is None:
            easing = self.ease_in_out

        start_time = time.ticks_ms()
        while True:
            elapsed = time.ticks_diff(time.ticks_ms(), start_time)
            if elapsed >= duration_ms:
                yield end
                break

            t = elapsed / duration_ms
            eased_t = easing(t)
            yield self.lerp(start, end, eased_t)
```

### Double Buffering

Prevent tearing by rendering offscreen.

```python
class DoubleBufferedDisplay:
    """
    Double-buffered display to prevent tearing.

    WARNING: Requires 2x memory for framebuffers!
    Only feasible with small regions or tile-based rendering.
    """

    def __init__(self, display, width, height):
        self.display = display
        self.width = width
        self.height = height

        # Front and back buffers
        self.front = bytearray(width * height * 2)
        self.back = bytearray(width * height * 2)

        self.front_fb = framebuf.FrameBuffer(
            self.front, width, height, framebuf.RGB565
        )
        self.back_fb = framebuf.FrameBuffer(
            self.back, width, height, framebuf.RGB565
        )

    def get_draw_buffer(self):
        """Get buffer to draw into (back buffer)."""
        return self.back_fb

    def swap(self):
        """Swap buffers and display."""
        # Swap references
        self.front, self.back = self.back, self.front
        self.front_fb, self.back_fb = self.back_fb, self.front_fb

        # Display front buffer
        self.display.blit_buffer(self.front, 0, 0, self.width, self.height)


# Usage
display = DoubleBufferedDisplay(spi_display, 240, 240)  # Smaller region

while True:
    # Draw to back buffer
    fb = display.get_draw_buffer()
    fb.fill(BLACK)
    draw_ui(fb)

    # Swap and display (no tearing!)
    display.swap()
```

## Performance Tips

### 1. Minimize Redraws

Only update changed elements.

```python
class StatefulDisplay:
    """Track state to avoid unnecessary redraws."""

    def __init__(self, fb):
        self.fb = fb
        self.last_timer_value = None
        self.last_status = None

    def update_timer(self, seconds):
        if seconds != self.last_timer_value:
            # Only redraw if changed
            self._draw_timer(seconds)
            self.last_timer_value = seconds

    def update_status(self, status):
        if status != self.last_status:
            self._draw_status(status)
            self.last_status = status
```

### 2. Use Integer Math

Avoid floating-point when possible.

```python
# Slow (floating-point)
x = int(240 * 0.5)

# Fast (integer)
x = 240 // 2

# Fixed-point for sub-pixel precision
x_fixed = 24000  # Represents 240.00 (scale by 100)
x_scaled = x_fixed // 2  # 12000 = 120.00
x = x_scaled // 100  # Final value: 120
```

### 3. Batch Drawing Operations

Group similar operations.

```python
# Slow (many small operations)
for i in range(100):
    fb.pixel(i, 100, WHITE)

# Fast (single line operation)
fb.hline(0, 100, 100, WHITE)
```

### 4. Pre-compute Graphics

Store complex graphics as bitmaps.

```python
# Pre-rendered icon (8x8, monochrome)
ICON_TIMER = bytearray([
    0b00111100,
    0b01000010,
    0b10000001,
    0b10000001,
    0b10001001,
    0b10000001,
    0b01000010,
    0b00111100,
])

def draw_icon(fb, x, y):
    """Draw pre-rendered icon."""
    for row in range(8):
        byte = ICON_TIMER[row]
        for col in range(8):
            if byte & (1 << (7 - col)):
                fb.pixel(x + col, y + row, WHITE)
```

## ADHD-Friendly UI Guidelines

### Visual Hierarchy

- **Large, simple elements**: Big buttons, clear text
- **High contrast**: White on black, or vivid colors
- **Minimal clutter**: One task per screen when possible

### Color Coding

```python
# Timer states with distinct colors
STATE_IDLE = (64, 64, 64)      # Gray
STATE_FOCUS = (30, 144, 255)    # Blue
STATE_BREAK = (50, 205, 50)     # Green
STATE_URGENT = (220, 20, 60)    # Red
STATE_PAUSED = (255, 191, 0)    # Amber

def draw_status_indicator(fb, state):
    """Draw clear state indicator."""
    color = rgb_to_rgb565(*state)

    # Large filled circle
    fb.ellipse(240, 50, 20, 20, color, True)

    # Status text
    texts = {
        STATE_IDLE: "Ready",
        STATE_FOCUS: "Focusing",
        STATE_BREAK: "Break Time",
        STATE_URGENT: "Almost Done!",
        STATE_PAUSED: "Paused"
    }

    text = texts.get(state, "Unknown")
    fb.text(text, 200, 75, WHITE)
```

### Progressive Disclosure

Show only necessary information, reveal details on interaction.

```python
def draw_minimal_timer(fb, seconds):
    """Simple timer view."""
    # Just show time remaining - large and clear
    mins = seconds // 60
    secs = seconds % 60

    # Large text (custom font recommended)
    time_str = f"{mins:02d}:{secs:02d}"

    # Center on screen
    fb.text(time_str, 200, 230, WHITE)  # Approximate center


def draw_detailed_timer(fb, seconds, total, tasks_completed):
    """Detailed timer view (shown on tap)."""
    # Time remaining
    draw_minimal_timer(fb, seconds)

    # Progress bar
    progress = 1 - (seconds / total)
    draw_progress_bar(fb, 100, 300, 280, 20, progress, GREEN)

    # Stats
    fb.text(f"Tasks: {tasks_completed}", 180, 350, WHITE)
```

## Complete Example: Timer Display

```python
import framebuf
import time

class TimerDisplay:
    """Complete timer display with animations."""

    def __init__(self, display):
        self.display = display

        # Use tile-based rendering for memory efficiency
        self.tile = TiledDisplay(display, tile_size=60)

        # Current state
        self.remaining = 0
        self.total = 0
        self.state = STATE_IDLE

    def draw_screen(self, fb, x_offset, y_offset):
        """Draw UI for specific tile."""
        # Background
        fb.fill(BLACK)

        # Draw circular progress
        if 160 <= x_offset <= 320 and 160 <= y_offset <= 320:
            progress = 1 - (self.remaining / self.total) if self.total > 0 else 0
            cx = 240 - x_offset
            cy = 240 - y_offset
            draw_circular_progress(fb, cx, cy, 80, progress, GREEN)

        # Draw time text
        if 180 <= x_offset <= 300 and 220 <= y_offset <= 260:
            mins = self.remaining // 60
            secs = self.remaining % 60
            text = f"{mins:02d}:{secs:02d}"

            # Center in tile
            tx = 240 - x_offset - len(text) * 4
            ty = 240 - y_offset - 4

            fb.text(text, tx, ty, WHITE)

    def update(self, remaining, total, state):
        """Update display with current timer state."""
        self.remaining = remaining
        self.total = total
        self.state = state

        # Render full screen
        self.tile.render_full_screen(self.draw_screen)
```

This provides a complete, memory-efficient timer display system for the Presto that follows ADHD-friendly design principles.
