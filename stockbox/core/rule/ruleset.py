class RuleSet:
    """Class defines the comparison rules to return a boolean. Once
    processed, the class then can later the containing Setup class to
    alter the behavior of the Setup/position held
    """

    name: str  # may not be needed, may be helpful to identify, remove?
    # rules: list = []
    # actions: dict = {"alter": [], "action": []}
    Setup = None

    # defines which Ticker.state value to target
    tickerstate: str  # standard, primed, held, negative

    def __init__(self, tickerstate, name: str):
        self.tickerstate = tickerstate
        self.name = name
        self.rules = []
        self.actions = {"alter": [], "action": []}

    def add(self, rule):
        self.rules.append(rule)

    def process(self, window=None):
        for rule in self.rules:
            # print(f"rule statement: {rule.statement}")
            if not rule.process(window):
                return False
        return True

    def inject_ticker_to_rules(self, Ticker):
        for rule in self.rules:
            rule.set_ticker(Ticker)

    def set_setup(self, Setup):
        self.Setup = Setup

    def alter_setup_prop(self, prop, value):
        self.Setup.alterprop(prop, value)

    def alter_setup_action(self, Action, window):
        self.Setup.take_action(Action, window)

    def define_action(self, action: str, prop=None, value=None, Action=None):
        """define an action to activate when the RuleSet returns true
        `alter` takes priority over `action`, all are called in the same
        order they are defined

        Args:
            action (str): `alter`|`action`
            prop (string, optional): a settings prop in Setup class.
                                     Defaults to None.
            value (float|int|bool, optional):  Defaults to None.
            Action (Action, optional): [description]. Defaults to None.
        """
        if action == "alter":
            if prop is None or value is None:
                print("RuleSet error: Missing `prop` or `value` attributes")
                exit()
            self.actions["alter"].append({"prop": prop, "value": value})
        elif action == "action":
            if Action is None:
                print("RuleSet error: Missing `Action` attribute")
                exit()
            self.actions["action"].append(Action)

    def run_actions(self, window):
        if self.actions["alter"]:
            self.run_setup_alters()
        if self.actions["action"]:
            self.run_setup_actions(window)

    def run_setup_alters(self):
        for alter in self.actions["alter"]:
            self.alter_setup_prop(alter["prop"], alter["value"])

    def run_setup_actions(self, window):
        for action in self.actions["action"]:
            self.alter_setup_action(action, window)

    def get_tickerstate(self):
        return self.tickerstate
