from langgraph.graph import StateGraph, START, END

from models import GraphState
from nodes import (
    classifier_node,
    teacher_node,
    interview_node,
    summary_node,
)

builder = StateGraph(GraphState)

# Add Nodes
builder.add_node("classifier", classifier_node)
builder.add_node("teacher", teacher_node)
builder.add_node("interview", interview_node)
builder.add_node("summary", summary_node)

# Start
builder.add_edge(START, "classifier")


def router(state):

    if state["category"] == "python":
        return "teacher"

    elif state["category"] == "interview":
        return "interview"

    else:
        return "summary"


builder.add_conditional_edges(
    "classifier",
    router,
    {
        "teacher": "teacher",
        "interview": "interview",
        "summary": "summary",
    },
)

builder.add_edge("teacher", END)
builder.add_edge("interview", END)
builder.add_edge("summary", END)

graph = builder.compile()