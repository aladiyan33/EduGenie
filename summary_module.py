from gemini_client import generate_text


def summarize_text(text: str, length: str = "medium") -> str:
    text = text.strip()
    if not text:
        raise ValueError("Text cannot be empty.")
    rules = {
        "short": "Give 3-5 concise bullet points.",
        "medium": "Give a compact summary with the key ideas and important details.",
        "long": "Give a detailed but focused summary while preserving the main ideas.",
    }
    prompt = "Summarize the following study material for a student. " + rules.get(length, rules["medium"]) + "\nDo not invent facts.\n\nSOURCE:\n" + text
    return generate_text(prompt)
