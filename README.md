\# Trade \& Risk Intelligence Platform



A small end-to-end analytics project for exploring trade activity, portfolio exposure, P\&L, and unusual trade detection.



\## Overview



This project simulates a trading dataset and builds a simple analytics pipeline:



Raw trade data → Python cleaning → SQLite star schema → SQL analysis → Power BI dashboard



The project focuses on:

\- Trade volume and activity

\- P\&L analysis

\- Customer and asset exposure

\- High-risk trade detection

\- Interactive Power BI reporting



\## Tech Stack



\- Python

\- Pandas

\- NumPy

\- SQLite

\- SQL

\- Power BI

\- Git / GitHub



\## Data Model



The database uses a simple star schema:



\- `fact\_trades` — trade-level transactions

\- `dim\_customer` — customer information

\- `dim\_account` — account information

\- `dim\_asset` — asset and asset-class information

\- `dim\_date` — date information



\## Risk Detection



Large trades are flagged using a statistical threshold:



`trade\_value > mean(trade\_value) + 3 × standard deviation`



The synthetic dataset intentionally contains 20 unusually large trades so the risk-analysis workflow can be demonstrated.



\## Dashboard



The Power BI dashboard contains:



\### Overview

\- Total Trading Volume

\- Total P\&L

\- Total Trades

\- High Risk Trades



\### Trade Intelligence

\- Trading volume by asset class

\- Monthly trading volume

\- Top customers by trading volume



\### Risk Intelligence

\- High-risk trades by asset class

\- High-risk trade details

\- Risk exposure by customer



\## Key Results



Using the generated dataset:



\- 20,000 trades

\- \~$3.03B total trading volume

\- \~$271.7K total estimated P\&L

\- 20 high-risk trades



\## Important Note



All trade data, market prices, and P\&L values in this project are synthetic and illustrative. They are not real market data, StoneX data, or investment advice.

