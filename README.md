# AI-Powered Sustainable Predictive Maintenance System

## Hackathon Track

**AI for Impact -> AI for Climate Action & Sustainability**

---

## Overview

The **AI-Powered Sustainable Predictive Maintenance System** is an industrial AI solution that combines machine failure prediction with a comprehensive sustainability-focused decision-support layer.

The system uses the **AI4I 2020 Predictive Maintenance Dataset** and a trained **Random Forest Classifier** to predict machine failure risk. It then connects that prediction to a full suite of sustainability, explainability, and monitoring features, including carbon footprint estimation, SHAP-based AI explanations, a Remaining Useful Life (RUL) estimator, real-time sensor simulation, sustainability badges, industry benchmark comparison, waste recycling guidance, and a **live IBM Bob AI assistant powered by IBM watsonx.ai**.

The goal is to move from **failure detection** to **responsible, condition-based maintenance** that reduces avoidable resource consumption, operational waste, and carbon emissions.

---

## Problem

Unexpected industrial machine failures cause downtime, emergency repairs, premature component replacement, and unnecessary consumption of materials and energy. A predictive system identifies risk early so maintenance can be planned, avoiding the environmental and financial cost of reactive repairs.

---

## Solution Architecture

```text
Industrial Machine / IoT Sensors
             |
             v
      Sensor Input Layer
             |
             |------------------ config.yaml
             |                  (all thresholds &
             |                   parameters)
             v
      Data Preprocessing
             |
             v
    Random Forest Classifier
             |
             v
      Failure Risk Score
          /          \
         v            v
Machine Health    Maintenance Recommendation
         \            /
          \          /
             v    v
       Sustainability Engine
          |      |      |      |
          v      v      v      v
        Waste  Downtime Efficiency Carbon
        Avoided Avoided   Score   Footprint
          \       |        |       /
           \      |        |      /
              v   v        v   v
         Sustainability Score + RUL
                    |
                    v
          Streamlit Dashboard
         /    |     |     |     \
        v     v     v     v      v
      SHAP  Badges Trend Industry Waste
      Chart System Chart Benchmark Guidance
                    |
                    v
          IBM Bob
     (IBM watsonx.ai - Live AI)
```

---

## Features

### Core Prediction

* **Random Forest** machine failure prediction (98.4% accuracy)
* Failure probability score
* Machine health score
* Risk-tiered maintenance recommendation (Low / Moderate / High)

### Sustainability Engine

* Estimated material waste avoided (kg)
* Potential downtime avoided (hrs)
* Operational efficiency score (%)
* Sustainability score (/100)

### Carbon Footprint Estimator

* Energy CO2 avoided based on machine power and grid carbon intensity
* Emergency repair logistics CO2 avoided
* Total CO2 avoided (kg) with visual progress bar
* Fully configurable via `config.yaml`

### Sustainability Badge System

* **Platinum** - exceptional sustainability performance (>=90)
* **Gold** - strong performance (>=75)
* **Silver** - acceptable performance (>=50)
* **Needs Improvement** - maintenance action required (<50)

### Remaining Useful Life (RUL) Estimator

* Tool wear remaining (min)
* Estimated hours of tool life left
* Tool life percentage with progress bar
* Configurable maximum tool life and wear rate in `config.yaml`

### SHAP Explainability

* SHAP-based explanation of model predictions
* Top driver sentence showing the most influential sensor for the prediction
* Clear "increases risk / reduces risk" indicators for each feature

### Real-Time Simulation Mode

* Toggle live monitoring mode from the sidebar
* Tool wear automatically increments at each configured interval
* Dashboard refreshes automatically
* Simulates real IoT sensor degradation

### Analysis History and Trend Charts

* Session history persisted across analysis runs
* Tab 1: Failure Probability vs Machine Health trend
* Tab 2: Sustainability Score vs Operational Efficiency trend
* Clear history button

### Downloadable Reports

* Download full analysis reports as **CSV** or **TXT**

### Model Feature Importance Chart

* Sidebar horizontal bar chart showing which sensors matter most
* Importance scores are pulled directly from the trained Random Forest model

### Industry Sustainability Benchmark

* Compares the machine's sustainability score against the industry average (65/100)
* Compares CO2 avoided against the industry average per maintenance event
* Visual bar chart comparison with delta indicators
* Benchmarks configurable in `config.yaml` under the `watsonx` section

