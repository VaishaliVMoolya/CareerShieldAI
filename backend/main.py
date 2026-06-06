from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ----------------------------
# FastAPI App
# ----------------------------
app = FastAPI()

# ----------------------------
# Gemini Configuration
# ----------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# Request Schema
# ----------------------------
class JobData(BaseModel):
    text: str

# ----------------------------
# API Endpoint
# ----------------------------
@app.post("/analyze")
def analyze_job(data: JobData):

    prompt = f"""
You are an AI Career Analyst.

Analyze the following job posting and provide:

1. Job Title
2. Company Name
3. Job Type (Internship / Full-Time / Contract / etc.)
4. Short Summary (2-3 lines)
5. Top Skills Required
6. Difficulty Level (Easy / Medium / Hard)
7. Suitable For (Beginner / Intermediate / Advanced)

Job Posting:

{data.text}
"""

    try:
        response = model.generate_content(prompt)

        return {
            "analysis": response.text
        }

    except Exception as e:
        return {
            "error": str(e)
        }

# ----------------------------
# Root Route
# ----------------------------
@app.get("/")
def home():
    return {
        "message": "CareerShield AI Backend Running Successfully 🚀"
    }