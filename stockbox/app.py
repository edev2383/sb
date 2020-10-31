from stockbox.core.ticker import Ticker


# # c44154c6c447190a64fd8060ee9818e02ff105d5
def run():

    x = Ticker("GLW", "1y")

    print(x.history())
