from stockbox.model import Stock, StockData
from stockbox.database import session
from stockbox.scraper import 
"""Initial acquisition of a non-existant ticker symbol
Create will add the Stock model and scrape yf for the 5y default
info
"""


class Create:
    default_range: str = "5y"
    symbol: str

    def __init__(self, symbol: str):
        self.insert_stock_model(symbol.upper())

    def insert_stock_model(self, symbol: str):
        stock = Stock(symbol=symbol)
        session.add(stock)
        session.commit()

    def scrape_yf(self):
        
