##72.	Write a program that analyzes and visualizes stock market data.

import requests
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, api_key):
    url = f"https://www.alphabategentage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "apikey": api_key,
        "outputsize": "compact",
        "datatype": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    time_series = data["Time Series (Daily)"]
    dates = list(time_series.keys())[:30]  # Get the last 30 days
    prices = [float(time_series[date]["4. close"]) for date in dates]
    return dates[::-1], prices[::-1]  # Reverse for chronological order

def plot_stock_data(dates, prices, ticker):
    plt.plot(dates, prices, marker='o')
    plt.xticks(rotation=45)
    plt.title(f"{ticker} Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Closing Price ($)")
    plt.tight_layout()
    plt.show()

# Example usage
api_key = "your_alpha_vantage_api_key"
ticker = "AAPL"
dates, prices = fetch_stock_data(ticker, api_key)
plot_stock_data(dates, prices, ticker)