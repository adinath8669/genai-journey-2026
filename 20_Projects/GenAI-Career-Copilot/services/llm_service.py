from config import api_key
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.resume_prompt import resume_prompt
from parsers.output_parser import parser2

llm=ChatGoogleGenerativeAI(
    
    model="gemini-2.5-flash",
    google_api_key=api_key
)

def generate_response(prompt : str)->str:
    chain=resume_prompt|llm|parser2
    response=chain.invoke(prompt)
    return response