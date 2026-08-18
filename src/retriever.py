from qdrant_client import AsyncQdrantClient
from sentence_transformers import SentenceTransformer


encoder = SentenceTransformer("all-MiniLM-L6-v2")
qdrant_client = AsyncQdrantClient(path="./qdrant_storage")

async def retrieve_context(query: str, collection_name: str = "msmarco_xi_sample") -> str:
    try:
        query_vector = encoder.encode(query).tolist()
        results = await qdrant_client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            limit=2 
        )
        if not results:
            return "No matching context found in dataset."
        return "\n".join([res.payload.get("text", "") for res in results])
    except Exception as e:
        return f"Retrieval placeholder context due to: {str(e)}"


