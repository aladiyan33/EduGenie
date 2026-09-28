from unittest.mock import patch
from qna import answer_question
from summary_module import summarize_text
from learning_path import create_learning_path
from quiz_module import generate_quiz

def test_qna_rejects_empty_question():
    try: answer_question(" ")
    except ValueError: return
    assert False

def test_summary_uses_generator():
    with patch("summary_module.generate_text", return_value="summary"):
        assert summarize_text("A long passage") == "summary"

def test_learning_path_uses_generator():
    with patch("learning_path.generate_text", return_value="path"):
        assert create_learning_path("Python", "build ML projects") == "path"

def test_quiz_parses_json():
    payload = '{"title":"Python Quiz","questions":[{"question":"2+2?","options":["1","2","4","5"],"answer":"C","explanation":"Two plus two is four."}]}'
    with patch("quiz_module.generate_text", return_value=payload):
        quiz = generate_quiz("Python", 1)
    assert quiz["questions"][0]["answer"] == "C"
