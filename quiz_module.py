import json
import re
from gemini_client import generate_text


def _extract_json(text: str) -> dict:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        lines = cleaned.splitlines()
        cleaned = "\n".join(lines[1:-1]).strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as exc:
        match = re.search(r"\{.*\}", cleaned, flags=re.S)
        if not match:
            raise ValueError("Quiz model returned invalid JSON.") from exc
        return json.loads(match.group(0))


def generate_quiz(topic: str, num_questions: int = 5) -> dict:
    topic = topic.strip()
    if not topic:
        raise ValueError("Topic cannot be empty.")
    if not 1 <= num_questions <= 15:
        raise ValueError("Number of questions must be between 1 and 15.")
    prompt = f'''Generate {num_questions} multiple-choice questions about "{topic}" for a student.
Return ONLY valid JSON with this shape:
{{"title":"string","questions":[{{"question":"string","options":["A","B","C","D"],"answer":"A","explanation":"short explanation"}}]}}
The answer field must be exactly A, B, C, or D. Avoid trick questions.'''
    data = _extract_json(generate_text(prompt))
    questions = data.get("questions")
    if not isinstance(questions, list) or not questions:
        raise ValueError("Quiz response did not contain questions.")
    normalized = []
    for item in questions[:num_questions]:
        options = item.get("options", [])
        answer = str(item.get("answer", "")).upper()
        if len(options) != 4 or answer not in {"A", "B", "C", "D"}:
            raise ValueError("Invalid quiz question returned by model.")
        normalized.append({"question": str(item.get("question", "")).strip(), "options": [str(x).strip() for x in options], "answer": answer, "explanation": str(item.get("explanation", "")).strip()})
    return {"title": str(data.get("title", f"{topic} Quiz")), "questions": normalized}
