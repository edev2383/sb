from stockbox.common.position import PositionController
from stockbox.common.log import Log


class Setup:
    """A set of rules for creating, maintaining, and closing a position"""

    Ticker = None
    Backtest = None

    # all values are of type RuleSet
    Patterns: list = []

    # backtest or activescan
    mode: str = "backtest"

    prime_date = None

    __name: str = "No name given"

    def __init__(self, Patterns, Ticker=None, **kwargs):

        self.Patterns = Patterns

        # Ticker set in init only for testing purposes, will remove
        if Ticker:
            self.Ticker = Ticker
        self.position_controller = self.create_position_controller(
            PositionController(kwargs)
        )

    def set_backtest(self, Backtest):
        self.Backtest = Backtest
        self.position_controller.set_backtest(Backtest)

    def create_position_controller(self, PositionController):
        PositionController.Setup = self
        return PositionController

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

    def backtest(self, window=None):
        """loop through valid RuleSet objects to process their rules
        if all rules are true call RuleSet.run_actions()

        Args:
            window (dataframe, optional): passed dataframe to process
            if None, RuleSet will process the provided ticker
        """
        for ruleset in self.get_patterns_to_process():
            value = ruleset.process(window)
            if value:
                # print(" ")
                # print("state: ", ruleset.tickerstate)
                # print("name: ", ruleset.name)
                # # print("---[ WINDOW ]---------------")
                # print(window.at[0, "Date"])
                # print("----------------------------")
                # print(" ")
                # dt = window.at[0, "Date"]
                ruleset.run_actions(window.iloc[0])
            else:
                print("name: ", ruleset.name)
                # print("---[ WINDOW ]---------------")
                print(window)
                # print("----------------------------")
                # print(" ")
                self.run_on_ruleset_failure(window.iloc[0])

    def alterprop(self, prop, value):
        if prop == "tickerstate":
            self.set_tickerstate(value)
        else:
            setattr(self, prop, value)

    def take_action(self, Action, window):
        Action.Setup = self
        Action.Backtest = self
        Action.window = window
        Action.process()

    def set_tickerstate(self, state):
        self.Ticker.state = state

    def open_position(self, window):
        self.position_controller.open(window)

    def close_position(self, window):
        self.position_controller.close_position(window)

    def run_on_ruleset_failure(self, window):
        self.position_controller.monitor_state(window)

    def reset(self):
        self.set_tickerstate("standard")
        self.position_controller.prime_date = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def set_primedate(self, date):
        self.position_controller.prime_date = date

    def scan_current(self, window=None):
        """loop through valid RuleSet objects to process their rules
        if all rules are true call RuleSet.run_actions()

        Args:
            window (dataframe, optional): passed dataframe to process
            if None, RuleSet will process the provided ticker
        """
        for ruleset in self.get_patterns_to_process():
            value = ruleset.process(window)
            if value:
                return True
            else:
                return False


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
