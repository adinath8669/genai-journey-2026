from services.job_match_service import generate_job_matches
import streamlit as st


def show_job_matcher(index, chunks):
    """
    Display job recommendations based on the uploaded resume.
    """

    with st.spinner("Generating your matching jobs based on your resume ...."):

        try:

            result=generate_job_matches(
                "Recommend the top 5 matching jobs for my resume.",
                index,
                chunks
                )

        except Exception as e :
            st.error(f"Failed to generate study plan: {e}")
            return

        st.header("💼 Recommended Job Roles")
        for job in result.recommended_jobs:
            st.subheader(f"🚀 {job.role}")

            st.metric("⭐ Match Score", f"{job.match_score}%")

            st.write("📈 why this role ..?")
            st.write(job.recommendation_reason)

            st.write("### 📚 Missing Skills")
            for skills in job.missing_skills:
                st.write(f"• {skills}")

            st.write("### 🎯  Next Steps")
            for step in job.next_steps:
                st.write(f"• {step}")

        st.divider()
