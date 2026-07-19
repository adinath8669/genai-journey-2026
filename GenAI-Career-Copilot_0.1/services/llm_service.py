from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import LLM_MODEL,api_key,TEMPERATURE


llm=ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    google_api_key=api_key,
    temperature=TEMPERATURE
)





