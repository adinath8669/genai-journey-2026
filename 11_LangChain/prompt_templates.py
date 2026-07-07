from langchain_core.prompts import PromptTemplate
def prompt_templet(mode):
    if mode =="Teacher":
        mode="Explain in simple words."

    elif mode=="Coder":
        mode="Explain with Python examples."

    else:
        mode="Ask me 5 interview questions with answers"

    prompt = PromptTemplate(
        input_variables=["topic","mode"],
        template="""You are an AI assistant.
        Follow this instruction:
        {mode}
        Now answer the following topic:
        {topic}""")

    return prompt