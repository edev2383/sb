from .action import Action


class Sell(Action):

    name: str = "sell"

    def process(self):
        self.set_tickerstate("standard")
        print("were buying here...", self.name)