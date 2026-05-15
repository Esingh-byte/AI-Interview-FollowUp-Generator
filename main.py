from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
import json
import os

# Initialize FastAPI app
app = FastAPI(
    title="AI Interview Follow-Up Generator",
    description="Welcome to the AI Interview Follow-Up Generator API! Click on the green POST box below to test it."
)

# Configure your API Key here (uncomment and paste your key)
# os.environ["GEMINI_API_KEY"] = "your_actual_api_key_here"

# Initialize the new Google GenAI client
client = genai.Client()

class InterviewData(BaseModel):
    question: str
    answer: str

class FollowUpResponse(BaseModel):
    follow_up_question: str

def build_prompt(question: str, answer: str) -> str:
    return f"""
    You are an expert technical interviewer. I will provide an Input Question and Candidate Answer.
    Generate ONE follow-up question that probes deeper into the candidate's understanding.
    Do not ask generic questions. Target specific technical details they mentioned.
    Return ONLY a valid JSON object. Do not include markdown formatting.

    Input Question: {question}
    Candidate Answer: {answer}

    Required JSON Output Format:
    {{
      "follow_up_question": "string"
    }}
    """

@app.post("/generate-follow-up", response_model=FollowUpResponse)
def generate_follow_up(data: InterviewData):
    try:
        prompt = build_prompt(data.question, data.answer)
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        
        raw_text = response.text.strip()
        
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:-3].strip()
            
        parsed_json = json.loads(raw_text)
        
        return FollowUpResponse(follow_up_question=parsed_json.get("follow_up_question", "Could you elaborate on that?"))

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate follow-up: {str(e)}")