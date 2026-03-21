from app.services.stt_client import transcribe
from app.services.llm_client import detect_intent
from app.services.memory_client import store_memory
from app.services.action_client import execute_action
from app.services.tts_client import synthesize


async def process_voice(audio_file):
    text = await transcribe(audio_file)

    await store_memory(text)

    intent = await detect_intent(text)

    result = await execute_action(intent)

    await store_memory("session1",result)

    audio = await synthesize(result)

    return {
        "text": text,
        "intent": intent,
        "result": result,
        "audio": audio
    }