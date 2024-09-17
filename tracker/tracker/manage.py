class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] += quantity
        else:
            self.stocks[symbol] = quantity
        print(f"Added {quantity} of {symbol} to the portfolio.")

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks and self.stocks[symbol] >= quantity:
            self.stocks[symbol] -= quantity
            if self.stocks[symbol] == 0:
                del self.stocks[symbol]
            print(f"Removed {quantity} of {symbol} from the portfolio.")
        else:
            print("Not enough shares to remove or stock not in portfolio.")

    def get_portfolio(self):
        return self.stocks

# Example usage
portfolio = Portfolio()
portfolio.add_stock("AAPL", 10)
portfolio.add_stock("GOOGL", 5)
portfolio.remove_stock("AAPL", 2)
print(portfolio.get_portfolio())
