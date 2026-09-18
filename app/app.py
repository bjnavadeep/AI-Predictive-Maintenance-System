import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH   = BASE_DIR / "model" / "predictive_model.pkl"
ENCODER_PATH = BASE_DIR / "model" / "type_encoder.pkl"
CONFIG_PATH  = BASE_DIR / "config.yaml"

# ── Load configuration ────────────────────────────────────────────────────────
with open(CONFIG_PATH, "r") as _f:
    CFG = yaml.safe_load(_f)

_s   = CFG["sustainability"]       # shorthand
_thr = CFG["thresholds"]           # shorthand
_def = CFG["sensor_defaults"]      # shorthand
_co2 = CFG["carbon"]               # shorthand
_rul = CFG["rul"]                  # shorthand
_bdg = CFG["badges"]               # shorthand
_rt  = CFG["realtime"]             # shorthand

# Load model and encoder — show a clear error instead of crashing
_missing = [p for p in (MODEL_PATH, ENCODER_PATH) if not p.exists()]
if _missing:
    st.set_page_config(page_title="AI Sustainable Predictive Maintenance", page_icon="🌱", layout="wide")
    st.error("❌ Model files not found. Please make sure the following files exist:")
    for p in _missing:
        st.code(str(p))
    st.info("Re-run the training notebook at `notebooks/Predictive_Maintenance.ipynb` to generate them.")
    st.stop()

try:
    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
except Exception as e:
    st.set_page_config(page_title="AI Sustainable Predictive Maintenance", page_icon="🌱", layout="wide")
    st.error(f"❌ Failed to load model files: {e}")
    st.stop()

st.set_page_config(page_title="AI Sustainable Predictive Maintenance", page_icon="🌱", layout="wide")

# ── Session-state initialisation ────────────────────────────────────────────
if "history" not in st.session_state:
    st.session_state.history = []
if "rt_running" not in st.session_state:
    st.session_state.rt_running = False
if "rt_wear" not in st.session_state:
    st.session_state.rt_wear = int(_def["tool_wear_min"])

st.title("🌱 AI-Powered Sustainable Predictive Maintenance System")
st.caption("AI + Industrial IoT + Predictive Maintenance + Climate Action & Sustainability")

with st.sidebar:
    st.header("⚙️ Project Information")
    st.write("**Track:** AI for Impact")
    st.write("**Use Case:** Climate Action & Sustainability")
    st.write("**ML Algorithm:** Random Forest")
    st.write("**Model Accuracy:** 98.4%")
    st.divider()
    st.info("Predict failures early, plan maintenance responsibly, and monitor sustainability indicators.")

    # ── Real-time simulation toggle ──────────────────────────────────────────
    st.divider()
    st.subheader("⏱️ Live Monitoring Mode")
    rt_on = st.toggle("Enable Real-Time Simulation", value=st.session_state.rt_running)
    if rt_on != st.session_state.rt_running:
        st.session_state.rt_running = rt_on
        if rt_on:
            st.session_state.rt_wear = int(_def["tool_wear_min"])
    if st.session_state.rt_running:
        st.success("🟢 Simulation running — tool wear auto-incrementing")
        st.caption(f"Incrementing +{_rt['wear_increment_min']} min every {_rt['tick_interval_sec']}s")
    else:
        st.caption("Toggle ON to simulate real-time sensor degradation.")

    # ── Feature Importance Chart ─────────────────────────────────────────────
    st.divider()
    st.subheader("🏆 Model Feature Importance")
    _feat_names = [
        "Machine Type", "Air Temp (K)", "Process Temp (K)",
        "Rotational Speed (RPM)", "Torque (Nm)", "Tool Wear (min)"
    ]
    _importances = model.feature_importances_
    _fi_df = pd.DataFrame({
        "Feature": _feat_names,
        "Importance": _importances
    }).sort_values("Importance", ascending=True)

    _fig, _ax = plt.subplots(figsize=(4, 3))
    _bars = _ax.barh(_fi_df["Feature"], _fi_df["Importance"], color="#3b82d4")
    _ax.set_xlabel("Importance Score")
    _ax.set_title("Which sensors matter most?")
    # Annotate each bar with its value
    for bar, val in zip(_bars, _fi_df["Importance"]):
        _ax.text(val + 0.002, bar.get_y() + bar.get_height() / 2,
                 f"{val:.3f}", va="center", fontsize=7)
    _fig.tight_layout()
    st.pyplot(_fig)
    plt.close(_fig)
    st.caption("Importance scores from the trained Random Forest model. Higher = more influential.")

