from lxml import html
from urllib.request import Request, urlopen


class BG:
    url: str = "https://bigcharts.marketwatch.com/quotes/multi.asp?refresh=on&view=Q&msymb=glw+msft+amd+spy+cort+angi&rand=9148"

    def request_current(self):
        req = Request(self.url, headers={"User-Agent": "Mozilla/5.0"})
        page = urlopen(req).read()
        print(page)
