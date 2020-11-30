from .indicator import Indicator

# from ..helpers import calc_fprime


class Slope(Indicator):
    name: str = "Slope"

    def perform_calculation(self):
        # TODO - add a check to ensure that there is a matching SMA col
        self.df = self.df.iloc[::-1]
        target = self.df[f"SMA({self.range})"]

        self.df[self.name] = target.rolling(window=2).apply(self.calc_fprime)
        return self.df.iloc[::-1].fillna(0)

    def calc_fprime(self, values):
        """Shortcut indicator to give change in SMA curves

        Args:
            values ([type]): [description]

        Returns:
            [type]: [description]
        """
        # reset_index swaps their order logically
        # what came in as index 9 -> 8, becomes 0 -> 1, so we sub 1 de
        values = values.reset_index()
        slope = values.at[1, 0] - values.at[0, 0]
        if slope > 5:
            return 0
        return slope
