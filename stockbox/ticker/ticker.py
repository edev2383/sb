from stockbox.history import History


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
    def __init__(self, symbol: str, range: str = "1y"):
        self.symbol = symbol.upper()
        self.range = range
        self.history = self.create_history().load()
        print(self.history)

    def create_history(self):
        return History(self.symbol, self.range)
