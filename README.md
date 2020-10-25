# Stockbox
_Stockbox is an equity testing suite that scrapes yahoo finance for ticker data. Returns a dataframe and calculates indicators. Backtesting will allow for 5-10 yrs of equity pattern recognition and allow the user to test complex stock position setups._

_Docs are incomplete_

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
RuleSets are a collection of rules and actions that are called based on the Ticker.state value. Sample RuleSet below w/ no docs:

```python
from stockbox.core.rule import Rule, RuleSet
from stockbox.core.setup import Setup

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
Setup takes a list of RuleSets as the only required argument. There are additional arguments that can be changed, but are set with default values when a Setup class initializes.


## Backtest
The Backtest class iterates through the dataframe, ever-expanding the dataframe with each iteration, checking each new index for the various _RuleSets_ via the _Setup_ class. If a true scenerio triggers, Setup triggers the RuleSet to take the predefined action. A PositionController class within the Setup handles the Position logic, while the Position class handles internal math and stoploss checks. 

The output below is from an equity backtest, using the above defined "SimpleSetup" over a 5yr period

```python

def run():

    bt = Backtest(Ticker("XXXX", "5y"), SimpleSetup)
    bt.process()

#	    bank_end  bank_start date_enter  date_exit date_prime  days_held  pos_id  price_enter  price_exit  stop_loss  total_pnl  total_shares
#	 0    9850.06    10000.00 2016-01-12 2016-01-14 2016-01-11        2.0  574656     2.390000    2.210000        0.0    -149.94         833.0
#	 1    9653.16     9850.06 2016-01-29 2016-02-02 2016-01-21        2.0  844736     2.200000    1.980000        1.0    -196.90         895.0
#	 2    9625.60     9653.16 2016-03-17 2016-04-05 2016-03-14       12.0  595616     2.800000    2.760000        0.0     -27.56         689.0
#	 3    9529.42     9625.60 2016-04-18 2016-04-19 2016-04-06        1.0  136864     2.760000    2.620000        0.0     -96.18         687.0
#	 4    9339.02     9529.42 2016-04-22 2016-04-25 2016-04-20        2.0  783952     3.990000    3.590000        1.0    -190.40         476.0
#	 . . .
#	 68  11578.88    11580.20 2020-06-30 2020-07-01 2020-06-12        1.0  575568    52.610001   52.580002        0.0      -1.32          44.0
#	 69  11825.72    11578.88 2020-07-24 2020-08-11 2020-07-22       12.0  576672    69.400002   76.879997        0.0     246.84          33.0
#	 70  11819.28    11825.72 2020-08-20 2020-09-03 2020-08-12       10.0  090608    82.769997   82.540001        0.0      -6.44          28.0
#	 71  11753.45    11819.28 2020-09-15 2020-09-16 2020-09-09        1.0  135232    78.930000   76.660004        0.0     -65.83          29.0
#	 72  11904.65    11753.45 2020-09-25 2020-10-09 2020-09-21       10.0  574272    78.059998   83.099998        0.0     151.20          30.0
# 
#  Final Bank Total: 11904.65
```
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
