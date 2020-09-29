from .yf import YahooFinance
from stockbox.range import Range


class Scraper:
    def history(
        self,
        symbol: str,
        range: str,
        interval: str = "1d",
    ):
        r = Range(range).generate_range()
        print(f"r: {r}")
        return YahooFinance().history(
            {
                "symbol": symbol,
                "date_from": r["start"],
                "date_to": r["end"],
                "interval": interval,
            }
        )
