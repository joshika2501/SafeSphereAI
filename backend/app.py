from fastapi import FastAPI

from backend.predict import predict_risk
from backend.schema import SensorInput

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

    prediction = predict_risk(sensor.dict())

    return {
        "Predicted Risk": prediction
    }