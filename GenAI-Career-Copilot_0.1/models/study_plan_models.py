from pydantic import BaseModel,Field
from typing import List

class StudyTask(BaseModel):
   topic : str=Field(description="The specific subject or topic to be studied.")
   goal:str=Field(description="The primary objective or learning outcome for this task.")
   mini_project:str=Field(description="A practical, hands-on mini project to apply the learned concepts.")
   resources: List[str] = Field(default_factory=list, description="A list of links, books, or documentation for study material.")
   interview_questions: List[str] = Field(  default_factory=list, description="Common interview questions related to this topic.")
   estimated_hours: int | None = None


class WeekPlan(BaseModel):
   week_number:int = Field(description="The sequential number of the week (e.g., 1, 2, 3).")
   week_goal:str = Field(description="The overarching theme or goal for the entire week.")
   study_tasks:list[StudyTask]=Field(description="The list of specific study tasks to complete this week.")
   deliverable: str | None = None

class StudyPlanResponse(BaseModel):
    weeks: List[WeekPlan] = Field(
        ..., 
        description="A chronological list of weekly plans that make up the entire study roadmap."
    )