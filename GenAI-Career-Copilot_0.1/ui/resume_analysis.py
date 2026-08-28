import streamlit as st
# from services.analysis_service import analyze_resume

def show_resume(index, chunks):
    """
    Display resume analysis.
    Analysis is now computed once at upload time (see app.py)
    and cached in st.session_state.resume_analysis — this tab
    just displays it, no separate Gemini call needed.

    """

    # ----------------------------
    # Generate Analysis
    # ----------------------------
    # if st.button("📊 Analyze Resume"):

    #     with st.spinner("Analyzing resume..."):
            
    #         try:
    #             response = analyze_resume(
    #                 "Analyze my resume",
    #                 index,
    #                 chunks
    #             )

    #             st.session_state.resume_analysis_data = response

    #         except Exception as e:
    #             st.error(f"Analysis failed: {e}")
    #             return

            # st.write(response)

    if st.session_state.resume_analysis is None:
        st.info("Upload a resume in the sidebar to see your analysis.")
        return
    
    response = st.session_state.resume_analysis

            
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
