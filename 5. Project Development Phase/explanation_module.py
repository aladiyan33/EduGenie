from functools import lru_cache

MODEL_NAME = "MBZUAI/LaMini-Flan-T5-783M"

@lru_cache(maxsize=1)
def _load_model():
    try:
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
        return tokenizer, model
    except ImportError as exc:
        raise RuntimeError("PyTorch/Transformers is not installed correctly. Install requirements.txt.") from exc
    except Exception as exc:
        raise RuntimeError(f"Could not load the local explanation model: {exc}") from exc


def explain_topic(topic: str, level: str = "beginner") -> str:
    topic = topic.strip()
    if not topic:
        raise ValueError("Topic cannot be empty.")
    level = level if level in {"beginner", "intermediate", "advanced"} else "beginner"
    tokenizer, model = _load_model()
    prompt = f"Explain the concept of '{topic}' for a {level} learner using simple and clear language. Use a short example where helpful."
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(**inputs, max_new_tokens=180, temperature=0.7, top_k=50, top_p=0.95, do_sample=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
