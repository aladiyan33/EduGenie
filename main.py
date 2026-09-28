from pathlib import Path
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from explanation_module import explain_topic
from learning_path import create_learning_path
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="EduGenie", description="Google Gemini powered learning assistant for students.", version="1.0.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

class ExplainRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=500)
    level: str = "beginner"
class QnARequest(BaseModel):
    question: str = Field(min_length=1, max_length=5000)
class QuizRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=500)
    num_questions: int = Field(default=5, ge=1, le=15)
class SummaryRequest(BaseModel):
    text: str = Field(min_length=1, max_length=20000)
    length: str = "medium"
class LearningPathRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=500)
    goal: str = Field(default="learn the topic", max_length=500)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.get("/health")
async def health():
    return {"status": "ok", "service": "EduGenie"}
@app.post("/api/explain")
async def explain(payload: ExplainRequest):
    try: return {"result": explain_topic(payload.topic, payload.level)}
    except Exception as exc: raise HTTPException(status_code=500, detail=str(exc)) from exc
@app.post("/api/qna")
async def qna(payload: QnARequest):
    try: return {"result": answer_question(payload.question)}
    except Exception as exc: raise HTTPException(status_code=500, detail=str(exc)) from exc
@app.post("/api/quiz")
async def quiz(payload: QuizRequest):
    try: return generate_quiz(payload.topic, payload.num_questions)
    except Exception as exc: raise HTTPException(status_code=500, detail=str(exc)) from exc
@app.post("/api/summary")
async def summary(payload: SummaryRequest):
    try: return {"result": summarize_text(payload.text, payload.length)}
    except Exception as exc: raise HTTPException(status_code=500, detail=str(exc)) from exc
@app.post("/api/learning-path")
async def learning_path(payload: LearningPathRequest):
    try: return {"result": create_learning_path(payload.topic, payload.goal)}
    except Exception as exc: raise HTTPException(status_code=500, detail=str(exc)) from exc
