from gemini_client import generate_text


def answer_question_with_gemini(question: str) -> str:
    question = question.strip()
    if not question:
        raise ValueError("Question cannot be empty.")

    prompt = f"""
You are EduGenie, an AI tutor for students.
Answer the following question clearly and accurately.
Use simple language suitable for a learner. Give a concise answer first,
then add a short explanation or example when useful.

Question:
{question}
"""
    return generate_text(prompt)


answer_question = answer_question_with_gemini
