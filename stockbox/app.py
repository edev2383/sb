from stockbox.core.rule import Rule, RuleSet
from stockbox.common.indicator import IndicatorFactory
from stockbox.core.ticker import Ticker
from stockbox.core.setup import Setup

# from stockbox.ticker import Ticker


def run():

    ticker = Ticker("Goog")

    # y = IndicatorFactory.create("SMA(18)", x)

    # print(y)
    # print("start rule doing")

    pattern = RuleSet("slosto_pattern")
    # a = Rule("[RSI(14)]<[40]")
    # b = Rule("[Close] < [Open]")
    # c = Rule("[High] < [SMA(10) * 0.99]")
    # pattern.add(a)
    # pattern.add(b)
    # pattern.add(c)

    # confirmation = RuleSet("slosto_confirmation")
    # d = Rule("[SloSto(14)] > [20]")
    # e = Rule("[Close] > [EMA(4)]")
    # confirmation.add(d)
    # confirmation.add(e)

    # patternexit = RuleSet("slosto_exit")
    # f = Rule("[Close] < [yesterday Close]")
    g = Rule("[RIS(14)] < [yesterday Close]", ticker)
    g.process()
    # patternexit.add(f)
    # patternexit.add(g)

    # setup = Setup(
    #     ticker,
    #   {"primer": pattern, "confirmation": confirmation, "exit": patternexit},
    # )
    # setup.process()

    # print(x.history().head())

    # rs.process()
    # x = Rule("[Close] > [SMA(20)]", x)

    # x = RuleParser("Close > 45")
    # x = RuleParser("Industry is plutonium")
    # x = RuleParser("SMA(45) == SMA(15)")
    # x = RuleParser("[Open] >= [Close(65)]")
    # x = RuleParser("[Open(78)]< [Close(1) * 1.03]")
    # x = RuleParser("[Open(3)]<[Close(5) * 1.25]")
