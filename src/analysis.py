import pandas as pd
from pathlib import Path

# Load cleaned dataset
file_path = Path("data/processed/cleaned_sales.csv")
df = pd.read_csv(file_path)

print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

total_sales = df["Sales"].sum()

print("\nTotal Sales:", total_sales)

total_profit = df["Profit"].sum()

print("Total Profit:", total_profit)

average_sales = df["Sales"].mean()

print("Average Sales:", average_sales)

total_quantity = df["Quantity"].sum()

print("Total Quantity Sold:", total_quantity)

category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

category_profit = df.groupby("Category")["Profit"].sum()

print("\nProfit by Category:")
print(category_profit)

region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(region_sales)

region_profit = df.groupby("Region")["Profit"].sum()

print("\nProfit by Region:")
print(region_profit)

state_sales = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nTop 10 States by Sales:")
print(state_sales.head(10))

state_profit = (
    df.groupby("State")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print("\nTop 10 States by Profit:")
print(state_profit.head(10))

segment_sales = df.groupby("Segment")["Sales"].sum()

print("\nSales by Segment:")
print(segment_sales)

subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nSales by Sub-Category:")
print(subcategory_sales)

subcategory_profit = (
    df.groupby("Sub-Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print("\nProfit by Sub-Category:")
print(subcategory_profit)

print("\nAverage Discount:", df["Discount"].mean())

print("\nCorrelation Matrix:")

print(df[["Sales","Quantity","Discount","Profit"]].corr())