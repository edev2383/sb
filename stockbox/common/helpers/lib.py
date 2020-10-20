import numpy as np


def column_index(df, query_cols):
    cols = df.columns.values
    sidx = np.argsort(cols)
    return sidx[np.searchsorted(cols, query_cols, sorter=sidx)]


def text2int(value):
    if is_int(value):
        return int(value)
    units = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
    ]
    return units.index(value.lower())


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


def format_candlekey(str):
    return str.lower().capitalize()
