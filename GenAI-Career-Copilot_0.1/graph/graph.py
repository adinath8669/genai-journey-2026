from langgraph.graph import StateGraph, START, END

from graph.state import GraphState,GraphState2
from graph.nodes import (
    retrieve_node,
    generate_node,
    analyze_node,
    interview_node,
    study_plan_node,
    route_request
)


# --------------------------------------------------
# Create Graph
# --------------------------------------------------

builder = StateGraph(GraphState)
builder2 = StateGraph(GraphState2)


# --------------------------------------------------
# Add Nodes
# --------------------------------------------------

builder.add_node(
    "retrieve",
    retrieve_node
)

builder.add_node(
    "generate",
    generate_node
)

builder2.add_node("analyze", analyze_node)
builder2.add_node("interview", interview_node)
builder2.add_node("study_plan", study_plan_node)


# --------------------------------------------------
# Add Edges
# --------------------------------------------------

builder.add_edge(
    START,
    "retrieve"
)

builder.add_edge(
    "retrieve",
    "generate"
)

builder.add_edge(
    "generate",
    END
)

builder2.add_edge(
    START,
    "analyze"
)

# Conditional routing
builder2.add_conditional_edges(
    "analyze",
    route_request,
    {
        "interview": "interview",
        "study_plan": "study_plan"
    }
)


# Both branches → END
builder2.add_edge(
    "interview",
    END
)

builder2.add_edge(
    "study_plan",
    END
)


# --------------------------------------------------
# Compile Graph
# --------------------------------------------------

graph = builder.compile()
graph2 = builder2.compile()
