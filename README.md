# ðŸŒ± AI-Powered Sustainable Predictive Maintenance System

## Hackathon Track
**AI for Impact â†’ AI for Climate Action & Sustainability**

---

## ðŸ“Œ Overview

The **AI-Powered Sustainable Predictive Maintenance System** is an industrial AI solution that combines machine failure prediction with a comprehensive sustainability-focused decision-support layer.

The system uses the **AI4I 2020 Predictive Maintenance Dataset** and a trained **Random Forest Classifier** to predict machine failure risk. It then connects that prediction to a full suite of sustainability, explainability, and monitoring features â€” including carbon footprint estimation, SHAP-based AI explanations, a Remaining Useful Life (RUL) estimator, real-time sensor simulation, sustainability badges, industry benchmark comparison, waste recycling guidance, and a **live IBM Bob AI assistant powered by IBM watsonx.ai**.

The goal is to move from **failure detection** to **responsible, condition-based maintenance** that reduces avoidable resource consumption, operational waste, and carbon emissions.

---

## ðŸŽ¯ Problem

Unexpected industrial machine failures cause downtime, emergency repairs, premature component replacement, and unnecessary consumption of materials and energy. A predictive system identifies risk early so maintenance can be planned â€” avoiding the environmental and financial cost of reactive repairs.

---

## ðŸ’¡ Solution Architecture

```
Industrial Machine / IoT Sensors
          |
          v
   Sensor Input Layer  â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
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
       /    |    |    |    \
      v     v    v    v     v
   SHAP  Badges Trend Industry  Waste
  Chart  System Chart Benchmark Guidance
               |
               v
    ðŸ¤– IBM Bob (IBM watsonx.ai â€” Live AI)
```

---

## ðŸš€ Features

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

### ðŸŒ Carbon Footprint Estimator
- Energy COâ‚‚ avoided (based on machine power & grid carbon intensity)
- Emergency repair logistics COâ‚‚ avoided
- Total COâ‚‚ avoided (kg) with visual progress bar
- Fully configurable via `config.yaml`

### ðŸ… Sustainability Badge System
- **Platinum** â€” exceptional sustainability performance (â‰¥90)
- **Gold** â€” strong performance (â‰¥75)
- **Silver** â€” acceptable performance (â‰¥50)
- **Needs Improvement** â€” maintenance action required (<50)

### â³ Remaining Useful Life (RUL) Estimator
- Tool wear remaining (min)
- Estimated hours of tool life left
- Tool life percentage with color-coded progress bar
- Configurable max tool life and wear rate in `config.yaml`

### ðŸ” SHAP Explainability
#NAME?
- Top driver sentence (most influential sensor for this prediction)
- Clear "increases risk / reduces risk" indicators for each feature

### â±ï¸ Real-Time Simulation Mode
- Toggle live monitoring mode from the sidebar
- Tool wear auto-increments each tick (configurable interval & step)
- Dashboard refreshes automatically â€” simulates real IoT sensor degradation

### ðŸ“ˆ Analysis History & Trend Charts
- Session history persisted across analysis runs
- Tab 1: Failure Probability vs Machine Health trend
- Tab 2: Sustainability Score vs Operational Efficiency trend
- Clear history button

### ðŸ“¥ Downloadable Reports
- Download full analysis report as **CSV** or **TXT**

### ðŸ† Model Feature Importance Chart
- Sidebar horizontal bar chart showing which sensors matter most
- Importance scores pulled directly from the trained Random Forest model

### ðŸ“Š Industry Sustainability Benchmark
- Compares your machine's sustainability score against the industry average (65/100)
- Compares COâ‚‚ avoided against the industry average per maintenance event
- Visual bar chart comparison with delta indicators
- Benchmarks configurable in `config.yaml` â†’ `watsonx` section

### â™»ï¸ Waste Disposal & Recycling Guidance
#NAME?
#NAME?
- Specific recycling/disposal action for each waste type
- COâ‚‚ saved estimate for recycling the worn tool vs landfilling

