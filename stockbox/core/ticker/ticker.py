from stockbox.common.history import History
from stockbox.common.indicator.indicator_factory import IndicatorFactory
import traceback


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

    data = None
    indicators = None
    symbol = ""
    range = ""

    # ! NEW @ 10/11/2020
    __state: str = "standard"  # "primed", "held"
    valid_state: list = ["standard", "primed", "held"]

    def __init__(self, symbol: str, range: str = "1y"):
        self.symbol = symbol.upper()
        self.range = range
        self.data = self.create_history().load()
        self.set_default_indicators()
        # print("Indicators ] ------------------------------")
        # print(self.data)
        print("- ------------------------------------------[End Ticker]-")
        print(" ")

    def create_history(self):
        print(" ")
        print("- ------------------------------------------[Begin Ticker]-")
        print(f"- Ticker - create history {self.symbol} - {self.range}")
        return History(self.symbol, self.range)

    def history(self):
        return self.data

    def set_default_indicators(self):
        print("- Ticker - appending default indicators")
        # self.data = IndicatorFactory.create("EMA(4)", self)
        # self.data = IndicatorFactory.create("SMA(10)", self)
        # self.data = IndicatorFactory.create("SMA(20)", self)
        # self.data = IndicatorFactory.create("SMA(50)", self)
        # self.data = IndicatorFactory.create("SMA(200)", self)
        # self.data = IndicatorFactory.create("SloSto(14)", self)
        # self.data = IndicatorFactory.create("RSI(14)", self)
        # self.data = ind.SimpleMovingAverage(self.data.copy(), 10).process()
        # self.data = ind.SimpleMovingAverage(self.data.copy(), 20).process()
        # self.data = ind.RelativeStrengthIndex(self.data.copy(), 14).process()
        # self.data = ind.SlowStochastic(self.data.copy(), 14).process()

    def add_indicator(self, key):
        self.data = IndicatorFactory.create(key, self)

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
