FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y docker.io

COPY webhook/webhook_server.py .
COPY agent/analyze.py .
COPY agent/rca.txt .

CMD ["python3", "webhook_server.py"]
