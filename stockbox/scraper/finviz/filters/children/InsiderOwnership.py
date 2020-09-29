from ..Filter import Filter


class InsiderOwn(Filter):
    prefix: str = "sh_insiderown"
    values: dict = {
        "low": "Low (<5%)",
        "high": "High (>30%)",
        "veryhigh": "Very High (>50%)",
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
