import pandas as pd
import streamlit as st


@st.cache_data
def load_data():

    # Load dataset
    df = pd.read_csv("output/cleaned_sales.csv")

    # -----------------------------
    # Clean Column Names
    # -----------------------------
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
    )

    # -----------------------------
    # Convert Date
    # -----------------------------
    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"],
        errors="coerce",
        infer_datetime_format=True
    )

    # Remove invalid dates
    df = df.dropna(subset=["Order_Date"])

    # -----------------------------
    # Convert Numeric Columns
    # -----------------------------
    df["Sales"] = pd.to_numeric(
        df["Sales"],
        errors="coerce"
    )

    df["Quantity"] = pd.to_numeric(
        df["Quantity"],
        errors="coerce"
    )

    # Remove invalid rows
    df = df.dropna(subset=["Sales", "Quantity"])

    # -----------------------------
    # Fill Missing Values
    # -----------------------------
    fill_columns = [
        "Category",
        "SKU",
        "Order_Status",
        "Fulfilment",
        "Sales_Channel",
        "Courier_Status",
        "Customer_Name",
        "State",
        "City"
    ]

    for col in fill_columns:

        if col in df.columns:

            df[col] = df[col].fillna("Unknown")

    # -----------------------------
    # Extra Columns
    # -----------------------------
    df["Year"] = df["Order_Date"].dt.year

    df["Month"] = df["Order_Date"].dt.month_name()

    df["Month_Number"] = df["Order_Date"].dt.month

    df["Weekday"] = df["Order_Date"].dt.day_name()

    df["Quarter"] = df["Order_Date"].dt.quarter

    # -----------------------------
    # Sort Data
    # -----------------------------
    df = df.sort_values("Order_Date")

    df = df.reset_index(drop=True)

    return df