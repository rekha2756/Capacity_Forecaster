# 🚀 IM-02 AI Capacity Forecaster

An AI-powered capacity forecasting dashboard that predicts future CPU, Memory, and Disk utilization trends using Time Series Forecasting and Anomaly Detection techniques.

The application enables proactive infrastructure monitoring by forecasting future resource usage, detecting anomalies, and identifying capacity risks before they impact system performance.

---

# 📌 Problem Statement

Organizations need to forecast future capacity utilization and identify anomalies before resource bottlenecks occur.

This solution predicts future utilization trends using AI forecasting techniques and highlights abnormal utilization patterns to support proactive infrastructure planning.

---

# ✨ Features

## 📊 AI Forecasting Engine

Supports multiple forecasting models:

- Prophet Forecasting
- ARIMA Forecasting

Forecasts:

- CPU Usage
- Memory Usage
- Disk Usage

---

## 🔍 Natural Language Query Interface

Users can ask:

- When will CPU usage hit 80%?
- Forecast Memory utilization
- Predict Disk usage growth

---

## 🚨 Anomaly Detection

Detects abnormal patterns using statistical logic:

- Threshold breach detection
- Forecast anomaly detection
- Risk classification

---

## 📈 Interactive Dashboard

Includes:

- KPI cards
- Forecast charts
- AI insights
- Risk indicators
- Dataset preview
- Summary tables

---

## 📥 Export Feature

Download forecast results as CSV for reporting and analysis.

---

# ⭐ Business Value

- Predict future capacity shortages
- Reduce downtime risks
- Improve infrastructure planning
- Detect anomalies early
- Enable proactive decision-making
- Optimize resource usage

---

# 📸 Screenshots

## 📊 Dashboard Overview
![Dashboard](screenshots/Prophet_dashboard.png)

---

## 📈 Prophet Forecast Graph
![Prophet Graph](screenshots/Prophet_graph.png)

---

## 📊 Prophet Output
![Prophet Output](screenshots/Prophet_output.png)

---

## 📉 ARIMA Forecast Graph
![ARIMA Graph](screenshots/ARIMA_graph.png)

---

## 📊 ARIMA Output
![ARIMA Output](screenshots/ARIMA_output.png)

---

# 🏗 Architecture

```text
CSV Input
   ↓
Data Validation
   ↓
Forecast Engine (Prophet / ARIMA)
   ↓
Anomaly Detection
   ↓
Risk Assessment
   ↓
Streamlit Dashboard
   ↓
Forecast Export
🛠 Technology Stack
Layer	Technology
Frontend	Streamlit
Forecasting	Prophet
Statistical Model	ARIMA
Data Processing	Pandas
Numerical Ops	NumPy
Visualization	Matplotlib
Testing	Pytest
Language	Python
📂 Project Structure
IM-02-Capacity-Forecaster/

├── app.py
├── requirements.txt
├── README.md
├── prompts.md
├── ai_usage_note.md
│
├── data/
│   └── metrics.csv
│
├── tests/
│   └── test_app.py
│
├── screenshots/
│   ├── Prophet_dashboard.png
│   ├── Prophet_graph.png
│   ├── Prophet_output.png
│   ├── ARIMA_graph.png
│   ├── ARIMA_output.png
│
├── resumes/
│   ├── Member1.pdf
│   ├── Member2.pdf
│   ├── Member3.pdf
│   ├── Member4.pdf
│
└── outputs/
    └── forecast.csv
⚙ Installation
git clone https://github.com/rekha2756/Capacity_Forecaster.git
cd Capacity_Forecaster
pip install -r requirements.txt
streamlit run app.py
📄 Input Format
Column	Description
Date	Date of metric
CPU	CPU usage %
Memory	Memory usage %
Disk	Disk usage %
📊 Sample Output
ds	yhat	anomaly
2025-05-01	78.4	False
2025-05-02	82.1	True
🚀 Workflow
Upload CSV
Select model (Prophet / ARIMA)
Set threshold
Run forecast
View insights + download report
🎯 Risk Levels
Level	Meaning
🟢 Low	Safe usage
🟠 Medium	Approaching threshold
🔴 High	Exceeds threshold
🤖 AI Capabilities
Time Series Forecasting
Prophet & ARIMA Models
Capacity Planning
Anomaly Detection
Predictive Analytics
Risk Analysis
🧪 Testing
pytest tests/test_app.py

Test coverage:

Forecast validation
Threshold checks
Anomaly detection
Output verification
📹 Demo Video

https://www.loom.com/share/63b136753290416caf0f323d986444c8

🔗 GitHub Repository

https://github.com/rekha2756/Capacity_Forecaster

👥 Team Information

Team Name: Team-5

Members:

P.Sreeja
G.Rekha
C.Sindhu
K.Varshitha
📦 Deliverables
Source Code
README
AI Usage Note
Prompt Documentation
Test Cases
Sample Data
Screenshots
Resume PDFs
Demo Video
🤝 AI Usage Disclosure

AI tools were used for:

UI generation
Forecasting logic
ARIMA integration
Anomaly detection
Testing
Documentation

All outputs were reviewed and validated by the team.

📜 License

This project is for academic and educational purposes only.
