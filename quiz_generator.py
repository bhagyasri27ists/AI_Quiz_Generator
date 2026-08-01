import re
import random

def generate_quiz(text):

    sentences = re.split(r'[.!?]', text)

    quiz = []

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        words = sentence.split()

        if len(words) < 8:
            continue

        answer = words[0]

        question = sentence.replace(answer, "______", 1)

        options = [
            answer,
            "Artificial Intelligence",
            "Machine Learning",
            "Python"
        ]

        random.shuffle(options)

        quiz.append({
            "question": question,
            "options": options,
            "answer": answer
        })

        if len(quiz) == 5:
            break

    return quiz