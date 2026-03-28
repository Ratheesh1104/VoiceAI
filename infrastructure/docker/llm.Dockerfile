FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# ✅ Install curl (required for your script)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY services/llm-service/ .

# ✅ Make script executable
RUN chmod +x /app/wait-for-ollama.sh

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8002"]