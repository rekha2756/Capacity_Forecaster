# 🚀 IM-02 AI Capacity Forecaster

An AI-powered capacity forecasting system that predicts future CPU, Memory, and Disk utilization using Prophet and ARIMA models. The application supports natural language queries, anomaly detection, risk analysis, and system health recommendations through an interactive Streamlit dashboard.

---

# 📌 Problem Statement

Infrastructure teams often rely on manual spreadsheet analysis to estimate future resource utilization.

This project automates capacity planning by:

- Forecasting resource consumption trends
- Predicting threshold breaches
- Detecting anomalies
- Providing risk assessment
- Generating AI-driven recommendations

The goal is to help organizations proactively prevent infrastructure bottlenecks and optimize resource planning.

---

# ✨ Key Features

## 📊 Capacity Forecasting

Supports multiple forecasting approaches:

- Prophet Forecasting
- ARIMA Forecasting

Forecasts:

- CPU Utilization
- Memory Utilization
- Disk Utilization

---

## 🤖 Natural Language Query Support

Users can ask questions such as:

- When will CPU hit 80?
- When will Memory hit 90?
- When will Disk hit 95?

The system automatically:

- Detects the metric
- Extracts threshold values
- Runs forecasting
- Returns predicted breach dates

---

## 🚨 Anomaly Detection

Automatically identifies abnormal forecast behavior.

Methods used:

### Prophet

- Rolling Mean Deviation

### ARIMA

- Statistical Deviation Detection

---

## 📈 Risk Analysis

Forecasted utilization is categorized into:

| Risk Level | Description |
|------------|-------------|
| 🟢 Low | Resource usage is healthy |
| 🟠 Medium | Approaching threshold |
| 🔴 High | Capacity risk detected |

---

## 💡 AI Recommendations

Provides simple recommendations such as:

- Monitor resource growth
- Scale infrastructure
- Optimize workload distribution
- Investigate abnormal spikes

---

## 📥 CSV Export

Users can download:

- Forecast dates
- Predicted values
- Anomaly flags

as a CSV file.

---

# 🏗 System Architecture

```text
Metrics CSV
     │
     ▼
Data Validation
     │
     ▼
NL Query Understanding
     │
     ▼
Metric Selection Agent
     │
     ▼
Forecast Engine
 ┌─────────────┐
 │   Prophet   │
 │    ARIMA    │
 └─────────────┘
     │
     ▼
Threshold Detection
     │
     ▼
Anomaly Detection
     │
     ▼
Risk Analysis
     │
     ▼
System Health &
Recommendations
     │
     ▼
Streamlit Dashboard
     │
     ▼
CSV Export
```

---

# 🛠 Technology Stack

| Layer | Technology |
|---------|------------|
| Frontend | Streamlit |
| Forecasting | Prophet |
| Statistical Forecasting | ARIMA |
| Data Processing | Pandas |
| Numerical Computing | NumPy |
| Visualization | Matplotlib |
| Testing | Pytest |
| Language | Python |

---

# 📂 Project Structure

```text
IM02_PROJECT/

│
├── app.py
├── requirements.txt
├── README.md
├── prompts.md
├── ai_usage_note.md
├── DEMO_LINK.md
├── Team_info.txt
│
├── data/
│   └── metrics.csv
│
├── outputs/
│   └── sample_forecast.csv
│
├── Resumes/
│   ├── Rekha_Resume.pdf
│   ├── Sindhu_Resume.pdf
│   ├── Sreeja_resume.pdf
│   └── Varshitha_Resume.pdf
│
├── screenshots/
│   ├── Prophet_dashboard.png
│   ├── Prophet_graph.png
│   ├── Prophet_output.png
│   ├── ARIMA_graph.png
│   ├── ARIMA_output.png
│
├── Test_cases/
│   └── test_cases.md
│
└── tests/
    └── test_app.py
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/rekha2756/IM-02_Capacity_Forecaster.git
```

Move into project directory:

```bash
cd Capacity_Forecaster
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app.py
```

---

# 📄 Input Dataset Format

The application accepts a CSV file with the following columns:

| Column | Description |
|----------|------------|
| Date | Observation Date |
| CPU | CPU Utilization (%) |
| Memory | Memory Utilization (%) |
| Disk | Disk Utilization (%) |

Example:

```csv
Date,CPU,Memory,Disk
2025-01-01,40,60,70
2025-01-02,42,62,72
2025-01-03,45,65,75
```

---

# 📊 Sample Forecast Output

| Date | Predicted Value | Anomaly |
|--------|---------------|---------|
| 2026-03-10 | 118.4 | False |
| 2026-03-12 | 130.2 | True |

---

# 🎯 Example Queries

## CPU Forecast

Input:

```text
When will CPU hit 120?
```

Output:

```text
CPU will hit 120 on 18-03-2026
```

---

## Memory Forecast

Input:

```text
When will Memory hit 130?
```

Output:

```text
Memory will hit 130 on 12-03-2026
```

---

## Disk Forecast

Input:

```text
When will Disk hit 140?
```

Output:

```text
Disk will hit 140 on <predicted date>
```

---

# 🧪 Testing

Run test suite:

```bash
pytest tests/test_app.py
```

Test coverage includes:

- Forecast generation
- Threshold detection
- Query parsing
- Output validation
- Anomaly detection
- Risk classification

---

# 📸 Screenshots

## Dashboard Overview

`screenshots/Prophet_dashboard.png`

## Prophet Forecast

`screenshots/Prophet_graph.png`

## Prophet Output

`screenshots/Prophet_output.png`

## ARIMA Forecast

`screenshots/ARIMA_graph.png`

## ARIMA Output

`screenshots/ARIMA_output.png`

---

# 📹 Demo Video

Refer:

```text
DEMO_LINK.md
```

---

# 🤖 AI Capabilities Demonstrated

- Natural Language Query Processing
- Time Series Forecasting
- Prophet Forecasting
- ARIMA Forecasting
- Capacity Planning
- Anomaly Detection
- Risk Assessment
- Predictive Analytics
- Decision Support System

---

# 📦 Deliverables

Included in repository:

- Source Code
- README
- AI Usage Note
- Prompt Documentation
- Test Cases
- Sample Dataset
- Screenshots
- Team Resumes
- Demo Video Link

---

# 🤝 AI Usage Disclosure

AI tools were used for:

- Streamlit dashboard development
- Forecasting workflow design
- ARIMA integration support
- Documentation assistance
- Test case preparation

All generated outputs were reviewed, tested, and validated by the project team.

---

# 👥 Team

- Rekha 
- Sindhu
- Sreeja
- Varshitha

---

# 📜 License

This project is developed for academic and educational purposes as part of the IM-02 Capacity Forecaster demonstration.
