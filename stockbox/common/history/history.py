# import stockbox.model as model
import pandas as pd
import datetime
from stockbox.common.range import Range
from stockbox.common.acquire import Acquire


class History:
    """
    History acquires, updates and returns the Ticker.history data frame


    Attributes
    ----------
    symbol: str
        supplied ticket symbol
    range: str
        supplied key for


    Methods
    -------
    load()
        access method to initiate acquisition of model data
    acquire()
        loads StockData model
    """

    symbol: str
    range: str

    def __init__(self, symbol: str, range: str = "1y"):
        self.symbol = symbol.upper()
        self.range = range

    def load(self):
        # check Stock model for exists
        #   - no    - scrape yf for 5y data
        #   - yes   - check last date of StockData model
        #           - is current?
        #               - no    - scrape yf for date range between today
        #                         and last existing dp
        #               - yes   - return the model as dataFrame
        #
        #
        #
        print(f" - History - calling Acquire - {self.symbol} - {self.range}")
        history = Acquire(self.symbol, self.range).process()
        return self.format_history(history)

    def format_history(self, df):
        df = self.adddelta(df)
        df = self.addpercent_d(df)
        df = self.converttodatetime(df)
        return df[::-1]

    def adddelta(self, df):
        df["Delta"] = round(df["Open"] - df["Adj Close"], 2)
        return df

    def addpercent_d(self, df):
        df["% Delta"] = round(df["Delta"] / df["Open"], 2)
        return df

    def converttodatetime(self, df):
        df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
        return df
