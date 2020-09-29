from .indicator import Indicator
import datetime


class Timestamp(Indicator):
    name: str = "Timestamp"
    range_one: int = 1
    range_two: int = 0

    def perform_calculation(self):

        self.dataframe[self.name] = int(
            datetime.datetime.timestamp(
                datetime.datetime.combine(
                    datetime.date(self.dataframe["Date"]), datetime.time(22, 0)
                )
            )
        )

        return self.dataframe
