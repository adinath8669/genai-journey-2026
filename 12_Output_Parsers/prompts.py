from langchain_core.prompts import PromptTemplate
from parser import parser,parser2

def prompt_template():
    templet = PromptTemplate(
        template="""
            Give me 5 interview questions on the topic: {topic}

            {format_instructions}
            """,
        input_variables=["topic"],
        partial_variables={ "format_instructions": parser.get_format_instructions()}

    )
    return templet


def resume_prompt():
    templet2 = PromptTemplate(
        template="""
            The candidate has the following skills:

            {skills}

            Analyze the skills and provide:

            1. Strengths
            2. Missing Skills
            3. Suggestions

            {format_instructions}
                        """,
        input_variables=["skills"],
        partial_variables={ "format_instructions": parser2.get_format_instructions()}

    )
    return templet2



