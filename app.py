import streamlit as st
from pdf_reader import extract_text_from_pdf
from ai_quiz import generate_ai_quiz

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
st.sidebar.success("✅ Generate AI Quiz")
st.sidebar.success("✅ Score")
st.sidebar.markdown("---")
st.sidebar.write("Developed by Bhagya Sri ❤️")

# ---------------- Main Title ---------------- #

st.title("🧠 AI Quiz Generator")
st.write("Upload a PDF file and automatically generate AI quiz questions.")
st.markdown("---")

# ---------------- Upload PDF ---------------- #

uploaded_file = st.file_uploader(
    "📄 Choose PDF File",
    type=["pdf"]
)

# ---------------- Process PDF ---------------- #

if uploaded_file is not None:

    st.success("✅ PDF Uploaded Successfully!")

    st.write("**File Name:**", uploaded_file.name)
    st.write("**File Size:**", round(uploaded_file.size / 1024, 2), "KB")

    # Extract Text
    text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Extracted Text")
    st.write(text)

    st.markdown("---")

    # Generate AI Quiz
    if st.button("🤖 Generate AI Quiz"):

        with st.spinner("Generating quiz using AI..."):

            quiz = generate_ai_quiz(text)

        if quiz:

            st.success("✅ AI Quiz Generated Successfully!")

            st.subheader("📝 AI Generated Quiz")

            st.write(quiz)

        else:

            st.error("❌ AI could not generate quiz. Please check your API Key or internet connection.")