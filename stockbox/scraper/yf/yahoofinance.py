from .request import Request


class YahooFinance:
    def history(self, params: dict):
        return Request().process("history", params)
