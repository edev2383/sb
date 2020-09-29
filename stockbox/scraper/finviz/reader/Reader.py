from lxml import html
from urllib.request import Request, urlopen


class Reader:

    # url for requesting screener select options, ft=4 is all options
    # url: str = "https://finviz.com/screener.ashx?v=111&ft=4"

    """Url for requesting equities w/ filters """
    url_base: str = "https://finviz.com/screener.ashx?v=111&f="

    """Query string of filters """
    filter_string: str

    """Page iteration, references first record to display """
    page_string: str = "&r="

    """Page handler props """
    page_count: int = 0
    records_per_page: int = 20
    total_pages: int = 1

    """Scraping props. tree holds the xml page, path gets the values """
    tree: object
    scrape_xpath: str = '//a[@class="screener-link-primary"]/text()'

    """Result container, returned by run() method """
    equities: list = []

    def __init__(self, filter_string: str):
        self.filter_string = filter_string

    def build_query_string(self):
        """Builds the query string to append to the url
        # concats the filter_string to the page suffix coefficient
        """
        page_coefficient = 1 + (self.page_count * self.records_per_page)
        return self.filter_string + self.page_string + str(page_coefficient)

    def build_url(self):
        self.url = self.url_base + self.build_query_string()

    def get_page_count(self):
        raw_pgcnt = self.tree.xpath('//td[@class="count-text"]/text()')[0]
        page_count = int(raw_pgcnt.split(" ")[0]) / self.records_per_page
        self.total_pages = int(page_count)

    def iterate_page(self, count: int):
        self.page_count = self.page_count + count

    def request_equities(self):
        req = Request(self.url, headers={"User-Agent": "Mozilla/5.0"})
        page = urlopen(req).read()
        self.tree = html.fromstring(page)

    def scrape_equities(self):
        self.equities.extend(self.tree.xpath(self.scrape_xpath))

    """Return list of equities corresponding to the requested filters

    Iterates through the pages, building the url and making new requests
    for each page. Then scrapes the equity values into self.equities
    list which is returned
    """

    def run(self):
        while self.page_count <= self.total_pages:
            self.build_url()
            self.request_equities()
            self.get_page_count()
            self.scrape_equities()
            self.iterate_page(1)
        return self.equities
