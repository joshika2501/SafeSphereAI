import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="SafeSphere AI",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main{
    background:#F5F7FA;
}

.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.08);
}

h1,h2,h3{
    color:#1F2937;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/factory.png",
        width=70
    )

    st.title("SafeSphere AI")

    st.caption("Industrial Safety Intelligence Platform")

    st.markdown("---")

    st.success(" System Online")

    st.markdown("### Navigation")

    st.write(" Dashboard")
    st.write(" Live Monitoring")
    st.write(" AI Safety Copilot")
    st.write(" PPE Detection")
    st.write(" Incident Reports")

    st.markdown("---")

    st.info(
        f"""
Version : **2.0**

Time :
{datetime.now().strftime("%d-%m-%Y %H:%M")}
"""
    )

# ==========================================================
# HEADER
# ==========================================================

left, right = st.columns([4,1])

with left:

    st.title("🏭 Industrial Safety Intelligence Platform")

    st.caption(
        "Real-Time AI Powered Industrial Risk Monitoring"
    )

with right:

    st.metric(
        "Status",
        "ONLINE"
    )

st.divider()

# ==========================================================
# LIVE SENSOR INPUTS
# ==========================================================

c1, c2, c3, c4 = st.columns(4)

temperature = c1.number_input(
    " Temperature (°C)",
    value=35.0,
    step=0.5
)

gas = c2.number_input(
    " Gas Level (ppm)",
    value=180.0,
    step=5.0
)

pressure = c3.number_input(
    " Pressure (bar)",
    value=2.80,
    step=0.10
)

workers = c4.number_input(
    " Workers",
    value=10,
    step=1
)

# ==========================================================
# LIVE KPI CARDS
# ==========================================================

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "Temperature",
    f"{temperature:.1f} °C",
    delta=f"{temperature-35:.1f}"
)

k2.metric(
    "Gas",
    f"{gas:.0f} ppm"
)

k3.metric(
    "Pressure",
    f"{pressure:.2f} bar"
)

k4.metric(
    "Workers",
    workers
)

st.divider()

# ==========================================================
# SENSOR CONFIGURATION
# ==========================================================

left, right = st.columns([2,1])

with left:

    st.subheader(" Sensor Configuration")

    a1, a2 = st.columns(2)

    humidity = a1.slider(
        "Humidity (%)",
        0,
        100,
        60
    )

    maintenance = a2.selectbox(
        "Maintenance",
        [
            "Yes",
            "No"
        ]
    )

    b1, b2 = st.columns(2)

    permit = b1.selectbox(
        "Permit",
        [
            "Yes",
            "No"
        ]
    )

    machine = b2.selectbox(
        "Machine Status",
        [
            "Normal",
            "Warning",
            "Fault"
        ]
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

    predict = st.button(
        " Predict Risk",
        use_container_width=True
    )

with right:

    st.subheader(" Current Readings")

    st.write(f" Temperature : **{temperature:.1f} °C**")
    st.write(f" Gas Level : **{gas:.0f} ppm**")
    st.write(f" Pressure : **{pressure:.2f} bar**")
    st.write(f" Humidity : **{humidity}%**")
    st.write(f" Workers : **{workers}**")
    st.write(f" Zone : **{zone}**")

st.divider()
# ==========================================================
# SEND DATA TO FASTAPI
# ==========================================================

if predict:

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

    try:

        with st.spinner(" Running AI Safety Analysis..."):

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=payload,
                timeout=30
            )

        if response.status_code != 200:

            st.error("Backend returned an error.")
            st.code(response.text)
            st.stop()

        result = response.json()

        risk = result["Predicted Risk"]
        score = result["Risk Score"]
        confidence = result["Confidence"]
        priority = result["Priority"]
        ai_report = result["AI Report"]

        st.divider()

# ==========================================================
# RISK STATUS
# ==========================================================

        if risk == "Safe":

            st.success(" SAFE OPERATING CONDITIONS")

        elif risk == "Warning":

            st.warning(" WARNING - ATTENTION REQUIRED")

        else:

            st.error(" CRITICAL - IMMEDIATE ACTION REQUIRED")

# ==========================================================
# SUMMARY METRICS
# ==========================================================

        m1, m2, m3 = st.columns(3)

        m1.metric(
            " Risk Score",
            score
        )

        m2.metric(
            " Confidence",
            f"{confidence*100:.1f}%"
        )

        m3.metric(
            " Priority",
            priority
        )

        st.divider()

# ==========================================================
# TWO COLUMN LAYOUT
# ==========================================================

        left, right = st.columns([2,1])

