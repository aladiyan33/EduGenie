# EduGenie: Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant for students. It supports question answering, concept explanation, quiz generation, long-passage summarization, and structured learning recommendations.

## Project technology

The implementation follows the supplied EduGenie project documentation:

- FastAPI backend
- HTML + CSS + JavaScript frontend
- Gemini API using a currently supported Gemini model (default: Gemini 3.8 Flash)
- LaMini-Flan-T5-783M for local concept explanation
- Uvicorn ASGI server
- Jinja2 templates

## Features

### 1. Asking questions
A student submits a question and EduGenie sends it to the configured Gemini model for a clear educational answer.

### 2. Explanation of any topic
The Explain feature uses MBZUAI/LaMini-Flan-T5-783M locally to produce a simple explanation.

### 3. Summarising long paragraphs
Study material is sent to Gemini and returned as a focused summary.

### 4. Generating quizzes
EduGenie generates exactly three multiple-choice questions with four options each. Students can select an option and click Check Answer to receive immediate feedback.

### 5. Learning recommendations
EduGenie generates a structured path from Beginner to Intermediate to Advanced, including topics, resources, timelines and practice.

## Architecture

Student input
→ HTML/CSS/JavaScript frontend
→ FastAPI endpoint
→ selected module
→ the configured Gemini model or LaMini-Flan-T5-783M
→ result
→ browser

## Project structure

EduGenie/
- main.py
- explanation_module.py
- qna.py
- quiz_module.py
- summary_module.py
- learning_path.py
- gemini_client.py
- templates/index.html
- static/style.css
- tests/
- requirements.txt
- .env.example
- .gitignore

## Setup

Create a virtual environment:

    python -m venv .venv
    .venv\Scripts\activate

Install dependencies:

    python -m pip install -r requirements.txt

Create the local environment file:

    copy .env.example .env

Edit .env:

    GEMINI_API_KEY=your_api_key_here
    GEMINI_MODEL=gemini-3.8-flash

Run the application:

    uvicorn main:app --reload

Open:

    http://127.0.0.1:8000

## Local LaMini model

The first time the Explain feature is used, Hugging Face downloads MBZUAI/LaMini-Flan-T5-783M and stores it in the local Hugging Face cache. Later runs reuse the cached model unless the cache is removed or the environment changes.

## API endpoints

- POST /qa
- POST /explain
- POST /quiz
- POST /summarize
- POST /learn/recommendations

Compatibility aliases under /api/* are also available.

## Security

Never commit .env or a Gemini API key to GitHub. Use environment variables or hosting secrets for deployment.

## Testing

Run:

    pytest -q

The tests mock AI generation where appropriate, so they do not require a live Gemini API key.

## SkillWallet deliverables

- GitHub repository link
- Documentation
- Demo video
- Working application screenshots

## Model compatibility note

The supplied project document specifies Gemini 1.5 Pro. Google shut down the Gemini 1.5 Pro API model on September 29, 2025, so it now returns 404 errors. The application therefore defaults to the currently supported `gemini-3.8-flash` model while keeping the same Gemini-powered functionality. The model can be changed through `GEMINI_MODEL` without changing application code.
