import os
from google import genai

MODEL_NAME = "gemini-3.8-flash"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def summarize_text(text: str) -> str:
    try:
        prompt = (
            "Summarize the following text in simple language:\n\n"
            + text
        )

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"⚠️ Error in Summary: {e}"