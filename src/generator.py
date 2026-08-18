import os
from groq import AsyncGroq

async def stream_llm_tokens(query: str, context: str):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        yield "Error: GROQ_API_KEY not configured."
        return

    client = AsyncGroq(api_key=api_key)
    
    system_prompt = (
        "You are an accurate RAG assistant. Answer the user's question using ONLY the provided context. "
        "If the answer cannot be found in the context, respond with 'I am sorry, but that information is not present in the dataset.' "
        "Do not hallucinate."
    )
    user_prompt = f"Context:\n{context}\n\nQuestion: {query}"
    
    try:
        stream = await client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.1,
            stream=True
        )
        async for chunk in stream:
            token = chunk.choices[0].delta.content
            if token:
                yield token
    except Exception as e:
        yield f"Inference engine exception occurred: {str(e)}"
