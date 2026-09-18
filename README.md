# ð± AI-Powered Sustainable Predictive Maintenance System

## Hackathon Track
**AI for Impact â AI for Climate Action & Sustainability**

## ð Overview

The **AI-Powered Sustainable Predictive Maintenance System** extends an industrial AI predictive-maintenance solution with a sustainability-focused decision-support layer.

The system uses the existing **AI4I 2020 Predictive Maintenance Dataset** and a trained **Random Forest Classifier** to predict whether a machine is likely to fail. The enhanced application then connects that prediction to preventive maintenance and sustainability indicators such as potential downtime avoided, estimated material waste avoided, operational efficiency, and a sustainability score.

The goal is to move from **failure detection** to **responsible, condition-based maintenance** that can help reduce avoidable resource consumption and operational waste.

## ð¯ Problem

Unexpected industrial machine failures can cause downtime, emergency repairs, premature replacement of components, and unnecessary consumption of materials and resources. A predictive system can identify risk earlier so maintenance can be planned before severe failure occurs.

## ð¡ Proposed Solution

**IoT/Sensor Inputs â Random Forest Failure Prediction â Machine Health â Preventive Maintenance Recommendation â Sustainability Analysis â Interactive Dashboard â AI Explanation Layer**

## ð Features

#NAME?
- Random Forest model with existing trained model files
- Failure probability
- Machine health score
- Preventive maintenance recommendation
- Estimated material waste avoided
- Potential downtime avoided
- Operational efficiency indicator
- Sustainability score
- Sensor and risk summary dashboard
- AI sustainability assistant
- IBM Bob integration point for natural-language explanations and recommendations

## ð Input Parameters

- Machine Type
- Air Temperature (K)
- Process Temperature (K)
- Rotational Speed (RPM)
- Torque (Nm)
- Tool Wear (Minutes)

## ð Output

- Machine Status: Healthy / Failure Likely
- Failure Probability
- Machine Health
- Maintenance Recommendation
- Estimated Material Waste Avoided
- Potential Downtime Avoided
- Operational Efficiency
- Sustainability Score

## ð ï¸ Technology Stack

#NAME?
#NAME?
#NAME?
#NAME?
#NAME?
#NAME?
- Matplotlib (notebook/analysis)
- AI4I 2020 Predictive Maintenance Dataset

## ð¤ Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Existing reported accuracy:** 98.4%
- **Model file:** `model/predictive_model.pkl`
- **Encoder:** `model/type_encoder.pkl`

## â»ï¸ Sustainability Approach

The sustainability layer links predictive maintenance with resource-conscious decisions:

1. Predict machine failure risk early.
2. Encourage preventive rather than reactive maintenance.
3. Reduce avoidable emergency downtime.
4. Avoid unnecessary component replacement where condition monitoring indicates it is not required.
5. Track prototype indicators for waste avoided, downtime avoided, efficiency, and sustainability.

> **Note:** Sustainability quantities are demonstration estimates. For real industrial deployment, they should be replaced with measured plant-specific energy, material, replacement, and downtime data.

## ð§© IBM Bob Integration

IBM Bob can be used as the conversational explanation layer. Example prompt:

> Analyze the machine sensor values, explain the failure risk in simple language, recommend preventive maintenance, and suggest actions that reduce unnecessary material waste and resource consumption.

## ð Project Structure

```text
AI-Predictive-Maintenance/
â
âââ app/
â   âââ app.py
âââ dataset/
â   âââ ai4i2020.csv
âââ model/
â   âââ predictive_model.pkl
â   âââ type_encoder.pkl
âââ notebooks/
â   âââ Predictive_Maintenance.ipynb
âââ images/
âââ Complete_AI_Predictive_Maintenance_Handbook.docx
âââ main.py
âââ README.md
âââ requirements.txt
```

## â¶ï¸ How to Run

```bash
pip install -r requirements.txt
python -m streamlit run app/app.py
```

## ð® Future Enhancements

#NAME?
- Live industrial dashboard
- Actual energy and material consumption tracking
- Historical maintenance records
- Explainable AI and feature importance
#NAME?
- Cloud deployment
- IBM Bob/API integration where supported
- Multilingual sustainability recommendations

## ð¨âð» Developer

**B.J. Navadeep**  
B.Tech - Electronics and Communication Engineering  
AI & Embedded Systems Enthusiast
![Uploading image.png…]()
