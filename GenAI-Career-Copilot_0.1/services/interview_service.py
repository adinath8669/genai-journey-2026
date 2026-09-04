from services.llm_service import llm
from services.retrieval_service import retrieve_chunks
from prompts.interview_prompt import interview_prompt
from parsers.output_parser import interview_question_parser
import logging

logger = logging.getLogger(__name__)

interview_question_chain = interview_prompt|llm|interview_question_parser


def generate_interview_questions(query:str,index ,chunks):

    retrieved_chunks=retrieve_chunks(
        query=query,
        index=index,
        chunks=chunks
    )

    try:

        response = interview_question_chain.invoke(
            {
                "context": "\n\n".join(retrieved_chunks)
            }
        )

    except Exception as e:
        logger.error(f"Interview question generation failed: {type(e).__name__}: {e}")
        raise ValueError(
            f"Interview question generation failed: {type(e).__name__}: {e}"
        )from e

    logger.info("Interview questions generated successfully.")
    return response