"""
MQTT Client with Auto-Reconnection for RP2350
Provides robust MQTT client with automatic reconnection and offline queueing
"""

import time
import network
from umqtt.simple import MQTTClient
from umqtt.robust import MQTTClient as RobustMQTTClient


class ReliableMQTTClient:
    """
    MQTT client with automatic reconnection and message queueing.

    Usage:
        def message_callback(topic, msg):
            print(f"Received: {topic} -> {msg}")

        mqtt = ReliableMQTTClient(
            client_id="presto-001",
            broker="192.168.1.100",
            callback=message_callback
        )

        mqtt.connect()
        mqtt.subscribe("productivity/timer/control/#")

        while True:
            mqtt.publish("productivity/status", "running")
            mqtt.check_msg()  # Check for incoming messages
            time.sleep(1)
    """

    def __init__(
        self,
        client_id,
        broker,
        port=1883,
        user=None,
        password=None,
        callback=None,
        keepalive=60,
    ):
        """
        Initialize MQTT client.

        Args:
            client_id: Unique client identifier
            broker: MQTT broker hostname/IP
            port: Broker port (default: 1883)
            user: Username (optional)
            password: Password (optional)
            callback: Message callback function(topic, msg)
            keepalive: Keepalive interval in seconds
        """
        self.client_id = client_id
        self.broker = broker
        self.port = port
        self.user = user
        self.password = password
        self.callback = callback
        self.keepalive = keepalive

        self._client = None
        self._connected = False
        self._subscriptions = []
        self._message_queue = []
        self._max_queue_size = 100
        self._last_ping = 0
        self._reconnect_delay = 5

    def connect(self):
        """
        Connect to MQTT broker.

        Returns:
            True if successful, False otherwise
        """
        try:
            # Create client instance
            self._client = RobustMQTTClient(
                self.client_id,
                self.broker,
                port=self.port,
                user=self.user,
                password=self.password,
                keepalive=self.keepalive,
            )

            if self.callback:
                self._client.set_callback(self.callback)

            # Connect
            self._client.connect()
            self._connected = True
            self._last_ping = time.time()

            print(f"MQTT: Connected to {self.broker}:{self.port}")

            # Resubscribe to topics
            for topic in self._subscriptions:
                self._client.subscribe(topic)
                print(f"MQTT: Subscribed to {topic}")

            # Send queued messages
            self._flush_queue()

            return True

        except Exception as e:
            print(f"MQTT: Connection failed: {e}")
            self._connected = False
            return False

    def disconnect(self):
        """Disconnect from broker."""
        if self._client and self._connected:
            try:
                self._client.disconnect()
            except:
                pass
        self._connected = False
        print("MQTT: Disconnected")

    def is_connected(self):
        """Check connection status."""
        return self._connected

    def subscribe(self, topic, qos=0):
        """
        Subscribe to topic.

        Args:
            topic: Topic to subscribe (supports wildcards)
            qos: Quality of Service (0 or 1)
        """
        if topic not in self._subscriptions:
            self._subscriptions.append(topic)

        if self._connected and self._client:
            try:
                self._client.subscribe(topic, qos)
                print(f"MQTT: Subscribed to {topic}")
            except Exception as e:
                print(f"MQTT: Subscribe failed: {e}")
                self._connected = False

    def publish(self, topic, message, qos=0, retain=False):
        """
        Publish message to topic.

        Args:
            topic: Topic to publish to
            message: Message payload (string or bytes)
            qos: Quality of Service (0 or 1)
            retain: Retain message on broker
        """
        if isinstance(message, str):
            message = message.encode()

        if self._connected and self._client:
            try:
                self._client.publish(topic, message, retain=retain, qos=qos)
                return True
            except Exception as e:
                print(f"MQTT: Publish failed: {e}")
                self._connected = False

        # Queue message if not connected
        if len(self._message_queue) < self._max_queue_size:
            self._message_queue.append((topic, message, qos, retain))
            print(f"MQTT: Message queued ({len(self._message_queue)} pending)")
        else:
            print("MQTT: Queue full, message dropped")

        return False

    def check_msg(self):
        """
        Check for incoming messages (non-blocking).
        Call this regularly in main loop.
        """
        if not self._connected:
            # Attempt reconnection
            if time.time() - self._last_ping > self._reconnect_delay:
                print("MQTT: Attempting reconnection...")
                self.connect()
            return

        try:
            self._client.check_msg()

            # Send ping if keepalive interval approaching
            current_time = time.time()
            if current_time - self._last_ping > self.keepalive / 2:
                self._client.ping()
                self._last_ping = current_time

        except Exception as e:
            print(f"MQTT: Error checking messages: {e}")
            self._connected = False

    def _flush_queue(self):
        """Send all queued messages."""
        while self._message_queue and self._connected:
            topic, message, qos, retain = self._message_queue.pop(0)
            try:
                self._client.publish(topic, message, retain=retain, qos=qos)
                print(f"MQTT: Sent queued message to {topic}")
            except Exception as e:
                print(f"MQTT: Failed to send queued message: {e}")
                # Re-queue the message
                self._message_queue.insert(0, (topic, message, qos, retain))
                self._connected = False
                break


class WiFiManager:
    """
    WiFi connection manager with auto-reconnect.

    Usage:
        wifi = WiFiManager("MySSID", "MyPassword")
        wifi.connect()

        while True:
            if not wifi.is_connected():
                wifi.reconnect()
            time.sleep(10)
    """

    def __init__(self, ssid, password, hostname=None):
        """
        Initialize WiFi manager.

        Args:
            ssid: Network SSID
            password: Network password
            hostname: Device hostname (optional)
        """
        self.ssid = ssid
        self.password = password
        self.hostname = hostname
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self, timeout=10):
        """
        Connect to WiFi network.

        Args:
            timeout: Connection timeout in seconds

        Returns:
            True if connected, False otherwise
        """
        self.wlan.active(True)

        if self.hostname:
            self.wlan.config(dhcp_hostname=self.hostname)

        if not self.wlan.isconnected():
            print(f"WiFi: Connecting to {self.ssid}...")
            self.wlan.connect(self.ssid, self.password)

            # Wait for connection
            start_time = time.time()
            while not self.wlan.isconnected():
                if time.time() - start_time > timeout:
                    print("WiFi: Connection timeout")
                    return False
                time.sleep(0.5)

        print(f"WiFi: Connected - {self.wlan.ifconfig()[0]}")
        return True

    def disconnect(self):
        """Disconnect from WiFi."""
        self.wlan.disconnect()
        self.wlan.active(False)
        print("WiFi: Disconnected")

    def is_connected(self):
        """Check WiFi connection status."""
        return self.wlan.isconnected()

    def reconnect(self):
        """Attempt to reconnect."""
        if not self.is_connected():
            print("WiFi: Attempting reconnection...")
            return self.connect()
        return True

    def get_ip(self):
        """Get current IP address."""
        if self.is_connected():
            return self.wlan.ifconfig()[0]
        return None

    def get_signal_strength(self):
        """
        Get WiFi signal strength (RSSI).

        Returns:
            RSSI in dBm (negative value, closer to 0 is better)
        """
        try:
            return self.wlan.status('rssi')
        except:
            return None
