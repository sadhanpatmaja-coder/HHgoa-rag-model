from sentence_transformers import SentenceTransformer
import faiss
import numpy as np



model = SentenceTransformer("all-MiniLM-L6-v2")



chunks = [
    "Artificial Intelligence is a field of computer science.",
    "Machine learning is a part of artificial intelligence.",
    "Deep learning uses neural networks to learn from data.",
    "Natural language processing works with human language."
]

embeddings = model.encode(
    chunks,
    convert_to_numpy=True
)



dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(
    embeddings.astype("float32")
)



def retrieve(query, k=2):


    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    query_embedding = query_embedding.astype("float32")


  
    distances, indices = index.search(
        query_embedding,
        k
    )


    
    results = []

    for i in indices[0]:

        results.append(chunks[i])


    return results




question = "What is machine learning?"

results = retrieve(question)


print("\nQuestion:")
print(question)


print("\nRetrieved chunks:")

for i, result in enumerate(results):

    print(f"\nResult {i + 1}:")
    print(result)
