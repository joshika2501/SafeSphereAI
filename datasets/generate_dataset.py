import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

np.random.seed(42)
random.seed(42)

NUM_ROWS = 10000

data = []

for _ in range(NUM_ROWS):

    timestamp = fake.date_time_this_year()

    temperature = round(np.random.normal(35, 8), 1)
    gas_level = max(0, round(np.random.normal(180, 90), 1))
    pressure = round(np.random.normal(2.8, 0.5), 2)
    humidity = round(np.random.uniform(30, 90), 1)

    worker_count = random.randint(1, 30)

    maintenance = random.choice(["Yes", "No"])
    permit = random.choice(["Yes", "No"])

    machine_status = random.choice(
        ["Normal", "Warning", "Fault"]
    )

    zone = random.choice(
        ["Zone A", "Zone B", "Zone C", "Zone D"]
    )

    risk_score = 0

    if gas_level > 300:
        risk_score += 2

    if temperature > 50:
        risk_score += 2

    if pressure > 3.5:
        risk_score += 1

    if maintenance == "Yes":
        risk_score += 1

    if permit == "Yes":
        risk_score += 1

    if machine_status == "Fault":
        risk_score += 2

    if worker_count > 20:
        risk_score += 1

    if risk_score <= 2:
        risk = "Safe"
    elif risk_score <= 5:
        risk = "Warning"
    else:
        risk = "Critical"

    data.append([
        timestamp,
        temperature,
        gas_level,
        pressure,
        humidity,
        worker_count,
        maintenance,
        permit,
        machine_status,
        zone,
        risk
    ])

columns = [
    "Timestamp",
    "Temperature",
    "GasLevel",
    "Pressure",
    "Humidity",
    "WorkerCount",
    "Maintenance",
    "Permit",
    "MachineStatus",
    "Zone",
    "Risk"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("datasets/industrial_safety_dataset.csv", index=False)

print(df.head())

print("\nDataset Shape:", df.shape)

print("\nRisk Distribution:")

print(df["Risk"].value_counts())