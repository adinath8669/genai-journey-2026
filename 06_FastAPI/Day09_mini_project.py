from google import genai
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
app=FastAPI(title="My First AI Backend")
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)


class Question(BaseModel):
    mode: str
    question: str

@app.get("/")
def get_data():
    return {"msg":"this is my home page"}

@app.post("/question")
def que_ans(questions:Question):

    data =  f"""
    You are acting as a {questions.mode}.

    Answer the following question:

    {questions.question}
    """
    try:
        response=client.models.generate_content(
            model="gemini-2.5-flash",
            contents=data,
            config={
                "max_output_tokens":1000,
                "temperature":0.9
            }
        )
        
        
        return { "answare":response.text}
    except Exception as e:
         return {
            "error": str(e)
        }