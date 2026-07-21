import streamlit as st

def executive_summary(df):

    total_sales = df["Sales"].sum()

    total_orders = df["Order_ID"].nunique()

    avg = total_sales / total_orders

    state = (
        df.groupby("State")["Sales"]
        .sum()
        .idxmax()
    )

    category = (
        df.groupby("Category")["Sales"]
        .sum()
        .idxmax()
    )

    customer = (
        df.groupby("Customer_Name")["Sales"]
        .sum()
        .idxmax()
    )

    st.markdown("## 📄 Executive Summary")

    st.markdown(f"""

### Sales Overview

- 💰 Total Revenue : **₹{total_sales:,.0f}**

- 📦 Orders Processed : **{total_orders:,}**

- 📍 Highest Revenue State : **{state}**

- 🛍 Highest Selling Category : **{category}**

- 👤 Best Customer : **{customer}**

- 💳 Average Order Value : **₹{avg:,.0f}**

""")