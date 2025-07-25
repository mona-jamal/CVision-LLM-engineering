# CVision – LLMs Resume Critique Tool

**Technical Report – July 2025**

---

## Team Members

* Mouna Jamal
* Abdulaziz Al Sayyed
* Wajed Rashed
* Reem El-Hadka
* Yahya Akel
* Zeinab Abo Hamdan

---

## Project Overview

**CVision** is a web-based application that helps users evaluate and improve their resumes using OpenAI's GPT-3.5 language model. It provides AI-powered, structured feedback across five quality dimensions. Users can upload a resume in PDF format or paste plain text directly into the app.

The feedback includes category-wise scores, visual indicators, and detailed improvement suggestions — all rendered in a modern Streamlit interface.

---

## Objectives

* Provide LLM-powered feedback on resumes
* Enable both PDF uploads and manual text input
* Deliver structured results in a user-friendly UI
* Help users enhance the clarity, relevance, and impact of their resumes

---

## Technologies Used

| Component       | Technology         |
| --------------- | ------------------ |
| Frontend        | Streamlit          |
| Backend         | Python, OpenAI SDK |
| PDF Parsing     | PyMuPDF (`fitz`)   |
| UI Styling      | Custom CSS         |
| Version Control | Git, GitHub        |

---

## File Structure

```
CVision-LLMs-Resume-Critique/
├── app.py                   # Main Streamlit application
├── llm_integration.py      # OpenAI GPT interaction
├── requirements.txt        # Python dependencies
├── styles/
│   └── style.css           # Custom UI styling
├── assets/
│   └── logo.png            # Application logo
├── .streamlit/
│   └── config.toml         # Streamlit configuration
└── README.md               # Project documentation
```

---

## Workflow Summary

1. **Resume Upload**
   Users can upload a PDF or paste their resume text into the interface.

2. **Text Extraction**
   If a PDF is uploaded, PyMuPDF is used to extract its content.

3. **LLM Processing**
   The extracted or pasted text is sent to OpenAI's GPT-3.5 for analysis and feedback generation.

4. **Result Display**
   The feedback is parsed and displayed using visual elements: scores, emojis, progress bars, and improvement suggestions.

---

## Evaluation Categories

| Category                  | Weight   |
| ------------------------- | -------- |
| Structure & Formatting    | 25%      |
| Grammar & Spelling        | 20%      |
| Clarity & Readability     | 20%      |
| Achievements & Impact     | 20%      |
| Technical Skill Relevance | 15%      |
| **Total**                 | **100%** |

---

## Key Features

* Upload a PDF or paste plain text
* Intelligent feedback from OpenAI GPT-3.5
* Scoring across 5 resume quality dimensions
* Progress bars and emoji indicators
* Clean, styled, responsive UI
* Works across various resume formats

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/CVision-LLMs-Resume-Critique.git
cd CVision-LLMs-Resume-Critique
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:

* `streamlit`
* `openai>=1.0.0`
* `pymupdf`

### 4. Run the App

```bash
streamlit run app.py
```

### 5. Use the App

* Upload a PDF or paste resume text
* Click **"Get Feedback"**
* Review scores and detailed improvement suggestions

---

## Team Contributions

* **Mouna Jamal** – Built the resume input interface (file uploader and text input)
* **Abdulaziz Al Sayyed & Wajed Rashed** – Developed OpenAI GPT-3.5 integration and structured prompt handling
* **Zeinab Abo Hamdan** – Created the results UI with scores and feedback visualization
* **Reem El-Hadka** – Implemented PDF parsing with PyMuPDF
* **Yahya Akel** – Performed QA testing, feedback evaluation, and logic refinement
* **All Members** – Worked collaboratively on documentation and final presentation

---

## Conclusion

**CVision** demonstrates how Large Language Models can be applied to real-world use cases like resume evaluation. By combining natural language processing with intuitive UI, the tool delivers practical, high-impact feedback to help job seekers stand out in competitive markets.
