# from services.interview_service import generate_interview_questions
# from graph.graph import graph
from helper_utils.helper import run_career_copilot_graph
import streamlit as st

def interview_show(index, chunks):

    has_cached_result = st.session_state.interview_data is not None

    button_label = "🔄 Regenerate interview questions" if has_cached_result else "💼 Show interview questions"

    if st.button(button_label):
        with st.spinner("Generating interview questions..."):

            try:
                result = run_career_copilot_graph("Generate interview questions", index, chunks)

                st.session_state.interview_data = result["interview_result"]

            except Exception as e:
                st.error(f"Failed to generate interview questions: {e}")
                return

    if st.session_state.interview_data is not None:
                result = st.session_state.interview_data

                st.subheader("Technical Questions")

                for q in result.technical_questions:
                    st.markdown(f"### ❓ {q.question}")
                    st.write(f"**Difficulty:** {q.difficulty}")
                    st.write(f"**Expected Answer:** {q.answer}")
                    st.divider()

                st.subheader("Behavioral Questions")

                for q in result.behavioral_questions:
                    st.markdown(f"### ❓ {q.question}")
                    st.write(f"**Difficulty:** {q.difficulty}")
                    st.write(f"**Expected Answer:** {q.answer}")
                    st.divider()

                st.subheader("Project Questions")

                for q in result.project_questions:
                    st.markdown(f"### ❓ {q.question}")
                    st.write(f"**Difficulty:** {q.difficulty}")
                    st.write(f"**Expected Answer:** {q.answer}")
                    st.divider()

                st.subheader("Follow-up Questions")

                for q in result.follow_up_questions:
                    st.markdown(f"### ❓ {q.question}")
                    st.write(f"**Difficulty:** {q.difficulty}")
                    st.write(f"**Expected Answer:** {q.answer}")
                    st.divider()
