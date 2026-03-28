FROM ollama/ollama:latest

RUN apt-get update && apt-get install -y curl

# your existing model preload
RUN ollama serve & \
    sleep 5 && \
    ollama pull llama3

EXPOSE 11434

ENTRYPOINT ["ollama", "serve"]

HEALTHCHECK --interval=10s --timeout=5s --start-period=40s --retries=10 \
  CMD curl -f http://localhost:11434/ || exit 1