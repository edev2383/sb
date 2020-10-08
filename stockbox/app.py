from stockbox.core.rule import Rule
from stockbox.core.ticker import Ticker

# from stockbox.ticker import Ticker


def run():

    x = Ticker("Goog").history()

    print(x)

    print("start rule doing")
    y = Rule("[RSI(14)]<[40]", x)
    print("y: ", y.process())
    # x = Rule("[Close] > [SMA(20)]", x)

    # x = RuleParser("Close > 45")
    # x = RuleParser("Industry is plutonium")
    # x = RuleParser("SMA(45) == SMA(15)")
    # x = RuleParser("[Open] >= [Close(65)]")
    # x = RuleParser("[Open(78)]< [Close(1) * 1.03]")
    # x = RuleParser("[Open(3)]<[Close(5) * 1.25]")
