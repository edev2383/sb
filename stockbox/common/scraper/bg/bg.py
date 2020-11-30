import numpy as np
import pandas as pd
from stockbox.common.log import Log
from lxml import html
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from .url import Url


class BG:

    scrape_xpath: str = "//tbody/tr/td/text()"

    def request_current(self, symbols: list):
        self.symbol_count = len(symbols)
        requrl = Url(symbols).url()
        # Log.info(f"bg - {requrl}")
        try:
            req = Request(requrl, headers={"User-Agent": "Mozilla/5.0"})
            page = urlopen(req).read()
            self.tree = html.fromstring(page)
            raw = self.tree.xpath(self.scrape_xpath)
            Log.info(f"bg - {raw[0]}")

            return self.format_results(raw)
        except HTTPError as e:
            Log.debug(e.code)
            Log.debug(e.read())

    def format_results(self, result: list):
        return self.create_df(self.filter_results(result))

    def filter_results(self, result: list):
        return np.array([i.strip() for i in result if "  " not in i])

    def create_df(self, nparr):
        print("create_df: ", nparr)
        breakarr = np.split(nparr, self.symbol_count)
        cols = [
            "Symbol",
            "Close",
            "Change",
            "% Change",
            "High",
            "Low",
            "Volume",
            "Time",
        ]
        return self.clean_df(pd.DataFrame(data=breakarr, columns=cols))

    def clean_df(self, df):
        df = df.drop(columns=["Time"])
        df["Date"] = pd.to_datetime("today").strftime("%Y-%m-%d")
        df["Date_Index"] = pd.to_datetime("today").strftime("%Y-%m-%d")
        df["Volume"] = df["Volume"].apply(lambda x: int(x.replace(",", "")))
        df["Close"] = df["Close"].apply(lambda x: float(x.replace(",", "")))
        df["High"] = df["High"].apply(lambda x: float(x.replace(",", "")))
        df["Low"] = df["Low"].apply(lambda x: float(x.replace(",", "")))
        df["Change"] = df["Change"].apply(self.__validate_change)
        df["Open"] = df["Close"] - df["Change"]
        df["Adj Close"] = df["Close"]
        df = df.set_index(["Date_Index"])
        return df

    def __validate_change(self, value):
        if value == "UNCH":
            return float(0)
        return float(value.replace(",", ""))
