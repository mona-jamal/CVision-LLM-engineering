import streamlit as st
import fitz
import os
from io import BytesIO
from llm_integration import get_resume_feedback
import re

# --- Page Setup ---
st.set_page_config(page_title="Resume Critique Tool", layout="centered")

# --- LIGHT / DARK Toggle ---
theme_mode = st.sidebar.radio("Select Theme", ["🌞 Light", "🌙 Dark"])

# --- Load CSS based on theme ---
css_file = 'styles/light.css' if theme_mode == "🌞 Light" else 'styles/dark.css'
css_path = os.path.join(os.path.dirname(__file__), css_file)
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning("Custom CSS file not found.")

# --- Logo and Title ---
st.image("assets/logo.png", width=80)
st.title("📄 Resume Critique Tool")
st.write("Upload your resume (PDF), or paste it below:")

# File upload
uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])

# Text area
resume_text = st.text_area("Or paste your resume text here:")

# Extract text from PDF if uploaded
if uploaded_file is not None:
    text = ""
    pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in pdf_doc:
        text += page.get_text("text")  # Keeps layout better
    resume_text = text
    st.success("✅ Resume text extracted from PDF!")

# Show extracted or pasted resume
if resume_text:
    st.subheader("📄 Your Resume Text:")
    st.write(resume_text)

    # Get Feedback button
    if st.button("Get Feedback"):
        with st.spinner("🔄 Sending resume to LLM..."):
            feedback = get_resume_feedback(resume_text)

        if feedback:
            # Parse scores
            st.subheader("🏆 Resume Evaluation")
            categories = {
                "Structure & Formatting": None,
                "Grammar & Spelling": None,
                "Clarity & Readability": None,
                "Achievements & Impact": None,
                "Technical Skill Relevance": None,
                "Overall Score": None
            }
            for category in categories:
                match = re.search(rf"{re.escape(category)}[:\s]+(\d+)%", feedback)
                if match:
                    score = int(match.group(1))
                    categories[category] = score
                    if category != "Overall Score":
                        st.write(f"**{category}: {score}%**")
                        st.progress(score)
                    else:
                        st.subheader(f"🎯 Overall Score: {score}%")
                        st.progress(score)
                        # Grade label
                        if score >= 90:
                            grade = "🔥 Excellent"
                        elif score >= 75:
                            grade = "✅ Good"
                        elif score >= 60:
                            grade = "⚠️ Fair"
                        else:
                            grade = "❌ Poor"
                        st.write(f"**Grade:** {grade}")

            # Show detailed feedback
            st.subheader("📢 Detailed Feedback")
            feedback_text = re.split(r"📢 \*\*Detailed Feedback\*\*", feedback)[-1]
            st.markdown(feedback_text.strip())
        else:
            st.error("❌ Failed to get feedback from LLM.")
