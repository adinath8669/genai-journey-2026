from utils import load_pdf, create_chunks
from embedding import create_embeddings, create_vector_db
from rag import retrieve_chunks, generate_answer
import streamlit as st
from datetime import datetime
import os

st.title("🤖 AI Study Assistant")

with st.sidebar:
    st.header("more options")
    mode=st.selectbox('select mode',
                      ['Teacher','coder','creative'])
    
    # if mode=='Teacher':
    #     temprature=0.5

    # elif mode=='coder':
    #     temprature=0.1
    # else:
    #     temprature=1.2

    clear_chat=st.button('Clear Chat')
    if clear_chat:
        st.session_state.history=[]

if 'history' not in st.session_state:
    st.session_state.history=[]


uploaded_file = st.file_uploader(
    "📄 Upload PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    upload_path = os.path.join("uploads", uploaded_file.name)

    os.makedirs("uploads", exist_ok=True)

    with open(upload_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

@st.cache_resource
def build_vector_db(upload_path):
    text = load_pdf(upload_path)
    # print(text[:1000])
    chunks = create_chunks(text)
    print("Number of chunks:", len(chunks))
    # print(chunks[0])
    embeddings = create_embeddings(chunks)
    index = create_vector_db(embeddings)
    return index, chunks


if uploaded_file is None:
    st.warning("Please upload a PDF first.")
    st.stop()


if (
    "current_pdf" not in st.session_state
    or st.session_state.current_pdf != uploaded_file.name
):

    with st.spinner("Creating embeddings..."):
        index, chunks = build_vector_db(upload_path)

        st.session_state.index = index
        st.session_state.chunks = chunks
        st.session_state.current_pdf = uploaded_file.name

    st.success("✅ PDF processed successfully!")


index = st.session_state.get("index")
chunks = st.session_state.get("chunks")
   
query = st.text_area("Enter your question")
# query = input("Ask Question : ")




if st.button("Ask AI "):
    
    if not query.strip():
      st.warning("Please enter a question.")
      st.stop()
    retrieved = retrieve_chunks(query, index, chunks) 
    # print("=" * 50)
    # print("Retrieved Chunks:")
    # print(retrieved)
    # print("=" * 50)
    
    with st.spinner("Thinking..."):
        try:
            answer = generate_answer(retrieved, query,mode)

        except Exception as e:
            st.error(str(e))
            st.stop()


    

    st.session_state.history.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "question": query,
        "answer": answer
        })
    st.write(answer)


chat_history = ""

for chat in reversed(st.session_state.history):
    chat_history += f"Time: {chat['time']}\n"
    chat_history += f"You: {chat['question']}\n"
    chat_history += f"AI: {chat['answer']}\n"
    chat_history += "-" * 50 + "\n"

# Download button
st.download_button(
    label="📥 Download Chat History",
    data=chat_history,
    file_name="chat_history.txt",
    mime="text/plain"
)
for chat in reversed(st.session_state.history):

    st.markdown(f"**🕒 {chat['time']}**")

    st.markdown(f"**🙋 You:** {chat['question']}")

    st.markdown(f"**🤖 AI:** {chat['answer']}")

    st.markdown("---")
