import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv")

print(df.head())
print(df.columns)
print(df.shape)
print(df.columns.tolist())
print("Missing Values:")
print(df.isnull().sum())
df = df.dropna(how="all")

print("After removing blank rows:")
print(df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())
print(df.dtypes)
df.to_csv("output/cleaned_sales_data.csv", index=False)
print("Cleaned CSV file created successfully!")
print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Total Quantity:", df["Quantity"].sum())
category_sales = df.groupby("Category")["Sales"].sum()

print("Sales by Category:")
print(category_sales)
city_sales = df.groupby("City")["Sales"].sum()
product_sales = df.groupby("Product")["Sales"].sum()

print("Sales by Product:")
print(product_sales)

print("Sales by City:")
print(city_sales)
product_sales = df.groupby("Product")["Sales"].sum()
category_profit = df.groupby("Category")["Profit"].sum()
import matplotlib.pyplot as plt

category_sales = df.groupby("Category")["Sales"].sum()

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()
print("Profit by Category:")
print(category_profit)
print("Sales by Product:")
print(product_sales)
city_sales = df.groupby("City")["Sales"].sum()

city_sales.plot(kind="bar")

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("charts/sales_by_city.png")
plt.show()

# Sales by Category Chart

category_sales = df.groupby("Category")["Sales"].sum()

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("charts/sales_by_category.png")
plt.show()

# Sales by Product

product_sales = df.groupby("Product")["Sales"].sum()

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("charts/sales_by_product.png")
plt.show()

# Profit by Category

category_profit = df.groupby("Category")["Profit"].sum()

category_profit.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("charts/profit_by_category.png")
plt.show()

# Monthly Sales Trend

monthly_sales = df.groupby(["Month", "Month_Name"])["Sales"].sum().reset_index()

monthly_sales = monthly_sales.sort_values("Month")

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales["Month_Name"],
    monthly_sales["Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("charts/monthly_sales.png")
plt.show()


