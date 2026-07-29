from services.llm_service import llm
from prompts.job_match_prompt import job_match_prompt
from services.retrieval_service import retrieve_chunks
from parsers.output_parser import job_matcher_parser

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


    response = job_matcher_chain.invoke(
            {
                "context": "\n\n".join(retrieved_chunks)
            }
        )

    return response

    