# import stockbox.model as model
from stockbox.range import Range
from stockbox.acquire import Acquire


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
        self.range = Range(range.lower()).generate_range()

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
        return Acquire(self.symbol, self.range).process()
