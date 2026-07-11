from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
import os 
from memory import chat_history
load_dotenv()

api_key=os.getenv("GENAI_API_KEY")


model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)


system_message = SystemMessage(
    content="You are a friendly AI assistant."
)


def chat(user_input):
    chat_history.add_user_message(HumanMessage(user_input))

    messages=[system_message]+chat_history.messages

    response=model.invoke(messages)

    chat_history.add_ai_message(AIMessage(response.content))

    return response.content