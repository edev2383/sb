from stockbox.common.position import PositionController


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
    Backtest = None

    # all values are of type RuleSet
    Patterns: list = []

    # backtest or activescan
    mode: str = "backtest"

    def __init__(self, Patterns, Ticker=None, **kwargs):

        self.Patterns = Patterns

        # Ticker set in init only for testing purposes, will remove
        if Ticker:
            self.Ticker = Ticker
        print("initing setup = = =======================================")
        self.position_controller = PositionController(kwargs)

    def set_backtest(self, Backtest):
        self.Backtest = Backtest
        self.position_controller.set_backtest(Backtest)
        self.position_controller.set_riskprofile(40.15)

    def get_patterns_to_process(self):
        """Filter self.Patterns based on Ticker.state value

        Returns:
            list: RuleSets
        """
        # cast the filter to list type
        return list(
            filter(
                lambda x: x.get_tickerstate() == self.Ticker.state,
                self.Patterns,
            )
        )

    def set_ticker(self, Ticker):
        """Set active Ticker object, from the Backtest class and init
        all of the patterns

        Args:
            Ticker (Ticker):
        """
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
            # We dont think this is necessary anymore, but will test
            # before we remove it
            pattern.inject_ticker_to_rules(self.Ticker)
        return Patterns

    # this is for testing, remove once sb_backtest is fully operational
    def process(self, window=None):
        """loop through valid RuleSet objects to process their rules
        if all rules are true call RuleSet.run_actions()

        Args:
            window (dataframe, optional): passed dataframe to process
            if None, RuleSet will process the provided ticker
        """
        exit()

        self.set_riskprofile()
        patterns = self.get_patterns_to_process()
        for ruleset in patterns:
            value = ruleset.process(window)
            if value:
                print("state: ", ruleset.tickerstate)
                print("name: ", ruleset.name)
                print("----------------------------")
                print("date: ", window.iloc[0])
                ruleset.run_actions(window.iloc[0])

    def alterprop(self, prop, value):
        if prop == "tickerstate":
            self.set_tickerstate(value)
        else:
            setattr(self, prop, value)

    def take_action(self, Action, window):
        Action.set_setup(self)
        self.Backtest.take_action(Action, window)

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
