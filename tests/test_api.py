from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_qna_endpoint():
    with patch("main.answer_question", return_value="Water is H2O."):
        response = client.post("/api/qna", json={"question": "What is water?"})
    assert response.status_code == 200
    assert response.json()["result"] == "Water is H2O."

def test_summary_validation():
    response = client.post("/api/summary", json={"text": ""})
    assert response.status_code == 422
