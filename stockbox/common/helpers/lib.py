def rsi(values):
    delta = values.diff()
    delta = delta[1:]
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    up = up.mean()
    down = down.mean()
    return 100 - (100 / (1 + abs(up / down)))
