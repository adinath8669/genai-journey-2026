from services.interview_service import generate_interview_questions
import streamlit as st

def interview_show(index, chunks):
    with st.spinner("Generating interview questions..."):

            result = generate_interview_questions(
                "Generate interview questions",
                index,
                chunks
            )

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
