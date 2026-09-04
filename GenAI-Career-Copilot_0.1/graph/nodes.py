from services.analysis_service import analyze_resume
from services.interview_service import generate_interview_questions
from services.study_plan_service import generate_study_plan
from services.job_match_service import generate_job_matches
from graph.state import GraphState
import logging

logger = logging.getLogger(__name__)


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


def analyze_node(state :GraphState)->GraphState:
    request=state["request"].lower()

    if "interview" in request:
        intent="interview"
    elif "study" in request or "plan" in request:
        intent="study_plan"
    elif "job" in request or "role"  in request or "match" in request:
        intent="job_match"
    else :
        intent="unknown"

    logger.info(f"Routed request '{state['request']}' to intent: {intent}")
    return {**state, "intent":intent}

def router_request(state: GraphState)->str:
    return state["intent"]


def interview_node(state: GraphState)->GraphState:
    result=generate_interview_questions(
        query=state["request"],
        index=state["index"],
        chunks=state["chunks"]
    )

    return {**state , "interview_result":result}

def study_plan_prep_node(state : GraphState)->GraphState:
    print (f"[study_paln_prep] gaps to plan around : {state['skill_gap_result']['missing_skills']}")
    return state

def study_plan_generate_node(state:GraphState)->GraphState:
    result=generate_study_plan(
        query=state["request"],
        index=state["index"],
        chunks=state["chunks"]
    )

    return {**state, "study_plan_result":result}

def job_match_node(state:GraphState)->GraphState:
    result=generate_job_matches(
        query=state["request"],
        index=state["index"],
        chunks=state["chunks"]
    )

    return {**state ,"job_match_result":result}

def unknown_node(state: GraphState) -> GraphState:
    return {
        **state,
        "interview_result": None,
        "study_plan_result": None,
        "job_match_result": None
    }

