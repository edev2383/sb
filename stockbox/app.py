from stockbox.scraper import Scraper

# from .database.conn import session
# from .model.stock import Stock
# from stockbox.ticker import Ticker


def run():
    # Ticker("BLoop", "1w")
    x = Scraper().history("MSFT", "1w")

    print(x)
