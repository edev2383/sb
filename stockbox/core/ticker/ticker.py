from stockbox.common.history import History
from stockbox.common.indicator.indicator_factory import IndicatorFactory
import pandas as pd


class Ticker:
    """ Ticker """

    #
    # Ticker class:
    #
    # symbol: str = "MSFT"
    # meta = {ath: 52, 52wkHigh: 51, 52wkLow: 24}
    # history: dataframe = [[]]
    # --
    #
    #

    daily = None
    weekly = None
    monthly = None
    indicators = None
    symbol = ""
    range = ""

    # ! NEW @ 10/11/2020
    __state: str = "standard"  # "primed", "held"
    valid_state: list = ["standard", "primed", "held"]

    def __init__(self, symbol: str, range: str = "1y"):
        self.symbol = symbol.upper()
        self.range = range
        self.format_daily_history()
        self.format_weekly_history()
        # self.compress_to_monthly()

    def create_history(self):
        return History(self.symbol, self.range)

    def history(self, term="daily"):
        if term == "weekly":
            return self.weekly
        elif term == "monthly":
            return self.monthly
        return self.daily

    def set_default_indicators(self):
        self.daily = IndicatorFactory.create("SMA(20)", self)
        self.daily = IndicatorFactory.create("SMA(50)", self)
        self.daily = IndicatorFactory.create("SMA(200)", self)
        self.daily = IndicatorFactory.create("SloSto(14)", self)
        self.daily = IndicatorFactory.create("RSI(14)", self)

    def set_default_indicators_weekly(self):
        self.weekly = IndicatorFactory.create("SMA(20)", self, "weekly")
        self.weekly = IndicatorFactory.create("SMA(50)", self, "weekly")
        self.weekly = IndicatorFactory.create("SMA(200)", self, "weekly")
        self.weekly = IndicatorFactory.create("SloSto(14)", self, "weekly")
        self.weekly = IndicatorFactory.create("RSI(14)", self, "weekly")

    def add_indicator(self, key):
        self.daily = IndicatorFactory.create(key, self)

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = self.validate_state(state)

    def validate_state(self, state):
        if state not in self.valid_state:
            print(f"Error: Invalid state received from Setup: {state}")
            print(" - valid state values: ", self.valid_state)
        return state

    def format_daily_history(self):
        self.daily = self.create_history().load()
        self.set_default_indicators()

    def format_weekly_history(self):
        self.weekly = self.compress_to_weekly()
        self.set_default_indicators_weekly()

    def compress_to_weekly(self):
        df_clone = self.daily[::-1].copy()
        df_clone["Week_Number"] = df_clone.loc[:, "Date"].dt.isocalendar().week
        df_clone["Year"] = df_clone["Date"].dt.year
        df_clone = df_clone.groupby(["Year", "Week_Number"]).agg(
            {
                "Date": "first",
                "High": "max",
                "Low": "min",
                "Open": "first",
                "Close": "last",
                "Adj Close": "last",
                "Volume": "sum",
            }
        )
        df_clone["Date_Index"] = df_clone["Date"]
        df_clone.set_index("Date_Index", inplace=True)
        return df_clone[::-1]

    def addrecord(self, df_window):
        df = pd.concat([df_window, self.daily[:]])
        df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
        df["Date_Index"] = df["Date"]
        df = df.set_index(["Date_Index"])
        self.daily = df[
            [
                "High",
                "Low",
                "Open",
                "Close",
                "Adj Close",
                "Volume",
                "Change",
                "Change %",
            ]
        ]
        self.set_default_indicators()
