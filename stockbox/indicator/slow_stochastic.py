from .indicator import Indicator


class SlowStochastic(Indicator):
    """[summary]

    Args:
        Indicator ([type]): [description]
    """

    name: str = "SloSto"

    def perform_calculation(self):
        return self.calc_stochastic()

    def calc_stochastic(self):
        df = self.df.copy()
        df = df[::-1]
        low_min = df["Low"].rolling(window=self.range).min()
        high_max = df["High"].rolling(window=self.range).max()

        df[self.name] = 100 * (
            (df["Adj_Close"] - low_min) / (high_max - low_min)
        )
        df[self.name] = df[self.name].rolling(window=3).mean()
        return df[::-1].fillna(0)
