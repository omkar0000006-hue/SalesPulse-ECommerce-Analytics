import pandas as pd


def get_metrics(df):
    """
    Returns all KPI metrics required for the dashboard.
    """

    revenue = df["Sales"].sum()

    orders = df["Order_ID"].nunique()

    customers = df["Customer_Name"].nunique()

    quantity = df["Quantity"].sum()

    avg_order = revenue / orders if orders > 0 else 0

    avg_quantity = quantity / orders if orders > 0 else 0

    # Delivered Orders
    delivered = df[
        df["Order_Status"]
        .str.contains("Delivered", case=False, na=False)
    ].shape[0]

    # Cancelled Orders
    cancelled = df[
        df["Order_Status"]
        .str.contains("Cancelled", case=False, na=False)
    ].shape[0]

    delivery_rate = (
        delivered / orders * 100
        if orders > 0
        else 0
    )

    cancellation_rate = (
        cancelled / orders * 100
        if orders > 0
        else 0
    )

    return {
        "Revenue": revenue,
        "Orders": orders,
        "Customers": customers,
        "Quantity": quantity,
        "Average_Order": avg_order,
        "Average_Quantity": avg_quantity,
        "Delivery_Rate": delivery_rate,
        "Cancellation_Rate": cancellation_rate
    }


# ---------------------------------------------------
# Revenue by Month
# ---------------------------------------------------

def monthly_sales(df):

    monthly = (
        df.groupby(["Year", "Month_Number", "Month"])["Sales"]
        .sum()
        .reset_index()
        .sort_values(["Year", "Month_Number"])
    )

    return monthly


# ---------------------------------------------------
# Revenue by State
# ---------------------------------------------------

def state_sales(df):

    state = (
        df.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    return state


# ---------------------------------------------------
# Revenue by Category
# ---------------------------------------------------

def category_sales(df):

    category = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    return category


# ---------------------------------------------------
# Top Products
# ---------------------------------------------------

def top_products(df, top_n=10):

    products = (
        df.groupby("SKU")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    return products


# ---------------------------------------------------
# Top Customers
# ---------------------------------------------------

def top_customers(df, top_n=10):

    customers = (
        df.groupby("Customer_Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    return customers


# ---------------------------------------------------
# Order Status
# ---------------------------------------------------

def order_status(df):

    status = (
        df["Order_Status"]
        .value_counts()
        .reset_index()
    )

    status.columns = [
        "Status",
        "Count"
    ]

    return status


# ---------------------------------------------------
# Sales Channel
# ---------------------------------------------------

def sales_channel(df):

    channel = (
        df["Sales_Channel"]
        .value_counts()
        .reset_index()
    )

    channel.columns = [
        "Channel",
        "Count"
    ]

    return channel


# ---------------------------------------------------
# Daily Revenue
# ---------------------------------------------------

def daily_sales(df):

    daily = (
        df.groupby("Order_Date")["Sales"]
        .sum()
        .reset_index()
    )

    return daily


# ---------------------------------------------------
# Executive Summary
# ---------------------------------------------------

def executive_summary(df):

    summary = {
        "Top State":
            df.groupby("State")["Sales"]
              .sum()
              .idxmax(),

        "Top Category":
            df.groupby("Category")["Sales"]
              .sum()
              .idxmax(),

        "Top Customer":
            df.groupby("Customer_Name")["Sales"]
              .sum()
              .idxmax(),

        "Top Product":
            df.groupby("SKU")["Sales"]
              .sum()
              .idxmax(),

        "Highest Sale":
            df["Sales"].max(),

        "Lowest Sale":
            df["Sales"].min(),

        "Average Sale":
            df["Sales"].mean()
    }

    return summary