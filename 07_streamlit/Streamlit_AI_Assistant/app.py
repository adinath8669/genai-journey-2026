from google import genai
from dotenv import load_dotenv
import os
import streamlit as st
from datetime import datetime

load_dotenv()

api_key=os.getenv('GENAI_API_KEY')

client=genai.Client(api_key=api_key)

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Study Assistant")

with st.sidebar:
    st.header("more options")
    mode=st.selectbox('select mode',
                      ['Teacher','coder','creative'])
    
    if mode=='Teacher':
        temprature=0.5

    elif mode=='coder':
        temprature=0.1
    else:
        temprature=1.2

    clear_chat=st.button('Clear Chat')
    if clear_chat:
        st.session_state.history=[]

if 'history' not in st.session_state:
    st.session_state.history=[]

user_question = st.text_area("Enter your question")


if st.button("Ask AI "):
    question = f"""
You are a {mode}.

Answer the following question:

{user_question}
"""
    if not user_question.strip():
      st.warning("Please enter a question.")
      st.stop()
    with st.spinner("Thinking..."):
        try:
    
            response=client.models.generate_content(
                model="gemini-2.5-flash",
                contents=question,
                config={
                    "max_output_tokens":1000,
                    "temperature":temprature
                }
            )

        except Exception as e:
            st.error("Error occured please try again")

    answer=response.text
    

    st.session_state.history.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "question": user_question,
        "answer": answer
        })
    st.write(answer)


chat_history = ""

for chat in reversed(st.session_state.history):
    chat_history += f"Time: {chat['time']}\n"
    chat_history += f"You: {chat['question']}\n"
    chat_history += f"AI: {chat['answer']}\n"
    chat_history += "-" * 50 + "\n"

# Download button
st.download_button(
    label="📥 Download Chat History",
    data=chat_history,
    file_name="chat_history.txt",
    mime="text/plain"
)
for chat in reversed(st.session_state.history):

    st.markdown(f"**🕒 {chat['time']}**")

    st.markdown(f"**🙋 You:** {chat['question']}")

    st.markdown(f"**🤖 AI:** {chat['answer']}")

    st.markdown("---")
