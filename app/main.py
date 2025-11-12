import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, summary_stats


st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

st.title("☀️ Solar Energy Comparison Dashboard")

st.markdown("""
Explore and compare solar irradiance metrics (GHI, DNI, DHI)
across Benin, Sierra Leone, and Togo.
""")

# Sidebar
st.sidebar.header("Controls")
countries = ["Benin", "Sierra Leone", "Togo"]
selected_countries = st.sidebar.multiselect("Select countries to compare:", countries, default=countries)

# Load data dynamically
data = load_data(selected_countries)

if not data.empty:
    metric = st.sidebar.selectbox("Select metric:", ["GHI", "DNI", "DHI"])

    # Boxplot comparison
    st.subheader(f"📊 {metric} Comparison")
    fig = px.box(data, x="Country", y=metric, color="Country", title=f"{metric} Distribution by Country")
    st.plotly_chart(fig, use_container_width=True)

    # Summary stats table
    st.subheader("📋 Summary Statistics")
    st.dataframe(summary_stats(data, metric))

    # Ranking bar chart
    st.subheader("🏆 Average GHI by Country")
    avg = data.groupby("Country")[metric].mean().reset_index()
    fig_bar = px.bar(avg, x="Country", y=metric, color="Country", text=metric)
    st.plotly_chart(fig_bar, use_container_width=True)

else:
    st.warning("No data loaded. Please ensure cleaned CSVs are available locally.")
