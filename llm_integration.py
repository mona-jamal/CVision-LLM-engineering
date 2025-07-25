import openai

# ✅ OpenAI v1+ Client
client = openai.OpenAI(
    api_key="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"
)

def get_resume_feedback(resume_text):
    """
    Send resume text to OpenAI and return structured feedback + scores.
    """
    prompt = f"""
You are a professional resume reviewer. Evaluate this resume and provide:
1. A score (0-100) for each of the following categories:
   - Structure & Formatting (25%)
   - Grammar & Spelling (20%)
   - Clarity & Readability (20%)
   - Achievements & Impact (20%)
   - Technical Skill Relevance (15%)
2. The weighted overall score out of 100.
3. Detailed feedback for each area explaining strengths and areas for improvement.

Format your response like this:
---
📊 **Resume Evaluation Scores**
- Structure & Formatting: 85%
- Grammar & Spelling: 90%
- Clarity & Readability: 80%
- Achievements & Impact: 70%
- Technical Skill Relevance: 75%
- ✅ Overall Score: 79%

📢 **Detailed Feedback**
**Structure & Formatting:** [feedback here]
**Grammar & Spelling:** [feedback here]
**Clarity & Readability:** [feedback here]
**Achievements & Impact:** [feedback here]
**Technical Skill Relevance:** [feedback here]

Here is the resume:
\"\"\"{resume_text}\"\"\"
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=1200
        )
        feedback = response.choices[0].message.content
        return feedback
    except Exception as e:
        print(f"❌ Error communicating with OpenAI API: {e}")
        return None
