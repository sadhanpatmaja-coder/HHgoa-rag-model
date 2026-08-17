import requests

def transcribe(audio_file_path):
   
    with open(audio_file_path, "rb") as f:
        response = requests.post("https://api.sarvam.ai/stt", files={"file": f})
    return response.json().get("text", "")
