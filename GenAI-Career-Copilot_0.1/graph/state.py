from typing import TypedDict,Optional,Any


class GraphState(TypedDict):

    request :str
    intent:str

    index :Any
    chunks :list[str]

    resume_analysis:Optional[dict]
    skill_gap_result :Optional[dict]

    interview_result :Optional[dict]
    study_plan_result :Optional[dict]
    job_match_result :Optional[dict]