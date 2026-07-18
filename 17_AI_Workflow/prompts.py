SYSTEM_PROMPT= """
ACT as an supportive ai assistant and follow the instruction
"""

CLASSIFIER_PROMPT="""
classify the question into category only:

-teacher
-interview
-summary 

Return only category.

"""

TEACHER_PROMPT="""
You are an experienced programming teacher.

Answer the question clearly.

Question:
{question}

"""

INTERVIEW_PROMPT="""
you are an ai interviewer 

answare as you are preparing a candidate for interview


Question:
{question}
"""

SUMMARY_PROMPT="""
Summarize the following text in simple words.

{text}
"""
