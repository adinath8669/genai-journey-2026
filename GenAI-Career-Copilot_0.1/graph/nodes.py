from graph.state import GraphState
from graph.state import GraphState2

from services.retrieval_service import retrieve_chunks
from services.llm_service import llm

from langchain_core.prompts import PromptTemplate


# --------------------------------------------------
# Prompt
# --------------------------------------------------

prompt = PromptTemplate.from_template(
    """
You are an AI assistant analyzing a user's resume.

Use ONLY the resume context provided below.

Resume Context:
{context}

Question:
{question}

Answer:
"""
)


# --------------------------------------------------
# Retrieve Node
# --------------------------------------------------

def retrieve_node(state: GraphState):
    """
    Retrieve relevant resume chunks based on the
    user's question.
    """

    question = state["question"]

    retrieved_chunks = retrieve_chunks(
        query=question,
        index=state["index"],
        chunks=state["chunks"]
    )

    return {
        "retrieved_chunks": retrieved_chunks
    }


# --------------------------------------------------
# Generate Node
# --------------------------------------------------

def generate_node(state: GraphState):
    """
    Generate an answer using the retrieved resume
    context and user's question.
    """

    context = "\n\n".join(
        state["retrieved_chunks"]
    )

    messages = prompt.invoke(
        {
            "context": context,
            "question": state["question"]
        }
    )

    response = llm.invoke(messages)

    return {
        "answer": response.content
    }



def analyze_node(state: GraphState2):
    request = state["request"]

    print(f"Analyzing request: {request}")

    return {
        "request": request
    }


def interview_node(state: GraphState2):

    return {
        "result": "I will generate interview questions for you."
    }


def study_plan_node(state: GraphState2):

    return {
        "result": "I will create a personalized study plan for you."
    }


def route_request(state: GraphState2):

    request = state["request"].lower()

    if "interview" in request or "question" in request:
        return "interview"

    elif "study" in request or "learn" in request or "plan" in request:
        return "study_plan"

    else:
        return "study_plan"
