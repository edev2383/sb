from stockbox.core.ticker import Ticker
from stockbox.common.scraper import Scraper
from stockbox.common.market import Market


class Records:
    """Uses Scraper to pull current historical data and pointed intra-
    day info and then merges them into working dataframes. This may not
    be strictly necessary because yF may include all info for intraday
    data, but that is unknown at the moment. It will still be useful
    when gathering data saved on the server, rather than scraping in
    real time
    """

    collection: list = []
    intraday: list = []

    def __init__(self, symbols: list):
        self.symbols = symbols
        self.get_symbol_histories()
        if Market().is_open():
            self.get_symbol_intraday()
            self.merge_collections()

    def get_symbol_intraday(self):
        """Scrape current information using bigcharts.marketwatch.com
        and set to intraday
        """
        self.intraday = Scraper().current(self.symbols)

    def get_symbol_histories(self):
        """Create Ticker references based on provided symbols and store
        them to the collection list
        """
        for s in self.symbols:
            self.collection.append({"symbol": s, "ticker": Ticker(s, "3m")})

    def merge_collections(self):
        """Merge collection dataframe w/ the scraped intraday dataframe"""
        for pair in self.collection:
            symbol = pair["symbol"]
            # extract the slice for the current symbole
            dfslice = self.intraday[self.intraday["Symbol"] == symbol]
            dfslice = dfslice.drop(columns=["Symbol"])
            # Ticker object takes the slice and restructs the history() df
            pair["ticker"].addrecord(dfslice)

    def get(self):
        """
        Returns:
            list: list of dataframes
        """
        return self.collection
