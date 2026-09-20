#  AI-Powered Sustainable Predictive Maintenance System

## Hackathon Track
**AI for Impact → AI for Climate Action & Sustainability**

---

##  Overview

The **AI-Powered Sustainable Predictive Maintenance System** is an industrial AI solution that combines machine failure prediction with a comprehensive sustainability-focused decision-support layer.

The system uses the **AI4I 2020 Predictive Maintenance Dataset** and a trained **Random Forest Classifier** to predict machine failure risk. It then connects that prediction to a full suite of sustainability, explainability, and monitoring features — including carbon footprint estimation, SHAP-based AI explanations, a Remaining Useful Life (RUL) estimator, real-time sensor simulation, sustainability badges, and a built-in AI assistant.

The goal is to move from **failure detection** to **responsible, condition-based maintenance** that reduces avoidable resource consumption, operational waste, and carbon emissions.

---

##  Problem

Unexpected industrial machine failures cause downtime, emergency repairs, premature component replacement, and unnecessary consumption of materials and energy. A predictive system identifies risk early so maintenance can be planned — avoiding the environmental and financial cost of reactive repairs.

---

##  Solution Architecture

```
Industrial Machine / IoT Sensors
          |
          v
   Sensor Input Layer  ──────────────────────────────┐
          |                                           |
          v                                    config.yaml
   Data Preprocessing                         (all thresholds &
          |                                    parameters)
          v
 Random Forest Classifier
          |
          v
    Failure Risk Score
       /         \
      v           v
 Machine Health   Maintenance Recommendation
       \         /
        v       v
     Sustainability Engine
        |       |       |       |
        v       v       v       v
    Waste   Downtime  Efficiency  Carbon
   Avoided  Avoided   Score     Footprint
        \       |       |       /
          \     |       |     /
            v   v       v   v
       Sustainability Score + RUL
               |
               v
        Streamlit Dashboard
       /         |        \
      v          v         v
   SHAP        Badges    Trend
 Explanation  System    Charts
               |
               v
      IBM Bob Explanation Layer
```

---

##  Features

### Core Prediction
- **Random Forest** machine failure prediction (98.4% accuracy)
- Failure probability score
- Machine health score
- Risk-tiered maintenance recommendation (Low / Moderate / High)

### Sustainability Engine
- Estimated material waste avoided (kg)
- Potential downtime avoided (hrs)
- Operational efficiency score (%)
- Sustainability score (/100)

###  Carbon Footprint Estimator *(New)*
- Energy CO₂ avoided (based on machine power & grid carbon intensity)
- Emergency repair logistics CO₂ avoided
- Total CO₂ avoided (kg) with visual progress bar
- Fully configurable via `config.yaml`

###  Sustainability Badge System *(New)*
- **Platinum** — exceptional sustainability performance (≥90)
- **Gold** — strong performance (≥75)
- **Silver** — acceptable performance (≥50)
- **Needs Improvement** — maintenance action required (<50)

###  Remaining Useful Life (RUL) Estimator *(New)*
- Tool wear remaining (min)
- Estimated hours of tool life left
- Tool life percentage with color-coded progress bar
- Configurable max tool life and wear rate in `config.yaml`

###  SHAP Explainability *(New)*
- Per-prediction SHAP waterfall bar chart
- Top driver sentence (most influential sensor for this prediction)
- Clear "increases risk / reduces risk" indicators for each feature

### ⏱ Real-Time Simulation Mode *(New)*
- Toggle live monitoring mode from the sidebar
- Tool wear auto-increments each tick (configurable interval & step)
- Dashboard refreshes automatically — simulates real IoT sensor degradation

###  Analysis History & Trend Charts *(New)*
- Session history persisted across analysis runs
- Tab 1: Failure Probability vs Machine Health trend
- Tab 2: Sustainability Score vs Operational Efficiency trend
- Clear history button

###  Downloadable Reports *(New)*
- Download full analysis report as **CSV** or **TXT**

###  AI Sustainability Assistant *(New)*
- Context-aware natural-language assistant
- Answers questions about failure risk, maintenance actions, sustainability impact, machine health, and individual sensor readings
- Fully driven by actual computed metrics for the current analysis run

###  Model Feature Importance Chart *(New)*
- Sidebar horizontal bar chart showing which sensors matter most
- Importance scores pulled directly from the trained Random Forest model

---

##  Input Parameters

| Parameter | Description |
|---|---|
| Machine Type | L / M / H (Low / Medium / High) |
| Air Temperature (K) | Ambient air temperature |
| Process Temperature (K) | Machine process temperature |
| Rotational Speed (RPM) | Spindle / motor rotational speed |
| Torque (Nm) | Machine torque |
| Tool Wear (min) | Cumulative tool wear time |

---

##  Output

