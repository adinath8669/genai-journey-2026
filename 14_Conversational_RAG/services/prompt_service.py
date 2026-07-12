from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)

from services.memory_service import chat_history


def chat(user_input, retrieved_chunks):

    context = "\n\n".join(retrieved_chunks)

    system = SystemMessage(
        content=f"""
You are a helpful AI assistant.

Answer ONLY from the context below.

Context:
{context}
"""
    )

    messages = [system]

    messages.extend(chat_history.messages)

    messages.append(HumanMessage(content=user_input))

    chat_history.add_user_message(user_input)

    return messages