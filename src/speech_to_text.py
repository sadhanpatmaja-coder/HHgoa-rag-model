import httpx
import os

async def transcribe_audio(audio_bytes: bytes) -> str:
    url = "https://sarvam.ai"
    headers = {"api-subscription-key": os.getenv("sk_n784q1fm_QZDiVxwTj4ltnlk6lagIFbg2")}
    files = {"file": ("input.wav", audio_bytes, "audio/wav")}
    data = {"model": "saaras:v4"}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, files=files, data=data, timeout=5.0)
        return response.json().get("transcript", "").strip()
