from .indicator import Indicator
import pandas as pd
import datetime


class Timestamp(Indicator):
    name: str = "Timestamp"
    range_one: int = 1
    range_two: int = 0

    def perform_calculation(self):

        self.dataframe[self.name] = int(
            datetime.datetime.timestamp(
                pd.to_datetime(self.dataframe["Date"], format="%Y-%m-%d"),
            )
        )

        return self.dataframe
