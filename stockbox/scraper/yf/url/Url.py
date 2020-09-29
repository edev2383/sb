import datetime
import time


class Url:

    incoming: dict = {}
    params: dict = {}
    url: str = ""
    base_url: str = "https://query1.finance.yahoo.com/v7/finance/download/"
    # url: str = "https://finance.yahoo.com/quote/"

    def __init__(self, params):
        self.incoming = params
        self.parse()

    def parse(self):
        # self.convert_timestamps()
        self.set_time_periods()
        self.set_symbol()
        self.set_interval()
        self.set_params()

    def set_params(self):

        print(self.incoming)
        self.url = (
            self.url
            + "period1="
            + self.params["period1"]
            + "&period2="
            + self.params["period2"]
            + "&interval="
            + self.incoming["interval"]
            + "&events="
            + self.incoming["filter"]
        )

    def set_time_periods(self):
        self.params["period2"] = str(self.incoming["date_to"])
        self.params["period1"] = str(self.incoming["date_from"])

    def set_interval(self):
        self.params["interval"] = self.incoming["interval"]

    def set_symbol(self):
        self.url = self.base_url + self.incoming["symbol"] + "?"

    def convert_timestamps(self):
        self.convert_to_date()
        self.convert_from_date()

    def convert_to_date(self):
        self.params["period2"] = self.convert_date(self.incoming["date_to"])

    def convert_from_date(self):
        self.params["period1"] = self.convert_date(self.incoming["date_from"])

    def convert_date(self, date):
        b = date.split("-")
        t = datetime.datetime(int(b[0]), int(b[1]), int(b[2]), 0, 0)
        return str(int(time.mktime(t.timetuple())))


#
# incoming:params
# {
#   symbol: str
#   date_from: str
#   date_to: str
#   interval: str
#   filter: str
# }
#
# https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1563505862&period2=1595128262&interval=1mo&events=history
#
#
# Interval: 1d 1wk 1mo
#
#
#
