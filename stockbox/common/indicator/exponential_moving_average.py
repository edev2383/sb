from .indicator import Indicator


class ExponentialMovingAverage(Indicator):

    name: str = "EMA"

    # ema = Price(t) * k + EMA(y) * (1 - k)
    # t = today
    # y = yesterday
    # k = weight
    #

    def perform_calculation(self):

        self.df = self.df.iloc[::-1]
        self.df[self.name] = (
            self.df.iloc[:, self.colkey].ewm(span=self.range).mean()
        )
        return self.df.iloc[::-1].fillna(0)

    def get_weight(self):
        return 2 / (self.range + 1)
