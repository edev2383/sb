class Calc:
    """[summary]

    Returns:
        [type]: [description]
    """

    v1: float
    v2: float
    operator: str

    def __init__(self, value_one, operator, value_two):
        self.v1 = float(value_one)
        self.operator = operator
        self.v2 = float(value_two)

    def calc(self):
        return self.switch_op()

    def greater_than(self, v1, v2):
        return v1 > v2

    def greater_than_or_equal(self, v1, v2):
        return v1 >= v2

    def less_than(self, v1, v2):
        return v1 < v2

    def less_than_or_equal(self, v1, v2):
        return v1 <= v2

    def equal_to(self, v1, v2):
        return v1 == v2

    def not_equal_two(self, v1, v2):
        return v1 != v2

    def add(self, v1, v2):
        return v1 + v2

    def subtract(self, v1, v2):
        return v1 - v2

    def multiply(self, v1, v2):
        return v1 * v2

    def divide(self, v1, v2):
        return v1 / v2

    def switch_op(self):
        switch = {
            ">": self.greater_than,
            ">=": self.greater_than_or_equal,
            "<": self.less_than,
            "<=": self.less_than_or_equal,
            "==": self.equal_to,
            "!=": self.not_equal_two,
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
        }
        func = switch.get(self.operator)
        return func(self.v1, self.v2)
