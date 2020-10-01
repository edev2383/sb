import numpy as np
from datetime import datetime
import pandas as pd
from sqlalchemy import desc
from stockbox.model import Stock, StockData, StockIndicator, StockIndicatorData
from stockbox.database import session
from stockbox.create import Create
from stockbox.update import Update


class Acquire:
    """
    Given a stock ticker symbol and a dictionary of range timestamps
    return stock history for that start-end range

    If the data does not already exist in the database, use the Create
    class to scrape it from yahoofinance (Scraper) and insert it into
    the database, before returning it.

    Final returned data, [process method], is then updated, with Update
    class
    """

    range: dict
    symbol: str
    stock_id: int

    def __init__(self, symbol, range: dict):
        self.range = range
        self.symbol = symbol.upper()

    def process(self):
        """
        Return stock data from the StockData model. Update performs
        additional update checks to make sure the existing record is
        current. If not, it scrapes back `1m` and updates the database

        Returns:
            [dataframe]: StockData model
        """
        self.stock_id = self.get_stock_model()
        return Update(
            self.get_stock_data_model(), self.symbol, self.stock_id, self.range
        ).process()

    def get_stock_model(self):
        """
        Checks for Stock model by self.symbol to exist. Sets it's value
        to stock and returns stock.id. If it does not exist, it creates
        it and then calls self and returns the stock.id

        Returns:
            [int]: Stock.id - used to get the StockData model
        """
        stock = self.stock_model_exists()
        if not stock:
            Create(self.symbol).process()
            stock = self.stock_model_exists()
        return stock.id

    def stock_model_exists(self):
        """
        returns the Stock model by self.symbol

        Returns:
            Stock: model data (only real interest is `id` prop)
        """
        return session.query(Stock).filter(Stock.symbol == self.symbol).first()

    def get_stock_data_model(self):
        """
        Get the StockData model by self.symbol and the provided range
        range values get convered to date stamps 'YYYY-MM-DD' format

        Returns:
            dataframe: requested StockData
        """
        start = datetime.fromtimestamp(self.range["start"]).date()
        end = datetime.fromtimestamp(self.range["end"]).date()
        return pd.read_sql(
            session.query(StockData)
            .filter(StockData.stock_id == self.stock_id)
            .filter(StockData.Date >= start)
            .filter(StockData.Date <= end)
            .order_by(desc(StockData.Date))
            .statement,
            session.bind,
        )
