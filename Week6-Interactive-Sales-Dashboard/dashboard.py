# dashboard.py
# Week 6: Interactive Sales Dashboard

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os

# -----------------------------
# SETUP
# -----------------------------

sns.set_theme(style="whitegrid")
os.makedirs("visualizations", exist_ok=True)

# Load data
df = pd.read_csv("C:/Users/anant/OneDrive/Documents/The Developers Arena/Week6-Interactive-Sales-Dashboard/sales_data.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Extract month
df['Month'] = df['Date'].dt.month

# -----------------------------
# 1. BOX PLOT (Price Distribution)
# -----------------------------

plt.figure()
sns.boxplot(x='Product', y='Price', data=df)
plt.title("Price Distribution by Product")
plt.tight_layout()
plt.savefig("visualizations/boxplot_price.png")
plt.close()

# -----------------------------
# 2. VIOLIN PLOT (Sales Distribution)
# -----------------------------

plt.figure()
sns.violinplot(x='Product', y='Total_Sales', data=df)
plt.title("Sales Distribution by Product")
plt.tight_layout()
plt.savefig("visualizations/violinplot_sales.png")
plt.close()

# -----------------------------
# 3. HEATMAP (Correlation)
# -----------------------------

plt.figure()
corr = df[['Quantity', 'Price', 'Total_Sales']].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("visualizations/heatmap_correlation.png")
plt.close()

# -----------------------------
# 4. BAR CHART (Product Sales)
# -----------------------------

product_sales = df.groupby('Product')['Total_Sales'].sum().reset_index()

plt.figure()
sns.barplot(x='Product', y='Total_Sales', data=product_sales)
plt.title("Total Sales by Product")
plt.tight_layout()
plt.savefig("visualizations/product_sales_bar.png")
plt.close()

# -----------------------------
# 5. LINE CHART (Monthly Sales)
# -----------------------------

monthly_sales = df.groupby('Month')['Total_Sales'].sum().reset_index()

plt.figure()
sns.lineplot(x='Month', y='Total_Sales', data=monthly_sales, marker='o')
plt.title("Monthly Sales Trend")
plt.tight_layout()
plt.savefig("visualizations/monthly_sales_line.png")
plt.close()

# -----------------------------
# 6. INTERACTIVE PLOT (PLOTLY)
# -----------------------------

fig = px.bar(
    product_sales,
    x='Product',
    y='Total_Sales',
    title="Interactive Product Sales",
    color='Product'
)

fig.show()

print("✅ Dashboard visualizations created successfully!")
