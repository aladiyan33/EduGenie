# EduGenie: Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant for students. It supports question answering, concept explanation, quiz generation, long-passage summarization, and structured learning recommendations.

## Project technology

The implementation follows the supplied EduGenie project documentation:

- FastAPI backend
- HTML + CSS + JavaScript frontend
- Gemini 1.5 Pro through the Gemini API
- LaMini-Flan-T5-783M for local concept explanation
- Uvicorn ASGI server
- Jinja2 templates

## Features

### 1. Asking questions
A student submits a question and EduGenie sends it to Gemini 1.5 Pro for a clear educational answer.

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
→ Gemini 1.5 Pro or LaMini-Flan-T5-783M
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
    GEMINI_MODEL=gemini-1.5-pro

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
