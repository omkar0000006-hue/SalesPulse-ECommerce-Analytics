import pandas as pd

# Load datasets
amazon = pd.read_csv("data/Amazon Sale Report.csv")
orders = pd.read_csv("data/List of Orders.csv")

print("Amazon Dataset:", amazon.shape)
print("Orders Dataset:", orders.shape)

# Select useful columns
amazon = amazon[
    [
        "Order ID",
        "Date",
        "Category",
        "SKU",
        "Qty",
        "Amount",
        "Status",
        "Fulfilment",
        "Sales Channel ",
        "Courier Status",
        "B2B"
    ]
]

orders = orders[
    [
        "CustomerName",
        "State",
        "City"
    ]
]

# Repeat customer records to match Amazon dataset size
orders = pd.concat(
    [orders] * ((len(amazon) // len(orders)) + 1),
    ignore_index=True
)

orders = orders.iloc[:len(amazon)]

# Merge horizontally
dataset = pd.concat(
    [amazon.reset_index(drop=True),
     orders.reset_index(drop=True)],
    axis=1
)

# Rename columns
dataset.columns = [
    "Order_ID",
    "Order_Date",
    "Category",
    "SKU",
    "Quantity",
    "Sales",
    "Order_Status",
    "Fulfilment",
    "Sales_Channel",
    "Courier_Status",
    "B2B",
    "Customer_Name",
    "State",
    "City"
]

# Save dataset
dataset.to_csv(
    "data/ecommerce_sales.csv",
    index=False
)

print("\nDataset Created Successfully!")

print(dataset.head())