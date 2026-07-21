import streamlit as st

def data_table(df):

    st.markdown("## 📋 Sales Records")

    st.dataframe(
        df,
        use_container_width=True,
        height=400
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Filtered CSV",
        csv,
        "filtered_sales.csv",
        "text/csv"
    )