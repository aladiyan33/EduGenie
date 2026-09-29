EDUGENIE — CODE LAYOUT, READABILITY AND REUSABILITY

Application layout
main.py, gemini_client.py, qna.py, explanation_module.py, quiz_module.py, summary_module.py, learning_path.py, templates/index.html, static/style.css, tests/, requirements.txt, .env.example, .gitignore.

Readability
Clear module names, focused functions, validation at API boundaries, structured prompts and consistent error handling.

Reusability
Shared Gemini generator, separated routing and feature logic, reusable Pydantic request models, isolated quiz parsing/validation, automated tests.

Security
Secrets are read from environment variables and .env is excluded from Git.