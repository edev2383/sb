class Position:

    entry_price: float
    entry_date: str
    days_active: int = 0

    exit_price: float
    exit_date: str

    current_price: float
    profit_loss: float

    stop_loss: float
    sharecount: int
    trailing_stop: float
    target: float

    length_valid_prime: int

    __prime_date: str

    Controller = None

    def __init__(self, config):
        for (prop, value) in config.items():
            setattr(self, prop, value)

    def open(self, window):
        self.entry_price = window["Close"]
        self.entry_date = window["Date"]
        print("OPEN POSITION: -============================================== ")
        print(window)

    def update(self, window):
        self.days_active += 1
        if self.stoploss_hit(window):
            print("We hit a stoploss here")
            window["Close"] = self.stop_loss
            self.close(window)

        # need to run process in here to determine if we've lapse on any
        # provided values, stops, targets etc. This all happens here

    def close(self, window):
        self.days_active += 1
        self.exit_price = window["Close"]
        self.exit_date = window["Date"]
        self.profit_loss = self.update_pnl(window)
        self.Controller.close()

    def update_pnl(self, window):
        return self.sharecount * (window["Close"] - self.entry_price)

    def pnl(self):
        return {
            "pos_id": str(id(self))[-6:],
            "bank_start": self.bank_start,
            "bank_end": round(self.bank_start + self.profit_loss, 2),
            "total_shares": self.sharecount,
            "price_enter": self.entry_price,
            "date_enter": self.entry_date,
            "price_exit": self.exit_price,
            "date_exit": self.exit_date,
            "days_held": self.days_active,
            "total_pnl": round(self.profit_loss, 2),
            "date_prime": self.__prime_date,
        }

    def stoploss_hit(self, window):
        return window["Low"] < self.stop_loss

    @property
    def prime_date(self):
        return self.__prime_date

    @prime_date.setter
    def prime_date(self, date):
        self.__prime_date = date