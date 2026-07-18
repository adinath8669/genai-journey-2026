import os 
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GEN_API_KEY")

LLM_MODEL = "gemini-2.5-flash"

TEMPERATURE = 0.2