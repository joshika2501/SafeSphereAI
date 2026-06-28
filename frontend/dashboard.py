import streamlit as st
import requests

st.set_page_config(
    page_title="SafeSphere AI",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 SafeSphere AI")
st.caption("Industrial Safety Intelligence Platform")

col1, col2, col3, col4 = st.columns(4)

temperature = col1.number_input("🌡 Temperature (°C)", value=35.0)
gas = col2.number_input("☁ Gas Level (ppm)", value=180.0)
pressure = col3.number_input("⚙ Pressure (bar)", value=2.8)
workers = col4.number_input("👷 Workers", value=10)

col1, col2 = st.columns(2)

humidity = col1.number_input("Humidity (%)", value=60.0)
maintenance = col2.selectbox("Maintenance", ["Yes", "No"])

col1, col2 = st.columns(2)

permit = col1.selectbox("Permit", ["Yes", "No"])
machine = col2.selectbox("Machine Status", ["Normal", "Warning", "Fault"])

zone = st.selectbox(
    "Plant Zone",
    ["Zone A", "Zone B", "Zone C", "Zone D"]
)

# 2. NOW display KPI cards
st.divider()

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "🌡 Temperature",
    f"{temperature:.1f} °C",
    delta=f"{temperature-35:.1f}"
)

k2.metric(
    "☁ Gas",
    f"{gas:.0f} ppm"
)

k3.metric(
    "⚙ Pressure",
    f"{pressure:.2f} bar"
)

k4.metric(
    "👷 Workers",
    workers
)

st.divider()

st.divider()

col1, col2, col3, col4 = st.columns(4)

temperature = col1.number_input("🌡 Temperature (°C)", value=35.0)
gas = col2.number_input("☁ Gas Level (ppm)", value=180.0)
pressure = col3.number_input("⚙ Pressure (bar)", value=2.8)
workers = col4.number_input("👷 Workers", value=10)

col1, col2 = st.columns(2)

humidity = col1.number_input("Humidity (%)", value=60.0)

maintenance = col2.selectbox(
    "Maintenance",
    ["Yes", "No"]
)

col1, col2 = st.columns(2)

permit = col1.selectbox(
    "Permit",
    ["Yes", "No"]
)

machine = col2.selectbox(
    "Machine Status",
    ["Normal", "Warning", "Fault"]
)

zone = st.selectbox(
    "Plant Zone",
    [
        "Zone A",
        "Zone B",
        "Zone C",
        "Zone D"
    ]
)

st.divider()

if st.button("🚨 Predict Risk", use_container_width=True):

    payload = {
        "Temperature": temperature,
        "GasLevel": gas,
        "Pressure": pressure,
        "Humidity": humidity,
        "WorkerCount": workers,
        "Maintenance": maintenance,
        "Permit": permit,
        "MachineStatus": machine,
        "Zone": zone
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )

    risk = response.json()["Predicted Risk"]

    if risk == "Safe":
        st.success("🟢 SAFE")

    elif risk == "Warning":
        st.warning("🟡 WARNING")

    else:
        st.error("🔴 CRITICAL")

    st.subheader("AI Recommendation")

    if risk == "Safe":
        st.info(
            "All monitored parameters are within acceptable operating limits."
        )

    elif risk == "Warning":
        st.warning(
            "Monitor sensor values closely and inspect equipment."
        )

    else:
        st.error(
            """
Immediate action recommended.

• Stop hazardous operations.

• Notify the safety officer.

• Inspect the affected machine.

• Evacuate nearby personnel if necessary.
"""
        )