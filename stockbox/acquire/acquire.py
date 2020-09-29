import numpy as np
import pandas as pd
from stockbox.model import Stock, StockData, StockIndicator, StockIndicatorData
from stockbox.database import session
from .create import Create


class Acquire:
    """[summary]"""

    range: dict
    symbol: str
    data: list

    stock_id: int
    stock_data: list

    default_scrape_range_key: str = "5y"

    def __init__(self, symbol, range: dict):
        self.range = range
        self.symbol = symbol.upper()
        self.process()

    def process(self):
        self.stock_id = self.get_stock_model()
        self.stock_data = self.get_stock_data_model()
        print(f"stock.id: ", self.stock_id)
        print(f"stock.data: __________________________________")
        print(self.stock_data)

    def get_stock_model(self):
        stock = self.stock_model_exists()
        if not stock:
            Create(self.symbol)
            stock = self.stock_model_exists()
        return stock.id

    def stock_model_exists(self):
        return session.query(Stock).filter(Stock.symbol == self.symbol).first()

    def get_stock_data_model(self):
        return pd.read_sql(
            session.query(StockData)
            .filter(StockData.stock_id == self.stock_id)
            .statement,
            session.bind,
        )


# #
# #
# # check if the stock exists
# #   yes - get the id, and get StockData by the id
# #   no  - insert it
# #       - scrape yf for 5 years of data
# #
# #
# #
# #
# #
# #
