import pandas as pd
import numpy as np

np.random.seed(42)

# Load the raw trade data
df = pd.read_csv("data/raw/trades.csv")

print("Original shape:", df.shape)

# Quick check before cleaning
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nData types:")
print(df.dtypes)


# Remove duplicate records
df = df.drop_duplicates()


# Make sure dates are stored correctly
df["trade_date"] = pd.to_datetime(df["trade_date"])


# Keep only valid trade records
df = df[
    (df["quantity"] > 0) &
    (df["price"] > 0) &
    (df["trade_value"] > 0)
]


# Add fields that will be useful for analysis
df["trade_month"] = df["trade_date"].dt.to_period("M").astype(str)
df["trade_year"] = df["trade_date"].dt.year

df["trade_value_millions"] = (
    df["trade_value"] / 1_000_000
)

df["commission_rate"] = (
    df["commission"] / df["trade_value"]
)


# Simulate a reference market price for analysis
df["market_price"] = df["price"] * np.random.uniform(
    0.90, 1.10, len(df)
)


# Estimate P&L based on the trade direction
df["pnl"] = np.where(
    df["trade_type"] == "BUY",
    (df["market_price"] - df["price"]) * df["quantity"],
    (df["price"] - df["market_price"]) * df["quantity"]
)


# Flag trades that are unusually large
mean_value = df["trade_value"].mean()
std_value = df["trade_value"].std()

df["risk_flag"] = df["trade_value"] > (
    mean_value + 3 * std_value
)


# Basic trade statistics
print("\nTotal trades:", len(df))

print(
    "Total trading volume:",
    round(df["trade_value"].sum(), 2)
)

print(
    "Average trade value:",
    round(df["trade_value"].mean(), 2)
)

print(
    "Total P&L:",
    round(df["pnl"].sum(), 2)
)

print(
    "Profitable trades:",
    (df["pnl"] > 0).sum()
)

print(
    "Losing trades:",
    (df["pnl"] < 0).sum()
)

print(
    "High-risk trades:",
    df["risk_flag"].sum()
)


print("\nVolume by asset class:")

volume_by_asset = (
    df.groupby("asset_class")["trade_value"]
    .sum()
    .sort_values(ascending=False)
)

print(volume_by_asset)


print("\nTop 10 customers:")

top_customers = (
    df.groupby("customer_id")["trade_value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)


# Save the cleaned data for the next stage
df.to_csv(
    "data/processed/clean_trades.csv",
    index=False
)

print("\nCleaned dataset saved!")

