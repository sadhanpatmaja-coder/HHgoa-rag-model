from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


# Load the same embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Our sample chunks
chunks = [
    "Artificial Intelligence is a field of computer science.",
    "Machine learning is a part of artificial intelligence.",
    "Deep learning uses neural networks to learn from data.",
    "Natural language processing works with human language."
]


# Create embeddings for the chunks
embeddings = model.encode(
    chunks,
    convert_to_numpy=True
)


# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(
    embeddings.astype("float32")
)


# --------------------------------------------------
# SEARCH FUNCTION
# --------------------------------------------------

def retrieve(query, k=2):

    # Convert the question into an embedding
    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    query_embedding = query_embedding.astype("float32")


    # Search FAISS
    distances, indices = index.search(
        query_embedding,
        k
    )


    # Get the matching chunks
    results = []

    for i in indices[0]:

        results.append(chunks[i])


    return results


# --------------------------------------------------
# TEST
# --------------------------------------------------

question = "What is machine learning?"

results = retrieve(question)


print("\nQuestion:")
print(question)


print("\nRetrieved chunks:")

for i, result in enumerate(results):

    print(f"\nResult {i + 1}:")
    print(result)