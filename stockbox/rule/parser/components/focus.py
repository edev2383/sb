import re
from .statement_component import StatementComponent


class Focus(StatementComponent):
    """Takes in the focus component from RuleParser class

    Args:
        StatementComponent

    Close(3)
    return {
        "key": "Close",
        "day_from_index: 3,
        "lamda": None
    }

    Close
    return {
        "key": "Close",
        "day_from_index: 3,
        "lamda": None
    }
    """

    candle_keys = ["close", "high", "low", "open", "volume"]

    re_simple = r"^[a-zA-Z]+$"
    re_range = r"(.*)\(([0-9]+)\)"

    def process(self):
        """regex check for range, return appropriately

        Returns:
            [type]: [description]
        """
        match = self.range_exists()
        if match:
            return self.hasrange(match)
        # validate the norange value, to ensure something like Close(f)
        # doesn't get passed
        self.validate_norange()
        return self.norange()

    def range_exists(self):
        return re.match(self.re_range, self.component)

    def norange(self):
        return {"key": self.component, "from_index": 0}

    def hasrange(self, match):
        """return the hasrange equivalent. Perform a candle key validat-
        ion. If the key exists in the candlekey list, we return with the
        range value, otherwise, we can assume it's an indicator value &
        the `range` is actually part of the focus key

        Args:
            match (re.match):

        Returns:
            dict:
        """
        if self.is_candlekey(self.component):
            return {
                "key": match.group(1).strip(),
                "from_index": match.group(2).strip(),
            }
        # assume it's an indicator and return it as no range
        return self.norange()

    def validate_norange(self):
        """regex to confirm the value is a string only"""
        if not re.search(self.re_simple, self.component):
            print(f"An error occured with a focus component: {self.component}")
            print("Ensure it's a `clean` simple expression, i.e. Close, or ")
            print("that it has a range of integer values only, i.e., Close(8)")
            exit()

    def is_candlekey(self, key):
        """Check that the found key exists in the candle_keys list

        Args:
            key (string): should only be self.component

        Returns:
            boolean:
        """
        return key in self.candle_keys
