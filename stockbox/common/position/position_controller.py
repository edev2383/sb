import math
import datetime
from .position import Position


class PositionController:

    config: dict

    # the percent of total bankroll to risk on the position
    total_risk_percent: float
    total_risk_dollar: float

    # bool to trigger use of trailing_stop
    use_trailing_stop: bool

    # percent or dollar amount for trailing stop
    trailing_stop_percent: float
    trailing_stop_dollar: float

    # percent gain or dollar amount for target exit
    target: float

    # boolean to trigger sale of half at target
    sell_half: bool = False
    sell_half_target: float = None

    # window of entry, i.e., entry signal is $40.50, if the stock gaps,
    # to $42.50, the entry confirmation is still true, but you may not
    # want to take the position that far from entry, default is 2%
    # 2% for $40.50 is $41.31, so anything over $41.31 would be bounced
    entry_percent_from_conf: float

    # same as above, but a fixed dollar amount, if both are set, Setup
    # will chose the largest entry value, i.e. same example above, with
    # dollar value being $1.00. $41.50 is greater than $41.31, so Setup
    # will treat the higher value as the upper-entry bound
    entry_dollar_from_conf: float

    # stop loss values. In contrast to `entry` above, the stop_loss prop
    # will default to the smallest bound
    stop_loss_percent: float
    stop_loss_dollar: float

    # define the time period (in days) during which the pattern is valid
    # reverts to default None, once triggered
    valid_duration: int

    max_position_shares: int
    max_position_dollars: float

    sharecount: int = 0

    position_config: dict = {}

    active: bool = False
    Position = None
    Backtest = None

    length_valid_prime = None

    __prime_date = None

    def __init__(self, config):
        prop_defaults = {
            "total_risk_percent": 0.02,  # done
            "total_risk_dollar": None,  # done
            "use_trailing_stop": False,
            "trailing_stop_percent": None,
            "trailing_stop_dollar": None,
            "target": None,
            "sell_half": False,
            "sell_half_target": None,
            "entry_percent_from_conf": 0.02,
            "entry_dollar_from_conf": None,
            "stop_loss_percent": 0.10,  # done
            "stop_loss_dollar": None,  # done
            "valid_duration": None,
            "max_position_shares": None,  # done
            "max_position_dollars": None,  # done
            "length_valid_prime": None,
        }

        for (prop, default) in prop_defaults.items():
            setattr(self, prop, config.get(prop, default))
        # print("testing --- : ", self.stop_loss_dollar, id(self))

    def set_backtest(self, Backtest):
        self.Backtest = Backtest

    def set_riskprofile(self, share_price: float):
        self.position_config["stop_loss"] = self.set_stoploss(share_price)
        self.position_config["sharecount"] = self.set_sharecount(share_price)
        self.position_config["bank_start"] = self.Backtest.bank

    def set_stoploss(self, share_price: float):
        """Setting position stop loss, the threshold at which the posit-
        ion would be closed if the price action fell below

        if both stop_loss_* values are set, the higher is returned, rep-
        resenting a smaller risk window, i.e. closer to entry.

        Args:
            share_price (float):

        Returns:
            float:
        """
        loss = []
        if self.stop_loss_percent:
            loss.append(share_price * (1 - self.stop_loss_percent))
        if self.stop_loss_dollar:
            loss.append(share_price - self.stop_loss_dollar)
        return round(max(loss), 2)

    def set_sharecount(self, share_price: float):
        """Determine share count by factoring stoploss value and risk
        against the current stock price

        Args:
            share_price (float):

        Returns:
            int: number of shares
        """
        num_of_shares = [self.max_position_shares]
        num_of_shares.append(
            self.set_totalrisk()
            / (share_price - self.position_config["stop_loss"])
        )
        # print("num of shares: ", num_of_shares)
        # print("total risk :", self.set_totalrisk())
        # print("config: ", self.position_config)
        return self.validate_shares(
            math.floor(min([i for i in num_of_shares if i])), share_price
        )

    def modify_stoploss(self, sharecount):
        x = 1

    def validate_shares(self, share_count, share_price):
        cost = share_price * share_count
        if cost > self.Backtest.bank:
            modified_shares = math.floor(self.Backtest.bank / share_price)
            print("mod shares: ", modified_shares)
            self.modify_stoploss(modified_shares)
            return modified_shares
        else:
            return share_count

    def set_totalrisk(self):
        """Total dollar risk, by total_risk_* values and max_position_$

        Returns:
            float: total dollar risk
        """
        risk = [
            self.Backtest.bank * self.total_risk_percent,
            self.total_risk_dollar,
            self.max_position_dollars,
        ]
        return min([i for i in risk if i])

    def open(self, window):
        self.set_riskprofile(window["Close"])
        self.Position = self.create_position(
            Position(self.position_config), window
        )
        self.active = True

    def create_position(self, Position, window):
        Position.open(window)
        Position.Controller = self
        Position.prime_date = self.__prime_date
        return Position

    def close_position(self, window):
        self.Position.close(window)

    def is_active(self):
        return self.active

    def close(self):
        self.Backtest.update_pnl(self.Position.pnl())
        self.active = False
        self.Position = None
        self.Setup.reset()

    def monitor_state(self, window):
        if self.active:
            self.Position.update(window)
        else:
            self.monitor_inactive_state(window)

    def monitor_inactive_state(self, window):
        self.prime_valid(window)

    def prime_valid(self, window):
        if self.length_valid_prime is not None:
            if self.__prime_date is not None:
                delta_t = window["Date"] - self.__prime_date
                if delta_t.days > self.length_valid_prime:
                    # print(" ")
                    # print(" *********** RESET CALLED ************")
                    # print("TYPE: length_valid_prime")
                    # print(window)
                    # print(" _________ END RESET _________ ")
                    # print(" ")
                    self.Setup.reset()

    @property
    def prime_date(self):
        return self.__prime_date

    @prime_date.setter
    def prime_date(self, date):
        self.__prime_date = date
