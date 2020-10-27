from .indicator import Indicator


class RelativeStrengthIndex(Indicator):
    """[summary]

    Args:
        Indicator ([type]): [description]
    """

    name: str = "RSI"

    def perform_calculation(self):
        colkey = "Adj Close"
        self.df = self.df[::-1]
        if "Adj_Close" in self.df.columns:
            colkey = "Adj_Close"
        self.df[self.name] = self.calc_rsi(self.df[colkey]).fillna(0)
        return self.df[::-1]

    def calc_rsi(self, data, time_window=14):
        diff = data.diff(1).dropna()  # diff in one field(one day)

        # this preservers dimensions off diff values
        up_chg = 0 * diff
        down_chg = 0 * diff

        # up change is equal to the positive difference,
        # otherwise equal to zero
        up_chg[diff > 0] = diff[diff > 0]

        # down change is equal to negative deifference, otherwise equal
        # to zero
        down_chg[diff < 0] = diff[diff < 0]

        # we set com=time_window-1 so we get decay alpha=1/time_window
        up_chg_avg = up_chg.ewm(
            com=time_window - 1, min_periods=time_window
        ).mean()
        down_chg_avg = down_chg.ewm(
            com=time_window - 1, min_periods=time_window
        ).mean()

        rs = abs(up_chg_avg / down_chg_avg)
        rsi = 100 - 100 / (1 + rs)
        return rsi
