from .yf import YahooFinance
from stockbox.range import Range


class Scraper:
    """
    Scraper class will control external scraping requests

    """

    def history(
        self,
        symbol: str,
        range: str,
        interval: str = "1d",
    ):
        """[summary]

        Args:
            symbol (str): [description]
            range (str): [description]
            interval (str, optional): [description]. Defaults to "1d".

        Returns:
            [dataframe]: returns a dataframe based on the provided
                         attrs
        """
        r = Range(range).generate_range()
        return YahooFinance().history(
            {
                "symbol": symbol,
                "date_from": r["start"],
                "date_to": r["end"],
                "interval": interval,
            }
        )
