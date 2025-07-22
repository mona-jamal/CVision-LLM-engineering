import openai

# 🚨 Hardcode your API key here (skip secrets.toml)
openai.api_key = "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"

def get_resume_feedback(resume_text):
    """
    Send resume text to OpenAI GPT-3.5 and return feedback.
    """
    prompt = f"""
    You are a professional resume reviewer.
    Review the following resume and provide constructive feedback on:
    - Structure
    - Grammar corrections
    - Clarity improvements
    - Suggestions to make it more impactful

    Resume:
    \"\"\"{resume_text}\"\"\"
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=800
        )
        feedback = response['choices'][0]['message']['content']
        return feedback
    except Exception as e:
        print(f"❌ Error communicating with OpenAI API: {e}")
        return None
