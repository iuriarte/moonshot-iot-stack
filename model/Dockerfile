FROM pytorch/pytorch:latest

RUN pip install flask onnxruntime

WORKDIR /app

COPY . /app

ENV MODEL_PATH=/app/model.onnx

CMD ["python3", "model_server.py"]

