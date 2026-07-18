from langchain_google_genai import ChatGoogleGenerativeAI

from config import api_key,TEMPERATURE,LLM_MODEL
from prompts import CLASSIFIER_PROMPT,SUMMARY_PROMPT,TEACHER_PROMPT,INTERVIEW_PROMPT

llm=ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    google_api_key=api_key,
    temperature=TEMPERATURE
)


def classify(question :str)->str:
    prompt=f"{CLASSIFIER_PROMPT}\n\n{question}"
    response=llm.invoke(prompt)

    return response.content.strip().lower()


def teacher(question :str)->str:
    prompt=TEACHER_PROMPT.format(question=question)

    return llm.invoke(prompt).content


def interview(question :str)->str:
    prompt=INTERVIEW_PROMPT.format(question=question)

    return llm.invoke(prompt).content

def summary(text):
    prompt = SUMMARY_PROMPT.format(text=text)

    return llm.invoke(prompt).content