### Waste Disposal and Recycling Guidance

* Waste classification and recycling guidance
* Specific recycling/disposal action for each waste type
* CO2 saved estimate for recycling the worn tool compared with landfilling

### IBM Bob - Live AI Assistant

* Powered by **Meta Llama 3.3 70B** via IBM watsonx.ai (eu-gb London region)
* Provides context-aware responses based on the current machine state
* Enter credentials once in the UI with no terminal or environment-variable setup required
* Graceful rule-based fallback when credentials are not configured
* Answers free-text questions about the machine, maintenance, sustainability, and carbon impact

---

## Input Parameters

| Parameter               | Description                      |
| ----------------------- | -------------------------------- |
| Machine Type            | L / M / H (Low / Medium / High)  |
| Air Temperature (K)     | Ambient air temperature          |
| Process Temperature (K) | Machine process temperature      |
| Rotational Speed (RPM)  | Spindle / motor rotational speed |
| Torque (Nm)             | Machine torque                   |
| Tool Wear (min)         | Cumulative tool wear time        |

---

## Output

| Output                     | Description                                           |
| -------------------------- | ----------------------------------------------------- |
| Machine Status             | Healthy / Failure Likely                              |
| Failure Probability        | 0-100%                                                |
| Machine Health             | 0-100%                                                |
| Maintenance Recommendation | Context-aware risk-tiered advice                      |
| Operational Efficiency     | 0-100%                                                |
| Sustainability Score       | 0-100                                                 |
| Material Waste Avoided     | kg (estimated)                                        |
| Downtime Avoided           | hrs (estimated)                                       |
| Carbon CO2 Avoided         | kg CO2 (estimated)                                    |
| Sustainability Badge       | Platinum / Gold / Silver / Needs Improvement          |
| RUL                        | Tool wear remaining, hours left, % tool life          |
| SHAP Explanation           | Per-feature contribution chart                        |
| Industry Benchmark         | Your score vs industry average (sustainability + CO2) |
| Waste Guidance             | Recycling/disposal instructions for maintenance waste |
| IBM Bob Response           | Live AI explanation and recommendations               |

---

## Technology Stack

| Technology         | Purpose                                      |
| ------------------ | -------------------------------------------- |
| Python 3.11        | Core language                                |
| Streamlit          | Interactive web dashboard                    |
| Scikit-learn       | Random Forest model                          |
| SHAP               | Model explainability                         |
| Pandas / NumPy     | Data processing                              |
| Matplotlib         | Feature importance and SHAP charts           |
| Joblib             | Model serialisation                          |
| PyYAML             | Configuration management                     |
| Requests           | IBM watsonx.ai API calls                     |
| Docker             | Containerised deployment                     |
| AI4I 2020 Dataset  | Training data                                |
| **IBM watsonx.ai** | **Live AI responses (Llama 3.3 70B, eu-gb)** |

---

## Machine Learning Model

* **Algorithm:** Random Forest Classifier
* **Reported Accuracy:** 98.4%
* **Model file:** `model/predictive_model.pkl`
* **Encoder:** `model/type_encoder.pkl`
* **Training notebook:** `notebooks/Predictive_Maintenance.ipynb`

---

## IBM Bob Integration

IBM Bob is integrated via the **IBM watsonx.ai REST API** using the **Meta Llama 3.3 70B Instruct** model on the `eu-gb` (London) endpoint.

### How It Works

1. After clicking **Analyze**, scroll to the **IBM Bob** section.
2. Open the **IBM Bob Credentials** expander.
3. Paste your **IBM Cloud API Key** and **watsonx.ai Project ID**.
4. Click **Save Credentials**.
5. Ask any question. IBM Bob responds with live, context-aware AI answers.

### Getting Credentials

| Credential            | Where to get it                                                  |
| --------------------- | ---------------------------------------------------------------- |
| IBM Cloud API Key     | `cloud.ibm.com/iam/apikeys` -> Create                            |
| watsonx.ai Project ID | `eu-gb.dataplatform.cloud.ibm.com` -> Your project -> Manage tab |

### What IBM Bob Knows Per Session

Every question is answered with awareness of the current machine state:

