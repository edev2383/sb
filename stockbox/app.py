# from stockbox.rule import Rule
from stockbox import Market

# from stockbox.ticker import Ticker


def run():

    # t = Ticker("GLW", "1m")

    y = Market.is_after_close()
    print("is after close: ", y)

    y = Market.is_open()
    print("is open: ", y)

    y = Market.is_trading_day()
    print("is trading day ", y)

    # x = Rule("[Open(3)]<[Close(5) * 1.25]")
    # x = Rule("[Open] >= [SMA(65)]")
    # x = Rule("[Open(78)]< [Close(1) / 1.03]")

    # x = RuleParser("Close > 45")
    # x = RuleParser("Industry is plutonium")
    # x = RuleParser("SMA(45) == SMA(15)")
    # x = RuleParser("[Open] >= [Close(65)]")
    # x = RuleParser("[Open(78)]< [Close(1) * 1.03]")
    # x = RuleParser("[Open(3)]<[Close(5) * 1.25]")
