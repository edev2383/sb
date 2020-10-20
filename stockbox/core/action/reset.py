from .action import Action


class Reset(Action):
    def process(self):
        print("RESET CALLED@")
        self.Setup.reset()
