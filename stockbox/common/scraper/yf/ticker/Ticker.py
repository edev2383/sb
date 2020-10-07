import time
from src.yF.Request.Request import Request


class Ticker:

    symbol: str
    valid_ranges: list = ["1d", "1wk", "1mo", "3mo", "1y", "2y", "5y"]
    valid_intervals: list = ["1d", "1wk", "1mo"]
    time_ranges: dict = {
        "1d": 3600 * 24,
        "1wk": 3600 * 24 * 7,
        "1mo": 3600 * 24 * 30,
        "3mo": 3600 * 24 * 90,
        "1y": 3600 * 24 * 365,
        "2y": 3600 * 24 * 365 * 2,
        "5y": 3600 * 24 * 365 * 5,
    }

    def __init__(self, symbol: str):
        self.symbol = symbol

    def history(self, range="3mo", interval="1d", start=False, end=False):
        self.validate_range(range)
        self.validate_interval(interval)
        self.set_end(end)
        self.set_start(start)
        return self.request("history", self.build_request_params())

    def request(self, type: str, request_params: dict):
        print("Supplied paramenters: ")
        print(request_params)
        print("---------------------------------------------")
        return Request().process(type, request_params)

    def build_request_params(self):
        return {
            "symbol": self.symbol,
            "date_from": self.start,
            "date_to": self.end,
            "interval": self.interval,
        }

    def set_start(self, start):
        if start is False:
            start = self.end - self.time_ranges[self.range]
        self.start = int(start)

    def set_end(self, end):
        if end is False:
            end = self.set_end_to_default()
        self.end = int(end)

    def set_end_to_default(self):
        return time.time()

    def validate_interval(self, interval):
        if interval in self.valid_intervals:
            self.interval = interval
            return True
        print("Error: Invalid interval supplied.")
        print("__________ Currently available intervals ______________")
        print(self.valid_intervals)
        exit()

    def validate_range(self, range):
        if range in self.valid_ranges:
            self.range = range
            return True
        print("Error: Invalid range supplied.")
        print("__________ Currently available ranges ______________")
        print(self.valid_ranges)
        exit()
