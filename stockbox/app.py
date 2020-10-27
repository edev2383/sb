import yfinance as yf
import finplot as fplt

df = yf.download("SPY", start="2018-01-01", end="2020-04-29")
fplt.candlestick_ochl(df[["Open", "Close", "High", "Low"]])
fplt.plot(df.Close.rolling(50).mean())
fplt.plot(df.Close.rolling(200).mean())
fplt.show()

# import matplotlib
# import matplotlib.pyplot as plt
# from matplotlib import style
# from stockbox.core.ticker import Ticker


# # c44154c6c447190a64fd8060ee9818e02ff105d5
# def run():

#     matplotlib.use("pdf")
#     # print(matplotlib.rcsetup.all_backends)
#     # style.use("ggplot")

#     ticker = Ticker("GLW", "6m")
#     ticker.add_indicator("SMA(10)")
#     df = ticker.history()
#     df.plot()

#     ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
#     ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

#     ax1.plot(df.index, df["Adj Close"])
#     ax1.plot(df.index, df["SMA(10)"])

#     ax2.bar(df.index, df["Volume"])

#     plt.savefig("test.png")
#     plt.show(block=True)