# ── Feature 5: Real-time wear simulation ────────────────────────────────────
import time as _time
if st.session_state.rt_running:
    st.session_state.rt_wear = min(
        st.session_state.rt_wear + _rt["wear_increment_min"],
        _rul["max_tool_life_min"]
    )

st.subheader("📡 Machine Sensor Inputs")
if st.session_state.rt_running:
    st.info(f"⏱️ **Live Monitoring Active** — Tool wear auto-incrementing. Current simulated wear: **{st.session_state.rt_wear} min**")

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    machine = st.selectbox("Machine Type", ["L", "M", "H"])
with c2:
    air_temp = st.number_input("Air Temperature (K)", value=float(_def["air_temperature_K"]), step=0.1)
with c3:
    process_temp = st.number_input("Process Temperature (K)", value=float(_def["process_temperature_K"]), step=0.1)
with c4:
    rpm = st.number_input("Rotational Speed (RPM)", value=int(_def["rotational_speed_rpm"]), step=10)
with c5:
    torque = st.number_input("Torque (Nm)", value=float(_def["torque_Nm"]), step=0.1)

# In live mode use simulated wear; otherwise use manual input
if st.session_state.rt_running:
    tool_wear = st.session_state.rt_wear
    st.metric("🔧 Simulated Tool Wear", f"{tool_wear} min",
              delta=f"+{_rt['wear_increment_min']} min/tick")
else:
    tool_wear = st.number_input("Tool Wear (Minutes)", min_value=0,
                                value=int(_def["tool_wear_min"]), step=1)

if st.session_state.rt_running:
    _time.sleep(_rt["tick_interval_sec"])
    st.rerun()

