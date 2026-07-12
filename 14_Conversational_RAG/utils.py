def export_chat_history(chat_history):

    conversation = ""

    for message in chat_history.messages:

        if message.type == "human":
            conversation += f"User: {message.content}\n\n"

        elif message.type == "ai":
            conversation += f"Assistant: {message.content}\n\n"

    return conversation


def export_markdown(chat_history):

    md = "# Conversation History\n\n"

    for message in chat_history.messages:

        if message.type == "human":
            md += f"## 👤 User\n{message.content}\n\n"

        else:
            md += f"## 🤖 Assistant\n{message.content}\n\n"

    return md