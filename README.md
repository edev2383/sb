# Stockbox
_Stockbox is an equity testing suite that scrapes yahoo finance for ticker data. Returns a dataframe and calculates indicators. Backtesting will allow for 5-10 yrs of equity pattern recognition and allow the user to test complex stock position setups._

__The docs will be chaotic until the backtesting is complete__

# Table of Contents
- Ticker
- Indicators
- Rules
- RuleSets
- Setup
- Backtest
- Action (Buy/Sell)
- ActiveScan
  - Watchlist
  - Risk Models

## Ticker
Behaves similar to a simplified YahooFinance python package ([yF](https://pypi.org/project/yfinance/))
```python
from stockbox.core.ticker import Ticker

# default range is 1y, allowed ranges are 1w, 1m, 3m, 6m, 1y, 2y, 5y, 10y
stock = Ticker("GOOG", "1y")

print(stock.history())

# -- output
#       id  stock_id     High      Low     Open    Close  Adj_Close   Volume        Date   SMA(10)    SMA(20)    RSI(14)  
# 0    1271        16  1468.96  1436.00  1464.29  1460.29    1460.29  1632521  2020-10-07  1460.744  1483.8785  50.052272 
# 1    1266        16  1486.76  1448.59  1475.58  1453.44    1453.44  1198917  2020-10-06  1460.193  1488.5405  43.332805 
# 2    1261        16  1488.21  1464.27  1466.21  1486.02    1486.02  1051041  2020-10-05  1457.644  1491.4370  44.345740 
# 3     252        16  1483.20  1450.92  1462.03  1458.42    1458.42  1282400  2020-10-02  1455.029  1499.3395  36.226691 
# 4     251        16  1499.04  1479.21  1484.27  1490.09    1490.09  1779500  2020-10-01  1458.627  1511.7235  44.999486 
# ..    ...       ...      ...      ...      ...      ...        ...      ...         ...       ...        ...        ... 
# 248     7        16  1226.33  1211.76  1212.34  1217.14    1217.14   867500  2019-10-14     0.000     0.0000   0.000000 
# 249     6        16  1228.39  1213.74  1222.21  1215.45    1215.45  1272700  2019-10-11     0.000     0.0000   0.000000 
# 250     5        16  1215.00  1197.34  1198.58  1208.67    1208.67   846600  2019-10-10     0.000     0.0000   0.000000 
# 251     4        16  1208.35  1197.63  1199.35  1202.31    1202.31   867700  2019-10-09     0.000     0.0000   0.000000 
# 252     3        16  1206.08  1189.01  1197.59  1189.13    1189.13  1039300  2019-10-08     0.000     0.0000   0.000000 
```
## Indicators

## Rules
Rules are the building block of the backtesting. We use rules to define specific criteria and return a value (usually a boolean) depending on that criteria. Our criteria is taken as an easily readable string, which is then broken down into a mathematic equation and our values are returned, with the Rule ultimately ending in a True or False value.
```python
from stockbox.core.rule import Rule

# using the stock.history values from above
y = Rule("[Close] > [SMA(10)]", stock.history())

print("boolean: ", y.process())

# output
# boolean: False
#
# Close: 1460.29  SMA(10): 1460.744\
```
Other examples of valid statements:
> "[RSI(14)] > [40]"

> "[Close] < [SMA(10) * 1.02]"

### [update] Rules
Rules can now use more complex verbiage to search indexes days in the past:
```python
Rule("[yesterday's Close] < [two days ago High]", Ticker)

# alternatively, to get a "candle key" value, i.e., High, Low, Open, Close, Volume from previous days, 
# the user can use Close(3) as shorthand. This could be confusing since it's not in alignment with 
# how indicators are typed, with the secondary value being their ranges/window, so this may be removed
# or an undocumented shorthand 

Rule("[Close(3)] < [Close(2)]", Ticker)
```
It's in the testing phase, so it only goes back twenty days max, will expand this as needed


## RuleSet
RuleSets are a collection of rules and actions that are called based on the Ticker.state value. RuleSets are defined as followed:

```python

# SimpleSetup
pattern = RuleSet("standard", "test_setup_primer")
pattern.add(Rule("[Close] > [yesterday's Close]"))
pattern.add(Rule("[SMA(10)] > [SMA(50)]"))

pattern.define_action("action", Action=Prime())

confirmation = RuleSet("primed", "test_setup_conf")
confirmation.add(Rule("[Close] > [yesterday High]"))

confirmation.define_action("action", Action=Buy())

setup_exit = RuleSet("held", "test_setup_exit")
setup_exit.add(Rule("[Close] < [yesterday Low]"))
setup_exit.add(Rule("[yesterday Close] < [two days ago Low]"))

setup_exit.define_action("action", Action=Sell())

SimpleSetup = Setup([pattern, confirmation])
```


## Setup
> More docs to come

Rules (note for later):
RuleParser breaks a statement
> [Close(3)] < [SMA(5) * 1.02] 

down to the following dictionary:
```python
{ 
  "focus": { 
        "key": "Close",
        "from_index": 3,
        },
  "operator": "<",
  "comparison": {
        "key": "SMA(5)",
        "from_index": 0,
        "extension": {
                "operator": *,
                "value": 1.02,
                }
        }
}
```

Todos - 
- Reorg modules, define internal vs pos. external modules and reorg accordingly
```
[structure]

|--sb/
|--|--stockbox/
|--|--|--common/    <= modules that are only called internally
|--|--|--core/      <= modules that may be called externally
|--|--|--tests/    
|--|--|--app.py
```
- first pass on Rule syntax, will refine before v1.0.0
- comment the indicator math formulas on next commit
