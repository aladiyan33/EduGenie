# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant for the SkillWallet project. It provides question answering, concept simplification, quiz generation, summarization, and personalized learning paths through a FastAPI web application.

## Features
- Question & Answer — Gemini answers student questions clearly.
- Explain — local LaMini-Flan-T5-783M explains concepts at multiple levels.
- Quiz — Gemini creates validated multiple-choice questions.
- Summary — Gemini condenses long study passages.
- Learning Path — Gemini creates a Beginner → Intermediate → Advanced route.
- Responsive HTML/CSS/JavaScript interface.
- REST APIs, health endpoint, automated tests, and GitHub Actions.

## Architecture
Student → HTML/CSS/JavaScript → FastAPI → selected module → Gemini or local LaMini model → browser result.

## Technology
- Python 3.11+
- FastAPI + Uvicorn
- Jinja2
- Google GenAI Python SDK (google-genai)
- Gemini 3.8 Flash by default
- Hugging Face Transformers + PyTorch
- HTML5 / CSS3 / JavaScript
- pytest

Google's current Gemini documentation recommends the google-genai Python SDK and documents Gemini 3.8 Flash. The older Gemini 1.5 setup in the reference video is therefore treated as historical guidance rather than the implementation target.

## Setup
1. Create and activate a Python 3.11+ virtual environment.
2. Install dependencies with: python -m pip install -r requirements.txt
3. Copy .env.example to .env.
4. Add GEMINI_API_KEY=your_api_key_here.
5. Run: uvicorn main:app --reload
6. Open http://127.0.0.1:8000

## Explain module
The LaMini model is loaded lazily when Explain is first used. It requires PyTorch and Transformers and downloads the model from Hugging Face on first use. This keeps normal server startup lightweight.

## API Endpoints
- GET / — web application
- GET /health — health check
- POST /api/explain — local concept explanation
- POST /api/qna — Gemini Q&A
- POST /api/quiz — Gemini quiz generation
- POST /api/summary — Gemini summarization
- POST /api/learning-path — Gemini learning path

## Testing
Run: pytest -q
AI generation is mocked in tests where appropriate, so tests do not require a live Gemini API key.

## Security
- .env is ignored by Git.
- Never commit Gemini API keys.
- API inputs are validated with Pydantic.
- Quiz responses are parsed and validated before reaching the frontend.

## SkillWallet Deliverables
- GitHub: this repository
- Documentation: this README and source
- Demo: screen-record the running application and each task
- Submission: provide the GitHub link, documentation, and demo video in SkillWallet

## Project Structure
EduGenie/
├── main.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── templates/index.html
├── static/style.css
├── tests/test_modules.py
├── tests/test_api.py
├── .github/workflows/tests.yml
├── requirements.txt
├── .env.example
└── .gitignore
