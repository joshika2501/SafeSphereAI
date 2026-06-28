import joblib
import pandas as pd

model = joblib.load("models/risk_model.pkl")

encoders = joblib.load("models/encoders.pkl")

risk_encoder = joblib.load("models/risk_encoder.pkl")


def predict_risk(data):

    df = pd.DataFrame([data])

    categorical = [
        "Maintenance",
        "Permit",
        "MachineStatus",
        "Zone"
    ]

    for col in categorical:
        df[col] = encoders[col].transform(df[col])

    prediction = model.predict(df)

    risk = risk_encoder.inverse_transform(prediction)

    return risk[0]