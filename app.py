import streamlit as st
import PyPDF2
from io import BytesIO

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

    # Next step button (used later to send to LLM)
    if st.button("Get Feedback"):
        st.write("Sending resume to LLM... (to be implemented)")
