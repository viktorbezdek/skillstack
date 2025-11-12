"""
RGB Backlight Control with Smooth Transitions
Provides PWM-based RGB control with animations and color transitions
"""

import time
from machine import Pin, PWM
import math


class RGBBacklight:
    """
    RGB backlight controller with smooth color transitions.

    Usage:
        rgb = RGBBacklight(red_pin=16, green_pin=17, blue_pin=18)

        # Instant color change
        rgb.set_color(255, 0, 0)  # Red

        # Smooth transition
        rgb.fade_to(0, 255, 0, duration_ms=1000)  # Fade to green

        # Pulse effect
        rgb.pulse((255, 128, 0), period_ms=2000)  # Orange pulse
    """

    def __init__(self, red_pin, green_pin, blue_pin, freq=1000, invert=False):
        """
        Initialize RGB backlight controller.

        Args:
            red_pin: GPIO pin for red channel
            green_pin: GPIO pin for green channel
            blue_pin: GPIO pin for blue channel
            freq: PWM frequency in Hz (default: 1000)
            invert: Invert PWM signal (for common anode LEDs)
        """
        self.r_pwm = PWM(Pin(red_pin))
        self.g_pwm = PWM(Pin(green_pin))
        self.b_pwm = PWM(Pin(blue_pin))

        self.r_pwm.freq(freq)
        self.g_pwm.freq(freq)
        self.b_pwm.freq(freq)

        self.invert = invert
        self.current_color = (0, 0, 0)
        self.target_color = (0, 0, 0)

        # For animations
        self._animation_active = False
        self._animation_start_time = 0
        self._animation_duration = 0

        self.set_color(0, 0, 0)

    def _value_to_duty(self, value):
        """Convert 0-255 value to PWM duty cycle."""
        if self.invert:
            value = 255 - value
        return int((value / 255) * 65535)

    def set_color(self, r, g, b):
        """
        Set RGB color immediately.

        Args:
            r, g, b: Color values (0-255)
        """
        self.current_color = (r, g, b)
        self.target_color = (r, g, b)

        self.r_pwm.duty_u16(self._value_to_duty(r))
        self.g_pwm.duty_u16(self._value_to_duty(g))
        self.b_pwm.duty_u16(self._value_to_duty(b))

    def fade_to(self, r, g, b, duration_ms=500, steps=50):
        """
        Smoothly fade to target color.

        Args:
            r, g, b: Target color (0-255)
            duration_ms: Fade duration in milliseconds
            steps: Number of interpolation steps
        """
        start_r, start_g, start_b = self.current_color
        step_delay = duration_ms / steps

        for i in range(steps + 1):
            progress = i / steps

            # Linear interpolation
            current_r = int(start_r + (r - start_r) * progress)
            current_g = int(start_g + (g - start_g) * progress)
            current_b = int(start_b + (b - start_b) * progress)

            self.set_color(current_r, current_g, current_b)
            time.sleep_ms(int(step_delay))

    def pulse(self, color, period_ms=2000, min_brightness=0.1, iterations=None):
        """
        Pulse effect (breathing).

        Args:
            color: Target color tuple (r, g, b)
            period_ms: Pulse period in milliseconds
            min_brightness: Minimum brightness (0.0-1.0)
            iterations: Number of pulses (None for infinite)
        """
        r, g, b = color
        count = 0

        while iterations is None or count < iterations:
            # Use sine wave for smooth breathing effect
            steps = 60
            for i in range(steps):
                # Sine wave from min_brightness to 1.0
                brightness = min_brightness + (1 - min_brightness) * (
                    (math.sin(2 * math.pi * i / steps) + 1) / 2
                )

                self.set_color(
                    int(r * brightness), int(g * brightness), int(b * brightness)
                )

                time.sleep_ms(period_ms // steps)

            count += 1

    def rainbow_cycle(self, duration_ms=5000, steps=100):
        """
        Cycle through rainbow colors.

        Args:
            duration_ms: Total cycle duration
            steps: Number of color steps
        """
        step_delay = duration_ms / steps

        for i in range(steps):
            hue = i / steps
            r, g, b = self._hsv_to_rgb(hue, 1.0, 1.0)
            self.set_color(r, g, b)
            time.sleep_ms(int(step_delay))

    def _hsv_to_rgb(self, h, s, v):
        """
        Convert HSV to RGB.

        Args:
            h: Hue (0.0-1.0)
            s: Saturation (0.0-1.0)
            v: Value/brightness (0.0-1.0)

        Returns:
            Tuple (r, g, b) with values 0-255
        """
        if s == 0.0:
            r = g = b = int(v * 255)
            return (r, g, b)

        i = int(h * 6.0)
        f = (h * 6.0) - i
        p = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        i = i % 6

        if i == 0:
            r, g, b = v, t, p
        elif i == 1:
            r, g, b = q, v, p
        elif i == 2:
            r, g, b = p, v, t
        elif i == 3:
            r, g, b = p, q, v
        elif i == 4:
            r, g, b = t, p, v
        else:
            r, g, b = v, p, q

        return (int(r * 255), int(g * 255), int(b * 255))

    def urgency_gradient(self, remaining_seconds, total_seconds):
        """
        Calculate urgency color based on time remaining.
        Green -> Yellow -> Orange -> Red

        Args:
            remaining_seconds: Time remaining
            total_seconds: Total time

        Returns:
            RGB tuple
        """
        if total_seconds == 0:
            return (255, 0, 0)  # Red

        ratio = remaining_seconds / total_seconds

        if ratio > 0.5:
            # Green to yellow (100% -> 50%)
            green_amount = 255
            red_amount = int(255 * (1 - (ratio - 0.5) * 2))
            return (red_amount, green_amount, 0)
        elif ratio > 0.25:
            # Yellow to orange (50% -> 25%)
            red_amount = 255
            green_amount = int(255 * ((ratio - 0.25) * 4))
            return (red_amount, green_amount, 0)
        else:
            # Orange to red (25% -> 0%)
            red_amount = 255
            green_amount = int(128 * (ratio * 4))
            return (red_amount, green_amount, 0)

    def off(self):
        """Turn off backlight."""
        self.set_color(0, 0, 0)

    def white(self, brightness=255):
        """Set to white at specified brightness."""
        self.set_color(brightness, brightness, brightness)


class PresetColors:
    """Common color presets."""

    # Basic colors
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Extended colors
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    PINK = (255, 192, 203)

    # ADHD-friendly colors (high contrast, distinct)
    FOCUS_BLUE = (30, 144, 255)  # Dodger blue
    BREAK_GREEN = (50, 205, 50)  # Lime green
    URGENT_RED = (220, 20, 60)  # Crimson
    PAUSED_AMBER = (255, 191, 0)  # Amber
    IDLE_DIM = (64, 64, 64)  # Dim gray


# Example usage combining color transitions with timer states
def demo_timer_colors():
    """
    Example showing how to use RGB backlight for timer feedback.
    """
    rgb = RGBBacklight(red_pin=16, green_pin=17, blue_pin=18)

    # Idle state
    print("Idle (dim)")
    rgb.set_color(*PresetColors.IDLE_DIM)
    time.sleep(2)

    # Focus mode starting
    print("Focus starting (blue)")
    rgb.fade_to(*PresetColors.FOCUS_BLUE, duration_ms=1000)
    time.sleep(2)

    # Simulate timer countdown with urgency gradient
    print("Timer running (urgency gradient)")
    total_time = 1500  # 25 minutes
    for remaining in range(1500, 0, -300):  # Every 5 minutes
        r, g, b = rgb.urgency_gradient(remaining, total_time)
        print(f"  {remaining}s remaining: RGB({r}, {g}, {b})")
        rgb.fade_to(r, g, b, duration_ms=500)
        time.sleep(2)

    # Timer complete - pulse green
    print("Timer complete (pulsing green)")
    rgb.pulse(PresetColors.BREAK_GREEN, period_ms=1500, iterations=3)

    # Off
    rgb.off()


if __name__ == "__main__":
    demo_timer_colors()
