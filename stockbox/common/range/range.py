import datetime


class Range:
    """
    Class returns a start and end date when given a key string

    Attributes
    ----------
    allowed: list
        list of allowed keys, invalid passed keys exit script
    key: str
        string passed to determine length of history
    eodHour: int
        end of day hour value to determine timestamp, 18 = 6pm
    timezone_offset: int
        current timezone is EST, -4:00 UTC

    Methods
    -------
    generate_range()
        returns the start and end timestamps by the given key
    validate_range_key(key: str)
        exits script with warning if key is not allowed
    default_end()
        returns current day 6pm EST in seconds
    one_week() [...] ten_year()
        uses the end date and subtracts the time (in stock market
        trading days) to get the {start, end} dictionary return value
    """

    allowed: list = ["1w", "1m", "3m", "6m", "1y", "2y", "5y", "10y"]

    key: str
    eodHour: int = 18
    timezone_offset: int = 4

    def __init__(self, key: str):
        print("key", key)
        """
        Args:
            key (str): range value, checked against allowed[]
        """
        self.validate_range_key(key)
        self.key = key.lower()

    def generate_range(self):
        """Performs a switch based on provided range key value

        Returns:
            dict: {start: int(timestamp), end: int(timestamp)}
        """
        switch = {
            "1w": self.one_week,
            "1m": self.one_month,
            "3m": self.three_month,
            "6m": self.six_month,
            "1y": self.one_year,
            "2y": self.two_year,
            "5y": self.five_year,
            "10y": self.ten_year,
        }
        print(f" - Range - generate range from provided key {self.key}")
        func = switch.get(self.key)
        return func()

    def validate_range_key(self, key: str):
        """Validate the provided key

        Args:
            key (str):
        """
        if key not in self.allowed:
            print(f"Error: key ({key}) not found in allowed keys.")
            print("Allowed keys: ")
            print("-----------------------------")
            for x in self.allowed:
                print(f" | ----- {x}")
            exit()

    def default_end(self):
        """Return the default end timestamp, current day 6pm EST

        Returns:
            int:
        """
        end = datetime.datetime.combine(
            datetime.date.today(),
            datetime.time(self.timezone_offset + self.eodHour, 0),
        )
        return int(datetime.datetime.timestamp(end))

    """
    The following methods are the calculations for each respective key
    value. 1wk returns one_week(), 1mo returns one_month(), etc
    """

    def one_week(self):
        end = self.default_end()
        return {
            "start": end - (3600 * 24 * 7) - (3600 * self.eodHour),
            "end": end,
        }

    def one_month(self):
        end = self.default_end()
        return {
            "start": end - (3600 * 24 * 30) - (3600 * self.eodHour),
            "end": end,
        }

    def three_month(self):
        end = self.default_end()
        return {
            "start": end - (3600 * 24 * 90) - (3600 * self.eodHour),
            "end": end,  # - (2 * 86400), # 2 day ajustment for testing
        }

    def six_month(self):
        end = self.default_end()
        return {
            "start": end - (3600 * 24 * 180) - (3600 * self.eodHour),
            "end": end,
        }

    # 1605304800
    def one_year(self):
        end = self.default_end()
        return {
            "start": end - (3600 * 24 * 365) - (3600 * self.eodHour),
            "end": end,
        }

    def two_year(self):
        end = self.default_end()
        return {
            "start": end - (3600 * 24 * 365 * 2) - (3600 * self.eodHour),
            "end": end,
        }

    def five_year(self):
        end = self.default_end()
        return {
            "start": end - (3600 * 24 * 365 * 5) - (3600 * self.eodHour),
            "end": end,
        }

    def ten_year(self):
        end = self.default_end()
        return {
            "start": end - (3600 * 24 * 365 * 10) - (3600 * self.eodHour),
            "end": end,
        }
