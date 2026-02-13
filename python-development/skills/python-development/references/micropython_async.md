# MicroPython Async Patterns for RP2350

## Introduction to Asyncio in MicroPython

MicroPython's `asyncio` library enables cooperative multitasking, allowing multiple tasks to run concurrently without blocking. This is essential for responsive UIs, network communication, and timer management.

## Basic Asyncio Concepts

### Coroutines

Functions defined with `async def` that can pause execution with `await`.

```python
import asyncio

async def my_coroutine():
    print("Starting")
    await asyncio.sleep(1)  # Pause for 1 second
    print("Done")

# Run the coroutine
asyncio.run(my_coroutine())
```

### Tasks

Tasks wrap coroutines and run them concurrently in the event loop.

```python
async def task1():
    while True:
        print("Task 1")
        await asyncio.sleep(1)

async def task2():
    while True:
        print("Task 2")
        await asyncio.sleep(2)

async def main():
    # Create tasks
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    # Wait for both (will run forever in this example)
    await asyncio.gather(t1, t2)

asyncio.run(main())
```

## Common Async Patterns for Presto

### Pattern 1: Non-Blocking UI Updates

Keep the UI responsive while performing other tasks.

```python
import asyncio
from touch_handler import TouchHandler
from rgb_backlight import RGBBacklight

async def ui_task(touch, rgb):
    """Handle touch input and update display."""
    while True:
        event = touch.poll()
        if event:
            # Handle touch event
            if event.type == TouchHandler.TOUCH_DOWN:
                rgb.set_color(255, 0, 0)  # Red feedback
            elif event.type == TouchHandler.TOUCH_UP:
                rgb.set_color(0, 255, 0)  # Green feedback

        # Yield to other tasks (10ms update rate)
        await asyncio.sleep_ms(10)

async def timer_task():
    """Run timer countdown."""
    remaining = 1500  # 25 minutes

    while remaining > 0:
        print(f"Time remaining: {remaining}s")
        remaining -= 1
        await asyncio.sleep(1)

    print("Timer complete!")

async def main():
    touch = TouchHandler(touch_device)
    rgb = RGBBacklight(16, 17, 18)

    # Run UI and timer concurrently
    await asyncio.gather(
        ui_task(touch, rgb),
        timer_task()
    )

asyncio.run(main())
```

### Pattern 2: MQTT with Auto-Reconnect

Non-blocking MQTT client that handles reconnection.

```python
import asyncio
from mqtt_client import ReliableMQTTClient

async def mqtt_task(mqtt):
    """Maintain MQTT connection and handle messages."""
    while True:
        # Check for messages (non-blocking)
        mqtt.check_msg()

        # If disconnected, reconnect
        if not mqtt.is_connected():
            mqtt.connect()

        await asyncio.sleep_ms(100)

async def publish_status(mqtt):
    """Periodically publish status."""
    while True:
        mqtt.publish("productivity/device/status", "online")
        await asyncio.sleep(30)  # Every 30 seconds

async def main():
    mqtt = ReliableMQTTClient(
        client_id="presto-001",
        broker="192.168.1.100",
        callback=message_callback
    )

    await asyncio.gather(
        mqtt_task(mqtt),
        publish_status(mqtt)
    )

asyncio.run(main())
```

### Pattern 3: BLE Server with UI

Run BLE server alongside touch interface.

```python
import asyncio
from ble_gatt_server import BLETimerServer

async def ble_task(ble):
    """Handle BLE commands."""
    while True:
        command = ble.get_command()
        if command is not None:
            handle_timer_command(command)

        await asyncio.sleep_ms(50)

async def timer_sync_task(ble, timer):
    """Sync timer state to BLE clients."""
    while True:
        ble.update_timer_state(
            timer.remaining_seconds,
            timer.is_running
        )
        await asyncio.sleep_ms(500)

async def main():
    ble = BLETimerServer("Presto-Timer")
    ble.start_advertising()

    timer = Timer()  # Your timer implementation

    await asyncio.gather(
        ble_task(ble),
        timer_sync_task(ble, timer)
    )

asyncio.run(main())
```

### Pattern 4: Periodic Display Updates

Update display at fixed intervals without blocking.

```python
import asyncio
import framebuf

async def display_task(display, state):
    """Update display every 100ms."""
    while True:
        # Create framebuffer
        buf = bytearray(480 * 480 * 2)  # RGB565
        fb = framebuf.FrameBuffer(buf, 480, 480, framebuf.RGB565)

        # Draw UI based on state
        draw_ui(fb, state)

        # Send to display (this should be fast)
        display.blit_buffer(buf, 0, 0, 480, 480)

        await asyncio.sleep_ms(100)  # 10 FPS

async def state_update_task(state):
    """Update application state."""
    while True:
        # Update state (timer countdown, etc.)
        state.update()
        await asyncio.sleep(1)

async def main():
    state = AppState()
    display = init_display()

    await asyncio.gather(
        display_task(display, state),
        state_update_task(state)
    )

asyncio.run(main())
```

