# from services.job_match_service import generate_job_matches
from graph.graph import graph
from helper_utils.helper import run_career_copilot_graph
import streamlit as st


def show_job_matcher(index, chunks):
    """
    Display job recommendations based on the uploaded resume.
    """
    has_cached_result = st.session_state.job_matcher_data is not None

    button_label = "🔄 Regenerate matching jobs" if has_cached_result else "💼 matching jobs"

    if st.button(button_label):
        with st.spinner("Generating your matching jobs based on your resume ...."):

            try:

                result = run_career_copilot_graph("Recommend the top 5 matching jobs for my resume.", index, chunks)
                                    
                                    
                 # Save result in session state
                st.session_state.job_matcher_data = result["job_match_result"]

            except Exception as e :
                st.error(f"Failed to generate study plan: {e}")
                return
            
    if st.session_state.job_matcher_data is not None:
            result = st.session_state.job_matcher_data

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
