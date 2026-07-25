from services.llm_service import llm
from services.retrieval_service import retrieve_chunks
from prompts.interview_prompt import interview_prompt
from parsers.output_parser import interview_question_parser

interview_question_chain = interview_prompt|llm|interview_question_parser


def generate_interview_questions(query:str,index ,chunks):

    retrieved_chunks=retrieve_chunks(
        query=query,
        index=index,
        chunks=chunks
    )

    response = interview_question_chain.invoke(
        {
            "context": "\n\n".join(retrieved_chunks)
        }
    )

    return response