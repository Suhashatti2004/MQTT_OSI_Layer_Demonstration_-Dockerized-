FROM python:3.10-slim
WORKDIR /app
RUN pip install paho-mqtt
COPY . .
CMD ["python", "subscriber_layers_detailed.py"]
