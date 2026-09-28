from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> str:
    topic = topic.strip()
    if not topic:
        raise ValueError("Topic cannot be empty.")

    prompt = f"""
You are EduGenie, an AI tutor.
Create a structured learning path for "{topic}".

Organize it as:
1. Beginner Level
2. Intermediate Level
3. Advanced Level

For each level provide:
- Main topics to study
- Recommended learning resources
- A realistic estimated duration
- A small practice task

End with practical learning tips and a suggested order.
Keep the recommendations useful for a student.
"""
    return generate_text(prompt)


create_learning_path = get_learning_recommendations
