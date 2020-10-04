from stockbox.rule import Rule


def run():

    x = Rule("[Open(3)]<[Close(5) * 1.25]")
    x = Rule("[Open] >= [SMA(65)]")
    x = Rule("[Open(78)]< [Close(1) / 1.03]")

    # x = RuleParser("Close > 45")
    # x = RuleParser("Industry is plutonium")
    # x = RuleParser("SMA(45) == SMA(15)")
    # x = RuleParser("[Open] >= [Close(65)]")
    # x = RuleParser("[Open(78)]< [Close(1) * 1.03]")
    # x = RuleParser("[Open(3)]<[Close(5) * 1.25]")
