from stockbox.model import Stock, StockData
from stockbox.database import session
from stockbox.scraper import Scraper
from stockbox.database import engine

"""Initial acquisition of a non-existant ticker symbol
Create will add the Stock model and scrape yf for the 5y default
info
"""


class Create:
    default_range: str = "1w"
    symbol: str
    stock_id: int

    def __init__(self, symbol: str):
        self.stock_id = self.insert_stock_model(symbol.upper())
        self.insert_stock_data_model(symbol.upper())

    def insert_stock_data_model(self, symbol: str):
        history = self.add_stock_id_to_dataframe(self.scrape_yf(symbol))
        print("history pre-insert, pre-drop", history)
        history = history.drop(columns=["Adj Close"])
        print("history pre-insert, post-drop", history)
        history.to_sql("StockData", con=engine, if_exists="append", index=False)

    def insert_stock_model(self, symbol: str):
        exists = self.stock_model_exists(symbol)
        if not exists:
            stock = self.commit_stock_model(symbol)
            return stock.id
        else:
            return exists.id

    def commit_stock_model(self, symbol):
        stock = Stock(symbol=symbol)
        session.add(stock)
        session.commit()
        session.refresh(stock)
        return stock

    def scrape_yf(self, symbol: str):
        return Scraper().history(symbol, self.default_range)

    def stock_model_exists(self, symbol):
        return session.query(Stock).filter(Stock.symbol == symbol).first()

    def add_stock_id_to_dataframe(self, df):
        df["stock_id"] = self.stock_id
        return df

    # def get_stock_id(self, symbol):
