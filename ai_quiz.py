from groq import Groq
import streamlit as st
import json

# Local PC -> config.py
# Streamlit Cloud -> Secrets
try:
    from config import API_KEY
except ImportError:
    API_KEY = st.secrets["API_KEY"]

client = Groq(api_key=API_KEY)


def generate_ai_quiz(text):

    prompt = f"""
You are an expert AI Quiz Generator.

Read the given text and create EXACTLY 5 multiple-choice questions.

Return ONLY valid JSON.

Format:

[
  {{
    "question": "What is Artificial Intelligence?",
    "options": [
      "Simulation of human intelligence by machines",
      "Programming language",
      "Database",
      "Operating System"
    ],
    "answer": "Simulation of human intelligence by machines"
  }}
]

Rules:
1. Generate exactly 5 questions.
2. Every question must have exactly 4 meaningful options.
3. Never use "Option 1", "Option 2", "Option 3", or "Option 4".
4. One option must exactly match the answer.
5. Other 3 options must be realistic but incorrect.
6. Return ONLY valid JSON.
7. No markdown.
8. No explanation.

Text:
{text}
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        result = response.choices[0].message.content

        result = result.replace("```json", "")
        result = result.replace("```", "").strip()

        quiz = json.loads(result)

        return quiz

    except Exception as e:
        st.error(f"AI Error: {e}")
        return None