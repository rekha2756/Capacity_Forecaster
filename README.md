# 🚀 IM-02 AI Capacity Forecaster

An AI-powered capacity forecasting dashboard that predicts future CPU, Memory, and Disk utilization trends using Time Series Forecasting and Anomaly Detection techniques.

The application enables proactive infrastructure monitoring by forecasting future resource usage, detecting anomalies, and identifying capacity risks before they impact system performance.

---

# 📌 Problem Statement

Organizations need to forecast future capacity utilization and identify anomalies before resource bottlenecks occur.

This solution predicts future utilization trends using AI forecasting techniques and highlights abnormal utilization patterns to support proactive infrastructure planning.

---

# ✨ Features

## 📊 AI Forecasting

Supports multiple forecasting models:

* Prophet Forecasting
* ARIMA Forecasting

Forecasts utilization trends for:

* CPU Usage
* Memory Usage
* Disk Usage

---

## 🔍 Natural Language Query Interface

Users can ask questions such as:

* When will CPU usage hit 80%?
* Forecast Memory utilization.
* Predict Disk usage growth.

The application automatically detects the requested metric and generates forecasts.

---

## 🚨 Anomaly Detection

Detects abnormal forecast behavior using statistical analysis.

Capabilities include:

* Threshold breach detection
* Forecast anomaly identification
* Risk categorization

---

## 📈 Interactive Dashboard

Includes:

* KPI Cards
* Dataset Preview
* Forecast Charts
* AI Insights
* Risk Indicators
* Forecast Summary Tables

---

## 📥 Export Functionality

Download forecast results as CSV for reporting and analysis.

---

# ⭐ Business Value

This solution helps organizations:

* Predict future capacity shortages
* Reduce downtime risks
* Improve infrastructure planning
* Detect abnormal utilization patterns early
* Support proactive operational decisions
* Optimize resource allocation

---

# 📸 Application Screenshots

## Dashboard Overview

![Dashboard](screenshots/dashboard.png)

---

## Forecast Prediction

![Forecast Result](screenshots/forecast_result.png)

---

## Risk Assessment

![Risk Analysis](screenshots/risk_analysis.png)

---

## Forecast Report Download

![Download Report](screenshots/download_report.png)

---

# 🏗 Architecture

```text
Historical Metrics CSV
          │
          ▼
    Data Validation
          │
          ▼
   Forecast Engine
 (Prophet / ARIMA)
          │
          ▼
  Anomaly Detection
          │
          ▼
   Risk Assessment
          │
          ▼
 Interactive Dashboard
          │
          ▼
 Forecast Report Export
```

---

# 🛠 Technology Stack

| Layer                | Technology |
| -------------------- | ---------- |
| Frontend             | Streamlit  |
| Forecasting          | Prophet    |
| Statistical Modeling | ARIMA      |
| Data Processing      | Pandas     |
| Numerical Operations | NumPy      |
| Visualization        | Matplotlib |
| Testing              | Pytest     |
| Programming Language | Python     |

---

# 📂 Project Structure

```text
IM-02-Capacity-Forecaster/

│
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
│   ├── dashboard.png
│   ├── forecast_result.png
│   ├── risk_analysis.png
│   └── download_report.png
│
├── resumes/
│   ├── Member1_Resume.pdf
│   ├── Member2_Resume.pdf
│   ├── Member3_Resume.pdf
│   └── Member4_Resume.pdf
│
│
└── outputs/
    └── forecast.csv
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/rekha2756/Capacity_Forecaster.git
cd Capacity_Forecaster
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

---

# 📄 Input Data Format

The application accepts CSV files containing:

| Column | Description               |
| ------ | ------------------------- |
| Date   | Date of metric collection |
| CPU    | CPU Utilization (%)       |
| Memory | Memory Utilization (%)    |
| Disk   | Disk Utilization (%)      |

Example:

```csv
Date,CPU,Memory,Disk
2025-01-01,45,55,62
2025-01-02,47,57,63
2025-01-03,49,58,65
```

---

# 📊 Sample Output

Forecast Output Example:

| Column  | Description           |
| ------- | --------------------- |
| ds      | Forecast Date         |
| yhat    | Predicted Utilization |
| anomaly | Anomaly Indicator     |

Example:

```csv
ds,yhat,anomaly
2025-05-01,78.4,False
2025-05-02,82.1,True
```

---

# 🚀 Workflow

### Step 1

Upload historical metrics CSV.

### Step 2

Select forecasting model:

* Prophet
* ARIMA

### Step 3

Configure threshold percentage.

Example:

```text
80%
```

### Step 4

Ask a forecasting question.

Example:

```text
When will Disk usage hit 80%?
```

### Step 5

Generate forecast and review results.

The application provides:

* Threshold crossing date
* Forecast trend
* Risk category
* Anomaly alerts

---

# 🎯 Risk Classification

| Risk Level     | Condition                                |
| -------------- | ---------------------------------------- |
| 🟢 Low Risk    | Forecast remains below threshold         |
| 🟠 Medium Risk | Forecast approaches threshold            |
| 🔴 High Risk   | Forecast significantly exceeds threshold |

---

# 🤖 AI Capabilities Demonstrated

* Time Series Forecasting
* Prophet-Based Forecasting
* ARIMA Statistical Forecasting
* Predictive Analytics
* Capacity Planning
* Resource Utilization Prediction
* Anomaly Detection
* Risk Assessment
* Decision Support Analytics

---

# 🧪 Testing

Run all tests:

```bash
pytest
```

Or run the specific test file:

```bash
pytest tests/test_app.py
```

### Test Coverage

* Forecast generation validation
* Threshold breach detection
* Anomaly detection logic
* Forecast output verification
* Data validation checks

---

# 📋 Assumptions

* Historical utilization data is available.
* Data is accurate and chronological.
* Utilization patterns continue similarly during the forecast horizon.
* Uploaded CSV contains all required columns.

---

# ⚠ Limitations

* Forecast accuracy depends on historical data quality.
* Sudden external events may affect prediction accuracy.
* Small datasets may reduce forecasting reliability.
* ARIMA performance may vary on highly volatile datasets.

---

# 📹 Demo Video

Demo Video Link:

https://www.loom.com/share/63b136753290416caf0f323d986444c8

The demo includes:

* CSV Upload
* Forecast Generation
* Anomaly Detection
* Risk Assessment
* Report Download

---

# 🔗 GitHub Repository

Public Repository Link:

https://github.com/rekha2756/Capacity_Forecaster

---

# 👥 Team Information

### Team Name

Team-5

### Team Members

1. P.Sreeja
2. G.Rekha
3. C.Sindhu
4. K.Varshitha

---

# 📄 Team Resumes

The resumes of all team members are included in the repository under:

```text
resumes/
```

Each resume contains:

* 10th Percentage
* 12th Percentage
* Undergraduate Percentage / CGPA

---

# 📦 Submission Deliverables

✔ Source Code

✔ Public GitHub Repository

✔ README Documentation

✔ AI Usage Note

✔ Prompt Documentation

✔ Sample Dataset

✔ Test Cases

✔ Team Resumes

✔ Supporting Documents

✔ Demo Video

✔ Forecast Output

---

# 🤝 AI Usage Disclosure

AI tools were used during development for:

* Streamlit UI generation
* Forecasting implementation
* ARIMA integration
* Anomaly detection logic
* Testing support
* Documentation generation
* Debugging assistance

All generated outputs were reviewed, modified, tested, and validated by the project team before final submission.

---

# 📜 License

This project is intended for academic, educational, and demonstration purposes.

---

Developed as part of the AI Capacity Forecasting Challenge.
