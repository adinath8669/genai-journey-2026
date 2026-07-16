from langgraph.graph import StateGraph,START,END
from state import GraphState
from nodes import teacher_node,interview_node,classifier_node

builder =StateGraph(GraphState)

builder.add_node("classifier",classifier_node)
builder.add_node("teacher",teacher_node)
builder.add_node("interview",interview_node)

builder.add_edge(START,"classifier")

def router(state):

    if state["category"] == "python":
        return "teacher"

    return "interview"

builder.add_conditional_edges("classifier",router)
builder.add_edge("teacher", END)
builder.add_edge("interview", END)

graph=builder.compile()


