from stockbox.history import History
import stockbox.indicator as ind
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
    #
    #
    #
    #
    #
    #
    data = None
    indicators = None
    symbol = ""
    range = ""

    def __init__(self, symbol: str, range: str = "1y"):
        self.symbol = symbol.upper()
        self.range = range
        self.data = self.create_history().load()
        self.set_default_indicators()
        # print("Indicators ] ------------------------------")
        # print(self.data)
        print(f"- ------------------------------------------[End Ticker]-")
        print(f" ")

    def create_history(self):
        print(f" ")
        print(f"- ------------------------------------------[Begin Ticker]-")
        print(f"- Ticker - create history {self.symbol} - {self.range}")
        return History(self.symbol, self.range)

    def history(self):
        return self.data

    def set_default_indicators(self):
        print(f"- Ticker - appending default indicators")
        self.data = ind.SimpleMovingAverage(self.data.copy(), 10).process()
        self.data = ind.SimpleMovingAverage(self.data.copy(), 20).process()
        self.data = ind.RelativeStrengthIndex(self.data.copy(), 14).process()
        self.data = ind.SlowStochastic(self.data.copy(), 14).process()