import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("data/trades.db")


queries = {
    "Asset Class Analysis": """
        SELECT
            a.asset_class,
            COUNT(f.trade_id) AS trade_count,
            SUM(f.trade_value) AS trading_volume,
            SUM(f.pnl) AS total_pnl
        FROM fact_trades f
        JOIN dim_asset a
            ON f.symbol = a.symbol
        GROUP BY a.asset_class
        ORDER BY trading_volume DESC;
    """,

    "Top Customers": """
        SELECT
            customer_id,
            COUNT(*) AS trade_count,
            SUM(trade_value) AS trading_volume,
            SUM(pnl) AS total_pnl
        FROM fact_trades
        GROUP BY customer_id
        ORDER BY trading_volume DESC
        LIMIT 10;
    """,

    "Risk Trades": """
        SELECT
            trade_id,
            customer_id,
            symbol,
            asset_class,
            trade_type,
            trade_value,
            pnl
        FROM fact_trades
        WHERE risk_flag = 1
        ORDER BY trade_value DESC;
    """,

    "Monthly Analysis": """
        SELECT
            trade_year,
            trade_month,
            COUNT(*) AS trade_count,
            SUM(trade_value) AS trading_volume,
            SUM(pnl) AS total_pnl
        FROM fact_trades
        GROUP BY trade_year, trade_month
        ORDER BY trade_year, trade_month;
    """
}


for name, query in queries.items():

    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    result = pd.read_sql(query, conn)

    print(result.to_string(index=False))


conn.close()