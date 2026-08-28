from langgraph.graph import StateGraph,START,END
from graph.state import GraphState
from graph.nodes import (
    resume_analysis_node,
    skill_gap_node
)

builder= StateGraph(GraphState)

builder.add_node("resume_analysis",resume_analysis_node)
builder.add_node("skill_gap",skill_gap_node)

builder.add_edge(START,"resume_analysis")
builder.add_edge("resume_analysis","skill_gap")


graph=builder.compile()
