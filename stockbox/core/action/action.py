from stockbox.common.log import Log


class Action:

    name: str
    # the data from the day that triggered the action
    window: dict
    # the Setup class to alter
    Setup = None
    Backtest = None

    def __init__(self, name):
        self.name = name

    def process(self):
        pass

    def set_window(self, window):
        self.window = window

    def set_setup(self, Setup):
        self.Setup = Setup

    def set_backtest(self, Backtest):
        self.Backtest = Backtest

    def set_tickerstate(self, state):
        self.Setup.set_tickerstate(state)
