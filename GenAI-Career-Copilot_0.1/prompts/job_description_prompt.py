from langchain_core.prompts import PromptTemplate
from parsers.output_parser import job_description_parser

job_description_prompt=PromptTemplate.from_template(
    """
You are an experienced technical recruiter.

Use ONLY the resume context below.

Resume Context:
{context}

Job Description:
{job_description}

Evaluate:

1. Overall Match Score
2. Matching Skills
3. Missing Skills
4. Resume Strengths
5. Resume Improvements
6. Missing ATS Keywords
7. Final Recommendation


{format_instructions}
    """,
    partial_variables={"format_instructions":job_description_parser.get_format_instructions()}
)