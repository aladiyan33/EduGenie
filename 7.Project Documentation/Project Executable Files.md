EDUGENIE — PROJECT EXECUTABLE FILES

Repository: aladiyan33/EduGenie

Run
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload

Browser
http://127.0.0.1:8000

Main files
main.py, qna.py, explanation_module.py, quiz_module.py, summary_module.py, learning_path.py, gemini_client.py, templates/index.html, static/style.css.

Testing
pytest -q

Environment
GEMINI_API_KEY=<your key>
GEMINI_MODEL=<supported Gemini model>

Do not commit the real .env or API key.