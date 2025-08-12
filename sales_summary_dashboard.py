import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Summary Dashboard", layout="wide")
st.title("📈 Sales Summary Dashboard")

# Sample sales data embedded directly
data = [
    {"Product": "Laptop", "Category": "Electronics", "Sales": 1200, "Price": 800},
    {"Product": "Shoes", "Category": "Fashion", "Sales": 300, "Price": 50},
    {"Product": "Phone", "Category": "Electronics", "Sales": 900, "Price": 600},
    {"Product": "Shirt", "Category": "Fashion", "Sales": 150, "Price": 30},
    {"Product": "Tablet", "Category": "Electronics", "Sales": 500, "Price": 400},
    {"Product": "Watch", "Category": "Fashion", "Sales": 200, "Price": 120},
]
df = pd.DataFrame(data)

# Show raw data
st.subheader("Raw Sales Data")
st.dataframe(df)

# Filters
st.sidebar.header("Filters")
categories = st.sidebar.multiselect(
    "Select Product Categories",
    options=df["Category"].unique(),
    default=list(df["Category"].unique())
)
filtered_df = df[df["Category"].isin(categories)]

# KPIs
total_sales = filtered_df["Sales"].sum()
avg_price = filtered_df["Price"].mean()

st.subheader("Key Metrics")
st.metric("Total Sales", f"${total_sales:,.2f}")
st.metric("Average Price", f"${avg_price:,.2f}")

# Bar chart
st.subheader("Sales by Product")
fig = px.bar(filtered_df, x="Product", y="Sales", color="Category", title="Sales by Product")
st.plotly_chart(fig, use_container_width=True)

# Export
st.subheader("Export Filtered Data")
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", csv, "filtered_sales.csv", "text/csv")
