from prompts.resume_prompt import resume_prompt
from services.llm_service import generate_response
from services.rag_service import retrieve_chunks


def analyze_resume(query, index, chunks):
    context = retrieve_chunks(query, index, chunks)
    # print(type(index))

    context = "\n\n".join(context)

    prompt = resume_prompt.format(
        context=context
    )

    return generate_response(prompt)