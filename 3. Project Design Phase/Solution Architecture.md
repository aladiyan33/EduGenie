EDUGENIE — SOLUTION ARCHITECTURE

Presentation Layer
Browser — HTML + CSS + JavaScript.

Application Layer
FastAPI: /qa, /explain, /quiz, /summarize, /learn/recommendations.

Feature Layer
Q&A, Explanation, Quiz, Summary, Learning Path modules.

AI Layer
Gemini API and local LaMini-Flan-T5-783M.

Infrastructure
Uvicorn, Python environment and environment variables.

Testing Layer
pytest, FastAPI TestClient/httpx, GitHub Actions.

Request sequence
Browser → FastAPI → Feature Module → AI Model → FastAPI → Browser.
