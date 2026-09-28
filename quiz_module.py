import json
import re

from gemini_client import generate_text


def _parse_quiz(text: str) -> dict:
    cleaned = text.strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as exc:
        match = re.search(r"\{.*\}", cleaned, flags=re.S)
        if not match:
            raise ValueError("Quiz model returned invalid JSON.") from exc
        return json.loads(match.group(0))


def generate_quiz(topic: str, num_questions: int = 3) -> dict:
    topic = topic.strip()
    if not topic:
        raise ValueError("Topic cannot be empty.")

    prompt = f"""
Create exactly {num_questions} multiple-choice questions about "{topic}".

Return ONLY valid JSON:
{{
  "title": "Quiz title",
  "questions": [
    {{
      "question": "Question text",
      "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
      "answer": "Option 1",
      "explanation": "Short explanation of the correct answer"
    }}
  ]
}}

Rules:
- Exactly four options for every question.
- The answer must exactly match one option.
- Questions should test understanding, not trivia.
- Do not use markdown or code fences.
"""

    data = _parse_quiz(generate_text(prompt))
    questions = data.get("questions")

    if not isinstance(questions, list) or len(questions) != num_questions:
        raise ValueError("Quiz response did not contain the expected number of questions.")

    normalized = []
    for item in questions:
        if not isinstance(item, dict):
            raise ValueError("Invalid quiz question returned by model.")

        options = item.get("options")
        answer = str(item.get("answer", "")).strip()

        if not isinstance(options, list) or len(options) != 4:
            raise ValueError("Each quiz question must contain exactly four options.")

        options = [str(option).strip() for option in options]
        if not answer or answer not in options:
            raise ValueError("Quiz answer must exactly match one of the options.")

        normalized.append({
            "question": str(item.get("question", "")).strip(),
            "options": options,
            "answer": answer,
            "explanation": str(item.get("explanation", "")).strip(),
        })

    return {
        "title": str(data.get("title", f"{topic} Quiz")),
        "questions": normalized,
    }
