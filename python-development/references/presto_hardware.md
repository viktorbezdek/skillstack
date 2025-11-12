# Pimoroni Presto Hardware Reference

## Overview

The Pimoroni Presto is a development board featuring the RP2350 microcontroller with integrated display, touch input, and RGB backlight.

## RP2350 Specifications

### Processor
- **CPU**: Dual ARM Cortex-M33 cores @ 150MHz
- **RAM**: 520KB SRAM
- **Flash**: 4MB (board-dependent)
- **Architecture**: ARMv8-M with TrustZone

### Key Features
- Dual-core processing
- Hardware floating-point
- Enhanced security features
- USB 1.1 host/device
- DMA controller
- PIO (Programmable I/O) - 4 state machines per PIO block

## Presto-Specific Hardware

### Display
- **Type**: IPS LCD
- **Resolution**: 480x480 pixels (typical)
- **Interface**: SPI or parallel
- **Controller**: ST7789 or similar
- **Color**: 16-bit RGB565

### Touch Controller
- **Type**: Capacitive touch
- **Interface**: I2C
- **Controller**: CST816S or FT6236 (board-dependent)
- **Resolution**: 480x480 touch points
- **Max Touch Points**: 1-2 simultaneous

### RGB Backlight
- **Type**: Common cathode RGB LED
- **Control**: 3x PWM channels
- **Pins**:
  - Red: GPIO 16 (example - check your specific board)
  - Green: GPIO 17
  - Blue: GPIO 18

### Buttons
- **USER Button**: GPIO 23 (example - verify with schematic)
- **BOOT Button**: GPIO 24 (for bootloader entry)

## GPIO Pinout (Typical Presto Configuration)

| Pin | Function | Usage |
|-----|----------|-------|
| GP0-GP7 | General GPIO | Available for user applications |
| GP8 | Display DC | Display data/command select |
| GP9 | Display CS | Display chip select |
| GP10 | Display SCK | SPI clock |
| GP11 | Display MOSI | SPI data out |
| GP12 | Display RST | Display reset |
| GP13 | Display BL | Backlight enable (on/off) |
| GP14 | I2C SDA | Touch controller data |
| GP15 | I2C SCL | Touch controller clock |
| GP16 | RGB Red | PWM for red backlight |
| GP17 | RGB Green | PWM for green backlight |
| GP18 | RGB Blue | PWM for blue backlight |
| GP23 | Button | User button (active low) |

**Note**: Pin assignments may vary. Always verify with your specific board's schematic.

## Display Interface Details

### SPI Configuration for ST7789
```python
import machine
from machine import Pin, SPI

# SPI setup for display
spi = SPI(
    1,
    baudrate=62_500_000,  # 62.5 MHz (max for ST7789)
    polarity=0,
    phase=0,
    sck=Pin(10),
    mosi=Pin(11)
)

dc_pin = Pin(8, Pin.OUT)   # Data/Command
cs_pin = Pin(9, Pin.OUT)   # Chip Select
rst_pin = Pin(12, Pin.OUT) # Reset
```

### Display Commands (ST7789)
- `0x01`: Software Reset
- `0x11`: Sleep Out
- `0x29`: Display On
- `0x2A`: Column Address Set
- `0x2B`: Row Address Set
- `0x2C`: Memory Write
- `0x3A`: Interface Pixel Format (RGB565: 0x55)

## Touch Controller Interface

### I2C Configuration for CST816S
```python
from machine import I2C, Pin

# I2C setup for touch controller
i2c = I2C(
    1,
    scl=Pin(15),
    sda=Pin(14),
    freq=400000  # 400kHz
)

# CST816S I2C address
TOUCH_ADDR = 0x15
```

### Touch Data Registers (CST816S)
- `0x00`: Gesture ID
- `0x01`: Number of touch points
- `0x02`: Event flag
- `0x03-0x04`: X coordinate (high/low)
- `0x05-0x06`: Y coordinate (high/low)

### Reading Touch Data
```python
def read_touch(i2c):
    """Read touch coordinates from CST816S."""
    try:
        data = i2c.readfrom_mem(TOUCH_ADDR, 0x02, 6)

        # Parse coordinates (adjust for display orientation)
        x = ((data[1] & 0x0F) << 8) | data[2]
        y = ((data[3] & 0x0F) << 8) | data[4]

        # Check if touched
        touched = data[0] != 0

        return touched, x, y
    except:
        return False, 0, 0
```

