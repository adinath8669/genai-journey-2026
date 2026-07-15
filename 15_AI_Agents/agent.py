from langchain.agents import create_agent
from tools import weather,calculator,interview_genarator,python_teacher
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import system_prompt
from dotenv import load_dotenv
import os
load_dotenv()

api_key=os.getenv("GEN_API_KEY")


model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0
)

def crating_agent():
    agent=create_agent(
        model=model,
        tools=[weather,calculator,interview_genarator,python_teacher],
        system_prompt=system_prompt
    )

    return agent