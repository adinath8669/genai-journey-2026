from services import classify, teacher, interview, summary


def classifier_node(state):

    category = classify(state["question"])

    return {
        "category": category
    }


def teacher_node(state):

    answer = teacher(state["question"])

    return {
        "answer": answer
    }


def interview_node(state):

    answer = interview(state["question"])

    return {
        "answer": answer
    }


def summary_node(state):

    answer = summary(state["answer"])

    return {
        "answer": answer
    }