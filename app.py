import streamlit as st
from pdf_reader import extract_text_from_pdf
from ai_quiz import generate_ai_quiz

st.set_page_config(
    page_title="AI Quiz Generator",
    page_icon="🧠",       
    layout="wide"
)

st.title("🧠 AI Quiz Generator")
st.write("Upload a PDF and generate an AI-powered quiz.")

uploaded_file = st.file_uploader(
    "📄 Upload PDF",
    type=["pdf"]
)

# ---------------- Generate Quiz ----------------

if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)

    st.success("✅ PDF Uploaded Successfully!")

    if st.button("🤖 Generate AI Quiz"):

        quiz = generate_ai_quiz(text)

        if quiz:

            st.session_state.quiz = quiz
            st.session_state.submitted = False

# ---------------- Quiz ----------------

if "quiz" in st.session_state:

    st.markdown("---")
    st.header("📝 Quiz")

    for i, q in enumerate(st.session_state.quiz):

        st.subheader(f"Question {i+1}")

        st.write(q["question"])

        st.radio(
            "Choose your answer",
            q["options"],
            index=None,
            key=f"q{i}"
        )

        st.write("---")

    if st.button("✅ Submit Quiz"):

        st.session_state.submitted = True

# ---------------- Result ----------------

if st.session_state.get("submitted", False):

    score = 0

    st.header("📊 Quiz Result")

    for i, q in enumerate(st.session_state.quiz):

        user_answer = st.session_state.get(f"q{i}")

        if user_answer is None:
            continue

        correct_answer = q["answer"].strip()

        if user_answer.strip().lower() == correct_answer.lower():
            score += 1

    st.success(f"🎯 Your Score: {score}/{len(st.session_state.quiz)}")

    if score == len(st.session_state.quiz):
        st.balloons()

    st.markdown("---")
    st.header("📑 Answer Review")

    for i, q in enumerate(st.session_state.quiz):

        st.subheader(f"Question {i+1}")

        user_answer = st.session_state.get(f"q{i}")

        correct_answer = q["answer"]

        st.write(q["question"])

        if user_answer is None:

            st.warning("⚠️ Not Answered")

        else:

            st.write(f"**Your Answer:** {user_answer}")
            st.write(f"**Correct Answer:** {correct_answer}")

            if user_answer.strip().lower() == correct_answer.strip().lower():

                st.success("✅ Correct")

            else:

                st.error("❌ Wrong")

        st.write("---")