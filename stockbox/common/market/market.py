import datetime


class Market:

    open_hour: int = 9
    close_hour: int = 16
    timezone_offset: int = 4
    cl_buffer: int = 1

    @staticmethod
    def is_open():
        if not Market.is_trading_day():
            return False
        if Market.is_after_close():
            return False
        return datetime.datetime.now().hour > Market.open_hour

    @staticmethod
    def is_trading_day():
        dow = datetime.datetime.today().weekday()
        return dow >= 0 and dow <= 4

    @staticmethod
    def is_after_close():
        now = datetime.datetime.now().hour
        return (
            now
            >= Market.close_hour + Market.timezone_offset + Market.cl_buffer
        )
