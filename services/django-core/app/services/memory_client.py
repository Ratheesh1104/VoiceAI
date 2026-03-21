import requests

MEMORY_URL = "http://memory-service:8005/store"

async def store_memory(session_id, message):

    requests.post(
        MEMORY_URL,
        json={
            "session_id": session_id,
            "message": message
        }
    )