### Pattern 5: Event-Driven Architecture

Use asyncio queues for event handling.

```python
import asyncio

# Global event queue
event_queue = asyncio.Queue()

async def touch_event_producer(touch):
    """Produce touch events."""
    while True:
        event = touch.poll()
        if event:
            await event_queue.put(("touch", event))
        await asyncio.sleep_ms(10)

async def mqtt_event_producer(mqtt):
    """Produce MQTT events."""
    # This would be integrated with MQTT callback
    pass

async def event_consumer(state):
    """Consume and process all events."""
    while True:
        event_type, event_data = await event_queue.get()

        if event_type == "touch":
            handle_touch_event(state, event_data)
        elif event_type == "mqtt":
            handle_mqtt_event(state, event_data)

async def main():
    state = AppState()
    touch = TouchHandler(touch_device)

    await asyncio.gather(
        touch_event_producer(touch),
        event_consumer(state)
    )

asyncio.run(main())
```

## Advanced Patterns

### Cancellable Tasks

Tasks that can be stopped cleanly.

```python
import asyncio

async def cancellable_timer(duration_seconds):
    """Timer that can be cancelled."""
    try:
        for i in range(duration_seconds, 0, -1):
            print(f"{i} seconds remaining")
            await asyncio.sleep(1)
        print("Timer complete!")
    except asyncio.CancelledError:
        print("Timer cancelled")
        raise  # Re-raise to properly cancel

async def main():
    # Start timer
    timer_task = asyncio.create_task(cancellable_timer(60))

    # Wait a bit
    await asyncio.sleep(5)

    # Cancel the timer
    timer_task.cancel()

    try:
        await timer_task
    except asyncio.CancelledError:
        print("Cleanup after cancellation")

asyncio.run(main())
```

### Task Synchronization with Locks

Prevent race conditions when multiple tasks access shared resources.

```python
import asyncio

class SharedState:
    def __init__(self):
        self.lock = asyncio.Lock()
        self.value = 0

    async def increment(self):
        async with self.lock:
            # Only one task can execute this at a time
            current = self.value
            await asyncio.sleep(0)  # Simulate work
            self.value = current + 1

async def incrementer(state, name):
    for _ in range(10):
        await state.increment()
        print(f"{name}: {state.value}")

async def main():
    state = SharedState()

    # Multiple tasks incrementing safely
    await asyncio.gather(
        incrementer(state, "Task 1"),
        incrementer(state, "Task 2")
    )

    print(f"Final value: {state.value}")

asyncio.run(main())
```

### Timeout Handling

Set maximum time for operations.

```python
import asyncio

async def slow_operation():
    """Operation that might take too long."""
    await asyncio.sleep(10)
    return "Done"

async def main():
    try:
        # Wait maximum 5 seconds
        result = await asyncio.wait_for(slow_operation(), timeout=5)
        print(result)
    except asyncio.TimeoutError:
        print("Operation timed out")

asyncio.run(main())
```

## Memory Management with Asyncio

### Limiting Concurrent Tasks

Prevent memory exhaustion from too many tasks.

```python
import asyncio

async def process_item(item, semaphore):
    """Process item with limited concurrency."""
    async with semaphore:
        # Only N tasks can run this simultaneously
        print(f"Processing {item}")
        await asyncio.sleep(1)
        print(f"Done with {item}")

async def main():
    items = range(100)

    # Limit to 5 concurrent tasks
    semaphore = asyncio.Semaphore(5)

    tasks = [process_item(item, semaphore) for item in items]
    await asyncio.gather(*tasks)

asyncio.run(main())
```

### Manual Memory Management

```python
import asyncio
import gc

async def memory_intensive_task():
    """Task that allocates lots of memory."""
    while True:
        # Do memory-intensive work
        data = bytearray(10000)
        process_data(data)
        del data  # Explicitly delete

        # Force garbage collection periodically
        gc.collect()

        await asyncio.sleep(1)
```

## Performance Optimization

### Minimize Sleep Time

Shorter sleep times = more responsive, but higher CPU usage.

```python
# High responsiveness (10ms polling)
await asyncio.sleep_ms(10)  # 100 checks/second

# Balanced (50ms polling)
await asyncio.sleep_ms(50)  # 20 checks/second

# Low power (200ms polling)
await asyncio.sleep_ms(200)  # 5 checks/second
```

### Batch Operations

Group operations to reduce task switching overhead.

