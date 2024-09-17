def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    return data['Close'][0]  # Get the closing price

def track_performance(portfolio):
    performance = {}
    for symbol, quantity in portfolio.items():
        current_price = get_stock_price(symbol)
        performance[symbol] = current_price * quantity
    return performance

# Example usage
performance = track_performance(portfolio.get_portfolio())
print(performance)
