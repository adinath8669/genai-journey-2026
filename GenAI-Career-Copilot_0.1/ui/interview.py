# from services.interview_service import generate_interview_questions
from graph.graph import graph
import streamlit as st

def interview_show(index, chunks):

    if st.button("💼 show interview questions"):
        with st.spinner("Generating interview questions..."):

            try:
                result = graph.invoke({
                    "request":"Generate interview questions",
                    "intent":"",
                    "index":index,
                    "chunks":chunks,
                    "resume_analysis": st.session_state.resume_analysis,
                    "skill_gap_result": st.session_state.skill_gap_result,
                    "interview_result": None,
                    "study_plan_result": None,
                    "job_match_result": None
                })

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
