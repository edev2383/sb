from ..Filter import Filter


class InstitutionalOwn(Filter):
    prefix: str = "sh_instown"
    values: dict = {
        "low": "Low (<5%)",
        "high": "High (>90%)",
        "u90": "Under 90%",
        "u80": "Under 80%",
        "u70": "Under 70%",
        "u60": "Under 60%",
        "u50": "Under 50%",
        "u40": "Under 40%",
        "u30": "Under 30%",
        "u20": "Under 20%",
        "u10": "Under 10%",
        "o10": "Over 10%",
        "o20": "Over 20%",
        "o30": "Over 30%",
        "o40": "Over 40%",
        "o50": "Over 50%",
        "o60": "Over 60%",
        "o70": "Over 70%",
        "o80": "Over 80%",
        "o90": "Over 90%",
    }
