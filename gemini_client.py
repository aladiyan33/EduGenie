import os
from functools import lru_cache

from dotenv import load_dotenv
from google import genai

load_dotenv()
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

@lru_cache(maxsize=1)
def get_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured. Add it to your .env file.")
    return genai.Client(api_key=api_key)

def generate_text(prompt: str) -> str:
    response = get_client().models.generate_content(model=MODEL_NAME, contents=prompt)
    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned an empty response.")
    return text.strip()
