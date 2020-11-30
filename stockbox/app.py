from stockbox.core.ticker import Ticker
import robin_stocks as r
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from stockbox.common.scraper import Scraper


# # c44154c6c447190a64fd8060ee9818e02ff105d5
def run():

    # matplotlib.use("pdf")
    sym = [
        "GLW",
        "MSFT",
        "CORT",
        "APVO",
        "RETA",
        "TXMD",
        "ICPT",
        "REPH",
        "LJPC",
        "ZSAN",
        "MYGN",
        "AERI",
        "CNMD",
        "FLXN",
        "ASMB",
        "ABUS",
        "PCRX",
        "EYPT",
        "AVDL",
        "QTNT",
        "EPZM",
        "AVRO",
        "LIVN",
        "VIST",
        "ZIOP",
        "TTNP",
        "RGNX",
        "ESPR",
        "FPRX",
        "VRAY",
        "AFMD",
        "ITCI",
        "ANCN",
        "TMDX",
        "TPTX",
        "SWAV",
        "ADVM",
        "LXRX",
        "DTIL",
        "CBLI",
        "CWBR",
        "PHIO",
        "CRBP",
        "RUBY",
        "EYES",
        "PBYI",
        "SESN",
        "FENC",
        "ZGNX",
        "VCEL",
        "DCPH",
        "SPPI",
        "GOSS",
        "VSTM",
        "EVLO",
        "MRNA",
    ]

    t = Ticker("GLW")
    x = t.history()

    print(x.iloc[0].at["Adj Close"])
    # x = Scraper().current(sym)
    # print(x)
    # # x = Ticker("GLW", "1y")

    # # df = x.history()

    # # df2 = x.history("weekly")

    # # print(df.head())
    # # print(df2.head())
    # # logic = {
    # #     "Open": "first",
    # #     "High": "max",
    # #     "Low": "min",
    # #     "Close": "last",
    # #     "Volume": "sum",
    # # }

    # # df = df[::-1]

    # # df["Week_Number"] = df["Date"].dt.isocalendar().week
    # # df["Year"] = df["Date"].dt.year
    # # df2 = df.groupby(["Year", "Week_Number"]).agg(
    # #     {
    # #         "Date": "first",
    # #         "High": "max",
    # #         "Low": "min",
    # #         "Open": "first",
    # #         "Close": "last",
    # #         "Adj Close": "last",
    # #         "Volume": "sum",
    # #     }
    # # )
    # # print(df)
    # # print(df2)
    # # offset = pd.offsets.timedelta(days=-6)
    # # wk = df.resample("W", loffset=offset).apply(logic)
    # # print(wk)

    # # df.replace(0, np.nan)
    # # ax1 = plt.subplot2grid((8, 1), (0, 0), rowspan=5, colspan=1)
    # # ax2 = plt.subplot2grid((8, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
    # # ax3 = plt.subplot2grid((8, 1), (6, 0), rowspan=2, colspan=1, sharex=ax1)

    # # ax1.plot(df.index, df["SMA(10)"].replace(0, np.nan))
    # # ax1.plot(df.index, df["SMA(50)"].replace(0, np.nan))
    # # ax1.plot(df.index, df["Adj Close"])

    # # ax2.bar(df.index, df["Volume"])

    # # ax3.plot(df.index, df["Slope(10)"].replace(0, np.nan))
    # # ax3.plot(df.index, df["Slope(50)"].replace(0, np.nan))
    # # # ax3.plot(df.index, df["Slope(200)"])
    # # ax3.set_ylim(-0.35, 0.35)
    # # plt.savefig("./test.png")
