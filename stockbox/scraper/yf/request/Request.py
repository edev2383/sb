from ..yf.url.Url import Url
from urllib.request import Request as Req, urlopen
import pandas as pd
import numpy as np
import csv


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
        data = np.array(self.parse_csv_to_array(page))
        return pd.DataFrame(data=data[1:, 1:], index=data[1:, 0], columns=data[0, 1:])

    # TODO - remove this to a library helper function
    # Breaks csv string into array to be pushed into a dataframe
    def parse_csv_to_array(self, csv):
        c = []
        tmp_array = csv.split("\n")
        for row in tmp_array:
            c.append(row.split(","))
        return c
