from stockbox.scraper import Scraper

# from .database.conn import session
# from .model.stock import Stock
from stockbox.ticker import Ticker


def run():
    x = Ticker("GOOG", "1w")
    print(x.history())
