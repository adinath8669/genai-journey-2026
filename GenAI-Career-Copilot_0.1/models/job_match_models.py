from pydantic import BaseModel,Field

class JobRecommendation(BaseModel):
    role : str=Field(description="Recommended job role based on the candidate's resume.")
    match_score:int=Field(description="Estimated resume match score for this role (0–100).")
    recommendation_reason :str=Field(description="Reason why this role matches the candidate's resume.")
    missing_skills:list[str]=Field(description="Skills missing from the candidate's resume for this role.")
    next_steps: list[str]=Field(description="Recommended next steps to improve suitability for this role.")

class JobMatchResponse(BaseModel):
    recommended_jobs : list[JobRecommendation]=Field(description="Top recommended job roles ranked by match score.")

