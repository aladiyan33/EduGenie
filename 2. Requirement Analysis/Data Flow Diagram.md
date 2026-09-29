EDUGENIE — DATA FLOW DIAGRAM

Student → HTML/CSS/JavaScript Web Interface → FastAPI → Feature Module → Gemini API or Local LaMini-Flan-T5-783M → FastAPI Response → Browser

Endpoints: POST /qa; POST /explain; POST /quiz; POST /summarize; POST /learn/recommendations.

Detailed flow: Student input → HTTP POST → Pydantic validation → FastAPI routing → feature module → Gemini or local LaMini model → response → JavaScript rendering.