import streamlit as st
from services.analysis_service import analyze_resume
from services.rag_service import build_vector_store
st.set_page_config(
    page_title="GenAI Career Copilot",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 GenAI Career Copilot")
st.write("Your AI-powered resume mentor.")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)

if uploaded_file:
    st.success("Resume uploaded successfully!")
    


if uploaded_file:

    with open("uploads/resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    index, chunks = build_vector_store(
        "uploads/resume.pdf"
        )
    # st.write(type(index))

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing..."):

            response = analyze_resume(
                "Analyze this resume",
                index,
                chunks
            )

        st.write(response)