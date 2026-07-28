from services.llm_service import llm
from services.retrieval_service import retrieve_chunks
from prompts.study_plan_prompt import studyPlanPrompt
from parsers.output_parser import study_plan_parser

study_plan_chain = studyPlanPrompt|llm|study_plan_parser


def generate_study_plan(query:str,index ,chunks):
    """
    Generate a personalized 30-day study plan
    based on the uploaded resume.
    """
    retrieved_chunks=retrieve_chunks(
        query=query,
        index=index,
        chunks=chunks
    )

    response = study_plan_chain.invoke(
        {
            "resume_context": "\n\n".join(retrieved_chunks)
        }
    )

    return response