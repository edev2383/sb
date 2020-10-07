from ..Filter import Filter


class ATR(Filter):
    prefix: str = "ta_averagetruerange"
    values: dict = {
        "o0.25": "Over 0.25",
        "o0.5": "Over 0.5",
        "o0.75": "Over 0.75",
        "o1": "Over 1",
        "o1.5": "Over 1.5",
        "o2": "Over 2",
        "o2.5": "Over 2.5",
        "o3": "Over 3",
        "o3.5": "Over 3.5",
        "o4": "Over 4",
        "o4.5": "Over 4.5",
        "o5": "Over 5",
        "u0.25": "Under 0.25",
        "u0.5": "Under 0.5",
        "u0.75": "Under 0.75",
        "u1": "Under 1",
        "u1.5": "Under 1.5",
        "u2": "Under 2",
        "u2.5": "Under 2.5",
        "u3": "Under 3",
        "u3.5": "Under 3.5",
        "u4": "Under 4",
        "u4.5": "Under 4.5",
        "u5": "Under 5",
    }
