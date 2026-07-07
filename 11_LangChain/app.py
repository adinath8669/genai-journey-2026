from langchain_google_genai import ChatGoogleGenerativeAI
from prompt_templates import prompt_templet
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GENAI_API_KEY")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

st.title("🤖 LangChain Prompt Playground")
with st.sidebar:
    st.header("more option")
    mode =st.selectbox('select mode',
                      ['Teacher','Coder','Interviewer'])


topic=st.text_area("enter your topic")

if st.button("Ask AI "):
    prompt = prompt_templet(mode)

    chain = prompt | llm

    with st.spinner("Thinking..."):
        try:
            response = chain.invoke({
            "topic":topic,
            "mode":mode
        })

        except Exception as e:
            st.error(str(e))
            st.stop()
    st.write(response.content)

