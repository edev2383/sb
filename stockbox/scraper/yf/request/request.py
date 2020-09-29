from ..url import Url
from urllib.request import Request as Req, urlopen
import pandas as pd
import numpy as np
import csv
from stockbox.indicator import Timestamp


class Request:

    history: list = []

    # `switch` style method to route requests
    def process(self, type, params):
        if type == "history":
            params["filter"] = type
            return self.request_history(params)

    def request_history(self, params):
        url = Url(params).url
        page = urlopen(url).read().decode("utf-8")
        return Timestamp(pd.read_csv(urlopen(url))).process()
