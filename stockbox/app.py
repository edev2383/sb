from stockbox.core.rule import Rule, RuleSet
from stockbox.common.indicator import IndicatorFactory
from stockbox.core.ticker import Ticker

# from stockbox.ticker import Ticker


def run():

    x = Ticker("Goog")

    y = IndicatorFactory.create("SMA(18)", x)

    print(y)
    # print("start rule doing")
    # a = Rule("[RSI(14)]<[40]", x)
    # b = Rule("[Close] < [Open]", x)
    # c = Rule("[High] < [SMA(10) * 0.99]", x)

    # rs = RuleSet("Testing")
    # rs.add(a)
    # rs.add(b)
    # rs.add(c)

    # rs.process()
    # x = Rule("[Close] > [SMA(20)]", x)

    # x = RuleParser("Close > 45")
    # x = RuleParser("Industry is plutonium")
    # x = RuleParser("SMA(45) == SMA(15)")
    # x = RuleParser("[Open] >= [Close(65)]")
    # x = RuleParser("[Open(78)]< [Close(1) * 1.03]")
    # x = RuleParser("[Open(3)]<[Close(5) * 1.25]")
