from ..Filter import Filter


class CurrentVolume(Filter):
    prefix: str = "sh_curvol"
    values: dict = {
        "u50": "Under 50K",
        "u100": "Under 100K",
        "u500": "Under 500K",
        "u750": "Under 750K",
        "u1000": "Under 1M",
        "o0": "Over 0",
        "o50": "Over 50K",
        "o100": "Over 100K",
        "o200": "Over 200K",
        "o300": "Over 300K",
        "o400": "Over 400K",
        "o500": "Over 500K",
        "o750": "Over 750K",
        "o1000": "Over 1M",
        "o2000": "Over 2M",
        "o5000": "Over 5M",
        "o10000": "Over 10M",
        "o20000": "Over 20M",
    }
