import streamlit as st
import PyPDF2
from io import BytesIO
from llm_integration import get_resume_feedback  # ✅ Import your LLM function

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
    pdf_reader = PyPDF2.PdfReader(BytesIO(uploaded_file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    resume_text = text  # Overwrite if file uploaded
    st.success("✅ Resume text extracted from PDF!")

# Show extracted or pasted resume
if resume_text:
    st.subheader("📄 Your Resume Text:")
    st.write(resume_text)

    # Get Feedback button
    if st.button("Get Feedback"):
        with st.spinner("🔄 Sending resume to LLM..."):
            feedback = get_resume_feedback(resume_text)  # ✅ Call LLM API
        if feedback:
            st.subheader("📢 LLM Feedback")
            st.write(feedback)
        else:
            st.error("❌ Failed to get feedback from LLM.")
