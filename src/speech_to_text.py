import os
import httpx
from fastapi import HTTPException

async def transcribe_audio_sarvam(audio_bytes: bytes, filename: str) -> str:
    api_key = os.getenv("sk_n784q1fm_QZDiVxwTj4ltnlk6lagIFbg2")
    if not api_key:
        raise HTTPException(status_code=500, detail="Missing SARVAM_API_KEY env variable.")
        
    url = "https://sarvam.ai"
    headers = {"api-subscription-key": api_key}
    files = {"file": (filename, audio_bytes, "audio/wav")}
    data = {"model": "saaras:v4"}
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, files=files, data=data, timeout=8.0)
            if response.status_code != 200:
                return ""
            return response.json().get("transcript", "").strip()
        except Exception:
            return ""

