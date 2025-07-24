import streamlit as st
import fitz
import os
import re
from io import BytesIO
from llm_integration import get_resume_feedback

# --- Load Custom CSS ---
css_path = os.path.join(os.path.dirname(__file__), 'styles/style.css')
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning("⚠️ CSS file not found.")

# --- Markdown wrapper ---
def styled_markdown(md_text, css_class="custom-markdown"):
    st.markdown(f'<div class="{css_class}">{md_text}</div>', unsafe_allow_html=True)

# --- Bullet auto-insertion helper ---
def auto_insert_bullets(text):
    lines = text.splitlines()
    updated = []
    for line in lines:
        if (
            line.strip() != "" and
            not line.strip().endswith(":") and
            not line.strip().isupper() and
            not line.strip().startswith("•") and
            not line.strip().startswith("-")
        ):
            # Treat indented lines or short task lines as bullets
            if line.startswith(" ") or line.startswith("\t") or len(line.strip().split()) < 10:
                line = f"• {line.strip()}"
        updated.append(line)
    return "\n".join(updated)

# --- Logo and Title ---
st.image("assets/logo.png", width=80)
st.title("📄 Resume Critique Tool")
st.write("Upload your resume (PDF), or paste it below:")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])
resume_text = st.text_area("Or paste your resume text here:", height=200)

# --- Extract from PDF ---
if uploaded_file is not None:
    text = ""
    pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page in pdf_doc:
        page_dict = page.get_text("dict")
        for block in page_dict["blocks"]:
            for line in block.get("lines", []):
                line_text = " ".join([span["text"] for span in line["spans"]]).strip()
                if line_text:
                    text += line_text + "\n"

    resume_text = auto_insert_bullets(text)
    st.success("✅ Resume text extracted from PDF!")


# --- Display resume text ---
if resume_text:
    st.subheader("📄 Your Resume Text:")
    styled_markdown(resume_text, "resume-preview")

    if st.button("Get Feedback"):
        with st.spinner("Sending resume to LLM..."):
            feedback = get_resume_feedback(resume_text)

        if feedback:
            st.subheader("🏆 Resume Evaluation")
            st.markdown("<div class='eval-wrapper'>", unsafe_allow_html=True)

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

                    # Add colored emoji
                    emoji = "❌"
                    if score >= 90:
                        emoji = "🟢"
                    elif score >= 75:
                        emoji = "🟡"
                    elif score >= 60:
                        emoji = "🟠"
                    st.markdown(f"<div class='score-label'><strong>{emoji} {category}:</strong> {score}%</div>", unsafe_allow_html=True)
                    st.progress(score)

            if categories["Overall Score"] is not None:
                overall = categories["Overall Score"]
                st.subheader(f"🎯 Overall Score: {overall}%")
                st.progress(overall)
                grade = "Poor"
                emoji = "❌"
                if overall >= 90:
                    grade = "Excellent"
                    emoji = "🔥"
                elif overall >= 75:
                    grade = "Good"
                    emoji = "✅"
                elif overall >= 60:
                    grade = "Fair"
                    emoji = "⚠️"
                st.markdown(f"<div class='score-label'><strong>Grade:</strong> {emoji} {grade}</div>", unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

            st.subheader("📢 Detailed Feedback")
            feedback_text = re.split(r"📢 \*\*Detailed Feedback\*\*", feedback)[-1]
            styled_markdown(feedback_text.strip(), "feedback-block")
        else:
            st.error("❌ Failed to get feedback from LLM.")
