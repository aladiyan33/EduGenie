# EduGenie — Google Gemini Powered Learning Assistant

## Submission-ready repository

This repository contains the working EduGenie application and the eight-phase SkillWallet submission structure from the provided project template.

## Eight project phases

1. Brainstorming & Ideation — problem statements, empathy map, idea prioritization.
2. Requirement Analysis — customer journey, data flow, solution requirements, technology stack.
3. Project Design Phase — problem-solution fit, proposed solution, solution architecture.
4. Project Planning Phase — project planning and team allocation.
5. Project Development Phase — code layout, coding solution, functional features.
6. Project Testing — performance/testing approach and automated tests.
7. Project Documentation — executable instructions and project documentation.
8. Project Demonstration — communication, feature demonstration, demo planning, scalability/future plan, and team involvement.

## Application

EduGenie provides Question Answering, Concept Explanation, Text Summarization, Quiz Generation with answer checking, and Beginner → Intermediate → Advanced Learning Recommendations.

## Working application layout

The application source is kept at repository root for direct execution: main.py, gemini_client.py, qna.py, explanation_module.py, quiz_module.py, summary_module.py, learning_path.py, templates/index.html, static/style.css, tests/, requirements.txt, .env.example, .gitignore.

## Team

- Aaladiyan V — Team Lead: Backend API with FastAPI; Build Web Interface; Live Integration; Future Enhancements.
- Kodeeswaran S: Pre-requisites; Workflow; Functional Testing.
- Sundaravel T: Select AI Models; Module Implementation; Run Locally.

## Run

python -m venv .venv
.venv\\Scripts\\activate
python -m pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload

Open http://127.0.0.1:8000.

## Configuration

Set GEMINI_API_KEY in local .env. The model is configurable through GEMINI_MODEL.

## Testing

pytest -q

AI calls are mocked in automated tests where appropriate.

## Security

Never commit .env or API keys.

## Submission document format

The reference template uses PDF deliverables. The eight numbered folders and all named deliverable items are present in this repository. Completed content is stored as Markdown so it remains directly reviewable and version controlled.
