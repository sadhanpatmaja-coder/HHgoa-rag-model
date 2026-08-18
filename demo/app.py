import time
import numpy as np
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse

app = FastAPI()
latencies = []

@app.post("/v1/voice-rag")
async def voice_rag(file: UploadFile = File(...)):
    start_time = time.perf_counter()
    audio_bytes = await file.read()
    
    text = await transcribe_audio(audio_bytes)
   
    if "unsafe" in text.lower():
        return {"error": "Guardrail triggered"}
        
 
    context = await retrieve_context(query_vector=[0.1]*384) 
    
 
    duration = (time.perf_counter() - start_time) * 1000
    latencies.append(duration)
    
    return {"text": text, "context": context, "latency_ms": duration}
