import streamlit as st
from memory import chat_history
from chat import chat

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
)

st.set_page_config(page_title="Conversation Memory")

st.title("🤖 AI Conversation Assistant")



if st.sidebar.button("Clear Chat"):
    chat_history.clear()
    st.rerun()



for message in chat_history.messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.write(message.content)

prompt = st.chat_input("Ask something...")

if prompt:

    with st.chat_message("user"):
        st.write(prompt)

    response = chat(
        prompt,
    )

    with st.chat_message("assistant"):
        st.write(response)

  