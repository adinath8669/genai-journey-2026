from langchain_core.prompts import PromptTemplate
from parsers.output_parser import parser


resume_prompt=PromptTemplate.from_template(
    """
    You are an expert AI Resume Reviewer.

Using ONLY the resume context below, analyze the resume.

Resume Context:
{context}

Task:
Analyze the resume and provide:

1. Resume Score (0-100)
2. ATS Score (0-100)
3. Top Strengths
4. Weaknesses
5. Missing Skills

{format_instructions}

    """,
    partial_variables={"format_instructions":parser.get_format_instructions()}
)