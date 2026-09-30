from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm

W,H=A4
NAVY=colors.HexColor("#172033"); BLUE=colors.HexColor("#274C77")
LIGHT=colors.HexColor("#EEF3F8"); DARK=colors.HexColor("#15191F"); GRAY=colors.HexColor("#4A5563")

pages=[
("SAMPLE PROJECT DOCUMENTATION","EduGenie: Google Gemini Powered Learning Assistant",["Team ID: SWTID-2026-3580","Date: 30 September 2026","Student-focused Generative AI learning assistant"]),
("PROJECT DESCRIPTION","What is EduGenie?",["Helps students ask questions and understand difficult concepts.","Supports explanation, Q&A, quizzes, summarization and learning recommendations.","Uses FastAPI with HTML/CSS/JavaScript and Google Gemini."]),
("LEARNING SCENARIOS","Core Student Use Cases",["Q&A — ask a topic-specific question and receive a clear answer.","Explain — simplify a difficult concept for easier understanding.","Quiz — generate multiple-choice practice questions.","Summary — reduce long passages into useful study notes."]),
("LEARNING PATH","Structured Recommendations",["Beginner: foundations and prerequisite concepts.","Intermediate: guided practice and connected concepts.","Advanced: deeper topics, practice and next-step resources.","Recommendations are generated from the student's requested topic."]),
("TECHNOLOGY STACK","Project Technologies",["Backend: Python + FastAPI + Uvicorn.","Frontend: HTML, CSS and JavaScript.","Generative AI: Google Gemini API.","Local AI: LaMini-Flan-T5-783M for concept explanation."]),
("PREREQUISITES","Development Environment",["Python 3.x and a virtual environment.","FastAPI, Jinja2 and Uvicorn.","Google Gemini API access through a configured API key.","Required Python packages installed from requirements.txt."]),
("PROJECT WORKFLOW","End-to-End Flow",["1. Student enters a request.","2. FastAPI validates and routes the request.","3. Specialized AI module builds the prompt.","4. Gemini or the local model generates the result.","5. EduGenie displays the result in the web interface."]),
("MILESTONE 1","Model Selection & Architecture",["Gemini handles Q&A, quiz generation, summaries and learning paths.","LaMini-Flan-T5-783M handles concept explanation.","AI responsibilities are separated into reusable Python modules.","The API key is kept outside source code using environment configuration."]),
("ACTIVITY 1.1","Secure API Configuration",["GEMINI_API_KEY is read from environment variables.","The secret is not hard-coded into the repository.","gemini_client.py provides a single reusable Gemini client.","Missing configuration produces a clear runtime error."]),
("ACTIVITY 1.2","Model Integration",["EduGenie uses the current Gemini model configured through GEMINI_MODEL.","The shared client sends prompts through the Google GenAI SDK.","Modules receive clean text responses from the shared client.","Provider configuration remains separate from business logic."]),
("ACTIVITY 1.3","Backend Architecture",["FastAPI exposes task-specific REST endpoints.","main.py coordinates validation, routing and responses.","Separate modules handle Q&A, explanation, quiz, summary and learning path tasks.","JSON responses make the backend easy to test and extend."]),
("ACTIVITY 1.4","Development Structure",["main.py — FastAPI application and routes.","gemini_client.py — Gemini configuration and generation.","qna.py, quiz_module.py, summary_module.py and learning_path.py — task logic.","templates/ and static/ — web interface assets."]),
("MILESTONE 2","Core Functionalities",["Question Answering: focused educational responses.","Concept Explanation: simplified explanations using the local model.","Quiz Generation: structured MCQs with options and answers.","Summarization and Learning Path: concise notes and staged recommendations."]),
("BACKEND API","REST Endpoint Design",["/qa — educational question answering.","/explain — concept explanation.","/quiz — quiz generation.","/summarize — long-passage summarization.","/learn/recommendations — structured learning path."]),
("RESPONSE HANDLING","AI Output Processing",["Inputs are validated before generation.","AI responses are normalized before returning to the frontend.","Quiz output is parsed into structured JSON for answer checking.","Errors are returned clearly instead of exposing implementation details."]),
("MILESTONE 3","Web Interface",["A simple student-facing interface provides task selection and input.","Results are displayed directly on the page.","Quiz responses can be checked interactively.","Responsive styling keeps the interface usable across screen sizes."]),
("MILESTONE 4","Dynamic Student Experience",["The browser sends requests to FastAPI using JavaScript.","Returned content is rendered into the result area.","Different tasks share the same interface while using different backend routes.","The design keeps the UI simple and focused on learning."]),
("MILESTONE 5","Local Run & Verification",["Create and activate a Python virtual environment.","Install dependencies from requirements.txt.","Run with: uvicorn main:app --reload.","Open the local EduGenie page and test each major feature."]),
("TESTING & SECURITY","Quality Checks",["API tests cover health, validation and mocked AI responses.","Module tests cover quiz parsing and task behavior.","API keys remain in environment configuration, not GitHub.","Functional testing checks Q&A, explanation, quiz, summary and recommendations."]),
("CONCLUSION & FUTURE","Project Outcome",["EduGenie connects a student-friendly interface to specialized AI learning features.","Future extensions can include voice interaction, multilingual learning, gamification and adaptive personalization.","Repository: aladiyan33/EduGenie","Team ID: SWTID-2026-3580"])
]

c=canvas.Canvas("7.Project Documentation/Sample Project Documentation.pdf",pagesize=A4)
c.setTitle("Sample Project Documentation - EduGenie")
for i,(section,title,bullets) in enumerate(pages,1):
    c.setFillColor(colors.white); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(NAVY); c.rect(0,H-34*mm,W,34*mm,fill=1,stroke=0)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold",11); c.drawString(17*mm,H-13*mm,section)
    c.setFont("Helvetica-Bold",8.5); c.drawRightString(W-17*mm,H-13*mm,"SMARTBRIDGE / SKILL WALL")
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold",25)
    y=H-53*mm; c.drawString(17*mm,y,title)
    c.setFillColor(BLUE); c.roundRect(17*mm,y-15*mm,62*mm,8*mm,3*mm,fill=1,stroke=0)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold",8.5); c.drawCentredString(48*mm,y-12.2*mm,"EDUGENIE • DOCUMENTATION")
    card_y=H-92*mm; card_h=112*mm
    c.setFillColor(LIGHT); c.roundRect(14*mm,card_y,182*mm,card_h,5*mm,fill=1,stroke=0)
    yy=card_y+card_h-15*mm
    for b in bullets:
        c.setFillColor(BLUE); c.circle(24*mm,yy+1.5*mm,2.1*mm,fill=1,stroke=0)
        c.setFillColor(DARK); c.setFont("Helvetica",13)
        words=b.split(); lines=[]; line=""
        for w in words:
            if len(line)+len(w)+1<=54: line=(line+" "+w).strip()
            else: lines.append(line); line=w
        if line: lines.append(line)
        for ln in lines: c.drawString(31*mm,yy,ln); yy-=8*mm
        yy-=7*mm
    c.setStrokeColor(colors.HexColor("#C9D2DD")); c.line(17*mm,16*mm,W-17*mm,16*mm)
    c.setFillColor(GRAY); c.setFont("Helvetica",8.5); c.drawString(17*mm,9*mm,"EduGenie • SWTID-2026-3580")
    c.drawRightString(W-17*mm,9*mm,f"Page {i} of 21"); c.showPage()
c.save()
