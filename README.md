## 🦙Offline Conversational AI with Llama3.2 via Ollama - RAG - FAISS

Offline, privacy-first AI assistant using a **local LLaMA 3.2** via **Ollama model**, FAISS memory, and document-grounded retrieval. Ask any questions and as well as questions about your PDFs and get precise, context-aware answers — all offline.

## 🚀 Features

- Local LLM inference with LLaMA 3.2 (via Ollama)
- Retrieval-Augmented Generation (RAG) using FAISS
- PDF ingestion: upload multiple PDFs as knowledge sources
- Conversational memory: remember previous messages
- Offline & privacy-safe: no cloud APIs needed
- Interactive UI: built with Streamlit
- Extensible & modular: easy to add voice, additional embeddings, or new models

  
### 🗂 Project Structure

```
LocalRAG-LLM/
│
├─ app.py                # Main Streamlit app
├─ ollama_client.py      # Handles communication with local LLaMA
├─ prompt.py             # SYSTEM_PROMPT for LLaMA instructions
├─ requirements.txt      # Project dependencies
│
├─ rag/
│   ├─ __init__.py
│   ├─ pdf_loader.py     # Extracts text from PDFs
│   └─ rag_store.py      # Adds/retrieves document chunks in memory
│
├─ memory/
│   ├─ __init__.py
│   └─ faiss_memory.py   # FAISS vector store + embeddings + retrieval
│
└─ data/
    └─ doc.pdf           # Example PDF storage folder
```

## 🛠 Installation

1. Clone the repository:

```
git clone https://github.com/sowmya13531/LocalRAG-LLM.git
cd LocalRAG-LLM
```

2. Create a virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

4. Install dependencies
```
pip install -r requirements.txt
```

4. Make sure Ollama is installed and LLaMA 3.2 model is ready locally.

## ⚙️ Usage

1. Run the Streamlit app:

*streamlit run app.py*

2. Upload PDF documents under “📄 Upload Doc”.

3. Ask questions in the chat area under “💬 Chat with Local RAG-LLM”.

4. LLaMA generates document-grounded answers, and the conversation is stored in memory.

## 💡 How It Works (Pipeline)

1. PDF Ingestion: pdf_loader.py extracts text from uploaded PDFs.

2. Chunking & Memory Storage: rag_store.py splits text into chunks and stores in FAISS memory using faiss_memory.py.

3. Query Handling:
User submits a question.
Relevant document chunks are retrieved with semantic similarity (retrieve_docs).

**SYSTEM_PROMPT + retrieved context + user query is sent to LLaMA (ollama_client.py).**

4. LLM Response: LLaMA generates an answer that is document-grounded, clear, and concise.

5. Memory Update: Both user input and assistant reply are stored in FAISS memory for multi-turn conversation.

## 🖤 SYSTEM_PROMPT

Controls assistant behavior:

*You are a helpful AI assistant.
Use conversation memory and provided documents when relevant.
If documents are provided, base answers strictly on them.
Be clear and concise.*

- Ensures factual, context-aware responses

- Avoids hallucinations

- Maintains consistent style


### ⚡ Tech Stack

- Python 3.10+
- Streamlit — interactive UI
- FAISS — fast semantic search
- Ollama + LLaMA 3.2 — local LLM inference
- PyPDF2 / pypdf — PDF parsing
- NumPy + sentence-transformers — embeddings
- Optional: Gradio, pyttsx3, speechrecognition, pydub for voice features

### 📈 Improvements / Future Work
- Replace random embeddings with real embeddings (sentence-transformers or Ollama embeddings)
- Support voice input/output
- Advanced chunking with sliding window for better retrieval
- Multi-document conflict handling & metadata filtering
- Save & load FAISS index to persist knowledge across sessions
- Streaming responses for better UX
