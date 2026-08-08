from pydantic import BaseModel,Field

class JobDescription(BaseModel):
    overall_match_score : int =Field(description="Overall match score between the resume and the job description (0-100)")
    matched_skills:list[str] = Field(description="Skills found in both the resume and the job description.")
    missing_skills:list[str] = Field(description="Skills required in the job description but missing from the resume.")
    resume_weakness:list[str] = Field(description="Weak areas in the resume for this job description.")
    ats_suggestions: list[str] = Field(description="Suggestions to improve ATS compatibility.")
    resume_improvements:list[str] = Field(description="Recommendations to improve the resume.")
    final_recommendation:str =Field(description="Overall recommendation for the candidate.")