from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_qna_endpoint():
    with patch("main.answer_question_with_gemini", return_value="Water is H2O."):
        response = client.post("/qa", json={"question": "What is water?"})
    assert response.status_code == 200
    assert response.json()["answer"] == "Water is H2O."


def test_summary_validation():
    response = client.post("/summarize", json={"text": ""})
    assert response.status_code == 422


def test_quiz_endpoint():
    payload = {
        "title": "Test Quiz",
        "questions": [
            {"question": "Q1", "options": ["A", "B", "C", "D"], "answer": "A", "explanation": "A"},
            {"question": "Q2", "options": ["A", "B", "C", "D"], "answer": "B", "explanation": "B"},
            {"question": "Q3", "options": ["A", "B", "C", "D"], "answer": "C", "explanation": "C"},
        ],
    }
    with patch("main.generate_quiz", return_value=payload):
        response = client.post("/quiz", json={"topic": "Python"})
    assert response.status_code == 200
    assert len(response.json()["questions"]) == 3
