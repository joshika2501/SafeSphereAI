from fastapi import FastAPI

from backend.predict import predict_risk
from backend.schema import SensorInput
from backend.ai_copilot import generate_ai_report

app = FastAPI(
    title="Industrial Safety Intelligence API"
)


@app.get("/")
def home():

    return {
        "message": "Industrial Safety API Running"
    }


@app.post("/predict")
def predict(sensor: SensorInput):

    data = sensor.dict()      # Use sensor.model_dump() if using Pydantic v2

    prediction = predict_risk(data)

    confidence = 0.98

    if prediction == "Safe":
        risk_score = 25
        priority = "Low"

    elif prediction == "Warning":
        risk_score = 65
        priority = "Medium"

    else:
        risk_score = 95
        priority = "High"

    try:
        ai_report = generate_ai_report(
            data,
            prediction
        )

    except Exception as e:

        ai_report = f"""
### AI Copilot Unavailable

Gemini could not generate the report.

Reason:

{str(e)}
"""

    return {

        "Predicted Risk": prediction,

        "Risk Score": risk_score,

        "Confidence": confidence,

        "Priority": priority,

        "AI Report": ai_report

    }