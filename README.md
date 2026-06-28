# SafeSphereAI
# SafeSphere AI

AI-Powered Industrial Safety Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Scikit-Learn](https://img.shields.io/badge/ML-RandomForest-orange)
![Gemini](https://img.shields.io/badge/AI-Gemini-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## Overview

Industrial environments are exposed to multiple operational hazards, including gas leakage, abnormal temperature, pressure fluctuations, and equipment failures. Conventional monitoring systems typically generate alerts only after unsafe conditions arise.

SafeSphere AI addresses this challenge by continuously analyzing industrial sensor data, predicting risk using a Random Forest classifier, and generating AI-assisted safety recommendations through Google's Gemini API.

---

## Key Features

- Real-time industrial risk prediction
- Machine Learning-based hazard classification
- AI Safety Copilot for intelligent recommendations
- Interactive Streamlit dashboard
- Risk score and confidence estimation
- Plant zone monitoring
- Incident timeline visualization
- Downloadable incident reports
- FastAPI backend for REST APIs
- IoT-ready architecture

---

## System Architecture

```
Industrial Sensors
        │
        ▼
FastAPI Backend
        │
        ▼
Random Forest Model
        │
        ▼
Gemini AI Copilot
        │
        ▼
Streamlit Dashboard
```

---

## Machine Learning Pipeline

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Random Forest Training
5. Risk Prediction
6. AI Safety Analysis
7. Dashboard Visualization

---

## Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Machine Learning | Scikit-Learn |
| AI Assistant | Google Gemini API |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |
| Language | Python |

---

## Project Structure

```
SafeSphereAI/
│
├── backend/
│   ├── app.py
│   ├── predict.py
│   ├── schema.py
│   ├── ai_copilot.py
│   └── model.pkl
│
├── frontend/
│   └── dashboard.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<username>/SafeSphereAI.git
```

### Navigate to the project

```bash
cd SafeSphereAI
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root.

```text
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Running the Backend

```bash
uvicorn backend.app:app --reload
```

---

## Running the Frontend

```bash
streamlit run frontend/dashboard.py
```

---

## Workflow

```
Sensor Data
      │
      ▼
Random Forest Prediction
      │
      ▼
Risk Classification
      │
      ▼
Gemini AI Copilot
      │
      ▼
Dashboard Visualization
      │
      ▼
Incident Report
```

---

## Results

The system predicts three operational states:

- Safe
- Warning
- Critical

For each prediction, the platform provides:

- Risk Score
- Confidence Score
- Priority Level
- AI-generated Safety Report

---

## Future Enhancements

- PPE Detection using YOLOv8
- CCTV-based safety monitoring
- ESP32 sensor integration
- Firebase cloud logging
- SMS and email alert system
- Predictive maintenance
- Mobile application
- Edge AI deployment

---

## Team

**Team SafeSphere AI**

Kalinga Institute of Industrial Technology (KIIT)

---

## License

This project was developed for academic and hackathon purposes.

---

## Acknowledgements

- Google Gemini API
- FastAPI
- Streamlit
- Plotly
- Scikit-Learn
- Pandas
- Python
