from langchain_core.prompts import PromptTemplate
from parsers.output_parser import job_matcher_parser

job_match_prompt=PromptTemplate.from_template(
"""
You are an expert technical recruiter.

Use ONLY the resume context provided below.

Resume Context:
{context}

Task:

Based on the candidate's resume, Recommend the top 5 most suitable job roles.
Rank the roles from highest to lowest match score.
If the resume is missing critical skills for a role,
reduce the match score accordingly.

For each recommended role, provide:

1. Role name
2. Estimate a realistic match_score between 0 and 100 based only on the provided resume.
3. Reason for recommending this role
4. Only include skills that are genuinely missing or insufficiently demonstrated in the resume.
5. Recommend practical next steps such as:
    - Learn a technology
    - Build a project
    - Earn a certification
    - Practice interview topics

Recommend only roles that closely match the candidate's demonstrated skills and experience.
Do not recommend unrealistic senior or unrelated roles.

{format_instruction}
    """,
partial_variables={'format_instruction':job_matcher_parser.get_format_instructions()}

)