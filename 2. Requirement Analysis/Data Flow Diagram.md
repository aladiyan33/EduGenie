EDUGENIE — DATA FLOW DIAGRAM

Student → HTML/CSS/JavaScript Web Interface → FastAPI → Feature Module → Gemini API or Local LaMini-Flan-T5-783M → FastAPI Response → Browser

Endpoints
POST /qa
POST /explain
POST /quiz
POST /summarize
POST /learn/recommendations

Detailed flow
1. Student enters input.
2. Frontend sends HTTP POST request.
3. Pydantic validates input.
4. FastAPI routes to a feature module.
5. Gemini handles Q&A, quiz, summarization and recommendations.
6. Local LaMini handles concept explanation.
7. Result is returned and rendered by JavaScript.
