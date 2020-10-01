from .request import Request


class YahooFinance:
    """
    Class controls scrape requests to yahoofinance.com
    """

    def history(self, params: dict):
        """
        Simple history requests

        Args:
            params (dict):
                            'symbol': ticker simple, ex: "MSFT"
                            'date_from': timestamp, ex 1567788900
                            'date_to': timestamp
                            'interval': 1d, 1w, 1m, etc
                            -- currently only supporting `1d` intervals

        Returns:
            [dataframe]: Request.process returns a dataframe from
                         scraped csv
        """
        return Request().process("history", params)
