import streamlit as st

# ===============================
# Import Modules
# ===============================

from utils.load_data import load_data
from utils.metrics import get_metrics
from components.sidebar import filters
from components.cards import show_cards

from components.charts import (
    monthly_sales_chart,
    category_chart,
    state_chart,
    order_status_chart,
    sales_channel_chart,
    top_customers_chart,
    top_products_chart,
    daily_sales_chart,
    city_sales_chart,
    fulfilment_chart,
)

# ===============================
# Page Configuration
# ===============================

st.set_page_config(
    page_title="E-Commerce Sales Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ===============================
# Title
# ===============================

st.title("📊 E-Commerce Sales Analytics Dashboard")
st.caption("Interactive Business Intelligence Dashboard")

st.divider()

# ===============================
# Load Data
# ===============================

df = load_data()

# ===============================
# Sidebar Filters
# ===============================

df = filters(df)

# ===============================
# KPI Cards
# ===============================

metrics = get_metrics(df)

show_cards(metrics)

st.divider()

# ===============================
# Charts - Row 1
# ===============================

col1, col2 = st.columns(2)

with col1:
    monthly_sales_chart(df)

with col2:
    category_chart(df)

# ===============================
# Charts - Row 2
# ===============================

col3, col4 = st.columns(2)

with col3:
    state_chart(df)

with col4:
    order_status_chart(df)

# ===============================
# Charts - Row 3
# ===============================

col5, col6 = st.columns(2)

with col5:
    sales_channel_chart(df)

with col6:
    fulfilment_chart(df)

# ===============================
# Charts - Row 4
# ===============================

col7, col8 = st.columns(2)

with col7:
    top_products_chart(df)

with col8:
    top_customers_chart(df)

# ===============================
# Charts - Row 5
# ===============================

col9, col10 = st.columns(2)

with col9:
    daily_sales_chart(df)

with col10:
    city_sales_chart(df)

# ===============================
# Data Table
# ===============================

st.divider()

st.subheader("📋 Filtered Sales Data")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
)

# ===============================
# Download CSV
# ===============================

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_sales.csv",
    mime="text/csv",
)

# ===============================
# Footer
# ===============================

st.divider()

st.caption(
    "Developed using Python • Streamlit • Plotly • Pandas"
)