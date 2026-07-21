# 📊 SalesPulse – E-Commerce Sales Analytics Dashboard

An interactive Business Intelligence Dashboard built with **Python, Streamlit, Pandas, and Plotly** to analyze e-commerce sales data. The dashboard provides real-time business insights through KPIs, interactive charts, filters, and downloadable reports.

---

## 🚀 Features

- 📈 Interactive Sales Dashboard
- 💰 Revenue & Order KPIs
- 👥 Customer Analytics
- 🏷 Category Performance
- 🗺 State & City Sales Analysis
- 📦 Product (SKU) Analysis
- 🚚 Order Status & Fulfilment Tracking
- 🌐 Sales Channel Analysis
- 📅 Date Range Filtering
- 🔍 Customer Search
- 📥 Download Filtered Data as CSV
- ⚡ Fast Data Loading using Streamlit Cache

---

## 📸 Dashboard Preview

> Add screenshots here after running the project.

Example:

```
assets/dashboard.png
```

---

## 📂 Project Structure

```
SalesPulse/
│
├── assets/
│   └── style.css
│
├── components/
│   ├── cards.py
│   ├── charts.py
│   ├── sidebar.py
│   ├── insights.py
│   └── table.py
│
├── scripts/
│   └── app.py
│
├── utils/
│   ├── load_data.py
│   └── metrics.py
│
├── output/
│   └── cleaned_sales.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dashboard Modules

### KPI Cards

- Total Revenue
- Total Orders
- Total Customers
- Average Order Value
- Quantity Sold
- Delivery Rate
- Cancellation Rate

---

### Interactive Charts

- Monthly Revenue Trend
- Revenue by Category
- Revenue by State
- Daily Revenue Trend
- Top Products
- Top Customers
- Order Status Distribution
- Sales Channel Analysis
- Fulfilment Analysis
- City-wise Revenue

---

### Filters

- Date Range
- State
- Category
- Order Status
- Sales Channel
- Fulfilment
- Customer Search

---

## 📊 Dataset

The project uses an E-Commerce Sales dataset containing:

- Order ID
- Order Date
- Product Category
- SKU
- Quantity
- Sales
- Order Status
- Fulfilment
- Sales Channel
- Courier Status
- Customer Name
- State
- City

---

## 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- NumPy

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SalesPulse.git
```

Move into the project folder

```bash
cd SalesPulse
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python -m streamlit run scripts/app.py
```

---

## 📈 Future Improvements

- Revenue Forecasting
- Machine Learning Sales Prediction
- Customer Segmentation
- RFM Analysis
- Inventory Analytics
- Executive AI Insights
- Dark/Light Theme Toggle
- PDF Report Generation
- User Authentication
- Database Integration (PostgreSQL/MySQL)

---

## 👨‍💻 Author

**Omkar Yeram**

Computer Engineering Student

Aspiring Data Engineer

---

## ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.