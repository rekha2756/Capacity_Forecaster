import streamlit as st
import pandas as pd
import re
from prophet import Prophet
import matplotlib.pyplot as plt

# Title
st.title("📈 AI Capacity Forecaster")

st.markdown("""
Forecast CPU, Memory, and Disk utilization using
Natural Language Queries and Time Series Forecasting.
""")

# File Upload
uploaded_file = st.file_uploader(
    "Upload Metrics CSV",
    type=["csv"]
)

# Load Data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("metrics.csv")

# Show Data
st.subheader("Resource Data")
st.dataframe(df)

# Query Input
query = st.text_input(
    "Ask a question",
    "When will disk usage hit 80%?"
)

# Forecast Button
if st.button("Forecast"):

    q = query.lower()

    # Detect Metric
    if "disk" in q:
        metric = "Disk"
    elif "cpu" in q:
        metric = "CPU"
    elif "memory" in q:
        metric = "Memory"
    else:
        st.error("Metric not found. Please ask about CPU, Memory, or Disk.")
        st.stop()

    # Show detected metric
    st.info(f"Detected Metric: {metric}")

    # Extract threshold
    numbers = re.findall(r"\d+", q)

    if len(numbers) == 0:
        st.error("Please provide a threshold value.")
        st.stop()

    threshold = int(numbers[0])

    # Prepare data for Prophet
    forecast_df = pd.DataFrame({
        "ds": pd.to_datetime(df["Date"]),
        "y": df[metric]
    })

    # Train Model
    model = Prophet()
    model.fit(forecast_df)

    # Future Predictions
    future = model.make_future_dataframe(periods=60)
    forecast = model.predict(future)

    # Find threshold crossing date
    crossing = forecast[forecast["yhat"] >= threshold]

    if len(crossing) > 0:
        hit_date = crossing.iloc[0]["ds"]

        st.success(
            f"Prediction Result: {metric} usage is expected "
            f"to reach {threshold}% on {hit_date.date()}"
        )
    else:
        st.warning("Threshold not reached in forecast period.")

    # Forecast Chart
    st.subheader("Forecast Visualization")

    fig = model.plot(forecast)
    st.pyplot(fig)