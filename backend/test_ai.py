from ai_copilot import generate_ai_report

sensor = {
    "Temperature": 65,
    "GasLevel": 420,
    "Pressure": 3.5,
    "Humidity": 80,
    "WorkerCount": 20
}

print(generate_ai_report(sensor, "Critical"))