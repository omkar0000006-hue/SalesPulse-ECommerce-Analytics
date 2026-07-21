import streamlit as st
import plotly.express as px


# =====================================================
# Monthly Sales Trend
# =====================================================

def monthly_sales_chart(df):

    monthly = (
        df.groupby(["Year", "Month_Number", "Month"])["Sales"]
        .sum()
        .reset_index()
        .sort_values(["Year", "Month_Number"])
    )

    fig = px.line(
        monthly,
        x="Month",
        y="Sales",
        markers=True,
        title="Monthly Revenue Trend"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        xaxis_title="Month",
        yaxis_title="Revenue",
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)


# =====================================================
# Revenue by Category
# =====================================================

def category_chart(df):

    category = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        category,
        x="Category",
        y="Sales",
        color="Sales",
        title="Revenue by Category",
        text_auto=".2s"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        title_x=0.5,
        coloraxis_showscale=False
    )

    st.plotly_chart(fig, use_container_width=True)


# =====================================================
# Revenue by State
# =====================================================

def state_chart(df):

    state = (
        df.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        state,
        x="Sales",
        y="State",
        orientation="h",
        color="Sales",
        title="Top 10 States by Revenue",
        text_auto=".2s"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        title_x=0.5,
        coloraxis_showscale=False
    )

    st.plotly_chart(fig, use_container_width=True)


# =====================================================
# Order Status Distribution
# =====================================================

def order_status_chart(df):

    status = (
        df["Order_Status"]
        .value_counts()
        .reset_index()
    )

    status.columns = [
        "Status",
        "Count"
    ]

    fig = px.pie(
        status,
        names="Status",
        values="Count",
        hole=0.55,
        title="Order Status Distribution"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)
    # =====================================================
# Sales Channel Distribution
# =====================================================

def sales_channel_chart(df):

    channel = (
        df["Sales_Channel"]
        .value_counts()
        .reset_index()
    )

    channel.columns = ["Channel", "Orders"]

    fig = px.treemap(
        channel,
        path=["Channel"],
        values="Orders",
        title="Sales Channel Distribution"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)


# =====================================================
# Top Customers
# =====================================================

def top_customers_chart(df):

    customer = (
        df.groupby("Customer_Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        customer,
        x="Sales",
        y="Customer_Name",
        orientation="h",
        color="Sales",
        title="Top 10 Customers",
        text_auto=".2s"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        title_x=0.5,
        coloraxis_showscale=False
    )

    st.plotly_chart(fig, use_container_width=True)


# =====================================================
# Top Products
# =====================================================

def top_products_chart(df):

    product = (
        df.groupby("SKU")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        product,
        x="Sales",
        y="SKU",
        orientation="h",
        color="Sales",
        title="Top 10 Products",
        text_auto=".2s"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        title_x=0.5,
        coloraxis_showscale=False
    )

    st.plotly_chart(fig, use_container_width=True)


# =====================================================
# Daily Sales Trend
# =====================================================

def daily_sales_chart(df):

    daily = (
        df.groupby("Order_Date")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.area(
        daily,
        x="Order_Date",
        y="Sales",
        title="Daily Revenue Trend"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        title_x=0.5,
        xaxis_title="Order Date",
        yaxis_title="Revenue"
    )

    st.plotly_chart(fig, use_container_width=True)


# =====================================================
# Top Cities
# =====================================================

def city_sales_chart(df):

    city = (
        df.groupby("City")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        city,
        x="City",
        y="Sales",
        color="Sales",
        title="Top 10 Cities by Revenue",
        text_auto=".2s"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        title_x=0.5,
        coloraxis_showscale=False
    )

    st.plotly_chart(fig, use_container_width=True)


# =====================================================
# Fulfilment Distribution
# =====================================================

def fulfilment_chart(df):

    fulfilment = (
        df["Fulfilment"]
        .value_counts()
        .reset_index()
    )

    fulfilment.columns = [
        "Fulfilment",
        "Orders"
    ]

    fig = px.pie(
        fulfilment,
        names="Fulfilment",
        values="Orders",
        hole=0.45,
        title="Fulfilment Distribution"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)