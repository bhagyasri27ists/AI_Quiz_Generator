from google import genai
from config import API_KEY

client = genai.Client(api_key=API_KEY)

def generate_ai_quiz(text):

    prompt = f"""
Generate 5 multiple-choice questions from the following text.

Rules:
1. Each question must have 4 options.
2. Mention the correct answer.

Text:
{text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return None