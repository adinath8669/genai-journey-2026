from graph.graph import graph
import streamlit as st

def run_career_copilot_graph(request:str,index,chunks)->dict:
    return graph.invoke({
        "request":request,
        "intent":"",
        "index":index,
        "chunks":chunks,
        "resume_analysis":st.session_state.resume_analysis,
        "skill_gap_result": st.session_state.skill_gap_result,
        "interview_result": None,
        "study_plan_result": None,
        "job_match_result": None

    })