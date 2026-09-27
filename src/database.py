import sqlite3
import pandas as pd

# Load the cleaned trade data
df = pd.read_csv("data/processed/clean_trades.csv")

# Connect to SQLite
conn = sqlite3.connect("data/trades.db")


# Create the fact table
df.to_sql(
    "fact_trades",
    conn,
    if_exists="replace",
    index=False
)


# Customer dimension
dim_customer = (
    df[
        ["customer_id", "country", "currency"]
    ]
    .drop_duplicates("customer_id")
)

dim_customer.to_sql(
    "dim_customer",
    conn,
    if_exists="replace",
    index=False
)


# Account dimension
dim_account = (
    df[
        ["account_id", "customer_id"]
    ]
    .drop_duplicates("account_id")
)

dim_account.to_sql(
    "dim_account",
    conn,
    if_exists="replace",
    index=False
)


# Asset dimension
dim_asset = (
    df[
        ["symbol", "asset_class"]
    ]
    .drop_duplicates("symbol")
)

dim_asset.to_sql(
    "dim_asset",
    conn,
    if_exists="replace",
    index=False
)


# Date dimension
dim_date = (
    df[
        ["trade_date", "trade_month", "trade_year"]
    ]
    .drop_duplicates("trade_date")
)

dim_date.to_sql(
    "dim_date",
    conn,
    if_exists="replace",
    index=False
)


# Check the tables
tables = pd.read_sql(
    """
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    """,
    conn
)

print("\nDatabase tables:")
print(tables)


# Check row counts
for table in [
    "fact_trades",
    "dim_customer",
    "dim_account",
    "dim_asset",
    "dim_date"
]:
    result = pd.read_sql(
        f"SELECT COUNT(*) AS rows FROM {table}",
        conn
    )

    print(f"{table}: {result.iloc[0, 0]}")


conn.close()

print("\nDatabase created successfully.")