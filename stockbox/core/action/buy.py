from .action import Action


class Buy(Action):

    name: str

    def process(self):
        self.set_tickerstate("held")
        print("were buying here...", self.name)
