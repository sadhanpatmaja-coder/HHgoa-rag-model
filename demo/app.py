import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.pipeline import run_voice_rag_pipeline, get_latency_stats

load_dotenv()

app = FastAPI(title="HH Goa Voice-RAG Service Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/voice-rag")
async def voice_rag_endpoint(file: UploadFile = File(...)):
    audio_content = await file.read()
    return StreamingResponse(
        run_voice_rag_pipeline(audio_content, file.filename),
        media_type="text/plain; charset=utf-8"
    )

@app.get("/api/analytics")
async def analytics_endpoint():
    return JSONResponse(content=get_latency_stats())

