import pandas as pd
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Load dataset
df = pd.read_csv("data/ecommerce_sales.csv")

print("=" * 60)
print("DATA CLEANING STARTED")
print("=" * 60)

# Dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df["Category"] = df["Category"].fillna("Unknown")
df["SKU"] = df["SKU"].fillna("Unknown")
df["Sales"] = df["Sales"].fillna(0)
df["Quantity"] = df["Quantity"].fillna(0)
df["Order_Status"] = df["Order_Status"].fillna("Unknown")
df["Fulfilment"] = df["Fulfilment"].fillna("Unknown")
df["Sales_Channel"] = df["Sales_Channel"].fillna("Unknown")
df["Courier_Status"] = df["Courier_Status"].fillna("Unknown")
df["Customer_Name"] = df["Customer_Name"].fillna("Unknown")
df["State"] = df["State"].fillna("Unknown")
df["City"] = df["City"].fillna("Unknown")

# Convert date column
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

# Remove rows with invalid dates
df = df.dropna(subset=["Order_Date"])

# Convert numeric columns
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(0)

df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0)

# Create additional columns
df["Month"] = df["Order_Date"].dt.month_name()
df["Year"] = df["Order_Date"].dt.year

# Save cleaned data
df.to_csv("output/cleaned_sales.csv", index=False)

print("\nCleaning Completed Successfully!")

print("\nFinal Dataset Shape:")
print(df.shape)