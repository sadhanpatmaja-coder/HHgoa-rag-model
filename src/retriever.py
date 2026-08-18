from qdrant_client import AsyncQdrantClient

qdrant_client = AsyncQdrantClient(path="./qdrant_storage")

async def retrieve_context(query_vector: list, limit: int = 1):
  
    results = await qdrant_client.search(
        collection_name="msmarco_subset",
        query_vector=query_vector,
        limit=limit
    )
    return [res.payload["text"] for res in results]

