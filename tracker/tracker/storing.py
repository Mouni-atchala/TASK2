import sqlite3

conn = sqlite3.connect('portfolio.db')
c = conn.cursor()

# Create a table for portfolios
c.execute('''CREATE TABLE IF NOT EXISTS portfolio
             (symbol TEXT, quantity INTEGER)''')

def save_to_db(symbol, quantity):
    c.execute("INSERT INTO portfolio (symbol, quantity) VALUES (?, ?)", (symbol, quantity))
    conn.commit()

# Save an example stock
save_to_db("AAPL", 10)
