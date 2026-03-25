import requests
import json
from prompt_template import SYSTEM_PROMPT

OLLAMA_URL = "http://ollama:11434"

def process_text(user_text):
    prompt = SYSTEM_PROMPT + f"\n\nUser: {user_text}"

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3"
            "prompt": prompt
            "stream": False
        }
    )

    result = response.json()["response"]

    try:
        return json.loads(result)
    except:
        return {
            "intent": "unknown",
            "entities": {},
            "action": "none",
            "response": result
        }