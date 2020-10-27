class Url:

    __url: str = "https://bigcharts.marketwatch.com/quotes/multi.asp?refresh=on&view=Q&msymb="

    def __init__(self, symbols: list):
        self.symbols = symbols

    def url(self):
        str = "+"
        return f"{self.__url}{str.join(self.symbols)}"
