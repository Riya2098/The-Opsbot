FROM python:3.10-slim

WORKDIR /app

# 1. Copy only requirements first to leverage Docker layer caching
COPY requirements.txt .

# 2. Install dependencies only if requirements.txt changes
RUN pip install --no-cache-dir -r requirements.txt

# 3. Now copy source code
COPY agent/*.py ./
#COPY webhook_server.py .
COPY webhook/webhook_server.py ./webhook_server.py
COPY agent/rca.txt ./
COPY .env .env

CMD ["python3", "webhook_server.py"]
