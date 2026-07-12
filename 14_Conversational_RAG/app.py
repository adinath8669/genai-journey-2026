import streamlit as st
import tempfile
import os

from services.rag_service import build_vectore_store
from services.retriever_service import retrive_chuncks
from chat import get_response
from services.memory_service import chat_history
from utils import export_chat_history,export_markdown

st.set_page_config(
    page_title="Conversational RAG",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Conversational RAG Assistant")
# -------------------------------
# Display Chat History
# -------------------------------

for message in chat_history.messages:

    if message.type == "human":
        with st.chat_message("user"):
            st.write(message.content)

    elif message.type == "ai":
        with st.chat_message("assistant"):
            st.write(message.content)

# -------------------------------
# Session State
# -------------------------------

if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "chunks" not in st.session_state:
    st.session_state.chunks = None

# -------------------------------
# Sidebar
# -------------------------------

with st.sidebar:

    st.header("📄 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type="pdf"
    )

    st.divider()

    st.subheader("Project Info")

    if st.session_state.chunks:

        st.write(f"**Chunks:** {len(st.session_state.chunks)}")

    st.write("Embedding Model: MiniLM")

    human_messages = len(
    [m for m in chat_history.messages if m.type == "human"]
    )

    ai_messages = len(
        [m for m in chat_history.messages if m.type == "ai"]
    )

    st.write(f"👤 User Messages : {human_messages}")
    st.write(f"🤖 AI Messages : {ai_messages}")
    st.write(f"💬 Total Messages : {len(chat_history.messages)}")

    if st.button("🗑 Clear Chat"):

        chat_history.clear()

        st.rerun()

    conversation = export_chat_history(chat_history)

    st.download_button(
        label="📥 Download Chat",
        data=conversation,
        file_name="conversation.txt",
        mime="text/plain"
    )

    st.download_button(
    "📥 Download Conversation (.md)",
    data=export_markdown(chat_history),
    file_name="conversation.md",
    mime="text/markdown"
)

# -------------------------------
# Build Vector Store
# -------------------------------

if uploaded_file is not None and st.session_state.vector_db is None:

    with st.spinner("Building Vector Database..."):

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

        temp_file.write(uploaded_file.read())

        temp_file.close()

        vector_db, chunks = build_vectore_store(temp_file.name)

        st.session_state.vector_db = vector_db
        st.session_state.chunks = chunks

        os.remove(temp_file.name)

    st.success("✅ PDF processed successfully!")

# -------------------------------
# Chat Interface
# -------------------------------

if st.session_state.vector_db is not None:

    user_question = st.chat_input("Ask a question about the PDF...")

    if user_question:

        with st.chat_message("user"):
            st.write(user_question)

        retrieved_chunks = retrive_chuncks(
            user_question,
            st.session_state.vector_db,
            st.session_state.chunks
        )

        with st.expander("📚 Retrieved Context"):

            for i, chunk in enumerate(retrieved_chunks, start=1):

                st.markdown(f"### Chunk {i}")

                st.write(chunk)

                st.divider()

        try:
            answer = get_response(
                user_question,
                retrieved_chunks
            )

        except Exception as e:
            st.write("error occors" ,e)

        with st.chat_message("assistant"):
            st.write(answer)

else:

    st.info("📄 Upload a PDF to start chatting.")