import re


class BreakStatement:
    """Handles the initial breaking of the statement, returning the
    `focus`, `operator`, and `comparison` to the RuleParser
    """

    re_bracket = r"(\[(.*)\])\s?(.+)\s?(\[(.*)\])"

    valid_operators: list = [
        ">",
        "==",
        "!=",
        "<",
        "<=",
        ">=",
        "is",
    ]

    def __init__(self, statement: str):
        self.statement = statement

    def shatter(self):
        """Performs a regex match `re_bracket` against the provided
        statement string. If the format is incorrect pop and error and
        an exit.

        TODO - add logging

        Returns:
            list: list of strings, the focus, operator, and comparison
                  strings to be sent back to the RuleParser class
        """
        found = re.match(self.re_bracket, self.statement, re.M | re.I)
        if found:
            focus = found.group(2).strip()
            operator = found.group(3).strip()
            comparison = found.group(5).strip()
            self.validate_operator(operator)
            return [
                focus,
                operator,
                comparison,
            ]
        print("Error: - Incorrect statement format...")
        print("Statement must be structured as follows: ")
        print("[Focus] Operator [Comparison]")
        print(" ")
        print("Example: [Close] < [SMA(5) * 1.02]")
        exit()

    def validate_operator(self, operator: str):
        """Pop an error and exit() if the provided operator is not in
        the valid_operators list

        Args:
            operator (str): [description]
        """
        if operator not in self.valid_operators:
            print("Error: Invalid operator detected...")
            print("Operator must match values listed in the following list:")
            print(self.valid_operators)
            exit()
