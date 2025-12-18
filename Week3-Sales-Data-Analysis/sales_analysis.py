# sales_analysis.py
# Week 3 Project: Sales Data Analysis

import pandas as pd

# Load dataset
df = pd.read_csv("C:/Users/anant/OneDrive/Documents/The Developers Arena/Week3-Sales-Data-Analysis/sales_data.csv")

print("📊 SALES DATA ANALYSIS")
print("----------------------")

# Display basic info
print("\nFirst 5 rows of data:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# Handle missing values
df.fillna(0, inplace=True)

# Calculate metrics
total_sales = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
max_sales = df["Total_Sales"].max()

# Best selling product
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

print("\n📈 ANALYSIS RESULTS")
print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Average Sales: ₹{average_sales:,.2f}")
print(f"Highest Single Sale: ₹{max_sales:,.2f}")
print(f"Best Selling Product: {best_product}")
