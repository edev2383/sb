from ..url import Url
from urllib.request import Request as Req, urlopen
import pandas as pd


class Request:
    """Container class for different scraping requests

    Returns:
        [type]: [description]
    """

    history: list = []

    # `switch` style method to route requests
    def process(self, type, params):
        """switch style method to route requests, currently only history
        is the only supported `type`

        Args:
            type ([type]): [description]
            params ([type]): see YahooFinance

        Returns:
            [dataframe]: raw scraped stock data by reqested range
        """
        if type == "history":
            params["filter"] = type
            return self.request_history(params)
        else:
            print(f"Request `type` unrecognized. {type} provided.")

    def request_history(self, params):
        """[summary]

        Args:
            params ([type]): see YahooFinance

        Returns:
            [dataframe]: raw scraped stock data by reqested range
        """
        url = Url(params).url
        page = urlopen(url).read().decode("utf-8")
        return pd.read_csv(urlopen(url))
