import re
from stockbox.common.helpers import text2int, format_candlekey


class ComplexRangeRe:

    re_simple_range = r"(.*)\(([0-9]+)\)"
    re_range_yesterday = r"^yesterday[\']?[s]? (.*)"
    re_range_days_ago = r"(.*?) day[s]? ago (.*)"

    candle_keys = ["close", "high", "low", "open", "volume"]

    def __init__(self, str: str):
        self.str = str

    def process(self):
        days = self.has_days_range()
        if days:
            return self.format_days(days)
        yesterday = self.has_yesterday()
        if yesterday:
            return self.format_yesterday(yesterday)
        simple = self.has_simple_range()
        if simple:
            return self.format_simple(simple)

    def has_days_range(self):
        return re.match(self.re_range_days_ago, self.str)

    def has_yesterday(self):
        return re.match(self.re_range_yesterday, self.str)

    def has_simple_range(self):
        return re.match(self.re_simple_range, self.str)

    def format_days(self, match):
        return {
            "key": match.group(2).strip(),
            "from_index": text2int(match.group(1).strip()),
        }

    def format_yesterday(self, match):
        key = match.group(1).strip()
        if self.is_candlekey(key):
            key = format_candlekey(key)
        return {"key": key, "from_index": 1}

    def format_simple(self, match):
        key = match.group(1).strip()
        if self.is_candlekey(key):
            return self.format_candlekey_range(match)
        return {"key": match.group().strip(), "from_index": 0}

    def format_candlekey_range(self, match):
        return {
            "key": format_candlekey(match.group(1).strip()),
            "from_index": match.group(2).strip(),
        }

    def is_candlekey(self, key):
        """Check that the found key exists in the candle_keys list

        Args:
            key (string): should only be self.component

        Returns:
            boolean:
        """
        return key.lower() in self.candle_keys
