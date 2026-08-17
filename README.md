# HHgoa-rag-model
*Voice‑Enabled RAG Model (HH Goa 2026 Task 2)*
📌 Overview
This project implements a voice‑enabled Retrieval‑Augmented Generation (RAG) system.
Users speak a question → the pipeline transcribes it → retrieves relevant context from the MSMARCO‑XI dataset → generates an answer.

Pipeline Flow:  
🎤 Voice → 🗣️ Speech‑to‑Text → 📑 Chunking → 📦 Vector DB → 🔍 Retrieval → 🤖 LLM → 🛡️ Guardrails → 💬 Answer

📂 Dataset
We use the MSMARCO‑XI dataset provided by AI4Bharat:
👉 MSMARCO‑XI on Hugging Face (huggingface.co in Bing)

⚙️ Technical Features
Speech‑to‑Text: Sarvam API (low‑latency transcription).

Chunking Strategies:

Fixed‑size with overlap

Semantic splitting (sentence embeddings)

Metadata‑aware (topic‑based)

Vector Database: FAISS for fast similarity search.

Answer Generation: GPT‑4 / HuggingFace LLMs.

Guardrails:

Off‑topic query handling

Unsafe input detection

Hallucination checks (answers grounded in retrieved text)

Latency Target: End‑to‑end pipeline under 200ms.

Harness: Structured orchestration with retries, error handling, and logging.

📊 Latency Analytics
We report latency across multiple queries:

P50 (median)

P70 (upper mid)

P100 (worst case)

Results are documented in docs/latency_report.md.





