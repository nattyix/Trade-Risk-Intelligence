import sqlite3
import os
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("data/trades.db")

# Folder for Power BI data
output_folder = "data/powerbi"

os.makedirs(output_folder, exist_ok=True)

tables = [
    "fact_trades",
    "dim_customer",
    "dim_account",
    "dim_asset",
    "dim_date"
]

# Export each table
for table in tables:

    df = pd.read_sql(
        f"SELECT * FROM {table}",
        conn
    )

    df.to_csv(
        f"{output_folder}/{table}.csv",
        index=False
    )

    print(f"{table}: {len(df)} rows exported")

conn.close()

print("\nPower BI files created.")