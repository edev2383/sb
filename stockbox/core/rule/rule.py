import pandas as pd
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

    """

    def __init__(self, statement, df=0):
        self.statement = statement
        self.rule = RuleParser(statement).process()
        self.df = df
        print(f"rule: {self.rule}")
        print(f"test: ", self.rule["focus"]["key"])

    def process(self):
        """[summary]

        Returns:
            boolean: Calc takes in values and operator and befores the
                     operation, returning a boolean
        """
        focus = self.getfocus()
        comp = self.getcomp()
        return Calc(focus, self.rule["operator"], comp).calc()

    def getfocus(self):
        """

        Returns:
            float: From the parsed dict["focus"] value
        """
        return self.getvalue("focus")

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
            extension = self.getextension()
            return self.calculate_extension(spotvalue, extension)

    def getvalue(self, rulekey: str):
        """Generic getvalue, to pull values from the RuleParse dict

        Args:
            rulekey (str): "comparison" or "focus" keys

        Returns:
            [type]: [description]
        """
        # column in the dataframe
        col = self.rule[rulekey]["key"]
        # days back from index (0-indexed)
        fi = self.rule[rulekey]["from_index"]
        return self.df.at[int(fi), col]

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
