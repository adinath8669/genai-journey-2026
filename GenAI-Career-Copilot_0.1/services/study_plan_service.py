from services.llm_service import llm
from services.retrieval_service import retrieve_chunks
from prompts.study_plan_prompt import studyPlanPrompt
from parsers.output_parser import study_plan_parser
import logging

logger = logging.getLogger(__name__)

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

    try:

        response = study_plan_chain.invoke(
            {
                "resume_context": "\n\n".join(retrieved_chunks)
            }
        )

    except Exception as e:
        logger.error(f"Study plan generation failed: {type(e).__name__}: {e}")
        raise ValueError(
             f"Study plan generation failed: {type(e).__name__}: {e}"
        )from e

    logger.info("Study plan generated successfully.")
    return response