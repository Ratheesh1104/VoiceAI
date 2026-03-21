import requests

TTS_URL = "http://tts-service:8004/speak"

async def synthesize(text):

    r = requests.post(
        TTS_URL,
        json={"text": text}
    )

    return r.json()["audio"]