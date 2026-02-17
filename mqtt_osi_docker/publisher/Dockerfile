FROM python:3.10-slim
WORKDIR /app
RUN pip install paho-mqtt
COPY . .
CMD ["python", "publisher_layers_detailed.py"]
