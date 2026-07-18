import streamlit as st
from graph import graph

st.set_page_config(
    page_title="Simple LangGraph Workflow",
    page_icon="🧠"
)

st.title("🧠 Simple LangGraph Workflow")

# -----------------------------
# Session State
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# User Input
# -----------------------------
question = st.text_input("Enter your Question")

if st.button("Submit"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    try:
        result = graph.invoke(
            {
                "question": question
            }
        )

        st.success(result["answer"])

        if "category" in result:
            st.info(f"Category: {result['category']}")

        st.session_state.history.append(
            {
                "question": question,
                "answer": result["answer"],
                "category": result.get("category", "N/A")
            }
        )

    except Exception as e:
        st.error(f"Error: {e}")

# -----------------------------
# Chat History
# -----------------------------
if st.session_state.history:

    st.divider()
    st.subheader("💬 Chat History")

    for chat in reversed(st.session_state.history):

        with st.container():

            st.markdown(f"### 🙋 You")
            st.write(chat["question"])

            st.markdown("### 🤖 AI")
            st.write(chat["answer"])

            st.caption(f"Category: {chat['category']}")

            st.divider()