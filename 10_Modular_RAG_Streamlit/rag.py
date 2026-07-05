import numpy as np
import os
from google import genai
from dotenv import load_dotenv
from embedding import model
from config import LLM_MODEL,TEMPERATURE,MAX_TOKENS

load_dotenv()

api_key=os.getenv("GENAI_API_KEY")

client=genai.Client(api_key=api_key)



def retrieve_chunks(query, index, chunks):
    query_embedding=model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances,indices =index.search(query_embedding,3)

    # retriving relevnet chuncks from pdf
    retrieved_chunks = "\n\n".join(
        [chunks[i] for i in indices[0]]
    )
    return retrieved_chunks



def generate_answer(retrieved_chunks,query,mode):
    prompt = f"""
You are a helpful {mode} AI assistant.

Answer ONLY from the provided context.

Context:
{retrieved_chunks}

User Question:
{query}

If the answer cannot be found in the context, reply exactly:
"I couldn't find the answer in the provided document."

Do not use your own knowledge.
"""

    # gemini model 
    response=client.models.generate_content(
        model=LLM_MODEL,
        contents=prompt,
        config={
            "temperature":TEMPERATURE,
            "max_output_tokens":MAX_TOKENS
        }
    )
    return response.text