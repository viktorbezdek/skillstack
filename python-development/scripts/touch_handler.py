"""
Touch Input Handler for Pimoroni Presto
Provides debounced touch event handling with gesture detection
"""

import time
from machine import Pin


class TouchHandler:
    """
    Handles touch input with debouncing and basic gesture detection.

    Usage:
        touch = TouchHandler(touchscreen_device)

        while True:
            event = touch.poll()
            if event:
                print(f"Touch at ({event.x}, {event.y}), type: {event.type}")
    """

    # Event types
    TOUCH_DOWN = 0
    TOUCH_UP = 1
    TOUCH_DRAG = 2

    def __init__(self, touch_device, debounce_ms=50):
        """
        Initialize touch handler.

        Args:
            touch_device: Touch interface from display driver
            debounce_ms: Minimum time between touch events (milliseconds)
        """
        self.device = touch_device
        self.debounce_ms = debounce_ms
        self.last_event_time = 0
        self.last_pos = None
        self.is_touching = False

    def poll(self):
        """
        Poll for touch events.

        Returns:
            TouchEvent object or None if no new event
        """
        current_time = time.ticks_ms()

        # Check debounce period
        if time.ticks_diff(current_time, self.last_event_time) < self.debounce_ms:
            return None

        # Get current touch state
        touched, x, y = self._read_touch()

        if touched:
            event_type = self.TOUCH_DRAG if self.is_touching else self.TOUCH_DOWN
            self.is_touching = True
            self.last_pos = (x, y)
            self.last_event_time = current_time
            return TouchEvent(event_type, x, y)
        elif self.is_touching:
            # Touch released
            self.is_touching = False
            self.last_event_time = current_time
            x, y = self.last_pos if self.last_pos else (0, 0)
            return TouchEvent(self.TOUCH_UP, x, y)

        return None

    def _read_touch(self):
        """
        Read raw touch data from device.
        Override this method for specific touch controller.
        """
        # Example for common I2C touch controllers
        try:
            touched = self.device.is_touched()
            if touched:
                x, y = self.device.get_point()
                return True, x, y
        except:
            pass
        return False, 0, 0


class TouchEvent:
    """Represents a single touch event."""

    def __init__(self, event_type, x, y):
        self.type = event_type
        self.x = x
        self.y = y
        self.timestamp = time.ticks_ms()

    def __repr__(self):
        type_names = {0: "DOWN", 1: "UP", 2: "DRAG"}
        return f"TouchEvent({type_names.get(self.type, 'UNKNOWN')}, {self.x}, {self.y})"


class GestureDetector:
    """
    Detects swipe gestures from touch events.

    Usage:
        gesture_detector = GestureDetector()

        # In touch event loop:
        if event.type == TouchHandler.TOUCH_DOWN:
            gesture_detector.start(event.x, event.y)
        elif event.type == TouchHandler.TOUCH_UP:
            gesture = gesture_detector.end(event.x, event.y)
            if gesture:
                print(f"Detected gesture: {gesture}")
    """

    # Gesture types
    SWIPE_LEFT = "left"
    SWIPE_RIGHT = "right"
    SWIPE_UP = "up"
    SWIPE_DOWN = "down"
    TAP = "tap"

    def __init__(self, min_swipe_distance=50, max_tap_distance=10):
        """
        Initialize gesture detector.

        Args:
            min_swipe_distance: Minimum distance for swipe detection (pixels)
            max_tap_distance: Maximum distance for tap detection (pixels)
        """
        self.min_swipe = min_swipe_distance
        self.max_tap = max_tap_distance
        self.start_pos = None
        self.start_time = None

    def start(self, x, y):
        """Record touch start position."""
        self.start_pos = (x, y)
        self.start_time = time.ticks_ms()

    def end(self, x, y):
        """
        Detect gesture from start to end position.

        Returns:
            Gesture string or None
        """
        if not self.start_pos:
            return None

        dx = x - self.start_pos[0]
        dy = y - self.start_pos[1]
        distance = (dx**2 + dy**2)**0.5

        # Tap detection
        if distance < self.max_tap:
            return self.TAP

        # Swipe detection
        if distance >= self.min_swipe:
            if abs(dx) > abs(dy):
                return self.SWIPE_RIGHT if dx > 0 else self.SWIPE_LEFT
            else:
                return self.SWIPE_DOWN if dy > 0 else self.SWIPE_UP

        return None
