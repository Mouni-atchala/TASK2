import yfinance as yf

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")  # Get the latest day's data
    return data

# Example usage
print(get_stock_data("AAPL"))
