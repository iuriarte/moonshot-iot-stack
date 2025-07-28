# Updated version to fix indentation issue
from flask import Flask, request, jsonify
import onnxruntime as ort
import numpy as np
import os

app = Flask(__name__)

# Root route
@app.route("/")
def index():
    return jsonify({
        "status": "ok",
        "message": "Welcome to the ONNX Model API",
        "routes": ["/healthcheck", "/readycheck", "/infer"]
    })

# Load model
MODEL_PATH = os.getenv("MODEL_PATH", "model/model.onnx")
try:
    session = ort.InferenceSession(MODEL_PATH)
    input_name = session.get_inputs()[0].name
except Exception as e:
    session = None
    input_name = None
    print(f"Error loading model: {e}")

# Healthcheck
@app.route("/healthcheck")
def healthcheck():
    if session:
        return jsonify({"status": "ok", "model_path": MODEL_PATH}), 200
    else:
        return jsonify({"status": "error", "message": "Model not loaded"}), 500

# Readycheck
@app.route("/readycheck")
def readycheck():
    return "Ready", 200

# Inference route
@app.route("/infer", methods=["POST"])
def infer():
    if not session:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.get_json()
    if not data or "inputs" not in data:
        return jsonify({"error": "Missing 'inputs' in request"}), 400

    try:
        inputs = np.array(data["inputs"], dtype=np.float32)
        result = session.run(None, {input_name: inputs})
        return jsonify({"result": result[0].tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
