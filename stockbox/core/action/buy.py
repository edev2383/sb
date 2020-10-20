from .action import Action


class Buy(Action):

    name: str

    def process(self):
        self.set_tickerstate("held")
        self.Setup.open_position(self.window)
