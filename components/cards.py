import streamlit as st


def show_cards(metrics):

    revenue = metrics["Revenue"]
    orders = metrics["Orders"]
    customers = metrics["Customers"]
    avg_order = metrics["Average_Order"]
    quantity = metrics["Quantity"]
    delivery = metrics["Delivery_Rate"]
    cancel = metrics["Cancellation_Rate"]

    st.markdown("""
    <style>

    .card{
        background: linear-gradient(135deg,#4F46E5,#7C3AED);
        padding:20px;
        border-radius:15px;
        color:white;
        text-align:center;
        box-shadow:0px 6px 18px rgba(0,0,0,.15);
        transition:.3s;
        margin-bottom:15px;
    }

    .card:hover{
        transform:translateY(-6px);
        box-shadow:0px 12px 25px rgba(0,0,0,.30);
    }

    .title{
        font-size:17px;
        opacity:.9;
    }

    .value{
        font-size:34px;
        font-weight:bold;
        margin-top:10px;
    }

    </style>
    """, unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="card">
        <div class="title">💰 Revenue</div>
        <div class="value">₹{revenue:,.0f}</div>
        </div>
        """,unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="card">
        <div class="title">📦 Orders</div>
        <div class="value">{orders:,}</div>
        </div>
        """,unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="card">
        <div class="title">👥 Customers</div>
        <div class="value">{customers:,}</div>
        </div>
        """,unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="card">
        <div class="title">🛒 Avg Order</div>
        <div class="value">₹{avg_order:,.0f}</div>
        </div>
        """,unsafe_allow_html=True)

    st.write("")

    c5,c6,c7 = st.columns(3)

    with c5:
        st.markdown(f"""
        <div class="card">
        <div class="title">📦 Quantity Sold</div>
        <div class="value">{quantity:,}</div>
        </div>
        """,unsafe_allow_html=True)

    with c6:
        st.markdown(f"""
        <div class="card">
        <div class="title">🚚 Delivery Rate</div>
        <div class="value">{delivery:.1f}%</div>
        </div>
        """,unsafe_allow_html=True)

    with c7:
        st.markdown(f"""
        <div class="card">
        <div class="title">❌ Cancellation</div>
        <div class="value">{cancel:.1f}%</div>
        </div>
        """,unsafe_allow_html=True)