import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Define a function to get the ticker name from the symbol
def get_ticker_name(symbol):
    return yf.Ticker(symbol).info['longName']

# Prompt for both stock symbols
tickr1 = input("Enter the first stock symbol: ")
tickr2 = input("Enter the second stock symbol: ")

# Fetch historical data of both stocks from Yahoo Finance
stock1 = yf.Ticker(tickr1)
stock2 = yf.Ticker(tickr2)
stock1_hist = stock1.history(start="2023-01-01")
stock2_hist = stock2.history(start="2023-01-01")

# Normalize the historical data
scaler = MinMaxScaler()
stock1_norm = scaler.fit_transform(stock1_hist["Close"].values.reshape(-1, 1))
stock2_norm = scaler.fit_transform(stock2_hist["Close"].values.reshape(-1, 1))

# Set the initial value of both stocks to 100
stock1_norm *= 100
stock2_norm *= 100

# Calculate the 20-day moving average for both stocks
stock1_ma = pd.DataFrame(stock1_norm).rolling(window=10).mean()
stock2_ma = pd.DataFrame(stock2_norm).rolling(window=10).mean()

# Calculate the returns of both stocks over the time period
stock1_return = (stock1_hist["Close"][-1] - stock1_hist["Close"][0]) / stock1_hist["Close"][0] * 100
stock2_return = (stock2_hist["Close"][-1] - stock2_hist["Close"][0]) / stock2_hist["Close"][0] * 100

# Print the returns of both stocks
print(get_ticker_name(tickr1) + " return: " + str(round(stock1_return, 2)) + "%")
print(get_ticker_name(tickr2) + " return: " + str(round(stock2_return, 2)) + "%")

# Plot the normalized historical data and moving averages
#plt.plot(stock1_hist.index, stock1_norm, label=tickr1)
#plt.plot(stock2_hist.index, stock2_norm, label=tickr2)
plt.plot(stock1_hist.index, stock1_ma, label=get_ticker_name(tickr1) + " 20-day MA")
plt.plot(stock2_hist.index, stock2_ma, label=get_ticker_name(tickr2) + " 20-day MA")
plt.title(get_ticker_name(tickr1) + " and " + get_ticker_name(tickr2) + " Price History")
plt.xlabel("Date")
plt.ylabel("Price (Normalized)")
plt.legend()
plt.show()
