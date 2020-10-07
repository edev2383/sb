from ..Filter import Filter


class AverageVolume(Filter):
    prefix: str = "sh_avgvol"
    values: dict = {
        "u50": "Under 50K",
        "u100": "Under 100K",
        "u500": "Under 500K",
        "u750": "Under 750K",
        "u1000": "Under 1M",
        "o50": "Over 50K",
        "o100": "Over 100K",
        "o200": "Over 200K",
        "o300": "Over 300K",
        "o400": "Over 400K",
        "o500": "Over 500K",
        "o750": "Over 750K",
        "o1000": "Over 1M",
        "o2000": "Over 2M",
        "100to500": "100K to 500K",
        "100to1000": "100K to 1M",
        "500to1000": "500K to 1M",
        "500to10000": "500K to 10M",
    }