# ==========================================================
# LEFT COLUMN
# ==========================================================

        with left:

            st.subheader(" Overall Risk Gauge")

            fig = go.Figure(

                go.Indicator(

                    mode="gauge+number",

                    value=score,

                    title={
                        "text":"Overall Risk Score"
                    },

                    gauge={

                        "axis":{
                            "range":[0,100]
                        },

                        "bar":{
                            "color":"darkred"
                        },

                        "steps":[

                            {
                                "range":[0,40],
                                "color":"green"
                            },

                            {
                                "range":[40,70],
                                "color":"gold"
                            },

                            {
                                "range":[70,100],
                                "color":"red"
                            }

                        ]

                    }

                )

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.subheader(" Live Sensor Values")

            sensor_df = pd.DataFrame({

                "Sensor":[
                    "Temperature",
                    "Gas",
                    "Pressure",
                    "Humidity"
                ],

                "Value":[
                    temperature,
                    gas,
                    pressure,
                    humidity
                ]

            })

            st.bar_chart(
                sensor_df.set_index("Sensor")
            )
            # ==========================================================
# RIGHT COLUMN
# ==========================================================

        with right:

            st.subheader(" Plant Zone Status")

            zone_status = {

                "Zone A": " Safe",
                "Zone B": " Safe",
                "Zone C": " Safe",
                "Zone D": " Safe"

            }

            if risk == "Critical":

                zone_status[zone] = " Critical"

            elif risk == "Warning":

                zone_status[zone] = " Warning"

            else:

                zone_status[zone] = " Safe"

            st.metric("Zone A", zone_status["Zone A"])
            st.metric("Zone B", zone_status["Zone B"])
            st.metric("Zone C", zone_status["Zone C"])
            st.metric("Zone D", zone_status["Zone D"])

            st.markdown("---")

            st.subheader("⚡ Current Status")

            st.write(f"**Risk:** {risk}")
            st.write(f"**Priority:** {priority}")
            st.write(f"**Confidence:** {confidence*100:.1f}%")
            st.write(
                f"**Time:** {datetime.now().strftime('%H:%M:%S')}"
            )

        st.divider()

# ==========================================================
# GEMINI AI SAFETY COPILOT
# ==========================================================

        st.subheader(" Gemini AI Safety Copilot")

        st.info(ai_report)

        st.divider()

# ==========================================================
# INCIDENT TIMELINE
# ==========================================================

        st.subheader(" Incident Timeline")

        timeline = pd.DataFrame({

            "Time":[
                datetime.now().strftime("%H:%M:%S")
            ],

            "Risk":[
                risk
            ],

            "Priority":[
                priority
            ],

            "Status":[
                "Prediction Completed"
            ]

        })

        st.dataframe(
            timeline,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

# ==========================================================
# SENSOR SNAPSHOT
# ==========================================================

        st.subheader(" Current Sensor Snapshot")

        snapshot = pd.DataFrame({

            "Parameter":[
                "Temperature",
                "Gas Level",
                "Pressure",
                "Humidity",
                "Workers",
                "Maintenance",
                "Permit",
                "Machine Status",
                "Plant Zone"
            ],

            "Value":[
                f"{temperature:.1f} °C",
                f"{gas:.0f} ppm",
                f"{pressure:.2f} bar",
                f"{humidity} %",
                workers,
                maintenance,
                permit,
                machine,
                zone
            ]

        })

        st.dataframe(
            snapshot,
            use_container_width=True,
            hide_index=True
        )

        st.divider()
        # ==========================================================
# SAFETY CHECKLIST
# ==========================================================

        st.subheader(" Safety Checklist")

        checklist = pd.DataFrame({

            "Safety Check":[

                "Gas Sensor Operational",
                "Pressure Sensor Operational",
                "Machine Inspection Completed",
                "Workers Accounted For",
                "Permit Verified",
                "Maintenance Verified"

            ],

            "Status":[

                "✔",
                "✔",
                "✔",
                "✔",
                "✔",
                "✔"

            ]

        })

        st.table(checklist)

        st.divider()

# ==========================================================
# DOWNLOAD INCIDENT REPORT
# ==========================================================

        report = f"""
===============================
SafeSphere AI Incident Report
===============================

Prediction Time:
{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

--------------------------------
Prediction
--------------------------------

Risk          : {risk}
Risk Score    : {score}
Confidence    : {confidence*100:.1f}%
Priority      : {priority}

--------------------------------
Sensor Values
--------------------------------

Temperature   : {temperature:.1f} °C
Gas Level     : {gas:.0f} ppm
Pressure      : {pressure:.2f} bar
Humidity      : {humidity} %
Workers       : {workers}

Maintenance   : {maintenance}
Permit        : {permit}
Machine       : {machine}
Plant Zone    : {zone}

--------------------------------
AI Safety Copilot
--------------------------------

{ai_report}

--------------------------------
Generated by SafeSphere AI
--------------------------------
"""

        st.download_button(

            label=" Download Incident Report",

            data=report,

            file_name="Incident_Report.txt",

            mime="text/plain",

            use_container_width=True

        )

        st.divider()

# ==========================================================
# FOOTER
# ==========================================================

        st.caption(

            f"""
🏭 SafeSphere AI • Industrial Safety Intelligence Platform

Prediction generated on
{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
"""

        )

# ==========================================================
# ERROR HANDLING
# ==========================================================

    except requests.exceptions.ConnectionError:

        st.error(
            " Cannot connect to FastAPI backend.\n\n"
            "Please ensure the backend is running:\n\n"
            "uvicorn backend.app:app --reload"
        )

    except requests.exceptions.Timeout:

        st.error(
            " Backend request timed out."
        )

    except Exception as e:

        st.error(" Unexpected Error")

        st.exception(e)