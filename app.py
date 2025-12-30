import streamlit as st
import os

from ollama_client import ask_llama
from prompt import SYSTEM_PROMPT
from memory.faiss_memory import add_message, get_relevant
from rag.pdf_loader import load_pdf
from rag.rag_store import add_docs, retrieve_docs

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Offline Conversational AI",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------- DARK THEME --------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    textarea, input {
        background-color: #161b22 !important;
        color: #fafafa !important;
        border-radius: 8px;
    }
    button {
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- TITLE --------------------
st.title("Local RAG-LLM: Offline Conversational AI with FAISS")

st.divider()

# -------------------- PDF UPLOAD (RAG) --------------------
st.markdown("### 📄 Upload Doc")

uploaded_file = st.file_uploader(
    "Upload a PDF document",
    type=["pdf"]
)

if uploaded_file:
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = load_pdf(file_path)
    add_docs(text)

    st.success("✅ PDF successfully added to knowledge base")
    st.caption(f"Loaded file: **{uploaded_file.name}**")

st.divider()

# -------------------- CHAT SECTION --------------------
st.markdown("### 💬 Chat with Local RAG-LLM")

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_area(
        "Your Question",
        height=90,
        placeholder="Ask something about the uploaded document..."
    )
    send = st.form_submit_button("🚀 Send")

if send and user_input.strip():
    # Store user message
    add_message(user_input, role="user")

    # Retrieve relevant memory + documents
    relevant_docs = retrieve_docs(user_input)
    context = "\n".join([doc["message"] for doc in relevant_docs])

    # Build final prompt
    final_prompt = (
        SYSTEM_PROMPT
        + "\n\nContext:\n"
        + context
        + "\n\nUser Question:\n"
        + user_input
    )

    # Ask LLaMA
    reply = ask_llama(final_prompt)

    # Store assistant reply
    add_message(reply, role="assistant")

    # Display response
    st.markdown("### 🤖 Response")
    st.text_area(
        label="",
        value=reply,
        height=240
    )

# -------------------- FOOTER --------------------
st.divider()
st.caption("⚡ Built with Streamlit + FAISS + Ollama | Local & Private")
