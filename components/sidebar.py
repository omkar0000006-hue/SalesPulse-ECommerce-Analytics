import streamlit as st
import pandas as pd


def filters(df):

    st.sidebar.title("📊 Dashboard Filters")

    st.sidebar.markdown("---")

    # ===============================
    # Date Range
    # ===============================

    min_date = df["Order_Date"].min().date()
    max_date = df["Order_Date"].max().date()

    date_range = st.sidebar.date_input(
        "📅 Order Date",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    # ===============================
    # State
    # ===============================

    states = sorted(df["State"].dropna().unique())

    selected_states = st.sidebar.multiselect(
        "🏙 State",
        states,
        default=states
    )

    # ===============================
    # Category
    # ===============================

    categories = sorted(df["Category"].dropna().unique())

    selected_categories = st.sidebar.multiselect(
        "🛍 Category",
        categories,
        default=categories
    )

    # ===============================
    # Order Status
    # ===============================

    status = sorted(df["Order_Status"].dropna().unique())

    selected_status = st.sidebar.multiselect(
        "📦 Order Status",
        status,
        default=status
    )

    # ===============================
    # Sales Channel
    # ===============================

    channels = sorted(df["Sales_Channel"].dropna().unique())

    selected_channels = st.sidebar.multiselect(
        "🌐 Sales Channel",
        channels,
        default=channels
    )

    # ===============================
    # Fulfilment
    # ===============================

    fulfilment = sorted(df["Fulfilment"].dropna().unique())

    selected_fulfilment = st.sidebar.multiselect(
        "🚚 Fulfilment",
        fulfilment,
        default=fulfilment
    )

    # ===============================
    # Customer Search
    # ===============================

    customer = st.sidebar.text_input(
        "🔍 Search Customer"
    )

    st.sidebar.markdown("---")

    # ===============================
    # Apply Date Filter
    # ===============================

    if len(date_range) == 2:

        start_date, end_date = date_range

        df = df[
            (df["Order_Date"] >= pd.to_datetime(start_date))
            &
            (df["Order_Date"] <= pd.to_datetime(end_date))
        ]

    # ===============================
    # Apply Filters
    # ===============================

    df = df[df["State"].isin(selected_states)]

    df = df[df["Category"].isin(selected_categories)]

    df = df[df["Order_Status"].isin(selected_status)]

    df = df[df["Sales_Channel"].isin(selected_channels)]

    df = df[df["Fulfilment"].isin(selected_fulfilment)]

    # ===============================
    # Customer Search
    # ===============================

    if customer != "":

        df = df[
            df["Customer_Name"]
            .str.contains(customer, case=False, na=False)
        ]

    # ===============================
    # Sidebar Statistics
    # ===============================

    st.sidebar.markdown("### 📈 Current Selection")

    st.sidebar.metric(
        "Orders",
        f"{df['Order_ID'].nunique():,}"
    )

    st.sidebar.metric(
        "Revenue",
        f"₹{df['Sales'].sum():,.0f}"
    )

    st.sidebar.metric(
        "Customers",
        f"{df['Customer_Name'].nunique():,}"
    )

    return df