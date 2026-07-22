import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="E-Commerce Dashboard",
    layout="wide"
)

df = pd.read_csv("data/processed/cleaned_sales.csv")

st.title("📊 E-Commerce Sales Dashboard")
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
average_discount = df["Discount"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📈 Total Profit", f"${total_profit:,.2f}")
col3.metric("📦 Quantity Sold", int(total_quantity))
col4.metric("🏷️ Avg Discount", f"{average_discount:.2%}")

st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

segment = st.sidebar.multiselect(
    "Select Segment",
    options=df["Segment"].unique(),
    default=df["Segment"].unique()
)

filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Segment"].isin(segment))
]

import plotly.express as px

category_sales = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Sales by Category"
)

st.plotly_chart(fig, use_container_width=True)

region_sales = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig = px.pie(
    region_sales,
    values="Sales",
    names="Region",
    title="Sales by Region"
)

st.plotly_chart(fig, use_container_width=True)

profit = (
    filtered_df.groupby("Category")["Profit"]
    .sum()
    .reset_index()
)

fig = px.bar(
    profit,
    x="Category",
    y="Profit",
    color="Category",
    title="Profit by Category"
)

st.plotly_chart(fig, use_container_width=True)

states = (
    filtered_df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    states,
    x="State",
    y="Sales",
    title="Top 10 States"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Correlation Matrix")

st.dataframe(
    filtered_df[
        ["Sales", "Profit", "Quantity", "Discount"]
    ].corr()
)

st.download_button(
    "⬇️ Download Filtered Data",
    filtered_df.to_csv(index=False),
    file_name="filtered_sales.csv",
    mime="text/csv"
)

st.dataframe(df)