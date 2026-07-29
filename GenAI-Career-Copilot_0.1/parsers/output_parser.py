from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import List
from models.schemas import InterviewResponse
from models.study_plan_models import StudyPlanResponse
from models.job_match_models import JobMatchResponse

class Parser(BaseModel):
    Resume_score: int =Field (description="Analyze the resume and provide Resume Score (0-100)")
    ATS_score: int =Field (description="Analyze the resume and provide ATS Score (0-100)")
    strengths: list[str] =Field (description="Analyze the resume and provide my strengths")
    Weakness: list[str] =Field (description="weak point found in my resume")
    missing_skills:List[str] =Field(description="Analyze the resume and provide  what are missing skills")
    

parser=PydanticOutputParser(pydantic_object=Parser)

interview_question_parser=PydanticOutputParser(pydantic_object=InterviewResponse)

study_plan_parser=PydanticOutputParser(pydantic_object=StudyPlanResponse)

job_matcher_parser=PydanticOutputParser(pydantic_object=JobMatchResponse)


