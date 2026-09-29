EDUGENIE — SOLUTION ARCHITECTURE

Presentation: Browser → HTML/CSS/JavaScript.
Application: FastAPI routes /qa, /explain, /quiz, /summarize, /learn/recommendations.
Feature layer: Q&A, Explanation, Quiz, Summary, Learning Path modules.
AI layer: Gemini API and local LaMini-Flan-T5-783M.
Infrastructure: Uvicorn, Python environment, environment variables.
Testing: pytest, FastAPI TestClient/httpx, GitHub Actions.

Request sequence: Browser → FastAPI → Feature Module → AI Model → FastAPI → Browser.