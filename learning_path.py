from gemini_client import generate_text


def create_learning_path(topic: str, goal: str = "learn the topic") -> str:
    topic = topic.strip()
    goal = goal.strip() or "learn the topic"
    if not topic:
        raise ValueError("Topic cannot be empty.")
    prompt = f"""
Create a practical learning path for the topic "{topic}".
Student goal: {goal}

Organize the answer into Beginner, Intermediate, and Advanced.
For every level include topics, a short purpose, and a small practice activity.
Finish with a suggested sequence and realistic weekly milestones.
"""
    return generate_text(prompt)
