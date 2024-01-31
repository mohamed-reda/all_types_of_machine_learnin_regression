import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbol and date range
stock_symbol = "AAPL"
start_date = "2022-01-01"
end_date = "2023-01-01"

# Download historical stock data using Yahoo Finance API
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Display the first few rows of the data
print(stock_data.head())

# Plotting the closing prices
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label=f'{stock_symbol} Close Price')
plt.title(f'{stock_symbol} Stock Price Analysis')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.show()

# Calculate daily returns
stock_data['Daily_Return'] = stock_data['Close'].pct_change()

# Plotting the daily returns
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Daily_Return'], label=f'{stock_symbol} Daily Returns')
plt.title(f'{stock_symbol} Daily Returns Analysis')
plt.xlabel('Date')
plt.ylabel('Daily Returns')
plt.legend()
plt.show()

# Basic statistics of the daily returns
print("\nBasic Statistics of Daily Returns:")
print(stock_data['Daily_Return'].describe())

# Cumulative returns
stock_data['Cumulative_Return'] = (1 + stock_data['Daily_Return']).cumprod()

# Plotting the cumulative returns
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Cumulative_Return'], label=f'{stock_symbol} Cumulative Returns')
plt.title(f'{stock_symbol} Cumulative Returns Analysis')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.show()
