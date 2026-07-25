import streamlit as st
from services.analysis_service import analyze_resume

def show_resume(index, chunks):
    with st.spinner("Analyzing resume..."):
        response = analyze_resume(
                "Analyze my resume",
                index,
                chunks
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
