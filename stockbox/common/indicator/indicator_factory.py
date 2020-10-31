import re
from .relative_strength_index import RelativeStrengthIndex
from .simple_moving_average import SimpleMovingAverage
from .slow_stochastic import SlowStochastic
from .exponential_moving_average import ExponentialMovingAverage
from .slope import Slope


class IndicatorFactory:

    tag: str

    re_range = r"(.*)\(([0-9]+)\)"

    def __init__(self, indicator_tag, Ticker):
        self.tag = indicator_tag
        self.Ticker = Ticker

    def process(self):
        """Get the key and range from the provided tag, use those values
        to create the Indicator w/ switch()

        Returns:
            []: [description]
        """
        found = re.match(self.re_range, self.tag)
        if found:
            indicator_key = found.group(1).strip().lower()
            indicator_range = int(found.group(2).strip())
            return self.switch(indicator_key, indicator_range).process()

    def switch(self, key: str, range: int):
        """switch to create and return the proper indicator object

        Args:
            key (str):
            range (int): [description]

        Returns:
            [type]: [description]
        """
        switcher = {
            "sma": SimpleMovingAverage,
            "slosto": SlowStochastic,
            "slowsto": SlowStochastic,
            "rsi": RelativeStrengthIndex,
            "ema": ExponentialMovingAverage,
            "slope": Slope,
        }
        func = switcher.get(key)
        if func:
            return func(self.Ticker.history().copy(), range)
        else:
            print(f"Provided indicator key not found: {key}")
            print("Valid keys: ", switcher.keys())
            exit()

    @staticmethod
    def create(indicator_tag, Ticker):
        """Static method to create the indicator and return the history

        Args:
            indicator_tag (str): [description]
            Ticker (Ticker): [description]

        Returns:
            [type]: [description]
        """
        return IndicatorFactory(indicator_tag, Ticker).process()