### ðŸ¤– IBM Bob â€” Live AI Assistant (IBM watsonx.ai)
- Powered by **Meta Llama 3.3 70B** via IBM watsonx.ai (eu-gb London region)
#NAME?
- Enter credentials once in the UI (no terminal / env vars needed)
- Graceful rule-based fallback when credentials are not configured
- Answers any free-text question about the machine, maintenance, sustainability, or carbon impact

---

## ðŸ“Š Input Parameters

| Parameter | Description |
|---|---|
| Machine Type | L / M / H (Low / Medium / High) |
| Air Temperature (K) | Ambient air temperature |
| Process Temperature (K) | Machine process temperature |
| Rotational Speed (RPM) | Spindle / motor rotational speed |
| Torque (Nm) | Machine torque |
| Tool Wear (min) | Cumulative tool wear time |

---

## ðŸ“ˆ Output

| Output | Description |
|---|---|
| Machine Status | Healthy / Failure Likely |
| Failure Probability | 0â€“100% |
| Machine Health | 0â€“100% |
| Maintenance Recommendation | Context-aware risk-tiered advice |
| Operational Efficiency | 0â€“100% |
| Sustainability Score | 0â€“100 |
| Material Waste Avoided | kg (estimated) |
| Downtime Avoided | hrs (estimated) |
| Carbon COâ‚‚ Avoided | kg COâ‚‚ (estimated) |
| Sustainability Badge | Platinum / Gold / Silver / Needs Improvement |
| RUL | Tool wear remaining, hours left, % tool life |
| SHAP Explanation | Per-feature contribution chart |
| Industry Benchmark | Your score vs industry average (sustainability + COâ‚‚) |
| Waste Guidance | Recycling/disposal instructions for maintenance waste |
| IBM Bob Response | Live AI explanation and recommendations |

---

## ðŸ› ï¸ Technology Stack

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
| Requests | IBM watsonx.ai API calls |
| Docker | Containerised deployment |
| AI4I 2020 Dataset | Training data |
| **IBM watsonx.ai** | **Live AI responses (Llama 3.3 70B, eu-gb)** |

---

## ðŸ¤– Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Reported Accuracy:** 98.4%
- **Model file:** `model/predictive_model.pkl`
- **Encoder:** `model/type_encoder.pkl`
- **Training notebook:** `notebooks/Predictive_Maintenance.ipynb`

---

## ðŸ§© IBM Bob Integration (Live)

IBM Bob is integrated via **IBM watsonx.ai REST API** using the **Meta Llama 3.3 70B Instruct** model on the `eu-gb` (London) endpoint.

### How it works
1. After clicking **Analyze**, scroll to the **ðŸ¤– IBM Bob** section
2. Open the **ðŸ”‘ IBM Bob Credentials** expander
3. Paste your **IBM Cloud API Key** and **watsonx.ai Project ID**
4. Click **ðŸ’¾ Save Credentials**
5. Ask any question â€” IBM Bob responds with live, context-aware AI answers

