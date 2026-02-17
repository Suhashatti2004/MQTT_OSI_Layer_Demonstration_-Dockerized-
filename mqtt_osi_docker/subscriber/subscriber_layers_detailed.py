import paho.mqtt.client as mqtt
import socket

BROKER = "broker"
PORT = 1883
TOPIC = "osi/layers/demo"

print("========== MQTT OSI LAYER DEMO : SUBSCRIBER ==========")

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

# -------- L5: Session Layer --------
def on_connect(client, userdata, flags, rc):
    print("\n[L5 - Session]")
    print("  MQTT CONNECT sent")
    print("  CONNACK rc      :", rc)
    print("  KeepAlive       : 60s")
    print("  Clean Session   : True")
    client.subscribe(TOPIC)
    print("  Subscribed Topic:", TOPIC)

# -------- L7 & L6: Receive --------
def on_message(client, userdata, msg):
    print("\n[L7 - Application]")
    print("  MQTT Control    : PUBLISH (Received)")
    print("  Topic           :", msg.topic)
    print("  QoS             :", msg.qos)

    print("\n[L6 - Presentation]")
    decoded = msg.payload.decode("utf-8")
    print("  Decoding        : UTF-8")
    print("  Raw Bytes       :", msg.payload)
    print("  Decoded Payload :", decoded)

client = mqtt.Client(client_id="osi_subscriber", clean_session=True)
client.on_connect = on_connect
client.on_message = on_message

print("\n[L7 - Application] Connecting to broker...")
client.connect(BROKER, PORT, keepalive=60)
client.loop_forever()
