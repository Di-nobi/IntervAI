from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os
import json

load_dotenv()

genai.configure(api_key=os.getenv('API_KEY'))
model = genai.GenerativeModel("gemini-2.5-flash-lite")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class JobRequest(BaseModel):
    jobTitle: str

""" Prompt for generating interview questions """
def chatResponse(job_title: str) -> list[str]:
    prompt = f"""You are a hiring manager and interviewer.
            Generate exactly 3 thoughtful, insightful interview questions for the role of "{job_title}".

            The questions should:
            - Be specific and relevant to this exact role
            - Assess both skills and cultural fit
            - Vary in type (e.g., behavioural, situational, role-specific knowledge)
            - Be open-ended and encourage detailed answers

            Respond ONLY with a JSON object in this exact format, no preamble, no markdown:
            {{"questions": ["Question 1 here?", "Question 2 here?", "Question 3 here?"]}}"""

    response = model.generate_content(prompt)
    text = response.text.strip()
    text = text.removeprefix("```json").removeprefix("```").removesuffix("```").strip()

    data = json.loads(text)
    return data["questions"]


@app.post("/generate")
async def generate(body: JobRequest):
    questions = chatResponse(body.jobTitle)
    return {"questions": questions}