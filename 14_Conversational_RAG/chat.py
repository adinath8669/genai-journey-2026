from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage
from services.memory_service import chat_history
from dotenv import load_dotenv
from config import LLM_MODEL
import os
from services.prompt_service import chat

load_dotenv()
api_key=os.getenv("GEN_API_KEY")



model=ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    google_api_key=api_key,
    temperature=0.1
)


def get_response(user_input, retrieved_chunks):

    messages = chat(user_input, retrieved_chunks)

    response = model.invoke(messages)

    chat_history.add_ai_message(response.content)

    return response.content