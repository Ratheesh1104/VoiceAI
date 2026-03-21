import requests

LLM_URL = "http://llm-service:8002//intent"

async def detect_intent(text):

    r = requests.post(
        LLM_URL,
        json={"text":text}
    )

    return r.json()["text"]