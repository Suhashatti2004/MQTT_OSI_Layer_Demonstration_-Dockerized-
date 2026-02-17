import paho.mqtt.client as mqtt
import socket
import time

BROKER = "broker"   # Docker service name
PORT = 1883
TOPIC = "osi/layers/demo"

print("========== MQTT OSI LAYER DEMO : PUBLISHER ==========")

# -------- L3: Network Layer --------
broker_ip = socket.gethostbyname(BROKER)
local_hostname = socket.gethostname()
local_ip = socket.gethostbyname(local_hostname)

print("\n[L3 - Network]")
print("  Source Hostname :", local_hostname)
print("  Source IP       :", local_ip)
print("  Destination IP  :", broker_ip)
print("  IP Version      : IPv4")

# -------- L4: Transport Layer --------
print("\n[L4 - Transport]")
print("  Protocol        : TCP")
print("  Destination Port:", PORT)

# -------- L5: Session Layer (print once) --------
connected_once = False

def on_connect(client, userdata, flags, reason_code, properties):
    global connected_once
    if not connected_once:
        print("\n[L5 - Session]")
        print("  MQTT CONNECT sent")
        print("  CONNACK rc      :", reason_code)
        print("  KeepAlive       : 60s")
        print("  Clean Session   : True")
        connected_once = True

# -------- L7: Application Layer --------
client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="osi_publisher",
    clean_session=True
)
client.on_connect = on_connect

print("\n[L7 - Application] Connecting to broker...")
client.connect(BROKER, PORT, keepalive=60)
client.loop_start()

try:
    while True:
        user_input = input("\n[L7 - Application] Enter message (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break

        # -------- L6: Presentation Layer --------
        encoded_data = user_input.encode("utf-8")
        print("\n[L6 - Presentation]")
        print("  Encoding        : UTF-8")
        print("  Original Length :", len(user_input), "chars")
        print("  Encoded Length  :", len(encoded_data), "bytes")
        print("  Raw Bytes       :", encoded_data)

        # -------- L7: MQTT Publish --------
        result = client.publish(TOPIC, encoded_data, qos=1, retain=False)
        time.sleep(0.2)

        print("\n[L7 - Application]")
        print("  MQTT Control    : PUBLISH")
        print("  Topic           :", TOPIC)
        print("  Payload         :", user_input)
        print("  QoS             :", 1)
        print("  Message ID      :", result.mid)

except KeyboardInterrupt:
    print("\n[!] Keyboard interrupt received")

print("\n[L5 - Session] Disconnecting MQTT session")
client.disconnect()
client.loop_stop()
print("====================================================")
