from services.llm_service import llm
from prompts.job_match_prompt import job_match_prompt
from services.retrieval_service import retrieve_chunks
from parsers.output_parser import job_matcher_parser
import logging

logger = logging.getLogger(__name__)


job_matcher_chain=job_match_prompt|llm|job_matcher_parser

def generate_job_matches(query:str,index,chunks):
    """
    Generate personalized job recommendations
    using RAG and Gemini.

    Flow:
    Retrieve resume context
    ↓
    PromptTemplate
    ↓
    Gemini
    ↓
    Structured Output
    """

    retrieved_chunks=retrieve_chunks(
        query=query,
        index=index,
        chunks=chunks
    )


    try:
        response = job_matcher_chain.invoke(
                {
                    "context": "\n\n".join(retrieved_chunks)
                }
            )

    except Exception as e:
        logger.error(f"Job matching failed: {type(e).__name__}: {e}")
        raise ValueError(
            f"Job matching failed: {type(e).__name__}: {e}"
        )from e

    logger.info("Job matching completed successfully.")
    return response

    