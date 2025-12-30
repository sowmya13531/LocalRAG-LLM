import faiss
import pickle
import numpy as np

# Simple in-memory FAISS index
DIM = 512  # embedding dimension
index = faiss.IndexFlatL2(DIM)
conversations = []

def embed(text):
    # Replace with proper embeddings (like OpenAI or Ollama embedding API)
    vec = np.random.rand(DIM).astype('float32')
    return vec

def add_message(message, role="user"):
    vec = embed(message)
    index.add(np.array([vec]))
    conversations.append({"role": role, "message": message})

def get_relevant(query, top_k=3):
    vec = embed(query)
    if index.ntotal == 0:
        return []
    D, I = index.search(np.array([vec]), top_k)
    results = [conversations[i] for i in I[0]]
    return results
