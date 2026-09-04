from graph.nodes import analyze_node


def make_state(request: str) -> dict:
    """
    Minimal fake GraphState — analyze_node only reads state["request"],
    so that's all we need to provide for this test.
    """
    return {
        "request": request,
        "intent": "",
        "index": None,
        "chunks": [],
        "resume_analysis": None,
        "skill_gap_result": None,
        "interview_result": None,
        "study_plan_result": None,
        "job_match_result": None
    }


def test_analyze_node_routes_interview_requests():
    state = make_state("I want interview questions")
    result = analyze_node(state)
    assert result["intent"] == "interview"


def test_analyze_node_routes_study_plan_requests_via_study_keyword():
    state = make_state("Create a study schedule for me")
    result = analyze_node(state)
    assert result["intent"] == "study_plan"


def test_analyze_node_routes_study_plan_requests_via_plan_keyword():
    state = make_state("Generate a 30-day plan")
    result = analyze_node(state)
    assert result["intent"] == "study_plan"


def test_analyze_node_routes_job_match_requests():
    state = make_state("What job roles match my resume?")
    result = analyze_node(state)
    assert result["intent"] == "job_match"


def test_analyze_node_routes_unknown_requests():
    state = make_state("What is the capital of France?")
    result = analyze_node(state)
    assert result["intent"] == "unknown"


def test_analyze_node_preserves_rest_of_state():
    """
    analyze_node should only add/update "intent" — it shouldn't
    lose or overwrite any other existing state fields.
    """
    state = make_state("interview")
    state["resume_analysis"] = {"fake": "data"}

    result = analyze_node(state)

    assert result["resume_analysis"] == {"fake": "data"}
    assert result["request"] == "interview"