from stockbox.scraper import Scraper

# from .database.conn import session
# from .model.stock import Stock
from stockbox.ticker import Ticker


def run():
    Ticker("GOOG")
    Ticker("MSFT")
    Ticker("AMD")
    Ticker("GLW")
    Ticker("CORT")
    # print(x.history().head())
