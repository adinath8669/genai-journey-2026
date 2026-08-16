from services.llm_service import llm
from services.retrieval_service import retrieve_chunks
from prompts.chat_prompt import chat_prompt
from memory.memory import chat_history


chat_chain = chat_prompt | llm


def chat_with_resume(query, index, chunks):

    # 1. Retrieve relevant resume chunks
    retrieved_chunks = retrieve_chunks(
        query=query,
        index=index,
        chunks=chunks
    )

    # 2. Convert retrieved chunks into context
    context = "\n\n".join(retrieved_chunks)

    # 3. Convert conversation history into text
    history = chat_history.messages

    

    # 4. Send context + history + current question to LLM
    response = chat_chain.invoke(
        {
            "context": context,
            "history": history,
            "query": query
        }
    )

    # 5. Get text response
    answer = response.content

    # 6. Save current conversation
    chat_history.add_user_message(query)
    chat_history.add_ai_message(response.content)

    # 7. Return answer
    return answer