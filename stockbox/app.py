from stockbox.core.rule import Rule, RuleSet
from stockbox.common.indicator import IndicatorFactory
from stockbox.core.ticker import Ticker
from stockbox.core.setup import Setup
from stockbox.common.scraper import Scraper
import re

# from stockbox.ticker import Ticker


def run():

    Scraper().current()
    # ticker = Ticker("GLW")
    # ticker.add_indicator("RSI(14)")
    # print(ticker.history().head())
    # # ticker = []

    # # y = IndicatorFactory.create("SMA(18)", x)

    # # print(y)
    # # print("start rule doing")

    # pattern = RuleSet("standard", "slosto_pattern")
    # a = Rule("[RSI(14)]<[40]")
    # b = Rule("[Close] < [Open]")
    # c = Rule("[High] < [SMA(10) * 0.99]")
    # pattern.add(a)
    # pattern.add(b)
    # pattern.add(c)

    # confirmation = RuleSet("standard", "slosto_confirmation")
    # d = Rule("[SloSto(14)] > [20]")
    # e = Rule("[Close] > [EMA(4)]")
    # confirmation.add(d)
    # confirmation.add(e)

    # patternexit = RuleSet("held", "slosto_exit")
    # f = Rule("[Close] < [yesterday Close]")
    # g = Rule("[Low] x [SMA(10)]", ticker).process()
    # print("g value: ", g)
    # print(ticker.history().head())

    # g = Rule("[yesterday's Close] < [yesterday Close]", ticker)
    # g = Rule("[two day ago RIS(14)] < [yesterday Close]", ticker)
    # g.process()
    # patternexit.add(f)
    # patternexit.add(g)

    # setup = Setup([pattern, confirmation, patternexit])
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
