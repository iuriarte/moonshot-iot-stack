# 🌕 Moonshot IoT Stack

**Moonshot IoT Stack** is an end-to-end industrial IoT data pipeline and edge inference platform. It integrates MQTT ingestion, time-series storage, real-time dashboards, and ONNX-based ML inference—all containerized and ready to deploy.

## 🚀 Features

- **Node-RED** for visual data flow orchestration
- **InfluxDB** for time-series storage
- **Grafana** for live dashboards
- **ONNX Model API** for local machine learning inference
- **Mosquitto** MQTT broker for sensor ingestion
- Docker Compose-based for easy deployment

## 🧱 Stack Architecture

```
[Sensor] --> [Mosquitto MQTT] --> [Node-RED] --> [InfluxDB] --> [Grafana]
                                     |
                                  [ONNX Model API (Flask)]
```

## 📦 Requirements

- Docker
- Docker Compose
- Git
- Python 3.8+ (for model development only)

## 🛠️ Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/iuriarte/moonshot-iot-stack.git
   cd moonshot-iot-stack
   ```

2. **Start the stack**
   ```bash
   docker compose up --build
   ```

3. **Access Services**
   - Node-RED: http://localhost:1880
   - Grafana: http://localhost:3000 (admin / admin)
   - InfluxDB: http://localhost:8086
   - ONNX Model API: http://localhost:5001

## 🧪 Inference API Usage

Make a POST request to `/infer` with input data:
```bash
curl -X POST http://localhost:5001/infer \
  -H "Content-Type: application/json" \
  -d '{"inputs": [[0.0, 1.0, 2.0, 3.0, 4.0]]}'
```

Other endpoints:
- `/healthcheck` – check if the model loaded
- `/readycheck` – confirms API is alive

## 🧠 Model Format

Place your ONNX model in:  
```bash
model/model.onnx
```

Update environment variable `MODEL_PATH` if using a different path.

## 🧪 Development Tips

To test just the model API:
```bash
cd model
docker build -t moonshot-modelapi .
docker run -p 5001:5000 moonshot-modelapi
```

Or pull from Docker Hub:
```bash
docker run -p 5000:5000 iuriarte/moonshot-iot-stack:modelapi
```

## 📁 Folder Structure

```
moonshot-iot-stack/
├── model/
│   ├── model.onnx
│   ├── model_server.py
│   └── Dockerfile
├── docker-compose.yml
├── config/
├── data/
└── README.md
```

## 🤝 Contributing

Pull requests are welcome. Please open issues first to discuss changes.

---

## 📄 License

MIT License – see `LICENSE` file for details.
