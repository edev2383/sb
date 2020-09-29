from lxml import html
from urllib.request import Request, urlopen
from .reader.Reader import Reader


class FinViz:

    filters: list = []
    filter_string: str

    def __init__(self, filters: list):
        self.filters = filters
        self.process_filters()

    def process_filters(self):
        tmp_string: str = ""
        for flt in self.filters:
            tmp_string = tmp_string + flt.get_filter_string() + ","
        self.filter_string = tmp_string

    def run(self):
        return Reader(self.filter_string).run()


# URL COMPONENTS
# base: https://finviz.com/screener.ashx?v=111&
# filters: f=[filterprefix_value],[]

# Filters to start for POC
# Selector  | Filter Prefix         |
# fs_       - fa_epsqoq             - Earnings Per Share Q-Over-Quarter
# fs_       - sh_short              - Float Short Percentage
# fs_       - sh_price              - Share Price
# fs_       - sh_curvol             - Current Volume
# fs_       - ind                   - Industry
# fs_       - cap                   - Market Cap
# fs_       - sh_avgvol             - Average Volume
#           - fa_salesqoq           - Sales Growth Quarter Over Quarter
#           - sh_insidertrans       - Insider Transactions
#           - sh_insderown          - Insider Ownership
#           - sh_instown            - Institutional Ownership
#           - sh_insttrans          - Institutional Transactions
#           - ta_averagetruerange   - Average True Range
#           - ta_highlow52w         - 52-Week High/Low
#           - ta_rsi                - RSI (14)
#
