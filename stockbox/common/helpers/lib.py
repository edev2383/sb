import numpy as np


def rsi(values):
    delta = values.diff()
    delta = delta[1:]
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    up = up.mean()
    down = down.mean()
    return 100 - (100 / (1 + abs(up / down)))


def column_index(df, query_cols):
    cols = df.columns.values
    sidx = np.argsort(cols)
    return sidx[np.searchsorted(cols, query_cols, sorter=sidx)]
