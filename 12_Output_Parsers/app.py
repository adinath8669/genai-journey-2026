from prompts import prompt_template,resume_prompt
from model import llm
from parser import parser,parser2

def main():
    interview_chain = prompt_template() | llm | parser

    result = interview_chain.invoke({"topic": "Machine Learning"})

    print("=" * 50)
    print("Interview Questions")
    print("=" * 50)

    # Debug
    # print(result)

    for i, q in enumerate(result["questions"], 1):
        print(f"{i}. {q}")

    print("\n" + "=" * 50)

    resume_chain = resume_prompt() | llm | parser2

    resume_result = resume_chain.invoke(
        {"skills": "Python, FastAPI, SQL"}
    )

    print("Strengths:")
    print(resume_result.strengths)

    print("\nMissing Skills:")
    print(resume_result.missing_skills)

    print("\nSuggestions:")
    print(resume_result.suggestions)

if __name__ == "__main__":
    main()