from .indicator import Indicator
from stockbox.helpers import rsi


class RelativeStrengthIndex(Indicator):
    """[summary]

    Args:
        Indicator ([type]): [description]
    """

    name: str = "RSI"

    def perform_calculation(self):
        self.df[self.name] = self.calc_rsi()
        return self.df

    def calc_rsi(self):
        df = self.df[::-1]
        xrsi = (
            df["Adj_Close"].rolling(center=False, window=self.range).apply(rsi)
        )
        return xrsi[::-1].fillna(0)
