import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "predictive_model.pkl"
ENCODER_PATH = BASE_DIR / "model" / "type_encoder.pkl"

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)


st.set_page_config(
    page_title="AI Predictive Maintenance",
    page_icon="🤖",
    layout="centered"
)
with st.sidebar:
    st.title("⚙️ Project Info")

    st.write("**Project:** AI Predictive Maintenance")

    st.write("**Algorithm:** Random Forest")

    st.write("**Accuracy:** 98.4%")

    st.write("**Developer:** B.J. Navadeep")

st.title("🤖 AI Predictive Maintenance System")
# User Inputs
machine = st.selectbox(
    "Machine Type",
    ["L", "M", "H"]
)

air_temp = st.number_input(
    "Air Temperature (K)",
    value=298.1
)

process_temp = st.number_input(
    "Process Temperature (K)",
    value=308.6
)

rpm = st.number_input(
    "Rotational Speed (RPM)",
    value=1551
)

torque = st.number_input(
    "Torque (Nm)",
    value=42.8
)

tool_wear = st.number_input(
    "Tool Wear (Minutes)",
    value=0
)

if st.button("🔍 Predict Machine Status"):

    machine_encoded = encoder.transform([machine])[0]

    input_data = pd.DataFrame(
        [[
            machine_encoded,
            air_temp,
            process_temp,
            rpm,
            torque,
            tool_wear
        ]],
        columns=[
            "Type",
            "Air temperature [K]",
            "Process temperature [K]",
            "Rotational speed [rpm]",
            "Torque [Nm]",
            "Tool wear [min]"
        ]
    )

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.divider()

    if prediction == 0:
        st.success("🟢 Machine Status: HEALTHY")
    else:
        st.error("🔴 Machine Failure Likely")

    st.metric(
        "Failure Probability",
        f"{probability*100:.2f}%"
    )

    st.progress(float(probability))

    st.subheader("💡 Maintenance Recommendation")

    if prediction == 0:
        st.info(
            "Machine is operating normally.\nContinue regular maintenance schedule."
        )
    else:
        st.warning(
            "Inspect bearings.\n"
            "Check tool wear.\n"
            "Schedule preventive maintenance immediately."
        )

st.divider()

st.caption("Developed by B.J. Navadeep | AI Internship Project")