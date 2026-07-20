from services.llm_service import llm
from parsers.output_parser import parser
from prompts.resume_prompt import resume_prompt
from services.retrieval_service import retrieve_chunks



# Build the chain once
resume_analysis_chain = resume_prompt | llm | parser

def analyze_resume(query: str, index, chunks):
    """
    Analyze a resume using RAG.

    Flow:
    Query -> Retrieve relevant chunks -> LLM -> Structured Response

    Args:
        query: User query (e.g. "Analyze this resume")
        index: FAISS vector index
        chunks: Resume text chunks

    Returns:
        Parsed resume analysis
    """

       # Retrieve relevant resume chunks
    retrieved_chunks = retrieve_chunks(
        query=query,
        index=index,
        chunks=chunks
    )

    # Invoke the LangChain pipeline
    response = resume_analysis_chain.invoke(
        {
            "context": "\n\n".join(retrieved_chunks)
        }
    )

    return response