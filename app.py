import streamlit as st
import fitz

from io import BytesIO
from llm_integration import get_resume_feedback
import re

# Set Streamlit page title
st.set_page_config(page_title="Resume Critique Tool")

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
