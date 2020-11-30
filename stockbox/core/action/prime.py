from .action import Action


class Prime(Action):

    name: str

    def process(self):
        self.set_tickerstate("primed")
        print(self.window)
        self.Setup.set_primedate(self.window["Date"])