* Live sensor readings including temperature, RPM, torque, and tool wear
* Failure probability and machine health score
* Sustainability score and CO2 avoided
* Risk level and RUL remaining

> Credentials are stored in browser session state only. They are not persisted to disk or sent anywhere except IBM IAM and watsonx.ai endpoints.

---

## Configuration

All thresholds, sustainability parameters, carbon factors, RUL values, badge thresholds, simulation settings, and watsonx.ai settings are stored in **`config.yaml`**. No code changes are needed to calibrate the system to real plant data.

| Section           | What it controls                                 |
| ----------------- | ------------------------------------------------ |
| `sensor_defaults` | Default UI input values                          |
| `thresholds`      | Risk bands, temperature/torque/wear alert limits |
| `sustainability`  | Efficiency formula, waste/downtime scaling       |
| `carbon`          | Grid carbon intensity, machine power (kW)        |
| `rul`             | Maximum tool life, average wear rate             |
| `badges`          | Platinum/Gold/Silver score thresholds            |
| `card_thresholds` | Dashboard card color bands                       |
| `realtime`        | Wear increment step, tick interval (s)           |
| `watsonx`         | API endpoint, model ID, benchmark values         |

> **Note:** Sustainability and carbon quantities are demonstration estimates. For production use, replace the constants in `config.yaml` with measured plant-specific energy, material, replacement, and downtime data.

---

## Sustainability Approach

1. Predict machine failure risk early using sensor data.
2. Encourage **preventive** rather than **reactive** maintenance.
3. Reduce avoidable emergency downtime.
4. Avoid unnecessary component replacement when condition monitoring shows it is not required.
5. Estimate and track carbon emissions avoided by acting early.
6. Reward high-performing machines with sustainability badges.
7. Provide RUL estimates to optimize replacement timing.
8. Guide responsible waste disposal and recycling when maintenance is performed.
9. Benchmark performance against industry averages to encourage sustainability improvement.

---

## Project Structure

```text
AI-Predictive-Maintenance/
|
+-- app/
|   +-- app.py                    # Full Streamlit dashboard
|
+-- dataset/
|   +-- ai4i2020.csv              # AI4I 2020 Predictive Maintenance Dataset
|
+-- model/
|   +-- predictive_model.pkl      # Trained Random Forest model
|   +-- type_encoder.pkl          # Label encoder for machine type
|
+-- notebooks/
|   +-- Predictive_Maintenance.ipynb   # Training and analysis notebook
|
+-- images/                       # Screenshots / assets
+-- .streamlit/                   # Streamlit theme configuration
+-- config.yaml                   # All parameters, thresholds and watsonx settings
+-- .env.example                  # Template for IBM watsonx.ai credentials
+-- Dockerfile                    # Docker container definition
+-- docker-compose.yml            # Docker Compose configuration
+-- Complete_AI_Predictive_Maintenance_Handbook.docx
+-- SUSTAINABILITY_ARCHITECTURE.md
+-- main.py
+-- README.md
+-- requirements.txt
```

---

## How to Run

### Local Python - Recommended

```bash
# Step 1: Create and activate virtual environment

python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
# source venv/bin/activate


# Step 2: Install dependencies

pip install -r requirements.txt


# Step 3: Run the application

python -m streamlit run app/app.py
```

Then open `http://localhost:8501` in your browser.

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

## Enabling Live IBM Bob

IBM Bob works with live AI responses when you provide watsonx.ai credentials directly in the application UI. No terminal setup is required.

1. Run the application and click **Analyze Machine & Sustainability**.
2. Scroll to **IBM Bob** and open the **IBM Bob Credentials** expander.
3. Paste your **IBM Cloud API Key** and **watsonx.ai Project ID**.
4. Click **Save Credentials**.

Without credentials, the application remains fully functional with a rule-based fallback assistant.

See `.env.example` for instructions on obtaining credentials.

---

## Future Enhancements

* Real IoT sensor integration using MQTT / OPC-UA
* Live industrial dashboard with WebSocket streaming
* Actual energy and material consumption tracking from plant systems
* Historical maintenance records and audit trail
* Cloud deployment on AWS, Azure, or IBM Cloud
* IBM Watson IoT Platform integration
* Multilingual sustainability recommendations via IBM Bob

---
