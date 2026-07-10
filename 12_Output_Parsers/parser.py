from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
 

parser=JsonOutputParser()

class ResumeFeedback(BaseModel):
    strengths:str =Field(description="as per input what is my strengets")
    missing_skills:str =Field(description="as per input what are missing skills")
    suggestions:str =Field(description="as per input what is your sugestion")

parser2=PydanticOutputParser(pydantic_object=ResumeFeedback)