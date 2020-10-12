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
    total_risk_percent: float = 0.02

    # percent or dollar amount for trailing stop
    trailing_stop: float = 0.05

    # percent gain or dollar amount for target exit
    target: float

    # boolean to trigger sale of half at target
    sell_half: bool = False

    def __init__(
        self,
        Ticker,
        Patterns,
        total_risk_percent: float = 0.02,
        trailing_stop: float = 0.05,
        target: float = None,
        sell_half: bool = False,
    ):
        self.Ticker = Ticker
        self.Patterns = Patterns
        self.total_risk_percent = total_risk_percent
        self.trailing_stop = trailing_stop
        self.target = target
        self.sell_half = sell_half
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


#
# bt = Backtest(Setup(Ticker, [... params ]))
# bt.run()
#
#
#
#
#
#
#
#
#
