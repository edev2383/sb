import pandas as pd
from .parser import RuleParser
from .calc import Calc


class Rule:
    """Takes in a df window range and a `statement` argument.

    These are simple statements, i.e.,
        - Close < 45
        - RSI(14) > 40
        - SloSto(14) < 20
        - SMA(14) > SMA(50)

    Rule then performs a calculation based on the statement and returns
    a boolean based on the statement's truthiness

    """

    def __init__(self, statement, df=0):
        self.rule = RuleParser(statement).process()
        self.df = df
        print(f"rule: {self.rule}")
        print(f"test: ", self.rule["focus"]["key"])
        self.process()

    def process(self):
        focus = self.getfocus()
        comp = self.getcomp()
        return Calc(focus, self.rule["operator"], comp).calc()

    def getfocus(self):
        return self.getvalue("focus")

    def getcomp(self):
        if self.direct_value_exists():
            return self.rule["comparison"]["value"]
        else:
            spotvalue = self.getvalue("comparison")
            extension = self.getextension()
            return self.calculate_extension(spotvalue, extension)

    def getvalue(self, rulekey: str):
        key = self.rule[rulekey]["key"]
        fi = self.rule[rulekey]["from_index"]
        return self.df.at[int(fi), key]

    def getextension(self):
        return self.rule["comparison"]["extension"]

    def calculate_extension(self, value: float, extension: dict):
        if not extension:
            return value
        return Calc(value, extension["operator"], extension["value"]).calc()

    def direct_value_exists(self):
        return "value" in self.rule["comparison"].keys()


#
# How to process these?
#
#
#
#
#
#
#
#
#
#
