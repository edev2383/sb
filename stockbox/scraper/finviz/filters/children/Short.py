from ..Filter import Filter


class Short(Filter):
    prefix: str = "sh_short"
    values: dict = {
        "low": "Low (<5%)",
        "high": "High (>20%)",
        "u5": "Under 5%",
        "u10": "Under 10%",
        "u15": "Under 15%",
        "u20": "Under 20%",
        "u25": "Under 25%",
        "u30": "Under 30%",
        "o5": "Over 5%",
        "o10": "Over 10%",
        "o15": "Over 15%",
        "o20": "Over 20%",
        "o25": "Over 25%",
        "o30": "Over 30%",
    }