### Getting credentials
| Credential | Where to get it |
|---|---|
| IBM Cloud API Key | [cloud.ibm.com/iam/apikeys](https://cloud.ibm.com/iam/apikeys) â†’ Create |
| watsonx.ai Project ID | [eu-gb.dataplatform.cloud.ibm.com](https://eu-gb.dataplatform.cloud.ibm.com) â†’ your project â†’ Manage tab |

### What IBM Bob knows per session
Every question is answered with full awareness of the current machine state:
- Live sensor readings (temperature, RPM, torque, tool wear)
- Failure probability and machine health score
- Sustainability score and COâ‚‚ avoided
- Risk level and RUL remaining

> Credentials are stored in browser session state only â€” never persisted to disk or sent anywhere except IBM's IAM and watsonx.ai endpoints.

---

## âš™ï¸ Configuration

All thresholds, sustainability parameters, carbon factors, RUL values, badge thresholds, simulation settings, and watsonx.ai settings live in **[`config.yaml`](config.yaml)** â€” no code changes needed to calibrate to real plant data.

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
| `watsonx` | API endpoint, model ID, benchmark values |

> **Note:** Sustainability and carbon quantities are demonstration estimates. For production, replace constants in `config.yaml` with measured plant-specific energy, material, replacement, and downtime data.

---

## â™»ï¸ Sustainability Approach

1. Predict machine failure risk early using sensor data.
2. Encourage **preventive** rather than **reactive** maintenance.
3. Reduce avoidable emergency downtime.
4. Avoid unnecessary component replacement where condition monitoring shows it is not required.
5. Estimate and track carbon emissions avoided by acting early.
6. Reward high-performing machines with sustainability badges.
7. Provide RUL estimates to optimize replacement timing.
8. Guide responsible waste disposal and recycling when maintenance is performed.
9. Benchmark performance against industry averages to encourage community-level sustainability improvement.

---

## ðŸ“ Project Structure

```text
AI-Predictive-Maintenance/
â”‚
â”œâ”€â”€ app/
â”‚   â””â”€â”€ app.py                  # Full Streamlit dashboard (all features)
â”œâ”€â”€ dataset/
â”‚   â””â”€â”€ ai4i2020.csv            # AI4I 2020 Predictive Maintenance Dataset
â”œâ”€â”€ model/
â”‚   â”œâ”€â”€ predictive_model.pkl    # Trained Random Forest model
â”‚   â””â”€â”€ type_encoder.pkl        # Label encoder for machine type
â”œâ”€â”€ notebooks/
â”‚   â””â”€â”€ Predictive_Maintenance.ipynb  # Training & analysis notebook
â”œâ”€â”€ images/                     # Screenshots / assets
â”œâ”€â”€ .streamlit/                 # Streamlit theme config
â”œâ”€â”€ config.yaml                 # All parameters, thresholds & watsonx settings
â”œâ”€â”€ .env.example                # Template for IBM watsonx.ai credentials
â”œâ”€â”€ Dockerfile                  # Docker container definition
â”œâ”€â”€ docker-compose.yml          # Docker Compose for easy deployment
â”œâ”€â”€ Complete_AI_Predictive_Maintenance_Handbook.docx
â”œâ”€â”€ SUSTAINABILITY_ARCHITECTURE.md
â”œâ”€â”€ main.py
â”œâ”€â”€ README.md
â””â”€â”€ requirements.txt
```

---

## â–¶ï¸ How to Run

### Local (Python) â€” Recommended

```bash
# Step 1: Create and activate virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the app
python -m streamlit run app/app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

### Docker

```bash
docker build -t ai-predictive-maintenance .
docker run -p 8501:8501 ai-predictive-maintenance
```

### Docker Compose

```bash
docker-compose up
```

> **First run:** If model files are missing, open and run `notebooks/Predictive_Maintenance.ipynb` to train and save the model.

---

## ðŸ”‘ Enabling Live IBM Bob (Optional)

IBM Bob works with live AI responses when you provide watsonx.ai credentials directly in the app UI â€” no terminal setup needed.

1. Run the app and click **Analyze Machine & Sustainability**
2. Scroll to **ðŸ¤– IBM Bob** â†’ open the **ðŸ”‘ IBM Bob Credentials** expander
3. Paste your **IBM Cloud API Key** and **watsonx.ai Project ID**
4. Click **ðŸ’¾ Save Credentials**

Without credentials, the app is fully functional with a rule-based fallback assistant.

See [`.env.example`](.env.example) for instructions on obtaining credentials.

---

## ðŸ”® Future Enhancements

- Real IoT sensor integration (MQTT / OPC-UA)
- Live industrial dashboard with WebSocket streaming
- Actual energy and material consumption tracking from plant systems
- Historical maintenance records and audit trail
#NAME?
- Cloud deployment (AWS / Azure / IBM Cloud)
- IBM Watson IoT Platform integration
- Multilingual sustainability recommendations via IBM Bob
#NAME?

---
<img width="109" height="10499" alt="image" src="https://github.com/user-attachments/assets/8a2e1b82-b7b8-42d4-a7cd-cda804286965" />
