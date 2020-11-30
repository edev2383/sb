import datetime
import time


class Market:

    open_hour: int = 14  # 2pm UTC NON-DST
    close_hour: int = 21  # 9pm UTC NON-DST
    is_dst: bool
    curr_hour: int
    curr_min: int

    def __init__(self):
        lt = time.localtime()
        self.is_dst = lt[-1]
        self.curr_hour = lt[3]
        self.curr_min = lt[4]
        self.dow = lt[6]

    def is_open(self):
        if self.is_trading_day() is False:
            return False
        if self.is_time() is False:
            return False
        return True

    def is_time(self):
        hr = self.curr_hour
        if self.is_dst:
            hr = hr - 1
        if hr < self.open_hour:
            return False
        if hr > self.close_hour:
            return False
        return True

    def is_trading_day(self):
        return self.dow >= 0 and self.dow <= 4
