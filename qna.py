from gemini_client import generate_text


def answer_question(question: str) -> str:
    question = question.strip()
    if not question:
        raise ValueError("Question cannot be empty.")
    prompt = """
You are EduGenie, a student-friendly educational assistant.
Answer the student's question accurately and clearly.
Use simple language, short paragraphs, and bullet points when useful.
If the question is ambiguous, state the assumption you are making.

Student question:
""" + question
    return generate_text(prompt)