```python
async def batched_updates(items):
    """Process items in batches."""
    batch_size = 10

    for i in range(0, len(items), batch_size):
        batch = items[i:i+batch_size]

        # Process entire batch
        for item in batch:
            process(item)

        # Yield to other tasks after batch
        await asyncio.sleep_ms(0)
```

## Debugging Asyncio

### Task Monitoring

```python
import asyncio

async def monitor_tasks():
    """Monitor active tasks."""
    while True:
        tasks = asyncio.all_tasks()
        print(f"Active tasks: {len(tasks)}")
        for task in tasks:
            print(f"  - {task.get_name()}: {task.done()}")

        await asyncio.sleep(5)

# Name your tasks for easier debugging
task = asyncio.create_task(my_coroutine(), name="my_task")
```

### Exception Handling

```python
async def risky_task():
    """Task that might raise exceptions."""
    try:
        await some_operation()
    except Exception as e:
        print(f"Error in risky_task: {e}")
        # Log error, set error state, etc.
        # Don't let exception crash entire event loop

async def main():
    # Gather with return_exceptions to prevent one failure from cancelling all
    results = await asyncio.gather(
        risky_task(),
        another_task(),
        return_exceptions=True
    )

    # Check for exceptions in results
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {i} failed: {result}")
```

## Best Practices for RP2350

1. **Keep coroutines small** - Easier to reason about and debug
2. **Avoid blocking operations** - Use `await` instead of `time.sleep()`
3. **Handle exceptions** - Don't let one task crash the event loop
4. **Monitor memory** - Call `gc.collect()` periodically in long-running tasks
5. **Use appropriate sleep times** - Balance responsiveness vs CPU usage
6. **Name your tasks** - Makes debugging much easier
7. **Clean up resources** - Cancel tasks and close connections on shutdown

## Complete Example: Presto Timer Application

```python
import asyncio
from touch_handler import TouchHandler, GestureDetector
from ble_gatt_server import BLETimerServer
from mqtt_client import ReliableMQTTClient, WiFiManager
from rgb_backlight import RGBBacklight, PresetColors


class TimerState:
    def __init__(self):
        self.remaining = 0
        self.total = 0
        self.running = False


async def touch_ui_task(touch, gesture, state, rgb):
    """Handle touch input."""
    while True:
        event = touch.poll()

        if event:
            if event.type == TouchHandler.TOUCH_DOWN:
                gesture.start(event.x, event.y)

            elif event.type == TouchHandler.TOUCH_UP:
                detected = gesture.end(event.x, event.y)

                if detected == GestureDetector.TAP:
                    # Toggle timer
                    state.running = not state.running
                    color = PresetColors.FOCUS_BLUE if state.running else PresetColors.PAUSED_AMBER
                    rgb.fade_to(*color, duration_ms=300)

        await asyncio.sleep_ms(10)


async def timer_countdown_task(state):
    """Timer countdown logic."""
    while True:
        if state.running and state.remaining > 0:
            state.remaining -= 1

        await asyncio.sleep(1)


async def backlight_task(state, rgb):
    """Update backlight based on timer state."""
    while True:
        if state.running and state.total > 0:
            r, g, b = rgb.urgency_gradient(state.remaining, state.total)
            rgb.fade_to(r, g, b, duration_ms=500)

        await asyncio.sleep(5)


async def ble_sync_task(ble, state):
    """Sync state with BLE clients."""
    while True:
        ble.update_timer_state(state.remaining, state.running)
        await asyncio.sleep_ms(500)


async def mqtt_task(mqtt, state):
    """Maintain MQTT connection."""
    while True:
        mqtt.check_msg()

        if not mqtt.is_connected():
            mqtt.connect()

        # Publish state
        mqtt.publish(
            "productivity/timer/state",
            f'{{"remaining": {state.remaining}, "running": {state.running}}}'
        )

        await asyncio.sleep(1)


async def main():
    # Initialize hardware
    touch = TouchHandler(touch_device)
    gesture = GestureDetector()
    rgb = RGBBacklight(16, 17, 18)
    ble = BLETimerServer("Presto-Timer")
    wifi = WiFiManager("SSID", "password")
    mqtt = ReliableMQTTClient("presto-001", "192.168.1.100")

    # Connect WiFi
    wifi.connect()

    # Start BLE advertising
    ble.start_advertising()

    # Application state
    state = TimerState()
    state.total = 1500
    state.remaining = 1500

    # Run all tasks concurrently
    await asyncio.gather(
        touch_ui_task(touch, gesture, state, rgb),
        timer_countdown_task(state),
        backlight_task(state, rgb),
        ble_sync_task(ble, state),
        mqtt_task(mqtt, state)
    )


# Run application
asyncio.run(main())
```

This example demonstrates a complete async application architecture for the Presto, handling touch input, timer logic, visual feedback, BLE synchronization, and MQTT communication all concurrently without blocking.
