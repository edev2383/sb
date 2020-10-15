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
    Patterns: list = []

    # backtest or activescan
    mode: str = "backtest"

    # the percent of total bankroll to risk on the position
    total_risk_percent: float

    # bool to trigger use of trailing_stop
    use_trailing_stop: bool

    # percent or dollar amount for trailing stop
    trailing_stop: float

    # percent gain or dollar amount for target exit
    target: float

    # boolean to trigger sale of half at target
    sell_half: bool = False
    sell_half_target: float = None

    # window of entry, i.e., entry signal is $40.50, if the stock gaps,
    # to $42.50, the entry confirmation is still true, but you may not
    # want to take the position that far from entry, default is 2%
    # 2% for $40.50 is $41.31
    entry_percent_from_conf: float

    # same as above, but a fixed dollar amount, if both are set, Setup
    # will chose the largest entry value, i.e. same example above, with
    # dollar value being $1.00. $41.50 is greater than $41.31, so Setup
    # will treat the higher value as the upper-entry bound
    entry_dollar_from_conf: float

    # stop loss values. In contrast to `entry` above, the stop_loss prop
    # will default to the smallest bound
    stop_loss_percent: float
    stop_loss_dollar: float

    def __init__(self, Patterns, Ticker=None, **kwargs):
        prop_defaults = {
            "mode": "backtest",
            "total_risk_percent": 0.02,
            "use_trailing_stop": False,
            "trailing_stop": None,
            "target": None,
            "sell_half": False,
            "sell_half_target": None,
            "entry_percent_from_conf": 0.02,
            "entry_dollar_from_conf": None,
            "stop_loss_percent": 0.02,
            "stop_loss_dollar": None,
        }

        self.Patterns = Patterns
        # ! Ticker set in init only for testing purposes, will remove
        if Ticker:
            self.Ticker = Ticker
        for (prop, default) in prop_defaults.items():
            setattr(self, prop, kwargs.get(prop, default))
        print("- - - - - - - - - - - - [ setup init... ] - - - - - -")

    def get_patterns_to_process(self):
        print("get_patterns_to_process called")
        return list(
            filter(
                lambda x: x.get_tickerstate() == self.Ticker.state,
                self.Patterns,
            )
        )

    def set_ticker(self, Ticker):
        self.Ticker = Ticker
        self.Patterns = self.init_patterns(self.Patterns)

    def init_patterns(self, Patterns):
        """RuleSets in Patterns must pass Ticker off to the Rule classes
        for processing

        Args:
            Patterns (dict): dict of RuleSets

        Returns:
            dict: RuleSets
        """
        for pattern in Patterns:
            pattern.set_setup(self)
            pattern.inject_ticker_to_rules(self.Ticker)
        return Patterns

    # this is for testing, remove once sb_backtest is fully operational
    def process(self, window=None):
        print("Setup process()")
        patterns = self.get_patterns_to_process()
        for ruleset in patterns:
            value = ruleset.process(window)
            if value:
                print("state: ", ruleset.tickerstate)
                print("name: ", ruleset.name)
                print("----------------------------")
                print("date: ", window.iloc[0]["Date"])
                ruleset.run_actions()

    def alterprop(self, prop, value):
        if prop == "tickerstate":
            self.set_tickerstate(value)
        else:
            setattr(self, prop, value)

    def take_action(self, Action):
        Action.set_setup(self)
        Action.process()  # ? need to expand action

    def set_tickerstate(self, state):
        self.Ticker.state = state


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
