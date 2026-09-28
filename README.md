# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered learning assistant built for the SkillWallet project. It provides question answering, concept explanation, quiz generation, summarization, and personalized learning paths through a FastAPI web application.

## Features

- Question & Answer powered by Gemini
- Simple concept explanations using a local LaMini-Flan-T5 model
- Multiple-choice quiz generation
- Passage summarization
- Beginner → intermediate → advanced learning paths
- Responsive HTML/CSS interface
- REST API endpoints for every learning module

## Architecture

Student → FastAPI → selected module → Gemini / local LaMini model → result → HTML frontend

## Tech Stack

- Python 3.11+
- FastAPI
- Uvicorn
- Jinja2
- Google GenAI Python SDK
- Gemini 3.8 Flash
- Hugging Face Transformers
- PyTorch
- HTML5 / CSS3 / JavaScript

## Setup

1. Create and activate a virtual environment.
2. Install dependencies with `python -m pip install -r requirements.txt`.
3. Copy `.env.example` to `.env`.
4. Put your Gemini API key in `GEMINI_API_KEY`.
5. Start the application:

```bash
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000`.

## Notes

The local LaMini model is loaded lazily when the Explain feature is first used. This keeps the server startup lightweight and makes the rest of the application usable while the local model is unavailable.

Never commit `.env` or API keys to GitHub.

## SkillWallet Deliverables

- GitHub repository: this repository
- Documentation: this README plus code comments and architecture notes
- Demo: record the running application showing each task

## Project Structure

```text
EduGenie/
├── main.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── tests/
│   ├── test_modules.py
│   └── test_api.py
├── requirements.txt
├── .env.example
└── .gitignore
```
