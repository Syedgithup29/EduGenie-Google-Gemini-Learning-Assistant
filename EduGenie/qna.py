import os
from google import genai

MODEL_NAME = "gemini-3.8-flash"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def answer_question_with_gemini(question: str) -> str:
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=question
        )

        return response.text.strip()

    except Exception as e:
        return f"⚠️ Error in QnA: {e}"