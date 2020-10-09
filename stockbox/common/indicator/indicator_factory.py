import re
from stockbox.core.ticker import Ticker
from .relative_strength_index import RelativeStrengthIndex
from .simple_moving_average import SimpleMovingAverage
from .slow_stochastic import SlowStochastic


class IndicatorFactory:

    tag: str
    Ticker: Ticker

    re_range = r"(.*)\(([0-9]+)\)"

    def __init__(self, indicator_tag, Ticker):
        self.tag = indicator_tag
        self.Ticker = Ticker

    def process(self):
        found = re.match(self.re_range, self.tag)
        if found:
            indicator_key = found.group(1).strip().lower()
            indicator_range = int(found.group(2).strip())
            return self.switch(indicator_key, indicator_range).process()

    def switch(self, key: str, range: int):
        switcher = {
            "sma": SimpleMovingAverage,
            "slosto": SlowStochastic,
            "slowsto": SlowStochastic,
            "rsi": RelativeStrengthIndex,
        }
        func = switcher.get(key)
        return func(self.Ticker.history(), range)

    @staticmethod
    def create(indicator_tag, Ticker):
        return IndicatorFactory(indicator_tag, Ticker).process()
