-- 1. Total trading volume

SELECT
    SUM(trade_value) AS total_trading_volume
FROM fact_trades;


-- 2. Average trade value

SELECT
    AVG(trade_value) AS average_trade_value
FROM fact_trades;


-- 3. Total P&L

SELECT
    SUM(pnl) AS total_pnl
FROM fact_trades;


-- 4. Trading volume by asset class

SELECT
    asset_class,
    COUNT(*) AS trade_count,
    SUM(trade_value) AS trading_volume,
    SUM(pnl) AS total_pnl
FROM fact_trades
GROUP BY asset_class
ORDER BY trading_volume DESC;


-- 5. BUY vs SELL analysis

SELECT
    trade_type,
    COUNT(*) AS trade_count,
    SUM(trade_value) AS trading_volume,
    SUM(pnl) AS total_pnl
FROM fact_trades
GROUP BY trade_type;


-- 6. Top 10 customers by trading volume

SELECT
    customer_id,
    COUNT(*) AS trade_count,
    SUM(trade_value) AS trading_volume,
    SUM(pnl) AS total_pnl
FROM fact_trades
GROUP BY customer_id
ORDER BY trading_volume DESC
LIMIT 10;


-- 7. High-risk trades

SELECT
    trade_id,
    customer_id,
    account_id,
    trade_date,
    asset_class,
    symbol,
    trade_type,
    trade_value,
    pnl
FROM fact_trades
WHERE risk_flag = 1
ORDER BY trade_value DESC;


-- 8. Monthly trading activity

SELECT
    trade_year,
    trade_month,
    COUNT(*) AS trade_count,
    SUM(trade_value) AS trading_volume,
    SUM(pnl) AS total_pnl
FROM fact_trades
GROUP BY trade_year, trade_month
ORDER BY trade_year, trade_month;


-- 9. Trading volume by country

SELECT
    country,
    COUNT(*) AS trade_count,
    SUM(trade_value) AS trading_volume,
    SUM(pnl) AS total_pnl
FROM fact_trades
GROUP BY country
ORDER BY trading_volume DESC;


-- 10. Largest trades

SELECT
    trade_id,
    customer_id,
    asset_class,
    symbol,
    trade_type,
    quantity,
    price,
    trade_value,
    pnl
FROM fact_trades
ORDER BY trade_value DESC
LIMIT 10;