| Output | Description |
|---|---|
| Machine Status | Healthy / Failure Likely |
| Failure Probability | 0–100% |
| Machine Health | 0–100% |
| Maintenance Recommendation | Context-aware risk-tiered advice |
| Operational Efficiency | 0–100% |
| Sustainability Score | 0–100 |
| Material Waste Avoided | kg (estimated) |
| Downtime Avoided | hrs (estimated) |
| Carbon CO₂ Avoided | kg CO₂ (estimated) |
| Sustainability Badge | Platinum / Gold / Silver / Needs Improvement |
| RUL | Tool wear remaining, hours left, % tool life |
| SHAP Explanation | Per-feature contribution chart |

---

##  Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Core language |
| Streamlit | Interactive web dashboard |
| Scikit-learn | Random Forest model |
| SHAP | Model explainability |
| Pandas / NumPy | Data processing |
| Matplotlib | Feature importance & SHAP charts |
| Joblib | Model serialisation |
| PyYAML | Configuration management |
| Docker | Containerised deployment |
| AI4I 2020 Dataset | Training data |

---

##  Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Reported Accuracy:** 98.4%
- **Model file:** `model/predictive_model.pkl`
- **Encoder:** `model/type_encoder.pkl`
- **Training notebook:** `notebooks/Predictive_Maintenance.ipynb`

---

##  Configuration

All thresholds, sustainability parameters, carbon factors, RUL values, badge thresholds, and simulation settings live in **[`config.yaml`](config.yaml)** — no code changes needed to calibrate to real plant data.

Key sections:

| Section | What it controls |
|---|---|
| `sensor_defaults` | Default UI input values |
| `thresholds` | Risk bands, temp/torque/wear alert limits |
| `sustainability` | Efficiency formula, waste/downtime scaling |
| `carbon` | Grid carbon intensity, machine power (kW) |
| `rul` | Max tool life, average wear rate |
| `badges` | Platinum/Gold/Silver score thresholds |
| `card_thresholds` | Dashboard card color bands |
| `realtime` | Wear increment step, tick interval (s) |

> **Note:** Sustainability and carbon quantities are demonstration estimates. For production, replace constants in `config.yaml` with measured plant-specific energy, material, replacement, and downtime data.

---

##  Sustainability Approach

1. Predict machine failure risk early using sensor data.
2. Encourage **preventive** rather than **reactive** maintenance.
3. Reduce avoidable emergency downtime.
4. Avoid unnecessary component replacement where condition monitoring shows it is not required.
5. Estimate and track carbon emissions avoided by acting early.
6. Reward high-performing machines with sustainability badges.
7. Provide RUL estimates to optimize replacement timing.

---

##  IBM Bob Integration

IBM Bob serves as the conversational explanation and recommendation layer. Example prompt:

> Analyze the machine sensor values, explain the failure risk in simple language, recommend preventive maintenance, and suggest actions that reduce unnecessary material waste and resource consumption.

---

##  Project Structure

```text
AI-Predictive-Maintenance/
│
├── app/
│   └── app.py                  # Full Streamlit dashboard (all features)
├── dataset/
│   └── ai4i2020.csv            # AI4I 2020 Predictive Maintenance Dataset
├── model/
│   ├── predictive_model.pkl    # Trained Random Forest model
│   └── type_encoder.pkl        # Label encoder for machine type
├── notebooks/
│   └── Predictive_Maintenance.ipynb  # Training & analysis notebook
├── images/                     # Screenshots / assets
├── .streamlit/                 # Streamlit theme config
├── config.yaml                 # All parameters & thresholds (calibrate here)
├── Dockerfile                  # Docker container definition
├── docker-compose.yml          # Docker Compose for easy deployment
├── Complete_AI_Predictive_Maintenance_Handbook.docx
├── SUSTAINABILITY_ARCHITECTURE.md
├── main.py
├── README.md
└── requirements.txt
```

---

##  How to Run

### Local (Python)

```bash
pip install -r requirements.txt
python -m streamlit run app/app.py
```

### Docker

```bash
docker build -t ai-predictive-maintenance .
docker run -p 8501:8501 ai-predictive-maintenance
```

### Docker Compose

```bash
docker-compose up
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

> **First run:** If model files are missing, open and run `notebooks/Predictive_Maintenance.ipynb` to train and save the model.

---

##  Future Enhancements

- Real IoT sensor integration (MQTT / OPC-UA)
- Live industrial dashboard with WebSocket streaming
- Actual energy and material consumption tracking from plant systems
- Historical maintenance records and audit trail
- Multi-machine fleet monitoring
- Cloud deployment (AWS / Azure / IBM Cloud)
- IBM Watson IoT Platform integration
- Multilingual sustainability recommendations
- Role-based access control for plant operators vs. managers

---

##  Developer

**B.J. Navadeep**
B.Tech — Electronics and Communication Engineering
AI & Embedded Systems Enthusiast
