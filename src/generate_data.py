import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
np.random.seed(42)

n = 20000

asset_classes = ["Equity", "Forex", "Commodity", "ETF", "Bond"]

symbols = {
    "Equity": ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL"],
    "Forex": ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD"],
    "Commodity": ["GOLD", "SILVER", "OIL", "NATGAS"],
    "ETF": ["SPY", "QQQ", "IWM", "EEM"],
    "Bond": ["US10Y", "US5Y", "UK10Y"]
}

countries = ["USA", "UK", "India", "Germany", "Singapore", "Australia"]
currencies = ["USD", "GBP", "EUR", "INR", "AUD", "SGD"]
trade_types = ["BUY", "SELL"]

rows = []

for i in range(n):

    asset_class = np.random.choice(asset_classes)
    symbol = np.random.choice(symbols[asset_class])

    quantity = np.random.randint(10, 1000)
    price = round(np.random.uniform(10, 500), 2)

    trade_value = round(quantity * price, 2)
    commission = round(trade_value * np.random.uniform(0.0005, 0.003), 2)

    rows.append({
        "trade_id": f"T{i+1:06}",
        "customer_id": f"C{np.random.randint(1, 501):04}",
        "account_id": f"A{np.random.randint(1, 1001):04}",
        "trade_date": fake.date_between(
            start_date="-1y",
            end_date="today"
        ),
        "asset_class": asset_class,
        "symbol": symbol,
        "country": np.random.choice(countries),
        "currency": np.random.choice(currencies),
        "trade_type": np.random.choice(trade_types),
        "quantity": quantity,
        "price": price,
        "trade_value": trade_value,
        "commission": commission
    })

df = pd.DataFrame(rows)

# Add a few intentionally unusual trades
for i in range(20):
    index = np.random.randint(0, n)
    df.loc[index, "quantity"] = np.random.randint(50000, 100000)
    df.loc[index, "trade_value"] = round(
        df.loc[index, "quantity"] * df.loc[index, "price"], 2
    )

df.to_csv("data/raw/trades.csv", index=False)

print("Dataset created!")
print(f"Rows: {len(df)}")
print(df.head())