import datetime


class Market:

    close_hour: int = 16
    timezone_offset: int = 4
    cl_buffer: int = 1

    def is_open(self):
        #
        x = 1

    def is_closed(self):
        #
        x = 1

    def is_trading_day(self):
        #
        dow = datetime.datetime.today().weekday()
        print("current dow: ", dow)
        return dow >= 0 and dow <= 4

    def is_after_close(self):
        now = datetime.datetime.now().hour
        return now >= self.close_hour + self.timezone_offset + self.cl_buffer
