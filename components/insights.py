import streamlit as st

def business_insights(df):

    revenue = df["Sales"].sum()

    top_state = (
        df.groupby("State")["Sales"]
        .sum()
        .idxmax()
    )

    top_category = (
        df.groupby("Category")["Sales"]
        .sum()
        .idxmax()
    )

    top_customer = (
        df.groupby("Customer_Name")["Sales"]
        .sum()
        .idxmax()
    )

    delivered = (
        df["Order_Status"]
        .astype(str)
        .str.contains("Delivered", case=False)
        .sum()
    )

    delivery_rate = delivered / len(df) * 100

    st.markdown("## 📌 Business Insights")

    st.success(f"🏆 Highest Revenue State : **{top_state}**")

    st.info(f"📦 Best Selling Category : **{top_category}**")

    st.warning(f"👤 Highest Spending Customer : **{top_customer}**")

    st.error(f"🚚 Delivery Success Rate : **{delivery_rate:.1f}%**")

    st.metric(
        "💰 Total Revenue",
        f"₹{revenue:,.0f}"
    )