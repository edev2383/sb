class StatementComponent:
    """Parent class for the Focus and Comparison classes

    returns a dict {key: , days_before_index: , lamda:}
    """

    component: str

    def __init__(self, string: str):
        self.component = string

    def process(self):
        pass
