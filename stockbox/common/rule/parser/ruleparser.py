import re
from .components import BreakStatement, Focus, Comparison


class RuleParser:
    """
    Class to break down the Rule Statements

    All types of statements:
        - direct comparison: Close < 45
        - descriptive: industry is xyz
        - complex comparison: [Close] < [SMA(10) * 1.02]

    Questions:
        1.) Do we want to use the sq-bracket syntax for complex?
            - I think it works, since this is internal. If we release
            we can work on an easier to use syntax, but this is being
            built for ME to use.
        2.) For simplicity, does it make sense to enclose both sides of
            the statement in sq-brackets? [Open(4)] <[Close(65)]
            - The re pattern easily breaks this into 3 separate parts

    Process:
        1.) Break the statement into parts, then parse the parts further


    Return:
        Focus: {key: , days_from_index: }
        Operator: {key: }
        Comparison: {key: , days_from_index: , lamda: }
    """

    # this needs to go elsewhere, inserted into Focus or Comparison
    # on next phase
    keywords: list = [
        "ATH",
        "yesterday",
        "yesterday's",
        "yesterdays",
        "today",
        "todays",
        "today's",
        "yearly low",
        "yearly high",
    ]

    def __init__(self, statement: str):
        """Break the incoming statement into its component parts

        Args:
            statement (str):
        """
        self.focus, self.operator, self.comparison = BreakStatement(
            statement
        ).shatter()

    def process(self):
        """Return the Rule dictionary w/ the component parts further refined

        Returns:
            [dict]:
        """
        return {
            "focus": Focus(self.focus).process(),
            "operator": self.operator,
            "comparison": Comparison(self.comparison).process(),
        }
