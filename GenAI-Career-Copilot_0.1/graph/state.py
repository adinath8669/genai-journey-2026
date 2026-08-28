from typing import TypedDict


class GraphState(TypedDict):
    """
    State shared between LangGraph nodes.
    """

    question: str
    index: object
    chunks: list[str]
    retrieved_chunks: list[str]
    answer: str


class GraphState2(TypedDict):
    request: str
    result: str
