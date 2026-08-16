import streamlit as st
from helper_utils.chat_utils import export_chat_history,export_markdown
from services.chat_service import chat_with_resume
from memory.memory import chat_history


def show_chat(index, chunks):
    """
    Display conversational chat with the uploaded resume.
    """

    # st.subheader("💬 Chat With Your Resume")

   

    # ----------------------------
    # Display Previous Messages
    # ----------------------------
    for message in chat_history.messages:

        if message.type == "human":

            with st.chat_message("user"):
                st.write(message.content)

        elif message.type == "ai":

            with st.chat_message("assistant"):
                st.write(message.content)


    # ----------------------------
    # User Input
    # ----------------------------
    user_input = st.chat_input(
        "Ask something about your resume..."
    )

    if user_input:

        # Display user's current message
        with st.chat_message("user"):
            st.write(user_input)

        # Generate AI response
        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                answer = chat_with_resume(
                    user_input,
                    index,
                    chunks,
                )

            st.write(answer)


        st.rerun()

     # ----------------------------
     # Clear Chat
    # ----------------------------
    if st.button("🗑️ Clear Chat"):
        chat_history.clear()
        st.rerun()

    conversation = export_chat_history(chat_history)
    
    st.download_button(
            label="📥 Download Chat",
            data=conversation,
            file_name="conversation.txt",
            mime="text/plain"
        )
    
    st.download_button(
        "📥 Download Conversation (.md)",
        data=export_markdown(chat_history),
        file_name="conversation.md",
        mime="text/markdown"
    )