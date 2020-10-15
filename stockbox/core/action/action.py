class Action:

    name: str
    Setup = None

    def __init__(self, name):
        self.name = name

    def process(self):
        pass

    def set_setup(self, Setup):
        self.Setup = Setup

    def set_tickerstate(self, state):
        self.Setup.set_tickerstate(state)