if st.button("🔍 Analyze Machine & Sustainability", type="primary", use_container_width=True) or st.session_state.rt_running:
    machine_encoded = encoder.transform([machine])[0]
    input_data = pd.DataFrame([[machine_encoded, air_temp, process_temp, rpm, torque, tool_wear]], columns=[
        "Type", "Air temperature [K]", "Process temperature [K]",
        "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]"
    ])

    prediction = model.predict(input_data)[0]
    probability = float(model.predict_proba(input_data)[0][1])
    health = max(0.0, 1.0 - probability)

    # Sustainability indicators — all constants come from config.yaml
    temp_stress   = min(max((process_temp - _s["temp_reference_K"]) / _s["temp_stress_range_K"], 0), 1)
    wear_stress   = min(tool_wear / _s["tool_wear_max_min"], 1)
    torque_stress = min(max((torque - _s["torque_reference_Nm"]) / _s["torque_stress_range_Nm"], 0), 1)
    operational_efficiency = max(
        _s["efficiency_min"],
        min(_s["efficiency_max"],
            _s["efficiency_base"]
            - _s["efficiency_temp_penalty"]   * temp_stress
            - _s["efficiency_wear_penalty"]   * wear_stress
            - _s["efficiency_torque_penalty"] * torque_stress)
    )
    waste_avoided    = round(_s["waste_base_kg"]    + probability * _s["waste_scale_kg"],    2)
    downtime_avoided = round(_s["downtime_base_hrs"] + probability * _s["downtime_scale_hrs"], 1)
    sustainability   = round(max(0.0, min(100.0,
        _s["health_weight"]     * health
        + _s["efficiency_weight"] * (operational_efficiency / 100)
    )), 1)

    # Save this run to history
    st.session_state.history.append({
        "Run": len(st.session_state.history) + 1,
        "Failure Probability (%)": round(probability * 100, 2),
        "Machine Health (%)": round(health * 100, 1),
        "Sustainability Score": sustainability,
        "Operational Efficiency (%)": round(operational_efficiency, 1),
    })

    st.divider()
    st.subheader("📊 AI Machine Health Dashboard")

    def _card_color(value, thresholds, reverse=False):
        """Return (bg_color, border_color, label) based on value vs thresholds (low, high)."""
        low, high = thresholds
        if reverse:
            # Lower is better (e.g. failure probability)
            if value <= low:
                return "#d4edda", "#28a745", "🟢 Good"
            elif value <= high:
                return "#fff3cd", "#ffc107", "🟡 Moderate"
            else:
                return "#f8d7da", "#dc3545", "🔴 Critical"
        else:
            # Higher is better (e.g. health, efficiency)
            if value >= high:
                return "#d4edda", "#28a745", "🟢 Good"
            elif value >= low:
                return "#fff3cd", "#ffc107", "🟡 Moderate"
            else:
                return "#f8d7da", "#dc3545", "🔴 Critical"

    _ct = CFG["card_thresholds"]
    cards = [
        ("⚠️ Failure Probability",    f"{probability * 100:.2f}%",    probability * 100,    tuple(_ct["failure_probability"]),    True),
        ("💚 Machine Health",          f"{health * 100:.1f}%",          health * 100,          tuple(_ct["machine_health"]),          False),
        ("⚙️ Operational Efficiency",  f"{operational_efficiency:.1f}%", operational_efficiency, tuple(_ct["operational_efficiency"]), False),
        ("🌱 Sustainability Score",    f"{sustainability}/100",          sustainability,         tuple(_ct["sustainability_score"]),    False),
    ]

    cols = st.columns(4)
    for col, (title, value_str, value_num, thresholds, reverse) in zip(cols, cards):
        bg, border, label = _card_color(value_num, thresholds, reverse)
        col.markdown(
            f"""
            <div style="
                background:{bg};
                border-left: 5px solid {border};
                border-radius: 8px;
                padding: 16px 18px;
                margin-bottom: 8px;
            ">
                <div style="font-size:12px;color:#555;font-weight:600;margin-bottom:4px;">{title}</div>
                <div style="font-size:26px;font-weight:700;color:#1f2328;">{value_str}</div>
                <div style="font-size:11px;margin-top:4px;color:#555;">{label}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.progress(probability)

    if prediction == 0:
        st.success("🟢 Machine Status: HEALTHY — operating within normal parameters.")
    else:
        st.error("🔴 Machine Failure Likely — immediate inspection recommended.")

    st.subheader("🛠️ Preventive Maintenance Recommendation")
    if prediction == 0 and probability < _thr["risk_low_max"]:
        st.info("Machine is operating normally. Continue condition monitoring and routine maintenance. Avoid unnecessary component replacement.")
    elif probability < _thr["risk_moderate_max"]:
        st.warning("Moderate risk detected. Schedule preventive inspection, monitor tool wear, and review temperature/vibration-related operating conditions.")
    else:
        st.error("High risk detected. Inspect critical components, check tool wear and thermal conditions, and schedule preventive maintenance as soon as possible.")

    st.subheader("🌱 Sustainability Impact")
    s1, s2, s3 = st.columns(3)
    s1.metric("Estimated Material Waste Avoided", f"{waste_avoided} kg")
    s2.metric("Potential Downtime Avoided", f"{downtime_avoided} hrs")
    s3.metric("Resource-Efficient Operation", f"{operational_efficiency:.1f}%")
    st.caption("Prototype estimates for demonstration. For deployment, connect actual plant energy, material, replacement, and downtime records.")

    # ── Feature 1: Carbon Footprint Estimator ───────────────────────────────
    st.subheader("🌍 Carbon Footprint Estimator")

    co2_energy_avoided = round(
        downtime_avoided * _co2["machine_power_kW"] * _co2["grid_carbon_intensity_kgCO2_per_kWh"], 2
    )
    co2_repair_avoided = round(
        probability * _co2["emergency_repair_co2_overhead_kg"], 2
    )
    co2_total_avoided = round(co2_energy_avoided + co2_repair_avoided, 2)

    cf1, cf2, cf3 = st.columns(3)
    cf1.metric("⚡ Energy CO₂ Avoided", f"{co2_energy_avoided} kg",
               help="CO₂ saved by avoiding unplanned downtime (machine idle energy waste)")
    cf2.metric("🚚 Repair Logistics CO₂ Avoided", f"{co2_repair_avoided} kg",
               help="CO₂ saved by avoiding emergency repair overhead")
    cf3.metric("🌍 Total CO₂ Avoided", f"{co2_total_avoided} kg CO₂",
               help="Total estimated carbon footprint reduction from this predictive action")

    # Visual CO₂ bar
    co2_max = _co2["machine_power_kW"] * _co2["grid_carbon_intensity_kgCO2_per_kWh"] * 12 + _co2["emergency_repair_co2_overhead_kg"]
    st.progress(min(co2_total_avoided / co2_max, 1.0),
                text=f"🌿 {co2_total_avoided} kg CO₂ avoided out of a possible {round(co2_max, 1)} kg max")
    st.caption("Based on grid carbon intensity of "
               f"{_co2['grid_carbon_intensity_kgCO2_per_kWh']} kg CO₂/kWh and "
               f"{_co2['machine_power_kW']} kW machine power. Calibrate in config.yaml.")

    # ── Feature 3: Sustainability Badge ─────────────────────────────────────
    st.subheader("🏅 Sustainability Badge")

    if sustainability >= _bdg["platinum"]:
        badge_html = """
        <div style="background:#e8f5e9;border:3px solid #1b5e20;border-radius:12px;
                    padding:18px 24px;text-align:center;">
            <div style="font-size:40px">🏆</div>
            <div style="font-size:22px;font-weight:700;color:#1b5e20;">PLATINUM</div>
            <div style="font-size:13px;color:#2e7d32;margin-top:4px;">Exceptional Sustainability Performance</div>
        </div>"""
    elif sustainability >= _bdg["gold"]:
        badge_html = """
        <div style="background:#fffde7;border:3px solid #f57f17;border-radius:12px;
                    padding:18px 24px;text-align:center;">
            <div style="font-size:40px">🥇</div>
            <div style="font-size:22px;font-weight:700;color:#f57f17;">GOLD</div>
            <div style="font-size:13px;color:#e65100;margin-top:4px;">Strong Sustainability Performance</div>
        </div>"""
    elif sustainability >= _bdg["silver"]:
        badge_html = """
        <div style="background:#f5f5f5;border:3px solid #757575;border-radius:12px;
                    padding:18px 24px;text-align:center;">
            <div style="font-size:40px">🥈</div>
            <div style="font-size:22px;font-weight:700;color:#424242;">SILVER</div>
            <div style="font-size:13px;color:#616161;margin-top:4px;">Acceptable Sustainability Performance</div>
        </div>"""
    else:
        badge_html = """
        <div style="background:#fce4ec;border:3px solid #b71c1c;border-radius:12px;
                    padding:18px 24px;text-align:center;">
            <div style="font-size:40px">⚠️</div>
            <div style="font-size:22px;font-weight:700;color:#b71c1c;">NEEDS IMPROVEMENT</div>
            <div style="font-size:13px;color:#c62828;margin-top:4px;">Maintenance action required to improve sustainability</div>
        </div>"""

    _bc1, _bc2, _bc3 = st.columns([1, 2, 1])
    with _bc2:
        st.markdown(badge_html, unsafe_allow_html=True)
    st.caption(f"Thresholds — Platinum: ≥{_bdg['platinum']} · Gold: ≥{_bdg['gold']} · Silver: ≥{_bdg['silver']}")

    # ── Feature 4: Remaining Useful Life (RUL) Estimator ────────────────────
    st.subheader("⏳ Remaining Useful Life (RUL) Estimator")

    rul_wear_remaining = max(0, _rul["max_tool_life_min"] - tool_wear)
    rul_hours_remaining = round(rul_wear_remaining / _rul["avg_wear_rate_min_per_hr"], 1)
    rul_pct = rul_wear_remaining / _rul["max_tool_life_min"]

    r1, r2, r3 = st.columns(3)
    r1.metric("🔧 Tool Wear Remaining", f"{rul_wear_remaining} min",
              delta=f"{tool_wear} min used", delta_color="inverse")
    r2.metric("⏱️ Estimated Hours Left", f"{rul_hours_remaining} hrs",
              help=f"Based on avg wear rate of {_rul['avg_wear_rate_min_per_hr']} min/hr")
    r3.metric("📊 Tool Life Remaining", f"{rul_pct * 100:.1f}%")

    # RUL progress bar — green to red
    rul_color = "normal" if rul_pct > 0.5 else "inverse"
    st.progress(rul_pct, text=f"Tool life: {rul_pct * 100:.1f}% remaining "
                              f"({rul_wear_remaining} min / {_rul['max_tool_life_min']} min max)")

    if rul_pct <= 0.10:
        st.error(f"🔴 **Critical:** Tool life almost exhausted ({rul_wear_remaining} min left). Replace immediately.")
    elif rul_pct <= 0.30:
        st.warning(f"🟡 **Warning:** Only {rul_hours_remaining} hrs of tool life remaining. Schedule replacement soon.")
    else:
        st.success(f"🟢 **Good:** Approximately {rul_hours_remaining} hrs of tool life remaining.")
    st.caption(f"RUL estimate based on max tool life of {_rul['max_tool_life_min']} min and avg wear rate of {_rul['avg_wear_rate_min_per_hr']} min/hr. Calibrate in config.yaml.")

    # ── SHAP Explainability ──────────────────────────────────────────────────
    st.subheader("🔍 Why Did the Model Predict This? (SHAP Explanation)")

    try:
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(input_data)

        # For binary classification shap_values is a list [class0, class1]
        # We want class 1 (failure)
        if isinstance(shap_values, list):
            sv = shap_values[1][0]
        else:
            sv = shap_values[0]

        feature_names = [
            "Machine Type", "Air Temp (K)", "Process Temp (K)",
            "Rotational Speed (RPM)", "Torque (Nm)", "Tool Wear (min)"
        ]

        shap_df = pd.DataFrame({
            "Feature": feature_names,
            "SHAP Value": sv,
            "Impact": ["⬆ Increases Risk" if v > 0 else "⬇ Reduces Risk" for v in sv],
            "Abs Contribution": np.abs(sv)
        }).sort_values("Abs Contribution", ascending=False).reset_index(drop=True)

        # Bar chart using matplotlib
        fig, ax = plt.subplots(figsize=(7, 3))
        colors = ["#e05c5c" if v > 0 else "#4caf7d" for v in shap_df["SHAP Value"]]
        ax.barh(shap_df["Feature"], shap_df["SHAP Value"], color=colors)
        ax.axvline(0, color="black", linewidth=0.8)
        ax.set_xlabel("SHAP Value  (positive = pushes toward failure)")
        ax.set_title("Feature Contribution to Failure Prediction")
        ax.invert_yaxis()
        fig.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

        st.caption("🔴 Red bars push the prediction toward failure &nbsp;|&nbsp; 🟢 Green bars push toward healthy")

        # Top driver sentence
        top = shap_df.iloc[0]
        direction = "increasing failure risk" if top["SHAP Value"] > 0 else "reducing failure risk"
        st.info(f"**Top driver:** `{top['Feature']}` is the most influential sensor, {direction} the most.")

    except Exception as shap_err:
        st.warning(f"SHAP explanation unavailable: {shap_err}")

    # ── History / Trend Chart ────────────────────────────────────────────────
    if len(st.session_state.history) > 1:
        st.subheader("📈 Analysis History & Trends")
        hist_df = pd.DataFrame(st.session_state.history).set_index("Run")

        tab1, tab2 = st.tabs(["Failure Probability & Health", "Sustainability & Efficiency"])

        with tab1:
            st.line_chart(hist_df[["Failure Probability (%)", "Machine Health (%)"]])
        with tab2:
            st.line_chart(hist_df[["Sustainability Score", "Operational Efficiency (%)"]])

        st.caption(f"Showing {len(st.session_state.history)} analysis runs this session. "
                   "Each point represents one 'Analyze' button click.")

        if st.button("🗑️ Clear History", use_container_width=False):
            st.session_state.history = []
            st.rerun()
    else:
        st.info("📈 **Trend chart** will appear here after your **2nd analysis run**. "
                "Change sensor values and click Analyze again to see trends.")

    # ── Sensor & Risk Summary ────────────────────────────────────────────────
    st.subheader("📋 Sensor & Risk Summary")
    summary = pd.DataFrame({
        "Parameter": ["Machine Type", "Air Temperature", "Process Temperature", "RPM", "Torque", "Tool Wear"],
        "Value": [machine, f"{air_temp:.1f} K", f"{process_temp:.1f} K", f"{rpm} RPM", f"{torque:.1f} Nm", f"{tool_wear} min"]
    })
    st.dataframe(summary, use_container_width=True, hide_index=True)

    # ── Download Report ──────────────────────────────────────────────────────
    st.subheader("📥 Download Report")

    report_df = pd.DataFrame({
        "Field": [
            "Machine Type",
            "Air Temperature (K)",
            "Process Temperature (K)",
            "Rotational Speed (RPM)",
            "Torque (Nm)",
            "Tool Wear (min)",
            "Machine Status",
            "Failure Probability (%)",
            "Machine Health (%)",
            "Operational Efficiency (%)",
            "Sustainability Score (/100)",
            "Estimated Material Waste Avoided (kg)",
            "Potential Downtime Avoided (hrs)",
        ],
        "Value": [
            machine,
            air_temp,
            process_temp,
            rpm,
            torque,
            tool_wear,
            "HEALTHY" if prediction == 0 else "FAILURE LIKELY",
            f"{probability * 100:.2f}",
            f"{health * 100:.1f}",
            f"{operational_efficiency:.1f}",
            f"{sustainability}",
            f"{waste_avoided}",
            f"{downtime_avoided}",
        ]
    })

    col_csv, col_txt = st.columns(2)

    with col_csv:
        csv_bytes = report_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📄 Download as CSV",
            data=csv_bytes,
            file_name="maintenance_report.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with col_txt:
        lines = ["AI Predictive Maintenance Report", "=" * 40]
        for _, row in report_df.iterrows():
            lines.append(f"{row['Field']:<45}: {row['Value']}")
        txt_bytes = "\n".join(lines).encode("utf-8")
        st.download_button(
            label="📝 Download as TXT",
            data=txt_bytes,
            file_name="maintenance_report.txt",
            mime="text/plain",
            use_container_width=True,
        )

    # ── AI Sustainability Assistant ──────────────────────────────────────────
    st.subheader("🤖 AI Sustainability Assistant")

    # Build a rich context string from all computed values for this run
    _status_str  = "HEALTHY" if prediction == 0 else "FAILURE LIKELY"
    _risk_level  = "low" if probability < _thr["risk_low_max"] else ("moderate" if probability < _thr["risk_moderate_max"] else "high")
    _health_str  = "excellent" if health > 0.80 else ("moderate" if health > 0.40 else "poor")
    _eff_str     = "efficient" if operational_efficiency >= 90 else ("acceptable" if operational_efficiency >= 70 else "inefficient")

    def _ai_response(q: str) -> str:
        """Generate a context-aware answer using actual machine metrics."""
        q = q.lower().strip()

        # ── Failure / risk ───────────────────────────────────────────────────
        if any(w in q for w in ["risk", "fail", "why", "cause", "reason", "danger"]):
            resp = (
                f"The machine is currently **{_status_str}** with a failure probability of "
                f"**{probability * 100:.2f}%** — this is a **{_risk_level} risk** level.\n\n"
            )
            if process_temp > _thr["process_temp_high_K"]:
                resp += f"- ⚠️ Process temperature is high at **{process_temp:.1f} K** (above {_thr['process_temp_high_K']} K), which stresses components.\n"
            if tool_wear > _thr["tool_wear_high_min"]:
                resp += f"- ⚠️ Tool wear is elevated at **{tool_wear} min** — consider replacing the tool soon.\n"
            if torque > _thr["torque_high_Nm"]:
                resp += f"- ⚠️ Torque of **{torque:.1f} Nm** is above normal operating range.\n"
            if rpm < _thr["rpm_min"] or rpm > _thr["rpm_max"]:
                resp += f"- ⚠️ Rotational speed of **{rpm} RPM** is outside the typical safe range ({_thr['rpm_min']}–{_thr['rpm_max']} RPM).\n"
            if _risk_level == "low":
                resp += "\n✅ All sensor readings are within acceptable ranges. No immediate action required."
            return resp

        # ── Maintenance ──────────────────────────────────────────────────────
        elif any(w in q for w in ["maintain", "maintenance", "service", "fix", "repair", "inspect", "action"]):
            if _risk_level == "low":
                return (
                    "✅ The machine is healthy. **Continue routine condition-based monitoring.**\n\n"
                    "- Check tool wear every scheduled interval\n"
                    "- Monitor temperature trends over time\n"
                    "- Avoid unnecessary part replacements — they waste materials and increase cost\n"
                    f"- Next suggested inspection: when tool wear exceeds **200 min** (currently {tool_wear} min)"
                )
            elif _risk_level == "moderate":
                return (
                    "⚠️ Moderate risk detected. **Schedule a preventive inspection soon.**\n\n"
                    f"- Current failure probability: **{probability * 100:.2f}%**\n"
                    f"- Tool wear: **{tool_wear} min** — inspect for wear and replace if needed\n"
                    f"- Process temp: **{process_temp:.1f} K** — verify cooling system\n"
                    "- Avoid running at full load until inspected\n"
                    "- Preventive maintenance now is cheaper and greener than emergency repair"
                )
            else:
                return (
                    "🔴 High risk — **immediate maintenance required.**\n\n"
                    f"- Failure probability: **{probability * 100:.2f}%**\n"
                    "- Stop non-critical operations and perform a full inspection\n"
                    f"- Tool wear at **{tool_wear} min** — likely needs replacement\n"
                    f"- Process temp **{process_temp:.1f} K** — check cooling and lubrication\n"
                    "- Delaying maintenance increases waste, downtime, and part replacement costs"
                )

        # ── Sustainability / waste / environment ─────────────────────────────
        elif any(w in q for w in ["sustain", "waste", "environment", "green", "carbon", "eco", "energy", "efficient"]):
            return (
                f"🌱 **Sustainability Summary for this analysis:**\n\n"
                f"- **Sustainability Score:** {sustainability}/100\n"
                f"- **Material Waste Avoided:** ~{waste_avoided} kg (by acting before failure)\n"
                f"- **Downtime Avoided:** ~{downtime_avoided} hrs\n"
                f"- **Operational Efficiency:** {operational_efficiency:.1f}% — {_eff_str}\n\n"
                f"By predicting failures early, you avoid emergency repairs that consume "
                f"extra materials, energy, and generate more waste. "
                f"A {_risk_level}-risk machine like this one "
                f"{'still benefits from monitoring' if _risk_level == 'low' else 'should be serviced to reduce its environmental footprint'}."
            )

        # ── Health ───────────────────────────────────────────────────────────
        elif any(w in q for w in ["health", "condition", "status", "state", "score"]):
            return (
                f"💚 **Machine Health: {health * 100:.1f}%** — rated as **{_health_str}**.\n\n"
                f"- Failure Probability: {probability * 100:.2f}%\n"
                f"- Operational Efficiency: {operational_efficiency:.1f}%\n"
                f"- Sustainability Score: {sustainability}/100\n\n"
                f"{'The machine is performing well within normal parameters.' if _health_str == 'excellent' else 'Some parameters need attention — review the sensor values and SHAP explanation above.'}"
            )

        # ── Sensor-specific ──────────────────────────────────────────────────
        elif any(w in q for w in ["temperature", "temp", "heat"]):
            return (
                f"🌡️ **Temperature Readings:**\n"
                f"- Air Temperature: **{air_temp:.1f} K** ({air_temp - 273.15:.1f} °C)\n"
                f"- Process Temperature: **{process_temp:.1f} K** ({process_temp - 273.15:.1f} °C)\n"
                f"- Temperature delta: **{process_temp - air_temp:.1f} K**\n\n"
                f"{'⚠️ Process temperature is elevated — check cooling.' if process_temp > _thr['process_temp_high_K'] else '✅ Temperature levels are within normal range.'}"
            )
        elif any(w in q for w in ["torque", "rpm", "speed", "rotation"]):
            return (
                f"⚙️ **Mechanical Readings:**\n"
                f"- Rotational Speed: **{rpm} RPM**\n"
                f"- Torque: **{torque:.1f} Nm**\n\n"
                f"{'⚠️ High torque detected — check for mechanical overload.' if torque > _thr['torque_high_Nm'] else '✅ Mechanical readings are within normal range.'}"
            )
        elif any(w in q for w in ["tool", "wear"]):
            return (
                f"🔧 **Tool Wear: {tool_wear} min**\n\n"
                + ("⚠️ Tool wear is high. Replacement is recommended before the next production cycle." if tool_wear > _thr["tool_wear_high_min"]
                   else "✅ Tool wear is within acceptable limits. Continue monitoring.")
            )

        # ── Fallback ─────────────────────────────────────────────────────────
        else:
            return (
                "I can answer questions about:\n"
                "- **Failure risk** — *'Why is the machine at risk?'*\n"
                "- **Maintenance** — *'What maintenance should I do?'*\n"
                "- **Sustainability** — *'How much waste is avoided?'*\n"
                "- **Machine health** — *'What is the machine health?'*\n"
                "- **Sensors** — *'What is the temperature / torque / tool wear?'*"
            )

    question = st.text_input(
        "Ask about the current machine",
        placeholder="e.g. Why is the machine at risk? What maintenance should I do?",
    )
    if question:
        st.markdown(_ai_response(question))

    st.subheader("🧩 IBM Bob Integration")
    st.write("IBM Bob can act as the natural-language explanation layer for this prototype: explain predictions, summarize machine health, and generate resource-conscious maintenance recommendations.")
    st.code("Analyze the machine sensor values, explain the failure risk in simple language, recommend preventive maintenance, and suggest actions that reduce unnecessary material waste and resource consumption.")

st.divider()
st.caption("AI-Powered Sustainable Predictive Maintenance | AI for Impact → AI for Climate Action & Sustainability")
