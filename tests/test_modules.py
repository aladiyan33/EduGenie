from unittest.mock import patch

from learning_path import create_learning_path
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text


def test_qna_rejects_empty_question():
    try:
        answer_question(" ")
    except ValueError:
        return
    assert False


def test_summary_uses_generator():
    with patch("summary_module.generate_text", return_value="summary"):
        assert summarize_text("A long passage") == "summary"


def test_learning_path_uses_generator():
    with patch("learning_path.generate_text", return_value="path"):
        assert create_learning_path("Python") == "path"


def test_quiz_parses_json():
    payload = '{"title":"Python Quiz","questions":[{"question":"2+2?","options":["1","2","4","5"],"answer":"4","explanation":"Two plus two is four."},{"question":"3+3?","options":["5","6","7","8"],"answer":"6","explanation":"Three plus three is six."},{"question":"4+4?","options":["7","8","9","10"],"answer":"8","explanation":"Four plus four is eight."}]}'
    with patch("quiz_module.generate_text", return_value=payload):
        quiz = generate_quiz("Python")
    assert len(quiz["questions"]) == 3
    assert quiz["questions"][0]["answer"] == "4"
