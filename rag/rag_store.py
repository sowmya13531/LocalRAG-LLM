from memory.faiss_memory import add_message, get_relevant

def add_docs(text):
    # Split text into chunks
    chunks = text.split("\n")
    for chunk in chunks:
        if chunk.strip():
            add_message(chunk, role="doc")

def retrieve_docs(query, top_k=3):
    return get_relevant(query, top_k)
