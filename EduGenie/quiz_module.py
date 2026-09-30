import json
import os
import re

from google import genai

MODEL_NAME = "gemini-3.8-flash"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def clean_json_block(text: str) -> str:
    return re.sub(
        r"```(?:json)?\s*(.*?)\s*```",
        r"\1",
        text,
        flags=re.DOTALL
    ).strip()


def generate_quiz(text: str) -> list:
    try:
        prompt = f"""
You are a quiz generator.

From the following passage, create 3 multiple-choice questions.

Each question should include:
- A "question"
- A list of 4 "options"
- A correct "answer" that exactly matches one option.

Return only valid JSON in this format:

[
  {{
    "question": "What is ...?",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Passage:
{text}
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        quiz_text = response.text.strip()

        cleaned_text = clean_json_block(quiz_text)

        quiz = json.loads(cleaned_text)

        return quiz

    except Exception as e:
        return [
            {
                "error": f"⚠️ Error in Quiz: {e}"
            }
        ]