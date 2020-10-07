import pandas as pd
import math
from datetime import datetime
from sqlalchemy import desc
from stockbox.common.market import Market
from stockbox.common.create import Create
from stockbox.common.database import session
from stockbox.common.model import StockData
from stockbox.common.scraper import Scraper


class Update:
    """Receives a dataframe, compares max date to current date, if date
    is not current, perform a scrape request. We purposefully scrape 1m
    which `should` be more than we need, so we can drop any values that
    are <= the last existing date record

    TODO - need to perform a date comp and not scrape on same day as
           last record date and/or if the market is closed, ie weekend
    """

    cache_dataframe = None
    return_dataframe = None
    update_range = "1m"

    def __init__(self, dataframe, symbol, stock_id, range):
        self.cache_dataframe = dataframe
        self.symbol = symbol
        self.stock_id = stock_id
        self.range = range
        if Market.is_open():
            print(" - Update - Market is open. Returning current dataframe.")
            self.return_dataframe = self.cache_dataframe
        else:
            last_entry = self.get_last_entry_date(dataframe)
            self.get_diff(dataframe, last_entry)

    def get_last_entry_date(self, dataframe):
        if dataframe.empty:
            return None
        return pd.Series(dataframe["Date"]).max()

    def get_diff(self, tmp_dataframe, last_entry_date):
        """Scrape history back `update_range`, then filter the scraped
        data. If scraped is empty after filtering, return the provided
        and cached dataframe, else add the stock_id to the scraped
        dataframe, store it to the database and then re-request the
        StockData model

        Args:
            tmp_dataframe (df): [description]
            last_entry_date (date): [description]
        """
        print(
            f" - Update - scraping history {self.symbol} - {self.update_range}"
        )
        scraped = Scraper().history(self.symbol, self.update_range)
        scraped.rename(columns={"Adj Close": "Adj_Close"}, inplace=True)

        if last_entry_date is not None:
            print(" - Update - filtering scraped results...")
            scraped = scraped.round(2)[
                scraped.Date > last_entry_date.strftime("%Y-%m-%d")
            ]
        if scraped.empty:
            print(" - Update - no new values found, returning original data")
            self.return_dataframe = self.cache_dataframe
        else:
            print(" - Update - new values filtered and storing to DB")
            scraped["stock_id"] = self.stock_id
            self.store_new_stock_data_model(scraped)
            self.return_dataframe = self.get_stock_model_data()

    def get_stock_model_data(self):
        """Get StockData model, identical implementation to same Acquire
        method

        Returns:
            dataframe: StockData history
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

    def store_new_stock_data_model(self, new_dataframe):
        """[summary]

        Args:
            new_dataframe (df): newly scraped dataframe to be inserted
        """
        Create(self.symbol).commit_stock_data_model(new_dataframe)

    def process(self):
        """simple return method for now

        Returns:
            dataframe:
        """
        return self.return_dataframe
