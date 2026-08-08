from services.job_description_service import analyze_job_description
import streamlit as st

def show_job_description_matcher(index, chunks):
    """
    Job description analysis based on the uploaded resume and job description.
    """
    job_description = st.text_area(
    "📋 Paste Job Description",
    height=300)

    query="""Compare this resume with the provided job description.
Retrieve experience, skills, projects, certifications,
and technologies relevant to hiring."""

    if st.button("Analyze JD Match"):
        with st.spinner("Analyzing Job Description ...."):

            st.session_state.job_description_matcher_data = analyze_job_description(
            query,
            index,
            chunks,
            job_description
        )

    if st.session_state.job_description_matcher_data is not None:

            result = st.session_state.job_description_matcher_data

        
            st.metric(
            "Overall Match",
            f"{result.overall_match_score}%")

            st.subheader("✅ Matching Skills")
            for skill in result.matched_skills:
                st.write(f"✔ {skill}")

            st.subheader("❌ Missing Skills")
            for skill in result.missing_skills:
                st.write(f"• {skill}")

            st.subheader("💪 Resume weakness")
            for item in result.resume_weakness:
                st.write(f"• {item}")

            st.subheader("📝 Resume Improvements")
            for i, improvement in enumerate(result.resume_improvements, 1):
                st.write(f"{i}. {improvement}")

            st.subheader("🎯 ATS Keywords suggestion")
            for keyword in result.ats_suggestions:
                st.write(f"• {keyword}")

            st.success(result.final_recommendation)