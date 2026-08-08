from services.llm_service import llm
from parsers.output_parser import job_description_parser
from prompts.job_description_prompt import job_description_prompt
from services.retrieval_service import retrieve_chunks


job_description_chain=job_description_prompt|llm|job_description_parser

def analyze_job_description(query:str,index,chunks,job_description:str):
    """
    Compare the uploaded resume with a job description
    and return a structured match analysis.
    """
    retrieved_chunks=retrieve_chunks(
        query=query,
        index=index,
        chunks=chunks
    )

    response=job_description_chain.invoke(
         {
            "context": "\n\n".join(retrieved_chunks),
            "job_description":job_description
         }
    )

    return response