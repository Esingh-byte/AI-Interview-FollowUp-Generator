# AI Interview Follow-Up Generator 🤖🎤

An intelligent REST API built with **FastAPI** and Google Gemini AI that generates context-aware, non-repetitive follow-up questions for automated technical interviews. FastAPI provides automatic interactive API documentation, including Swagger UI at `/docs` by default, which makes the project easy to test locally.[1]

This project represents Phase 2 of an AI Interview Engine, moving from static questioning to dynamic technical probing based on a candidate’s response.

## ✨ Features

- **Dynamic follow-ups:** Analyzes the candidate’s answer and asks a deeper technical question based on detected concepts.
- **Structured API design:** FastAPI supports request and response modeling with Pydantic, making the API easier to validate and maintain.[2]
- **Interactive documentation:** FastAPI exposes Swagger UI at `/docs` by default for quick endpoint testing.[1]
- **Modern AI integration:** The Google GenAI SDK for Python supports Gemini models and is installed with the `google-genai` package.[3]

## 🛠️ Tech Stack

- **Language:** Python 3
- **Framework:** FastAPI
- **Server:** Uvicorn
- **AI Integration:** Google GenAI SDK (`gemini-2.5-flash`)
- **Validation:** Pydantic

## 📦 Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Esingh-byte/AI-Interview-FollowUp-Generator.git
   cd AI-Interview-FollowUp-Generator
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   If you add new packages later, you can refresh the dependency file with:

   ```bash
   pip freeze > requirements.txt
   ```

3. **Set your API key**

   Get a Google Gemini API key, then configure it before starting the server. The Google GenAI Python SDK is distributed as `google-genai`.[3]

   ```python
   import os

   os.environ["GEMINI_API_KEY"] = "your_api_key_here"
   ```

4. **Run the development server**

   ```bash
   uvicorn main:app --reload
   ```

## 🧪 Usage & Testing

Once the server is running, open the Swagger UI in your browser:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

FastAPI serves Swagger UI at `/docs` by default, so this endpoint is the standard local testing page for the API.[1]

### Example Request

```json
{
  "question": "What is the difference between a list and a tuple in Python?",
  "answer": "A list is mutable, but a tuple is immutable."
}
```

### Example Response

```json
{
  "follow_up_question": "You mentioned tuples are immutable. If a tuple contains a mutable object, such as a list, does that tuple remain immutable? Please explain."
}
```

## 📂 Project Structure

```text
AI-Interview-FollowUp-Generator/
├── main.py
├── prompt_logic.md
├── examples.json
├── requirements.txt
└── README.md
```

- `main.py` — Core FastAPI application, routes, and AI model integration.
- `prompt_logic.md` — System instructions that guide the model as a technical interviewer.
- `examples.json` — Sample domain-specific test cases for validating follow-up quality.
- `requirements.txt` — Project dependencies.
- `README.md` — Project documentation.

## 🚀 Git Commands

After saving your updated README, push it to GitHub with:

```bash
git add README.md
git commit -m "Update professional README"
git push
```

## 👩‍💻 Developed By

Etti Singh
