# main.py
# Week 4: Complete Data Analysis & Visualization Project

import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure folders exist
os.makedirs("visualizations", exist_ok=True)

# Load data
try:
    df = pd.read_csv("C:/Users/anant/OneDrive/Documents/The Developers Arena/Week4-Complete-Data-Analysis/sales_data.csv")
except FileNotFoundError:
    print("❌ sales_data.csv not found!")
    exit()

# Data cleaning
df.fillna(0, inplace=True)

# ---------------- ANALYSIS ---------------- #

# Total sales
total_sales = df["Total_Sales"].sum()

# Sales by product
sales_by_product = df.groupby("Product")["Total_Sales"].sum()

# ---------------- VISUALIZATION ---------------- #

# Bar Chart: Sales by Product
plt.figure()
sales_by_product.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/sales_by_product.png")
plt.close()

# Line Chart: Sales Trend
plt.figure()
df["Total_Sales"].plot(kind="line")
plt.title("Sales Trend")
plt.xlabel("Order Index")
plt.ylabel("Sales Amount")
plt.tight_layout()
plt.savefig("visualizations/sales_trend.png")
plt.close()

# ---------------- REPORT ---------------- #

print("📊 E-COMMERCE SALES ANALYSIS")
print("----------------------------")
print(f"Total Sales: ₹{total_sales:,.2f}")
print("Charts saved in 'visualizations/' folder")
