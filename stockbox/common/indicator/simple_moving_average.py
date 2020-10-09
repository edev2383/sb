from .indicator import Indicator


class SimpleMovingAverage(Indicator):
    """[summary]

    Args:
        Indicator ([type]): [description]

    Returns:
        [type]: [description]
    """

    name: str = "SMA"

    def perform_calculation(self):
        self.df = self.df.iloc[::-1]

        self.df[self.name] = (
            self.df.iloc[:, self.colkey].rolling(window=self.range).mean()
        )
        return self.df.iloc[::-1].fillna(0)
