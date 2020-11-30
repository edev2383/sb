from .parser import RuleParser
from .calc import Calc


class Rule:
    """Takes in a df window range and a `statement` argument.

    These are simple statements, i.e.,
        - [Close] < [45]
        - [RSI(14)] > [40]
        - [SloSto(14)] < [20]
        - [SMA(14)] > [SMA(50)]

    Rule then performs a calculation based on the statement and returns
    a boolean based on the statement's truthiness

    # ! Note ---
    Ticker is optional because RuleSet.process() will add the ticker obj
    from Setup() when it runs. It's still in the init() for external
    testing, it may be removed as the application develops
    """

    # string rule statement to parse
    statement: str
    # dict of values breakdown
    rule: dict
    # active dataframe
    window = None

    def __init__(self, statement, Ticker=None):
        self.statement = statement
        self.rule = RuleParser(statement).process()
        if Ticker:
            self.Ticker = Ticker

    def process(self, window=None):
        """[summary]

        Returns:
            boolean: Calc takes in values and operator and performs the
                     operation, and in this case returning a boolean
        """
        if window is None:
            self.window = self.Ticker.history()
        else:
            self.window = window
        focus = self.getfocus()
        comp = self.getcomp()
        print(f"focus: {focus}")
        print(f"comp: {comp}")
        if not focus or not comp:
            return False
        return Calc(focus, self.rule["operator"], comp).calc()

    def getfocus(self):
        """

        Returns:
            float: From the parsed dict["focus"] value
        """
        if self.rule["operator"] == "x":
            return self.get_crossesover_focus()
        return self.getvalue("focus")

    def get_crossesover_focus(self):
        index_value = self.getvalue("focus")
        current_index = self.rule["focus"]["from_index"]
        self.rule["focus"]["from_index"] = current_index + 1
        previous_index_value = self.getvalue("focus")
        return {"prev": previous_index_value, "curr": index_value}

    def getcomp(self):
        """Calculate and return the comparison portion of the RuleParse
        return dictionary

        Returns:
            float: caluclated value
        """
        # if 'value' key exists, bypass and return that value
        if self.direct_value_exists():
            return self.rule["comparison"]["value"]
        else:
            # otherwise, perform the calculation
            spotvalue = self.getvalue("comparison")
            # break to False if value not found
            if not spotvalue:
                return False
            extension = self.getextension()
            return self.calculate_extension(spotvalue, extension)

    def getvalue(self, rulekey: str):
        """Generic getvalue, to pull values from the RuleParse dict

        Args:
            rulekey (str): "comparison" or "focus" keys

        Returns:
            mixed|float|int: value at given loc of the active window
        """
        # column exists in the dataframe
        col = self.validate_indicator_column(self.rule[rulekey]["key"])
        # days back from index (0-indexed)
        fi = self.rule[rulekey]["from_index"]
        print(f"col: {col}, fi: {fi}")
        # return False if the requested from_index is beyond the window
        if int(fi) not in self.window.index:
            return False
        return self.window.iloc[int(fi)].at[col]

    def validate_indicator_column(self, key):
        """check if the column name is present in the dataframe,
        otherwise, sideload it to the Ticker object

        Args:
            key (str): requested column name

        Returns:
            str: provided column name
        """
        if key not in self.window.columns:
            self.sideload_indicator(key)
        return key

    def sideload_indicator(self, key):
        """add indicator to the ticket object, and update the Rule df

        Args:
            key (str): df column name
        """
        self.Ticker.add_indicator(key)
        self.reassign_window()

    def reassign_window(self):
        """Update the window values to include the same portion of the
        overall Ticker.history() dataframe, with the added indicator
        """
        self.window = self.Ticker.history().tail(len(self.window))

    def getextension(self):
        """
        Returns:
            dict|None:
        """
        if self.extension_exists():
            return self.rule["comparison"]["extension"]
        return None

    def calculate_extension(self, value: float, extension: dict):
        """Return value if dict has no extension value, otherwise
        perform the calculation described in the extension

        Args:
            value (float):
            extension (dict):

        Returns:
            [type]: [description]
        """
        if not extension:
            return value
        return Calc(value, extension["operator"], extension["value"]).calc()

    def direct_value_exists(self):
        return "value" in self.rule["comparison"].keys()

    def extension_exists(self):
        return "extension" in self.rule["comparison"].keys()

    def set_ticker(self, Ticker):
        self.Ticker = Ticker
