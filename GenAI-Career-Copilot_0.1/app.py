from services.analysis_service import analyze_resume
from services.vector_store_service import build_vector_store
import streamlit as st
import os
from helper_utils.helpers import initialize_session
from services.pdf_service import save_uploaded_file



st.set_page_config(
    page_title="GenAI Career Copilot",
    page_icon="🚀",
    layout="wide"
)
st.title("GenAI Career Copilot")

# ----------------------------
# Initialize Session State
# ----------------------------
initialize_session()


# ----------------------------
# Upload Resume
# ----------------------------

uploaded_file=st.file_uploader("upload_file",type=["pdf"])

if uploaded_file :
    # Save PDF
    file_path = save_uploaded_file(uploaded_file)


# Process only if a different resume is uploaded
    if st.session_state.current_resume != uploaded_file.name:
        with st.spinner("Building Vector Database..."):
            index, chunks = build_vector_store(file_path)
            st.session_state.index = index
            st.session_state.chunks = chunks
            st.session_state.current_resume = uploaded_file.name
        st.success("Vector store built successfully!")


if st.session_state.index is not None:
    if st.button("📊 Analyze Resume"):
        with st.spinner("Analyzing resume..."):
            response = analyze_resume(
                "Analyze my resume",
                st.session_state.index,
                st.session_state.chunks
            )

        # st.write(response)
        
        st.header("📊 Resume Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Resume Score", response.Resume_score)

        with col2:
            st.metric("ATS Score", response.ATS_score)

        st.subheader("✅ Strengths")

        for item in response.strengths:
            st.write(f"✔️ {item}")

        st.subheader("⚠️ Weaknesses")

        for item in response.Weakness:
            st.write(f"• {item}")

        st.subheader("📚 Missing Skills")

        for item in response.missing_skills:
            st.write(f"• {item}")


else:
    # Disable or hide button functionality if no file has been processed yet
    st.info("Please upload a resume to start the scanning process.")

