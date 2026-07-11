from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import List

class ResumeFeedback(BaseModel):
    resume_score :int= Field(description="Analyze the resume and provide Resume Score (0-100)")
    ats_score :int= Field(description="Analyze the resume and provide ATS Score (0-100)")
    strengths:List[str] =Field(description="Analyze the resume and provide s my strengets")
    weaknesses: List[str] = Field(description="Weak points found in the resume")
    missing_skills:List[str] =Field(description="Analyze the resume and provide  what are missing skills")

parser2=PydanticOutputParser(pydantic_object=ResumeFeedback)