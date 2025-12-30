import sys
import os

# Add the root directory of the project
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# Add the 'rag' folder explicitly (optional but can help)
RAG_DIR = os.path.join(ROOT_DIR, "rag")
if RAG_DIR not in sys.path:
    sys.path.append(RAG_DIR)

# Imports
from ollama_client import ask_llama
from prompt import SYSTEM_PROMPT
from memory.faiss_memory import add_message, get_relevant
from rag.pdf_loader import load_pdf
from rag.rag_store import add_docs, retrieve_docs

print("All imports successful ✅")
