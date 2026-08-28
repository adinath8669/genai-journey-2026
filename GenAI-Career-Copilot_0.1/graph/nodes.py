from services.analysis_service import analyze_resume
from graph.state import GraphState


def resume_analysis_node(state:GraphState)->GraphState:
    if state.get("resume_analysis") is not None:
        return state

    result=analyze_resume(
        query=state['request'],
        index=state['index'],
        chunks=state['chunks']
    )

    return {**state ,"resume_analysis":result}

def skill_gap_node(state:GraphState)->GraphState:
    if state.get("skill_gap_result") is not None:
        return state # already cached — skip recompute

    missing_skills=state['resume_analysis'].missing_skills
    skill_gap_result={
        "missing_skills":missing_skills,
        "gap_summary":f"{len(missing_skills)} missing skill(s) identified"
    }

    return {**state ,"skill_gap_result":skill_gap_result}