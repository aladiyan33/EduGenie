from gemini_client import generate_text


def summarize_text(text: str) -> str:
    text = text.strip()
    if not text:
        raise ValueError("Text cannot be empty.")

    prompt = f"""
Summarize the following educational passage for a student.
Keep the important ideas, key facts, and relationships.
Use short paragraphs or bullet points where helpful.
Do not invent information that is not present in the source.

Passage:
{text}
"""
    return generate_text(prompt)
