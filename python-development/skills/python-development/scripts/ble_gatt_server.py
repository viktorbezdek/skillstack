"""
BLE GATT Server Implementation for RP2350
Provides reusable BLE peripheral server with custom services
"""

import bluetooth
import struct
import time
from micropython import const

# BLE Events
_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE = const(3)
_IRQ_GATTS_READ_REQUEST = const(4)

# BLE Appearance values
_ADV_APPEARANCE_GENERIC_COMPUTER = const(128)

# Common Service and Characteristic UUIDs
# Timer Service (custom)
_TIMER_SERVICE_UUID = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef0")
_TIMER_STATE_CHAR = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef1")
_TIMER_CONTROL_CHAR = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef2")

# Battery Service (standard)
_BATTERY_SERVICE_UUID = bluetooth.UUID(0x180F)
_BATTERY_LEVEL_CHAR = bluetooth.UUID(0x2A19)


class BLETimerServer:
    """
    BLE GATT server for timer control and state synchronization.

    Usage:
        ble_server = BLETimerServer("Presto-Timer")
        ble_server.start_advertising()

        while True:
            # Update timer state
            ble_server.update_timer_state(remaining_seconds, is_running)

            # Check for control commands
            command = ble_server.get_command()
            if command:
                handle_command(command)

            time.sleep(0.1)
    """

    def __init__(self, name="RP2350-Device"):
        """
        Initialize BLE GATT server.

        Args:
            name: Device name for advertising
        """
        self._ble = bluetooth.BLE()
        self._ble.active(True)
        self._ble.irq(self._irq_handler)

        self._name = name
        self._connections = set()
        self._command_queue = []

        # Register services
        self._register_services()

        print(f"BLE GATT Server initialized: {name}")

    def _register_services(self):
        """Register GATT services and characteristics."""

        # Timer Service
        timer_state = (
            _TIMER_STATE_CHAR,
            bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY,
        )
        timer_control = (
            _TIMER_CONTROL_CHAR,
            bluetooth.FLAG_WRITE,
        )

        timer_service = (
            _TIMER_SERVICE_UUID,
            (timer_state, timer_control),
        )

        # Battery Service
        battery_level = (
            _BATTERY_LEVEL_CHAR,
            bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY,
        )

        battery_service = (
            _BATTERY_SERVICE_UUID,
            (battery_level,),
        )

        # Register all services
        services = (timer_service, battery_service)
        ((self._timer_state_handle, self._timer_control_handle),
         (self._battery_handle,)) = self._ble.gatts_register_services(services)

        # Initialize values
        self._ble.gatts_write(self._timer_state_handle, struct.pack("<IB", 0, 0))
        self._ble.gatts_write(self._battery_handle, struct.pack("<B", 100))

    def _irq_handler(self, event, data):
        """Handle BLE events."""

        if event == _IRQ_CENTRAL_CONNECT:
            conn_handle, _, _ = data
            self._connections.add(conn_handle)
            print(f"BLE: Central connected (handle: {conn_handle})")

        elif event == _IRQ_CENTRAL_DISCONNECT:
            conn_handle, _, _ = data
            self._connections.discard(conn_handle)
            print(f"BLE: Central disconnected (handle: {conn_handle})")
            # Resume advertising
            self.start_advertising()

        elif event == _IRQ_GATTS_WRITE:
            conn_handle, attr_handle = data
            if attr_handle == self._timer_control_handle:
                # Read the command
                command_data = self._ble.gatts_read(self._timer_control_handle)
                self._handle_timer_command(command_data)

    def _handle_timer_command(self, data):
        """Parse and queue timer control commands."""
        if len(data) >= 1:
            command = data[0]
            self._command_queue.append(command)

    def start_advertising(self):
        """Start BLE advertising."""
        # Payload: Flags, Name
        payload = bytearray()

        # Flags
        payload.extend(b'\x02\x01\x06')  # General discoverable, BR/EDR not supported

        # Complete name
        name_bytes = self._name.encode()
        payload.extend(struct.pack('BB', len(name_bytes) + 1, 0x09))
        payload.extend(name_bytes)

        # Appearance
        payload.extend(b'\x03\x19')
        payload.extend(struct.pack('<H', _ADV_APPEARANCE_GENERIC_COMPUTER))

        self._ble.gap_advertise(100000, payload)  # Advertise every 100ms
        print("BLE: Advertising started")

    def stop_advertising(self):
        """Stop BLE advertising."""
        self._ble.gap_advertise(None)
        print("BLE: Advertising stopped")

    def update_timer_state(self, remaining_seconds, is_running):
        """
        Update timer state and notify connected clients.

        Args:
            remaining_seconds: Time remaining (0-4294967295)
            is_running: Boolean indicating if timer is running
        """
        # Pack state: 4 bytes for seconds, 1 byte for running flag
        state_data = struct.pack("<IB", remaining_seconds, 1 if is_running else 0)

        # Update characteristic value
        self._ble.gatts_write(self._timer_state_handle, state_data)

        # Notify all connected clients
        for conn_handle in self._connections:
            try:
                self._ble.gatts_notify(conn_handle, self._timer_state_handle)
            except OSError:
                pass  # Client may have disconnected

    def update_battery_level(self, percentage):
        """
        Update battery level.

        Args:
            percentage: Battery level (0-100)
        """
        data = struct.pack("<B", max(0, min(100, percentage)))
        self._ble.gatts_write(self._battery_handle, data)

        # Notify connected clients
        for conn_handle in self._connections:
            try:
                self._ble.gatts_notify(conn_handle, self._battery_handle)
            except OSError:
                pass

    def get_command(self):
        """
        Get next command from queue.

        Returns:
            Command byte (0=stop, 1=start, 2=pause, 3=reset) or None
        """
        if self._command_queue:
            return self._command_queue.pop(0)
        return None

    def is_connected(self):
        """Check if any clients are connected."""
        return len(self._connections) > 0

    def disconnect_all(self):
        """Disconnect all clients."""
        for conn_handle in list(self._connections):
            try:
                self._ble.gap_disconnect(conn_handle)
            except OSError:
                pass
        self._connections.clear()


# Command constants for timer control
TIMER_CMD_STOP = 0
TIMER_CMD_START = 1
TIMER_CMD_PAUSE = 2
TIMER_CMD_RESET = 3
