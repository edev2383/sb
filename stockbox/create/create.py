from stockbox.model import Stock, StockData
from stockbox.database import session
from stockbox.scraper import Scraper
from stockbox.database import engine

"""Initial acquisition of a non-existant ticker symbol
Create will add the Stock model and scrape yf for the 5y default
info
"""


class Create:
    default_range: str = "1y"
    symbol: str
    stock_id: int

    def __init__(self, symbol: str):
        self.symbol = symbol.upper()

    def process(self):
        self.stock_id = self.insert_stock_model(self.symbol)
        self.insert_stock_data_model(self.symbol)

    def insert_stock_data_model(self, symbol: str):
        history = self.add_stock_id_to_dataframe(self.scrape_yf(symbol))
        history.rename(columns={"Adj Close": "Adj_Close"}, inplace=True)
        self.commit_stock_data_model(history)

    def commit_stock_data_model(self, dataframe):
        dataframe.to_sql(
            "StockData", con=engine, if_exists="append", index=False
        )

    def insert_stock_model(self, symbol: str):
        exists = self.stock_model_exists(symbol)
        if not exists:
            return self.commit_stock_model(symbol)
        else:
            return exists.id

    def commit_stock_model(self, symbol):
        stock = Stock(symbol=symbol)
        session.add(stock)
        session.commit()
        session.refresh(stock)
        return stock.id

    def scrape_yf(self, symbol: str):
        return Scraper().history(symbol, self.default_range)

    def stock_model_exists(self, symbol):
        return session.query(Stock).filter(Stock.symbol == symbol).first()

    def add_stock_id_to_dataframe(self, df):
        df["stock_id"] = self.stock_id
        return df

    def get_stock_id(self, symbol):
        stock = self.stock_model_exists(symbol)
        return stock.id

    def set_stock_id(self, symbol):
        self.stock_id = self.get_stock_id(symbol)
