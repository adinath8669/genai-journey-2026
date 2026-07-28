from langchain_core.prompts import PromptTemplate
from parsers.output_parser import study_plan_parser

studyPlanPrompt=PromptTemplate.from_template(
    """
You are an expert career coach and technical architect.

Resume Context:
{resume_context}
Use only the information from the resume context.
If a required skill is missing, recommend learning it.
Do not assume experience that is not mentioned.

Instructions:
1. Analyze the resume context provided above.
2. Identify missing skills required for their target career trajectory to become GenAI Engineer.
3. Prioritize learning based on foundational requirements.
4. Design a realistic roadmap spanning exactly 30 days (broken down by weeks).
5. Assume the user can dedicate 3–4 hours per day.
6. Recommend ONLY high-quality, free resources (e.g., official docs, free courses, YouTube).
7. Give exactly one hands-on mini project each week.
8. Include relevant technical interview questions for each topic.
    

{format_instruction}
    """,
    partial_variables={"format_instruction":study_plan_parser.get_format_instructions()}
)