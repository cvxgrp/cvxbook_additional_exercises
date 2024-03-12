import numpy as np

### Data ###
# This data file contains stock market data for Apple Inc. (AAPL) from February
# 8, 2024, to February 22, 2024. The data is from Yahoo Finance and contains the
# following parameters:
"""
- T: number of periods (days)
- Q: desired total purchase quantity (millions of shares)
- p1: initial share price (USD)
- sigma: price volatility (USD)
- pi_max: maximum participation rate
- gamma: risk aversion parameter
- v: T-vector of market volumes (millions of shares)
"""

T = 10
Q = 10 
p1 = 188 
sigma = 2.1 
pi_max = 0.05 
gamma = 0.05 
v = np.array(
    [41, 45, 42, 57, 55, 65, 50, 54, 42, 52]
)

### NOT NEEDED TO SOLVE THE EXERCISE ###
# To scrape this data from Yahoo Finance, uncomment and run the following code
# in Python:
# import numpy as np
# import yfinance as yf
# T = 10
# start_date = "2024-02-08"

# apple = yf.Ticker("AAPL")
# data = apple.history(period="max")
# price = data["Close"]
# volume = np.round(data["Volume"].loc[start_date:].iloc[:T] / 1e6).astype(int)
# p1 = np.round(price.loc[start_date]).astype(int)
# sigma = np.round(price.loc[:start_date][-63:].diff().std(), 1)
