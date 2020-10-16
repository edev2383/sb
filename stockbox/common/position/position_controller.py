class PositionController:

    config: dict

    # the percent of total bankroll to risk on the position
    total_risk_percent: float
    total_risk_dollar: float

    # bool to trigger use of trailing_stop
    use_trailing_stop: bool

    # percent or dollar amount for trailing stop
    trailing_stop: float

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

    Backtest = None

    def __init__(self, config):
        prop_defaults = {
            "mode": "backtest",
            "total_risk_percent": 0.02,
            "total_risk_dollar": None,
            "use_trailing_stop": False,
            "trailing_stop": None,
            "target": None,
            "sell_half": False,
            "sell_half_target": None,
            "entry_percent_from_conf": 0.02,
            "entry_dollar_from_conf": None,
            "stop_loss_percent": 0.10,
            "stop_loss_dollar": None,
            "valid_duration": None,
            "max_position_shares": None,
            "max_position_dollars": None,
        }

        for (prop, default) in prop_defaults.items():
            setattr(self, prop, config.get(prop, default))
        print("testing --- : ", self.stop_loss_dollar, id(self))

    def set_backtest(self, Backtest):
        self.Backtest = Backtest

    def set_riskprofile(self, share_price: float):
        self.stoploss = self.set_stoploss(share_price)
        self.sharecount = self.set_sharecount(share_price)
        print("self.stoploss: ", self.stoploss)

    def set_stoploss(self, share_price: float):
        """Setting position stop loss, the threshold at which the posit-
        ion would be closed if the price action fell below

        if both stop_loss_* values are set, the higher is returned, rep-
        resenting a smaller risk window.

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
        return max(loss)

    def set_sharecount(self, share_price: float):
        """Determine share count by factoring stoploss value and risk
        against the current stock price

        Args:
            share_price (float):

        Returns:
            int: number of shares
        """
        total_risk = self.set_totalrisk()
        self.sharecount = total_risk / (share_price - self.stoploss)
        print("sharecount: ", self.sharecount)

    def set_totalrisk(self):
        """Total dollar risk, by total_risk_* values. If both are set,
        take the lesser value

        Returns:
            float: total dollar risk
        """
        bank = self.Backtest.bank
        risk = []
        if self.total_risk_percent is not None:
            risk.append(bank * self.total_risk_percent)
        if self.total_risk_dollar is not None:
            risk.append(self.total_risk_dollar)
        print("risk: ", risk)
        return min(risk)
