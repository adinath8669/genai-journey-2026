from langgraph.graph import StateGraph,START,END
from graph.state import GraphState
from graph.nodes import (
    resume_analysis_node,
    skill_gap_node,
    analyze_node,
    interview_node,
    study_plan_prep_node,
    study_plan_generate_node,
    job_match_node,
    unknown_node,
    router_request
)

builder= StateGraph(GraphState)

builder.add_node("resume_analysis",resume_analysis_node)
builder.add_node("skill_gap",skill_gap_node)
builder.add_node("analyze",analyze_node)
builder.add_node("interview",interview_node)
builder.add_node("study_paln_prep",study_plan_prep_node)
builder.add_node("study_plan_genrate",study_plan_generate_node)
builder.add_node("job_match",job_match_node)
builder.add_node("unknown", unknown_node)

builder.add_edge(START,"resume_analysis")
builder.add_edge("resume_analysis","skill_gap")
builder.add_edge("skill_gap","analyze")

builder.add_conditional_edges(
    "analyze",
    router_request,
    {
        "interview":"interview",
        "study_plan":"study_paln_prep",
        "job_match":"job_match",
        "unknown": "unknown"

    }
)

builder.add_edge("interview",END)
builder.add_edge("study_paln_prep","study_plan_genrate")
builder.add_edge("study_plan_genrate",END)
builder.add_edge("job_match",END)
builder.add_edge("unknown", END)


graph=builder.compile()
