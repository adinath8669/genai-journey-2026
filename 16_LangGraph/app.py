
import streamlit as st

from graph import graph

st.title("🧠 Simple LangGraph Workflow")

question=st.text_input("Ask Question")

if st.button("submit"):

    try:
        response=graph.invoke({
            "question":question
        })
    except Exception as e:
        st.write(e)

    st.success(response["answer"])
    st.write("Category:", response["category"])