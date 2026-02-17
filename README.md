# MQTT_OSI_Layer_Demonstration_-Dockerized-
This project demonstrates how MQTT communication maps to the OSI model layers (Layer 7 to Layer 3) using a fully containerized setup with Docker and Docker Compose.  
It provides a hands-on visualization of how application-layer data flows through presentation, session, transport, and network layers in a real MQTT-based system.
---
## 🚀 Project Overview
The system consists of three services running as Docker containers:
- **MQTT Publisher (Python + paho-mqtt)**  
  Takes user input at the Application layer and publishes messages to an MQTT topic.
- **MQTT Broker (Eclipse Mosquitto)**  
  Acts as the message broker, handling MQTT sessions and routing messages.
- **MQTT Subscriber (Python + paho-mqtt)**  
  Subscribes to the topic and displays received messages along with OSI layer-wise logs.
This setup helps in understanding:
- How MQTT works at the **Application layer (L7)**
- How data is encoded at the **Presentation layer (L6)**
- How sessions are established using **MQTT CONNECT/CONNACK (L5)**
- How data is transported over **TCP (L4)**
- How packets are routed using **IP networking (L3)** inside a Docker virtual network
> Physical (L1) and Data Link (L2) layers are abstracted by Docker networking and are not explicitly demonstrated.
---
## 🧩 Architecture
[ Python MQTT Publisher ] ---> [ MQTT Broker (Mosquitto) ] ---> [ Python MQTT Subscriber ]
All services communicate over a Docker bridge network.
---
## 📂 Project Structure
mqtt_osi_docker/
│
├── docker-compose.yml
│
├── publisher/
│ ├── Dockerfile
│ └── publisher_layers_detailed.py
│
└── subscriber/
├── Dockerfile
└── subscriber_layers_detailed.py


---
## ⚙️ Prerequisites
- Docker Desktop installed  
- Docker Compose (comes with Docker Desktop)  
- Windows / Linux / macOS host system
---
## ▶️ How to Run
1. Clone this repository:
   ```bash
   git clone <your-github-repo-url>
   cd mqtt_osi_docker
Build and start all services:
docker compose up -d --build

Open subscriber logs (to see received messages):
docker logs -f mqtt-subscriber

Open publisher interactively and send messages:
docker exec -it mqtt-publisher sh
python publisher_layers_detailed.py

Type messages when prompted:
Hello from OSI demo

OSI Layer Mapping

| OSI Layer         | How it is Demonstrated                     |
| ----------------- | ------------------------------------------ |
| L7 – Application  | MQTT publish/subscribe using Python        |
| L6 – Presentation | UTF-8 encoding/decoding of message payload |
| L5 – Session      | MQTT CONNECT / CONNACK, KeepAlive          |
| L4 – Transport    | TCP communication on port 1883             |
| L3 – Network      | IP routing over Docker bridge network      |
| L2 – Data Link    | Abstracted by Docker networking            |
| L1 – Physical     | Abstracted by host hardware                |

🐳 Docker Images
This project builds custom Docker images for:
MQTT Publisher
MQTT Subscriber
Docker Hub links (to be added later by the author):
🔗 Docker Hub Publisher Image: < https://hub.docker.com/repository/docker/suhas6/mqtt-osi-publisher/general >
🔗 Docker Hub Subscriber Image: < https://hub.docker.com/repository/docker/suhas6/mqtt-osi-subscriber/general >

🛠️ Technologies Used
Python
paho-mqtt
Eclipse Mosquitto
Docker & Docker Compose
TCP/IP Networking

🎓 Learning Outcomes
Hands-on understanding of MQTT protocol
Practical mapping of OSI layers in a real communication system
Experience with Dockerized microservices
Debugging and observing network communication flows

Author
Suhas R Hatti
