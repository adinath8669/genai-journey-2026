from dotenv import load_dotenv
import os
load_dotenv()
api_key=os.getenv('GENAI_API_KEY')
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TOP_K = 3
CHUNK_SIZE = 500
TEMPERATURE = 0.1
MAX_TOKENS = 1000
LLM_MODEL="gemini-2.5-flash"
UPLOAD_DIR = "uploads"

