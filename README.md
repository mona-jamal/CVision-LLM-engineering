# CVision – LLMs Resume Critique Tool

CVision is a web-based application that helps users enhance their resumes using AI-powered feedback from OpenAI’s GPT-3.5. Users can upload a PDF or paste resume text, and the app will analyze the content, score it across five key categories, and offer detailed improvement suggestions — all within a clean and user-friendly interface built with Streamlit.

---

## Features

* **Upload or Paste**: Support for PDF uploads or plain text input
* **AI Feedback**: Uses GPT-3.5 to analyze resumes and generate improvement tips
* **Structured Scoring**: Feedback across key resume quality categories:

  * Structure & Formatting
  * Grammar & Spelling
  * Clarity & Readability
  * Achievements & Impact
  * Technical Skill Relevance
* **Visual Feedback**: Emoji score indicators, progress bars, and structured suggestions
* **Custom UI**: Styled interface with custom CSS
* **PDF Parsing**: Resume content is extracted using PyMuPDF

---

## Tech Stack

| Component       | Technology           |
| --------------- | -------------------- |
| Frontend        | Streamlit            |
| Backend         | Python 3, OpenAI SDK |
| PDF Parsing     | PyMuPDF (`fitz`)     |
| UI Styling      | Custom CSS           |
| Version Control | Git + GitHub         |

---

## Project Structure

```
CVision-LLMs-Resume-Critique/
├── app.py                   # Main Streamlit app
├── llm_integration.py      # Handles OpenAI GPT interactions
├── requirements.txt        # Project dependencies
├── styles/
│   └── style.css           # Custom CSS styling
├── assets/
│   └── logo.png            # App logo
├── .streamlit/
│   └── config.toml         # Streamlit configuration
└── README.md               # Project documentation
```

---

## How to Run the Project

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/CVision-LLMs-Resume-Critique.git
   cd CVision-LLMs-Resume-Critique
   ```

2. **(Optional) Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate         # On Windows: venv\Scripts\activate
   ```

3. **Install Required Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is missing, install individually:

   ```bash
   pip install streamlit openai PyMuPDF
   ```

4. **Run the Application**

   ```bash
   streamlit run app.py
   ```

5. **Use the App**

   * Upload your PDF resume or paste resume text
   * Click **“Get Feedback”**
   * View AI-generated feedback and score breakdown

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

## Team Contributors

* **Mouna Jamal** – Resume upload & input interface
* **Abdulaziz Al Sayyed** & **Wajed Rashed** – LLM prompt integration and backend logic
* **Zeinab Abo Hamdan** – UI display of results and visual indicators
* **Reem El-Hadka** – PDF parsing using PyMuPDF
* **Yahya Akel** – Testing, validation, and overall refinement
* **Entire Team** – Documentation, GitHub setup, and final presentation

---

## Project Highlights

* Designed for job seekers and students to improve resume quality
* Real-world application of LLMs for natural language analysis
* Combines AI with intuitive UI to deliver instant, actionable insights
