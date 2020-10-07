from .parser import RuleParser


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

    def process(self):
        x = 1


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