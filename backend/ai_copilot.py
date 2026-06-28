import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_ai_report(sensor_data, risk):

    prompt = f"""
You are an Industrial Safety Expert.

Sensor Data:
{sensor_data}

Predicted Risk:
{risk}

Generate a professional industrial safety report.

Use these headings:

## Root Cause

## Hazard Analysis

## Immediate Actions

## Preventive Measures

Keep the response below 200 words.
"""

    response = model.generate_content(prompt)

    return response.text