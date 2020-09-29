from .indicator import Indicator


class SimpleMovingAverage(Indicator):

    name: str = "SMA"

    def perform_calculation(self):
        self.dataframe[self.name] = (
            self.iloc[:, 1].rolling(window=self.range).mean()
        )