## Power Consumption

### Typical Power Draw
- **Active (Display on, WiFi active)**: ~200-300mA @ 5V
- **Active (Display on, WiFi idle)**: ~150-200mA @ 5V
- **Low power (Display dimmed)**: ~50-100mA @ 5V
- **Sleep mode**: <5mA @ 5V

### Power Optimization Tips
1. Dim or turn off backlight when idle
2. Reduce display update frequency
3. Use WiFi sleep modes
4. Disable unused peripherals
5. Lower CPU frequency for non-critical tasks

## Memory Considerations

### RP2350 Memory Layout
- **RAM**: 520KB total
  - ~50-100KB used by MicroPython runtime
  - ~400KB available for application
- **Flash**: 4MB
  - ~500KB MicroPython firmware
  - ~3.5MB available for code/data

### Framebuffer Memory
For 480x480 RGB565 display:
- Full framebuffer: 480 × 480 × 2 bytes = 460,800 bytes (~450KB)
- **Problem**: Nearly uses all available RAM
- **Solutions**:
  1. Use partial display updates
  2. Tile-based rendering (render small sections)
  3. Single color depth (1-bit for simple graphics)
  4. External PSRAM (if available on your board)

### Memory Management Tips
```python
import gc

# Manual garbage collection
gc.collect()
print(f"Free memory: {gc.mem_free()} bytes")

# Monitor memory usage
gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
```

## Peripheral Interfaces

### BLE (Bluetooth Low Energy)
- **Stack**: Built into RP2350 MicroPython firmware
- **Roles**: Central, Peripheral, or both
- **Profiles**: Custom GATT services
- **Range**: ~10-30 meters (open air)

### WiFi
- **Requires**: External WiFi module (e.g., ESP32-C3 on Pico W)
- **Standards**: 802.11 b/g/n
- **Security**: WPA2-PSK, WPA3
- **Protocols**: TCP, UDP, MQTT, HTTP

**Note**: Not all RP2350 boards include WiFi. Verify your board specifications.

## Timing and Real-Time Constraints

### Timer Resources
- **Hardware timers**: 4 available
- **PWM slices**: 16 slices (2 channels each)
- **PIO state machines**: 8 total (4 per PIO block)

### Accurate Timing
```python
import time
from machine import Timer

# Hardware timer for precise intervals
timer = Timer()

def timer_callback(t):
    print("Timer fired!")

# Fire every 1000ms
timer.init(period=1000, mode=Timer.PERIODIC, callback=timer_callback)
```

### Asyncio Timing
```python
import asyncio

async def precise_task():
    """Task with precise timing using asyncio."""
    while True:
        start = time.ticks_ms()

        # Do work here
        print("Task running")

        # Calculate sleep to maintain 1000ms period
        elapsed = time.ticks_diff(time.ticks_ms(), start)
        await asyncio.sleep_ms(max(0, 1000 - elapsed))
```

## Development Tools

### Firmware
- **Official**: [Pimoroni MicroPython builds](https://github.com/pimoroni/pimoroni-pico)
- **Vanilla**: Standard MicroPython (may lack board-specific drivers)

### Upload Tools
- **Thonny**: GUI IDE with integrated REPL
- **rshell**: Command-line file transfer
- **ampy**: Adafruit MicroPython tool
- **mpremote**: Official MicroPython remote control

### Debugging
```python
# Enable debugging output
import micropython
micropython.alloc_emergency_exception_buf(100)

# Stack trace on exceptions
import sys
sys.print_exception(e)
```

## Known Issues and Limitations

1. **Limited RAM**: Full framebuffer barely fits - use partial updates
2. **No floating-point hardware in MicroPython**: Use fixed-point math
3. **I2C reliability**: Add pull-up resistors if experiencing issues
4. **Touch sensitivity**: May need calibration for accurate coordinates
5. **WiFi+BLE**: If using external WiFi, may conflict with BLE (shared radio on some modules)

## Additional Resources

- [RP2350 Datasheet](https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf)
- [MicroPython Documentation](https://docs.micropython.org/)
- [Pimoroni GitHub](https://github.com/pimoroni)
- [ST7789 Display Driver](https://github.com/devbis/st7789_mpy)
