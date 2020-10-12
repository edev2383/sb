class RuleSet:
    """[summary]"""

    name: str
    rules: list = []
    Setup = None

    def __init__(self, name: str):
        self.name = name

    def add(self, rule):
        self.rules.append(rule)

    def process(self):
        print(" - RuleSet - process(): _____________________")
        for rule in self.rules:
            print(rule.statement, rule.process())

    def inject_ticker_to_rules(self, Ticker):
        for rule in self.rules:
            rule.set_ticker(Ticker)
