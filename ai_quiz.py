from groq import Groq
from config import API_KEY

client = Groq(api_key=API_KEY)

def generate_ai_quiz(text):

    prompt = f"""
Generate 5 multiple choice questions from the following text.

Rules:
1. Each question should have exactly 4 options (A, B, C, D).
2. Mention the correct answer after each question.
3. Keep questions simple.
4. Return only the quiz.

Text:
{text}
"""

    try:

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.5
        )

        return response.choices[0].message.content

    except Exception as e:
        print(e)
        return None