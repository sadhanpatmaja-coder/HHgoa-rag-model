import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(chunks):
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, chunks

def search_index(index, chunks, query, k=5):
    query_emb = model.encode([query])
    distances, indices = index.search(np.array(query_emb), k)
    return [chunks[i] for i in indices[0]]
