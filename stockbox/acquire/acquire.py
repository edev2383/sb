from stockbox.model import Stock, StockData, StockIndicator, StockIndicatorData
from stockbox.database import session


class Acquire:
    """[summary]"""

    range: dict
    symbol: str
    data: list

    default_scrape_range_key: str = "5y"

    def __init__(self, symbol, range: dict):
        self.range = range
        self.symbol = symbol.upper()
        if not self.stock_model_exists():
            print("it doesnt exist mother fucker")
        else:
            print("we found it bitches")

    def stock_model_exists(self):
        return session.query(Stock).filter(Stock.symbol == self.symbol).first()


#
#
# check if the stock exists
#   yes - get the id, and get StockData by the id
#   no  - insert it
#       - scrape yf for 5 years of data
#
#
#
#
#
#
