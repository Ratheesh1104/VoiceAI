#!/bin/bash
set -e
echo "Waiting for Ollama to be ready..."
until curl -s http://ollama:11434 > /dev/null; do
  sleep 4
done
echo "Ollama is ready. Starting LLM service..."
exec "$@"