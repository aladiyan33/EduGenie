from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from explanation_module import explain_topic
from learning_path import get_learning_recommendations
from qna import answer_question_with_gemini
from quiz_module import generate_quiz
from summary_module import summarize_text

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="EduGenie: Google Gemini Powered Learning Assistant",
    description="AI-powered educational assistant for questions, explanations, quizzes, summaries and learning recommendations.",
    version="2.0.0",
)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=5000)


class ExplainRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=500)


class QuizRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=500)


class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=20000)


class RecommendationRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=500)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={})


@app.get("/health")
async def health():
    return {"status": "ok", "service": "EduGenie"}


@app.post("/qa")
async def qa(payload: QuestionRequest):
    try:
        return {"answer": answer_question_with_gemini(payload.question)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/explain")
async def explain(payload: ExplainRequest):
    try:
        return {"explanation": explain_topic(payload.topic)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/quiz")
async def quiz(payload: QuizRequest):
    try:
        return generate_quiz(payload.topic)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/summarize")
async def summarize(payload: SummaryRequest):
    try:
        return {"summary": summarize_text(payload.text)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/learn/recommendations")
async def recommendations(payload: RecommendationRequest):
    try:
        return {"recommendations": get_learning_recommendations(payload.topic)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


# Backward-compatible aliases.
@app.post("/api/qna")
async def api_qna(payload: QuestionRequest):
    return await qa(payload)


@app.post("/api/explain")
async def api_explain(payload: ExplainRequest):
    return await explain(payload)


@app.post("/api/quiz")
async def api_quiz(payload: QuizRequest):
    return await quiz(payload)


@app.post("/api/summary")
async def api_summary(payload: SummaryRequest):
    return await summarize(payload)


@app.post("/api/learning-path")
async def api_learning_path(payload: RecommendationRequest):
    return await recommendations(payload)
