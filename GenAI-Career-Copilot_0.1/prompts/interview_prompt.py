from langchain_core.prompts import PromptTemplate
from parsers.output_parser import interview_question_parser

interview_prompt=PromptTemplate.from_template(
    """
You are an expert technical interviewer.

Use ONLY the information available in the resume context.

Do not invent projects, skills, or experience that are not mentioned in the resume.

Generate interview questions that are directly related to the candidate's experience and skills

Resume Context:
{context}
Task:
Analyze the resume and provide:

1. 10 Technical interview questions
2. 5 Behavioral interview questions
3. 5 Projects based interview questions
4. 5 Follow-up interview questions
 
{format_instructions}
    """,
    partial_variables={"format_instructions":interview_question_parser.get_format_instructions()}

)