class Setup:
    """A set of rules for creating, maintaining, and closing a position
    name: str

    primer: RuleSet
    confirmation: RuleSet
    conf_failure: RuleSet
    abort: RuleSet
    sell: RuleSet

    is_primed: boolean

    """

    Ticker = None

    # all values are of type RuleSet
    Patterns: dict = {
        "primer": None,
        "confirmation": None,
        "exit": None,
        "emergency": None,
    }

    # backtest or activescan
    mode: str = "backtest"

    # the percent of total bankroll to risk on the position
    total_risk_percent: float

    # percent or dollar amount for trailing stop
    trailing_stop: float

    # percent gain or dollar amount for target exit
    target: float

    # boolean to trigger sale of half at target
    sell_half: bool = False

    # window of entry, i.e., entry signal is $40.50, if the stock gaps,
    # to $42.50, the entry confirmation is still true, but you may not
    # want to take the position that far from entry, default is 2%
    # 2% for $40.50 is $41.31
    percent_from_entry: float

    # interpret the `pfe` value as $ amount, rather than a percentage
    percent_from_entry_dollar: bool

    def __init__(self, Ticker, Patterns, **kwargs):

        prop_defaults = {
            "mode": "backtest",
            "total_risk_percent": 0.02,
            "trailing_stop": 0.05,
            "target": None,
            "sell_half": False,
            "percent_from_entry": 0.02,
            "percent_from_entry_dollar": False,
        }
        self.Ticker = Ticker
        self.Patterns = self.init_patterns(Patterns)

        for (prop, default) in prop_defaults.items():
            setattr(self, prop, kwargs.get(prop, default))
        print("setup init...")

    def switch_pattern(self):
        """switcher to get the right RuleSet to process

        Returns:
            [RuleSet]: returns an instance of the RuleSet class,
            determined by Ticker.state
        """
        switch = {
            "standard": self.Patterns["primer"],
            "primed": self.Patterns["confirmation"],
            "held": self.Patterns["exit"],
        }
        return switch.get(self.Ticker.state)

    def init_patterns(self, Patterns):
        """RuleSets in Patterns must pass Ticker off to the Rule classes
        for processing

        Args:
            Patterns (dict): dict of RuleSets

        Returns:
            dict: RuleSets
        """
        for ptt in Patterns.values():
            ptt.Setup = self
            ptt.inject_ticker_to_rules(self.Ticker)
        return Patterns

    # this is for testing, remove once sb_backtest is fully operational
    def process(self):

        for ptt in self.Patterns.values():
            ptt.process()
        print("ticker: ", self.Ticker.history().head())
        print("mode: ", self.mode)
        print("total_risk_percent: ", self.total_risk_percent)
        print("trailing_stop: ", self.trailing_stop)
        print("percent_from_entry: ", self.percent_from_entry)
        print("percent_from_entry_dollar: ", self.percent_from_entry_dollar)


#
# bt = Backtest(Setup(Ticker, [... params ]))
# bt.run()
# "mode": "backtest"
# "total_risk_percent": 0.02,
# "trailing_stop": 0.05,
# "target": None,
# "sell_half": False,
# "percent_from_entry": 0.02,
# "percent_from_entry_dollar": False,
#
#
#
#
#
#
#
#
