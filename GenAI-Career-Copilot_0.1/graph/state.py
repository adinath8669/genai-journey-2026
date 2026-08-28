from typing import TypedDict,Optional,Any


class GraphState(TypedDict):

    request :str
    intent:str

    index :Any
    chunks :list[str]

    resume_analysis:Optional[dict]
    skill_gap_result :Optional[dict]