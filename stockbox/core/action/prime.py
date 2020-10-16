from .action import Action


class Prime(Action):

    name: str

    def process(self):
        self.set_tickerstate("primed")
        print("were buying here...", self.name, self.window)
