from langchain.tools import tool
# from agent import model
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()


api_key=os.getenv("GEN_API_KEY")

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0
)

@tool("calculator_tool")
def calculator(exprssion : str)->str:
    "use this tool for solving mathematical calculations"
    return str(eval(exprssion))

@tool("wether_tool")
def weather(loaction:str)->str:
    "return wheather information"
    return f"wheatrhe at the {loaction} is sunny"

@tool("python_teacher_tool")
def python_teacher(topic:str)->str:
    """ Use this tool to explain Python programming concepts,
    syntax, functions, OOP, decorators, lists, tuples,
    dictionaries, and other Python-related topics."""
    
    result=model.invoke(f"Explain the Python topic '{topic}' in simple language with an example.")

    return result.content


@tool("interview_tool")
def interview_genarator(topic:str)->str:
    """Use this tool to generate interview questions on any programming or technical topic."""
    result=model.invoke(f"Generate 5 interview questions on {topic}")
    return result.content

    
  