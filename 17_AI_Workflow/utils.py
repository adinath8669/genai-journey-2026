def clean_text(text: str):

    return text.strip()


def validate_question(question: str):

    return len(question.strip()) > 0