from pydantic import BaseModel,Field
# from typing import List

class InterviewQuestion(BaseModel):
    question: str =Field (
        description="interview questions"
    )
    
    difficulty: str = Field(
        description="Difficulty level (Easy, Medium, Hard)"
    )

    answer: str = Field(
        description="Expected answer or key points the candidate should cover"
    )


class InterviewResponse(BaseModel):
    technical_questions: list[InterviewQuestion] =Field (description="techinical interview questions")
    behavioral_questions: list[InterviewQuestion] =Field (description="behavioral interview questions")
    project_questions: list[InterviewQuestion] =Field (description="project based interview questions")
    follow_up_questions: list[InterviewQuestion] =Field (description="follow_up interview questions")

