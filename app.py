import streamlit as st
import pandas as pd
from prophet import Prophet
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AI Capacity Dashboard",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# METRIC DETECTION
# --------------------------------------------------
def detect_metric(query):
    q = query.lower()

    if "cpu" in q:
        return "CPU"
    elif "memory" in q or "ram" in q:
        return "Memory"
    elif "disk" in q or "storage" in q:
        return "Disk"

    return None


# --------------------------------------------------
# PROPHET MODEL
# --------------------------------------------------
def prophet_forecast(df, metric, threshold):

    data = pd.DataFrame({
        "ds": pd.to_datetime(df["Date"]),
        "y": df[metric]
    })

    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=60)

    forecast = model.predict(future)

    crossing = forecast[forecast["yhat"] >= threshold]

    hit_date = (
        crossing.iloc[0]["ds"]
        if not crossing.empty
        else None
    )

    forecast["rolling_mean"] = (
        forecast["yhat"]
        .rolling(5)
        .mean()
    )

    forecast["anomaly"] = (
        forecast["yhat"]
        > forecast["rolling_mean"] + 5
    )

    return hit_date, forecast


# --------------------------------------------------
# ARIMA MODEL
# --------------------------------------------------
def arima_forecast(df, metric, threshold):

    series = df[metric]

    model = ARIMA(series, order=(2, 1, 2))
    fitted = model.fit()

    forecast_values = fitted.forecast(steps=60)

    future_dates = pd.date_range(
        start=pd.to_datetime(df["Date"].iloc[-1])
        + pd.Timedelta(days=1),
        periods=60
    )

    forecast = pd.DataFrame({
        "ds": future_dates,
        "yhat": forecast_values
    })

    crossing = forecast[
        forecast["yhat"] >= threshold
    ]

    hit_date = (
        crossing.iloc[0]["ds"]
        if not crossing.empty
        else None
    )

    mean_val = forecast["yhat"].mean()
    std_val = forecast["yhat"].std()

    forecast["anomaly"] = (
        abs(forecast["yhat"] - mean_val)
        > 2 * std_val
    )
    return hit_date, forecast


# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
# 📊 AI Capacity Monitoring Dashboard
### Forecast CPU, Memory & Disk Usage using Prophet & ARIMA
""")

st.divider()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:

    st.header("⚙ Control Panel")

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    threshold = st.slider(
        "Threshold (%)",
        50,
        100,
        80
    )

    model_choice = st.selectbox(
        "Forecast Model",
        ["Prophet", "ARIMA"]
    )

    st.markdown("---")

    st.success("AI Forecasting Engine v3.0")


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
if uploaded_file:
    df = pd.read_csv(uploaded_file)

else:
    df = pd.read_csv("data/metrics.csv")


required_cols = [
    "Date",
    "CPU",
    "Memory",
    "Disk"
]

if not all(
    col in df.columns
    for col in required_cols
):
    st.error(
        "CSV must contain Date, CPU, Memory, Disk"
    )
    st.stop()


# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------
c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "📅 Records",
    len(df)
)

c2.metric(
    "🔥 CPU Avg",
    round(df["CPU"].mean(), 1)
)

c3.metric(
    "🧠 Memory Avg",
    round(df["Memory"].mean(), 1)
)

c4.metric(
    "💾 Disk Avg",
    round(df["Disk"].mean(), 1)
)

st.divider()

# --------------------------------------------------
# DATA PREVIEW
# --------------------------------------------------
with st.expander("📂 View Dataset"):
    st.dataframe(
        df,
        use_container_width=True
    )

st.divider()

# --------------------------------------------------
# QUERY INPUT
# --------------------------------------------------
st.subheader("🔍 Ask AI Forecast Engine")

query = st.text_input(
    "Enter query",
    "When will Disk usage hit 80%?"
)

run = st.button("🚀 Run Forecast")

st.divider()

# --------------------------------------------------
# FORECAST
# --------------------------------------------------
if run:

    metric = detect_metric(query)

    if metric is None:
        st.error(
            "Please ask about CPU, Memory or Disk."
        )
        st.stop()

    if model_choice == "Prophet":
        hit_date, forecast = prophet_forecast(
            df,
            metric,
            threshold
        )

    else:
        hit_date, forecast = arima_forecast(
            df,
            metric,
            threshold
        )

    # ------------------------------------------
    # RESULT
    # ------------------------------------------
    st.subheader("🎯 Prediction Result")

    if hit_date is not None:
        st.success(
            f"{metric} will reach "
            f"{threshold}% on "
            f"{hit_date.date()}"
        )
    else:
        st.warning(
            "Threshold not reached "
            "within forecast window."
        )

    st.divider()

    # ------------------------------------------
    # FORECAST KPIs
    # ------------------------------------------
    k1, k2, k3 = st.columns(3)

    k1.metric(
        "Current Usage",
        f"{df[metric].iloc[-1]}%"
    )

    k2.metric(
        "Forecast Peak",
        f"{round(forecast['yhat'].max(),1)}%"
    )

    k3.metric(
        "Threshold",
        f"{threshold}%"
    )

    st.divider()

    # ------------------------------------------
    # RISK INDICATOR
    # ------------------------------------------
    peak = forecast["yhat"].max()

    if peak >= threshold + 15:
        st.error(
            "🔴 High Risk: Capacity likely to exceed limits"
        )

    elif peak >= threshold:
        st.warning(
            "🟠 Medium Risk: Capacity approaching threshold"
        )

    else:
        st.success(
            "🟢 Low Risk: System healthy"
        )

    st.divider()

    # ------------------------------------------
    # INSIGHTS
    # ------------------------------------------
    st.subheader("🧠 AI Insights")

    left, right = st.columns(2)

    with left:

        if metric == "CPU":
            st.info(
                "CPU usage reflects processing load."
            )

        elif metric == "Memory":
            st.info(
                "Memory usage reflects workload demand."
            )

        else:
            st.info(
                "Disk usage reflects storage growth."
            )

    with right:

        if forecast["anomaly"].any():
            st.error(
                "⚠ Forecast anomaly detected."
            )

        else:
            st.success(
                "✔ System behavior appears stable."
            )

    st.divider()

    # ------------------------------------------
    # CHART
    # ------------------------------------------
    st.subheader(
        f"📈 {model_choice} Forecast"
    )

    fig, ax = plt.subplots(
        figsize=(14, 7)
    )

    ax.plot(
        pd.to_datetime(df["Date"]),
        df[metric],
        linewidth=3,
        label="Historical"
    )

    ax.plot(
        forecast["ds"],
        forecast["yhat"],
        linewidth=3,
        linestyle="--",
        marker="o",
        label="Forecast"
    )
    ax.axhline(
        y=threshold,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Threshold {threshold}%"
    )

    ax.set_title(
        f"{metric} Forecast using {model_choice}"
    )

    ax.set_xlabel("Date")
    ax.set_ylabel("Usage (%)")

    ax.grid(True,alpha = 0.3)

    ax.legend()

    st.pyplot(fig)

    st.divider()

    # ------------------------------------------
    # FORECAST DATA
    # ------------------------------------------
    with st.expander("📄 Forecast Summary"):

        display_df = forecast[["ds", "yhat"]].copy()

        display_df["ds"] = display_df["ds"].dt.strftime("%Y-%m-%d")

        display_df["yhat"] = display_df["yhat"].round(2)

        display_df.columns = [
            "Forecast Date",
            "Predicted Usage (%)"
        ]

        st.dataframe(
            display_df,
            use_container_width=True
        )
    # ------------------------------------------
    # DOWNLOAD
    # ------------------------------------------
    st.download_button(
        "⬇ Download Forecast Report",
        forecast.to_csv(index=False),
        file_name="forecast.csv",
        mime="text/csv"
    )