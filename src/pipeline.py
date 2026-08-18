
import time
import numpy as np
from src.speech_to_text import transcribe_audio_sarvam
from src.guardrails import check_input_guardrails
from src.retriever import retrieve_context
from src.generator import stream_llm_tokens

pipeline_latencies = []

async def run_voice_rag_pipeline(audio_bytes: bytes, filename: str):
    start_time = time.perf_counter()
    

    query = await transcribe_audio_sarvam(audio_bytes, filename)
    if not query:
        yield "Pipeline Error: Transcription failed or returned empty payload.\n"
        return
        
    yield f"🗣️ [Query]: {query}\n\n"
    
   
    if not check_input_guardrails(query):
        yield "🛡️ Guardrail Triggered: Request blocked due to unsafe content or out-of-domain alignment.\n"
        return
        
  
    context = await retrieve_context(query)
  
    yield "🤖 [Answer]: "
    async for token in stream_llm_tokens(query, context):
        yield token
        

    duration_ms = (time.perf_counter() - start_time) * 1000
    pipeline_latencies.append(duration_ms)
    
    yield f"\n\n⏱️ [Pipeline Latency]: {duration_ms:.2f} ms\n"

def get_latency_stats():
    if not pipeline_latencies:
        return {"status": "No queries executed yet."}
    return {
        "runs": len(pipeline_latencies),
        "P50": f"{float(np.percentile(pipeline_latencies, 50)):.2f} ms",
        "P70": f"{float(np.percentile(pipeline_latencies, 70)):.2f} ms",
        "P100": f"{float(np.max(pipeline_latencies)):.2f} ms"
    }
