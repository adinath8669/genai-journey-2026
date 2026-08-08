import streamlit as st
from services.analysis_service import analyze_resume

def show_resume(index, chunks):
    """
    Display resume analysis.
    Analysis is generated only once and cached in session state.
    """

    # ----------------------------
    # Generate Analysis
    # ----------------------------
    if st.button("📊 Analyze Resume"):

        with st.spinner("Analyzing resume..."):
            
            try:
                response = analyze_resume(
                    "Analyze my resume",
                    index,
                    chunks
                )

                st.session_state.resume_analysis_data = response

            except Exception as e:
                st.error(f"Analysis failed: {e}")
                return

            # st.write(response)
    if st.session_state.resume_analysis_data is not None:
            response = st.session_state.resume_analysis_data

            
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
