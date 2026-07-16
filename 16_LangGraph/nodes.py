from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEN_API_KEY"),
    temperature=0
)


def classifier_node(state):

    question=state["question"].lower()
    if "python" in question:

        category = "python"

    else:

        category = "interview"

    return {"category": category}


def teacher_node(state):

    response = llm.invoke(
        f"Teach this topic simply:\n{state['question']}"
    )

    return {
        "answer": response.content
    }



def interview_node(state):

    response = llm.invoke(
        f"Answer this interview question:\n{state['question']}"
    )

    return {
        "answer": response.content
    }

