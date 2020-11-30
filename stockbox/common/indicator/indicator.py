from stockbox.common.helpers import column_index


class Indicator:

    name: str
    range: int
    range_two: int
    colkey: int

    def __init__(self, dataframe, range=None):
        self.df = dataframe
        self.range = range
        self.set_header_name()
        self.colkey = column_index(self.df, ["Adj Close"])

    def set_header_name(self):
        if self.range:
            self.name = f"{self.name}({self.range})"

    def process(self):
        return self.perform_calculation()

    def perform_calculation(self):
        pass
