import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Better-looking graphs
plt.style.use("ggplot")
sns.set_theme()

# Load cleaned dataset
df = pd.read_csv(Path("data/processed/cleaned_sales.csv"))

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar", color="skyblue")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("images/sales_by_category.png")
plt.show()

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
category_profit.plot(kind="bar", color="green")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("images/profit_by_category.png")
plt.show()

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar", color="orange")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("images/sales_by_region.png")
plt.show()

region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(8,5))
region_profit.plot(kind="bar", color="purple")

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("images/profit_by_region.png")
plt.show()

top_states = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))
top_states.plot(kind="bar", color="red")

plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("images/top_states_sales.png")
plt.show()

segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(7,7))

plt.pie(
    segment_sales,
    labels=segment_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales by Segment")

plt.savefig("images/segment_sales_pie.png")
plt.show()

plt.figure(figsize=(8,5))

sns.histplot(df["Discount"], bins=20)

plt.title("Discount Distribution")

plt.tight_layout()

plt.savefig("images/discount_distribution.png")
plt.show()

plt.figure(figsize=(8,5))

sns.histplot(df["Profit"], bins=30)

plt.title("Profit Distribution")

plt.tight_layout()

plt.savefig("images/profit_distribution.png")
plt.show()

plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit"
)

plt.title("Sales vs Profit")

plt.tight_layout()

plt.savefig("images/sales_vs_profit.png")
plt.show()

plt.figure(figsize=(8,6))

corr = df[["Sales","Profit","Quantity","Discount"]].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("images/correlation_heatmap.png")
plt.show()

plt.figure(figsize=(8,5))

sns.boxplot(
    x=df["Profit"]
)

plt.title("Profit Boxplot")

plt.tight_layout()

plt.savefig("images/profit_boxplot.png")
plt.show()