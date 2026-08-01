import streamlit as st
from pdf_reader import extract_text_from_pdf
from quiz_generator import generate_quiz

# ---------------- Page Configuration ---------------- #

st.set_page_config(
    page_title="AI Quiz Generator",
    page_icon="🧠",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

st.sidebar.title("🧠 AI Quiz Generator")
st.sidebar.markdown("---")
st.sidebar.success("✅ Upload PDF")
st.sidebar.success("✅ Extract Text")
st.sidebar.success("✅ Generate Quiz")
st.sidebar.success("✅ Score")
st.sidebar.markdown("---")
st.sidebar.write("Developed by Bhagya Sri ❤️")

# ---------------- Session State ---------------- #

if "quiz" not in st.session_state:
    st.session_state.quiz = None

if "score" not in st.session_state:
    st.session_state.score = None

# ---------------- Main Title ---------------- #

st.title("🧠 AI Quiz Generator")
st.write("Upload a PDF file and automatically generate quiz questions.")
st.markdown("---")

# ---------------- Upload PDF ---------------- #

uploaded_file = st.file_uploader(
    "📄 Choose PDF File",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("✅ PDF Uploaded Successfully!")

    st.write("**File Name:**", uploaded_file.name)
    st.write("**File Size:**", round(uploaded_file.size / 1024, 2), "KB")

    # Extract Text
    text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Extracted Text")
    st.write(text)

    st.markdown("---")

    # Generate Quiz
    if st.button("📝 Generate Quiz"):
        st.session_state.quiz = generate_quiz(text)
        st.session_state.score = None

    # Show Quiz
    if st.session_state.quiz is not None:

        quiz = st.session_state.quiz

        st.subheader("📝 Quiz")

        for i, q in enumerate(quiz):

            st.write(f"### Question {i+1}")
            st.write(q["question"])

            st.radio(
                "Choose your answer",
                q["options"],
                key=f"q{i}"
            )

            st.write("---")

        # Submit Quiz
        if st.button("✅ Submit Quiz"):

            score = 0

            for i, q in enumerate(quiz):

                if st.session_state[f"q{i}"] == q["answer"]:
                    score += 1

            st.session_state.score = score

    # Show Score
    if st.session_state.score is not None:

        st.success(
            f"🎉 Your Score: {st.session_state.score}/{len(st.session_state.quiz)}"
        )