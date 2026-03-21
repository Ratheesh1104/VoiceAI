import requests

ACTION_URL = "http://action-service:8003/execute"

async def execute_action(intent):

    r = requests.post(
        ACTION_URL,
        json={"intent": intent}
    )

    return r.json()["result"]